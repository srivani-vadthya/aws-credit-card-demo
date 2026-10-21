"""Write the review bundle ZIP with forward-slash entry names and explicit directory entries.

Usage: python zip_review_bundle.py <bundle-dir> <zip>

Entries are stored as <bundle-name>/<relative path> in sorted order; every directory,
including the top-level <bundle-name>/, gets its own entry. Compress-Archive in Windows
PowerShell 5 writes backslash separators, which other unzip tools treat as file names.
"""
import os
import sys
import time
import zipfile


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 2
    src, out = os.path.normpath(argv[1]), argv[2]
    top = os.path.basename(src)
    if os.path.exists(out):
        os.remove(out)
    z = zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED)
    n_dirs = n_files = 0
    try:
        for d, ds, fs in os.walk(src):
            ds.sort()
            rel = os.path.relpath(d, os.path.dirname(src)).replace(os.sep, "/")
            info = zipfile.ZipInfo(rel + "/", time.localtime(os.path.getmtime(d))[:6])
            info.external_attr = (0o40755 << 16) | 0x10
            z.writestr(info, b"")
            n_dirs += 1
            for f in sorted(fs):
                p = os.path.join(d, f)
                info = zipfile.ZipInfo(rel + "/" + f, time.localtime(os.path.getmtime(p))[:6])
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                z.writestr(info, open(p, "rb").read())
                n_files += 1
    finally:
        z.close()
    print("zip=%s top=%s/ directories=%d files=%d" % (out, top, n_dirs, n_files))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
