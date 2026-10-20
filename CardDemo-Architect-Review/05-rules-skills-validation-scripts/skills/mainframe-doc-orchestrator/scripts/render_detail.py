"""Render detailed component pages from structure + semantic + legacy work facts.

Usage (from the repository root):
  python render_detail.py <work_dir> <output_dir>

Reads  <work_dir>/structure/**   (extract_structure.py, ground truth)
       <work_dir>/semantic/**    (batch analysis, validated by batch_manager.py)
       <work_dir>/programs, jobs, layouts, xref, batch, rules (earlier phase facts)
Writes <output_dir>/07-programs/<PGM>.md and index.md      (every COBOL program)
       <output_dir>/08-data/layouts/<CPY>.md                (every copybook / DCLGEN)
       <output_dir>/06-batch/jobs/<JOB>.md                  (every JCL job)
       <output_dir>/05-online/cics-resources.md             (every CSD definition)
       <output_dir>/09-business-rules-catalog.md            (all rules + no-rule programs)
       <output_dir>/17-dependencies/*.md                    (program, copybook, job dependencies)
       <work_dir>/rules/rules.json (consolidated; legacy copy kept in rules-legacy.json)
Only facts present in the inputs are rendered; missing semantics are shown as
"Not analyzed" so the coverage validator can count them. Python 3.1+.
"""
import json
import os
import re
import shutil
import sys

SYSTEM_PROGRAMS = set(["CEE3ABD", "CEEDAYS", "CBLTDLI", "MQOPEN", "MQGET", "MQPUT", "MQPUT1", "MQCLOSE",
                       "MQCONN", "MQDISC", "DSNTIAR", "IKJEFT01", "DFSRRC00", "CEEGMT", "CEELOCT", "AIBTDLI"])


# ----------------------------------------------------------------- io helpers
def load(path, default=None):
    if not os.path.exists(path):
        return default
    f = open(path, "r", encoding="utf-8-sig")
    try:
        return json.load(f)
    finally:
        f.close()


def save(path, obj):
    d = os.path.dirname(path)
    if d and not os.path.isdir(d):
        os.makedirs(d)
    f = open(path, "w", encoding="utf-8", newline="\n")
    try:
        json.dump(obj, f, indent=1, sort_keys=True)
        f.write("\n")
    finally:
        f.close()


def write(path, lines):
    d = os.path.dirname(path)
    if d and not os.path.isdir(d):
        os.makedirs(d)
    text = "\n".join(lines).rstrip() + "\n"
    f = open(path, "w", encoding="utf-8", newline="\n")
    try:
        f.write(text)
    finally:
        f.close()


def cell(v):
    if v is None:
        return ""
    if isinstance(v, (list, tuple)):
        v = ", ".join(str(x) for x in v)
    s = str(v).replace("\r", " ").replace("\n", " ").replace("|", "\\|")
    return s.strip()


def code(v):
    s = cell(v).replace("`", "'")
    return "`%s`" % s if s else ""


def rel(from_dir, to_path):
    return os.path.relpath(to_path, from_dir).replace("\\", "/")


def table(header, rows):
    out = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    for r in rows:
        out.append("| " + " | ".join(cell(x) if not (isinstance(x, str) and x.startswith("`")) else x for x in r) + " |")
    return out


def anchor_id(name):
    return re.sub(r"[^a-z0-9 -]", "", name.lower()).replace(" ", "-")


# ----------------------------------------------------------------- context
class Ctx(object):
    pass


def load_ctx(work, out):
    c = Ctx()
    c.work, c.out = work, out
    c.inv = load(os.path.join(work, "inventory.json"))
    c.progs = {}
    for fn in sorted(os.listdir(os.path.join(work, "structure", "programs"))):
        s = load(os.path.join(work, "structure", "programs", fn))
        c.progs[s["member"]] = s
    c.cpys = {}
    for fn in sorted(os.listdir(os.path.join(work, "structure", "copybooks"))):
        c.cpys[fn[:-5]] = load(os.path.join(work, "structure", "copybooks", fn))
    c.jcl = {}
    for fn in sorted(os.listdir(os.path.join(work, "structure", "jcl"))):
        j = load(os.path.join(work, "structure", "jcl", fn))
        c.jcl[j["source_path"]] = j
    c.usage = load(os.path.join(work, "structure", "copybook-usage.json"))["edges"]
    c.csd = load(os.path.join(work, "structure", "csd.json"))
    c.ddefs = load(os.path.join(work, "structure", "data-definitions.json"))
    c.sem = {}
    sd = os.path.join(work, "semantic", "programs")
    if os.path.isdir(sd):
        for fn in os.listdir(sd):
            c.sem[fn[:-5]] = load(os.path.join(sd, fn))
    c.reviews = {}
    sd = os.path.join(work, "semantic", "reviews")
    if os.path.isdir(sd):
        for fn in os.listdir(sd):
            if fn.endswith(".json"):
                c.reviews[fn[:-5]] = load(os.path.join(sd, fn))
    c.review_checks = (load(os.path.join(work, "batches", "reviews-checkpoint.json"), {}) or {}).get("members", {})
    c.csem = {}
    sd = os.path.join(work, "semantic", "copybooks")
    if os.path.isdir(sd):
        for fn in os.listdir(sd):
            c.csem[fn[:-5]] = load(os.path.join(sd, fn))
    c.old_prog = {}
    for fn in os.listdir(os.path.join(work, "programs")):
        c.old_prog[fn[:-5]] = load(os.path.join(work, "programs", fn))
    c.old_jobs = {}
    for fn in os.listdir(os.path.join(work, "jobs")):
        j = load(os.path.join(work, "jobs", fn))
        c.old_jobs[j["source_path"]] = (fn[:-5], j)
    c.callgraph = load(os.path.join(work, "xref", "call-graph.json"), {"edges": []})["edges"]
    c.schedule = load(os.path.join(work, "batch", "schedule.json"), {})
    c.dataflow = (load(os.path.join(work, "batch", "dataflow.json"), {}) or {}).get("edges", [])
    legacy_p = os.path.join(work, "rules", "rules-legacy.json")
    if not os.path.exists(legacy_p):
        shutil.copyfile(os.path.join(work, "rules", "rules.json"), legacy_p)
    c.legacy_rules = load(legacy_p)["rules"]
    c.checkpoints = {}
    bd = os.path.join(work, "batches")
    if os.path.isdir(bd):
        for b in os.listdir(bd):
            cp = load(os.path.join(bd, b, "checkpoint.json"))
            if cp:
                for k, v in cp.get("programs", {}).items():
                    c.checkpoints[k] = v
                for k, v in cp.get("copybooks", {}).items():
                    c.checkpoints["CPY:" + k] = v
    # job -> steps running each program
    c.prog_steps = {}
    for path, j in c.jcl.items():
        if j["artifact_type"] != "jcl-job":
            continue
        jobname = (j.get("job") or {}).get("name") or j["member"]
        for st in j["steps"]:
            for p in set([(st.get("pgm") or "").upper(), ((st.get("application_program") or {}).get("program") or "").upper()]):
                if p:
                    c.prog_steps.setdefault(p, []).append((jobname, j, st))
    c.transactions = [r for r in c.csd["resources"] if r["type"] == "TRANSACTION"]
    c.csd_files = dict((r["name"], r) for r in c.csd["resources"] if r["type"] == "FILE")
    c.job_page = {}
    for path, j in c.jcl.items():
        if j["artifact_type"] == "jcl-job":
            c.job_page[path] = ((j.get("job") or {}).get("name") or j["member"]).upper()
    return c


# ----------------------------------------------------------------- rules
def new_rules(c):
    out = []
    for pgm in sorted(c.sem):
        s = c.sem[pgm]
        for r in s.get("rules", []):
            rr = dict(r)
            rr["program"] = pgm
            out.append(rr)
    return out


def legacy_reviews(c):
    rev = {}
    for pgm, s in c.sem.items():
        for e in s.get("existing_rules_reviewed", []):
            rev[e.get("id")] = dict(e, program=pgm)
    for member, s in c.reviews.items():
        if (c.review_checks.get(member) or {}).get("status") != "validated":
            continue
        for e in s.get("existing_rules_reviewed", []):
            rev.setdefault(e.get("id"), dict(e, program=member))
    return rev


def consolidate_rules(c):
    rev = legacy_reviews(c)
    rules = []
    for r in c.legacy_rules:
        x = dict(r)
        if r["id"] in rev:
            x["verification"] = {k: rev[r["id"]].get(k) for k in ("verdict", "source", "anchor", "note", "program")}
        x["origin"] = "legacy"
        rules.append(x)
    for r in new_rules(c):
        rules.append({
            "id": r["id"], "category": r.get("category"), "statement": r.get("statement"),
            "confidence": r.get("confidence"), "conditions": r.get("conditions"), "outcome": r.get("outcome"),
            "data": r.get("data", []), "messages": r.get("messages", []), "origin": "batch-analysis",
            "anchor": r.get("anchor"),
            "implementations": [{"program": r["program"], "paragraph": r.get("paragraph"), "source": r.get("source"),
                                 "copybook": r.get("copybook")}] +
                               [{"program": r["program"], "source": s2} for s2 in r.get("additional_sources", [])]})
    save(os.path.join(c.work, "rules", "rules.json"), {"schema": "rules/2", "rules": rules,
                                                       "note": "Legacy rules are kept with their batch review verdict under 'verification'."})
    return rules


def rules_for_program(c, pgm, all_rules):
    out = []
    for r in all_rules:
        if any(i.get("program") == pgm for i in r.get("implementations", [])):
            out.append(r)
    return out


# ----------------------------------------------------------------- program page
def resolve_value(s, name):
    if not name:
        return None
    n = name.strip().strip("'\"")
    if name.strip()[:1] in ("'", '"'):
        return n
    for it in s["data_items"]:
        if it["name"] == n.upper() and it.get("value"):
            m = re.match(r"^['\"](.*?)['\"]", it["value"])
            if m:
                return m.group(1).strip()
    return None


