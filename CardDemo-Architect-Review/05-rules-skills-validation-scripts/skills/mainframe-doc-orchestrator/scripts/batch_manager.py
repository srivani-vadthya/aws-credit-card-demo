"""Batch planning, checkpoints and semantic validation for incremental analysis.

Usage (from the repository root; <work_dir> is usually docs/_work):
  python batch_manager.py init <work_dir> [--budget 4500]   plan batches -> batches/manifest.json
  python batch_manager.py worksheets <work_dir> <BATCH|all>   write worksheets + semantic skeletons
  python batch_manager.py check <work_dir> <BATCH|all|PGM>    validate semantic files, update checkpoints
                                                              ("all" also runs check-reviews)
  python batch_manager.py check-reviews <work_dir>            validate semantic/reviews/*.json (legacy-rule
                                                              reviews for non-COBOL members, e.g. Assembler)
  python batch_manager.py status <work_dir>                   print batch / program status
  python batch_manager.py next <work_dir>                     print the next batch that is not validated

Inputs: <work_dir>/structure/** (extract_structure.py), <work_dir>/inventory.json,
<work_dir>/rules/rules.json (existing rules, optional).
Outputs: <work_dir>/batches/manifest.json, batches/<ID>/worksheet-<PGM>.md,
<work_dir>/semantic/programs/<PGM>.json (skeleton, filled by the analyst),
<work_dir>/semantic/copybooks/<CPY>.json, batches/<ID>/checkpoint.json.

A semantic file is accepted only when: every structural paragraph has a logic
description; every rule cites an existing line range and a verbatim code
anchor found inside that range; a program without rules states why; and the
source sha256 still matches the structure file (otherwise it is stale).
Python 3.1+ standard library only.
"""
import json
import os
import re
import sys
import time

CATEGORIES = ("validation", "calculation", "decision", "transformation", "error-policy",
              "security", "data-integrity", "routing")
CONFIDENCE = ("Confirmed", "Inferred", "Unverified")
VERDICTS = ("confirmed", "corrected", "disputed")


def load(path):
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


def write_text(path, text):
    d = os.path.dirname(path)
    if d and not os.path.isdir(d):
        os.makedirs(d)
    f = open(path, "w", encoding="utf-8", newline="\n")
    try:
        f.write(text)
    finally:
        f.close()


def now():
    return time.strftime("%Y-%m-%dT%H:%M:%S")


def structure_programs(work):
    d = os.path.join(work, "structure", "programs")
    out = {}
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".json"):
            s = load(os.path.join(d, fn))
            out[s["member"]] = s
    return out


def structure_copybooks(work):
    d = os.path.join(work, "structure", "copybooks")
    out = {}
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".json"):
            s = load(os.path.join(d, fn))
            out[fn[:-5]] = s
    return out


def program_edges(progs, jobs_dir):
    """Undirected relationship edges between programs: literal XCTL/LINK/CALL and shared JCL job."""
    names = set(progs)
    edges = dict((p, set()) for p in progs)
    for p, s in progs.items():
        for para in s["paragraphs"]:
            for c in para["calls"]:
                t = c.get("target")
                if t in names and t != p:
                    edges[p].add(t)
                    edges[t].add(p)
            for e in para["exec"]:
                prog = (e.get("options") or {}).get("PROGRAM", "")
                prog = prog.strip("'\"").upper()
                if prog in names and prog != p:
                    edges[p].add(prog)
                    edges[prog].add(p)
    if os.path.isdir(jobs_dir):
        for fn in os.listdir(jobs_dir):
            j = load(os.path.join(jobs_dir, fn))
            run = set()
            for st in j["steps"]:
                for k in ("pgm",):
                    v = (st.get(k) or "").upper()
                    if v in names:
                        run.add(v)
                app = st.get("application_program") or {}
                if app.get("program", "").upper() in names:
                    run.add(app["program"].upper())
            run = sorted(run)
            for a in run:
                for b in run:
                    if a != b:
                        edges[a].add(b)
    return edges


