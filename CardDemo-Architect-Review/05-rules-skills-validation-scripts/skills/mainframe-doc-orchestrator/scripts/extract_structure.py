"""Deterministic structural extraction from mainframe source (ground truth for coverage).

Usage (run from the repository root):
  python extract_structure.py <inventory.json> <work_dir> [--only cobol|copybook|jcl|csd|data]

Reads every inventoried COBOL program, copybook/DCLGEN, JCL job/PROC, CICS CSD,
DB2 DDL, IMS DBD/PSB and writes, under <work_dir>/structure/:

  programs/<MEMBER>.json   divisions, sections, paragraphs (line ranges), SELECTs,
                           FDs, data items, COPY statements, and per paragraph:
                           PERFORM/GO TO edges, decision points (IF/EVALUATE/WHEN,
                           AT END, INVALID KEY), calculations, file I/O, EXEC
                           CICS/SQL/DLI blocks, CALLs, literal MOVEs, terminations
  copybooks/<MEMBER>.json  data items (level, PIC, USAGE, OCCURS, REDEFINES, VALUE,
                           88-levels) or procedure paragraphs, nested COPY
  copybook-usage.json      every COPY / EXEC SQL INCLUDE edge, resolved
  jcl/<MEMBER>.json        job card, steps, EXEC PGM/PROC, PARM, COND, IF/THEN,
                           DDs, in-stream control data, application program
  csd.json                 CICS resources by type, with source lines
  data-definitions.json    DDL tables/indexes, DCLGEN tables, DBD segments, PSB PCBs
  summary.json             counts per artifact type

Facts are syntactic (Confirmed by the cited line). Decision-point "class" is a
keyword heuristic used only to measure business-rule coverage; it is not a fact.
Python 3.1+ standard library only.
"""
import hashlib
import json
import os
import re
import sys

SCHEMA = "structure/1"

STMT_VERBS = set((
    "ACCEPT ADD ALTER CALL CANCEL CLOSE COMPUTE CONTINUE DELETE DISPLAY DIVIDE ELSE "
    "EVALUATE EXEC EXIT GO GOBACK IF INITIALIZE INSPECT MERGE MOVE MULTIPLY NEXT OPEN "
    "PERFORM READ RELEASE RETURN REWRITE SEARCH SET SORT START STOP STRING SUBTRACT "
    "UNSTRING WHEN WRITE INVALID AT NOT THEN END-IF END-EVALUATE END-PERFORM END-READ "
    "END-EXEC END-COMPUTE END-STRING END-UNSTRING END-CALL END-WRITE END-REWRITE "
    "END-DELETE END-START END-SEARCH END-ADD END-SUBTRACT END-MULTIPLY END-DIVIDE "
    "END-RETURN ON OTHERWISE").split())
NON_PARAGRAPH_WORDS = STMT_VERBS | set(["DECLARATIVES", "END", "EJECT", "SKIP1", "SKIP2",
                                        "SKIP3", "COPY", "PROCEDURE"])
SYSTEM_COPYBOOKS = re.compile(r"^(DFH[A-Z0-9]*|SQLCA|SQLDA|CMQ[A-Z0-9]*|CSQ[A-Z0-9]*|"
                              r"DLIUIB|CEEIGZCT)$")
COPY_TYPES = ("cobol-copybook", "db2-dclgen", "bms-symbolic-map", "asm-copybook")

TECH_PATTERNS = [
    ("io-status", re.compile(r"STATUS|\bRESP\b|RESP-CD|RESP2|SQLCODE|SQLSTATE|EIBRESP|DIBSTAT|"
                             r"COMPCODE|COMP-CODE|REASON|MQCC|MQRC|APPL-AOK|APPL-EOF|APPL-RESULT|"
                             r"IO-STAT|END-OF-FILE|\bEOF\b|-EOF\b|FILE-STAT|PCB-STATUS|"
                             r"WS-RETURN-CODE|RETURN-CODE|NOTFND|NORMAL|DUPREC|DUPKEY|ENDFILE")),
    ("pseudo-conversation", re.compile(r"EIBCALEN|REENTER|FIRST-TIME|PGM-CONTEXT|"
                                       r"CDEMO-PGM-|FROM-PROGRAM|LENGTH OF")),
    ("screen-key", re.compile(r"EIBAID|DFHENTER|DFHPF|DFHCLEAR|DFHPA|CCARD-AID|\bAID\b|"
                              r"PFK|PF-KEY|PFKEY")),
    ("error-flag", re.compile(r"ERR-FLG|ERROR-FLAG|ERR-FLAG|INPUT-ERROR|INPUT-OK|ERRMSG|"
                              r"WS-ERROR|ERROR-FOUND|RETURN-MSG|WS-MESSAGE|MESSAGE-")),
]


# ----------------------------------------------------------------- helpers
def load_json(path):
    f = open(path, "r", encoding="utf-8")
    try:
        return json.load(f)
    finally:
        f.close()


def save_json(path, obj):
    d = os.path.dirname(path)
    if d and not os.path.isdir(d):
        os.makedirs(d)
    f = open(path, "w", encoding="utf-8", newline="\n")
    try:
        json.dump(obj, f, indent=1, sort_keys=True)
        f.write("\n")
    finally:
        f.close()


def read_lines(path):
    f = open(path, "rb")
    try:
        data = f.read()
    finally:
        f.close()
    text = data.decode("latin-1").replace("\r\n", "\n").replace("\r", "\n")
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    return lines, hashlib.sha256(data).hexdigest()


def src(path, a, b=None):
    if b is None or b == a:
        return "%s:%d" % (path, a)
    return "%s:%d-%d" % (path, a, b)


def strip_quotes_upper(text):
    """Upper-case text outside literals; literals kept verbatim."""
    out, q = [], None
    for ch in text:
        if q:
            out.append(ch)
            if ch == q:
                q = None
        elif ch in "'\"":
            q = ch
            out.append(ch)
        else:
            out.append(ch.upper())
    return "".join(out)


def first_word(text):
    m = re.match(r"\s*([A-Za-z0-9][A-Za-z0-9-]*)", text)
    return m.group(1).upper() if m else ""


def squash(text):
    return re.sub(r"\s+", " ", text).strip()


def literals(text):
    return [m.group(2) for m in re.finditer(r"(['\"])(.*?)\1", text)]


# ----------------------------------------------------------------- COBOL lines
def cobol_lines(raw):
    out = []
    for i, l in enumerate(raw):
        n = i + 1
        tab = "\t" in l
        e = l.expandtabs(8) if tab else l
        if len(e) < 7 or not e[6:].strip():
            out.append({"n": n, "kind": "blank", "code": "", "area_a": False})
            continue
        ind = e[6]
        code = e[7:] if tab else e[7:72]
        if ind in "*/":
            kind = "comment"
        elif ind in "dD":
            kind = "debug"
        elif ind == "-":
            kind = "cont"
        else:
            kind = "code"
        if kind in ("code", "cont") and not code.strip():
            kind = "blank"
        out.append({"n": n, "kind": kind, "code": code.rstrip(),
                    "area_a": kind == "code" and code[:4].strip() != ""})
    return out


def join_entries(lines, start_idx, stop_idx):
    """Group code lines into period-terminated entries: list of (first_n, last_n, text)."""
    entries, buf, first, last = [], [], None, None
    for k in range(start_idx, stop_idx):
        ln = lines[k]
        if ln["kind"] not in ("code", "cont"):
            continue
        if first is None:
            first = ln["n"]
        last = ln["n"]
        buf.append(ln["code"].strip())
        if ends_with_period(ln["code"]) or re.search(r"\bEND-EXEC\b", ln["code"].upper()):
            entries.append((first, last, " ".join(buf)))
            buf, first = [], None
    if buf:
        entries.append((first, last, " ".join(buf)))
    return entries


def ends_with_period(code):
    s = code.rstrip()
    if not s.endswith("."):
        return False
    q = None
    for ch in s:
        if q:
            if ch == q:
                q = None
        elif ch in "'\"":
            q = ch
    return q is None


# ----------------------------------------------------------------- data entries
USAGE_RE = re.compile(r"\b(COMP-1|COMP-2|COMP-3|COMP-4|COMP-5|COMPUTATIONAL-3|COMPUTATIONAL-5|"
                      r"COMPUTATIONAL|COMP|BINARY|PACKED-DECIMAL|DISPLAY|INDEX|POINTER|"
                      r"NATIONAL)\b")