def program_page(c, pgm, all_rules):
    s = c.progs[pgm]
    sem = c.sem.get(pgm) or {}
    old = c.old_prog.get(pgm) or {}
    path = s["source_path"]
    pdir = os.path.join(c.out, "07-programs")
    cp = c.checkpoints.get(pgm, {})
    semantic_ok = cp.get("status") == "validated"
    L = ["# Program %s" % pgm, ""]
    rt = ", ".join(old.get("runtime_type", [])) or "Not recorded"
    txs = [t for t in c.transactions if t["attrs"].get("PROGRAM") == pgm]
    steps = c.prog_steps.get(pgm, [])
    ident = s.get("identification", {})
    rows = [("Source", "`%s`" % path), ("Lines", "%d total, %d code, %d comment, %d blank" % (
        s["loc"]["total"], s["loc"]["code"], s["loc"]["comment"], s["loc"]["blank"])),
        ("PROGRAM-ID", ident.get("PROGRAM-ID", {}).get("value", "")),
        ("Author", ident.get("AUTHOR", {}).get("value", "")),
        ("Runtime", rt), ("Module", old.get("module") or ""),
        ("CICS transactions", ", ".join("%s (`%s`)" % (t["name"], t["source"]) for t in txs) or "None in CSD"),
        ("JCL steps", ", ".join("[%s](../06-batch/jobs/%s.md).%s (`%s`)" % (jn, jn, st["name"], st["source"]) for jn, j, st in steps) or "None"),
        ("Paragraphs", str(s["counts"]["paragraphs"])),
        ("Semantic analysis", "validated (batch %s)" % sem.get("batch") if semantic_ok else "NOT validated - see coverage report"),
        ("Version banner", (old.get("header") or {}).get("version_banner", ""))]
    L += ["| Item | Value |", "|---|---|"]
    for k, v in rows:
        v = v or ""
        L.append("| %s | %s |" % (k, v if v.startswith("`") or v.startswith("[") else cell(v)))
    L += ["", "## Summary", ""]
    summ = sem.get("summary") or {}
    if summ.get("text"):
        L.append("%s (%s)" % (summ["text"], summ.get("confidence", "Inferred")))
        if summ.get("evidence"):
            L += ["", "Evidence: " + ", ".join("`%s`" % e for e in summ["evidence"])]
    else:
        L.append("Not analyzed - no validated semantic summary for this program.")
    hdr = old.get("header") or {}
    if hdr.get("description"):
        L += ["", "Header comment (Unverified, `%s`): %s" % (hdr.get("source", path), cell(hdr["description"]))]

    # divisions
    L += ["", "## Divisions and sections", ""]
    rows = [(d["name"] + " DIVISION", "`%s`" % d["source"], ", ".join(d.get("using", [])) and "USING " + " ".join(d.get("using", []))) for d in s["divisions"]]
    rows += [(x["division"] + " / " + x["name"] + " SECTION", "`%s`" % x["source"], "") for x in s["sections"]]
    rows += [("PROCEDURE / " + x["name"] + " SECTION", "`%s`" % x["source"], "%d paragraphs" % len(x["paragraphs"])) for x in s["procedure_sections"]]
    L += table(["Division / section", "Lines", "Notes"], rows)

    # files
    L += ["", "## Files and data stores", ""]
    if s["selects"]:
        rows = []
        for sel in s["selects"]:
            dd = sel["assign"].split("-")[-1]
            phys = []
            for jn, j, st in steps:
                for d in st["dds"]:
                    if d["ddname"] in (sel["assign"], dd) and d.get("dsn"):
                        phys.append("%s (%s.%s `%s`)" % (d["dsn"], jn, st["name"], d["source"]))
            modes = []
            for p in s["paragraphs"]:
                for io in p["io"]:
                    if io["verb"] == "OPEN":
                        for m, fl in io.get("files", {}).items():
                            if sel["file"] in fl:
                                modes.append("%s (line %d)" % (m, io["line"]))
            fd = [f for f in s["fds"] if f["file"] == sel["file"]]
            rows.append((sel["file"], sel["assign"], sel.get("organization", ""), sel.get("access", ""),
                         sel.get("record_key", ""), sel.get("alternate_key", ""), sel.get("file_status", ""),
                         ", ".join(sorted(set(modes))), "; ".join(phys) or "No JCL step found for this program",
                         "`%s`" % sel["source"] + (", FD `%s`" % fd[0]["source"] if fd else "")))
        L += table(["File", "ASSIGN", "Org", "Access", "Record key", "Alt key", "Status field", "OPEN modes",
                    "Physical dataset (JCL)", "Evidence"], rows)
    else:
        L.append("No SELECT entries (no COBOL file I/O).")
    cics_files = []
    for p in s["paragraphs"]:
        for e in p["exec"]:
            if e.get("kind") == "CICS":
                for rsc in e.get("resources", []):
                    if rsc["type"] in ("FILE", "DATASET"):
                        lit = resolve_value(s, rsc["value"])
                        csdf = c.csd_files.get((lit or "").upper())
                        cics_files.append((e["verb"], rsc["value"], lit or "unresolved",
                                           (csdf or {}).get("attrs", {}).get("DSNAME", "") if csdf else "",
                                           "`%s`" % csdf["source"] if csdf else "", "`%s`" % e["source"]))
    if cics_files:
        L += ["", "CICS file commands (file name resolved from VALUE clauses and the CSD):", ""]
        L += table(["Command", "FILE option", "Resolved name", "CSD DSNAME", "CSD evidence", "Line"], cics_files)
    crud = old.get("crud") or []
    if crud:
        L += ["", "CRUD summary from the program facts:", ""]
        L += table(["Store", "Kind", "Ops", "Evidence"], [(x["store"], x.get("store_kind", ""), ", ".join(x["ops"]), "`%s`" % x["source"]) for x in crud])

    # embedded commands
    L += ["", "## Embedded CICS, SQL and DL/I commands", ""]
    rows = []
    for p in s["paragraphs"]:
        for e in p["exec"]:
            res = ", ".join("%s(%s)" % (r["type"], r["value"]) for r in e.get("resources", []))
            if e.get("kind") == "SQL":
                res = ", ".join(e.get("tables", [])) + (" cursor " + e["cursor"] if e.get("cursor") else "")
            if e.get("kind") == "DLI":
                res = ", ".join(e.get("segments", [])) + (" PCB " + e["pcb"] if e.get("pcb") else "")
            resp = "RESP" if e.get("resp") else ("NOHANDLE" if e.get("nohandle") else "")
            rows.append((p["name"], e.get("kind"), e.get("verb", ""), res, resp, "`%s`" % e["source"]))
    L += table(["Paragraph", "Kind", "Verb", "Resources", "Response", "Lines"], rows) if rows else ["No EXEC blocks."]

    # calls
    L += ["", "## Calls, transfers and callers", ""]
    rows = []
    for p in s["paragraphs"]:
        for cl in p["calls"]:
            kind = "system/LE" if cl.get("target") in SYSTEM_PROGRAMS else ("dynamic" if cl.get("dynamic") else "static")
            rows.append(("CALL " + kind, cl.get("target", ""), ", ".join(cl.get("using", [])), p["name"], "`%s`" % cl["source"]))
        for e in p["exec"]:
            if e.get("kind") == "CICS" and e.get("verb") in ("XCTL", "LINK", "START", "RETURN"):
                o = e.get("options", {})
                tgt = o.get("PROGRAM") or o.get("TRANSID") or ""
                if e["verb"] == "RETURN" and not tgt:
                    continue
                lit = resolve_value(s, tgt)
                res = [x for x in c.callgraph if x.get("from") == pgm and x.get("source", "").endswith(":%d" % e["line"])]
                resolved = lit or ", ".join(sorted(set(t["target"] for x in res for t in x.get("resolved_to", []))))
                rows.append(("EXEC CICS " + e["verb"], tgt + (" = " + resolved if resolved and resolved != tgt else ""),
                             o.get("COMMAREA", ""), p["name"], "`%s`" % e["source"]))
    L += table(["Mechanism", "Target", "Parameters", "Paragraph", "Lines"], rows) if rows else ["No CALL, XCTL, LINK or START."]
    callers = []
    for x in c.callgraph:
        tg = [x.get("to")] + [t.get("target") for t in x.get("resolved_to", [])]
        if pgm in tg and x.get("from") != pgm:
            callers.append((x["from"], x.get("mechanism"), x.get("resolution_confidence") or x.get("confidence"), "`%s`" % x["source"]))
    if callers:
        L += ["", "Programs that transfer to or call this program (from `docs/_work/xref/call-graph.json`):", ""]
        L += table(["Caller", "Mechanism", "Confidence", "Evidence"], sorted(set(callers)))

    # copybooks
    L += ["", "## Copybooks", ""]
    rows = []
    for u in c.usage:
        if u["from"] != path:
            continue
        tgt = u["copybook"]
        link = tgt
        if u["resolution"] == "inventory" and u.get("resolved_path"):
            t = [e for e in c.inv["files"] if e["path"] == u["resolved_path"]]
            if t and t[0]["type"] in ("cobol-copybook", "db2-dclgen"):
                link = "[%s](../08-data/layouts/%s.md)" % (tgt, tgt)
        rows.append((link, u["kind"], u["resolution"] + (" (commented out)" if u["commented"] else ""),
                     u.get("resolved_path") or "", u.get("replacing", ""), "`%s`" % u["source"]))
    L += table(["Copybook", "Statement", "Resolution", "Resolved path", "REPLACING", "Line"], rows) if rows else ["No COPY statements."]

    # data division
    L += ["", "## Data division items", "",
          "Every data entry coded in this source (copybook contents are on the copybook pages). Lengths are computed from PIC and USAGE.", ""]
    rows = []
    for it in s["data_items"]:
        conds = "; ".join("%s = %s" % (x["name"], x["value"]) for x in it.get("conditions", []))
        occ = ""
        if it.get("occurs"):
            occ = "%s%s%s" % (it.get("occurs_min", "") and "%s TO " % it["occurs_min"], it["occurs"],
                               " DEPENDING ON " + it["depending_on"] if it.get("depending_on") else "")
        rows.append((it.get("section", ""), "%02d" % it["level"] if it["level"] else "SQL", it["name"], it.get("pic", ""),
                     it.get("usage", ""), it.get("length", ""), occ, it.get("redefines", ""),
                     (it.get("value") or it.get("sql", ""))[:80], conds[:200], it["line"]))
    L += table(["Section", "Lvl", "Name", "PIC", "Usage", "Len", "OCCURS", "REDEFINES", "VALUE", "88-levels", "Line"], rows) if rows else ["No data entries."]

    # statement inventory
    kinds = [("decisions", "Decisions (IF, EVALUATE, WHEN, loops, handlers)"), ("calculations", "Calculations"),
             ("io", "File I/O"), ("exec", "EXEC CICS / SQL / DLI"), ("calls", "CALL"), ("performs", "PERFORM"),
             ("goto", "GO TO"), ("literal_moves", "MOVE literal"), ("data_moves", "MOVE field"),
             ("sets", "SET"), ("other_statements", "STRING, UNSTRING, INSPECT, INITIALIZE, COPY, ENTRY and others"),
             ("displays", "DISPLAY"), ("terminations", "GOBACK, STOP RUN, RETURN, XCTL"),
             ("unclassified", "Not classified by the parser")]
    L += ["", "## Statement inventory", "",
          "Every procedure statement the parser recorded, by kind. Each one is listed with its line under Paragraph details.", ""]
    L += table(["Kind", "Count"], [(lbl, sum(len(p.get(k, [])) for p in s["paragraphs"])) for k, lbl in kinds])

    # control flow
    L += ["", "## Control flow", ""]
    paras = [p for p in s["paragraphs"]]
    if paras:
        idx = dict((p["name"], "P%d" % i) for i, p in enumerate(paras))
        edges = []
        for p in paras:
            for t in sorted(set(x["target"] for x in p["performs"] if x.get("target"))):
                if t in idx:
                    edges.append((p["name"], t))
            for g in p["goto"]:
                for t in g["targets"]:
                    if t in idx:
                        edges.append((p["name"], t + "|GO TO"))
        nodes = set()
        for a, b in edges:
            nodes.add(a)
            nodes.add(b.split("|")[0])
        nodes.add(paras[0]["name"])
        limited = len(nodes) > 40
        if limited:
            first = paras[0]["name"]
            lvl1 = set(b.split("|")[0] for a, b in edges if a == first)
            keep = set([first]) | lvl1
            edges = [(a, b) for a, b in edges if a in keep and b.split("|")[0] in keep]
            nodes = keep
        L += ["```mermaid", "flowchart TD"]
        for p in paras:
            if p["name"] in nodes:
                L.append('    %s["%s"]' % (idx[p["name"]], p["name"]))
        seen = set()
        for a, b in edges:
            if (a, b) in seen:
                continue
            seen.add((a, b))
            if b.endswith("|GO TO"):
                L.append('    %s -->|"GO TO"| %s' % (idx[a], idx[b[:-6]]))
            else:
                L.append("    %s --> %s" % (idx[a], idx[b]))
        L += ["```", ""]
        if limited:
            L += ["The diagram shows the entry paragraph and the paragraphs it performs directly (the full graph has more than 40 nodes). The paragraph table lists every PERFORM edge.", ""]
        semp = dict((p.get("name"), p) for p in sem.get("paragraphs", []))
        rows = []
        for p in paras:
            sp = semp.get(p["name"]) or {}
            logic = sp.get("logic") or "Not analyzed"
            rows.append(("[%s](#%s)" % (p["name"], anchor_id("para " + p["name"])), "%d-%d" % (p["start_line"], p["end_line"]),
                         ("%s (%s)" % (logic, sp.get("confidence", ""))) if sp.get("logic") else logic,
                         ", ".join(sorted(set(x["target"] for x in p["performs"] if x.get("target")))),
                         ", ".join(p.get("performed_by", [])),
                         "yes" if p.get("reachable_static") else "no static path"))
        L += table(["Paragraph", "Lines", "Logic", "Performs", "Performed by", "Reachable"], rows)
        unresolved = s.get("unresolved_targets") or []
        if unresolved:
            L += ["", "Unresolved PERFORM/GO TO targets: " + ", ".join("%s (`%s`)" % (u["target"], u["source"]) for u in unresolved)]

    # paragraph detail
    L += ["", "## Paragraph details", ""]
    semp = dict((p.get("name"), p) for p in sem.get("paragraphs", []))
    rule_by_para = {}
    for r in rules_for_program(c, pgm, all_rules):
        for i in r.get("implementations", []):
            if i.get("program") == pgm and i.get("paragraph"):
                rule_by_para.setdefault(i["paragraph"], set()).add(r["id"])
    for p in paras:
        L += ["### Para %s" % p["name"], "",
              "Lines `%s`. %s" % (p["source"], ("Section " + p["section"] + ". ") if p.get("section") else "")]
        sp = semp.get(p["name"])
        L.append("")
        L.append("Logic: " + ("%s (%s)" % (sp["logic"], sp.get("confidence", "Inferred")) if sp and sp.get("logic") else "Not analyzed."))
        if rule_by_para.get(p["name"]):
            L.append("")
            L.append("Rules: " + ", ".join("[%s](../09-business-rules-catalog.md#%s)" % (x, x.lower()) for x in sorted(rule_by_para[p["name"]])))
        items = []
        for d in p["decisions"]:
            items.append((d["line"], 0, "- %s %s at `%s` (%s)" % (d["type"], code(d["condition"][:200]), d["source"], d["class"])))
        for x in p["calculations"]:
            items.append((x["line"], 1, "- Calculation %s at `%s`%s" % (code(x["text"][:200]), x["source"], " ROUNDED" if x.get("rounded") else " (no ROUNDED)" if x["verb"] in ("COMPUTE", "DIVIDE", "MULTIPLY") else "")))
        for x in p["io"]:
            items.append((x["line"], 1, "- File I/O %s at `%s`" % (code(x["text"][:160]), x["source"])))
        for x in p["exec"]:
            items.append((x["line"], 1, "- EXEC %s %s at `%s`" % (x.get("kind"), x.get("verb", ""), x["source"])))
        for x in p["calls"]:
            items.append((x["line"], 1, "- CALL %s at `%s`" % (x.get("target", "?"), x["source"])))
        for x in p["performs"]:
            if x.get("target"):
                items.append((x["line"], 1, "- PERFORM %s%s%s at `%s`" % (x["target"], " THRU " + x["thru"] if x.get("thru") else "",
                                                                         " " + code(x["loop"]) if x.get("loop") else "", x["source"])))
            else:
                items.append((x["line"], 1, "- Inline PERFORM %s at `%s`" % (code(x.get("loop", "")), x["source"])))
        for x in p["goto"]:
            items.append((x["line"], 1, "- GO TO %s at `%s`" % (" ".join(x["targets"]), x["source"])))
        for x in p["literal_moves"]:
            items.append((x["line"], 1, "- MOVE %s TO %s at `%s`" % (code(("'" + x["value"] + "'") if not x.get("numeric") else x["value"]), x["to"], x["source"])))
        for x in p.get("data_moves", []):
            items.append((x["line"], 1, "- %s at `%s`" % (code(x["text"][:200]), x["source"])))
        for x in p["sets"]:
            items.append((x["line"], 1, "- %s at `%s`" % (code(x["text"][:160]), x["source"])))
        for x in p["other_statements"]:
            items.append((x["line"], 1, "- %s at `%s`" % (code(x["text"][:160]), x["source"])))
        for x in p["displays"]:
            items.append((x["line"], 1, "- %s at `%s`" % (code(x["text"][:160]), x["source"])))
        for x in p.get("unclassified", []):
            items.append((x["line"], 1, "- Not classified by the parser (%s): %s at `%s`" % (x.get("first_word", ""), code(x["text"][:200]), x["source"])))
        for x in p["terminations"]:
            items.append((x["line"], 2, "- Ends with %s at `%s`" % (x["verb"], x["source"])))
        if items:
            L += ["", "Statements in source order:", ""] + [t for _, _, t in sorted(items, key=lambda z: (z[0], z[1]))]
        L.append("")

    # rules
    L += ["## Business rules", ""]
    prs = rules_for_program(c, pgm, all_rules)
    if prs:
        rows = []
        for r in prs:
            impl = [i for i in r.get("implementations", []) if i.get("program") == pgm]
            ver = (r.get("verification") or {}).get("verdict", "")
            rows.append(("[%s](../09-business-rules-catalog.md#%s)" % (r["id"], r["id"].lower()), r.get("category", ""),
                         r.get("statement", ""), ", ".join(i.get("paragraph") or "" for i in impl if i.get("paragraph")),
                         ", ".join("`%s`" % i["source"] for i in impl if i.get("source")),
                         r.get("confidence", "") + (" / review: " + ver if ver else "")))
        L += table(["Rule", "Category", "Statement", "Paragraph", "Source", "Confidence"], rows)
    if sem.get("no_business_rules_reason"):
        L += ["", "No business rules identified: %s" % sem["no_business_rules_reason"]]
    if not prs and not sem.get("no_business_rules_reason"):
        L.append("Not analyzed - no validated rule analysis for this program.")
    if sem.get("no_rule_decisions"):
        L += ["", "Decision points reviewed and classified as not business rules:", ""]
        L += table(["Lines", "Reason"], [("`%s`" % n["source"], n["reason"]) for n in sem["no_rule_decisions"]])
    if cp:
        L += ["", "Decision coverage: %d of %d business-candidate decision points are linked to a rule or a no-rule reason (%d inside rule ranges)." % (
            cp.get("decision_covered", 0), cp.get("decision_candidates", 0), cp.get("decision_in_rules", 0))]
        if cp.get("uncovered_decisions"):
            L += ["", "Uncovered decision points:", ""]
            L += table(["Line", "Paragraph", "Condition"], [(u["line"], u["paragraph"], code(u["condition"])) for u in cp["uncovered_decisions"]])

    # error handling
    L += ["", "## Error handling", ""]
    rows = []
    for p in paras:
        for d in p["decisions"]:
            if d["class"] == "io-status":
                rows.append((p["name"], "check", code(d["condition"][:140]), "`%s`" % d["source"]))
        for x in p["calls"]:
            if x.get("target") in ("CEE3ABD",):
                rows.append((p["name"], "abend", "CALL CEE3ABD", "`%s`" % x["source"]))
        for x in p["exec"]:
            if x.get("kind") == "CICS" and x.get("verb", "").startswith(("ABEND", "HANDLE")):
                rows.append((p["name"], x["verb"].lower(), code(x["text"][:140]), "`%s`" % x["source"]))
        for x in p["literal_moves"]:
            if "RETURN-CODE" in x["to"].upper():
                rows.append((p["name"], "return code", "MOVE %s TO RETURN-CODE" % x["value"], "`%s`" % x["source"]))
    L += table(["Paragraph", "Kind", "Detail", "Lines"], rows) if rows else ["No status checks, abends or return-code settings were found."]

    # observations
    L += ["", "## Observations and SME questions", ""]
    obs = []
    for o in sem.get("observations", []):
        obs.append("- %s: %s%s" % (o.get("kind", "observation"), o.get("text", ""), " (`%s`)" % o["source"] if o.get("source") else ""))
    for o in old.get("observations", []):
        t = o.get("text", "")
        if t.startswith("Commented COPY") and not re.search(r"\bCOPY\s+[A-Z0-9$#@-]+", t.split(":", 1)[-1]):
            continue
        obs.append("- earlier pass: %s (%s, `%s`)" % (o.get("text", ""), o.get("confidence", ""), o.get("source", "")))
    for q in sem.get("sme_questions", []):
        obs.append("- SME question: %s%s" % (q.get("question", ""), " (`%s`)" % q["source"] if q.get("source") else ""))
    L += obs or ["None recorded."]
    L += ["", "## Sources", "", "- `%s`" % path, "- `docs/_work/structure/programs/%s.json`" % pgm,
          "- `docs/_work/semantic/programs/%s.json`" % pgm, "- `docs/_work/programs/%s.json`" % pgm,
          "", "## Confidence", "",
          "Structure tables (divisions, items, paragraphs, statements, line numbers) are Confirmed: they are parsed from the source. "
          "Paragraph logic and rule statements carry their own Confirmed/Inferred tag from the batch analysis, and every rule anchor was "
          "checked against the cited lines. Decision-point classes are a keyword heuristic used only for coverage measurement. "
          "Header comments are Unverified."]
    write(os.path.join(pdir, pgm + ".md"), L)


