"""Extract a baseline cross-reference from classified mainframe sources.

Usage:
  python scan_references.py <inventory.json> --out <references.json>

Reads files listed in inventory.json (paths relative to its repo_root),
ignores comment lines and sequence/identification areas, joins multi-line
EXEC blocks, and emits raw references with line numbers. Results are a
baseline for analysis, not a final model. Python 3.1+ compatible.
"""
import json
import os
import re
import sys

COBOL_TYPES = ("cobol-program", "cobol-copybook", "bms-symbolic-map", "db2-dclgen")
JCL_TYPES = ("jcl-job", "jcl-proc", "jcl-template")

NAME = r"[A-Z0-9@#$][A-Z0-9@#$_-]*"
# COBOL word boundary: hyphens are part of names (END-CALL, 3200-IMS-CALL).
WB = r"(?<![A-Z0-9@#$_-])"


def read_lines(path):
    f = open(path, "rb")
    try:
        data = f.read()
    finally:
        f.close()
    return data.decode("latin-1").splitlines()


class Joined(object):
    """Concatenate code fragments while remembering the source line of each offset."""

    def __init__(self):
        self.parts = []
        self.starts = []
        self.lines = []
        self.length = 0

    def add(self, text, lineno):
        self.starts.append(self.length)
        self.lines.append(lineno)
        self.parts.append(text + "\n")
        self.length += len(text) + 1

    def text(self):
        return "".join(self.parts)

    def line_at(self, pos):
        lo, hi = 0, len(self.starts) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if self.starts[mid] <= pos:
                lo = mid
            else:
                hi = mid - 1
        return self.lines[lo] if self.lines else 0


def cobol_code(lines, fixed):
    j = Joined()
    for i, raw in enumerate(lines):
        ln = raw.rstrip("\r")
        if fixed:
            if len(ln) < 7:
                continue
            ind = ln[6]
            if ind in "*/":
                continue
            if ind in "dD":
                continue
            code = ln[7:72]
        else:
            s = ln.lstrip()
            if s.startswith("*") or s.startswith("*>"):
                continue
            code = ln
        k = code.find("*>")
        if k >= 0:
            code = code[:k]
        j.add(code.upper(), i + 1)
    return j


def is_fixed(entry, lines):
    fmt = entry.get("format") or {}
    if fmt.get("sequence_area"):
        return True
    code_like = 0
    fixed_like = 0
    for ln in lines[:400]:
        if len(ln.strip()) == 0:
            continue
        code_like += 1
        head = ln[:6]
        if head.strip() == "" or head.strip().isdigit():
            fixed_like += 1
    return code_like == 0 or fixed_like * 10 >= code_like * 8


def opt(block, name):
    m = re.search(r"\b" + name + r"\s*\(\s*('([^']*)'|\"([^\"]*)\"|([^)\s]+))\s*\)", block)
    if not m:
        return None
    lit = m.group(2) or m.group(3)
    if lit is not None:
        return {"value": lit.strip(), "literal": True}
    return {"value": m.group(4), "literal": False}


def blank_literals(text):
    """Replace the inside of quoted literals with spaces, preserving offsets."""
    def repl(m):
        s = m.group(0)
        return s[0] + " " * (len(s) - 2) + s[-1]
    return re.sub(r"'[^'\n]*'|\"[^\"\n]*\"", repl, text)


