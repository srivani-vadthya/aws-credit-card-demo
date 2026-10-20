"""Independent verification of the CardDemo architect review bundle.

Usage:
  python verify_review_bundle.py <bundle_dir> [--repo <repository_root>] [--no-write]

Runs inside the bundle with no other input (sources come from 06-source-snapshot/). With
--repo it also compares the snapshot with the repository and checks that the original FTP
connection lines appear nowhere in the bundle. It does not reuse the pipeline's parsers:
counts come from file extensions and JCL JOB cards, paragraph spans from Area A labels.

Writes 02-coverage-validation-report/bundle-verification.{md,json} unless --no-write.
Exit code 1 when a hard check fails; warnings do not fail.
Python 3.1+ standard library only.
"""
import hashlib
import json
import os
import re
import sys
import time
import zipfile

DOCS = "01-detailed-documentation/application-documentation"
SNAP = "06-source-snapshot"
OUTPUTS = ("02-coverage-validation-report/bundle-verification.md", "02-coverage-validation-report/bundle-verification.json")
FTP_COMMANDS = set("ascii binary bin put get mput mget quit bye close cd lcd locsite site open type mode pwd dir ls".split())
REF = re.compile(r"`([A-Za-z0-9_./-]+\.[A-Za-z0-9]+):(\d+)(?:-(\d+))?`")
LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


class Result(object):
    def __init__(self):
        self.checks = []

    def add(self, cid, name, ok, measured, detail=None, hard=True):
        self.checks.append({"id": cid, "check": name, "status": "pass" if ok else ("FAIL" if hard else "warn"),
                            "measured": measured, "detail": detail or []})


def read_lines(path):
    f = open(path, "rb")
    try:
        t = f.read().decode("latin-1")
    finally:
        f.close()
    parts = t.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    if parts and parts[-1] == "":
        parts.pop()
    return parts


def text(path):
    f = open(path, "r", encoding="utf-8", errors="replace")
    try:
        return f.read()
    finally:
        f.close()


def load(path):
    f = open(path, "r", encoding="utf-8-sig")
    try:
        return json.load(f)
    finally:
        f.close()


def walk(root, exts=None):
    for d, dirs, fs in os.walk(root):
        dirs.sort()
        for f in sorted(fs):
            if exts is None or f.lower().endswith(exts):
                yield os.path.join(d, f)


def rel(p, root):
    return os.path.relpath(p, root).replace("\\", "/")


def slug(h):
    h = re.sub(r"<[^>]+>", "", h).strip().lower()
    h = re.sub(r"[`*_~]", lambda m: "_" if m.group(0) == "_" else "", h)
    h = re.sub(r"[^\w\- ]", "", h)
    return h.replace(" ", "-")


def anchors_of(t):
    out = set(re.findall(r"<a\s+(?:id|name)=\"([^\"]+)\"", t))
    seen = {}
    fence = False
    for l in t.split("\n"):
        if l.startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        m = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", l)
        if m:
            s = slug(m.group(2))
            if s in seen:
                seen[s] += 1
                out.add("%s-%d" % (s, seen[s]))
            else:
                seen[s] = 0
                out.add(s)
    return out


def strip_code(t):
    """Drop fenced blocks (``` or ~~~, any length) and inline code spans."""
    out, fence = [], None
    for l in t.split("\n"):
        m = re.match(r"^\s*(`{3,}|~{3,})", l)
        if fence is None and m:
            fence = m.group(1)
            continue
        if fence is not None:
            if l.strip().startswith(fence[0] * len(fence)) and not l.strip().strip(fence[0]):
                fence = None
            continue
        out.append(re.sub(r"`[^`\n]*`", "", l))
    return "\n".join(out)


def cobol_labels(lines):
    """[(line_no, NAME)] for paragraph/section labels starting in Area A (columns 8-11)."""
    out = []
    for i, l in enumerate(lines):
        if len(l) < 8 or l[6:7] in ("*", "/", "-"):
            continue
        area_a = l[7:11]
        if not area_a.strip() or area_a[0] == " " and not area_a.strip():
            continue
        body = l[7:72].strip()
        m = re.match(r"^([A-Z0-9][A-Z0-9-]*)(\s+SECTION)?\s*\.\s*$", body, re.I)
        if m and m.group(1).upper() not in ("PROCEDURE", "DATA", "WORKING-STORAGE", "LINKAGE", "FILE", "ENVIRONMENT", "IDENTIFICATION",
                                             "CONFIGURATION", "INPUT-OUTPUT", "LOCAL-STORAGE", "FILE-CONTROL", "I-O-CONTROL", "END"):
            out.append((i + 1, m.group(1).upper()))
    return out