def program_index(c, all_rules):
    L = ["# Programs", "", "One page per program. COBOL pages are generated from the parsed structure and the validated batch analysis.", ""]
    rows = []
    for pgm, s in sorted(c.progs.items()):
        cp = c.checkpoints.get(pgm, {})
        nrules = len(rules_for_program(c, pgm, all_rules))
        sem = c.sem.get(pgm) or {}
        rows.append(("[%s](%s.md)" % (pgm, pgm), s["source_path"], ", ".join((c.old_prog.get(pgm) or {}).get("runtime_type", [])),
                     s["line_count"], s["counts"]["paragraphs"], cp.get("paragraphs_described", 0), nrules,
                     "%s/%s" % (cp.get("decision_covered", 0), cp.get("decision_candidates", 0)),
                     cp.get("status", "unanalyzed"), "no rules: yes" if sem.get("no_business_rules_reason") else ""))
    L += table(["Program", "Source", "Runtime", "Lines", "Paragraphs", "Described", "Rules", "Decisions covered", "Semantic status", "Note"], rows)
    asm = [(k, v) for k, v in sorted(c.old_prog.items()) if v.get("language") == "Assembler"]
    if asm:
        L += ["", "## Assembler programs", "",
              "Assembler members are documented from the earlier program facts; the COBOL structure parser does not apply to them.", ""]
        L += table(["Program", "Source", "Runtime"], [("[%s](%s.md)" % (k, k), v["source_path"], ", ".join(v.get("runtime_type", []))) for k, v in asm])
    L += ["", "## Sources", "", "- `docs/_work/structure/programs/`", "- `docs/_work/semantic/programs/`", "- `docs/_work/batches/*/checkpoint.json`",
          "", "## Confidence", "", "Counts are computed by the toolkit scripts. Semantic status comes from `batch_manager.py check`."]
    write(os.path.join(c.out, "07-programs", "index.md"), L)