def cmd_init(work, budget):
    progs = structure_programs(work)
    inv = load(os.path.join(work, "inventory.json"))
    module = {}
    for e in inv["files"]:
        if e["type"] == "cobol-program":
            module[e["member"].upper()] = e.get("module") or "none"
    edges = program_edges(progs, os.path.join(work, "structure", "jcl"))
    # connected components inside each module
    seen, comps = set(), []
    for p in sorted(progs, key=lambda x: (module.get(x, ""), x)):
        if p in seen:
            continue
        queue, comp = [p], []
        while queue:
            x = queue.pop(0)
            if x in seen:
                continue
            seen.add(x)
            comp.append(x)
            for y in sorted(edges[x]):
                if module.get(y) == module.get(p) and y not in seen:
                    queue.append(y)
        comps.append((module.get(p, ""), comp))
    # pack components into batches under the line budget (split oversized components)
    batches, cur, cur_lines, cur_mod = [], [], 0, None
    for mod, comp in comps:
        for p in comp:
            n = progs[p]["line_count"]
            if cur and (cur_lines + n > budget or mod != cur_mod):
                batches.append((cur_mod, cur))
                cur, cur_lines = [], 0
            cur.append(p)
            cur_lines += n
            cur_mod = mod
    if cur:
        batches.append((cur_mod, cur))
    usage = load(os.path.join(work, "structure", "copybook-usage.json"))["edges"]
    cpy_members = set(v["member"] for v in structure_copybooks(work).values())
    usage = [u for u in usage if u["copybook"] in cpy_members]
    cpy_module = {}
    for e in inv["files"]:
        if e["type"] in ("cobol-copybook", "db2-dclgen"):
            cpy_module.setdefault(e["member"].upper(), e.get("module"))
    copy_owner = {}
    manifest = {"schema": "batch-manifest/1", "created": now(), "budget_lines": budget, "batches": []}
    used_by_batch = []
    for i, (mod, members) in enumerate(batches):
        cpys = sorted(set(u["copybook"] for u in usage if u["from_member"] in members and
                          u["resolution"] == "inventory" and not u["commented"]))
        used_by_batch.append(cpys)
    for i, (mod, members) in enumerate(batches):
        for c in used_by_batch[i]:
            if c in copy_owner:
                continue
            same = [k for k, (m2, _) in enumerate(batches) if c in used_by_batch[k] and m2 == cpy_module.get(c)]
            copy_owner[c] = "B%02d" % ((same[0] if same else i) + 1)
    for i, (mod, members) in enumerate(batches):
        bid = "B%02d" % (i + 1)
        manifest["batches"].append({
            "id": bid, "module": mod, "programs": members,
            "lines": sum(progs[p]["line_count"] for p in members),
            "copybooks_used": used_by_batch[i],
            "copybooks_owned": sorted(c for c, b in copy_owner.items() if b == bid),
            "status": "pending", "updated": now()})
    # copybooks that no program copies go to a final batch
    cmap = structure_copybooks(work)
    orphan = sorted(set(s["member"] for s in cmap.values()) - set(copy_owner))
    if orphan:
        manifest["batches"].append({"id": "B%02d" % (len(batches) + 1), "module": "copybooks-only",
                                    "programs": [], "lines": 0, "copybooks_used": orphan,
                                    "copybooks_owned": orphan, "status": "pending", "updated": now()})
    save(os.path.join(work, "batches", "manifest.json"), manifest)
    for b in manifest["batches"]:
        sys.stdout.write("%s %-16s %5d lines  %s | copybooks owned: %s\n" % (
            b["id"], b["module"], b["lines"], " ".join(b["programs"]), " ".join(b["copybooks_owned"])))


def existing_rules_for(work, pgm):
    p = os.path.join(work, "rules", "rules.json")
    if not os.path.exists(p):
        return []
    out = []
    for r in load(p)["rules"]:
        if any(i.get("program") == pgm for i in r.get("implementations", [])):
            out.append(r)
    return out