def scan_cobol(entry, lines, add):
    fixed = is_fixed(entry, lines)
    j = cobol_code(lines, fixed)
    t = j.text()
    tb = blank_literals(t)
    for m in re.finditer(r"\bPROGRAM-ID\s*\.?\s*['\"]?\s*(" + NAME + r")?", tb):
        tm = re.match(r"PROGRAM-ID\s*\.?\s*['\"]?\s*(" + NAME + r")", t[m.start():])
        if tm:
            add("program-id", tm.group(1), j.line_at(m.start()))
    for m in re.finditer(WB + r"COPY\s+(" + NAME + r")(\s+(OF|IN)\s+(" + NAME + r"))?", tb):
        rep = "REPLACING" in tb[m.end():m.end() + 40]
        add("copy", m.group(1), j.line_at(m.start()), {"library": m.group(4), "replacing": rep})
    for m in re.finditer(WB + r"CALL\s+", tb):
        tm = re.match(r"(?:'([^']+)'|\"([^\"]+)\"|(" + NAME + r"))", t[m.end():])
        if not tm:
            continue
        lit = tm.group(1) or tm.group(2)
        if lit:
            add("call", lit.strip(), j.line_at(m.start()), {"dynamic": False})
        elif tm.group(3) not in ("USING",):
            add("call", tm.group(3), j.line_at(m.start()), {"dynamic": True})
    for m in re.finditer(WB + r"SELECT\s+(?:OPTIONAL\s+)?(" + NAME + r")\s+ASSIGN\s+(?:TO\s+)?", tb):
        tm = re.match(r"(?:'([^']+)'|\"([^\"]+)\"|(" + NAME + r"))", t[m.end():])
        dd = (tm.group(1) or tm.group(2) or tm.group(3)) if tm else None
        add("file-assign", m.group(1), j.line_at(m.start()), {"ddname": dd})
    for m in re.finditer(WB + r"FD\s+(" + NAME + r")", tb):
        add("fd", m.group(1), j.line_at(m.start()))
    for m in re.finditer(WB + r"EXEC\s+(CICS|SQL|DLI)\b(.*?)END-EXEC", tb, re.DOTALL):
        kind = m.group(1)
        block = " ".join(t[m.start(2):m.end(2)].split())
        line = j.line_at(m.start())
        words = block.split(" ")
        verb = words[0] if words else ""
        detail = {"block": block[:300]}
        if kind == "CICS":
            if verb == "HANDLE" and len(words) > 1:
                verb = "HANDLE " + words[1]
            for o in ("PROGRAM", "FILE", "DATASET", "MAP", "MAPSET", "TRANSID", "QUEUE", "QNAME",
                      "RIDFLD", "INTO", "FROM", "COMMAREA", "ABCODE", "SYSID"):
                v = opt(block, o)
                if v:
                    detail[o.lower()] = v
            add("exec-cics", verb, line, detail)
        elif kind == "SQL":
            if verb == "INCLUDE" and len(words) > 1:
                add("sql-include", words[1].rstrip("."), line)
                continue
            tables = set()
            for tm in re.finditer(r"\b(FROM|INTO|UPDATE|JOIN|TABLE)\s+(" + NAME + r"(\." + NAME + r")?)", block):
                tgt = tm.group(2)
                if not tgt.startswith(":") and tgt not in ("SELECT",):
                    tables.add(tgt)
            cm = re.search(r"DECLARE\s+(" + NAME + r")\s+CURSOR", block)
            if cm:
                detail["cursor"] = cm.group(1)
            dm = re.search(r"DECLARE\s+(" + NAME + r"(\." + NAME + r")?)\s+TABLE", block)
            if dm:
                tables.add(dm.group(1))
            detail["tables"] = sorted(tables)
            add("exec-sql", verb, line, detail)
        else:
            for o in ("PSB", "SEGMENT", "USING PCB", "PCB"):
                v = opt(block, o)
                if v:
                    detail[o.lower().replace(" ", "_")] = v
            add("exec-dli", verb, line, detail)


def jcl_statements(lines):
    """Yield (lineno, text) for joined JCL statements, skipping comments and in-stream data."""
    stmts = []
    cur = None
    instream = False
    dlm = "/*"
    for i, raw in enumerate(lines):
        ln = raw.rstrip("\r")[:72]
        if instream:
            if ln.startswith(dlm) or (ln.startswith("//") and dlm == "/*"):
                instream = False
                if not ln.startswith("//"):
                    continue
            else:
                stmts.append((i + 1, "SYSIN-DATA " + ln.upper()))
                continue
        if not ln.startswith("//") or ln.startswith("//*"):
            continue
        body = ln[2:].upper()
        if cur is not None and cur[2] and body[:1] == " ":
            # Continuation: operand is the first token; anything after it is a comment.
            parts = body.split()
            operand = parts[0] if parts else ""
            cur[1] += " " + operand
            cur[2] = operand.endswith(",")
        else:
            if cur is not None:
                stmts.append((cur[0], cur[1]))
            parts = body.split()
            # name field is absent when the statement starts with a blank.
            op_idx = 1 if body[:1] == " " else 2
            head = parts[:op_idx]
            operand = parts[op_idx] if len(parts) > op_idx else ""
            text = " ".join(([""] if body[:1] == " " else []) + head + [operand])
            cur = [i + 1, text, operand.endswith(",")]
        if re.search(r"\bDD\s+(\*|DATA)\b", body):
            if cur is not None:
                stmts.append((cur[0], cur[1]))
                cur = None
            instream = True
            dm = re.search(r"DLM=('?)(\S\S)\1", body)
            dlm = dm.group(2) if dm else "/*"
    if cur is not None:
        stmts.append((cur[0], cur[1]))
    return stmts