# ----------------------------------------------------------------- copybook page
_word_index = {}


def procedure_word_index(c, path):
    """word -> sorted line numbers in the procedure code of path (comments and literals removed)."""
    if path in _word_index:
        return _word_index[path]
    idx = {}
    if os.path.isfile(path):
        f = open(path, "rb")
        try:
            raw = f.read().decode("latin-1").replace("\r\n", "\n").replace("\r", "\n").split("\n")
        finally:
            f.close()
        lo, hi = 1, len(raw)
        prog = [s for s in c.progs.values() if s["source_path"] == path]
        if prog:
            pd = [d for d in prog[0]["divisions"] if d["name"] == "PROCEDURE"]
            if not pd:
                _word_index[path] = idx
                return idx
            lo, hi = pd[0]["start_line"], pd[0]["end_line"]
        for n in range(lo, hi + 1):
            l = raw[n - 1].expandtabs(8)
            if len(l) < 8 or l[6] in "*/":
                continue
            text = re.sub(r"'[^']*'|\"[^\"]*\"", " ", l[7:72].upper())
            for w in set(re.findall(r"[A-Z0-9][A-Z0-9-]*", text)):
                idx.setdefault(w, []).append(n)
    _word_index[path] = idx
    return idx


def field_references(c, cpy, path, s):
    """Field-level where-used: which programs name each field or 88-level in procedure code."""
    names = []
    for it in s.get("data_items", []):
        if it["name"] != "FILLER" and it.get("level"):
            names.append((it["name"], it["line"]))
        for x in it.get("conditions", []):
            names.append((x["name"], x["line"]))
    if not names:
        return []
    direct = [u for u in c.usage if u["copybook"] == cpy and not u["commented"] and u.get("resolved_path") == path]
    replaced = sorted(set(u["from_member"] for u in direct if u.get("replacing")))
    via = {}
    for u in direct:
        if u["from_type"] == "cobol-program":
            via.setdefault(u["from_member"], cpy)
        else:
            for u2 in c.usage:
                if u2["copybook"] == u["from_member"] and not u2["commented"] and u2["from_type"] == "cobol-program":
                    via.setdefault(u2["from_member"], u["from_member"])
    scan = {}
    for pgm in sorted(via):
        sp = c.progs.get(pgm)
        if not sp:
            continue
        paths = [sp["source_path"]]
        for u in c.usage:
            if u["from"] == sp["source_path"] and not u["commented"] and u.get("resolved_path"):
                k = [v for v in c.cpys.values() if v["source_path"] == u["resolved_path"] and v.get("content") == "procedure"]
                if k:
                    paths.append(u["resolved_path"])
        scan[pgm] = paths
    out = ["", "## Field references by program", "",
           "Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. "
           "Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. "
           "A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.", ""]
    if replaced:
        out += ["Copied with REPLACING by: %s. Names after replacement differ from the names below, so those uses are not matched." % ", ".join(replaced), ""]
    if not scan:
        out.append("No COBOL program copies this member, so no field references exist.")
        return out
    rows, unused = [], []
    for name, line in names:
        refs = []
        for pgm, paths in sorted(scan.items()):
            hits = []
            for pth in paths:
                for n in procedure_word_index(c, pth).get(name, []):
                    hits.append("`%s:%d`" % (pth, n))
            if hits:
                refs.append("%s (%d): %s%s" % (pgm, len(hits), ", ".join(hits[:3]), ", ..." if len(hits) > 3 else ""))
        if refs:
            rows.append((name, line, "; ".join(refs)))
        else:
            unused.append("%s (line %d)" % (name, line))
    out += table(["Field", "Line", "Referenced by (count): first lines"], rows) if rows else ["No field of this member is named in procedure code."]
    if unused:
        out += ["", "Named in no procedure statement of the copying programs (may still be moved as part of a group): " + ", ".join(unused) + "."]
    return out