def worksheet(work, s, rules):
    L = ["# Worksheet %s (%s)" % (s["member"], s["source_path"]), "",
         "Lines: %d. Paragraphs: %d. Decision points: %d (business candidates: %d)." % (
             s["line_count"], s["counts"]["paragraphs"], s["counts"]["decisions"],
             s["counts"]["business_candidate_decisions"]), "",
         "Fill `docs/_work/semantic/programs/%s.json`. Read the whole source; this list only "
         "indexes it." % s["member"], "", "## Paragraphs", "",
         "| Paragraph | Lines | Performs | Performed by |", "|---|---|---|---|"]
    for p in s["paragraphs"]:
        L.append("| %s | %d-%d | %s | %s |" % (p["name"], p["start_line"], p["end_line"],
                                             ", ".join(sorted(set(x["target"] for x in p["performs"] if x.get("target")))),
                                             ", ".join(p.get("performed_by", []))))
    L += ["", "## Decision points that look like business logic", "",
          "Each line below must fall inside a rule `source` range or a `no_rule_decisions` range.", "",
          "| Line | Paragraph | Type | Condition |", "|---|---|---|---|"]
    for p in s["paragraphs"]:
        for d in p["decisions"]:
            if d["class"] == "business-candidate":
                L.append("| %d | %s | %s | `%s` |" % (d["line"], p["name"], d["type"], d["condition"][:120].replace("|", "\\|")))
    L += ["", "## Calculations", ""]
    for p in s["paragraphs"]:
        for c in p["calculations"]:
            L.append("- %d (%s): `%s`" % (c["line"], p["name"], c["text"][:160]))
    if rules:
        L += ["", "## Existing rules to review (record a verdict and anchor for each)", ""]
        for r in rules:
            L.append("- %s: %s (%s)" % (r["id"], r["statement"], ", ".join(i["source"] for i in r.get("implementations", []))))
    L.append("")
    return "\n".join(L)


def skeleton(s, batch, rules):
    return {
        "schema": "program-semantics/1", "program": s["member"], "source_path": s["source_path"],
        "source_sha256": s["sha256"], "batch": batch, "status": "skeleton",
        "summary": {"text": "", "confidence": "Inferred", "evidence": []},
        "paragraphs": [{"name": p["name"], "lines": "%d-%d" % (p["start_line"], p["end_line"]),
                        "logic": "", "confidence": "Inferred"} for p in s["paragraphs"]],
        "rules": [],
        "existing_rules_reviewed": [{"id": r["id"], "verdict": "", "anchor": "", "source": "", "note": ""} for r in rules],
        "no_rule_decisions": [],
        "no_business_rules_reason": None,
        "observations": [], "sme_questions": []}


def cmd_worksheets(work, which):
    man = load(os.path.join(work, "batches", "manifest.json"))
    progs = structure_programs(work)
    cmap = structure_copybooks(work)
    by_member = {}
    for k, v in cmap.items():
        by_member.setdefault(v["member"], []).append(v)
    for b in man["batches"]:
        if which not in ("all", b["id"]):
            continue
        for pgm in b["programs"]:
            s = progs[pgm]
            rules = existing_rules_for(work, pgm)
            write_text(os.path.join(work, "batches", b["id"], "worksheet-%s.md" % pgm), worksheet(work, s, rules))
            sp = os.path.join(work, "semantic", "programs", pgm + ".json")
            if not os.path.exists(sp):
                save(sp, skeleton(s, b["id"], rules))
        for c in b["copybooks_owned"]:
            cp = os.path.join(work, "semantic", "copybooks", c + ".json")
            if not os.path.exists(cp):
                srcs = by_member.get(c, [])
                save(cp, {"schema": "copybook-semantics/1", "copybook": c, "batch": b["id"], "status": "skeleton",
                          "source_paths": [x["source_path"] for x in srcs],
                          "source_sha256": [x["sha256"] for x in srcs],
                          "purpose": "", "confidence": "Inferred", "evidence": [],
                          "key_fields": [], "observations": []})
        b["status"] = "worksheets-ready" if b["status"] == "pending" else b["status"]
        b["updated"] = now()
    save(os.path.join(work, "batches", "manifest.json"), man)
    sys.stdout.write("worksheets written for %s\n" % which)