def scan_jcl(entry, lines, add):
    last_step = None
    last_dd = None
    for lineno, s in jcl_statements(lines):
        if s.startswith("SYSIN-DATA "):
            d = s[len("SYSIN-DATA "):]
            for m in re.finditer(r"RUN\s+PROGRAM\s*\(\s*(" + NAME + r")\s*\)", d):
                add("jcl-run-program", m.group(1), lineno, {"step": last_step})
            for m in re.finditer(r"\bPLAN\s*\(\s*(" + NAME + r")\s*\)", d):
                add("db2-plan", m.group(1), lineno, {"step": last_step})
            for m in re.finditer(r"\b(INFILE|OUTFILE|INDATASET|OUTDATASET|NAME)\s*\(\s*([A-Z0-9@#$.&()+-]+?)\s*\)", d):
                add("utility-dataset", m.group(2), lineno, {"step": last_step, "keyword": m.group(1)})
            continue
        m = re.match(r"(\S*)\s+(JOB|EXEC|DD|PROC|SET|INCLUDE|JCLLIB|PEND|IF|ENDIF|ELSE|OUTPUT)\b\s*(.*)", s)
        if not m:
            continue
        label, op, rest = m.group(1), m.group(2), m.group(3)
        if op == "JOB":
            add("jcl-job", label, lineno)
        elif op == "PROC":
            add("jcl-proc-def", label, lineno)
        elif op == "EXEC":
            last_step = label
            pm = re.match(r"(PGM=([^,\s]+)|PROC=([^,\s]+)|([^,\s=]+))", rest)
            parm = re.search(r"\bPARM(\.\S+)?=('[^']*'|\([^)]*\)|[^,\s]+)", rest)
            cond = re.search(r"\bCOND(\.\S+)?=(\([^)]*\)+|[^,\s]+)", rest)
            det = {"step": label, "parm": parm.group(2) if parm else None,
                   "cond": cond.group(2) if cond else None}
            if pm and pm.group(2):
                add("jcl-exec-pgm", pm.group(2), lineno, det)
            elif pm:
                add("jcl-exec-proc", pm.group(3) or pm.group(4), lineno, det)
        elif op == "DD":
            if label:
                last_dd = label
            dsn = re.search(r"\bDSN(AME)?=([^,\s]+)", rest)
            disp = re.search(r"\bDISP=(\([^)]*\)|[^,\s]+)", rest)
            det = {"step": last_step, "ddname": last_dd,
                   "disp": disp.group(1) if disp else None,
                   "sysout": bool(re.search(r"\bSYSOUT=", rest)),
                   "dummy": rest.startswith("DUMMY")}
            for k in ("RECFM", "LRECL", "BLKSIZE", "SPACE", "UNIT"):
                km = re.search(r"\b" + k + r"=(\([^)]*\)+|[^,\s]+)", rest)
                if km:
                    det[k.lower()] = km.group(1)
            if "INTRDR" in rest:
                det["internal_reader"] = True
            add("jcl-dd", dsn.group(2) if dsn else None, lineno, det)
        elif op == "INCLUDE":
            im = re.search(r"MEMBER=([^,\s]+)", rest)
            if im:
                add("jcl-include", im.group(1), lineno)
        elif op == "JCLLIB":
            add("jcl-jcllib", rest.strip(), lineno)
        elif op == "SET":
            add("jcl-set", rest.strip(), lineno)


def scan_csd(entry, lines, add):
    text = "\n".join(l.rstrip("\r") for l in lines).upper()
    starts = [m for m in re.finditer(r"^\s*DEFINE\s+(\w+)\s*\(\s*([^)\s]+)\s*\)", text, re.MULTILINE)]
    for idx, m in enumerate(starts):
        end = starts[idx + 1].start() if idx + 1 < len(starts) else len(text)
        block = " ".join(text[m.start():end].split())
        det = {}
        for o in ("GROUP", "PROGRAM", "DSNAME", "TRANSID", "PLAN", "ENTRY", "DESCRIPTION",
                  "TYPE", "DDNAME", "DSNAME01", "TWASIZE", "TASKDATALOC"):
            v = opt(block, o)
            if v:
                det[o.lower()] = v["value"]
        add("csd-" + m.group(1).lower(), m.group(2), text.count("\n", 0, m.start()) + 1, det)


def scan_bms(entry, lines, add):
    for i, raw in enumerate(lines):
        ln = raw.upper()
        if ln.startswith("*"):
            continue
        m = re.match(r"(" + NAME + r")\s+(DFHMSD|DFHMDI)\b", ln)
        if m:
            add("bms-" + m.group(2).lower(), m.group(1), i + 1)
        m = re.match(r"(" + NAME + r")\s+DFHMDF\b", ln)
        if m:
            add("bms-field", m.group(1), i + 1)