def copybook_page(c, key, s):
    cpy = s["member"]
    sem = c.csem.get(cpy) or {}
    path = s["source_path"]
    lay = load(os.path.join(c.work, "layouts", cpy + ".json")) or {}
    off = {}
    for rec in lay.get("records", []):
        for f in rec.get("fields", []):
            off[(f.get("line"), f.get("name"))] = f
    cp = c.checkpoints.get("CPY:" + cpy, {})
    L = ["# Layout %s" % cpy, "",
         "| Item | Value |", "|---|---|",
         "| Source | `%s` |" % path,
         "| Type | %s |" % s["artifact_type"],
         "| Content | %s |" % (s.get("content") or "data"),
         "| Lines | %d |" % s["line_count"],
         "| Data items | %d (88-levels: %d) |" % (s["counts"]["data_items"], s["counts"]["conditions_88"]),
         "| Semantic analysis | %s |" % ("validated (batch %s)" % sem.get("batch") if cp.get("status") == "validated" else "NOT validated"),
         "", "## Purpose", ""]
    if sem.get("purpose"):
        L.append("%s (%s)" % (sem["purpose"], sem.get("confidence", "Inferred")))
        if sem.get("evidence"):
            L += ["", "Evidence: " + ", ".join("`%s`" % e for e in sem["evidence"])]
    else:
        L.append("Not analyzed.")
    if s.get("data_items"):
        L += ["", "## Record structure", "",
              "Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.", ""]
        rows = []
        for it in s["data_items"]:
            o = off.get((it["line"], it["name"])) or {}
            occ = ""
            if it.get("occurs"):
                occ = "%s%s%s" % (("%s TO " % it["occurs_min"]) if it.get("occurs_min") else "", it["occurs"],
                                   " DEPENDING ON " + it["depending_on"] if it.get("depending_on") else "")
            rows.append(("%02d" % it["level"] if it["level"] else "SQL", ("&nbsp;" * 2 * max(0, (o.get("depth") or 0))) + it["name"],
                         it.get("pic", ""), it.get("usage", "") or ("DISPLAY" if it.get("pic") else ""),
                         o.get("offset", ""), o.get("end", ""), o.get("total_length", o.get("length", it.get("length", ""))),
                         occ, it.get("redefines", ""), (it.get("value") or "")[:60], it["line"]))
        L += table(["Lvl", "Field", "PIC", "Usage", "Start", "End", "Len", "OCCURS", "REDEFINES", "VALUE", "Line"], rows)
        conds = [(it["name"], x["name"], x["value"], x["line"]) for it in s["data_items"] for x in it.get("conditions", [])]
        L += ["", "## Level-88 conditions", ""]
        L += table(["Field", "Condition", "Values", "Line"], conds) if conds else ["None."]
    if s.get("sql_tables"):
        L += ["", "## DB2 table declaration", ""]
        for t in s["sql_tables"]:
            L += ["Table `%s` (`%s`):" % (t["table"], t["source"]), ""]
            L += table(["Column", "Type", "NOT NULL"], [(x["name"], x["type"], "yes" if x["not_null"] else "") for x in t["columns"]])
    if s.get("paragraphs"):
        L += ["", "## Procedure paragraphs", "", "This copybook contains procedure-division code copied into programs.", ""]
        L += table(["Paragraph", "Lines", "Decisions", "Calculations", "Performs"],
                   [(p["name"], "`%s`" % p["source"], len(p["decisions"]), len(p["calculations"]),
                     ", ".join(sorted(set(x["target"] for x in p["performs"] if x.get("target"))))) for p in s["paragraphs"]])
    L += ["", "## Used by", ""]
    rows = []
    for u in c.usage:
        if u["copybook"] == cpy and (u.get("resolved_path") == path or (u["resolution"] != "inventory")):
            fm = u["from_member"]
            link = "[%s](../../07-programs/%s.md)" % (fm, fm) if u["from_type"] == "cobol-program" else (
                "[%s](%s.md)" % (fm, fm) if u["from_type"] in ("cobol-copybook", "db2-dclgen") else fm)
            rows.append((link, u["from_type"], u["kind"], "commented out" if u["commented"] else "active",
                         u.get("replacing", ""), "`%s`" % u["source"]))
    L += table(["Used by", "Type", "Statement", "State", "REPLACING", "Line"], rows) if rows else ["No program or copybook copies this member."]
    nested = [x for x in s.get("copy_statements", [])]
    if nested:
        L += ["", "## Copybooks included by this copybook", ""]
        L += table(["Copybook", "Statement", "Line"], [(x["name"], x["kind"], "`%s`" % x["source"]) for x in nested])
    L += field_references(c, cpy, path, s)
    if sem.get("key_fields"):
        L += ["", "## Key fields", ""]
        L += table(["Field", "Meaning", "Source"], [(k["name"], k.get("meaning", ""), "`%s`" % k["source"] if k.get("source") else "") for k in sem["key_fields"]])
    obs = ["- %s: %s%s" % (o.get("kind", "observation"), o.get("text", ""), " (`%s`)" % o["source"] if o.get("source") else "") for o in sem.get("observations", [])]
    if obs:
        L += ["", "## Observations", ""] + obs
    L += ["", "## Sources", "", "- `%s`" % path, "- `docs/_work/structure/copybooks/%s.json`" % key,
          "- `docs/_work/layouts/%s.json`" % cpy, "- `docs/_work/semantic/copybooks/%s.json`" % cpy,
          "", "## Confidence", "", "Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis."]
    write(os.path.join(c.out, "08-data", "layouts", cpy + ".md"), L)


# ----------------------------------------------------------------- job page
def program_opens(c, pgm):
    s = c.progs.get(pgm)
    if not s:
        return {}
    by_dd = {}
    for sel in s["selects"]:
        modes = set()
        for p in s["paragraphs"]:
            for io in p["io"]:
                if io["verb"] == "OPEN":
                    for m, fl in io.get("files", {}).items():
                        if sel["file"] in fl:
                            modes.add(m)
        for dd in set([sel["assign"], sel["assign"].split("-")[-1]]):
            by_dd[dd] = (sel["file"], sorted(modes), sel["source"])
    return by_dd


def job_page(c, path, j):
    if j["artifact_type"] == "jcl-job":
        name = c.job_page[path]
        title, outdir = "Job", os.path.join(c.out, "06-batch", "jobs")
    else:
        name = j["member"]
        title, outdir = ("PROC" if j["artifact_type"] == "jcl-proc" else "JCL template"), os.path.join(c.out, "06-batch", "procs")
    oldname, old = c.old_jobs.get(path, (None, {}))
    old = old or {}
    jc = j.get("job") or {}
    L = ["# %s %s" % (title, name), "", "| Item | Value |", "|---|---|",
         "| Source | `%s` |" % path, "| Member | %s |" % j["member"], "| Job card | `%s` |" % jc.get("source", ""),
         "| CLASS / MSGCLASS | %s / %s |" % (cell(jc.get("class")), cell(jc.get("msgclass"))),
         "| NOTIFY | %s |" % cell(jc.get("notify")), "| Job COND | %s |" % cell(jc.get("cond")),
         "| Steps | %d |" % len(j["steps"]), "| Module | %s |" % cell(old.get("module")), ""]
    if j.get("procs"):
        L += ["PROC/PEND statements: " + ", ".join("%s %s `%s`" % (p["op"], p["name"], p["source"]) for p in j["procs"]), ""]
        users = []
        for p2, j2 in sorted(c.jcl.items()):
            for st in j2["steps"]:
                if (st.get("proc") or "").upper() == name.upper():
                    users.append("%s step %s (`%s`)" % (c.job_page.get(p2, j2["member"]), st["name"], st["source"]))
        L += ["Executed by: " + ("; ".join(users) if users else "no EXEC PROC= reference in the repository JCL"), ""]
    desc = old.get("description") or {}
    L += ["## Purpose", ""]
    if desc.get("text"):
        L.append("Comment in the JCL (Unverified, `%s`): %s" % (desc.get("source", path), desc["text"]))
    else:
        L.append("No descriptive comment in the JCL.")
    apps = []
    for st in j["steps"]:
        p = ((st.get("application_program") or {}).get("program") or st.get("pgm") or "").upper()
        if p in c.progs:
            apps.append(p)
    if apps:
        L += ["", "Application programs run by this job: " + ", ".join("[%s](../../07-programs/%s.md)" % (p, p) for p in apps) + "."]
        for p in apps:
            summ = ((c.sem.get(p) or {}).get("summary") or {}).get("text")
            if summ:
                L += ["", "%s: %s (Inferred, from the program analysis)" % (p, summ)]
    L += ["", "## Step flow", "", "```mermaid", "flowchart TD"]
    for i, st in enumerate(j["steps"]):
        lab = "%s: %s" % (st["name"], (st.get("pgm") or ("PROC " + (st.get("proc") or ""))))
        L.append('    S%d["%s"]' % (i, lab.replace('"', "'")))
        if i:
            L.append("    S%d --> S%d" % (i - 1, i))
    if not j["steps"]:
        L.append('    S0["No EXEC steps"]')
    L += ["```", ""]
    if j["conditionals"]:
        L += ["## Conditional execution", ""]
        L += table(["Statement", "Condition", "Steps inside", "Line"],
                   [(x["op"], code(x.get("condition", "")), ", ".join(x.get("steps", [])), "`%s`" % x["source"]) for x in j["conditionals"]])
        L.append("")
    L += ["## Steps", ""]
    oldsteps = old.get("steps", [])
    for i, st in enumerate(j["steps"]):
        os_ = oldsteps[i] if i < len(oldsteps) and oldsteps[i].get("name") == st["name"] else {}
        app = st.get("application_program") or {}
        apg = (app.get("program") or st.get("pgm") or "").upper()
        L += ["### %s" % st["name"], "",
              "| Item | Value |", "|---|---|",
              "| EXEC | `%s` |" % st["source"],
              "| Program | %s |" % (("[%s](../../07-programs/%s.md)" % (st["pgm"], st["pgm"])) if (st.get("pgm") or "").upper() in c.progs else cell(st.get("pgm"))),
              "| PROC | %s |" % cell(st.get("proc")),
              "| Application program | %s |" % ((("[%s](../../07-programs/%s.md)" % (app["program"], app["program"])) if app["program"].upper() in c.progs
                                                 else "%s (no source in repository)" % cell(app["program"])) + " via %s" % app.get("via") if app else ""),
              "| PARM | %s |" % code(st.get("parm")),
              "| COND | %s |" % code(st.get("cond")),
              "| Function (earlier pass) | %s |" % cell(os_.get("function")), ""]
        opens = program_opens(c, apg)
        rows = []
        for d in st["dds"]:
            prog_file = ""
            if d["ddname"] in opens:
                f, modes, srcref = opens[d["ddname"]]
                prog_file = "%s OPEN %s (`%s`)" % (f, "/".join(modes) or "none", srcref)
            ctl = d.get("control") or {}
            extra = ""
            if d.get("instream_lines"):
                extra = "in-stream lines %d-%d" % (d["instream_lines"]["first"], d["instream_lines"]["last"])
                if ctl.get("verbs"):
                    extra += "; statements: " + " ".join(ctl["verbs"])
                if ctl.get("names"):
                    extra += "; NAME(): " + " ".join(ctl["names"][:8])
                if ctl.get("tables"):
                    extra += "; tables: " + " ".join(ctl["tables"])
                if ctl.get("run_program"):
                    extra += "; RUN PROGRAM(%s)" % ctl["run_program"]
            rows.append((d["ddname"] + (" (concat)" if d.get("concatenation") else ""), d.get("dsn") or ("SYSOUT=" + d["sysout"] if d.get("sysout") else ("DUMMY" if d.get("dummy") else ("*" if d.get("instream") else ""))),
                         d.get("disp", ""), d.get("dcb") or d.get("recfm") or "", prog_file, extra, "`%s`" % d["source"]))
        L += table(["DD", "Dataset / output", "DISP", "DCB", "Program file and OPEN mode", "Control data", "Line"], rows) if rows else ["No DD statements."]
        inherited = [e for e in c.dataflow if e.get("job") == name and e.get("step") == st["name"]
                     and not (e.get("source") or "").startswith(path + ":")]
        if inherited:
            L += ["", "Datasets supplied by PROC %s for this step:" % cell(st.get("proc")), ""]
            L += table(["Dataset", "Usage", "Line"], [(e["dsn"], "/".join(e.get("usage", [])), "`%s`" % e["source"]) for e in inherited])
        if apg in c.progs:
            rc = []
            for p in c.progs[apg]["paragraphs"]:
                for x in p["literal_moves"]:
                    if "RETURN-CODE" in x["to"].upper():
                        rc.append("RETURN-CODE %s (`%s`)" % (x["value"], x["source"]))
                for x in p["calls"]:
                    if x.get("target") == "CEE3ABD":
                        rc.append("abend via CEE3ABD (`%s`)" % x["source"])
            if rc:
                L += ["", "Return codes and abends set by %s: %s." % (apg, "; ".join(sorted(set(rc))))]
        L.append("")
    # scheduling
    L += ["## Scheduling and dependencies", ""]
    sched = []
    for e in c.schedule.get("ca7_edges", []):
        if name in (e.get("from"), e.get("to")):
            sched.append(("CA7 trigger", e["from"], e["to"], "`%s`" % e["source"]))
    for e in c.schedule.get("controlm_edges", []):
        if name in (e.get("from"), e.get("to")):
            ev = "`%s` (OUTCOND)" % e["source"]
            if e.get("incond_source"):
                ev += ", `%s` (INCOND)" % e["incond_source"]
            sched.append(("Control-M condition " + cell(e.get("condition")), e["from"], e["to"], ev))
    for e in c.schedule.get("script_submits", []):
        if e.get("job") == name:
            sched.append(("Shell submit", e["script"], name, "`%s`" % e["source"]))
    L += table(["Mechanism", "From", "To", "Evidence"], sched) if sched else ["Not referenced by the CA7 or Control-M exports or the shell scripts (see the gap report)."]
    if j.get("jcllib") or j.get("includes") or j.get("sets"):
        L += ["", "## JCL library, INCLUDE and SET", ""]
        L += table(["Statement", "Text", "Line"], [("JCLLIB", x["text"], "`%s`" % x["source"]) for x in j.get("jcllib", [])] +
                   [("INCLUDE", x["member"], "`%s`" % x["source"]) for x in j.get("includes", [])] +
                   [("SET", x["text"], "`%s`" % x["source"]) for x in j.get("sets", [])])
    syms = sorted(set(re.findall(r"&&?[A-Z][A-Z0-9#@$]*", " ".join(st["operands"] + " " + " ".join(d["operands"] for d in st["dds"]) for st in j["steps"]) + " " + (jc.get("notify") or ""))))
    if syms:
        L += ["", "## Parameters", "", "Symbols left as parameters (not resolved): " + ", ".join(code(x) for x in syms) + "."]
    L += ["", "## Sources", "", "- `%s`" % path, "- `docs/_work/structure/jcl/%s.json`" % j["member"]]
    if oldname:
        L.append("- `docs/_work/jobs/%s.json`" % oldname)
    L += ["", "## Confidence", "", "Steps, DDs, conditions and control-data summaries are Confirmed from the JCL. OPEN modes come from the program source. Comments are Unverified."]
    write(os.path.join(outdir, name + ".md"), L)