def parse_data_entry(text):
    t = strip_quotes_upper(text).rstrip(".").strip()
    m = re.match(r"^(\d{1,2})(?:\s+([A-Z0-9][A-Z0-9-]*))?(.*)$", t)
    if not m:
        return None
    level = int(m.group(1))
    name = m.group(2) or "FILLER"
    rest = m.group(3) or ""
    if name in ("PIC", "PICTURE", "VALUE", "VALUES", "REDEFINES", "OCCURS", "USAGE", "COMP",
                "COMP-3", "BINARY"):
        rest = " " + name + rest
        name = "FILLER"
    item = {"level": level, "name": name}
    r = re.search(r"\bREDEFINES\s+([A-Z0-9-]+)", rest)
    if r:
        item["redefines"] = r.group(1)
    p = re.search(r"\bPIC(?:TURE)?\s+(?:IS\s+)?(\S+)", rest)
    if p:
        item["pic"] = p.group(1).rstrip(".")
    o = re.search(r"\bOCCURS\s+(\d+)(?:\s+TO\s+(\d+))?(?:\s+TIMES)?", rest)
    if o:
        item["occurs"] = int(o.group(2) or o.group(1))
        if o.group(2):
            item["occurs_min"] = int(o.group(1))
        d = re.search(r"\bDEPENDING\s+ON\s+([A-Z0-9-]+)", rest)
        if d:
            item["depending_on"] = d.group(1)
        ix = re.search(r"\bINDEXED\s+BY\s+([A-Z0-9-]+)", rest)
        if ix:
            item["indexed_by"] = ix.group(1)
    u = USAGE_RE.search(re.sub(r"\bPIC(?:TURE)?\s+(?:IS\s+)?\S+", " ", rest))
    if u:
        item["usage"] = u.group(1).replace("COMPUTATIONAL", "COMP")
    v = re.search(r"\bVALUES?\s+(?:ARE\s+|IS\s+)?(.*)$", rest)
    if v:
        item["value"] = squash(v.group(1))[:200]
    if re.search(r"\bSIGN\s+(IS\s+)?(LEADING|TRAILING)", rest):
        item["sign"] = re.search(r"(LEADING|TRAILING)(\s+SEPARATE)?", rest).group(0)
    return item


def pic_length(pic, usage):
    if not pic:
        return None
    p = pic.upper()
    count, digits = 0, 0
    for m in re.finditer(r"([AXZ9BSVP0/,.+\-*$CRDBE])(\((\d+)\))?", p):
        ch, n = m.group(1), int(m.group(3) or 1)
        if ch in ("S", "V", "P"):
            continue
        count += n
        if ch == "9":
            digits += n
    if "CR" in p or "DB" in p:
        count -= 1
    u = (usage or "DISPLAY").upper()
    if u in ("COMP-3", "PACKED-DECIMAL"):
        return digits // 2 + 1
    if u in ("COMP", "COMP-4", "COMP-5", "BINARY"):
        return 2 if digits <= 4 else (4 if digits <= 9 else 8)
    if u == "COMP-1":
        return 4
    if u == "COMP-2":
        return 8
    return count


def data_items(lines, path, lo, hi, section_of=None):
    items, fds, copies = [], [], []
    for first, last, text in join_entries(lines, lo, hi):
        u = strip_quotes_upper(text)
        if re.match(r"^\s*COPY\s", u):
            continue
        fm = re.match(r"^\s*(FD|SD)\s+([A-Z0-9-]+)(.*)$", u)
        if fm:
            fds.append({"type": fm.group(1), "file": fm.group(2), "clauses": squash(fm.group(3))[:200],
                        "source": src(path, first, last)})
            continue
        if re.match(r"^\s*EXEC\s+SQL", u):
            dm = re.search(r"\bDECLARE\s+([A-Z0-9_-]+)\s+CURSOR", u)
            if dm:
                items.append({"level": 0, "name": dm.group(1), "kind": "sql-cursor",
                              "sql": squash(text)[:600], "line": first,
                              "source": src(path, first, last)})
            continue
        it = parse_data_entry(text)
        if not it:
            continue
        it["line"] = first
        it["source"] = src(path, first, last)
        if section_of:
            it["section"] = section_of(first)
        if it.get("pic"):
            it["length"] = pic_length(it["pic"], it.get("usage"))
        items.append(it)
    # attach 88-levels to their parent
    out, parent = [], None
    for it in items:
        if it["level"] == 88:
            cond = {"name": it["name"], "value": it.get("value", ""), "line": it["line"]}
            if parent is not None:
                parent.setdefault("conditions", []).append(cond)
            else:
                out.append(it)
            continue
        if it["level"] != 0:
            parent = it
        out.append(it)
    return out, fds, copies


def copy_record(upper_text, name, path, first, last, commented, kind="COPY"):
    rec = {"name": name.strip("'\"").upper(), "kind": kind, "source": src(path, first, last),
           "line": first, "commented": commented}
    r = re.search(r"\bREPLACING\b(.*)$", upper_text)
    if r:
        rec["replacing"] = squash(r.group(1)).rstrip(".")
    lib = re.search(r"\b(?:OF|IN)\s+([A-Z0-9@#$-]+)", upper_text)
    if lib:
        rec["library"] = lib.group(1)
    return rec


def commented_copies(lines, path):
    out = []
    for ln in lines:
        if ln["kind"] != "comment":
            continue
        m = re.match(r"^\s*COPY\s+['\"]?([A-Z0-9@#$-]+)['\"]?\s*\.?\s*$", ln["code"].upper())
        if m:
            out.append(copy_record(ln["code"].upper(), m.group(1), path, ln["n"], ln["n"], True))
    return out


def line_copies(lines, path, proc_start=None):
    """COPY and EXEC SQL INCLUDE statements found line by line (they need not start an entry)."""
    out, k, n = [], 0, len(lines)
    while k < n:
        ln = lines[k]
        if ln["kind"] != "code":
            k += 1
            continue
        u = strip_quotes_upper(ln["code"])
        m = re.match(r"^\s*COPY\s+['\"]?([A-Z0-9@#$-]+)['\"]?", u)
        if m:
            parts, last, j = [u], ln["n"], k + 1
            while not ends_with_period(parts[-1]) and j < n and re.search(r"\bREPLACING\b", " ".join(parts)):
                if lines[j]["kind"] in ("code", "cont"):
                    parts.append(strip_quotes_upper(lines[j]["code"]))
                    last = lines[j]["n"]
                j += 1
            rec = copy_record(" ".join(parts), m.group(1), path, ln["n"], last, False)
            if proc_start is not None and ln["n"] > proc_start:
                rec["procedure_division"] = True
            out.append(rec)
        elif re.match(r"^\s*EXEC\s+SQL\b", u):
            parts, last, j = [u], ln["n"], k + 1
            while "END-EXEC" not in " ".join(parts) and j < n:
                if lines[j]["kind"] in ("code", "cont"):
                    parts.append(strip_quotes_upper(lines[j]["code"]))
                    last = lines[j]["n"]
                j += 1
            im = re.match(r"^\s*EXEC\s+SQL\s+INCLUDE\s+([A-Z0-9@#$-]+)", " ".join(parts))
            if im:
                rec = copy_record(" ".join(parts), im.group(1), path, ln["n"], last, False, "EXEC SQL INCLUDE")
                if proc_start is not None and ln["n"] > proc_start:
                    rec["procedure_division"] = True
                out.append(rec)
        k += 1
    return out


# ----------------------------------------------------------------- procedure
def classify_condition(text):
    u = text.upper()
    for name, rx in TECH_PATTERNS:
        if rx.search(u):
            return name
    return "business-candidate"


def gather(lines, k, hi, stop_on_verb=True):
    """Join continuation lines of a statement that starts at index k; return (text, last_n, next_k)."""
    parts = [lines[k]["code"].strip()]
    last = lines[k]["n"]
    j = k + 1
    if ends_with_period(lines[k]["code"]):
        return " ".join(parts), last, j
    while j < hi:
        ln = lines[j]
        if ln["kind"] in ("blank", "comment", "debug"):
            j += 1
            continue
        fw = first_word(ln["code"])
        if stop_on_verb and (fw in STMT_VERBS or ln["area_a"]):
            break
        parts.append(ln["code"].strip())
        last = ln["n"]
        j += 1
        if ends_with_period(ln["code"]):
            break
    return " ".join(parts), last, j


CICS_RESOURCE_OPTS = ("FILE", "DATASET", "PROGRAM", "MAP", "MAPSET", "TRANSID", "QUEUE", "QNAME",
                      "TSQUEUE", "TDQUEUE", "CHANNEL", "CONTAINER")


