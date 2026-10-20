"""Fail if in-stream FTP data (host, user id, password) from a JCL member appears in shared outputs.

Usage: python check_instream_secrets.py <jcl-member> <file-or-dir> [<file-or-dir> ...]

Only line numbers and hit counts are printed, never line content. In-stream lines whose
first word is a standard FTP command (ascii, put, quit, ...) are allowed to appear.
Exit code 1 when any other in-stream line is found in an output file.
"""
import os
import sys

FTP_COMMANDS = set("ascii binary bin put get mput mget quit bye close cd lcd locsite site "
                   "open type mode pwd dir ls".split())
TEXT_EXT = (".md", ".json", ".txt", ".yaml", ".yml", ".ps1", ".py", ".mdc", ".csv", ".html")


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    member, roots = argv[1], argv[2:]
    src = [l.rstrip("\r\n") for l in open(member, encoding="latin-1")]
    secret = []
    for i, l in enumerate(src):
        s = l.strip()
        if not s or l.startswith("//") or l.startswith("/*"):
            continue
        if s.split()[0].lower() in FTP_COMMANDS:
            continue
        secret.append((i + 1, s))
    files = []
    for r in roots:
        if os.path.isfile(r):
            files.append(r)
        elif os.path.isdir(r):
            for d, _, fs in os.walk(r):
                files.extend(os.path.join(d, f) for f in fs if f.lower().endswith(TEXT_EXT))
    bad = 0
    for n, s in secret:
        hits = []
        for f in files:
            if s in open(f, encoding="utf-8", errors="replace").read():
                hits.append(f)
        print("%s:%d hits=%d" % (member.replace("\\", "/"), n, len(hits)))
        for f in hits:
            print("  found in %s" % f.replace("\\", "/"))
        bad += len(hits)
    print("checked_lines=%d files=%d findings=%d" % (len(secret), len(files), bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