# ----------------------------------------------------------------- CICS, rules catalog, dependencies
def cics_page(c):
    L = ["# CICS resource definitions", "", "Every DEFINE statement in the CICS System Definition (CSD) files, parsed by `extract_structure.py`.", ""]
    by = {}
    for r in c.csd["resources"]:
        by.setdefault(r["type"], []).append(r)
    for t in sorted(by):
        L += ["## %s (%d)" % (t, len(by[t])), ""]
        rows = []
        for r in by[t]:
            a = r["attrs"]
            key = ""
            if t == "TRANSACTION":
                p = a.get("PROGRAM", "")
                key = "PROGRAM " + (("[%s](../07-programs/%s.md)" % (p, p)) if p in c.progs else p + (" (no source in repository)" if p else ""))
            elif t == "FILE":
                key = "DSNAME " + a.get("DSNAME", "")
            elif t == "PROGRAM":
                key = "LANGUAGE %s%s" % (a.get("LANGUAGE", ""), "" if r["name"] in c.progs or r["name"] in c.old_prog else " (no source in repository)")
            elif t in ("TDQUEUE",):
                key = "TYPE %s DDNAME %s" % (a.get("TYPE", ""), a.get("DDNAME", ""))
            elif t == "LIBRARY":
                key = "DSNAME01 " + a.get("DSNAME01", "")
            else:
                key = ", ".join("%s(%s)" % (k, v) for k, v in sorted(a.items())[:4])
            rows.append((r["name"], a.get("GROUP", ""), key, a.get("DESCRIPTION", ""), "`%s`" % r["source"]))
        L += table(["Name", "Group", "Key attributes", "Description", "Source"], rows) + [""]
    L += ["## Sources", ""] + ["- `%s`" % f["path"] for f in c.csd["files"]] + ["- `docs/_work/structure/csd.json`", "",
          "## Confidence", "", "Confirmed: copied from the CSD definitions."]
    write(os.path.join(c.out, "05-online", "cics-resources.md"), L)


def data_definitions_page(c):
    d = c.ddefs
    L = ["# Data definitions", "",
         "Every DB2 DDL object (from DDL members and DB2 control cards), IMS DBD segment and PSB PCB, parsed by `extract_structure.py`. "
         "Table pages in [db2/](db2/) and database pages in [ims/](ims/) carry the earlier narrative.", "", "## DB2 objects", ""]
    rows = []
    for o in d["ddl"]:
        extra = ""
        if o.get("columns"):
            extra = "columns: " + ", ".join("%s %s" % (x["name"], x["type"]) for x in o["columns"])
        if o.get("primary_key"):
            extra += "; primary key (%s)" % ", ".join(o["primary_key"])
        if o.get("on_table"):
            extra = "on " + o["on_table"]
        users = []
        short = o["name"].split(".")[-1]
        for pgm, s in sorted(c.progs.items()):
            for p in s["paragraphs"]:
                for e in p["exec"]:
                    if e.get("kind") == "SQL" and any(t.split(".")[-1] == short for t in e.get("tables", [])):
                        users.append(pgm)
        rows.append((o["object"], o["name"], o["artifact_type"], extra, ", ".join(sorted(set(users))), "`%s`" % o["source"]))
    L += table(["Object", "Name", "Defined in", "Details", "Programs with SQL on it", "Source"], rows)
    L += ["", "## IMS databases (DBD)", ""]
    for dbd in d["dbd"]:
        L += ["### %s" % (dbd.get("name") or dbd["path"]), "", "Access %s, source `%s`." % (dbd.get("access") or "not coded", dbd.get("source") or dbd["path"]), ""]
        rows = []
        for sg in dbd["segments"]:
            rows.append((sg["name"], sg["parent"], sg.get("bytes") or "", ", ".join("%s start %s len %s type %s" % (f["name"], f["start"], f["bytes"], f.get("type") or "") for f in sg["fields"]), "`%s`" % sg["source"]))
        L += table(["Segment", "Parent", "Bytes", "Fields", "Source"], rows) if rows else ["No SEGM statements."]
        L.append("")
    L += ["## IMS program specification blocks (PSB)", ""]
    rows = []
    for psb in d["psb"]:
        for pcb in psb["pcbs"]:
            rows.append((psb.get("name") or psb["path"], pcb.get("label") or "", pcb["type"], pcb.get("dbd") or "", pcb.get("procopt") or "", ", ".join(pcb["senseg"]), "`%s`" % pcb["source"]))
    L += table(["PSB", "PCB label", "Type", "DBD", "PROCOPT", "Sensitive segments", "Source"], rows)
    L += ["", "## Sources", "", "- `docs/_work/structure/data-definitions.json`", "", "## Confidence", "", "Confirmed: parsed from DDL, control cards, DBD and PSB sources."]
    write(os.path.join(c.out, "08-data", "data-definitions.md"), L)