def parse_exec(text, path, a, b):
    u = strip_quotes_upper(text)
    m = re.match(r"^\s*EXEC\s+(CICS|SQL|DLI)\s+(.*?)\s*(END-EXEC)?\s*\.?\s*$", u, re.DOTALL)
    if not m:
        return {"kind": "EXEC", "text": squash(text)[:800], "source": src(path, a, b), "line": a}
    kind, body = m.group(1), squash(m.group(2))
    words = body.split(" ")
    rec = {"kind": kind, "text": squash(text)[:800], "source": src(path, a, b), "line": a,
           "end_line": b}
    if kind == "CICS":
        verb = words[0] if words else ""
        if verb in ("SEND", "RECEIVE", "HANDLE", "WRITEQ", "READQ", "DELETEQ", "IGNORE", "PUSH",
                    "POP", "START", "GET", "PUT", "ASSIGN", "INQUIRE", "SET") and len(words) > 1:
            nxt = re.match(r"^[A-Z]+", words[1])
            if nxt and nxt.group(0) in ("MAP", "TEXT", "CONTROL", "CONDITION", "ABEND", "AID", "TS",
                                        "TD", "PAGE", "CONTAINER", "BR", "TRANSID", "FILE",
                                        "PROGRAM"):
                verb = verb + " " + nxt.group(0)
        rec["verb"] = verb
        opts = {}
        for om in re.finditer(r"\b([A-Z][A-Z0-9-]*)\s*\(((?:[^()]|\([^()]*\))*)\)", body):
            opts.setdefault(om.group(1), om.group(2).strip())
        rec["options"] = opts
        for o in CICS_RESOURCE_OPTS:
            if o in opts:
                rec.setdefault("resources", []).append({"type": o, "value": opts[o]})
        rec["resp"] = "RESP" in opts
        rec["nohandle"] = "NOHANDLE" in words
    elif kind == "SQL":
        verb = words[0] if words else ""
        if verb == "DECLARE" and "CURSOR" in words:
            verb = "DECLARE CURSOR"
        rec["verb"] = verb
        tables = set()
        for tm in re.finditer(r"\b(?:FROM|INTO|UPDATE|JOIN|TABLE)\s+([A-Z][A-Z0-9_]*\.[A-Z0-9_]+|"
                              r"[A-Z][A-Z0-9_]{2,})", body):
            t = tm.group(1)
            if not t.startswith(":") and t not in ("SELECT", "VALUES", "TABLE"):
                tables.add(t)
        rec["tables"] = sorted(tables)
        cm = re.search(r"\b(?:OPEN|FETCH|CLOSE)\s+([A-Z0-9_-]+)", body)
        if verb in ("OPEN", "FETCH", "CLOSE") and cm:
            rec["cursor"] = cm.group(1)
        rec["host_variables"] = sorted(set(re.findall(r":([A-Z0-9-]+)", body)))[:40]
    else:
        rec["verb"] = words[0] if words else ""
        sm = re.findall(r"SEGMENT\s*\(\s*([A-Z0-9#@$-]+)\s*\)", body)
        rec["segments"] = sm
        pm = re.search(r"PCB\s*\(\s*([A-Z0-9-]+)\s*\)", body)
        if pm:
            rec["pcb"] = pm.group(1)
        rec["where"] = re.findall(r"WHERE\s*\(([^)]*)\)", body)
    return rec


def parse_procedure(lines, path, lo, hi, para_names):
    """Return (paragraph list, sections). lo/hi are indexes into lines (procedure body)."""
    paras, sections = [], []
    cur = None
    cur_section = None
    k = lo
    while k < hi:
        ln = lines[k]
        if ln["kind"] == "code" and ln["area_a"]:
            u = strip_quotes_upper(ln["code"]).strip()
            sm = re.match(r"^([A-Z0-9][A-Z0-9-]*)\s+SECTION\s*\.?$", u)
            pm = re.match(r"^([A-Z0-9][A-Z0-9-]*)\s*\.\s*(.*)$", u)
            if not pm and re.match(r"^[A-Z0-9][A-Z0-9-]*$", u) and next_code_is_period(lines, k + 1, hi):
                pm = re.match(r"^([A-Z0-9][A-Z0-9-]*)()$", u)
            if sm:
                cur_section = {"name": sm.group(1), "start_line": ln["n"]}
                sections.append(cur_section)
                cur = new_para(sm.group(1), ln["n"], cur_section["name"], True)
                paras.append(cur)
                k += 1
                continue
            if pm and pm.group(1) not in NON_PARAGRAPH_WORDS and not re.match(r"^\d+$", pm.group(1)) \
                    or (pm and re.match(r"^\d+$", pm.group(1)) and len(pm.group(1)) >= 3):
                cur = new_para(pm.group(1), ln["n"], cur_section and cur_section["name"], False)
                paras.append(cur)
                k += 1
                continue
        if ln["kind"] not in ("code", "cont"):
            k += 1
            continue
        if cur is None:
            cur = new_para("(PROCEDURE DIVISION entry)", ln["n"], None, False)
            cur["unnamed"] = True
            paras.append(cur)
        k = parse_statement(lines, k, hi, path, cur)
    # ranges
    for i, p in enumerate(paras):
        nxt = paras[i + 1]["start_line"] if i + 1 < len(paras) else (lines[hi - 1]["n"] + 1 if hi > 0 else p["start_line"] + 1)
        end = nxt - 1
        while end > p["start_line"] and lines[end - 1]["kind"] in ("blank", "comment"):
            end -= 1
        p["end_line"] = end
        p["source"] = src(path, p["start_line"], end)
    for s in sections:
        members = [p for p in paras if p["section"] == s["name"]]
        s["end_line"] = members[-1]["end_line"] if members else s["start_line"]
        s["paragraphs"] = [p["name"] for p in members if not p.get("is_section_header")]
        s["source"] = src(path, s["start_line"], s["end_line"])
    return paras, sections


def next_code_is_period(lines, j, hi):
    while j < hi:
        if lines[j]["kind"] in ("code", "cont"):
            return lines[j]["code"].strip() == "."
        j += 1
    return False


def new_para(name, n, section, is_section):
    p = {"name": name, "start_line": n, "section": section, "performs": [], "goto": [],
         "decisions": [], "calculations": [], "io": [], "exec": [], "calls": [],
         "literal_moves": [], "data_moves": [], "sets": [], "terminations": [], "displays": [],
         "other_statements": [], "unclassified": [], "statement_count": 0}
    if is_section:
        p["is_section_header"] = True
    return p