# ----------------------------------------------------------------- validation
_line_cache = {}


def source_lines(path):
    if path not in _line_cache:
        f = open(path, "rb")
        try:
            t = f.read().decode("latin-1")
        finally:
            f.close()
        lines = t.replace("\r\n", "\n").replace("\r", "\n").split("\n")
        if lines and lines[-1] == "":
            lines.pop()
        _line_cache[path] = lines
    return _line_cache[path]


def parse_src(ref):
    m = re.match(r"^(.+?):(\d+)(?:-(\d+))?$", ref.strip().strip("`"))
    if not m:
        return None
    return m.group(1), int(m.group(2)), int(m.group(3) or m.group(2))


def norm(text):
    return re.sub(r"\s+", " ", text.replace("\t", " ")).strip().upper()


def code_text(path, a, b):
    lines = source_lines(path)
    parts = []
    is_cobol = re.search(r"\.(cbl|cpy|cob|dcl)$", path, re.I) is not None
    for l in lines[a - 1:b]:
        if is_cobol:
            e = l.expandtabs(8)
            if len(e) > 6 and e[6] in "*/":
                continue
            parts.append(e[7:] if "\t" in l else e[7:72])
        else:
            parts.append(l[:72] if path.lower().endswith((".jcl", ".prc")) else l)
    return norm(" ".join(parts))


def check_ref(ref, issues, where, anchor=None):
    p = parse_src(ref or "")
    if not p:
        issues.append("%s: unparseable source '%s'" % (where, ref))
        return None
    path, a, b = p
    if not os.path.isfile(path):
        issues.append("%s: file not found %s" % (where, path))
        return None
    n = len(source_lines(path))
    if a < 1 or b > n or a > b:
        issues.append("%s: line range %d-%d outside 1-%d of %s" % (where, a, b, n, path))
        return None
    if anchor is not None:
        if not anchor.strip():
            issues.append("%s: empty anchor" % where)
        elif norm(anchor) not in code_text(path, a, b):
            issues.append("%s: anchor not found verbatim in %s: '%s'" % (where, ref, anchor[:80]))
    return p


COBOL_WORDS = set((
    "ACCEPT ADD AFTER ALL ALSO AND ANY ARE AREA AT BEFORE BY CALL CANCEL CLOSE COMPUTE CONTINUE CORR "
    "CORRESPONDING DELETE DEPENDING DISPLAY DIVIDE ELSE END EQUAL ERROR EVALUATE EXEC EXIT FALSE FILE FROM "
    "FUNCTION GIVING GOBACK GREATER INITIALIZE INSPECT INTO INVALID KEY LENGTH LESS MOVE MULTIPLY NEXT NOT "
    "NUMERIC ALPHABETIC OF OFF ON OPEN OR OTHER PERFORM PROGRAM READ RECORD REPLACING RETURN REWRITE ROUNDED "
    "SENTENCE SET SIZE SPACE SPACES START STOP STRING SUBTRACT TALLYING TEST THAN THEN THROUGH THRU TIMES TO "
    "TRUE UNSTRING UNTIL UPON USING VALUE VARYING WHEN WITH WRITE ZERO ZEROS ZEROES HIGH-VALUES LOW-VALUES "
    "INPUT OUTPUT I-O EXTEND CICS SQL DLI RESP RESP2 NOHANDLE COMMAREA DELIMITED POINTER COUNT INTO "
    "INDEXED SEARCH IS NULL NULLS QUOTE QUOTES").split())


