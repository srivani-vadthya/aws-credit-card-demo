"""Compute a byte-level layout (offset, length, type) for a COBOL copybook.

Usage:
  python copybook_layout.py <copybook-file> [--free] [--json <out.json>] [--md <out.md>]

- Fixed format (columns 8-72) by default; --free for free-format source.
- Handles PIC/PICTURE, USAGE (DISPLAY, COMP, COMP-3, COMP-4, COMP-5,
  BINARY, PACKED-DECIMAL, COMP-1, COMP-2, POINTER, INDEX), SIGN SEPARATE,
  OCCURS n [TO m] [DEPENDING ON x], REDEFINES, level 66/77/88, FILLER.
- OCCURS DEPENDING ON lengths are reported at their maximum.
- SYNCHRONIZED slack bytes are NOT added; flagged instead.
Python 3.1+ compatible.
"""
import json
import re
import sys


def read_source(path, free):
    f = open(path, "rb")
    try:
        raw = f.read().decode("latin-1")
    finally:
        f.close()
    out = []
    for i, ln in enumerate(raw.splitlines()):
        ln = ln.rstrip("\r")
        if free:
            s = ln.strip()
            if s.startswith("*"):
                continue
            code = ln
        else:
            if len(ln) < 7 or ln[6] in "*/dD":
                continue
            code = ln[7:72]
        k = code.find("*>")
        if k >= 0:
            code = code[:k]
        out.append((i + 1, code))
    return out


def sentences(lines):
    """Split into period-terminated data description entries with start line."""
    buf = []
    start = None
    for lineno, code in lines:
        text = code
        while text:
            m = re.search(r"\.(\s|$)", text)
            if start is None and text.strip():
                start = lineno
            if m and not _inside_literal("".join(buf) + text[:m.start()]):
                buf.append(text[:m.start()])
                entry = " ".join("".join(buf).split())
                if entry:
                    yield start, entry
                buf = []
                start = None
                text = text[m.end():]
            else:
                buf.append(text + " ")
                text = ""
    if buf and "".join(buf).strip():
        yield start, " ".join("".join(buf).split())


def _inside_literal(s):
    return (s.count("'") % 2 == 1) or (s.count('"') % 2 == 1)


def expand_pic(pic):
    out = []
    i = 0
    while i < len(pic):
        c = pic[i]
        if i + 1 < len(pic) and pic[i + 1] == "(":
            j = pic.index(")", i)
            out.append(c * int(pic[i + 2:j]))
            i = j + 1
        else:
            out.append(c)
            i += 1
    return "".join(out)


def pic_info(pic):
    p = expand_pic(pic.upper())
    signed = p.startswith("S")
    body = p.replace("S", "", 1) if signed else p
    digits = sum(1 for c in body if c in "9P")
    implied = body.replace("P", "").replace("V", "")
    display_len = len(implied)
    scale = 0
    if "V" in body:
        scale = len([c for c in body.split("V", 1)[1] if c == "9"])
    if set(body) <= set("X"):
        cat = "alphanumeric"
    elif set(body) <= set("A"):
        cat = "alphabetic"
    elif set(body) <= set("9VPS"):
        cat = "numeric"
    elif set(body) <= set("N"):
        cat = "national"
    else:
        cat = "numeric-edited" if any(c in body for c in "Z*.,+-$CRDB0B/") else "alphanumeric"
    return {"expanded": p, "signed": signed, "digits": digits, "scale": scale,
            "display_len": display_len, "category": cat}


def storage_len(info, usage, sign_separate):
    u = usage or "DISPLAY"
    if u in ("COMP-1",):
        return 4
    if u in ("COMP-2",):
        return 8
    if u in ("POINTER", "INDEX", "PROCEDURE-POINTER", "FUNCTION-POINTER"):
        return 4
    if info is None:
        return 0
    if u in ("COMP", "COMP-4", "COMP-5", "BINARY"):
        d = info["digits"]
        return 2 if d <= 4 else 4 if d <= 9 else 8
    if u in ("COMP-3", "PACKED-DECIMAL"):
        return info["digits"] // 2 + 1
    if info["category"] == "national":
        return info["display_len"] * 2
    return info["display_len"] + (1 if sign_separate else 0)