def parse_statement(lines, k, hi, path, p):
    ln = lines[k]
    code = ln["code"]
    u = strip_quotes_upper(code).strip()
    fw = first_word(u)
    n = ln["n"]
    if fw == "EXEC":
        j, parts, last = k, [], n
        while j < hi:
            if lines[j]["kind"] in ("code", "cont"):
                parts.append(lines[j]["code"].strip())
                last = lines[j]["n"]
                if "END-EXEC" in lines[j]["code"].upper():
                    j += 1
                    break
            j += 1
        rec = parse_exec(" ".join(parts), path, n, last)
        p["exec"].append(rec)
        p["statement_count"] += 1
        if rec.get("kind") == "CICS" and rec.get("verb") in ("RETURN", "XCTL", "ABEND"):
            p["terminations"].append({"verb": "EXEC CICS " + rec["verb"], "line": n,
                                      "source": rec["source"]})
        return j
    if fw in ("END-IF", "END-EVALUATE", "END-PERFORM", "END-READ", "END-EXEC", "END-WRITE",
              "END-REWRITE", "END-DELETE", "END-START", "END-CALL", "END-STRING", "END-COMPUTE",
              "END-UNSTRING", "END-SEARCH", "THEN", "ELSE", "CONTINUE", "OTHERWISE"):
        if fw == "ELSE":
            p["statement_count"] += 0
        rest = re.sub(r"^\s*(END-[A-Z]+|THEN|ELSE|CONTINUE)\s*\.?\s*", "", u)
        if rest and first_word(rest) in STMT_VERBS and first_word(rest) != fw:
            ln2 = dict(ln)
            ln2["code"] = rest
            lines_copy = lines[:]
            lines_copy[k] = ln2
            return parse_statement(lines_copy, k, hi, path, p)
        return k + 1
    p["statement_count"] += 1
    if fw == "IF":
        text, last, j = gather(lines, k, hi)
        cond = re.sub(r"^\s*IF\s+", "", text, flags=re.I) if sys.version_info >= (3, 1) else text[3:]
        cut = re.search(r"\s(THEN|MOVE|PERFORM|SET|DISPLAY|GO\s+TO|CONTINUE|COMPUTE|ADD|NEXT\s+SENTENCE)\b",
                        strip_quotes_upper(cond))
        rest = ""
        if cut:
            rest = squash(cond[cut.start():]).rstrip(".")
            cond = cond[:cut.start()]
        cond = squash(cond).rstrip(".")
        p["decisions"].append({"type": "IF", "condition": cond, "line": n,
                               "source": src(path, n, last), "class": classify_condition(cond)})
        if rest and not re.match(r"^(THEN|CONTINUE)\b", rest.upper()):
            p["unclassified"].append({"first_word": "INLINE-AFTER-IF", "text": rest[:300], "line": n,
                                      "source": src(path, n, last)})
        return j
    if fw == "EVALUATE":
        text, last, j = gather(lines, k, hi)
        subj = squash(re.sub(r"^\s*EVALUATE\s+", "", text, flags=re.I)).rstrip(".")
        p["decisions"].append({"type": "EVALUATE", "condition": subj, "line": n,
                               "source": src(path, n, last), "class": classify_condition(subj)})
        return j
    if fw == "WHEN":
        text, last, j = gather(lines, k, hi)
        w = squash(re.sub(r"^\s*WHEN\s+", "", text, flags=re.I))
        cut = re.search(r"\s(MOVE|PERFORM|SET|DISPLAY|GO\s+TO|CONTINUE|COMPUTE)\b", strip_quotes_upper(w))
        if cut:
            rest = squash(w[cut.start():]).rstrip(".")
            if rest and not rest.upper().startswith("CONTINUE"):
                p["unclassified"].append({"first_word": "INLINE-AFTER-WHEN", "text": rest[:300], "line": n,
                                          "source": src(path, n, last)})
            w = w[:cut.start()]
        evs = [d for d in p["decisions"] if d["type"] == "EVALUATE"]
        subject = evs[-1]["condition"] if evs else ""
        basis = w if subject.upper() in ("", "TRUE", "FALSE") else subject + " " + w
        rec = {"type": "WHEN", "condition": w.rstrip("."), "line": n,
               "source": src(path, n, last), "class": classify_condition(basis)}
        if subject:
            rec["evaluate_subject"] = subject[:120]
        p["decisions"].append(rec)
        return j
    if fw in ("AT", "INVALID", "NOT", "ON") and re.match(
            r"^\s*(AT\s+END|INVALID(\s+KEY)?|NOT\s+(AT\s+END|INVALID(\s+KEY)?|ON\s+\w+)|ON\s+(SIZE|EXCEPTION|OVERFLOW))", u):
        h = re.match(r"^\s*(NOT\s+)?(AT\s+END|INVALID(\s+KEY)?|ON\s+SIZE\s+ERROR|ON\s+EXCEPTION|ON\s+OVERFLOW|ON\s+\w+)", u).group(0)
        p["decisions"].append({"type": "HANDLER", "condition": squash(h), "line": n,
                               "source": src(path, n), "class": "io-status"})
        rest = u[len(h):].strip()
        if rest:
            ln2 = dict(ln)
            ln2["code"] = rest
            lines_copy = lines[:]
            lines_copy[k] = ln2
            p["statement_count"] -= 1
            return parse_statement(lines_copy, k, hi, path, p)
        return k + 1
    if fw == "PERFORM":
        text, last, j = gather(lines, k, hi)
        t = strip_quotes_upper(text)
        m = re.match(r"^\s*PERFORM\s+([A-Z0-9][A-Z0-9-]*)(?:\s+(?:THRU|THROUGH)\s+([A-Z0-9][A-Z0-9-]*))?(.*)$", t)
        if m and m.group(1) not in ("UNTIL", "VARYING", "WITH", "TEST") and not re.match(r"^\s*TIMES\b", m.group(3) or ""):
            rec = {"target": m.group(1), "line": n, "source": src(path, n, last)}
            if m.group(2):
                rec["thru"] = m.group(2)
            loop = squash(m.group(3) or "").rstrip(".")
            if loop:
                rec["loop"] = loop
            p["performs"].append(rec)
        else:
            loop = squash(re.sub(r"^\s*PERFORM\s*", "", t)).rstrip(".")
            p["performs"].append({"target": None, "inline": True, "loop": loop, "line": n,
                                  "source": src(path, n, last)})
            if loop:
                p["decisions"].append({"type": "LOOP", "condition": loop, "line": n,
                                       "source": src(path, n, last), "class": classify_condition(loop)})
        return j
    if fw == "GO":
        text, last, j = gather(lines, k, hi)
        m = re.match(r"^\s*GO\s+(?:TO\s+)?(.*?)\s*\.?\s*$", strip_quotes_upper(text))
        tg = m.group(1) if m else ""
        dep = None
        if " DEPENDING ON " in tg:
            tg, dep = tg.split(" DEPENDING ON ", 1)
        p["goto"].append({"targets": [x for x in tg.split() if x], "depending_on": dep, "line": n,
                          "source": src(path, n, last)})
        return j
    if fw in ("COMPUTE", "ADD", "SUBTRACT", "MULTIPLY", "DIVIDE"):
        text, last, j = gather(lines, k, hi)
        p["calculations"].append({"verb": fw, "text": squash(text).rstrip(".")[:400], "line": n,
                                  "source": src(path, n, last),
                                  "rounded": " ROUNDED" in strip_quotes_upper(text)})
        return j
    if fw in ("OPEN", "CLOSE", "READ", "WRITE", "REWRITE", "DELETE", "START", "RETURN", "RELEASE",
              "SORT", "MERGE"):
        text, last, j = gather(lines, k, hi)
        t = strip_quotes_upper(text)
        rec = {"verb": fw, "text": squash(text).rstrip(".")[:300], "line": n, "source": src(path, n, last)}
        if fw in ("OPEN", "CLOSE"):
            modes = {}
            mode = "CLOSE" if fw == "CLOSE" else None
            for w in re.sub(r"^\s*(OPEN|CLOSE)\s+", "", t).rstrip(".").split():
                if w in ("INPUT", "OUTPUT", "I-O", "EXTEND"):
                    mode = w
                elif mode:
                    modes.setdefault(mode, []).append(w)
            rec["files"] = modes
        else:
            m = re.match(r"^\s*\w+\s+([A-Z0-9-]+)", t)
            rec["target"] = m.group(1) if m else None
            if fw == "READ" and " NEXT" in t:
                rec["next"] = True
            km = re.search(r"\bKEY\s+(?:IS\s+)?([A-Z0-9-]+)", t)
            if km:
                rec["key"] = km.group(1)
            im = re.search(r"\bINTO\s+([A-Z0-9-]+)", t)
            if im:
                rec["into"] = im.group(1)
            fm = re.search(r"\bFROM\s+([A-Z0-9-]+)", t)
            if fm:
                rec["from"] = fm.group(1)
        p["io"].append(rec)
        return j
    if fw == "CALL":
        text, last, j = gather(lines, k, hi)
        t = strip_quotes_upper(text)
        m = re.match(r"^\s*CALL\s+(['\"]?)([A-Za-z0-9@#$-]+)\1(.*)$", t)
        rec = {"line": n, "source": src(path, n, last), "text": squash(text).rstrip(".")[:300]}
        if m:
            rec["target"] = m.group(2).upper()
            rec["dynamic"] = m.group(1) == ""
            us = re.search(r"\bUSING\s+(.*)$", m.group(3))
            if us:
                rec["using"] = [w for w in re.split(r"[\s,]+", us.group(1).rstrip(".")) if w and w not in ("BY", "REFERENCE", "CONTENT", "VALUE")][:20]
        p["calls"].append(rec)
        return j
    if fw == "MOVE":
        text, last, j = gather(lines, k, hi)
        m = re.match(r"^\s*MOVE\s+(['\"])(.*?)\1\s+TO\s+(.*)$", text, re.I | re.DOTALL)
        if m:
            p["literal_moves"].append({"value": m.group(2), "to": squash(m.group(3)).rstrip(".")[:120],
                                       "line": n, "source": src(path, n, last)})
        else:
            m = re.match(r"^\s*MOVE\s+([+-]?\d+(?:\.\d+)?)\s+TO\s+(.*)$", text, re.I | re.DOTALL)
            if m:
                p["literal_moves"].append({"value": m.group(1), "to": squash(m.group(2)).rstrip(".")[:120],
                                           "line": n, "source": src(path, n, last), "numeric": True})
            else:
                m = re.match(r"^\s*MOVE\s+(?:(CORR|CORRESPONDING)\s+)?(.*?)\s+TO\s+(.*)$", text, re.I | re.DOTALL)
                rec = {"text": squash(text).rstrip(".")[:300], "line": n, "source": src(path, n, last)}
                if m:
                    rec["from"] = squash(m.group(2))[:160]
                    rec["to"] = squash(m.group(3)).rstrip(".")[:160]
                    if m.group(1):
                        rec["corresponding"] = True
                p["data_moves"].append(rec)
        return j
    if fw == "SET":
        text, last, j = gather(lines, k, hi)
        p["sets"].append({"text": squash(text).rstrip(".")[:200], "line": n, "source": src(path, n, last)})
        return j
    if fw in ("GOBACK", "STOP") or re.match(r"^\s*EXIT\s+PROGRAM", u):
        p["terminations"].append({"verb": squash(u).rstrip("."), "line": n, "source": src(path, n)})
        return k + 1
    if fw == "DISPLAY":
        text, last, j = gather(lines, k, hi)
        p["displays"].append({"text": squash(text).rstrip(".")[:200], "line": n, "source": src(path, n, last)})
        return j
    if fw in ("STRING", "UNSTRING", "INSPECT", "INITIALIZE", "SEARCH", "ACCEPT", "CANCEL"):
        text, last, j = gather(lines, k, hi)
        p["other_statements"].append({"verb": fw, "text": squash(text).rstrip(".")[:300], "line": n,
                                      "source": src(path, n, last)})
        return j
    if fw == "EXIT":
        p["statement_count"] -= 1
        return k + 1
    if fw in ("NEXT", "ALTER", "COPY", "ENTRY") or re.match(r"^\s*NEXT\s+SENTENCE", u):
        text, last, j = gather(lines, k, hi, stop_on_verb=fw != "COPY")
        p["other_statements"].append({"verb": "NEXT SENTENCE" if fw == "NEXT" else fw,
                                      "text": squash(text).rstrip(".")[:300], "line": n,
                                      "source": src(path, n, last)})
        return j
    if u.strip() in ("", "."):
        p["statement_count"] -= 1
        return k + 1
    # Anything else is kept, not dropped, so coverage can show what the parser did not classify.
    text, last, j = gather(lines, k, hi)
    p["unclassified"].append({"first_word": fw, "text": squash(text).rstrip(".")[:300], "line": n,
                              "source": src(path, n, last)})
    return j