def code_tokens(path, a, b):
    """Identifiers and literals a paragraph description could name (comments excluded)."""
    words, lits = set(), set()
    for n, l in enumerate(source_lines(path)[a - 1:b]):
        e = l.expandtabs(8)
        if len(e) < 8 or e[6] in "*/":
            continue
        body = e[7:72]
        if n == 0 and body[:4].strip():
            body = re.sub(r"^\s*[A-Za-z0-9][A-Za-z0-9-]*(\s+SECTION)?\s*\.", " ", body, flags=re.I)
        for m in re.finditer(r"'([^']*)'|\"([^\"]*)\"", body):
            v = (m.group(1) or m.group(2) or "").strip()
            if len(v) >= 2:
                lits.add(v.upper())
        body = re.sub(r"'[^']*'|\"[^\"]*\"", " ", body.upper())
        for w in re.findall(r"(?<![A-Z0-9-])[A-Z0-9][A-Z0-9-]*[A-Z0-9](?![A-Z0-9-])", body):
            if w in COBOL_WORDS or w.startswith("END-") or len(w) < 3 or not re.search(r"[A-Z]", w):
                continue
            words.add(w)
    return words, lits


def logic_grounded(logic, name, path, a, b):
    """True when the description names at least one identifier or literal of its own code."""
    words, lits = code_tokens(path, a, b)
    if not words and not lits:
        return True
    up = " " + re.sub(r"\s+", " ", (logic or "").upper()) + " "
    if name.upper() in up:
        return True
    for w in words:
        if re.search(r"(?<![A-Z0-9-])" + re.escape(w) + r"(?![A-Z0-9-])", up):
            return True
    for v in lits:
        if v in up:
            return True
    return False


