"""Compare the source inventory (ground truth) with the generated documentation.

Usage (from the repository root):
  python coverage_validate.py <work_dir> <output_dir> [--report-md <path>] [--json <path>]

Ground truth comes from <work_dir>/structure/** (re-run extract_structure.py
first) and <work_dir>/inventory.json. The documentation is <output_dir>/**.md.
Semantic status comes from <work_dir>/batches/*/checkpoint.json
(batch_manager.py check). Nothing here trusts a page merely because it exists:
each item must be present on the page that should document it, with its
source line reference where one applies.

Categories: programs, paragraphs (structural, semantic, logic grounding),
every procedure statement and decision point by line, unclassified
statements, program elements (EXEC, CALL, SELECT, data items by name+line),
copybooks, copybook fields (name+line) and 88-levels, copy edges, JCL jobs,
PROCs, steps, DDs, CICS transactions and resources, data definitions (DDL,
DBD, PSB), datasets, dependencies (call/transfer, job->program,
transaction->program), scheduler edges, dataflow edges, business-rule
decision coverage, rule traceability (anchor in cited lines, paragraph
exists, legacy rules re-verified, rule in catalog), and source references
(every `path:line` in the package must resolve).

Writes JSON (machine-readable) and Markdown (human-readable). Exit code 1
when any acceptance criterion fails. Python 3.1+ standard library only.
"""
import json
import os
import re
import sys
import time


def load(path, default=None):
    if not os.path.exists(path):
        return default
    f = open(path, "r", encoding="utf-8-sig")
    try:
        return json.load(f)
    finally:
        f.close()


def read(path):
    f = open(path, "r", encoding="utf-8")
    try:
        return f.read()
    finally:
        f.close()


def write(path, text):
    d = os.path.dirname(path)
    if d and not os.path.isdir(d):
        os.makedirs(d)
    f = open(path, "w", encoding="utf-8", newline="\n")
    try:
        f.write(text)
    finally:
        f.close()


class Cat(object):
    def __init__(self, name, kind, description):
        self.name, self.kind, self.description = name, kind, description
        self.items = []

    def add(self, key, status, detail=""):
        self.items.append({"item": key, "status": status, "detail": detail})

    def summary(self):
        tot = len(self.items)
        ok = sum(1 for i in self.items if i["status"] == "documented")
        part = sum(1 for i in self.items if i["status"] == "partial")
        miss = sum(1 for i in self.items if i["status"] == "missing")
        other = tot - ok - part - miss
        return {"category": self.name, "kind": self.kind, "description": self.description, "total": tot,
                "documented": ok, "partial": part, "missing": miss, "classified_other": other,
                "percent_documented": round(100.0 * ok / tot, 1) if tot else 100.0}


def norm_ws(s):
    return re.sub(r"\s+", " ", s)


STATEMENT_KEYS = ("decisions", "calculations", "io", "exec", "calls", "performs", "goto", "literal_moves", "data_moves",
                  "sets", "other_statements", "displays", "terminations", "unclassified")


def name_line_rows(text):
    """(name, line) pairs from layout table rows whose last cell is a line number."""
    out = set()
    for row in text.split("\n"):
        if not row.startswith("|"):
            continue
        cells = [x.strip() for x in row.strip().strip("|").split("|")]
        if len(cells) < 2 or not cells[-1].isdigit():
            continue
        for x in cells[:-1]:
            out.add((x.replace("&nbsp;", "").strip(), cells[-1]))
    return out