def analyze_cobol(path, member, kind):
    raw, sha = read_lines(path)
    lines = cobol_lines(raw)
    res = {"schema": SCHEMA, "member": member, "source_path": path, "sha256": sha,
           "line_count": len(raw), "artifact_type": kind}
    code_n = sum(1 for l in lines if l["kind"] in ("code", "cont"))
    res["loc"] = {"total": len(raw), "code": code_n,
                  "comment": sum(1 for l in lines if l["kind"] == "comment"),
                  "blank": sum(1 for l in lines if l["kind"] == "blank")}
    divs = []
    for idx, l in enumerate(lines):
        if l["kind"] != "code":
            continue
        m = re.match(r"^\s*(IDENTIFICATION|ID|ENVIRONMENT|DATA|PROCEDURE)\s+DIVISION\b(.*)$",
                     strip_quotes_upper(l["code"]))
        if m:
            name = "IDENTIFICATION" if m.group(1) == "ID" else m.group(1)
            d = {"name": name, "start_line": l["n"], "idx": idx}
            if name == "PROCEDURE":
                text, last, j = gather(lines, idx, len(lines), stop_on_verb=False)
                um = re.search(r"\bUSING\s+(.*?)\.?\s*$", strip_quotes_upper(text))
                if um:
                    d["using"] = [w for w in um.group(1).split() if w not in ("BY", "REFERENCE", "VALUE")]
            divs.append(d)
    for i, d in enumerate(divs):
        nxt_idx = divs[i + 1]["idx"] if i + 1 < len(divs) else len(lines)
        d["end_idx"] = nxt_idx
        end_n = lines[nxt_idx - 1]["n"] if nxt_idx > 0 else d["start_line"]
        d["end_line"] = end_n
        d["source"] = src(path, d["start_line"], end_n)
    res["divisions"] = [dict((k, v) for k, v in d.items() if k not in ("idx", "end_idx")) for d in divs]
    by = dict((d["name"], d) for d in divs)

    # identification
    ident = {}
    if "IDENTIFICATION" in by:
        d = by["IDENTIFICATION"]
        for first, last, text in join_entries(lines, d["idx"], d["end_idx"]):
            m = re.match(r"^\s*(PROGRAM-ID|AUTHOR|DATE-WRITTEN|DATE-COMPILED|INSTALLATION)\s*\.\s*(.*)$",
                         text, re.I)
            if m:
                ident[m.group(1).upper()] = {"value": m.group(2).strip().rstrip(".").strip("'\" "),
                                             "source": src(path, first, last)}
    res["identification"] = ident

    # data-division and environment-division sections
    data_sections = []
    for dname in ("ENVIRONMENT", "DATA"):
        if dname not in by:
            continue
        d = by[dname]
        for idx in range(d["idx"], d["end_idx"]):
            l = lines[idx]
            if l["kind"] != "code":
                continue
            m = re.match(r"^\s*([A-Z0-9-]+)\s+SECTION\s*\.", strip_quotes_upper(l["code"]))
            if m:
                data_sections.append({"division": dname, "name": m.group(1), "start_line": l["n"], "idx": idx})
    for i, s in enumerate(data_sections):
        same = [x for x in data_sections[i + 1:] if x["division"] == s["division"]]
        end_idx = same[0]["idx"] if same else by[s["division"]]["end_idx"]
        s["end_idx"] = end_idx
        s["end_line"] = lines[end_idx - 1]["n"]
        s["source"] = src(path, s["start_line"], s["end_line"])
    res["sections"] = [dict((k, v) for k, v in s.items() if k not in ("idx", "end_idx")) for s in data_sections]

    def section_of(n):
        for s in data_sections:
            if s["start_line"] <= n <= s["end_line"]:
                return s["name"]
        return None

    # SELECT entries
    selects = []
    for s in data_sections:
        if s["name"] != "INPUT-OUTPUT":
            continue
        for first, last, text in join_entries(lines, s["idx"], s["end_idx"]):
            t = strip_quotes_upper(text)
            m = re.match(r"^\s*SELECT\s+(?:OPTIONAL\s+)?([A-Z0-9-]+)\s+ASSIGN\s+(?:TO\s+)?(\S+)(.*)$", t)
            if not m:
                continue
            rest = m.group(3)
            sel = {"file": m.group(1), "assign": m.group(2).rstrip("."), "source": src(path, first, last)}
            for key, rx in (("organization", r"ORGANIZATION\s+(?:IS\s+)?([A-Z-]+)"),
                            ("access", r"ACCESS\s+(?:MODE\s+)?(?:IS\s+)?([A-Z-]+)"),
                            ("record_key", r"(?<!ALTERNATE )RECORD\s+KEY\s+(?:IS\s+)?([A-Z0-9-]+)"),
                            ("alternate_key", r"ALTERNATE\s+(?:RECORD\s+)?KEY\s+(?:IS\s+)?([A-Z0-9-]+)"),
                            ("file_status", r"(?:FILE\s+)?STATUS\s+(?:IS\s+)?([A-Z0-9-]+)")):
                mm = re.search(rx, rest)
                if mm:
                    sel[key] = mm.group(1).rstrip(".")
            selects.append(sel)
    res["selects"] = selects

    # data items
    items, fds, copies = [], [], []
    if "DATA" in by:
        d = by["DATA"]
        items, fds, copies = data_items(lines, path, d["idx"] + 1, d["end_idx"], section_of)
        items = [it for it in items if not re.match(r"^(WORKING-STORAGE|LINKAGE|FILE|LOCAL-STORAGE)$", it["name"])]
    res["data_items"] = items
    res["fds"] = fds

    # procedure
    paras, psections = [], []
    if "PROCEDURE" in by:
        d = by["PROCEDURE"]
        start = d["idx"]
        # skip the PROCEDURE DIVISION header (may span lines when USING is long)
        text, last, j = gather(lines, start, d["end_idx"], stop_on_verb=False)
        paras, psections = parse_procedure(lines, path, j, d["end_idx"], None)
    if not divs:
        # copybook or fragment: data entries and/or procedure paragraphs
        has_para = any(l["kind"] == "code" and l["area_a"] and
                       re.match(r"^[A-Z0-9][A-Z0-9-]*\s*\.\s*$", strip_quotes_upper(l["code"]).strip()) and
                       first_word(l["code"]) not in NON_PARAGRAPH_WORDS
                       for l in lines)
        first_code = [l for l in lines if l["kind"] == "code"]
        starts_with_level = bool(first_code) and re.match(r"^\s*\d{1,2}\s", first_code[0]["code"]) is not None
        if has_para and not starts_with_level:
            paras, psections = parse_procedure(lines, path, 0, len(lines), None)
            res["content"] = "procedure"
        else:
            items, fds, copies = data_items(lines, path, 0, len(lines))
            res["content"] = "data"
            res["data_items"] = items
            if has_para:
                res["notes"] = ["Contains area-A names that look like paragraphs; parsed as data"]
            # EXEC SQL DECLARE TABLE (DCLGEN)
            for first, last, text in join_entries(lines, 0, len(lines)):
                u = strip_quotes_upper(text)
                tm = re.search(r"EXEC\s+SQL\s+DECLARE\s+([A-Z0-9_.]+)\s+TABLE\s*\((.*)\)\s*END-EXEC", u)
                if tm:
                    cols = []
                    for cm2 in re.finditer(r"([A-Z][A-Z0-9_]*)\s+((?:VAR)?CHAR\s*\(\d+\)|DECIMAL\s*\(\s*\d+\s*(?:,\s*\d+\s*)?\)|"
                                           r"SMALLINT|INTEGER|BIGINT|DATE|TIMESTAMP|TIME)(\s+NOT\s+NULL)?", tm.group(2)):
                        cols.append({"name": cm2.group(1), "type": squash(cm2.group(2)),
                                     "not_null": bool(cm2.group(3))})
                    res.setdefault("sql_tables", []).append({"table": tm.group(1), "columns": cols,
                                                             "source": src(path, first, last)})
    copies = line_copies(lines, path, by["PROCEDURE"]["start_line"] if "PROCEDURE" in by else None)
    copies.extend(commented_copies(lines, path))
    res["copy_statements"] = copies
    res["paragraphs"] = paras
    res["procedure_sections"] = psections
    # roll-ups
    res["counts"] = {
        "paragraphs": len([p for p in paras if not p.get("is_section_header")]),
        "procedure_sections": len(psections),
        "data_items": len(items),
        "conditions_88": sum(len(it.get("conditions", [])) for it in items),
        "decisions": sum(len(p["decisions"]) for p in paras),
        "business_candidate_decisions": sum(1 for p in paras for d in p["decisions"] if d["class"] == "business-candidate"),
        "calculations": sum(len(p["calculations"]) for p in paras),
        "exec_blocks": sum(len(p["exec"]) for p in paras),
        "io_statements": sum(len(p["io"]) for p in paras),
        "calls": sum(len(p["calls"]) for p in paras),
        "performs": sum(len(p["performs"]) for p in paras),
        "literal_moves": sum(len(p["literal_moves"]) for p in paras),
        "data_moves": sum(len(p["data_moves"]) for p in paras),
        "unclassified_statements": sum(len(p["unclassified"]) for p in paras),
        "recorded_statements": sum(len(p[k]) for p in paras for k in STATEMENT_KEYS),
    }
    return res