def main(argv):
    if len(argv) < 2:
        raise SystemExit(__doc__)
    B = os.path.abspath(argv[1])
    repo = os.path.abspath(argv[argv.index("--repo") + 1]) if "--repo" in argv else None
    write = "--no-write" not in argv
    R = Result()
    snap = os.path.join(B, SNAP)
    docs = os.path.join(B, DOCS)
    inv = load(os.path.join(B, "02-coverage-validation-report", "inventory.json"))
    cov = load(os.path.join(B, "02-coverage-validation-report", "coverage.json"))
    chk = load(os.path.join(B, "02-coverage-validation-report", "check_package.json"))
    gaps = load(os.path.join(B, "04-gap-report", "gaps.json"))
    rules = load(os.path.join(B, "03-business-rules-and-traceability", "rules.json"))["rules"]
    metrics = {}

    # ---------------------------------------------------------------- V1 source inventory recount
    src = [rel(p, snap) for p in walk(snap) if not p.endswith("REDACTIONS.md")]

    def ext(p):
        return os.path.splitext(p)[1].lower()
    groups = {
        "COBOL programs (.cbl)": [p for p in src if ext(p) == ".cbl"],
        "COBOL copybooks (.cpy outside cpy-bms)": [p for p in src if ext(p) == ".cpy" and "/cpy-bms/" not in p],
        "DB2 DCLGEN members (.dcl)": [p for p in src if ext(p) == ".dcl"],
        "BMS symbolic-map copybooks (cpy-bms/*.cpy)": [p for p in src if ext(p) == ".cpy" and "/cpy-bms/" in p],
        "BMS mapsets (.bms)": [p for p in src if ext(p) == ".bms"],
        "JCL members (.jcl)": [p for p in src if ext(p) == ".jcl"],
        "Catalogued PROCs (.prc)": [p for p in src if ext(p) == ".prc"],
        "Assembler programs (.asm)": [p for p in src if ext(p) == ".asm"],
    }
    inv_types = {}
    for f in inv["files"]:
        inv_types[f["type"]] = inv_types.get(f["type"], 0) + 1
    expect = {
        "COBOL programs (.cbl)": ("cobol-program", inv_types.get("cobol-program", 0)),
        "COBOL copybooks (.cpy outside cpy-bms)": ("cobol-copybook", inv_types.get("cobol-copybook", 0)),
        "DB2 DCLGEN members (.dcl)": ("db2-dclgen", inv_types.get("db2-dclgen", 0)),
        "BMS symbolic-map copybooks (cpy-bms/*.cpy)": ("bms-symbolic-map", inv_types.get("bms-symbolic-map", 0)),
        "BMS mapsets (.bms)": ("bms-mapset", inv_types.get("bms-mapset", 0)),
        "JCL members (.jcl)": ("jcl-job", inv_types.get("jcl-job", 0)),
        "Catalogued PROCs (.prc)": ("jcl-proc", inv_types.get("jcl-proc", 0)),
        "Assembler programs (.asm)": ("asm-program", inv_types.get("asm-program", 0)),
    }
    pages = {
        "COBOL programs (.cbl)": "07-programs/%s.md",
        "COBOL copybooks (.cpy outside cpy-bms)": "08-data/layouts/%s.md",
        "DB2 DCLGEN members (.dcl)": "08-data/layouts/%s.md",
        "BMS mapsets (.bms)": "05-online/screens/%s.md",
        "Catalogued PROCs (.prc)": "06-batch/procs/%s.md",
        "Assembler programs (.asm)": "07-programs/%s.md",
    }
    order = ["COBOL programs (.cbl)", "Assembler programs (.asm)", "COBOL copybooks (.cpy outside cpy-bms)", "DB2 DCLGEN members (.dcl)",
             "BMS mapsets (.bms)", "BMS symbolic-map copybooks (cpy-bms/*.cpy)", "JCL members (.jcl)", "Catalogued PROCs (.prc)"]
    usage_page = text(os.path.join(docs, "17-dependencies", "copybook-usage.md"))
    rows, bad = [], []
    for g in order:
        files = groups[g]
        t, n_inv = expect[g]
        no_page = []
        if g.startswith("BMS symbolic"):
            no_page = [p for p in files if p not in usage_page]
        elif g in pages:
            for p in files:
                m = os.path.splitext(os.path.basename(p))[0].upper()
                if not os.path.isfile(os.path.join(docs, pages[g] % m)):
                    no_page.append(p)
        elif g == "JCL members (.jcl)":
            for p in files:
                job = None
                for l in read_lines(os.path.join(snap, p)):
                    m = re.match(r"^//(\S+)\s+JOB\b", l)
                    if m:
                        job = m.group(1).upper()
                        break
                if not job or not os.path.isfile(os.path.join(docs, "06-batch/jobs/%s.md" % job)):
                    no_page.append("%s (JOB %s)" % (p, job))
        ok = len(files) == n_inv and not no_page
        rows.append({"group": g, "files": len(files), "inventory_type": t, "inventory": n_inv, "without_page": no_page})
        if not ok:
            bad.append(g)
    layouts = len([p for p in os.listdir(os.path.join(docs, "08-data", "layouts")) if p.endswith(".md")])
    procs = len([p for p in os.listdir(os.path.join(docs, "06-batch", "procs")) if p.endswith(".md")])
    metrics["source_groups"] = rows
    metrics["layout_pages"] = layouts
    metrics["proc_pages"] = procs
    detail = ["%s: %d files, inventory %s=%d, %s %d" % (r["group"], r["files"], r["inventory_type"], r["inventory"],
                                                      "not on the copybook-usage page" if r["group"].startswith("BMS symbolic") else "without page", len(r["without_page"])) for r in rows]
    detail.append("BMS symbolic-map copybooks have no page of their own; the check is that each path is listed on 17-dependencies/copybook-usage.md with the program that copies it")
    n_cpy = len(groups["COBOL copybooks (.cpy outside cpy-bms)"]) + len(groups["DB2 DCLGEN members (.dcl)"])
    detail.append("copybook layout pages %d = %d .cpy + %d .dcl" % (layouts, len(groups["COBOL copybooks (.cpy outside cpy-bms)"]), len(groups["DB2 DCLGEN members (.dcl)"])))
    tmpl = inv_types.get("jcl-template", 0)
    detail.append("PROC pages %d = %d .prc + %d JCL template(s) (inventory type jcl-template)" % (procs, len(groups["Catalogued PROCs (.prc)"]), tmpl))
    R.add("V1", "Source files recounted by extension match the inventory and each has a page", not bad and layouts == n_cpy and procs == len(groups["Catalogued PROCs (.prc)"]) + tmpl,
          "%d groups checked, %d mismatched" % (len(rows), len(bad)), detail + ["MISMATCH " + b for b in bad])

    # ---------------------------------------------------------------- V2 page counts
    md = [p for p in walk(docs, (".md",))]
    other = [rel(p, docs) for p in walk(docs) if not p.endswith(".md")]
    metrics["markdown_pages"] = len(md)
    ok = len(md) == cov["documents"] == gaps["markdown_pages"] == chk["documents"]
    R.add("V2", "Markdown page count agrees across the package, coverage.json, gaps.json and check_package.json", ok,
          "%d pages; coverage.json %d; gaps.json %d; check_package.json %d; other files: %s" % (len(md), cov["documents"], gaps["markdown_pages"], chk["documents"], ", ".join(other)))

    # ---------------------------------------------------------------- V3 source references
    ref_files = md + [p for d in ("02-coverage-validation-report", "03-business-rules-and-traceability", "04-gap-report") for p in walk(os.path.join(B, d), (".md",))
                      if rel(p, B) not in OUTPUTS]
    counts = {}
    distinct = {}
    occ = 0
    lc = {}
    redacted = set()
    rp = os.path.join(snap, "REDACTIONS.md")
    if os.path.isfile(rp):
        for m in re.finditer(r"\| `([^`]+)` \| (\d+) \|", text(rp)):
            redacted.add((m.group(1), int(m.group(2))))
    for p in ref_files:
        for m in REF.finditer(text(p)):
            occ += 1
            key = (m.group(1), int(m.group(2)), int(m.group(3) or m.group(2)))
            if key in distinct:
                continue
            path = key[0]
            target = os.path.join(B, "01-detailed-documentation", path) if path == "COMBINED_DOCUMENTATION.md" else os.path.join(snap, path)
            if path not in lc:
                lc[path] = len(read_lines(target)) if os.path.isfile(target) else -1
            n = lc[path]
            if n < 0:
                distinct[key] = "file not in bundle"
            elif not (1 <= key[1] <= key[2] <= n):
                distinct[key] = "line range outside file (%d lines)" % n
            elif any(f == path and key[1] <= ln <= key[2] for f, ln in redacted):
                distinct[key] = "ok (range includes a redacted line)"
            else:
                distinct[key] = "ok"
    badr = sorted("%s:%d-%d %s" % (k[0], k[1], k[2], v) for k, v in distinct.items() if not v.startswith("ok"))
    red_refs = sorted("%s:%d-%d" % k for k, v in distinct.items() if "redacted" in v)
    metrics["source_references"] = {"occurrences": occ, "distinct": len(distinct), "invalid": len(badr), "touching_redacted_lines": len(red_refs), "files_cited": len(lc)}
    R.add("V3", "Every `path:line` citation in the documentation and reports resolves to an existing line range in the source snapshot", not badr,
          "%d occurrences, %d distinct, %d files cited, %d invalid, %d touch redacted lines" % (occ, len(distinct), len(lc), len(badr), len(red_refs)),
          badr[:50] + ["cites redacted line(s): " + r for r in red_refs])

    # ---------------------------------------------------------------- V4 rule traceability
    impl_n, para_ok, para_out, para_missing, no_para, range_bad = 0, 0, [], [], {}, []
    label_cache = {}
    for r in rules:
        for i in r.get("implementations", []):
            impl_n += 1
            m = re.match(r"^(.+?):(\d+)(?:-(\d+))?$", i.get("source") or "")
            if not m:
                range_bad.append("%s: no line range" % r["id"])
                continue
            path, a, b = m.group(1), int(m.group(2)), int(m.group(3) or m.group(2))
            fp = os.path.join(snap, path)
            if not os.path.isfile(fp):
                range_bad.append("%s: %s not in snapshot" % (r["id"], path))
                continue
            lines = read_lines(fp)
            if not (1 <= a <= b <= len(lines)):
                range_bad.append("%s: %s outside file" % (r["id"], i["source"]))
                continue
            if path.lower().endswith((".cbl", ".cpy")):
                if path not in label_cache:
                    label_cache[path] = (cobol_labels(lines), next((k + 1 for k, l in enumerate(lines) if re.search(r"PROCEDURE\s+DIVISION", l[6:72] if len(l) > 6 else "", re.I) and l[6:7] not in ("*", "/")), None))
                labels, proc_line = label_cache[path]
            else:
                labels, proc_line = [], None
            para = (i.get("paragraph") or "").upper()
            if para:
                names = [x.strip() for x in para.split(",") if x.strip()]
                spans = []
                for nm in names:
                    if nm == "(PROCEDURE DIVISION ENTRY)" and proc_line:
                        first = [ln for ln, _ in labels if ln > proc_line]
                        spans.append((proc_line, (first[0] - 1) if first else len(lines)))
                        continue
                    for k, (ln, lab) in enumerate(labels):
                        if lab == nm:
                            spans.append((ln, labels[k + 1][0] - 1 if k + 1 < len(labels) else len(lines)))
                if not spans:
                    para_missing.append("%s: paragraph %s not found as an Area A label in %s" % (r["id"], para, path))
                    continue
                inside = any(s0 <= a <= s1 for s0, s1 in spans)
                if inside:
                    para_ok += 1
                else:
                    para_out.append("%s: %s starts outside paragraph %s" % (r["id"], i["source"], para))
            else:
                if path.lower().endswith(".asm"):
                    k = "Assembler source"
                elif not path.lower().endswith((".cbl", ".cpy")):
                    k = "non-COBOL source (%s)" % os.path.splitext(path)[1]
                elif proc_line and a >= proc_line:
                    k = "PROCEDURE DIVISION, no paragraph named"
                elif proc_line:
                    k = "before PROCEDURE DIVISION (data definitions)"
                else:
                    k = "copybook without PROCEDURE DIVISION (data definitions)"
                no_para[k] = no_para.get(k, 0) + 1
    tp = text(os.path.join(docs, "14-cross-reference-traceability.md"))
    page_ids = set(re.findall(r"^\| \[(BR-[A-Za-z0-9-]+)\]\(09-business-rules-catalog\.md#([a-z0-9-]+)\)", tp, re.M))
    cat_anchors = anchors_of(text(os.path.join(docs, "09-business-rules-catalog.md")))
    ids = set(r["id"] for r in rules)
    missing_rows = sorted(ids - set(x for x, _ in page_ids))
    bad_anchor = sorted(x for x, a in page_ids if a not in cat_anchors)
    metrics["rules"] = {"rules": len(rules), "implementations": impl_n, "paragraph_named": para_ok + len(para_out) + len(para_missing),
                        "paragraph_confirmed_by_label_scan": para_ok, "paragraph_range_outside": len(para_out), "paragraph_label_not_found": len(para_missing),
                        "no_paragraph_named": no_para, "traceability_rows": len(page_ids)}
    R.add("V4a", "Every rule implementation cites an existing line range", not range_bad, "%d implementations of %d rules, %d invalid" % (impl_n, len(rules), len(range_bad)), range_bad)
    R.add("V4b", "Every rule appears on the traceability page and links to an existing catalog anchor", not missing_rows and not bad_anchor and len(page_ids) == len(ids),
          "%d rules, %d rows, %d missing, %d bad anchors" % (len(ids), len(page_ids), len(missing_rows), len(bad_anchor)), missing_rows + bad_anchor)
    R.add("V4c", "Named paragraphs exist in the cited source and contain the first cited line (independent Area A label scan)", not para_missing and not para_out,
          "%d named: %d confirmed, %d start outside the named paragraph, %d labels not found" % (para_ok + len(para_out) + len(para_missing), para_ok, len(para_out), len(para_missing)),
          para_missing + para_out, hard=False)
    R.add("V4d", "Implementations without a named paragraph, by location (informational)", True,
          ", ".join("%s %d" % kv for kv in sorted(no_para.items())), [], hard=False)

    # ---------------------------------------------------------------- V5 links and anchors
    all_md = [p for p in walk(B, (".md",)) if "/templates/" not in rel(p, B) and rel(p, B) not in OUTPUTS and not rel(p, B).startswith(SNAP + "/")]
    anchor_cache = {}
    broken, n_links = [], 0
    for p in all_md:
        t = strip_code(text(p))
        for m in LINK.finditer(t):
            tgt = m.group(1)
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", tgt):
                continue
            n_links += 1
            path, frag = (tgt.split("#", 1) + [""])[:2]
            dest = os.path.normpath(os.path.join(os.path.dirname(p), path)) if path else p
            if not dest.startswith(B):
                broken.append("%s -> %s (leaves the bundle)" % (rel(p, B), tgt))
                continue
            if not os.path.exists(dest):
                broken.append("%s -> %s (missing)" % (rel(p, B), tgt))
                continue
            if frag and dest.endswith(".md"):
                if dest not in anchor_cache:
                    anchor_cache[dest] = anchors_of(text(dest))
                if frag.lower() not in anchor_cache[dest] and frag not in anchor_cache[dest]:
                    broken.append("%s -> %s (no anchor)" % (rel(p, B), tgt))
    metrics["links"] = {"files": len(all_md), "links": n_links, "broken": len(broken)}
    R.add("V5", "Every relative Markdown link and anchor in the bundle resolves inside the bundle (templates excluded)", not broken,
          "%d files, %d relative links, %d broken" % (len(all_md), n_links, len(broken)), broken[:80])

    # ---------------------------------------------------------------- V6 hygiene
    junk = [rel(p, B) for p in walk(B) if re.search(r"(\.pyc|\.pyo|~|\.bak|\.tmp)$", p) or os.path.basename(p).startswith("_tmp")
            or os.path.basename(p) in ("Thumbs.db", ".DS_Store") or "__pycache__" in p]
    empty = [rel(p, B) for p in walk(B) if os.path.getsize(p) == 0]
    R.add("V6", "No compiled, temporary or empty files", not junk and not empty, "%d junk, %d empty" % (len(junk), len(empty)), junk + empty)

    # ---------------------------------------------------------------- V7 secrets
    sec_detail, sec_ok = [], True
    if repo:
        member = os.path.join(repo, "app", "jcl", "FTPJCL.JCL")
        secrets = []
        for i, l in enumerate(read_lines(member)):
            s = l.strip()
            if s and not l.startswith("//") and not l.startswith("/*") and s.split()[0].lower() not in FTP_COMMANDS:
                secrets.append((i + 1, s))
        hits = 0
        for p in walk(B):
            if p.lower().endswith(".docx"):
                z = zipfile.ZipFile(p)
                try:
                    body = " ".join(z.read(n).decode("utf-8", "replace") for n in z.namelist() if n.endswith(".xml"))
                finally:
                    z.close()
            elif p.lower().endswith((".md", ".json", ".txt", ".yaml", ".yml", ".ps1", ".py", ".mdc", ".jcl", ".csv")) or "/06-source-snapshot/" in p.replace("\\", "/"):
                body = open(p, "rb").read().decode("latin-1")
            else:
                continue
            for n, s in secrets:
                if s in body:
                    hits += 1
                    sec_detail.append("FTPJCL.JCL:%d found in %s" % (n, rel(p, B)))
        sec_ok = hits == 0
        measured = "%d connection lines checked in every text file and inside the DOCX; %d findings" % (len(secrets), hits)
    else:
        measured = "repository not given; only the redaction markers were checked"
    snapf = os.path.join(snap, "app", "jcl", "FTPJCL.JCL")
    marks = len([l for l in read_lines(snapf) if "REDACTED" in l]) if os.path.isfile(snapf) else 0
    R.add("V7", "FTP connection lines from app/jcl/FTPJCL.JCL are absent from the bundle (snapshot copy redacted)", sec_ok and marks > 0,
          measured + "; %d redaction markers in the snapshot copy" % marks, sec_detail)

    # ---------------------------------------------------------------- V8 snapshot integrity
    sha = dict((f["path"], f.get("sha256")) for f in inv["files"])
    mism, red_files, diff_repo, raw_ok, lf_ok = [], [], [], 0, 0
    red_paths = set(f for f, _ in redacted)
    for p in src:
        b = open(os.path.join(snap, p), "rb").read()
        h = hashlib.sha256(b).hexdigest()
        if p in red_paths:
            red_files.append(p)
        elif sha.get(p) == h:
            raw_ok += 1
        elif sha.get(p) == hashlib.sha256(b.replace(b"\r\n", b"\n")).hexdigest():
            lf_ok += 1
        else:
            mism.append(p)
        if repo and p not in red_paths:
            if hashlib.sha256(open(os.path.join(repo, p), "rb").read()).hexdigest() != h:
                diff_repo.append(p)
    metrics["snapshot"] = {"files": len(src), "sha256_match": raw_ok, "sha256_match_after_crlf_to_lf": lf_ok, "mismatch": len(mism), "redacted": len(red_files)}
    R.add("V8", "Snapshot files match the analysed sources (inventory sha256%s)" % (" and the repository" if repo else ""), not mism and not diff_repo,
          "%d files: %d identical, %d identical after CRLF->LF normalisation (the working tree was checked out with CRLF after analysis; line numbers are unaffected), "
          "%d mismatches, %d differ from repository, %d redacted (expected to differ)" % (len(src), raw_ok, lf_ok, len(mism), len(diff_repo), len(red_files)), mism + diff_repo)

    # ---------------------------------------------------------------- V9 report consistency
    det = []
    comps = gaps["components"]
    ok = True
    s_counts = sum(n for v in gaps["counts"].values() for n in v.values())
    det.append("gap components %d, sum of per-type counts %d" % (len(comps), s_counts))
    ok = ok and s_counts == len(comps)
    reg = gaps.get("register", [])
    parts = len(gaps["unresolved"]) + len(gaps["sme_questions"]) + len(gaps["conflicts"]) + len(gaps["unverified"]) + len(gaps["ambiguous_dependencies"])
    det.append("register rows %d = unresolved %d + SME %d + conflicts %d + unverified %d + ambiguous %d = %d" % (
        len(reg), len(gaps["unresolved"]), len(gaps["sme_questions"]), len(gaps["conflicts"]), len(gaps["unverified"]), len(gaps["ambiguous_dependencies"]), parts))
    ok = ok and len(reg) == parts
    noline = [r["id"] for r in reg if not re.search(r":\d+", r.get("source") or "")]
    det.append("register rows without a line-level source: %d %s" % (len(noline), " ".join(noline)))
    ok = ok and not noline
    crit = cov["criteria"]
    failed = [c["criterion"] for c in crit if not c["pass"]]
    det.append("coverage_validate criteria %d, failed %d" % (len(crit), len(failed)))
    ok = ok and not failed
    issues = sum(len([x for x in (chk.get(k) or []) if x]) for k in ("uncovered_artifacts", "broken_links", "placeholders", "template_guides_left", "mermaid_warnings", "missing_sources_section"))
    det.append("check_package issues %d" % issues)
    ok = ok and issues == 0
    rt = [s for s in cov["summaries"] if s["category"] == "rule-traceability"][0]
    det.append("rule-traceability total %d, rules.json %d" % (rt["total"], len(rules)))
    ok = ok and rt["total"] == len(rules)
    sr = [s for s in cov["summaries"] if s["category"] == "source-references"][0]
    det.append("coverage_validate source references %d distinct (documentation folder only); this check %d distinct (documentation + report copies)" % (sr["total"], len(distinct)))
    R.add("V9", "Reports agree with each other (gap counts, register, criteria, package check, rule totals)", ok, "%d cross-checks" % len(det), det)

    # ---------------------------------------------------------------- V10 duplicates
    by_hash = {}
    for p in walk(B):
        if rel(p, B) in OUTPUTS:
            continue
        by_hash.setdefault(hashlib.sha256(open(p, "rb").read()).hexdigest(), []).append(rel(p, B))
    dups = [v for v in by_hash.values() if len(v) > 1]
    R.add("V10", "Identical files (informational; intended copies are explained in README.md)", True, "%d groups of identical files" % len(dups),
          ["; ".join(v) for v in sorted(dups)], hard=False)

    fails = [c for c in R.checks if c["status"] == "FAIL"]
    warns = [c for c in R.checks if c["status"] == "warn"]
    out = {"schema": "bundle-verification/1", "generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "repository_checked": bool(repo),
           "checks": R.checks, "metrics": metrics, "failed": len(fails), "warnings": len(warns)}
    if write:
        L = ["# Bundle verification", "",
             "Generated by `verify_review_bundle.py` on %s%s. Independent of the pipeline's parsers: source counts come from file extensions and JCL JOB cards, "
             "paragraph spans from Area A labels in the source snapshot, links and anchors from the Markdown text." % (out["generated"], " with the repository available" if repo else " from the bundle alone"), "",
             "Result: %d checks, %d failed, %d warnings." % (len(R.checks), len(fails), len(warns)), "",
             "| ID | Check | Status | Measured |", "|---|---|---|---|"]
        for c in R.checks:
            L.append("| %s | %s | %s | %s |" % (c["id"], c["check"].replace("|", "\\|"), c["status"], str(c["measured"]).replace("|", "\\|")))
        for c in R.checks:
            if c["detail"]:
                L += ["", "## %s detail" % c["id"], ""] + ["- %s" % str(d).replace("|", "\\|") for d in c["detail"][:200]]
                if len(c["detail"]) > 200:
                    L.append("- ... %d more in bundle-verification.json" % (len(c["detail"]) - 200))
        L += ["", "## What these checks do not prove", "",
              "- That a cited line range supports the sentence that cites it. V3 proves the range exists; V4c proves a named paragraph contains the first cited line. Semantic correctness needs human review.",
              "- That business rules are complete or correctly interpreted. Rules come from AI-assisted analysis validated by schema and citation checks; open questions are in the gap register.",
              "- Runtime behaviour. No program was compiled or executed; CICS, IMS, DB2, MQ and the schedulers were not available."]
        f = open(os.path.join(B, OUTPUTS[0]), "w", encoding="utf-8", newline="\n")
        f.write("\n".join(L) + "\n")
        f.close()
        f = open(os.path.join(B, OUTPUTS[1]), "w", encoding="utf-8", newline="\n")
        json.dump(out, f, indent=1, sort_keys=True)
        f.close()
    for c in R.checks:
        sys.stdout.write("%-4s %-5s %s | %s\n" % (c["id"], c["status"], c["check"][:90], c["measured"]))
    sys.stdout.write("checks=%d failed=%d warnings=%d\n" % (len(R.checks), len(fails), len(warns)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