USAGE_RE = r"\b(COMPUTATIONAL-[1-5]|COMP-[1-5]|COMPUTATIONAL|COMP|BINARY|PACKED-DECIMAL|DISPLAY|POINTER|INDEX|NATIONAL)\b"


def parse_entry(text):
    m = re.match(r"(\d{1,2})\s+([A-Z0-9][A-Z0-9-]*)?(.*)$", text.upper())
    if not m:
        return None
    level = int(m.group(1))
    name = m.group(2) or "FILLER"
    rest = m.group(3)
    if name in ("PIC", "PICTURE", "REDEFINES", "OCCURS", "VALUE", "VALUES", "USAGE", "COMP", "COMP-3"):
        rest = name + rest
        name = "FILLER"
    e = {"level": level, "name": name, "raw": text}
    pm = re.search(r"\bPIC(TURE)?\s+(IS\s+)?(\S+)", rest)
    if pm:
        e["pic"] = pm.group(3)
    um = re.search(USAGE_RE, rest)
    if um:
        u = um.group(1).replace("COMPUTATIONAL", "COMP")
        if u == "COMP-4":
            u = "COMP"
        e["usage"] = u
    rm = re.search(r"\bREDEFINES\s+([A-Z0-9-]+)", rest)
    if rm:
        e["redefines"] = rm.group(1)
    om = re.search(r"\bOCCURS\s+(\d+)(\s+TO\s+(\d+))?(\s+TIMES)?(.*?)(DEPENDING\s+ON\s+([A-Z0-9-]+))?", rest)
    if om:
        e["occurs_min"] = int(om.group(1))
        e["occurs"] = int(om.group(3)) if om.group(3) else int(om.group(1))
        if om.group(7):
            e["depending_on"] = om.group(7)
    vm = re.search(r"\bVALUES?\s+(ARE\s+|IS\s+)?(.+)$", rest)
    if vm:
        e["value"] = vm.group(2).strip()
    if re.search(r"\bSIGN\s+(IS\s+)?(LEADING|TRAILING)\s+SEPARATE", rest) or re.search(r"\bSEPARATE\b", rest):
        e["sign_separate"] = True
    if re.search(r"\bSYNC(HRONIZED)?\b", rest):
        e["sync"] = True
    if re.search(r"\bRENAMES\b", rest):
        e["renames"] = True
    return e


def build_tree(entries):
    root = {"level": 0, "name": "(root)", "children": []}
    stack = [root]
    for e in entries:
        if e["level"] == 88:
            stack[-1].setdefault("conditions", []).append(
                {"name": e["name"], "value": e.get("value"), "line": e["line"]})
            continue
        if e["level"] == 66:
            root.setdefault("renames", []).append(e)
            continue
        lvl = 1 if e["level"] == 77 else e["level"]
        while len(stack) > 1 and stack[-1]["level"] >= lvl:
            stack.pop()
        e["children"] = []
        stack[-1]["children"].append(e)
        stack.append(e)
    return root


def compute(node, offset, by_name, notes):
    if "redefines" in node and node["redefines"] in by_name:
        offset = by_name[node["redefines"]]["offset"]
    node["offset"] = offset
    by_name[node["name"]] = node
    if node.get("sync"):
        notes.append("SYNC on %s: slack bytes not computed" % node["name"])
    if node["children"]:
        cur = offset
        end = offset
        for ch in node["children"]:
            compute(ch, cur, by_name, notes)
            ch_end = ch["offset"] + ch["total_length"]
            if "redefines" not in ch:
                cur = ch_end
            end = max(end, ch_end)
        unit = end - offset
        node["type"] = "group"
    else:
        info = pic_info(node["pic"]) if "pic" in node else None
        unit = storage_len(info, node.get("usage"), node.get("sign_separate"))
        if info:
            node["category"] = info["category"]
            node["digits"] = info["digits"]
            node["scale"] = info["scale"]
            node["signed"] = info["signed"]
        node["type"] = "elementary"
        if unit == 0 and "pic" not in node:
            notes.append("No PIC/size for %s (line %s)" % (node["name"], node.get("line")))
    node["length"] = unit
    node["total_length"] = unit * node.get("occurs", 1)