# Every per-paragraph statement list; renderers and validators iterate over these.
STATEMENT_KEYS = ("decisions", "calculations", "io", "exec", "calls", "performs", "goto", "literal_moves",
                  "data_moves", "sets", "other_statements", "displays", "terminations", "unclassified")


def resolve_performs(res, proc_copybook_paras):
    names = set(p["name"] for p in res["paragraphs"])
    secs = set(s["name"] for s in res["procedure_sections"])
    unresolved = []
    for p in res["paragraphs"]:
        for pf in p["performs"]:
            t = pf.get("target")
            if not t:
                continue
            if t in names or t in secs:
                pf["resolved"] = "local"
            elif t in proc_copybook_paras:
                pf["resolved"] = "copybook:" + proc_copybook_paras[t]
            else:
                pf["resolved"] = "unresolved"
                unresolved.append({"paragraph": p["name"], "target": t, "source": pf["source"]})
        for g in p["goto"]:
            for t in g["targets"]:
                if t not in names and t not in secs and t not in proc_copybook_paras:
                    unresolved.append({"paragraph": p["name"], "target": t, "source": g["source"], "goto": True})
    res["unresolved_targets"] = unresolved
    # reachability from entry (first paragraph), following PERFORM/GO TO/fall-through for sections
    if res["paragraphs"]:
        order = [p["name"] for p in res["paragraphs"]]
        edges = {}
        for p in res["paragraphs"]:
            tg = set()
            for pf in p["performs"]:
                if pf.get("target"):
                    tg.add(pf["target"])
                    if pf.get("thru") and pf["target"] in order and pf["thru"] in order:
                        a, b = order.index(pf["target"]), order.index(pf["thru"])
                        tg.update(order[a:b + 1])
            for g in p["goto"]:
                tg.update(g["targets"])
            edges[p["name"]] = tg
        # fall-through: a paragraph without a termination or GO TO flows into the next one
        for i, p in enumerate(res["paragraphs"][:-1]):
            if not p["terminations"] and not p["goto"] and p.get("unnamed"):
                edges[p["name"]].add(order[i + 1])
        seen, stack = set(), [order[0]]
        while stack:
            x = stack.pop()
            if x in seen:
                continue
            seen.add(x)
            stack.extend(edges.get(x, ()))
        for p in res["paragraphs"]:
            p["reachable_static"] = p["name"] in seen
            p["performed_by"] = sorted(q for q, t in edges.items() if p["name"] in t and q != p["name"])


# ----------------------------------------------------------------- JCL
def jcl_statements(raw, path):
    """Yield statements: dict(kind, name, op, operands, first, last, instream)."""
    stmts, i, n = [], 0, len(raw)
    while i < n:
        line = raw[i]
        l72 = line[:72] if len(line) > 72 else line
        if l72.startswith("//*"):
            stmts.append({"kind": "comment", "first": i + 1, "last": i + 1, "text": l72[3:].rstrip()})
            i += 1
            continue
        if l72.startswith("/*"):
            i += 1
            continue
        if not l72.startswith("//"):
            i += 1
            continue
        body = l72[2:]
        m = re.match(r"^(\S*)\s+(\S+)\s*(.*)$", body)
        if not m:
            stmts.append({"kind": "null", "first": i + 1, "last": i + 1})
            i += 1
            continue
        name, op, rest = m.group(1), m.group(2).upper(), m.group(3)
        operands = operand_field(rest)
        first = i + 1
        j = i + 1
        while operands.endswith(",") and j < n:
            nl = raw[j][:72]
            if nl.startswith("//*"):
                j += 1
                continue
            if not nl.startswith("//"):
                break
            operands += operand_field(nl[2:].strip())
            j += 1
        st = {"kind": "stmt", "name": name, "op": op, "operands": operands, "first": first, "last": j}
        stmts.append(st)
        i = j
        if op == "DD" and re.match(r"^(\*|DATA)(,|$)", operands.upper()):
            dlm = re.search(r"DLM=(?:'([^']+)'|(\S\S))", operands.upper())
            dlm = (dlm.group(1) or dlm.group(2)) if dlm else None
            data_first, data = i + 1, []
            while i < n:
                dl = raw[i]
                if dlm and dl.startswith(dlm):
                    i += 1
                    break
                if not dlm and (dl.startswith("/*") or (dl.startswith("//") and not operands.upper().startswith("DATA"))):
                    if dl.startswith("/*"):
                        i += 1
                    break
                data.append(dl[:72].rstrip())
                i += 1
            st["instream"] = {"first": data_first, "last": data_first + len(data) - 1, "lines": data}
    return stmts


def operand_field(rest):
    """Operand field ends at the first blank outside quotes and parentheses."""
    out, q, depth = [], False, 0
    for ch in rest:
        if ch == "'":
            q = not q
        elif not q:
            if ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
            elif ch == " " and depth <= 0:
                break
        out.append(ch)
    return "".join(out)


def kw(operands, key):
    m = re.search(r"(?:^|,)" + key + r"=((?:\([^()]*(?:\([^()]*\)[^()]*)*\))|'[^']*'|[^,]+)", operands, re.I)
    return m.group(1) if m else None