def rules_catalog(c, all_rules):
    L = ["# Business rules catalog", "",
         "All business rules: %d legacy rules from the first pass (each re-reviewed in the batch analysis) and %d rules from the batch analysis. "
         "Every rule cites a line range; batch rules also carry a verbatim code anchor that `batch_manager.py check` verified inside that range." % (
             sum(1 for r in all_rules if r.get("origin") == "legacy"), sum(1 for r in all_rules if r.get("origin") != "legacy")), ""]
    cats = {}
    for r in all_rules:
        cats[r.get("category") or "uncategorized"] = cats.get(r.get("category") or "uncategorized", 0) + 1
    L += table(["Category", "Rules"], sorted(cats.items())) + [""]
    progs = {}
    for r in all_rules:
        ps = sorted(set(i.get("program") for i in r.get("implementations", []) if i.get("program")))
        progs.setdefault(ps[0] if ps else "(none)", []).append(r)
    L += ["## Programs without business rules", ""]
    rows = []
    for pgm in sorted(c.progs):
        if pgm not in progs:
            reason = (c.sem.get(pgm) or {}).get("no_business_rules_reason") or "Not analyzed"
            rows.append(("[%s](07-programs/%s.md)" % (pgm, pgm), reason))
    L += table(["Program", "Reason"], rows) if rows else ["Every program has at least one rule."]
    for pgm in sorted(progs):
        L += ["", "## %s" % pgm, ""]
        if pgm in c.progs:
            L += ["Program page: [%s](07-programs/%s.md)." % (pgm, pgm), ""]
        for r in progs[pgm]:
            L += ["### %s" % r["id"], ""]
            L.append("%s" % r.get("statement", ""))
            L.append("")
            rows = [("Category", r.get("category", "")), ("Confidence", r.get("confidence", ""))]
            if r.get("conditions"):
                rows.append(("Conditions", r["conditions"] if isinstance(r["conditions"], str) else "; ".join(
                    "%s %s %s" % (x.get("field", ""), x.get("op", ""), x.get("value", "")) for x in r["conditions"])))
            if r.get("outcome") or r.get("outcomes"):
                rows.append(("Outcome", r.get("outcome") or "; ".join("%s%s" % (o.get("action", ""), (" - " + o["message"]) if o.get("message") else "") for o in r["outcomes"])))
            if r.get("messages"):
                rows.append(("Messages", "; ".join(r["messages"])))
            for i in r.get("implementations", []):
                rows.append(("Implemented at", "%s %s `%s`" % (i.get("program", ""), i.get("paragraph") or i.get("copybook") or "", i.get("source", ""))))
            if r.get("anchor"):
                rows.append(("Anchor (verified)", code(r["anchor"])))
            v = r.get("verification")
            if v:
                rows.append(("Batch review", "%s: %s (`%s`, anchor %s)" % (v.get("verdict"), cell(v.get("note")), v.get("source"), code(v.get("anchor")))))
            elif r.get("origin") == "legacy":
                rows.append(("Batch review", "not reviewed"))
            L += ["| Item | Value |", "|---|---|"] + ["| %s | %s |" % (k, v2 if str(v2).startswith("`") else cell(v2)) for k, v2 in rows]
            L.append("")
    L += ["## Sources", "", "- `docs/_work/rules/rules.json`", "- `docs/_work/rules/rules-legacy.json`", "- `docs/_work/semantic/programs/`", "",
          "## Confidence", "", "Each rule carries its own Confirmed/Inferred tag. Legacy rules without a batch review are listed as not reviewed."]
    write(os.path.join(c.out, "09-business-rules-catalog.md"), L)


def transfer_targets(c, e):
    """(target, confidence) pairs of one call-graph edge, using resolved dynamic targets."""
    if e.get("resolved_to"):
        best = {}
        order = []
        for r in e["resolved_to"]:
            t = r.get("target")
            if not t:
                continue
            conf = r.get("confidence") or "Inferred"
            if t not in best:
                order.append(t)
                best[t] = conf
            elif conf == "Confirmed":
                best[t] = conf
        return [(t, best[t]) for t in order]
    return [(e["to"], e.get("confidence") or "Confirmed")]


def transaction_reach(c):
    """program -> {transaction: confidence}; Confirmed only if every hop on some path is Confirmed."""
    out_edges = {}
    for e in c.callgraph:
        if e.get("mechanism") in ("XCTL", "LINK", "CALL-static", "CALL-dynamic"):
            for t, conf in transfer_targets(c, e):
                out_edges.setdefault(e["from"], []).append((t, conf))
    reach = {}
    for t in c.transactions:
        start = t["attrs"].get("PROGRAM")
        if not start:
            continue
        best = {start: "Confirmed"}
        todo = [start]
        while todo:
            p = todo.pop()
            for q, conf in out_edges.get(p, []):
                nc = "Confirmed" if best[p] == "Confirmed" and conf == "Confirmed" else "Inferred"
                if q not in best or (best[q] == "Inferred" and nc == "Confirmed"):
                    best[q] = nc
                    todo.append(q)
        for p, conf in best.items():
            cur = reach.setdefault(p, {})
            if cur.get(t["name"]) != "Confirmed":
                cur[t["name"]] = conf
    return reach


def source_locator(c):
    """'path:a[-b]' -> paragraph name, or '<NAME> DIVISION', from the parsed program and copybook structure."""
    idx = {}
    for s in list(c.progs.values()) + list(c.cpys.values()):
        spans = [(p["start_line"], p["end_line"], p["name"]) for p in s.get("paragraphs", []) if p.get("start_line")]
        divs = [(d["start_line"], d["end_line"], d["name"] + " DIVISION") for d in s.get("divisions", []) if d.get("start_line")]
        idx[s["source_path"]] = (spans, divs)

    def locate(src):
        m = re.match(r"^(.+?):(\d+)(?:-(\d+))?$", src or "")
        if not m or m.group(1) not in idx:
            return ""
        a = int(m.group(2))
        spans, divs = idx[m.group(1)]
        for s0, s1, n in spans:
            if s0 <= a <= s1:
                return n
        for s0, s1, n in divs:
            if s0 <= a <= s1:
                return n
        return ""
    return locate


def traceability_page(c, all_rules):
    reach = transaction_reach(c)
    locate = source_locator(c)
    direct = {}
    for t in c.transactions:
        direct.setdefault(t["attrs"].get("PROGRAM"), []).append(t["name"])

    def plink(p):
        return "[%s](07-programs/%s.md)" % (p, p) if p in c.progs else p

    def jlink(j):
        return "[%s](06-batch/jobs/%s.md)" % (j, j) if j in c.job_page.values() else j

    def tx_text(p):
        r = reach.get(p, {})
        if not r:
            return ""
        ds = set(direct.get(p, []))
        parts = []
        for t in sorted(r):
            tag = "starts" if t in ds else ("reached, " + r[t])
            parts.append("%s (%s)" % (t, tag))
        return ", ".join(parts)

    def job_text(p):
        return ", ".join("%s.%s (`%s`)" % (jlink(jn), st["name"], st["source"]) for jn, j, st in c.prog_steps.get(p.upper(), []))

    n_tx = sum(1 for r in all_rules if any(reach.get(i.get("program")) for i in r.get("implementations", [])))
    n_job = sum(1 for r in all_rules if any(c.prog_steps.get((i.get("program") or "").upper()) for i in r.get("implementations", [])))
    L = ["# Cross-reference and traceability", "",
         "Generated by `render_detail.py` from the validated rules (`docs/_work/rules/rules.json`), the CSD structure, the JCL structure and the program call graph. "
         "Every rule is mapped to its program, paragraph (or procedure copybook) and source lines, and to the CICS transactions and batch job steps that run that program. "
         "A transaction *starts* a program when the CSD names it as the transaction's PROGRAM; it *reaches* a program through XCTL, LINK or CALL edges. "
         "A reach is Confirmed when every hop is a literal target and Inferred when a hop uses a resolved dynamic program name (see the call graph below). "
         "The Paragraph column lists the paragraph named by each implementation of the rule; *(derived)* marks a location looked up from the cited line in the parsed "
         "structure (a paragraph, or a division such as DATA DIVISION for 88-level and record definitions) because the rule itself names none.", "",
         "Rules: %d. Rules in programs reached from a CICS transaction: %d. Rules in programs run by a JCL step: %d. "
         "Detail per rule (conditions, outcome, verified anchor) is in the [business rules catalog](09-business-rules-catalog.md)." % (len(all_rules), n_tx, n_job), "",
         "## Rule traceability", ""]
    rows = []
    for r in sorted(all_rules, key=lambda x: x["id"]):
        impl = r.get("implementations") or [{}]
        first = impl[0]
        pgm = first.get("program") or ""
        wh = []
        for i in impl:
            if i.get("paragraph"):
                w = i["paragraph"]
            else:
                d = locate(i.get("source"))
                w = ("%s (derived)" % d) if d else (("copybook " + i["copybook"]) if i.get("copybook") else "")
                if not w and (i.get("source") or "").split(":")[0].lower().endswith(".asm"):
                    w = "Assembler source (no COBOL paragraphs)"
            if w and w not in wh:
                wh.append(w)
        where = ", ".join(wh)
        srcs = ", ".join("`%s`" % i["source"] for i in impl if i.get("source"))
        rows.append(("[%s](09-business-rules-catalog.md#%s)" % (r["id"], anchor_id(r["id"])), r.get("category") or "", r.get("confidence") or "",
                     plink(pgm), cell(where), srcs, tx_text(pgm), job_text(pgm)))
    L += table(["Rule", "Category", "Confidence", "Program", "Paragraph", "Source lines", "CICS transactions", "Batch job steps"], rows)

    L += ["", "## Online flows", "",
          "One row per CSD transaction: the program it starts, the mapsets that program sends or receives, and its XCTL/LINK transfers.", ""]
    rows = []
    for t in sorted(c.transactions, key=lambda x: x["name"]):
        p = t["attrs"].get("PROGRAM", "")
        maps = set()
        if p in c.progs:
            for para in c.progs[p]["paragraphs"]:
                for e in para["exec"]:
                    ms = (e.get("options") or {}).get("MAPSET")
                    if e.get("kind") == "CICS" and ms:
                        maps.add(ms.strip("'\""))
        outs = []
        for e in c.callgraph:
            if e["from"] == p and e.get("mechanism") in ("XCTL", "LINK"):
                tg = ", ".join("%s (%s)" % (x, conf) for x, conf in transfer_targets(c, e))
                outs.append("%s %s `%s`" % (e["mechanism"], tg, e["source"]))
        nrules = len(rules_for_program(c, p, all_rules))
        rows.append((t["name"], plink(p) if p else "", "`%s`" % t["source"], ", ".join(sorted(maps)), nrules, "; ".join(outs) or ("no source in repository" if p and p not in c.progs else "")))
    L += table(["Transaction", "Program", "CSD definition", "Mapsets", "Rules in program", "Transfers out"], rows)

    L += ["", "## Batch flows", "",
          "One row per JCL step that runs an application program (directly, or through `DFSRRC00`/`IKJEFT01`). Datasets and DD lines are on each job page.", ""]
    rows = []
    for path, j in sorted(c.jcl.items()):
        if j["artifact_type"] != "jcl-job":
            continue
        jn = c.job_page[path]
        for st in j["steps"]:
            app = (st.get("application_program") or {}).get("program") or ""
            p = app or (st.get("pgm") or "")
            if p.upper() not in c.progs:
                continue
            rows.append((jlink(jn), st["name"], plink(p.upper()), (st.get("pgm") or "") + (" -> " + app if app else ""), "`%s`" % st["source"],
                         len(rules_for_program(c, p.upper(), all_rules))))
    L += table(["Job", "Step", "Program", "EXEC", "Step source", "Rules in program"], rows) if rows else ["No JCL step runs an application program."]

    L += ["", "## Program calls and transfers", "", "Every CALL, XCTL, LINK and RETURN TRANSID edge. Dynamic targets show each resolved value with its confidence.", ""]
    rows = []
    for e in sorted(c.callgraph, key=lambda x: (x["from"], x.get("source") or "")):
        tg = ", ".join("%s (%s)" % (x, conf) for x, conf in transfer_targets(c, e))
        rows.append((plink(e["from"]), tg if e.get("resolved_to") else plink(e["to"]), e.get("mechanism") or "", e.get("confidence") or "", "`%s`" % e.get("source", "")))
    L += table(["From", "To", "Mechanism", "Confidence", "Source"], rows)

    L += ["", "## Copybooks", "", "Program-to-copybook edges with line numbers are in the [copybook usage matrix](17-dependencies/copybook-usage.md); "
          "field-level references are on each layout page under `08-data/layouts/`.", "",
          "## Sources", "", "- `docs/_work/rules/rules.json`", "- `docs/_work/structure/csd.json`", "- `docs/_work/structure/jcl/`",
          "- `docs/_work/xref/call-graph.json`", "", "## Confidence", "",
          "Rule locations, CSD and JCL rows are Confirmed from source. Transaction reach is Confirmed or Inferred as tagged; Inferred reach depends on resolved dynamic program names."]
    write(os.path.join(c.out, "14-cross-reference-traceability.md"), L)