def flatten(node, depth, rows):
    for ch in node["children"]:
        rows.append({
            "level": ch["level"], "name": ch["name"], "depth": depth,
            "offset": ch["offset"] + 1, "end": ch["offset"] + ch["total_length"],
            "length": ch["length"], "occurs": ch.get("occurs"), "occurs_min": ch.get("occurs_min"),
            "depending_on": ch.get("depending_on"), "total_length": ch["total_length"],
            "pic": ch.get("pic"), "usage": ch.get("usage") or ("DISPLAY" if ch.get("pic") else None),
            "category": ch.get("category"), "signed": ch.get("signed"), "scale": ch.get("scale"),
            "redefines": ch.get("redefines"), "value": ch.get("value"), "line": ch.get("line"),
            "conditions": ch.get("conditions", []),
        })
        flatten(ch, depth + 1, rows)


def main(argv):
    if len(argv) < 2:
        raise SystemExit(__doc__)
    path = argv[1]
    free = "--free" in argv
    out_json = argv[argv.index("--json") + 1] if "--json" in argv else None
    out_md = argv[argv.index("--md") + 1] if "--md" in argv else None
    entries = []
    for line, text in sentences(read_source(path, free)):
        if not re.match(r"\d{1,2}\s", text):
            continue
        e = parse_entry(text)
        if e:
            e["line"] = line
            entries.append(e)
    root = build_tree(entries)
    notes = []
    if root["children"] and all(c["level"] not in (1, 77) for c in root["children"]):
        # Copybook starts below level 01 (it is COPY'd into a caller's group):
        # lay its top-level items out consecutively as one implicit record.
        root["children"] = [{"level": 1, "name": "(FRAGMENT)", "children": root["children"],
                             "line": root["children"][0].get("line")}]
        notes.append("Copybook has no 01 level; offsets are relative to the COPY position")
    by_name = {}
    records = []
    for rec in root["children"]:
        compute(rec, 0, by_name, notes)
        rows = []
        flatten({"children": [rec]}, 0, rows)
        records.append({"name": rec["name"], "length": rec["total_length"], "line": rec.get("line"),
                        "redefines": rec.get("redefines"), "fields": rows})
    result = {"schema": "copybook-layout/1", "source": path.replace("\\", "/"),
              "records": records, "notes": notes,
              "conventions": "offset/end are 1-based byte positions; ODO at maximum"}
    if out_json:
        f = open(out_json, "w", encoding="utf-8")
        try:
            json.dump(result, f, indent=1)
        finally:
            f.close()
    md = []
    for r in records:
        md.append("### %s (length %d)\n" % (r["name"], r["length"]))
        md.append("| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |")
        md.append("|---|---|---|---|---|---|---|---|---|---|")
        for x in r["fields"]:
            occ = ""
            if x["occurs"]:
                occ = str(x["occurs"]) if not x["depending_on"] else "%s-%s DEP %s" % (
                    x["occurs_min"], x["occurs"], x["depending_on"])
            md.append("| %02d | %s%s | %d | %d | %d | %s | %s | %s | %s | %s |" % (
                x["level"], "&nbsp;&nbsp;" * x["depth"], x["name"], x["offset"], x["end"],
                x["length"], occ, x["pic"] or "", x["usage"] or "", x["redefines"] or "", x["line"]))
            for c in x["conditions"]:
                md.append("| 88 | %s%s = %s |  |  |  |  |  |  |  | %s |" % (
                    "&nbsp;&nbsp;" * (x["depth"] + 1), c["name"], c["value"], c["line"]))
        md.append("")
    if notes:
        md.append("Notes: " + "; ".join(notes))
    text = "\n".join(md) + "\n"
    if out_md:
        f = open(out_md, "w", encoding="utf-8")
        try:
            f.write(text)
        finally:
            f.close()
    if not out_json and not out_md:
        sys.stdout.write(text)
    else:
        for r in records:
            sys.stdout.write("%s length=%d fields=%d\n" % (r["name"], r["length"], len(r["fields"])))


if __name__ == "__main__":
    main(sys.argv)