def validate_program(work, pgm, struct):
    issues, warnings = [], []
    sp = os.path.join(work, "semantic", "programs", pgm + ".json")
    if not os.path.exists(sp):
        return {"program": pgm, "status": "unanalyzed", "issues": ["no semantic file"], "warnings": []}
    try:
        sem = load(sp)
    except ValueError as ex:
        return {"program": pgm, "status": "invalid", "issues": ["JSON error: %s" % ex], "warnings": []}
    if sem.get("source_sha256") != struct["sha256"]:
        issues.append("stale: source sha256 changed since analysis")
    if sem.get("status") == "skeleton":
        issues.append("status is still 'skeleton'")
    if not (sem.get("summary") or {}).get("text"):
        issues.append("summary.text empty")
    for ev in (sem.get("summary") or {}).get("evidence", []):
        check_ref(ev, issues, "summary.evidence")
    want = dict((p["name"], p) for p in struct["paragraphs"])
    got = {}
    for p in sem.get("paragraphs", []):
        got[p.get("name")] = p
    described = 0
    ungrounded = []
    for name, p in want.items():
        g = got.get(name)
        if not g:
            issues.append("paragraph missing: %s" % name)
            continue
        if len((g.get("logic") or "").strip()) < 15:
            issues.append("paragraph logic empty/too short: %s" % name)
        else:
            described += 1
            if os.path.isfile(struct["source_path"]) and not logic_grounded(
                    g["logic"], name, struct["source_path"], p["start_line"], p["end_line"]):
                ungrounded.append(name)
        if g.get("confidence") not in CONFIDENCE:
            issues.append("paragraph %s: bad confidence" % name)
    for name in got:
        if name not in want:
            issues.append("paragraph not in source structure: %s" % name)
    ids = set()
    rule_ranges = []
    for i, r in enumerate(sem.get("rules", [])):
        w = "rule[%d] %s" % (i, r.get("id"))
        if not r.get("id") or r["id"] in ids:
            issues.append("%s: missing or duplicate id" % w)
        ids.add(r.get("id"))
        if r.get("category") not in CATEGORIES:
            issues.append("%s: category must be one of %s" % (w, ", ".join(CATEGORIES)))
        if r.get("confidence") not in CONFIDENCE:
            issues.append("%s: bad confidence" % w)
        if len((r.get("statement") or "").strip()) < 20:
            issues.append("%s: statement too short" % w)
        if r.get("paragraph") and r["paragraph"] not in want and not r.get("copybook"):
            issues.append("%s: paragraph %s not in structure" % (w, r["paragraph"]))
        refs = [r.get("source")] + list(r.get("additional_sources", []))
        p = check_ref(r.get("source"), issues, w, r.get("anchor", ""))
        for extra in r.get("additional_sources", []):
            q = check_ref(extra, issues, w + " additional")
            if q:
                rule_ranges.append(q)
        if p:
            rule_ranges.append(p)
            if r.get("paragraph") in want and p[0] == struct["source_path"]:
                para = want[r["paragraph"]]
                if p[2] < para["start_line"] or p[1] > para["end_line"]:
                    issues.append("%s: source %s outside paragraph %s (%d-%d)" % (
                        w, r["source"], r["paragraph"], para["start_line"], para["end_line"]))
    for i, e in enumerate(sem.get("existing_rules_reviewed", [])):
        w = "existing[%s]" % e.get("id")
        if e.get("verdict") not in VERDICTS:
            issues.append("%s: verdict must be one of %s" % (w, ", ".join(VERDICTS)))
        p = check_ref(e.get("source"), issues, w, e.get("anchor", ""))
        if p:
            rule_ranges.append(p)
    nr_ranges = []
    for i, n in enumerate(sem.get("no_rule_decisions", [])):
        w = "no_rule_decisions[%d]" % i
        if not (n.get("reason") or "").strip():
            issues.append("%s: reason required" % w)
        p = check_ref(n.get("source"), issues, w)
        if p:
            nr_ranges.append(p)
    if not sem.get("rules") and not (sem.get("no_business_rules_reason") or "").strip() \
            and not sem.get("existing_rules_reviewed"):
        issues.append("no rules and no no_business_rules_reason")
    for i, o in enumerate(sem.get("observations", [])):
        if o.get("source"):
            check_ref(o["source"], issues, "observations[%d]" % i)
    for i, q in enumerate(sem.get("sme_questions", [])):
        if q.get("source"):
            check_ref(q["source"], issues, "sme_questions[%d]" % i)
    # decision coverage
    path = struct["source_path"]
    cand, covered, uncovered = 0, 0, []
    for p in struct["paragraphs"]:
        for d in p["decisions"]:
            if d["class"] != "business-candidate":
                continue
            cand += 1
            hit = any(r[0] == path and r[1] <= d["line"] <= r[2] for r in rule_ranges + nr_ranges)
            if hit:
                covered += 1
            else:
                uncovered.append({"line": d["line"], "paragraph": p["name"], "condition": d["condition"][:100]})
    in_rules = sum(1 for p in struct["paragraphs"] for d in p["decisions"]
                   if d["class"] == "business-candidate" and
                   any(r[0] == path and r[1] <= d["line"] <= r[2] for r in rule_ranges))
    if uncovered:
        warnings.append("%d business-candidate decision points not linked to a rule or no-rule reason" % len(uncovered))
    if ungrounded:
        warnings.append("%d paragraph descriptions name no identifier or literal of their code: %s" % (
            len(ungrounded), ", ".join(ungrounded[:20])))
    status = "validated" if not issues else "failed"
    return {"program": pgm, "status": status, "issues": issues, "warnings": warnings,
            "paragraphs_total": len(want), "paragraphs_described": described,
            "ungrounded_paragraphs": ungrounded,
            "rules": len(sem.get("rules", [])), "existing_reviewed": len(sem.get("existing_rules_reviewed", [])),
            "decision_candidates": cand, "decision_covered": covered, "decision_in_rules": in_rules,
            "uncovered_decisions": uncovered, "checked": now()}