def scan_ims(entry, lines, add):
    for i, raw in enumerate(lines):
        ln = raw.upper()[:71]
        if ln.startswith("*"):
            continue
        for kw, kind in (("DBD", "ims-dbd"), ("SEGM", "ims-segment"), ("LCHILD", "ims-lchild"),
                         ("PCB", "ims-pcb"), ("SENSEG", "ims-senseg"), ("PSBGEN", "ims-psbgen"),
                         ("DATASET", "ims-dataset")):
            m = re.match(r"\S*\s+" + kw + r"\s+(.*)", ln)
            if m:
                body = m.group(1)
                nm = re.search(r"\b(NAME|DBDNAME|PSBNAME)=\(?([A-Z0-9@#$]+)", body)
                det = {}
                for k in ("ACCESS", "PARENT", "BYTES", "PROCOPT", "TYPE", "DD1", "LANG", "KEYLEN"):
                    km = re.search(r"\b" + k + r"=(\([^)]*\)+|[^,\s]+)", body)
                    if km:
                        det[k.lower()] = km.group(1)
                add(kind, nm.group(2) if nm else None, i + 1, det)
                break


def scan_sql_text(entry, lines, add):
    text = "\n".join(l.rstrip("\r")[:72] for l in lines).upper()
    for m in re.finditer(r"\bCREATE\s+(UNIQUE\s+)?(TABLE|INDEX|TABLESPACE|DATABASE|VIEW|ALIAS|STOGROUP)\s+(\S+)", text):
        add("sql-create-" + m.group(2).lower(), m.group(3), text.count("\n", 0, m.start()) + 1)
    for m in re.finditer(r"\b(INSERT\s+INTO|DELETE\s+FROM|UPDATE|SELECT\b.*?\bFROM)\s+([A-Z0-9_<>.$#@-]+)", text, re.DOTALL):
        add("sql-dml", m.group(2), text.count("\n", 0, m.start()) + 1, {"op": m.group(1).split()[0]})
    for m in re.finditer(r"\b(REPRO|DEFINE\s+\w+|DELETE)\b", text):
        add("idcams-command", " ".join(m.group(1).split()), text.count("\n", 0, m.start()) + 1)


def scan_script(entry, lines, add):
    for i, raw in enumerate(lines):
        ln = raw.strip()
        if ln.startswith("#"):
            continue
        m = re.search(r"\b(put|submit|SUBMIT)\s+(\S+)", ln)
        if m:
            add("script-submit", m.group(2), i + 1, {"verb": m.group(1)})


def main(argv):
    if len(argv) < 4 or argv[2] != "--out":
        raise SystemExit(__doc__)
    inv_path, out_path = argv[1], argv[3]
    f = open(inv_path, "r", encoding="utf-8")
    try:
        inv = json.load(f)
    finally:
        f.close()
    root = inv["repo_root"]
    refs = []
    counts = {}
    for e in inv["files"]:
        t = e["type"]
        path = os.path.join(root, e["path"])

        def add(kind, target, line, detail=None, _e=e):
            r = {"from": _e["path"], "from_member": _e["member"], "from_type": _e["type"],
                 "kind": kind, "target": target, "line": line}
            if detail:
                r["detail"] = detail
            refs.append(r)
            counts[kind] = counts.get(kind, 0) + 1

        if t in COBOL_TYPES:
            scan_cobol(e, read_lines(path), add)
        elif t in JCL_TYPES:
            scan_jcl(e, read_lines(path), add)
        elif t == "cics-csd":
            scan_csd(e, read_lines(path), add)
        elif t == "bms-mapset":
            scan_bms(e, read_lines(path), add)
        elif t in ("ims-dbd", "ims-psb"):
            scan_ims(e, read_lines(path), add)
        elif t in ("db2-ddl", "control-cards"):
            scan_sql_text(e, read_lines(path), add)
        elif t == "script-shell":
            scan_script(e, read_lines(path), add)
    out = {"schema": "references/1", "inventory": os.path.basename(inv_path),
           "summary": counts, "references": refs}
    d = os.path.dirname(os.path.abspath(out_path))
    if not os.path.isdir(d):
        os.makedirs(d)
    f = open(out_path, "w", encoding="utf-8")
    try:
        json.dump(out, f, indent=1)
    finally:
        f.close()
    sys.stdout.write("references=%d\n" % len(refs))
    for k in sorted(counts):
        sys.stdout.write("  %-22s %d\n" % (k, counts[k]))


if __name__ == "__main__":
    main(sys.argv)
