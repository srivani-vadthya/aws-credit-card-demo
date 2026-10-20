"""Classify every in-scope component and publish the gap report.

Usage (from the repository root, after coverage_validate.py):
  python gap_report.py <work_dir> <output_dir> [--claimed-pages N]

Status per component (primary status uses this precedence):
  missing > unanalyzed > partially documented > unresolved > requires SME clarification > documented
Also lists conflicting definitions and ambiguous dependencies found in the
structure, the semantic analysis, the earlier work facts and the scheduler data.
Writes <work_dir>/coverage/gaps.json and <output_dir>/18-coverage/gap-report.md.
Python 3.1+ standard library only.
"""
import json
import os
import re
import sys
import time

RENDERER_PAGES = ["06-batch/procs", "05-online/cics-resources.md", "08-data/data-definitions.md", "17-dependencies", "18-coverage"]
ORDER = ["missing", "unanalyzed", "partially documented", "unresolved", "requires SME clarification", "documented"]


def load(path, default=None):
    if not os.path.exists(path):
        return default
    f = open(path, "r", encoding="utf-8-sig")
    try:
        return json.load(f)
    finally:
        f.close()


def esc(s):
    return str(s if s is not None else "").replace("|", "\\|").replace("\n", " ")


def main(argv):
    if len(argv) < 3:
        raise SystemExit(__doc__)
    work, out = argv[1], argv[2]
    claimed = int(argv[argv.index("--claimed-pages") + 1]) if "--claimed-pages" in argv else None
    S = os.path.join(work, "structure")
    inv = load(os.path.join(work, "inventory.json"))
    cov = load(os.path.join(work, "coverage", "coverage.json"))
    if cov is None:
        raise SystemExit("run coverage_validate.py first")
    details = cov["details"]
    progs = {}
    for f in sorted(os.listdir(os.path.join(S, "programs"))):
        s = load(os.path.join(S, "programs", f))
        progs[s["member"]] = s
    cpys = dict((f[:-5], load(os.path.join(S, "copybooks", f))) for f in os.listdir(os.path.join(S, "copybooks")))
    jcl = [load(os.path.join(S, "jcl", f)) for f in sorted(os.listdir(os.path.join(S, "jcl")))]
    usage = load(os.path.join(S, "copybook-usage.json"))["edges"]
    csd = load(os.path.join(S, "csd.json"))
    callgraph = load(os.path.join(work, "xref", "call-graph.json"), {"edges": []})["edges"]
    schedule = load(os.path.join(work, "batch", "schedule.json"), {})
    rules = load(os.path.join(work, "rules", "rules.json"), {"rules": []})["rules"]
    sem = {}
    for f in os.listdir(os.path.join(work, "semantic", "programs")):
        sem[f[:-5]] = load(os.path.join(work, "semantic", "programs", f))
    csem = {}
    for f in os.listdir(os.path.join(work, "semantic", "copybooks")):
        csem[f[:-5]] = load(os.path.join(work, "semantic", "copybooks", f))
    cps = {}
    for b in os.listdir(os.path.join(work, "batches")):
        cp = load(os.path.join(work, "batches", b, "checkpoint.json"))
        if cp:
            for k, v in cp.get("programs", {}).items():
                cps[k] = v
            for k, v in cp.get("copybooks", {}).items():
                cps["CPY:" + k] = v
    open_items = {}
    for cat, items in details.items():
        for i in items:
            open_items.setdefault(cat, []).append(i)

    comps = []

    def comp(kind, name, path, flags, reasons):
        flags = [f for f in ORDER if f in flags] or ["documented"]
        comps.append({"kind": kind, "name": name, "path": path, "status": flags[0], "flags": flags, "reasons": reasons})

    def opens_for(cat, prefix):
        return [i for i in open_items.get(cat, []) if i["item"].startswith(prefix)]

    rule_progs = {}
    for r in rules:
        for i in r.get("implementations", []):
            if i.get("program"):
                rule_progs.setdefault(i["program"], set()).add(r["id"])
    reviews = {}
    rv_dir = os.path.join(work, "semantic", "reviews")
    rv_cp = (load(os.path.join(work, "batches", "reviews-checkpoint.json"), {}) or {}).get("members", {})
    if os.path.isdir(rv_dir):
        for fn in sorted(os.listdir(rv_dir)):
            if fn.endswith(".json") and (rv_cp.get(fn[:-5]) or {}).get("status") == "validated":
                for e in (load(os.path.join(rv_dir, fn), {}) or {}).get("existing_rules_reviewed", []):
                    reviews[e.get("id")] = dict(e, program=fn[:-5])
    sme, conflicts, ambiguous, unresolved = [], [], [], []
    # programs
    for pgm, s in sorted(progs.items()):
        flags, reasons = set(), []
        cp = cps.get(pgm, {})
        if cp.get("status") != "validated":
            flags.add("unanalyzed")
            reasons.append("semantic analysis status: %s" % (cp.get("status") or "none"))
        for cat in ("paragraphs-structural", "exec-commands", "call-statements", "file-selects", "program-data-items",
                    "procedure-statements", "unclassified-statements", "decision-points-all"):
            o = opens_for(cat, pgm + ".") + opens_for(cat, pgm + ":")
            if o:
                flags.add("partially documented")
                reasons.append("%d %s not on page" % (len(o), cat))
        o = opens_for("paragraph-logic-grounding", pgm + ".")
        if o:
            flags.add("partially documented")
            reasons.append("%d paragraph descriptions name nothing from their code" % len(o))
        o = [i for i in open_items.get("rule-traceability", []) if i["item"] in rule_progs.get(pgm, set())]
        if o:
            flags.add("partially documented")
            reasons.append("%d rules fail traceability: %s" % (len(o), ", ".join(i["item"] for i in o)))
        o = [i for i in open_items.get("decision-points", []) if i["item"].startswith(pgm + ":") and i["status"] == "partial"]
        if o:
            flags.add("partially documented")
            reasons.append("%d business-candidate decisions not linked to a rule or reason" % len(o))
        if s.get("unresolved_targets"):
            flags.add("unresolved")
            reasons.append("unresolved PERFORM/GO TO targets: " + ", ".join(u["target"] for u in s["unresolved_targets"]))
        sm = sem.get(pgm) or {}
        for q in sm.get("sme_questions", []):
            flags.add("requires SME clarification")
            sme.append({"component": pgm, "question": q.get("question"), "source": q.get("source")})
        for ob in sm.get("observations", []):
            if ob.get("kind") == "conflict":
                conflicts.append({"component": pgm, "text": ob.get("text"), "source": ob.get("source"), "origin": "batch analysis"})
        if sm.get("sme_questions"):
            reasons.append("%d SME questions" % len(sm["sme_questions"]))
        comp("cobol-program", pgm, s["source_path"], flags, reasons)
    # copybooks
    for key, s in sorted(cpys.items()):
        cpy = s["member"]
        flags, reasons = set(), []
        cp = cps.get("CPY:" + cpy, {})
        if cp.get("status") != "validated":
            flags.add("unanalyzed")
            reasons.append("semantic purpose status: %s" % (cp.get("status") or "none"))
        for cat in ("copybook-fields", "copybook-88-levels", "copybook-paragraphs"):
            o = opens_for(cat, cpy + ".")
            if o:
                flags.add("partially documented")
                reasons.append("%d %s not on page" % (len(o), cat))
        users = [u for u in usage if u["copybook"] == cpy and not u["commented"]]
        if not users:
            reasons.append("not copied by any program or copybook")
        alts = sorted(set(a for u in usage if u["copybook"] == cpy for a in u.get("other_candidates", [])))
        if alts:
            conflicts.append({"component": cpy, "text": "member name resolves to more than one file: %s and %s" % (s["source_path"], ", ".join(alts)), "source": s["source_path"], "origin": "copybook resolution"})
        cs = csem.get(cpy) or {}
        n_dead = 0
        for ob in cs.get("observations", []):
            if ob.get("kind") in ("conflict",):
                conflicts.append({"component": cpy, "text": ob.get("text"), "source": ob.get("source"), "origin": "batch analysis"})
            if ob.get("kind") in ("dead-code",):
                n_dead += 1
                flags.add("requires SME clarification")
                sme.append({"component": cpy, "question": "Is this copybook still needed? " + (ob.get("text") or ""), "source": ob.get("source")})
        if n_dead:
            reasons.append("%d dead-code observations need an SME decision" % n_dead)
        for q in cs.get("sme_questions", []):
            flags.add("requires SME clarification")
            sme.append({"component": cpy, "question": q.get("question"), "source": q.get("source")})
        if cs.get("sme_questions"):
            reasons.append("%d SME questions" % len(cs["sme_questions"]))
        comp(s["artifact_type"], cpy, s["source_path"], flags, reasons)
    # jobs and procs
    sched_jobs = set()
    for e in schedule.get("ca7_edges", []) + schedule.get("controlm_edges", []):
        sched_jobs.add(e.get("from"))
        sched_jobs.add(e.get("to"))
    for e in schedule.get("script_submits", []):
        sched_jobs.add(e.get("job"))
    dd_dsn = {}
    for j in jcl:
        name = ((j.get("job") or {}).get("name") or j["member"]).upper() if j["artifact_type"] == "jcl-job" else j["member"]
        flags, reasons = set(), []
        for cat in ("jcl-steps", "jcl-dds", "jcl-conditions", "dataflow-edges"):
            o = opens_for(cat, name + ".") + opens_for(cat, name + " ")
            if o:
                flags.add("partially documented")
                reasons.append("%d %s not on page" % (len(o), cat))
        if [i for i in open_items.get("jcl-jobs", []) + open_items.get("jcl-procs", []) if i["item"] == name]:
            flags.add("missing")
        syms = sorted(set(re.findall(r"&&?[A-Z][A-Z0-9#@$]*", " ".join(st["operands"] + " " + " ".join(d["operands"] for d in st["dds"]) for st in j["steps"]))))
        syms = [x for x in syms if not x.startswith("&&")]
        if syms:
            flags.add("unresolved")
            reasons.append("symbolic parameters left unresolved: " + ", ".join(syms))
            unresolved.append({"component": name, "item": ", ".join(syms), "kind": "JCL symbolic parameter", "source": j["source_path"],
                               "resolution": "value supplied at submission or by PROC defaults outside the repository"})
        if j["artifact_type"] == "jcl-job" and name not in sched_jobs:
            reasons.append("not named in CA7, Control-M or shell submit lists")
        o = [i for i in open_items.get("scheduler-edges", []) if i["status"] == "missing" and re.search(r"(^|\s)%s(\s|$)" % re.escape(name), i["item"])]
        if o:
            flags.add("partially documented")
            reasons.append("%d scheduler edges not on page" % len(o))
        for st in j["steps"]:
            pg = (st.get("pgm") or "").upper()
            app = (st.get("application_program") or {}).get("program", "").upper()
            for d in st["dds"]:
                if d.get("dsn") and d["ddname"] not in ("STEPLIB", "SYSPRINT", "SYSOUT", "SYSIN", "JOBLIB"):
                    dd_dsn.setdefault((app or pg, d["ddname"]), set()).add((d.get("gdg_base") or d["dsn"], d["source"]))
        comp(j["artifact_type"], name, j["source_path"], flags, reasons)
    for (pg, dd), vals in sorted(dd_dsn.items()):
        names = sorted(set(v[0] for v in vals))
        if len(names) > 1 and pg:
            conflicts.append({"component": pg, "text": "DD %s is bound to different datasets across jobs: %s" % (dd, "; ".join("%s (%s)" % v for v in sorted(vals))),
                              "source": sorted(vals)[0][1], "origin": "JCL"})
    # CICS
    have = set(progs) | set(e["member"].upper() for e in inv["files"] if e["type"] in ("asm-program",))
    for r in csd["resources"]:
        flags, reasons = set(), []
        if r["type"] == "PROGRAM" and r["name"] not in have:
            flags.add("unresolved")
            reasons.append("CSD PROGRAM has no source member in the repository")
            unresolved.append({"component": r["name"], "item": "CICS program definition", "kind": "external-or-missing program", "source": r["source"],
                               "resolution": "obtain the source or confirm the program is retired"})
        if r["type"] == "TRANSACTION" and r["attrs"].get("PROGRAM") not in have:
            flags.add("unresolved")
            reasons.append("starts program %s which has no source" % r["attrs"].get("PROGRAM"))
        comp("cics-" + r["type"].lower(), r["name"], r["source"], flags, reasons)
    # dynamic / inferred dependencies
    for e in callgraph:
        if e.get("resolution_confidence") == "Inferred" or (e.get("mechanism") == "CALL-dynamic"):
            ambiguous.append({"from": e.get("from"), "mechanism": e.get("mechanism"), "variable": e.get("to"),
                              "candidates": sorted(set(t.get("target") for t in e.get("resolved_to", []))), "source": e.get("source"),
                              "why": "target held in a variable; resolved from MOVEs and caller lists (Inferred)"})
        elif e.get("to") and not e.get("resolved_to") and e.get("mechanism") in ("XCTL", "LINK") and e.get("to") not in have and re.search(r"[-]", e.get("to") or ""):
            ambiguous.append({"from": e.get("from"), "mechanism": e.get("mechanism"), "variable": e.get("to"), "candidates": [],
                              "source": e.get("source"), "why": "variable target not resolved"})
    for j in schedule.get("jobs_in_scheduler_without_jcl", []):
        ambiguous.append({"from": "scheduler", "mechanism": "CA7 job", "variable": j.get("job"), "candidates": [j.get("jcl_member")],
                          "source": j.get("source"), "why": "scheduler job name has no job card of that name; it names JCL member %s" % j.get("jcl_member")})
    q = schedule.get("td_queue_submit")
    if q:
        ambiguous.append({"from": q.get("writer"), "mechanism": "TD queue %s -> internal reader" % q.get("queue"), "variable": "job stream built in program",
                          "candidates": [], "source": (q.get("queue_attributes") or {}).get("source"), "why": "submitted JCL is assembled at run time"})
    # legacy rule verdicts
    for r in rules:
        v = r.get("verification") or reviews.get(r["id"]) or {}
        if v.get("verdict") in ("corrected", "disputed"):
            conflicts.append({"component": v.get("program") or "", "text": "legacy rule %s %s by the batch review: %s" % (r["id"], v["verdict"], v.get("note") or ""),
                              "source": v.get("source"), "origin": "rule review"})
            if v["verdict"] == "disputed":
                sme.append({"component": v.get("program"), "question": "Confirm the intended behaviour for %s: %s" % (r["id"], r.get("statement")), "source": v.get("source")})
        if r.get("origin") == "legacy" and not v:
            unresolved.append({"component": ",".join(sorted(set(i.get("program", "") for i in r.get("implementations", [])))), "item": r["id"],
                               "kind": "legacy rule not re-reviewed", "source": (r.get("implementations") or [{}])[0].get("source"),
                               "resolution": "review in the owning batch, or in semantic/reviews/<MEMBER>.json for non-COBOL members"})
    # earlier-pass vs structure conflicts
    for pgm, s in progs.items():
        old = load(os.path.join(work, "programs", pgm + ".json"))
        if old:
            a = set(p["name"] for p in old.get("paragraphs", []))
            b = set(p["name"] for p in s["paragraphs"])
            if a - b:
                conflicts.append({"component": pgm, "text": "earlier program facts list paragraphs not found by the parser: %s (the parser output is used)" % ", ".join(sorted(a - b)),
                                  "source": s["source_path"], "origin": "earlier facts vs parser"})
            if b - a:
                conflicts.append({"component": pgm, "text": "parser found paragraphs missing from the earlier facts: %s" % ", ".join(sorted(b - a)),
                                  "source": s["source_path"], "origin": "earlier facts vs parser"})
    for e in usage:
        if e["resolution"] == "external-or-missing":
            unresolved.append({"component": e["from_member"], "item": e["copybook"], "kind": "missing copybook", "source": e["source"], "resolution": "provide the member"})
    # in-scope inventory artifacts not covered above
    covered_paths = set(c["path"].split(":")[0] for c in comps)
    for e in inv["files"]:
        if e["path"] in covered_paths or e["type"] in ("placeholder", "repo-meta", "excluded"):
            continue
        st = "documented"
        reasons = ["named in the package (inventory coverage check)"]
        if any(i["item"] == e["path"] for i in open_items.get("inventory-artifacts", []) if i["status"] == "missing"):
            st = "missing"
            reasons = ["not named anywhere in the package"]
        elif e["type"] in ("documentation", "diagram"):
            reasons = ["secondary evidence; listed in the component inventory, not analyzed as code"]
        if e.get("analysis_status") == "pending":
            reasons.append("inventory analysis_status is pending (no fact uses it as evidence)")
        comp(e["type"], e["member"], e["path"], set([st]), reasons)
    excluded = [{"path": e["path"], "type": e["type"], "reason": e.get("classified_by")} for e in inv["files"] if e["type"] in ("placeholder", "repo-meta", "excluded")]

    # page reconciliation
    pages = {}
    for d, dirs, files in os.walk(out):
        for fn in files:
            rp = os.path.relpath(os.path.join(d, fn), out).replace("\\", "/")
            top = rp.split("/")[0] if "/" in rp else "(top level)"
            sub = "/".join(rp.split("/")[:-1]) or "(top level)"
            pages.setdefault(sub, {"md": 0, "other": 0})
            pages[sub]["md" if fn.endswith(".md") else "other"] += 1
    total_md = sum(v["md"] for v in pages.values())

    # statements whose only evidence is a comment, README, diagram or label (confidence Unverified)
    unverified = []
    seen_unv = set()

    def collect_unverified(o, parent, rel):
        if isinstance(o, dict):
            for ck, tk in (("confidence", None), ("comment_confidence", "comment")):
                if str(o.get(ck, "")).strip().lower() != "unverified":
                    continue
                text = o.get(tk) if tk else (o.get("text") or o.get("note") or o.get("comment") or o.get("statement"))
                if not text:
                    continue
                comp_name = o.get("job") or o.get("program") or o.get("member") or o.get("proc_label") or parent.get("job") \
                    or parent.get("program") or parent.get("member") or os.path.splitext(os.path.basename(rel))[0]
                src = o.get("source") or parent.get("source") or ""
                key = (comp_name, text)
                if key in seen_unv:
                    continue
                seen_unv.add(key)
                unverified.append({"component": comp_name, "statement": text, "source": src, "facts": rel})
            for v in o.values():
                collect_unverified(v, o, rel)
        elif isinstance(o, list):
            for x in o:
                collect_unverified(x, parent, rel)

    for d, dirs, files in os.walk(work):
        dirs[:] = sorted(x for x in dirs if x not in ("batches", "coverage", "structure"))
        for fn in sorted(files):
            if fn.endswith(".json") and fn not in ("inventory.json", "references.json"):
                fp = os.path.join(d, fn)
                collect_unverified(load(fp, {}), {}, os.path.relpath(fp, work).replace("\\", "/"))
    unverified.sort(key=lambda u: (u["facts"].split("/")[0], u["component"], u["source"]))

    counts = {}
    for c in comps:
        counts.setdefault(c["kind"], {})
        counts[c["kind"]][c["status"]] = counts[c["kind"]].get(c["status"], 0) + 1
    result = {"schema": "gaps/1", "generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "components": comps, "counts": counts,
              "sme_questions": sme, "conflicts": conflicts, "ambiguous_dependencies": ambiguous, "unresolved": unresolved,
              "unverified": unverified,
              "excluded": excluded, "pages": pages, "markdown_pages": total_md, "claimed_pages": claimed}
    f = open(os.path.join(work, "coverage", "gaps.json"), "w", encoding="utf-8", newline="\n")
    try:
        json.dump(result, f, indent=1, sort_keys=True)
    finally:
        f.close()

    L = ["# Gap report", "",
         "Generated by `gap_report.py` on %s from `docs/_work/coverage/coverage.json`, the structure, semantic and earlier work files. "
         "Every in-scope component has exactly one primary status; secondary flags are listed with it. "
         "The narrative register of earlier findings stays in [16-gaps-assumptions-open-questions.md](../16-gaps-assumptions-open-questions.md)." % result["generated"], "",
         "Status precedence: missing > unanalyzed > partially documented > unresolved > requires SME clarification > documented.", "",
         "## Summary by component type", "", "| Type | " + " | ".join(ORDER) + " | Total |", "|---|" + "---|" * (len(ORDER) + 1)]
    tot = dict((o, 0) for o in ORDER)
    for k in sorted(counts):
        row = [counts[k].get(o, 0) for o in ORDER]
        for o, n in zip(ORDER, row):
            tot[o] += n
        L.append("| %s | %s | %d |" % (k, " | ".join(str(n) for n in row), sum(row)))
    L.append("| **all** | %s | %d |" % (" | ".join(str(tot[o]) for o in ORDER), sum(tot.values())))
    L += ["", "Excluded from documentation with a reason: %d inventory entries (placeholders, repository metadata, excluded binaries). They are listed in `docs/_work/coverage/gaps.json` under `excluded`." % len(excluded)]
    L += ["", "## Page count reconciliation", ""]
    if claimed is not None:
        added = []
        for rel in RENDERER_PAGES:
            full = os.path.join(out, rel)
            if os.path.isdir(full):
                n = len([x for x in os.listdir(full) if x.endswith(".md")])
                if n:
                    added.append((rel + "/", n))
            elif os.path.isfile(full):
                added.append((rel, 1))
        n_added = sum(n for _, n in added)
        L.append("The earlier progress log reported %d Markdown documents. The package now holds %d Markdown pages (%d files of other types). "
                 "Pages that only `render_detail.py`, `coverage_validate.py` and `gap_report.py` produce account for %d of them: %s. "
                 "%d + %d = %d%s. All other pages existed before and were regenerated in place (programs, layouts, jobs) or left unchanged. "
                 "The earlier figure counted every Markdown file, including indexes and overview pages, not only detailed component pages."
                 % (claimed, total_md, sum(v["other"] for v in pages.values()), n_added,
                    ", ".join("`%s` (%d)" % a for a in added), claimed, n_added, claimed + n_added,
                    "" if claimed + n_added == total_md else "; the remaining difference of %d is unexplained and must be checked" % (total_md - claimed - n_added)))
        L.append("")
    L += ["| Folder | Markdown pages | Other files |", "|---|---|---|"]
    for k in sorted(pages):
        L.append("| %s | %d | %d |" % (k, pages[k]["md"], pages[k]["other"]))
    L += ["", "## Components that are not fully documented", ""]
    rows = [c for c in comps if c["status"] != "documented"]
    if rows:
        L += ["| Component | Type | Status | Flags | Reasons | Path |", "|---|---|---|---|---|---|"]
        for c in sorted(rows, key=lambda x: (ORDER.index(x["status"]), x["kind"], x["name"])):
            L.append("| %s | %s | %s | %s | %s | `%s` |" % (esc(c["name"]), c["kind"], c["status"], ", ".join(c["flags"][1:]), esc("; ".join(c["reasons"])), c["path"]))
    else:
        L.append("None.")
    L += ["", "## Unresolved items", "", "| Component | Item | Kind | What would resolve it | Source |", "|---|---|---|---|---|"]
    for u in unresolved:
        L.append("| %s | %s | %s | %s | `%s` |" % (esc(u["component"]), esc(u["item"]), esc(u["kind"]), esc(u["resolution"]), u.get("source") or ""))
    L += ["", "## Questions requiring SME clarification", "", "| Component | Question | Source |", "|---|---|---|"]
    for q in sme:
        L.append("| %s | %s | %s |" % (esc(q["component"]), esc(q["question"]), ("`%s`" % q["source"]) if q.get("source") else ""))
    L += ["", "## Unverified statements", "",
          "Statements whose only evidence is a source comment, a README, a diagram or a scheduler label. They are reported as written and are not used as "
          "evidence for any Confirmed fact; an SME or the runtime environment must confirm them. %d statements." % len(unverified), ""]
    if unverified:
        L += ["| Component | Statement | Source | Facts file |", "|---|---|---|---|"]
        for u in unverified:
            L.append("| %s | %s | %s | `docs/_work/%s` |" % (esc(u["component"]), esc(u["statement"]), ("`%s`" % u["source"]) if u["source"] else "", u["facts"]))
    else:
        L.append("None.")
    L += ["", "## Conflicting definitions", "", "| Component | Conflict | Origin | Source |", "|---|---|---|---|"]
    for cf in conflicts:
        L.append("| %s | %s | %s | %s |" % (esc(cf["component"]), esc(cf["text"]), esc(cf["origin"]), ("`%s`" % cf["source"]) if cf.get("source") else ""))
    L += ["", "## Ambiguous dependencies", "", "| From | Mechanism | Target expression | Candidates | Why ambiguous | Source |", "|---|---|---|---|---|---|"]
    for a in ambiguous:
        L.append("| %s | %s | %s | %s | %s | %s |" % (esc(a["from"]), esc(a["mechanism"]), esc(a["variable"]), esc(", ".join(str(x) for x in a["candidates"] if x)), esc(a["why"]),
                                                    ("`%s`" % a["source"]) if a.get("source") else ""))
    L += ["", "## Sources", "", "- `docs/_work/coverage/gaps.json`", "- `docs/_work/coverage/coverage.json`", "- `docs/_work/semantic/`", "- `docs/_work/xref/call-graph.json`",
          "- `docs/_work/batch/schedule.json`", "", "## Confidence", "", "Classification is computed by script. SME questions and conflict observations come from the batch analysis and carry their source lines."]
    p = os.path.join(out, "18-coverage", "gap-report.md")
    if not os.path.isdir(os.path.dirname(p)):
        os.makedirs(os.path.dirname(p))
    f = open(p, "w", encoding="utf-8", newline="\n")
    try:
        f.write("\n".join(L) + "\n")
    finally:
        f.close()
    sys.stdout.write("components=%d %s sme=%d conflicts=%d ambiguous=%d unresolved=%d unverified=%d pages=%d\n" % (
        len(comps), json.dumps(tot), len(sme), len(conflicts), len(ambiguous), len(unresolved), len(unverified), total_md))


if __name__ == "__main__":
    main(sys.argv)