def validate_copybook(work, cpy, cmap):
    cp = os.path.join(work, "semantic", "copybooks", cpy + ".json")
    if not os.path.exists(cp):
        return {"copybook": cpy, "status": "unanalyzed", "issues": ["no semantic file"]}
    sem = load(cp)
    issues = []
    if sem.get("status") == "skeleton":
        issues.append("status is still 'skeleton'")
    if len((sem.get("purpose") or "").strip()) < 20:
        issues.append("purpose empty/too short")
    shas = [v["sha256"] for v in cmap.values() if v["member"] == cpy]
    if sorted(sem.get("source_sha256", [])) != sorted(shas):
        issues.append("stale: copybook sha256 changed since analysis")
    for ev in sem.get("evidence", []):
        check_ref(ev, issues, "evidence")
    names = set()
    for v in cmap.values():
        if v["member"] == cpy:
            for it in v.get("data_items", []):
                names.add(it["name"])
                for c in it.get("conditions", []):
                    names.add(c["name"])
            for p in v.get("paragraphs", []):
                names.add(p["name"])
    for i, k in enumerate(sem.get("key_fields", [])):
        if k.get("name") not in names:
            issues.append("key_fields[%d]: %s is not an item, 88-level or paragraph of %s" % (i, k.get("name"), cpy))
        if k.get("source"):
            check_ref(k["source"], issues, "key_fields[%d]" % i)
    for i, o in enumerate(sem.get("observations", [])):
        if o.get("source"):
            check_ref(o["source"], issues, "observations[%d]" % i)
    for key, val in sem.items():
        if key in ("key_fields", "observations", "evidence") or not isinstance(val, list):
            continue
        for i, o in enumerate(val):
            if isinstance(o, dict) and isinstance(o.get("source"), str) and ":" in o["source"]:
                check_ref(o["source"], issues, "%s[%d]" % (key, i))
    return {"copybook": cpy, "status": "validated" if not issues else "failed", "issues": issues, "checked": now()}


def cmd_check(work, which, quiet=False, write_manifest=True):
    man = load(os.path.join(work, "batches", "manifest.json"))
    progs = structure_programs(work)
    cmap = structure_copybooks(work)
    results = []
    for b in man["batches"]:
        sel = which in ("all", b["id"]) or which in b["programs"] or which in b["copybooks_owned"]
        if not sel:
            continue
        cp = {"batch": b["id"], "programs": {}, "copybooks": {}, "checked": now()}
        for pgm in b["programs"]:
            if which in b["programs"] and which != pgm:
                continue
            r = validate_program(work, pgm, progs[pgm])
            cp["programs"][pgm] = r
            results.append(r)
        for c in b["copybooks_owned"]:
            if which in b["copybooks_owned"] and which != c:
                continue
            r = validate_copybook(work, c, cmap)
            cp["copybooks"][c] = r
            results.append(r)
        prev_p = os.path.join(work, "batches", b["id"], "checkpoint.json")
        if os.path.exists(prev_p) and which not in ("all", b["id"]):
            prev = load(prev_p)
            prev["programs"].update(cp["programs"])
            prev["copybooks"].update(cp["copybooks"])
            prev["checked"] = cp["checked"]
            cp = prev
        save(prev_p, cp)
        sts = [x["status"] for x in list(cp["programs"].values()) + list(cp["copybooks"].values())]
        expected = len(b["programs"]) + len(b["copybooks_owned"])
        if len(sts) == expected and sts and all(s == "validated" for s in sts):
            b["status"] = "validated"
        elif any(s in ("validated", "failed") for s in sts):
            b["status"] = "in-progress"
        b["updated"] = now()
    if write_manifest:
        save(os.path.join(work, "batches", "manifest.json"), man)
    bad = 0
    for r in results:
        name = r.get("program") or r.get("copybook")
        extra = ""
        if "paragraphs_total" in r:
            extra = " paragraphs %d/%d rules %d decisions %d/%d" % (
                r["paragraphs_described"], r["paragraphs_total"], r["rules"], r["decision_covered"], r["decision_candidates"])
        sys.stdout.write("%-10s %-10s issues=%d%s\n" % (name, r["status"], len(r["issues"]), extra))
        if not quiet:
            for i in r["issues"][:40]:
                sys.stdout.write("    - %s\n" % i)
            for w in r.get("warnings", []):
                sys.stdout.write("    ~ %s\n" % w)
        if r["status"] != "validated":
            bad += 1
    return bad


