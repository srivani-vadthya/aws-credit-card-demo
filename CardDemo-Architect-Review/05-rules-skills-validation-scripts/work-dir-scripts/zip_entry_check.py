"""Report raw ZIP entry names from the central directory (no path normalisation).

Usage: python zip_entry_check.py <zip> <top-level-dir>
Exit code 1 when an entry name contains a backslash or lies outside <top-level-dir>/.
"""
import struct
import sys


def raw_names(path):
    data = open(path, "rb").read()
    end = data.rfind(b"PK\x05\x06")
    if end < 0:
        raise ValueError("no end of central directory record")
    count, size, offset = struct.unpack("<HII", data[end + 10:end + 20])
    names, pos = [], offset
    for _ in range(count):
        if data[pos:pos + 4] != b"PK\x01\x02":
            raise ValueError("bad central directory entry at %d" % pos)
        n, m, k = struct.unpack("<HHH", data[pos + 28:pos + 34])
        names.append(data[pos + 46:pos + 46 + n].decode("utf-8", "replace"))
        pos += 46 + n + m + k
    return names


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 2
    names = raw_names(argv[1])
    top = argv[2].rstrip("/") + "/"
    back = [x for x in names if "\\" in x]
    outside = [x for x in names if not x.startswith(top)]
    dirs = [x for x in names if x.endswith("/")]
    print("entries=%d files=%d directories=%d backslash_entries=%d outside_top_level=%d top_level_entry=%s" % (
        len(names), len(names) - len(dirs), len(dirs), len(back), len(outside), "yes" if top in names else "no"))
    for x in (back + outside)[:5]:
        print("  bad entry: %s" % x)
    return 1 if back or outside or top not in names else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