def analyze_jcl(path, member, kind):
    raw, sha = read_lines(path)
    stmts = jcl_statements(raw, path)
    res = {"schema": SCHEMA, "member": member, "source_path": path, "sha256": sha, "artifact_type": kind,
           "line_count": len(raw), "job": None, "steps": [], "conditionals": [], "sets": [],
           "jcllib": [], "includes": [], "procs": [], "comments": 0}
    step, last_dd = None, None
    for st in stmts:
        if st["kind"] == "comment":
            res["comments"] += 1
            continue
        if st["kind"] != "stmt":
            continue
        op, name, ops = st["op"], st["name"], st["operands"]
        s = src(path, st["first"], st["last"])
        if op == "JOB":
            res["job"] = {"name": name, "source": s, "class": kw(ops, "CLASS"), "msgclass": kw(ops, "MSGCLASS"),
                          "notify": kw(ops, "NOTIFY"), "cond": kw(ops, "COND"), "region": kw(ops, "REGION"),
                          "restart": kw(ops, "RESTART"), "typrun": kw(ops, "TYPRUN")}
        elif op == "EXEC":
            pgm = kw(ops, "PGM")
            proc = kw(ops, "PROC")
            if not pgm and not proc:
                first_op = ops.split(",")[0]
                if "=" not in first_op:
                    proc = first_op
            step = {"name": name or "(unnamed)", "line": st["first"], "source": s, "pgm": pgm, "proc": proc,
                    "parm": kw(ops, "PARM"), "cond": kw(ops, "COND"), "region": kw(ops, "REGION"),
                    "dds": [], "operands": ops[:300]}
            for pk in re.finditer(r"(PARM\.[A-Z0-9#@$]+|COND\.[A-Z0-9#@$]+)=", ops, re.I):
                step.setdefault("overrides", []).append(pk.group(1))
            res["steps"].append(step)
            last_dd = None
        elif op == "DD":
            dd = {"ddname": name, "line": st["first"], "source": s, "dsn": kw(ops, "DSN") or kw(ops, "DSNAME"),
                  "disp": kw(ops, "DISP"), "sysout": kw(ops, "SYSOUT"), "operands": ops[:300]}
            u = ops.upper()
            if u.startswith("DUMMY") or "DSN=NULLFILE" in u:
                dd["dummy"] = True
            if re.match(r"^(\*|DATA)(,|$)", u):
                dd["instream"] = True
            for k2 in ("DCB", "RECFM", "LRECL", "SPACE", "UNIT", "BLKSIZE"):
                v = kw(ops, k2)
                if v:
                    dd[k2.lower()] = v
            if st.get("instream"):
                ins = st["instream"]
                dd["instream_lines"] = {"first": ins["first"], "last": ins["last"]}
                dd["control"] = control_summary(ins["lines"])
            if name == "" and last_dd is not None:
                dd["ddname"] = last_dd["ddname"]
                dd["concatenation"] = True
            if "." in (name or "") and name:
                dd["override_of"] = name
            if dd["dsn"]:
                g = re.match(r"^(.*)\(([+-]?\d+)\)$", dd["dsn"])
                if g:
                    dd["gdg_base"], dd["gdg_generation"] = g.group(1), g.group(2)
                if dd["dsn"].startswith("&&"):
                    dd["temporary"] = True
            if step is not None:
                step["dds"].append(dd)
            else:
                res.setdefault("job_dds", []).append(dd)
            last_dd = dd
        elif op in ("IF", "ELSE", "ENDIF"):
            res["conditionals"].append({"op": op, "name": name, "condition": squash(ops + " " ), "line": st["first"],
                                        "source": s, "before_step": None})
        elif op == "SET":
            res["sets"].append({"text": ops, "source": s})
        elif op == "JCLLIB":
            res["jcllib"].append({"text": ops, "source": s})
        elif op == "INCLUDE":
            res["includes"].append({"member": kw(ops, "MEMBER"), "source": s})
        elif op in ("PROC", "PEND"):
            res["procs"].append({"op": op, "name": name, "operands": ops, "source": s})
    # IF/THEN block membership: steps whose line falls between IF and ENDIF
    stack = []
    for c in res["conditionals"]:
        if c["op"] == "IF":
            stack.append(c)
        elif c["op"] == "ENDIF" and stack:
            o = stack.pop()
            o["end_line"] = c["line"]
    for c in res["conditionals"]:
        if c["op"] == "IF":
            c["steps"] = [x["name"] for x in res["steps"] if c["line"] < x["line"] < c.get("end_line", 10 ** 9)]
            c["condition"] = re.sub(r"\s*THEN\s*$", "", c["condition"], flags=re.I).strip()
    # application program behind utility steps
    for stp in res["steps"]:
        app = None
        pg = (stp["pgm"] or "").upper()
        if pg == "DFSRRC00" and stp["parm"]:
            parts = stp["parm"].strip("'()").split(",")
            if len(parts) >= 2:
                app = {"program": parts[1].strip(), "via": "DFSRRC00 PARM", "region_type": parts[0].strip(),
                       "psb": parts[2].strip() if len(parts) > 2 else None}
        for dd in stp["dds"]:
            ctl = dd.get("control") or {}
            if ctl.get("run_program") and pg in ("IKJEFT01", "IKJEFT1B", "IKJEFT1A"):
                app = {"program": ctl["run_program"], "via": "TSO DSN RUN PROGRAM", "plan": ctl.get("plan")}
        if app:
            stp["application_program"] = app
    return res


def control_summary(lines):
    text = "\n".join(lines)
    u = text.upper()
    out = {"line_count": len(lines)}
    m = re.search(r"RUN\s+PROGRAM\s*\(\s*([A-Z0-9#@$]+)\s*\)", u)
    if m:
        out["run_program"] = m.group(1)
        pm = re.search(r"PLAN\s*\(\s*([A-Z0-9#@$]+)\s*\)", u)
        if pm:
            out["plan"] = pm.group(1)
    verbs = []
    for l in lines:
        w = first_word(l)
        if w in ("DEFINE", "DELETE", "REPRO", "PRINT", "LISTCAT", "ALTER", "BLDINDEX", "VERIFY",
                 "SORT", "MERGE", "INCLUDE", "OMIT", "OUTREC", "INREC", "OUTFIL", "SUM", "OPTION",
                 "SELECT", "INSERT", "UPDATE", "CREATE", "DROP", "GRANT", "COMMIT", "LOAD",
                 "PUT", "GET", "CD", "QUIT", "BIND", "RUN", "DSN", "END", "SET"):
            verbs.append(w)
    if verbs:
        seen, ordered = set(), []
        for v in verbs:
            if v not in seen:
                seen.add(v)
                ordered.append(v)
        out["verbs"] = ordered
    names = re.findall(r"\bNAME\s*\(\s*([A-Z0-9.#@$&]+)\s*\)", u)
    if names:
        out["names"] = sorted(set(names))[:30]
    tables = re.findall(r"\b(?:FROM|INTO|TABLE|UPDATE)\s+([A-Z][A-Z0-9_]*\.[A-Z0-9_]+)", u)
    if tables:
        out["tables"] = sorted(set(tables))
    return out


# ----------------------------------------------------------------- CSD
def analyze_csd(paths):
    res = {"schema": SCHEMA, "files": [], "resources": []}
    for path in paths:
        raw, sha = read_lines(path)
        res["files"].append({"path": path, "sha256": sha})
        cur = None
        for i, l in enumerate(raw):
            n = i + 1
            u = l.upper()
            if u.strip().startswith("*"):
                continue
            m = re.match(r"^\s*DEFINE\s+([A-Z][A-Z0-9]*)\s*\(\s*([^)\s]+)\s*\)(.*)$", u)
            if m:
                cur = {"type": m.group(1), "name": m.group(2), "source_path": path, "line": n,
                       "attrs": {}, "end_line": n}
                res["resources"].append(cur)
                text = m.group(3)
            elif cur is not None and l.strip():
                text = u
                cur["end_line"] = n
            else:
                continue
            for am in re.finditer(r"\b([A-Z][A-Z0-9]*)\s*\(([^()]*)\)", text):
                cur["attrs"].setdefault(am.group(1), am.group(2).strip())
    for r in res["resources"]:
        r["source"] = src(r["source_path"], r["line"], r["end_line"])
    return res