def dependency_pages(c):
    d = os.path.join(c.out, "17-dependencies")
    # programs
    L = ["# Program dependencies", "", "For each COBOL program: what starts it, what it calls or transfers to, the copybooks it copies, and the data stores it touches.", ""]
    for pgm, s in sorted(c.progs.items()):
        L += ["## %s" % pgm, "", "Page: [%s](../07-programs/%s.md)." % (pgm, pgm), ""]
        rows = []
        for t in c.transactions:
            if t["attrs"].get("PROGRAM") == pgm:
                rows.append(("started by", "CICS transaction " + t["name"], "`%s`" % t["source"]))
        for jn, j, st in c.prog_steps.get(pgm, []):
            rows.append(("started by", "job [%s](../06-batch/jobs/%s.md) step %s" % (jn, jn, st["name"]), "`%s`" % st["source"]))
        for x in c.callgraph:
            tg = [x.get("to")] + [t.get("target") for t in x.get("resolved_to", [])]
            if pgm in tg and x.get("from") != pgm:
                rows.append(("called/transferred by", "%s (%s)" % (x["from"], x.get("mechanism")), "`%s`" % x["source"]))
        for x in c.callgraph:
            if x.get("from") == pgm:
                tg = [t.get("target") for t in x.get("resolved_to", [])] or [x.get("to")]
                rows.append(("calls/transfers to", "%s (%s)" % (", ".join(sorted(set(str(t) for t in tg))), x.get("mechanism")), "`%s`" % x["source"]))
        for u in c.usage:
            if u["from"] == s["source_path"] and not u["commented"]:
                rows.append(("copies", u["copybook"] + (" (system)" if u["resolution"] == "system" else ""), "`%s`" % u["source"]))
        for x in (c.old_prog.get(pgm) or {}).get("crud", []):
            rows.append(("data store", "%s [%s]" % (x["store"], ", ".join(x["ops"])), "`%s`" % x["source"]))
        for p in s["paragraphs"]:
            for e in p["exec"]:
                if e.get("kind") == "SQL" and e.get("tables"):
                    rows.append(("SQL " + e.get("verb", ""), ", ".join(e["tables"]), "`%s`" % e["source"]))
                if e.get("kind") == "DLI" and e.get("verb"):
                    rows.append(("DL/I " + e["verb"], ", ".join(e.get("segments", [])) or e.get("pcb", ""), "`%s`" % e["source"]))
        L += table(["Relation", "Target", "Evidence"], rows) if rows else ["No dependencies recorded."]
        L.append("")
    L += ["## Sources", "", "- `docs/_work/structure/`", "- `docs/_work/xref/call-graph.json`", "- `docs/_work/xref/crud-matrix.json`", "",
          "## Confidence", "", "Confirmed except resolved dynamic transfers, which keep the confidence recorded in the call graph."]
    write(os.path.join(d, "program-dependencies.md"), L)
    # copybooks
    L = ["# Copybook usage matrix", "", "Every COPY and EXEC SQL INCLUDE edge, including commented-out statements and system copybooks.", ""]
    rows = []
    for u in sorted(c.usage, key=lambda x: (x["copybook"], x["from_member"], x["source"])):
        tgt = u["copybook"]
        is_cpy = any(v["member"] == tgt for v in c.cpys.values())
        rows.append(("[%s](../08-data/layouts/%s.md)" % (tgt, tgt) if is_cpy else tgt, u["from_member"], u["from_type"], u["kind"],
                     u["resolution"] + (" (commented out)" if u["commented"] else ""), u.get("resolved_path") or "", "`%s`" % u["source"]))
    L += table(["Copybook", "Used by", "User type", "Statement", "Resolution", "Resolved path", "Line"], rows)
    L += ["", "## Sources", "", "- `docs/_work/structure/copybook-usage.json`", "", "## Confidence", "", "Confirmed: parsed from source."]
    write(os.path.join(d, "copybook-usage.md"), L)
    # jobs
    L = ["# Job dependencies", "", "Programs, PROCs, datasets and scheduler links for every JCL job.", ""]
    for path, j in sorted(c.jcl.items(), key=lambda x: c.job_page.get(x[0], x[1]["member"])):
        if j["artifact_type"] != "jcl-job":
            continue
        name = c.job_page[path]
        L += ["## %s" % name, "", "Page: [%s](../06-batch/jobs/%s.md). Source `%s`." % (name, name, path), ""]
        rows = []
        for st in j["steps"]:
            tgt = st.get("pgm") or ("PROC " + str(st.get("proc")))
            app = st.get("application_program")
            rows.append((st["name"], tgt + (" -> " + app["program"] if app else ""), "`%s`" % st["source"]))
            for dd in st["dds"]:
                if dd.get("dsn") and dd["ddname"] not in ("STEPLIB", "JOBLIB", "SYSPROC"):
                    rows.append((st["name"] + "." + dd["ddname"], "%s DISP=%s" % (dd["dsn"], dd.get("disp") or ""), "`%s`" % dd["source"]))
        for e in c.schedule.get("ca7_edges", []) + c.schedule.get("controlm_edges", []):
            ev = "`%s`" % e["source"]
            if e.get("incond_source"):
                ev += ", `%s`" % e["incond_source"]
            if name == e.get("to"):
                rows.append(("predecessor", e["from"], ev))
            if name == e.get("from"):
                rows.append(("successor", e["to"], ev))
        L += table(["Step / relation", "Target", "Evidence"], rows) if rows else ["No steps."]
        L.append("")
    L += ["## Sources", "", "- `docs/_work/structure/jcl/`", "- `docs/_work/batch/schedule.json`", "", "## Confidence", "", "Confirmed from JCL and scheduler exports."]
    write(os.path.join(d, "job-dependencies.md"), L)
    L = ["# Dependencies", "", "- [Program dependencies](program-dependencies.md)", "- [Copybook usage matrix](copybook-usage.md)",
         "- [Job dependencies](job-dependencies.md)", "- [CICS resource definitions](../05-online/cics-resources.md)", "",
         "## Sources", "", "- `docs/_work/structure/`", "", "## Confidence", "", "Generated index."]
    write(os.path.join(d, "index.md"), L)


def main(argv):
    if len(argv) < 3:
        raise SystemExit(__doc__)
    c = load_ctx(argv[1], argv[2])
    all_rules = consolidate_rules(c)
    for pgm in sorted(c.progs):
        program_page(c, pgm, all_rules)
    program_index(c, all_rules)
    for key, s in sorted(c.cpys.items()):
        copybook_page(c, key, s)
    for path, j in sorted(c.jcl.items()):
        job_page(c, path, j)
    cics_page(c)
    data_definitions_page(c)
    rules_catalog(c, all_rules)
    traceability_page(c, all_rules)
    dependency_pages(c)
    sys.stdout.write("programs=%d copybooks=%d jobs=%d rules=%d\n" % (
        len(c.progs), len(c.cpys), len(c.job_page), len(all_rules)))


if __name__ == "__main__":
    main(sys.argv)