def cmd_check_reviews(work, quiet=False):
    """Validate semantic/reviews/<MEMBER>.json: legacy-rule reviews for members outside the COBOL batches
    (Assembler, PL/I, JCL). Same anchor rules as program semantics; writes batches/reviews-checkpoint.json."""
    d = os.path.join(work, "semantic", "reviews")
    inv = load(os.path.join(work, "inventory.json"))
    sha = dict((e["path"], e.get("sha256")) for e in inv["files"])
    legacy_p = os.path.join(work, "rules", "rules-legacy.json")
    legacy = dict((r["id"], r) for r in load(legacy_p)["rules"]) if os.path.exists(legacy_p) else {}
    out = {"schema": "reviews-checkpoint/1", "checked": now(), "members": {}}
    bad = 0
    for fn in sorted(os.listdir(d)) if os.path.isdir(d) else []:
        if not fn.endswith(".json"):
            continue
        member, issues = fn[:-5], []
        try:
            r = load(os.path.join(d, fn))
        except ValueError as ex:
            r, issues = {}, ["JSON error: %s" % ex]
        sp = r.get("source_path", "")
        if not os.path.isfile(sp):
            issues.append("source_path not found: %s" % sp)
        else:
            import hashlib
            f = open(sp, "rb")
            try:
                cur = hashlib.sha256(f.read()).hexdigest()
            finally:
                f.close()
            if r.get("source_sha256") != cur:
                issues.append("stale: source sha256 changed since review")
            if sha.get(sp) and sha[sp] != cur:
                issues.append("inventory sha256 differs from file; re-run discovery")
        for e in r.get("existing_rules_reviewed", []):
            w = "existing[%s]" % e.get("id")
            if e.get("id") not in legacy:
                issues.append("%s: not a rule id in rules-legacy.json" % w)
            if e.get("verdict") not in VERDICTS:
                issues.append("%s: verdict must be one of %s" % (w, ", ".join(VERDICTS)))
            if len((e.get("note") or "").strip()) < 20:
                issues.append("%s: note must explain the verdict" % w)
            check_ref(e.get("source"), issues, w, e.get("anchor", ""))
        st = "validated" if not issues else "failed"
        out["members"][member] = {"status": st, "issues": issues, "reviewed": len(r.get("existing_rules_reviewed", [])),
                                  "checked": now()}
        sys.stdout.write("%-10s %-10s issues=%d reviews=%d\n" % (member, st, len(issues), len(r.get("existing_rules_reviewed", []))))
        if not quiet:
            for i in issues:
                sys.stdout.write("    - %s\n" % i)
        if issues:
            bad += 1
    save(os.path.join(work, "batches", "reviews-checkpoint.json"), out)
    return bad


def cmd_status(work):
    man = load(os.path.join(work, "batches", "manifest.json"))
    for b in man["batches"]:
        sys.stdout.write("%s %-18s %-16s %s\n" % (b["id"], b["status"], b["module"], " ".join(b["programs"] + b["copybooks_owned"])))
    rc = os.path.join(work, "batches", "reviews-checkpoint.json")
    if os.path.exists(rc):
        for m, v in sorted(load(rc).get("members", {}).items()):
            sys.stdout.write("REVIEW %-15s %-16s %s\n" % (v["status"], "non-cobol", m))


def cmd_next(work):
    man = load(os.path.join(work, "batches", "manifest.json"))
    for b in man["batches"]:
        if b["status"] != "validated":
            sys.stdout.write(json.dumps(b, indent=1, sort_keys=True) + "\n")
            return
    sys.stdout.write("all batches validated\n")


def main(argv):
    if len(argv) < 3:
        raise SystemExit(__doc__)
    cmd, work = argv[1], argv[2]
    if cmd == "init":
        budget = int(argv[argv.index("--budget") + 1]) if "--budget" in argv else 4500
        cmd_init(work, budget)
    elif cmd == "worksheets":
        cmd_worksheets(work, argv[3] if len(argv) > 3 else "all")
    elif cmd == "check":
        which = argv[3] if len(argv) > 3 else "all"
        bad = cmd_check(work, which, "--quiet" in argv, "--no-manifest" not in argv)
        if which == "all":
            bad += cmd_check_reviews(work, "--quiet" in argv)
        sys.exit(1 if bad else 0)
    elif cmd == "check-reviews":
        sys.exit(1 if cmd_check_reviews(work, "--quiet" in argv) else 0)
    elif cmd == "status":
        cmd_status(work)
    elif cmd == "next":
        cmd_next(work)
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main(sys.argv)
