"""Finish a copied review bundle: source snapshot, redaction, link repair, cleanup.

Usage (from the repository root, after the bundle folders were copied):
  python prepare_review_bundle.py <bundle_dir> [--redact <jcl-member> ...]

1. 06-source-snapshot/: every in-scope inventoried text artifact (inventory.json), at its
   repository-relative path, so `path:line` citations can be checked without the repository.
   Not copied: diagrams, binary data, test data files (types diagram, data-binary, data-text)
   and excluded types. Copies are byte-identical except redacted members.
2. Redaction: in each --redact JCL member, in-stream lines that are not JCL statements and do
   not start with a standard FTP command (host, user id, password) are replaced by a marker
   line, keeping the line count. Line numbers and content are listed in REDACTIONS.md
   (line numbers only).
3. Markdown copies in 02-04 whose relative links pointed into the documentation folder are
   rewritten to point at ../01-detailed-documentation/application-documentation/...
4. Compiled Python files and __pycache__ folders are removed.
Python 3.1+ standard library only.
"""
import json
import os
import re
import shutil
import sys

DOCS = "01-detailed-documentation/application-documentation"
REPORT_DIRS = ["02-coverage-validation-report", "03-business-rules-and-traceability", "04-gap-report"]
SKIP_TYPES = ("placeholder", "repo-meta", "excluded", "diagram", "data-binary", "data-text")
FTP_COMMANDS = set("ascii binary bin put get mput mget quit bye close cd lcd locsite site open type mode pwd dir ls".split())
MARKER = "<<REDACTED: in-stream FTP connection line withheld from the review bundle>>"
LINK = re.compile(r"(!?\[[^\]]*\]\()([^)\s]+)(\))")


def rel(p, root):
    return os.path.relpath(p, root).replace("\\", "/")