def main(argv):
    if len(argv) < 3:
        raise SystemExit(__doc__)
    work, out = argv[1], argv[2]
    md_path = argv[argv.index("--report-md") + 1] if "--report-md" in argv else os.path.join(out, "18-coverage", "coverage-report.md")
    js_path = argv[argv.index("--json") + 1] if "--json" in argv else os.path.join(work, "coverage", "coverage.json")
    S = os.path.join(work, "structure")
    inv = load(os.path.join(work, "inventory.json"))
    progs = dict((load(os.path.join(S, "programs", f))["member"], load(os.path.join(S, "programs", f)))
                 for f in sorted(os.listdir(os.path.join(S, "programs"))))
    cpys = dict((f[:-5], load(os.path.join(S, "copybooks", f))) for f in sorted(os.listdir(os.path.join(S, "copybooks"))))
    jcl = [load(os.path.join(S, "jcl", f)) for f in sorted(os.listdir(os.path.join(S, "jcl")))]
    usage = load(os.path.join(S, "copybook-usage.json"))["edges"]
    csd = load(os.path.join(S, "csd.json"))
    ddefs = load(os.path.join(S, "data-definitions.json"))
    callgraph = load(os.path.join(work, "xref", "call-graph.json"), {"edges": []})["edges"]
    checkpoints = {}
    bd = os.path.join(work, "batches")
    if os.path.isdir(bd):
        for b in sorted(os.listdir(bd)):
            cp = load(os.path.join(bd, b, "checkpoint.json"))
            if cp:
                for k, v in cp.get("programs", {}).items():
                    checkpoints[k] = v
                for k, v in cp.get("copybooks", {}).items():
                    checkpoints["CPY:" + k] = v

    pages = {}
    for d, dirs, files in os.walk(out):
        for fn in files:
            if fn.endswith(".md"):
                p = os.path.join(d, fn)
                pages[os.path.relpath(p, out).replace("\\", "/")] = read(p)
    corpus = "\n".join(pages.values())
    cats = []

    def page(relp):
        return pages.get(relp)

    # ------------------------------------------------ programs + paragraphs + elements
    c_prog = Cat("programs", "structural+semantic", "COBOL program page exists, cites the source, and semantic analysis validated")
    c_para_s = Cat("paragraphs-structural", "structural", "Paragraph listed on its program page with the exact line range")
    c_para_m = Cat("paragraphs-semantic", "semantic", "Paragraph has a validated logic description")
    c_exec = Cat("exec-commands", "structural", "Each EXEC CICS/SQL/DLI block cited on the program page")
    c_call = Cat("call-statements", "structural", "Each CALL cited on the program page")
    c_sel = Cat("file-selects", "structural", "Each SELECT/FD file documented on the program page")
    c_item = Cat("program-data-items", "structural", "Each data item coded in the program appears on its page")
    c_dec = Cat("decision-points", "semantic", "Business-candidate decision linked to a rule or a reviewed no-rule reason")
    c_rules = Cat("program-rule-analysis", "semantic", "Program has validated rules or a stated reason for having none")
    c_stmt = Cat("procedure-statements", "structural", "Every parsed procedure statement (all kinds, including field-to-field MOVEs) cited on the program page")
    c_uncl = Cat("unclassified-statements", "structural", "Statements the parser could not classify, shown on the program page")
    c_dall = Cat("decision-points-all", "structural", "Every IF/EVALUATE/WHEN, business-candidate or technical, cited on the program page")
    c_grnd = Cat("paragraph-logic-grounding", "semantic", "Paragraph description names an identifier, literal or the paragraph itself from its code")
    for pgm, s in sorted(progs.items()):
        rp = "07-programs/%s.md" % pgm
        t = page(rp)
        cp = checkpoints.get(pgm, {})
        if t is None:
            c_prog.add(pgm, "missing", "no page " + rp)
        elif s["source_path"] not in t:
            c_prog.add(pgm, "partial", "page does not cite " + s["source_path"])
        elif cp.get("status") != "validated":
            c_prog.add(pgm, "partial", "semantic status: %s" % (cp.get("status") or "unanalyzed"))
        else:
            c_prog.add(pgm, "documented")
        t = t or ""
        for p in s["paragraphs"]:
            key = "%s.%s" % (pgm, p["name"])
            rng = "%d-%d" % (p["start_line"], p["end_line"])
            if ("[%s](" % p["name"]) in t and ("| %s |" % rng) in t:
                c_para_s.add(key, "documented")
            elif p["name"] in t:
                c_para_s.add(key, "partial", "line range %s not shown" % rng)
            else:
                c_para_s.add(key, "missing")
        n_desc = cp.get("paragraphs_described", 0) if cp.get("status") == "validated" else 0
        sem = load(os.path.join(work, "semantic", "programs", pgm + ".json"), {}) or {}
        semp = dict((x.get("name"), x) for x in sem.get("paragraphs", []))
        for p in s["paragraphs"]:
            key = "%s.%s" % (pgm, p["name"])
            lg = (semp.get(p["name"]) or {}).get("logic") or ""
            if cp.get("status") == "validated" and len(lg.strip()) >= 15:
                c_para_m.add(key, "documented")
            elif len(lg.strip()) >= 15:
                c_para_m.add(key, "partial", "described but program semantic file not validated")
            else:
                c_para_m.add(key, "unanalyzed", "no logic description")
        for p in s["paragraphs"]:
            for e in p["exec"]:
                c_exec.add("%s:%d" % (pgm, e["line"]), "documented" if e["source"] in t else "missing", e.get("verb", ""))
            for x in p["calls"]:
                c_call.add("%s:%d" % (pgm, x["line"]), "documented" if x["source"] in t else "missing", x.get("target", ""))
            for d in p["decisions"]:
                if d["class"] != "business-candidate":
                    continue
                key = "%s:%d" % (pgm, d["line"])
                if cp.get("status") != "validated":
                    c_dec.add(key, "unanalyzed", "program semantics not validated")
                elif any(u["line"] == d["line"] for u in cp.get("uncovered_decisions", [])):
                    c_dec.add(key, "partial", "not linked to a rule or a no-rule reason: " + d["condition"][:80])
                else:
                    c_dec.add(key, "documented")
            for kind in STATEMENT_KEYS:
                for x in p.get(kind, []):
                    src = "`%s`" % x["source"]
                    c_stmt.add("%s:%d %s" % (pgm, x["line"], kind), "documented" if src in t else "missing", x["source"])
            for x in p.get("unclassified", []):
                c_uncl.add("%s:%d" % (pgm, x["line"]), "documented" if ("`%s`" % x["source"]) in t else "missing", x.get("first_word", ""))
            for d in p["decisions"]:
                c_dall.add("%s:%d" % (pgm, d["line"]), "documented" if ("`%s`" % d["source"]) in t and ("(%s)" % d["class"]) in t else "missing", d["class"])
        ungrounded = set(cp.get("ungrounded_paragraphs", []) or [])
        for p in s["paragraphs"]:
            key = "%s.%s" % (pgm, p["name"])
            if cp.get("status") != "validated" or "ungrounded_paragraphs" not in cp:
                c_grnd.add(key, "unanalyzed", "checkpoint has no grounding result; re-run batch_manager.py check")
            elif p["name"] in ungrounded:
                c_grnd.add(key, "partial", "description names nothing from the paragraph's code")
            else:
                c_grnd.add(key, "documented")
        for sel in s["selects"]:
            c_sel.add("%s.%s" % (pgm, sel["file"]), "documented" if (sel["source"] in t and sel["file"] in t) else "missing")
        rows_nl = name_line_rows(t)
        for it in s["data_items"]:
            if it["name"] == "FILLER":
                continue
            if (it["name"], str(it["line"])) in rows_nl:
                st_ = "documented"
            elif ("| %s |" % it["name"]) in t:
                st_ = "partial"
            else:
                st_ = "missing"
            c_item.add("%s.%s@%d" % (pgm, it["name"], it["line"]), st_, "" if st_ == "documented" else "name and line %d not on one row" % it["line"])
        if cp.get("status") == "validated":
            if cp.get("rules", 0) or cp.get("existing_reviewed", 0):
                c_rules.add(pgm, "documented", "%d new rules, %d legacy reviewed" % (cp.get("rules", 0), cp.get("existing_reviewed", 0)))
            elif sem.get("no_business_rules_reason"):
                c_rules.add(pgm, "documented", "no rules: " + sem["no_business_rules_reason"][:100])
            else:
                c_rules.add(pgm, "partial")
        else:
            c_rules.add(pgm, "unanalyzed")
    cats += [c_prog, c_para_s, c_para_m, c_grnd, c_stmt, c_uncl, c_dall, c_exec, c_call, c_sel, c_item, c_dec, c_rules]

    # ------------------------------------------------ copybooks
    c_cpy = Cat("copybooks", "structural+semantic", "Copybook/DCLGEN page exists, cites source, semantic purpose validated")
    c_fld = Cat("copybook-fields", "structural", "Each copybook field (non-FILLER) on its layout page")
    c_88 = Cat("copybook-88-levels", "structural", "Each level-88 condition on its layout page")
    c_cpara = Cat("copybook-paragraphs", "structural", "Procedure paragraphs inside copybooks listed on the layout page")
    for key, s in sorted(cpys.items()):
        cpy = s["member"]
        t = page("08-data/layouts/%s.md" % cpy)
        cp = checkpoints.get("CPY:" + cpy, {})
        if t is None:
            c_cpy.add(cpy, "missing")
            t = ""
        elif s["source_path"] not in t:
            c_cpy.add(cpy, "partial", "page does not cite source")
        elif cp.get("status") != "validated":
            c_cpy.add(cpy, "partial", "semantic status: %s" % (cp.get("status") or "unanalyzed"))
        else:
            c_cpy.add(cpy, "documented")
        rows_nl = name_line_rows(t)
        for it in s.get("data_items", []):
            if it["name"] != "FILLER":
                if (it["name"], str(it["line"])) in rows_nl:
                    c_fld.add("%s.%s@%d" % (cpy, it["name"], it["line"]), "documented")
                elif re.search(r"(\||;)\s*(&nbsp;)*" + re.escape(it["name"]) + r"\s*\|", t):
                    c_fld.add("%s.%s@%d" % (cpy, it["name"], it["line"]), "partial", "name and line %d not on one row" % it["line"])
                else:
                    c_fld.add("%s.%s@%d" % (cpy, it["name"], it["line"]), "missing")
            for cnd in it.get("conditions", []):
                c_88.add("%s.%s" % (cpy, cnd["name"]), "documented" if ("| %s |" % cnd["name"]) in t else "missing")
        for p in s.get("paragraphs", []):
            c_cpara.add("%s.%s" % (cpy, p["name"]), "documented" if ("| %s |" % p["name"]) in t else "missing")
    cats += [c_cpy, c_fld, c_88, c_cpara]

    # ------------------------------------------------ copy edges
    c_edge = Cat("copy-edges", "dependency", "Each COPY/INCLUDE statement cited on the user's page and in the usage matrix")
    matrix = page("17-dependencies/copybook-usage.md") or ""
    for u in usage:
        user_page = page("07-programs/%s.md" % u["from_member"]) if u["from_type"] == "cobol-program" else page("08-data/layouts/%s.md" % u["from_member"])
        ok = user_page is not None and u["source"] in user_page and u["source"] in matrix
        c_edge.add("%s->%s@%s" % (u["from_member"], u["copybook"], u["source"]), "documented" if ok else "missing")
    cats.append(c_edge)

    # ------------------------------------------------ JCL
    c_job = Cat("jcl-jobs", "structural", "JCL job page exists and cites the source")
    c_proc = Cat("jcl-procs", "structural", "PROC / JCL template page exists")
    c_step = Cat("jcl-steps", "structural", "Each EXEC step on the job/PROC page with its line reference")
    c_dd = Cat("jcl-dds", "structural", "Each DD statement on the job/PROC page with its line reference")
    c_cond = Cat("jcl-conditions", "structural", "Each COND / IF-THEN condition shown")
    for j in jcl:
        if j["artifact_type"] == "jcl-job":
            name = ((j.get("job") or {}).get("name") or j["member"]).upper()
            rp = "06-batch/jobs/%s.md" % name
            cat = c_job
        else:
            name = j["member"]
            rp = "06-batch/procs/%s.md" % name
            cat = c_proc
        t = page(rp)
        cat.add(name, "documented" if t is not None and j["source_path"] in t else "missing", j["source_path"])
        t = t or ""
        for st in j["steps"]:
            c_step.add("%s.%s@%s" % (name, st["name"], st["line"]), "documented" if ("### %s" % st["name"]) in t and st["source"] in t else "missing")
            if st.get("cond"):
                c_cond.add("%s.%s COND" % (name, st["name"]), "documented" if st["cond"].replace("|", "\\|") in t else "missing")
            for dd in st["dds"]:
                c_dd.add("%s.%s.%s@%d" % (name, st["name"], dd["ddname"], dd["line"]), "documented" if dd["source"] in t else "missing")
        for cnd in j["conditionals"]:
            c_cond.add("%s %s@%d" % (name, cnd["op"], cnd["line"]), "documented" if cnd["source"] in t else "missing")
    cats += [c_job, c_proc, c_step, c_dd, c_cond]

    # ------------------------------------------------ CICS
    c_tx = Cat("cics-transactions", "structural", "Transaction in the CSD page and the transaction catalog, program resolved")
    c_res = Cat("cics-resources", "structural", "Every CSD DEFINE listed with its source line")
    cpage = page("05-online/cics-resources.md") or ""
    tcat = page("05-online/transaction-catalog.md") or ""
    prog_names = set(progs) | set(e["member"].upper() for e in inv["files"] if e["type"] == "asm-program")
    for r in csd["resources"]:
        c_res.add("%s %s" % (r["type"], r["name"]), "documented" if r["source"] in cpage else "missing", r["source"])
        if r["type"] == "TRANSACTION":
            prog = r["attrs"].get("PROGRAM", "")
            if r["source"] not in cpage or r["name"] not in tcat:
                c_tx.add(r["name"], "missing", "not in cics-resources or transaction-catalog")
            elif prog not in prog_names:
                c_tx.add(r["name"], "unresolved", "PROGRAM(%s) has no source in the repository" % prog)
            else:
                c_tx.add(r["name"], "documented", "PROGRAM(%s)" % prog)
    cats += [c_tx, c_res]

    # ------------------------------------------------ data definitions and datasets
    c_ddl = Cat("data-definitions", "structural", "DDL objects, DBD segments and PSB PCBs named in the package")
    for o in ddefs["ddl"]:
        nm = o["name"].split(".")[-1]
        c_ddl.add("DDL %s %s" % (o["object"], o["name"]), "documented" if nm in corpus else "missing", o["source"])
    for d in ddefs["dbd"]:
        for sgm in d["segments"]:
            c_ddl.add("DBD %s.%s" % (d.get("name"), sgm["name"]), "documented" if sgm["name"] in corpus else "missing", sgm["source"])
    for p in ddefs["psb"]:
        for pcb in p["pcbs"]:
            c_ddl.add("PSB %s.%s" % (p.get("name"), pcb.get("label") or pcb.get("dbd")), "documented" if (pcb.get("dbd") or "") in corpus and (p.get("name") or "") in corpus else "missing", pcb["source"])
    c_dsn = Cat("datasets", "structural", "Every dataset name coded in JCL appears in the package")
    dsns = set()
    for j in jcl:
        for st in j["steps"]:
            for dd in st["dds"]:
                if dd.get("dsn") and not dd["dsn"].startswith("&&"):
                    dsns.add(dd.get("gdg_base") or dd["dsn"])
    for d in sorted(dsns):
        c_dsn.add(d, "documented" if d in corpus else "missing")
    cats += [c_ddl, c_dsn]

    # ------------------------------------------------ dependencies
    c_dep = Cat("dependencies", "dependency", "Call/transfer edges, job->program and transaction->program links documented")
    dep_page = page("17-dependencies/program-dependencies.md") or ""
    for e in callgraph:
        if e.get("from") in progs:
            ok = e["source"] in (page("07-programs/%s.md" % e["from"]) or "") or e["source"] in dep_page
            st = "documented" if ok else "missing"
            if e.get("mechanism") in ("XCTL", "RETURN-TRANSID", "CALL-dynamic", "LINK") and e.get("resolution_confidence") == "Inferred":
                st = "documented" if ok else "missing"
            c_dep.add("%s -%s-> %s @%s" % (e["from"], e.get("mechanism"), e.get("to"), e["source"]), st)
    for j in jcl:
        if j["artifact_type"] != "jcl-job":
            continue
        name = ((j.get("job") or {}).get("name") or j["member"]).upper()
        for st in j["steps"]:
            app = (st.get("application_program") or {}).get("program") or st.get("pgm") or ""
            if app.upper() in progs:
                c_dep.add("job %s.%s -> %s" % (name, st["name"], app), "documented" if st["source"] in dep_page else "missing")
    for r in csd["resources"]:
        if r["type"] == "TRANSACTION" and r["attrs"].get("PROGRAM") in progs:
            c_dep.add("tran %s -> %s" % (r["name"], r["attrs"]["PROGRAM"]), "documented" if r["source"] in dep_page else "missing")
    cats.append(c_dep)

    # ------------------------------------------------ rule traceability
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import batch_manager as bm

    def anchor_ok(ref, anchor):
        iss = []
        return bm.check_ref(ref, iss, "anchor", anchor) is not None and not iss
    c_rt = Cat("rule-traceability", "traceability", "Rule cites resolvable lines, its paragraph exists there, its anchor is in the cited code, and it is in the catalog")
    rules = (load(os.path.join(work, "rules", "rules.json"), {"rules": []}) or {}).get("rules", [])
    catalog = page("09-business-rules-catalog.md") or ""
    reviewed = {}
    rv_dir = os.path.join(work, "semantic", "reviews")
    rv_cp = (load(os.path.join(work, "batches", "reviews-checkpoint.json"), {}) or {}).get("members", {})
    if os.path.isdir(rv_dir):
        for fn in sorted(os.listdir(rv_dir)):
            if fn.endswith(".json") and (rv_cp.get(fn[:-5]) or {}).get("status") == "validated":
                for e in (load(os.path.join(rv_dir, fn), {}) or {}).get("existing_rules_reviewed", []):
                    reviewed[e.get("id")] = e
    for r in rules:
        probs = []
        impls = r.get("implementations", [])
        if not impls:
            probs.append("no implementation")
        for i in impls:
            iss = []
            pr = bm.check_ref(i.get("source"), iss, "impl")
            probs += iss
            if pr and i.get("paragraph") and i.get("program") in progs:
                pool = progs[i["program"]]["paragraphs"] if progs[i["program"]]["source_path"] == pr[0] else \
                    [p for s_ in cpys.values() if s_["source_path"] == pr[0] for p in s_.get("paragraphs", [])]
                names = [x.strip() for x in i["paragraph"].split(",") if x.strip()]
                para = [p for p in pool if p["name"] in names]
                lost = [x for x in names if x not in set(p["name"] for p in para)]
                if lost:
                    probs.append("paragraph %s not in %s" % (", ".join(lost), pr[0]))
                elif not any(p["start_line"] <= pr[2] and pr[1] <= p["end_line"] for p in para):
                    probs.append("%s lies outside paragraph %s" % (i["source"], i["paragraph"]))
        if r.get("anchor"):
            if not any(anchor_ok(i.get("source"), r["anchor"]) for i in impls):
                probs.append("anchor not found in any cited range")
        elif r.get("origin") == "legacy":
            v = r.get("verification") or reviewed.get(r["id"])
            if not v:
                probs.append("legacy rule not re-verified (no program semantics or reviews entry)")
            else:
                iss = []
                bm.check_ref(v.get("source"), iss, "verification", v.get("anchor", ""))
                probs += iss
        else:
            probs.append("no anchor")
        if r["id"] not in catalog:
            probs.append("not in 09-business-rules-catalog.md")
        c_rt.add(r["id"], "documented" if not probs else "partial", "; ".join(probs)[:300])
    cats.append(c_rt)

    # ------------------------------------------------ scheduler and dataflow edges
    sched = load(os.path.join(work, "batch", "schedule.json"), {}) or {}
    dflow = (load(os.path.join(work, "batch", "dataflow.json"), {}) or {}).get("edges", [])
    jobdep = page("17-dependencies/job-dependencies.md") or ""
    c_sch = Cat("scheduler-edges", "dependency", "Every CA7 trigger, Control-M condition and script submit shown on a job page or the job-dependency page")
    for e in sched.get("ca7_edges", []) + sched.get("controlm_edges", []):
        key = "%s %s -> %s @%s" % (e.get("kind"), e.get("from"), e.get("to"), e.get("source"))
        texts = [x for x in (page("06-batch/jobs/%s.md" % e.get("from")), page("06-batch/jobs/%s.md" % e.get("to"))) if x]
        hit = any(("`%s`" % e["source"]) in x and e["from"] in x and e["to"] in x for x in texts + [jobdep])
        cites = [e.get("source")] + ([e["incond_source"]] if e.get("kind") == "controlm-condition" else [])
        if e.get("kind") == "controlm-condition" and not e.get("incond_source"):
            c_sch.add(key, "partial", "Control-M edge has no INCOND line (run schedule_lines.py)")
        elif not all(re.search(r":\d+(-\d+)?$", s or "") for s in cites):
            c_sch.add(key, "partial", "scheduler citation has no line number")
        elif hit and not all(("`%s`" % s) in "".join(texts + [jobdep]) for s in cites):
            c_sch.add(key, "partial", "INCOND line not shown on a job or dependency page")
        elif hit:
            c_sch.add(key, "documented")
        elif not texts:
            c_sch.add(key, "unresolved", "neither job has a JCL page (scheduler job without JCL member)")
        else:
            c_sch.add(key, "missing")
    for e in sched.get("script_submits", []):
        key = "script %s -> %s @%s" % (e.get("script"), e.get("job"), e.get("source"))
        t = page("06-batch/jobs/%s.md" % e.get("job"))
        if t is None:
            c_sch.add(key, "unresolved", "job %s has no JCL page" % e.get("job"))
        elif not re.search(r":\d+(-\d+)?$", e.get("source") or ""):
            c_sch.add(key, "partial", "script citation has no line number")
        else:
            c_sch.add(key, "documented" if ("`%s`" % e["source"]) in t else "missing")
    c_dfl = Cat("dataflow-edges", "dependency", "Every job/step/dataset edge shown on the job page with its DD line")
    for e in dflow:
        key = "%s.%s %s @%s" % (e.get("job"), e.get("step"), e.get("dsn"), e.get("source"))
        t = page("06-batch/jobs/%s.md" % e.get("job"))
        if t is None:
            c_dfl.add(key, "missing", "no job page")
        else:
            starts = re.search(re.escape("`" + e["source"]) + r"(?:-\d+)?`", t) is not None
            c_dfl.add(key, "documented" if starts and (e.get("dsn") or "") in t else "missing")
    cats += [c_sch, c_dfl]

    # ------------------------------------------------ inventory completeness
    c_inv = Cat("inventory-artifacts", "structural", "Every inventoried artifact named in the package or excluded with a reason")
    for e in inv["files"]:
        if e["type"] in ("placeholder", "repo-meta", "excluded"):
            c_inv.add(e["path"], "excluded", "type %s: %s" % (e["type"], e.get("classified_by", "")))
            continue
        m = e["member"].upper()
        found = e["path"] in corpus or re.search(r"(?<![A-Z0-9@#$-])" + re.escape(m) + r"(?![A-Z0-9@#$-])", corpus.upper()) is not None
        c_inv.add(e["path"], "documented" if found else "missing", e["type"])
    cats.append(c_inv)

    # ------------------------------------------------ source references
    c_ref = Cat("source-references", "traceability", "Every `path:line` reference in the package resolves to an existing file and line range")
    line_counts = {}
    seen = set()
    for relp, t in sorted(pages.items()):
        for m in re.finditer(r"`([A-Za-z0-9_./-]+\.[A-Za-z0-9]+):(\d+)(?:-(\d+))?`", t):
            pth, a, b = m.group(1), int(m.group(2)), int(m.group(3) or m.group(2))
            key = (pth, a, b)
            if key in seen:
                continue
            seen.add(key)
            if pth not in line_counts:
                if os.path.isfile(pth):
                    ff = open(pth, "rb")
                    try:
                        parts = ff.read().decode("latin-1").replace("\r\n", "\n").replace("\r", "\n").split("\n")
                        if parts and parts[-1] == "":
                            parts.pop()
                        line_counts[pth] = len(parts)
                    finally:
                        ff.close()
                else:
                    line_counts[pth] = None
            n = line_counts[pth]
            ref = "%s:%d-%d" % key
            if n is None:
                c_ref.add(ref, "missing", "file not found (first seen in %s)" % relp)
            elif a < 1 or b > n or a > b:
                c_ref.add(ref, "missing", "outside 1-%d (first seen in %s)" % (n, relp))
            else:
                c_ref.add(ref, "documented")
    cats.append(c_ref)

    # ------------------------------------------------ results and acceptance
    summaries = [c.summary() for c in cats]
    by = dict((s["category"], s) for s in summaries)
    criteria = []

    def crit(name, ok, measured, target):
        criteria.append({"criterion": name, "pass": bool(ok), "measured": measured, "target": target})

    for cname in ("programs", "paragraphs-structural", "exec-commands", "call-statements", "file-selects", "program-data-items",
                  "copybooks", "copybook-fields", "copybook-88-levels", "copybook-paragraphs", "copy-edges", "jcl-jobs", "jcl-procs",
                  "jcl-steps", "jcl-dds", "jcl-conditions", "cics-resources", "data-definitions", "datasets", "dependencies",
                  "procedure-statements", "decision-points-all", "dataflow-edges"):
        s = by[cname]
        crit("%s fully documented" % cname, s["documented"] == s["total"], "%d/%d (%.1f%%)" % (s["documented"], s["total"], s["percent_documented"]), "100%")
    s = by["paragraphs-semantic"]
    crit("every paragraph has a validated logic description", s["documented"] == s["total"], "%d/%d (%.1f%%)" % (s["documented"], s["total"], s["percent_documented"]), "100%")
    s = by["paragraph-logic-grounding"]
    crit("every paragraph description names something from its code", s["documented"] == s["total"], "%d/%d (%.1f%%)" % (s["documented"], s["total"], s["percent_documented"]), "100%")
    s = by["unclassified-statements"]
    crit("statements the parser could not classify are shown on the page", s["missing"] == 0, "%d unclassified, %d not shown" % (s["total"], s["missing"]), "0 not shown")
    s = by["rule-traceability"]
    crit("every rule (new and legacy) traceable to verified source and in the catalog", s["documented"] == s["total"], "%d/%d (%.1f%%)" % (s["documented"], s["total"], s["percent_documented"]), "100%")
    s = by["scheduler-edges"]
    crit("scheduler edges documented or classified unresolved", s["missing"] == 0, "%d documented, %d unresolved, %d missing" % (s["documented"], s["classified_other"], s["missing"]), "0 missing")
    s = by["program-rule-analysis"]
    crit("every program has validated rules or a no-rule reason", s["documented"] == s["total"], "%d/%d" % (s["documented"], s["total"]), "100%")
    s = by["decision-points"]
    crit("business-candidate decision points linked to a rule or reviewed reason", s["documented"] == s["total"], "%d/%d (%.1f%%)" % (s["documented"], s["total"], s["percent_documented"]), "100%")
    s = by["cics-transactions"]
    crit("CICS transactions documented or classified unresolved", s["missing"] == 0, "%d documented, %d unresolved, %d missing" % (s["documented"], s["classified_other"], s["missing"]), "0 missing")
    s = by["inventory-artifacts"]
    crit("every inventoried artifact documented or excluded with reason", s["missing"] == 0, "%d documented, %d excluded, %d missing" % (s["documented"], s["classified_other"], s["missing"]), "0 missing")
    s = by["source-references"]
    crit("every source reference resolves", s["missing"] == 0, "%d of %d distinct references valid" % (s["documented"], s["total"]), "0 invalid")

    report = {"schema": "coverage/1", "generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "summaries": summaries,
              "criteria": criteria, "all_pass": all(c["pass"] for c in criteria),
              "details": dict((c.name, [i for i in c.items if i["status"] != "documented"]) for c in cats),
              "documents": len(pages)}
    d = os.path.dirname(js_path)
    if d and not os.path.isdir(d):
        os.makedirs(d)
    f = open(js_path, "w", encoding="utf-8", newline="\n")
    try:
        json.dump(report, f, indent=1, sort_keys=True)
    finally:
        f.close()

    L = ["# Coverage report", "",
         "Generated by `coverage_validate.py` on %s. It compares the source inventory parsed by `extract_structure.py` "
         "with the %d Markdown pages of this package. A page existing is not enough: each item must appear on the page "
         "that should document it, with its line reference where one applies. Semantic coverage (paragraph logic, rules, "
         "decision points) is counted only for programs whose batch analysis passed `batch_manager.py check`." % (report["generated"], len(pages)), "",
         "Overall: **%s** (%d of %d acceptance criteria pass)." % ("PASS" if report["all_pass"] else "FAIL", sum(1 for c in criteria if c["pass"]), len(criteria)), "",
         "## Acceptance criteria", "", "| Criterion | Measured | Target | Result |", "|---|---|---|---|"]
    for c in criteria:
        L.append("| %s | %s | %s | %s |" % (c["criterion"], c["measured"], c["target"], "pass" if c["pass"] else "FAIL"))
    L += ["", "## Coverage by category", "", "| Category | Kind | Total | Documented | Partial | Missing | Other (unanalyzed, unresolved, excluded) | % documented |",
          "|---|---|---|---|---|---|---|---|"]
    for s in summaries:
        L.append("| %s | %s | %d | %d | %d | %d | %d | %.1f |" % (s["category"], s["kind"], s["total"], s["documented"], s["partial"], s["missing"], s["classified_other"], s["percent_documented"]))
    L += ["", "## What these numbers do not prove", "",
          "- Structural coverage means every parsed element appears on its page with a line reference. It does not prove that the prose explains the element correctly.",
          "- Semantic coverage counts paragraph descriptions and rules that passed automated checks: every rule anchor was found verbatim in its cited lines, and every paragraph has a description. The checks cannot judge whether a description is complete or a rule is the right business interpretation; that needs SME review (see the gap report).",
          "- Paragraph-logic grounding only proves that each description names an identifier, literal or the paragraph itself from the paragraph's code. It catches generic or misplaced text, not wrong text.",
          "- Business-candidate decision points are selected by a keyword heuristic (`TECH_PATTERNS` in `extract_structure.py`). Technical decisions (file status, RESP, keys, pseudo-conversation) are counted in `decision-points-all`, which checks that they are cited on the page, not that a rule explains them.",
          "- `procedure-statements` counts statements found by a line-oriented parser. Statements it splits or merges differently from a compiler are still cited by line, but the parser is not a COBOL compiler.",
          "- Rule traceability proves that each rule's anchor text occurs in the cited lines and that the paragraph exists there. It does not prove that the rule statement is the correct business reading of that code.",
          "- Data items are matched by name and source line on one table row; a `partial` means the name appears but not with its line (for example a duplicate name at another level).",
          "- 100% here is therefore not a claim of 100% semantic correctness.", "",
          "## Items not fully documented", ""]
    any_open = False
    for c in cats:
        open_items = [i for i in c.items if i["status"] not in ("documented", "excluded")]
        if not open_items:
            continue
        any_open = True
        L += ["### %s (%d)" % (c.name, len(open_items)), ""]
        L += ["| Item | Status | Detail |", "|---|---|---|"]
        for i in open_items[:200]:
            L.append("| %s | %s | %s |" % (i["item"].replace("|", "\\|"), i["status"], (i["detail"] or "").replace("|", "\\|")))
        if len(open_items) > 200:
            L.append("| ... | | %d more in `docs/_work/coverage/coverage.json` |" % (len(open_items) - 200))
        L.append("")
    if not any_open:
        L.append("None.")
    L += ["", "## Sources", "", "- `docs/_work/coverage/coverage.json`", "- `docs/_work/structure/`", "- `docs/_work/batches/`", "",
          "## Confidence", "", "All counts are computed by script from the files listed above."]
    write(md_path, "\n".join(L) + "\n")
    for c in criteria:
        sys.stdout.write("%-4s %-75s %s\n" % ("ok" if c["pass"] else "FAIL", c["criterion"], c["measured"]))
    sys.stdout.write("documents=%d all_pass=%s\n" % (len(pages), report["all_pass"]))
    sys.exit(0 if report["all_pass"] else 1)


if __name__ == "__main__":
    main(sys.argv)