# ----------------------------------------------------------------- data definitions
def analyze_data_defs(inv):
    out = {"schema": SCHEMA, "ddl": [], "dbd": [], "psb": []}
    for e in inv["files"]:
        t, path = e["type"], e["path"]
        if t not in ("db2-ddl", "ims-dbd", "ims-psb", "control-cards"):
            continue
        raw, sha = read_lines(path)
        if t in ("db2-ddl", "control-cards"):
            text = "\n".join(raw)
            for m in re.finditer(r"CREATE\s+(TABLE|UNIQUE\s+INDEX|INDEX|TABLESPACE|DATABASE|VIEW|STOGROUP)\s+([A-Z0-9_.<>-]+)",
                                 text, re.I):
                ln = text.count("\n", 0, m.start()) + 1
                obj = {"object": squash(m.group(1)).upper(), "name": m.group(2).upper(), "path": path,
                       "source": src(path, ln), "artifact_type": t}
                if obj["object"] == "TABLE":
                    body_m = re.search(r"\((.*?)\)\s*(?:IN\s|;|$)", text[m.end():], re.S)
                    cols = []
                    if body_m:
                        for cm in re.finditer(r"^\s*([A-Z][A-Z0-9_]*)\s+((?:VAR)?CHAR\s*\(\d+\)|DECIMAL\s*\([^)]*\)|"
                                              r"SMALLINT|INTEGER|BIGINT|DATE|TIMESTAMP|TIME)", body_m.group(1), re.I | re.M):
                            if cm.group(1).upper() not in ("PRIMARY", "CONSTRAINT", "FOREIGN"):
                                cols.append({"name": cm.group(1).upper(), "type": squash(cm.group(2)).upper()})
                    obj["columns"] = cols
                    pk = re.search(r"PRIMARY\s+KEY\s*\(([^)]*)\)", text[m.end():m.end() + 4000], re.I)
                    if pk:
                        obj["primary_key"] = [x.strip().upper() for x in pk.group(1).split(",")]
                if obj["object"] in ("INDEX", "UNIQUE INDEX"):
                    on = re.search(r"\bON\s+([A-Z0-9_.]+)", text[m.end():m.end() + 400], re.I)
                    if on:
                        obj["on_table"] = on.group(1).upper()
                out["ddl"].append(obj)
        elif t == "ims-dbd":
            dbd = {"path": path, "segments": [], "name": None}
            for i, l in enumerate(raw):
                if l.startswith("*"):
                    continue
                m = re.search(r"\bDBD\s+NAME=([A-Z0-9#@$]+)(?:,ACCESS=(\([^)]*\)|[A-Z]+))?", l)
                if m:
                    dbd["name"], dbd["access"], dbd["source"] = m.group(1), m.group(2), src(path, i + 1)
                m = re.search(r"\bSEGM\s+NAME=([A-Z0-9#@$]+),PARENT=(\(\([^)]*\)\)|[A-Z0-9#@$]+)(?:,BYTES=(\d+))?", l)
                if m:
                    dbd["segments"].append({"name": m.group(1), "parent": m.group(2).strip("()").rstrip(","),
                                            "bytes": m.group(3), "source": src(path, i + 1), "fields": []})
                m = re.search(r"\bFIELD\s+NAME=(\([^)]*\)|[A-Z0-9#@$]+),START=(\d+),BYTES=(\d+)(?:,TYPE=([A-Z]))?", l)
                if m and dbd["segments"]:
                    dbd["segments"][-1]["fields"].append({"name": m.group(1), "start": m.group(2), "bytes": m.group(3),
                                                          "type": m.group(4), "source": src(path, i + 1)})
            out["dbd"].append(dbd)
        else:
            psb = {"path": path, "pcbs": [], "name": None}
            for i, l in enumerate(raw):
                if l.startswith("*"):
                    continue
                m = re.search(r"^(\S*)\s+PCB\s+TYPE=([A-Z]+)(?:,DBDNAME=([A-Z0-9#@$]+))?(?:,PROCOPT=([A-Z]+))?", l)
                if m:
                    psb["pcbs"].append({"label": m.group(1) or None, "type": m.group(2), "dbd": m.group(3),
                                        "procopt": m.group(4), "source": src(path, i + 1), "senseg": []})
                m = re.search(r"\bSENSEG\s+NAME=([A-Z0-9#@$]+)", l)
                if m and psb["pcbs"]:
                    psb["pcbs"][-1]["senseg"].append(m.group(1))
                m = re.search(r"\bPSBGEN\s+.*PSBNAME=([A-Z0-9#@$]+)", l)
                if m:
                    psb["name"], psb["source"] = m.group(1), src(path, i + 1)
            out["psb"].append(psb)
    return out


# ----------------------------------------------------------------- main
def main(argv):
    if len(argv) < 3:
        raise SystemExit(__doc__)
    inv = load_json(argv[1])
    work = argv[2]
    only = argv[argv.index("--only") + 1] if "--only" in argv else None
    out = os.path.join(work, "structure")
    files = inv["files"]
    members = {}
    for e in files:
        if e["type"] in COPY_TYPES:
            members.setdefault(e["member"].upper(), []).append(e)
    summary = {"schema": SCHEMA, "counts": {}}

    if only in (None, "copybook", "cobol"):
        cpy_res = {}
        for e in files:
            if e["type"] in ("cobol-copybook", "db2-dclgen"):
                r = analyze_cobol(e["path"], e["member"].upper(), e["type"])
                cpy_res[r["member"] + "|" + e["path"]] = r
        proc_paras = {}
        for r in cpy_res.values():
            if r.get("content") == "procedure":
                for p in r["paragraphs"]:
                    proc_paras.setdefault(p["name"], r["member"])
        for key, r in cpy_res.items():
            if r.get("content") == "procedure":
                resolve_performs(r, proc_paras)
            save_json(os.path.join(out, "copybooks", file_key(r, members) + ".json"), r)
        summary["counts"]["copybooks"] = len(cpy_res)

    if only in (None, "cobol"):
        usage = []
        prog_n = 0
        for e in files:
            if e["type"] not in ("cobol-program", "cobol-copybook", "db2-dclgen"):
                continue
            if e["type"] == "cobol-program":
                r = analyze_cobol(e["path"], e["member"].upper(), e["type"])
                pid = r["identification"].get("PROGRAM-ID", {}).get("value", "").upper()
                r["program_id"] = pid or r["member"]
                resolve_performs(r, proc_paras)
                save_json(os.path.join(out, "programs", r["member"] + ".json"), r)
                prog_n += 1
            else:
                r = cpy_res[e["member"].upper() + "|" + e["path"]]
            for c in r["copy_statements"]:
                cand = members.get(c["name"], [])
                same_mod = [x for x in cand if x.get("module") == e.get("module")]
                if cand:
                    pick = (same_mod or cand)[0]
                    res_kind, rpath = "inventory", pick["path"]
                    alts = [x["path"] for x in cand if x["path"] != rpath]
                elif SYSTEM_COPYBOOKS.match(c["name"]):
                    res_kind, rpath, alts = "system", None, []
                else:
                    res_kind, rpath, alts = "external-or-missing", None, []
                rec = {"from": e["path"], "from_member": e["member"].upper(), "from_type": e["type"],
                       "copybook": c["name"], "kind": c["kind"], "source": c["source"],
                       "commented": c["commented"], "resolution": res_kind, "resolved_path": rpath}
                if alts:
                    rec["other_candidates"] = alts
                if c.get("replacing"):
                    rec["replacing"] = c["replacing"]
                if c.get("procedure_division"):
                    rec["procedure_division"] = True
                usage.append(rec)
        save_json(os.path.join(out, "copybook-usage.json"), {"schema": SCHEMA, "edges": usage})
        summary["counts"]["programs"] = prog_n
        summary["counts"]["copy_edges"] = len(usage)

    if only in (None, "jcl"):
        jn = 0
        for e in files:
            if e["type"] in ("jcl-job", "jcl-proc", "jcl-template"):
                r = analyze_jcl(e["path"], e["member"].upper(), e["type"])
                save_json(os.path.join(out, "jcl", jcl_key(r) + ".json"), r)
                jn += 1
        summary["counts"]["jcl"] = jn

    if only in (None, "csd"):
        c = analyze_csd([e["path"] for e in files if e["type"] == "cics-csd"])
        save_json(os.path.join(out, "csd.json"), c)
        summary["counts"]["csd_resources"] = len(c["resources"])

    if only in (None, "data"):
        d = analyze_data_defs(inv)
        save_json(os.path.join(out, "data-definitions.json"), d)
        summary["counts"]["ddl_objects"] = len(d["ddl"])

    if only is None:
        save_json(os.path.join(out, "summary.json"), summary)
    sys.stdout.write(json.dumps(summary["counts"], sort_keys=True) + "\n")


def file_key(r, members):
    if len(members.get(r["member"], [])) > 1:
        return r["member"] + "__" + re.sub(r"[^A-Za-z0-9]+", "_", os.path.dirname(r["source_path"]))
    return r["member"]


def jcl_key(r):
    if r["artifact_type"] == "jcl-proc":
        return r["member"] + "__PROC"
    if r["artifact_type"] == "jcl-template":
        return r["member"] + "__TEMPLATE"
    return r["member"]


if __name__ == "__main__":
    main(sys.argv)