def snapshot(bundle, redact):
    inv = json.load(open(os.path.join(bundle, "02-coverage-validation-report", "inventory.json"), encoding="utf-8"))
    dst_root = os.path.join(bundle, "06-source-snapshot")
    n, skipped, red = 0, {}, []
    for f in inv["files"]:
        if f["type"] in SKIP_TYPES:
            skipped[f["type"]] = skipped.get(f["type"], 0) + 1
            continue
        if not os.path.isfile(f["path"]):
            raise SystemExit("inventoried file missing: " + f["path"])
        dst = os.path.join(dst_root, f["path"])
        if not os.path.isdir(os.path.dirname(dst)):
            os.makedirs(os.path.dirname(dst))
        if f["path"] in redact:
            raw = open(f["path"], "rb").read()
            nl = "\r\n" if b"\r\n" in raw else "\n"
            lines = raw.decode("latin-1").replace("\r\n", "\n").split("\n")
            for i, l in enumerate(lines):
                s = l.strip()
                if not s or l.startswith("//") or l.startswith("/*") or s.split()[0].lower() in FTP_COMMANDS:
                    continue
                lines[i] = MARKER
                red.append((f["path"], i + 1))
            open(dst, "wb").write(nl.join(lines).encode("latin-1"))
        else:
            shutil.copyfile(f["path"], dst)
        n += 1
    L = ["# Source snapshot", "",
         "Read-only copy of %d in-scope source and definition files from the repository, at their repository-relative paths, "
         "so that every `path:line` citation in this bundle can be opened and checked without the repository. "
         "Each file is byte-identical to the analysed source (sha256 in `../02-coverage-validation-report/inventory.json`) except the redacted lines below." % n, "",
         "Not included (by inventory type): %s. These are listed in the inventory and documented on their pages; they are images, binary data or test data, not code." %
         ", ".join("%s %d" % kv for kv in sorted(skipped.items())), "",
         "## Redactions", "",
         "Lines replaced by `%s`. The original lines hold FTP connection data (host, user id, password) and are deliberately not reproduced anywhere in the bundle. "
         "The line count is unchanged, so citations to other lines still resolve." % MARKER, ""]
    L += ["| File | Line |", "|---|---|"] + ["| `%s` | %d |" % r for r in red] if red else ["None."]
    open(os.path.join(dst_root, "REDACTIONS.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    return n, red


def rewrite_links(path, resolve):
    """Apply resolve(target_path) -> new path or None to every relative link outside code fences."""
    text = open(path, encoding="utf-8").read()
    d = os.path.dirname(path)
    out, fence = [], None

    def fix(m):
        tgt = m.group(2)
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", tgt) or tgt.startswith("#"):
            return m.group(0)
        p, frag = (tgt.split("#", 1) + [""])[:2]
        if os.path.exists(os.path.normpath(os.path.join(d, p))):
            return m.group(0)
        target = resolve(p)
        if not target or not os.path.exists(target):
            return m.group(0)
        return m.group(1) + rel(target, d) + ("#" + frag if frag else "") + m.group(3)
    for l in text.split("\n"):
        f = re.match(r"^\s*(`{3,}|~{3,})", l)
        if fence is None and f:
            fence = f.group(1)
        elif fence is not None:
            if l.strip().startswith(fence) and not l.strip().strip(fence[0]):
                fence = None
        else:
            l = LINK.sub(fix, l)
        out.append(l)
    new = "\n".join(out)
    if new != text:
        open(path, "w", encoding="utf-8", newline="\n").write(new)
        return True
    return False


def repair_links(bundle):
    docs = os.path.join(bundle, DOCS)
    changed = 0
    for rd in REPORT_DIRS:
        base = os.path.join(bundle, rd)
        for d, _, fs in os.walk(base):
            for f in fs:
                if not f.endswith(".md"):
                    continue
                cp = os.path.join(d, f)
                sub = rel(cp, base)
                cands = [os.path.join(dd, ff) for dd, _, ffs in os.walk(docs) for ff in ffs
                         if rel(os.path.join(dd, ff), docs) == sub or rel(os.path.join(dd, ff), docs).endswith("/" + sub)]
                if len(cands) != 1:
                    continue
                odir = os.path.dirname(cands[0])
                if rewrite_links(cp, lambda p, odir=odir: os.path.normpath(os.path.join(odir, p))):
                    changed += 1
    combined = os.path.join(bundle, "01-detailed-documentation", "COMBINED_DOCUMENTATION.md")
    snap = os.path.join(bundle, "06-source-snapshot")
    by_name = {}
    for dd, _, ffs in os.walk(bundle):
        if rel(dd, bundle).startswith("06-source-snapshot"):
            continue
        for ff in ffs:
            by_name.setdefault(ff, []).append(os.path.join(dd, ff))

    def repo_path(p):
        p = p.replace("\\", "/")
        if p.startswith("docs/application-documentation/"):
            return os.path.join(docs, p[len("docs/application-documentation/"):])
        if os.path.exists(os.path.join(snap, p)):
            return os.path.join(snap, p)
        hits = by_name.get(os.path.basename(p.rstrip("/")), [])
        return hits[0] if len(hits) == 1 else None
    if os.path.isfile(combined) and rewrite_links(combined, repo_path):
        changed += 1
    return changed


def cleanup(bundle):
    removed = []
    for d, dirs, fs in os.walk(bundle, topdown=False):
        for f in fs:
            if f.endswith((".pyc", ".pyo")) or f.startswith("_tmp") or f in ("Thumbs.db", ".DS_Store"):
                os.remove(os.path.join(d, f))
                removed.append(rel(os.path.join(d, f), bundle))
        if os.path.basename(d) == "__pycache__":
            shutil.rmtree(d)
            removed.append(rel(d, bundle) + "/")
    return removed


def main(argv):
    if len(argv) < 2:
        raise SystemExit(__doc__)
    bundle = argv[1]
    redact = [argv[i + 1] for i, a in enumerate(argv) if a == "--redact"]
    n, red = snapshot(bundle, redact)
    changed = repair_links(bundle)
    removed = cleanup(bundle)
    sys.stdout.write("snapshot_files=%d redacted_lines=%d link_repaired_files=%d removed=%d %s\n" % (n, len(red), changed, len(removed), " ".join(removed)))


if __name__ == "__main__":
    main(sys.argv)
