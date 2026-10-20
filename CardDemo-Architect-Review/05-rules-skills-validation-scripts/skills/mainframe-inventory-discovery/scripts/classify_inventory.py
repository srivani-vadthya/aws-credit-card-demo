"""Classify every file in a mainframe repository by content signature.

Usage:
  python classify_inventory.py <repo_root> --out <inventory.json>
         [--signatures <signatures.json>] [--exclude <glob>]...
         [--module <id>=<glob>]... [--skip-dir <name>]...

Compatible with Python 3.1+ and no third-party packages.
"""
import hashlib
import json
import os
import re
import sys

SAMPLE_BYTES = 65536
DEFAULT_SKIP_DIRS = [".git", ".svn", ".hg", "node_modules", ".cursor"]


def parse_args(argv):
    opts = {"root": None, "out": None, "signatures": None,
            "exclude": [], "module": [], "skip_dir": list(DEFAULT_SKIP_DIRS)}
    i = 1
    while i < len(argv):
        a = argv[i]
        if a in ("--out", "--signatures", "--exclude", "--module", "--skip-dir"):
            if i + 1 >= len(argv):
                raise SystemExit("Missing value for " + a)
            key = a[2:].replace("-", "_")
            if isinstance(opts[key], list):
                opts[key].append(argv[i + 1])
            else:
                opts[key] = argv[i + 1]
            i += 2
        elif opts["root"] is None:
            opts["root"] = a
            i += 1
        else:
            raise SystemExit("Unexpected argument: " + a)
    if not opts["root"] or not opts["out"]:
        raise SystemExit(__doc__)
    if not opts["signatures"]:
        opts["signatures"] = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                          "signatures.json")
    return opts


def glob_to_regex(pattern):
    """Translate a glob with ** support into a compiled regex (case-insensitive)."""
    pattern = pattern.replace("\\", "/")
    out = []
    i = 0
    while i < len(pattern):
        c = pattern[i]
        if c == "*":
            if pattern[i:i + 3] == "**/":
                out.append("(?:.*/)?")
                i += 3
                continue
            if pattern[i:i + 2] == "**":
                out.append(".*")
                i += 2
                continue
            out.append("[^/]*")
        elif c == "?":
            out.append("[^/]")
        elif c == "{":
            j = pattern.find("}", i)
            if j == -1:
                out.append(re.escape(c))
            else:
                alts = pattern[i + 1:j].split(",")
                out.append("(?:" + "|".join(re.escape(x) for x in alts) + ")")
                i = j + 1
                continue
        else:
            out.append(re.escape(c))
        i += 1
    return re.compile("^" + "".join(out) + "$", re.IGNORECASE)


def detect_encoding(data):
    if not data:
        return "empty"
    if b"\x00" in data:
        return "binary"
    sample = data[:8192]
    total = float(len(sample))
    printable = 0
    ebcdic_like = 0
    ascii_letters = 0
    for b in bytearray(sample):
        if b in (9, 10, 13) or 32 <= b <= 126:
            printable += 1
        if 65 <= b <= 90 or 97 <= b <= 122:
            ascii_letters += 1
        if b == 0x40 or 0xC1 <= b <= 0xE9 or 0xF0 <= b <= 0xF9 or 0x81 <= b <= 0xA9:
            ebcdic_like += 1
    if printable / total >= 0.95:
        return "ascii"
    if ebcdic_like / total > 0.5 and ascii_letters / total < 0.2:
        return "ebcdic"
    if printable / total < 0.7:
        return "binary"
    return "ascii-with-high-bytes"


def text_format(text):
    lines = text.splitlines()
    max_len = 0
    long_lines = 0
    seq_numeric = 0
    tabs = 0
    for ln in lines:
        n = len(ln.rstrip("\r"))
        if n > max_len:
            max_len = n
        if "\t" in ln:
            tabs += 1
        if n >= 80:
            long_lines += 1
            tail = ln[72:80].strip()
            if tail and tail.isdigit():
                seq_numeric += 1
    return {
        "line_count": len(lines),
        "max_line_length": max_len,
        "has_tabs": tabs > 0,
        "sequence_area": bool(long_lines) and seq_numeric * 2 >= long_lines,
        "lines_with_numeric_cols_73_80": seq_numeric,
    }


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def compile_signatures(path):
    f = open(path, "r", encoding="utf-8")
    try:
        cfg = json.load(f)
    finally:
        f.close()
    sigs = []
    for s in cfg["signatures"]:
        e = dict(s)
        if "regex" in s:
            e["_re"] = re.compile(s["regex"], re.MULTILINE)
        if "requires" in s:
            e["_req"] = re.compile(s["requires"], re.MULTILINE)
        if "excludes" in s:
            e["_exc"] = re.compile(s["excludes"], re.MULTILINE)
        if "name_requires" in s:
            e["_nreq"] = re.compile(s["name_requires"])
        if "name" in s:
            e["_name"] = re.compile(s["name"])
        if "ext" in s:
            e["_ext"] = set(x.lower() for x in s["ext"])
        sigs.append(e)
    return cfg, sigs


