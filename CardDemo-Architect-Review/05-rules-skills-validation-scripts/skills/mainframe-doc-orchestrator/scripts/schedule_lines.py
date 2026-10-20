#!/usr/bin/env python
"""Add source line numbers to Control-M facts in <work_dir>/batch/schedule.json.

Usage: schedule_lines.py <work_dir> [--repo .]

For every Control-M edge the OUTCOND SIGN="+" line of the predecessor job
becomes `source` and the INCOND line of the successor job becomes
`incond_source`. Every Control-M job record gets the line of its JOB tag.
Jobs are located by enclosing FOLDER / SMART_FOLDER FOLDER_NAME and JOBNAME.
Facts that cannot be located exactly once are left unchanged and listed.
Standard library only; Python 3.1 compatible.
"""
import json
import os
import re
import sys

ATTR = re.compile(r'(\w+)="([^"]*)"')


def attrs(line):
    return dict(ATTR.findall(line))


def scan(path):
    """Return {(folder, job): {"job": n, "in": {name: [n]}, "out+": {name: [n]}}}."""
    jobs = {}
    folder = None
    cur = None
    f = open(path, encoding="utf-8-sig", errors="replace")
    try:
        for n, line in enumerate(f, 1):
            s = line.strip()
            if s.startswith("<FOLDER ") or s.startswith("<SMART_FOLDER "):
                folder = attrs(s).get("FOLDER_NAME")
                cur = None
            elif s.startswith("<JOB "):
                key = (folder, attrs(s).get("JOBNAME"))
                cur = jobs.setdefault(key, {"job": [], "in": {}, "out+": {}})
                cur["job"].append(n)
            elif s.startswith("</JOB>"):
                cur = None
            elif cur is not None and s.startswith("<INCOND "):
                cur["in"].setdefault(attrs(s).get("NAME"), []).append(n)
            elif cur is not None and s.startswith("<OUTCOND "):
                a = attrs(s)
                if a.get("SIGN") == "+":
                    cur["out+"].setdefault(a.get("NAME"), []).append(n)
    finally:
        f.close()
    return jobs


def has_line(src):
    return bool(src) and re.search(r":\d+(-\d+)?$", src) is not None


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    work = argv[1]
    repo = "."
    if "--repo" in argv:
        repo = argv[argv.index("--repo") + 1]
    spath = os.path.join(work, "batch", "schedule.json")
    sched = json.load(open(spath, encoding="utf-8-sig"))
    cache = {}
    unresolved = []
    changed = 0

    def jobs_for(src):
        rel = src.split(":")[0]
        if rel not in cache:
            cache[rel] = scan(os.path.join(repo, rel))
        return rel, cache[rel]

    for e in sched.get("controlm_edges", []):
        rel, jobs = jobs_for(e["source"])
        cond = e.get("condition")
        frm = jobs.get((e.get("from_folder"), e.get("from")), {})
        to = jobs.get((e.get("to_folder"), e.get("to")), {})
        out_lines = frm.get("out+", {}).get(cond, [])
        in_lines = to.get("in", {}).get(cond, [])
        if len(out_lines) == 1 and len(in_lines) == 1:
            new = "%s:%d" % (rel, out_lines[0])
            inc = "%s:%d" % (rel, in_lines[0])
            if e.get("source") != new or e.get("incond_source") != inc:
                e["source"], e["incond_source"] = new, inc
                changed += 1
        elif not has_line(e.get("source")):
            unresolved.append("edge %s -> %s (%s): OUTCOND+ lines %s, INCOND lines %s"
                              % (e.get("from"), e.get("to"), cond, out_lines, in_lines))

    for j in sched.get("controlm_jobs", []):
        rel, jobs = jobs_for(j["source"])
        lines = jobs.get((j.get("folder"), j.get("job")), {}).get("job", [])
        if len(lines) == 1:
            new = "%s:%d" % (rel, lines[0])
            if j.get("source") != new:
                j["source"] = new
                changed += 1
        elif not has_line(j.get("source")):
            unresolved.append("job %s in %s: JOB lines %s" % (j.get("job"), j.get("folder"), lines))

    out = open(spath, "w", encoding="utf-8")
    try:
        json.dump(sched, out, indent=2, ensure_ascii=False)
    finally:
        out.close()
    print("controlm facts updated=%d unresolved=%d" % (changed, len(unresolved)))
    for u in unresolved:
        print("  UNRESOLVED " + u)
    return 1 if unresolved else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
