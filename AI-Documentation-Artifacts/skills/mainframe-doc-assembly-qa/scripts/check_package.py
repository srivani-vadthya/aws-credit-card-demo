"""Validate a generated mainframe documentation package.

Usage:
  python check_package.py <inventory.json> <output_dir> [--json <report.json>]

Checks: artifact coverage, broken relative links, leftover placeholders and
template guide comments, Mermaid conventions, missing Sources sections.
Exit code 1 when any issue is found. Python 3.1+ compatible.
"""
import json
import os
import re
import sys

NOT_DOCUMENTED_TYPES = ("placeholder", "repo-meta", "excluded")
RESERVED_IDS = ("end", "graph", "subgraph", "flowchart")


def load(path):
    f = open(path, "r", encoding="utf-8")
    try:
        return json.load(f)
    finally:
        f.close()


def md_files(root):
    out = []
    for d, dirs, files in os.walk(root):
        dirs.sort()
        for fn in sorted(files):
            if fn.lower().endswith(".md"):
                out.append(os.path.join(d, fn))
    return out


def read(path):
    f = open(path, "r", encoding="utf-8")
    try:
        return f.read()
    finally:
        f.close()


def check_mermaid(block):
    warnings = []
    for ln in block.splitlines():
        s = ln.strip()
        if not s or s.startswith("%%"):
            continue
        if re.match(r"(style|classDef|class|click)\s", s) or ":::" in s:
            warnings.append("styling/click not allowed: " + s[:60])
        for rid in RESERVED_IDS:
            if re.match(r"^" + rid + r"\s*[\[\(\{]", s):
                warnings.append("reserved node id '%s': %s" % (rid, s[:60]))
        m = re.match(r"^([A-Za-z0-9_]+ [A-Za-z0-9_ ]+)\s*[\[\(\{]", s)
        if m and not s.startswith(("subgraph", "participant", "actor", "note", "Note")):
            warnings.append("space in node id: " + s[:60])
        if re.search(r"-->\|[^\"|][^|]*[()\[\]{}][^|]*\|", s):
            warnings.append("unquoted edge label with special chars: " + s[:60])
    return warnings


def main(argv):
    if len(argv) < 3:
        raise SystemExit(__doc__)
    inv = load(argv[1])
    out_dir = argv[2]
    report_path = argv[argv.index("--json") + 1] if "--json" in argv else None
    docs = md_files(out_dir)
    texts = {}
    for p in docs:
        texts[p] = read(p)
    corpus = "\n".join(texts.values()).upper()

    uncovered = []
    for e in inv["files"]:
        if e["type"] in NOT_DOCUMENTED_TYPES:
            continue
        member = e["member"].upper()
        if not re.search(r"(?<![A-Z0-9@#$-])" + re.escape(member) + r"(?![A-Z0-9@#$-])", corpus) \
                and e["path"].upper() not in corpus:
            uncovered.append({"path": e["path"], "type": e["type"]})

    broken, placeholders, guides, mermaid, no_sources = [], [], [], [], []
    for p, t in texts.items():
        rel = os.path.relpath(p, out_dir).replace("\\", "/")
        for m in re.finditer(r"\]\(([^)#\s]+)(#[^)]*)?\)", t):
            target = m.group(1)
            if re.match(r"[a-z]+://", target) or target.startswith("mailto:"):
                continue
            full = os.path.normpath(os.path.join(os.path.dirname(p), target))
            if not os.path.exists(full):
                broken.append({"file": rel, "link": target})
        for m in re.finditer(r"\{\{[^}]+\}\}", t):
            placeholders.append({"file": rel, "text": m.group(0)})
        if "<!-- guide:" in t:
            guides.append(rel)
        for m in re.finditer(r"```mermaid\s*\n(.*?)```", t, re.DOTALL):
            for w in check_mermaid(m.group(1)):
                mermaid.append({"file": rel, "warning": w})
        if not re.search(r"^##\s+Sources\b", t, re.MULTILINE):
            no_sources.append(rel)

    report = {"documents": len(docs), "uncovered_artifacts": uncovered,
              "broken_links": broken, "placeholders": placeholders,
              "template_guides_left": guides, "mermaid_warnings": mermaid,
              "missing_sources_section": no_sources}
    if report_path:
        f = open(report_path, "w", encoding="utf-8")
        try:
            json.dump(report, f, indent=1)
        finally:
            f.close()
    issues = 0
    for k in ("uncovered_artifacts", "broken_links", "placeholders", "template_guides_left",
              "mermaid_warnings", "missing_sources_section"):
        n = len(report[k])
        issues += n
        sys.stdout.write("%-26s %d\n" % (k, n))
        for item in report[k][:50]:
            sys.stdout.write("   - %s\n" % (item if isinstance(item, str) else json.dumps(item)))
    sys.stdout.write("documents=%d issues=%d\n" % (len(docs), issues))
    sys.exit(1 if issues else 0)


if __name__ == "__main__":
    main(sys.argv)