def classify(name, ext, data, encoding, text_upper, sigs, binary_types):
    # Name and empty checks first, then binary short-circuit, then content, then extension.
    for s in sigs:
        if "_name" in s and s["_name"].search(name.upper()):
            return s["type"], "name:" + s["name"], None
        if s.get("empty") and encoding == "empty":
            return s["type"], "empty-file", None
    for s in sigs:
        if "_ext" in s and "regex" not in s and ext in s["_ext"] and s["type"] in (
                "archive", "diagram", "documentation"):
            return s["type"], "ext:" + ext, None
    if encoding in binary_types:
        return binary_types[encoding], "encoding:" + encoding, None
    for s in sigs:
        if "_re" in s:
            m = s["_re"].search(text_upper)
            if not m:
                continue
            if "_req" in s and not s["_req"].search(text_upper):
                continue
            if "_exc" in s and s["_exc"].search(text_upper):
                continue
            if "_nreq" in s and not s["_nreq"].search(name.upper()):
                continue
            return s["type"], "regex:" + s["regex"][:60], line_of(text_upper, m.start())
    for s in sigs:
        if "_ext" in s and "regex" not in s and ext in s["_ext"]:
            return s["type"], "ext:" + ext, None
    return "unclassified", None, None


def main(argv):
    opts = parse_args(argv)
    root = os.path.abspath(opts["root"])
    cfg, sigs = compile_signatures(opts["signatures"])
    binary_types = cfg.get("binary_types", {})
    excludes = [(g, glob_to_regex(g)) for g in opts["exclude"]]
    modules = []
    for m in opts["module"]:
        if "=" not in m:
            raise SystemExit("--module expects id=glob, got " + m)
        mid, g = m.split("=", 1)
        modules.append((mid, g, glob_to_regex(g)))
    skip = set(d.lower() for d in opts["skip_dir"])

    files = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d.lower() not in skip)
        for fn in sorted(filenames):
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, root).replace("\\", "/")
            ext = fn.rsplit(".", 1)[1].lower() if "." in fn.lstrip(".") else ""
            f = open(full, "rb")
            try:
                data = f.read()
            finally:
                f.close()
            entry = {
                "path": rel,
                "name": fn,
                "member": fn.rsplit(".", 1)[0].upper() if "." in fn.lstrip(".") else fn.upper(),
                "ext": ext,
                "size": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
                "module": None,
                "analysis_status": "pending",
            }
            exc = [g for g, rx in excludes if rx.match(rel)]
            sample = data[:SAMPLE_BYTES]
            encoding = detect_encoding(sample)
            entry["encoding"] = encoding
            if exc:
                entry["type"] = "excluded"
                entry["classified_by"] = "exclude:" + exc[0]
                entry["analysis_status"] = "excluded"
            else:
                text = sample.decode("latin-1")
                t, by, line = classify(fn, ext, sample, encoding, text.upper(), sigs, binary_types)
                entry["type"] = t
                entry["classified_by"] = by
                entry["evidence_line"] = line
                if encoding in ("ascii", "ascii-with-high-bytes"):
                    entry["format"] = text_format(data.decode("latin-1"))
                if t in ("diagram", "archive", "data-binary", "placeholder", "repo-meta"):
                    entry["analysis_status"] = "not-analyzable"
            best = None
            for mid, g, rx in modules:
                if rx.match(rel) and (best is None or len(g) > len(best[1])):
                    best = (mid, g)
            if best:
                entry["module"] = best[0]
            files.append(entry)

    by_type = {}
    for e in files:
        by_type[e["type"]] = by_type.get(e["type"], 0) + 1
    by_module = {}
    for e in files:
        k = e["module"] or "(none)"
        by_module[k] = by_module.get(k, 0) + 1
    seq_files = [e["path"] for e in files if e.get("format", {}).get("sequence_area")]
    inventory = {
        "schema": "inventory/1",
        "generated_by": "mainframe-inventory-discovery/classify_inventory.py",
        "repo_root": root.replace("\\", "/"),
        "options": {"exclude": opts["exclude"], "module": opts["module"],
                    "signatures": os.path.basename(opts["signatures"])},
        "summary": {
            "file_count": len(files),
            "by_type": by_type,
            "by_module": by_module,
            "files_with_sequence_area": seq_files,
        },
        "unclassified": [e["path"] for e in files if e["type"] == "unclassified"],
        "files": files,
    }
    out_dir = os.path.dirname(os.path.abspath(opts["out"]))
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)
    f = open(opts["out"], "w", encoding="utf-8")
    try:
        json.dump(inventory, f, indent=2, sort_keys=False)
    finally:
        f.close()
    sys.stdout.write("files=%d unclassified=%d\n" % (len(files), len(inventory["unclassified"])))
    for t in sorted(by_type):
        sys.stdout.write("  %-22s %d\n" % (t, by_type[t]))
    for p in inventory["unclassified"]:
        sys.stdout.write("  UNCLASSIFIED: %s\n" % p)


if __name__ == "__main__":
    main(sys.argv)
