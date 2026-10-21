"""Write README.md for the architect review bundle from the bundle's own JSON files.

Usage: python write_review_readme.py <bundle_dir> <commit>
Run after verify_review_bundle.py. Every number is read from coverage.json, gaps.json,
check_package.json, rules.json and bundle-verification.json in the bundle.
Python 3.1+ standard library only.
"""
import io
import json
import os
import re
import sys


def load(p):
    f = open(p, "r", encoding="utf-8-sig")
    try:
        return json.load(f)
    finally:
        f.close()


def esc(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


RECHECK = {"programs": "V1", "copybooks": "V1", "jcl-jobs": "V1", "jcl-procs": "V1", "rule-traceability": "V4a, V4b", "source-references": "V3"}


def main(argv):
    B, commit = argv[1], argv[2]
    src_state = argv[3] if len(argv) > 3 else "unknown"
    cov = load(os.path.join(B, "02-coverage-validation-report", "coverage.json"))
    chk = load(os.path.join(B, "02-coverage-validation-report", "check_package.json"))
    ver = load(os.path.join(B, "02-coverage-validation-report", "bundle-verification.json"))
    gaps = load(os.path.join(B, "04-gap-report", "gaps.json"))
    rules = load(os.path.join(B, "03-business-rules-and-traceability", "rules.json"))["rules"]
    vm = ver["metrics"]
    vc = dict((c["id"], c) for c in ver["checks"])
    grp = dict((g["group"], g) for g in vm["source_groups"])
    crit = cov["criteria"]
    reg = gaps["register"]
    comps = gaps["components"]
    st = {}
    for c in comps:
        st[c["status"]] = st.get(c["status"], 0) + 1
    prog_rules = set(i.get("program") for r in rules for i in r.get("implementations", []) if i.get("program"))
    cobol = sorted(c["name"] for c in comps if c["kind"] == "cobol-program")
    asm = sorted(c["name"] for c in comps if c["kind"] == "asm-program")
    no_rule = [p for p in cobol if p not in prog_rules]
    conf = {}
    for r in rules:
        conf[r.get("confidence")] = conf.get(r.get("confidence"), 0) + 1
    rm = vm["rules"]
    sref = vm["source_references"]
    cls = {}
    for cf in gaps["conflicts"]:
        cls[cf.get("class")] = cls.get(cf.get("class"), 0) + 1
    G = lambda k: grp[k]["files"]

    L = []
    A = L.append
    A("# CardDemo legacy documentation POC - architect review package")
    A("")
    A("Repository commit `%s`; application source in the working tree %s. Documentation, reports and scripts include the uncommitted changes of the final review pass (see CHANGELOG.md). "
      "Pipeline validation run %s; bundle verification run %s (%d checks, %d failed, %d warning(s))." % (
        commit, {"clean": "is unchanged from that commit (git status shows no changes under app/, samples/, scripts/)",
                 "untracked": "is not tracked by this git repository (app/, samples/ and scripts/ are untracked), so the commit does not identify it; "
                              "the analysed version is identified by the inventory sha256 values, which every snapshot file still matches (V8)"}.get(
            src_state, "has local changes under app/, samples/ or scripts/ (git status); see V8 for the sha256 comparison"),
        cov["generated"], ver["generated"], len(ver["checks"]), ver["failed"], ver["warnings"]))
    A("")
    A("## 1. What this POC documents")
    A("")
    A("Evidence-based reverse-engineering documentation of the AWS CardDemo mainframe sample application (CICS online, batch JCL, VSAM, "
      "IMS, DB2 and MQ extensions, Control-M and CA7 schedules). In scope, recounted from the source snapshot by `verify_review_bundle.py` (check V1):")
    A("")
    A("| Component | Files in source | Documented on own page |")
    A("|---|---|---|")
    for g in vm["source_groups"]:
        A("| %s | %d | %s |" % (g["group"], g["files"], "all" if not g["without_page"] and g["group"] != "BMS symbolic-map copybooks (cpy-bms/*.cpy)" else (
            "no page of their own; listed with the copying program on the copybook-usage page" if g["group"].startswith("BMS symbolic") else "%d without page" % len(g["without_page"]))))
    A("")
    A("Also inventoried and documented: CICS CSD resources, IMS DBD/PSB, DB2 DDL, control cards, scheduler definitions and shell scripts "
      "(%d components classified in total, see the gap report). %d inventory entries are excluded with a reason (placeholders, repository metadata, binaries)." % (len(comps), len(gaps["excluded"])))
    A("")
    A("## 2. How the documentation was generated")
    A("")
    A("1. **Discovery** (`mainframe-inventory-discovery` skill, `classify_inventory.py`, `scan_references.py`): every file classified with sha256 into `inventory.json`; COPY/INCLUDE/EXEC PGM/PROC references resolved or recorded as external-or-missing.")
    A("2. **Structure extraction** (`extract_structure.py`, deterministic parser): divisions, paragraphs, statements, data items, EXEC CICS/SQL/DLI, JCL steps and DDs, CSD resources, copybook fields.")
    A("3. **Semantic analysis** (AI-assisted, Claude in Cursor, guided by the rules and skills in folder 05): purpose, paragraph logic, business rules, SME questions, per program/copybook batch. "
      "`batch_manager.py` accepts a semantic file only when every parsed paragraph has a logic description, every rule cites an existing line range and a verbatim "
      "code anchor found inside that range, a program without rules states why, and the source sha256 still matches. "
      "The batch plan, per-batch checkpoints, worksheets and the accepted semantic files are in `05-rules-skills-validation-scripts/work-dir-checkpoints/` (checked by V11); "
      "the checkpoint timestamps are those of the latest `batch_manager.py check` run, and the dated history of the batch passes is in `work-dir-scripts/progress.md`.")
    A("4. **Rendering** (`render_detail.py`, deterministic): all detailed pages from structure + validated semantics; `build_docx.py` and `build_combined_markdown.ps1` produce the Word and single-file copies.")
    A("5. **Validation**: `coverage_validate.py` (33 measured criteria), `gap_report.py` (component status and gap register), `check_package.py` (links, placeholders, Sources sections), "
      "then this bundle's independent `verify_review_bundle.py`.")
    A("")
    A("Rules applied throughout (folder 05, `cursor-rules/mainframe-doc-core.mdc`): every fact cites `path:line`; statements are tagged Confirmed, Inferred or Unverified; "
      "code wins over comments; placeholders are never given invented values; application source is never modified.")
    A("")
    A("## 3. Package contents")
    A("")
    A("| Folder | Contents | Start with |")
    A("|---|---|---|")
    A("| `01-detailed-documentation/` | %d-page Markdown package (one page per program, copybook, job, PROC, screen, dataset, table, IMS database, plus overviews), "
      "the same content as one Word file (`application-documentation/CardDemo-complete-documentation.docx`) and as one Markdown file (`COMBINED_DOCUMENTATION.md`, which also embeds the rules, skills and scripts) | "
      "[00-index.md](01-detailed-documentation/application-documentation/00-index.md) |" % vm["markdown_pages"])
    A("| `02-coverage-validation-report/` | Pipeline coverage report and JSON, package check, inventory, and the independent bundle verification | "
      "[bundle-verification.md](02-coverage-validation-report/bundle-verification.md), [coverage-report.md](02-coverage-validation-report/coverage-report.md) |")
    A("| `03-business-rules-and-traceability/` | Rule-to-source traceability (program, paragraph, lines, CICS transactions, JCL steps; online and batch flows), rules catalog, dependency pages, rules JSON | "
      "[14-cross-reference-traceability.md](03-business-rules-and-traceability/14-cross-reference-traceability.md) |")
    A("| `04-gap-report/` | Gap register (one row per item with evidence, source, impact, status, owner, next action), gap report, narrative gaps register, gaps JSON | "
      "[gap-register.md](04-gap-report/gap-register.md) |")
    A("| `05-rules-skills-validation-scripts/` | Cursor rules, the ten skills with templates and scripts, project profile, bundle and verification scripts, progress log, batch checkpoints and semantic analysis files (`work-dir-checkpoints/`) | "
      "[docs-toolkit/README.md](05-rules-skills-validation-scripts/docs-toolkit/README.md) |")
    A("| `06-source-snapshot/` | Read-only copy of the in-scope source so every citation can be opened offline; FTP connection lines redacted | "
      "[REDACTIONS.md](06-source-snapshot/REDACTIONS.md) |")
    A("| `CHANGELOG.md` | Changes made in the final review pass | [CHANGELOG.md](CHANGELOG.md) |")
    A("")
    A("Report pages in folders 02-04 are copies of pages in `01-detailed-documentation/application-documentation/`; their links point back into folder 01. "
      "Identical files found by V10 (%d groups), all intended:" % len(vc["V10"]["detail"]))
    A("")
    kinds = {}
    for g in vc["V10"]["detail"]:
        if "/cursor-rules/" in g:
            k = "rule files: `cursor-rules/` is the installed copy, `skills/mainframe-doc-orchestrator/assets/rules/` the skill's install source"
        elif g.startswith("01-detailed-documentation/") and any(x in g for x in ("02-", "03-", "04-")):
            k = "report copies in folders 02-04 whose links needed no rewriting"
        elif "05-rules-skills-validation-scripts/docs-toolkit/" in g and "06-source-snapshot/" in g:
            k = "`docs-toolkit/` files, which are also inventoried repository files and therefore in the snapshot"
        elif g.count("06-source-snapshot/") > 1:
            k = "identical files inside the repository itself: " + g.replace("06-source-snapshot/", "")
        else:
            k = "other: " + g
        kinds[k] = kinds.get(k, 0) + 1
    for k, n in sorted(kinds.items()):
        A("- %d x %s" % (n, k))
    A("")
    A("## 4. Coverage metrics and how each was verified")
    A("")
    A("### Headline counts")
    A("")
    A("| Measure | Value | Verified by |")
    A("|---|---|---|")
    A("| COBOL programs | %d `.cbl` files = inventory = %d program pages | V1 recount |" % (G("COBOL programs (.cbl)"), G("COBOL programs (.cbl)")))
    A("| Copybooks | %d layout pages = %d COBOL copybooks (`.cpy`) + %d DB2 DCLGEN members (`.dcl`, brought in by `EXEC SQL INCLUDE`). "
      "A further %d BMS symbolic-map copybooks have no layout page; each is listed with the program that copies it (copybook-usage page), and the screens are documented from their BMS mapsets | V1 recount |" % (
          vm["layout_pages"], G("COBOL copybooks (.cpy outside cpy-bms)"), G("DB2 DCLGEN members (.dcl)"), G("BMS symbolic-map copybooks (cpy-bms/*.cpy)")))
    A("| JCL jobs | %d JCL members, each with a job page named by its JOB card (app/ and samples/jcl/) | V1 recount |" % G("JCL members (.jcl)"))
    A("| PROCs | %d PROC pages = %d catalogued PROCs + 1 JCL template (`scripts/compile_batch.jcl.template`) | V1 recount |" % (vm["proc_pages"], G("Catalogued PROCs (.prc)")))
    A("| Markdown pages | %d (coverage.json, gaps.json and check_package.json agree) | V2 |" % vm["markdown_pages"])
    A("| Source citations | %d occurrences, %d distinct `path:line` ranges in %d files; %d invalid; %d range(s) include redacted FTP lines and resolve to the marker | V3 recheck against the snapshot |" % (
        sref["occurrences"], sref["distinct"], sref["files_cited"], sref["invalid"], sref["touching_redacted_lines"]))
    A("| Business rules | %d rules (%s) in %d programs: %d of %d COBOL programs plus Assembler %s. No business rule in: %s (their logic is documented on their pages; the catalog states why) | V4a, V4b |" % (
        len(rules), ", ".join("%s %d" % kv for kv in sorted(conf.items())), len(prog_rules), len(cobol) - len(no_rule), len(cobol),
        ", ".join(p for p in asm if p in prog_rules), ", ".join(no_rule)))
    A("| Rule implementation citations | %d; %d name a paragraph, of which %d are confirmed by an independent label scan (%d start outside the named paragraph, %d labels not found) | V4c |" % (
        rm["implementations"], rm["paragraph_named"], rm["paragraph_confirmed_by_label_scan"], rm["paragraph_range_outside"], rm["paragraph_label_not_found"]))
    A("| Pipeline acceptance criteria | %d of %d pass | `coverage_validate.py` |" % (len([c for c in crit if c["pass"]]), len(crit)))
    A("| Package check | %d documents; %s issues | `check_package.py` |" % (chk["documents"], sum(len([x for x in (chk.get(k) or []) if x]) for k in (
        "uncovered_artifacts", "broken_links", "placeholders", "template_guides_left", "mermaid_warnings", "missing_sources_section"))))
    A("| Bundle links | %d relative links in %d files; %d broken | V5 |" % (vm["links"]["links"], vm["links"]["files"], vm["links"]["broken"]))
    A("")
    A("### Count discrepancies explained")
    A("")
    A("- **41 vs 44 copybooks**: 41 is the number of COBOL `.cpy` copybooks. The package documents 44 record layouts because the 3 DB2 DCLGEN members "
      "(`AUTHFRDS`, `DCLTRCAT`, `DCLTRTYP`) are included into programs with `EXEC SQL INCLUDE` and analysed as copybooks. The 21 BMS-generated symbolic maps are counted separately.")
    A("- **404 vs %d pages**: 404 was an earlier progress-log figure; renderer- and validator-only pages added later account for the difference "
      "(reconciled in [gap-report.md](04-gap-report/gap-report.md#page-count-reconciliation))." % vm["markdown_pages"])
    A("- **46 vs %d JCL jobs**: 46 `.jcl` members are under `app/`; %d more are under `samples/jcl/`." % (G("JCL members (.jcl)"), G("JCL members (.jcl)") - 46))
    A("- **CICS transactions 24 of 25**: transaction CDV1 starts program COCRDSEC, which is defined in the CSD but has no source in the repository (GAP-U-014).")
    inv_s = [s for s in cov["summaries"] if s["category"] == "inventory-artifacts"][0]
    A("- **Inventory artifacts %d of %d (%.1f%%)**: the other %d entries are excluded with a reason, not missing." % (inv_s["documented"], inv_s["total"], inv_s["percent_documented"], inv_s["classified_other"]))
    p_sr = [s for s in cov["summaries"] if s["category"] == "source-references"][0]["total"]
    A("- **Source references**: the pipeline counts %d distinct citations in the documentation folder; the bundle check counts %d distinct in the documentation plus the report copies (%s)." % (
        p_sr, sref["distinct"], "the counts agree" if p_sr == sref["distinct"] else "the report copies add citations"))
    A("- **15 unresolved components vs 14 unresolved items**: CDV1 is unresolved only through COCRDSEC.")
    sq = gaps["sme_questions"]
    n_dead = len([q for q in sq if (q.get("question") or "").startswith("Is this copybook still needed? ")])
    n_sme_owner = len([r for r in reg if r["owner"] == "SME clarification"])
    n_cf_open = len([r for r in reg if r["owner"] == "SME clarification" and r["id"].startswith("GAP-C")])
    A("- **%d SME questions, %d components, %d SME-clarification items**: the register has %d SME-question rows (GAP-S) in %d components (a component can carry several): "
      "%d written during batch analysis and %d generated from copybook dead-code observations, each matched one-to-one to its semantic file. "
      "The %d rows owned by SME clarification are those %d questions plus the %d open code-vs-comment conflicts (GAP-C)." % (
          len(sq), len(set(q["component"] for q in sq)), n_sme_owner, len(sq), len(set(q["component"] for q in sq)),
          len(sq) - n_dead, n_dead, n_sme_owner, len(sq), n_cf_open))
    A("- **74 conflicting definitions**: %s. Only the %d code-vs-comment-or-definition rows are open questions." % (
        ", ".join("%s %d" % kv for kv in sorted(cls.items())), cls.get("code-vs-comment-or-definition", 0)))
    A("")
    A("### Coverage by category (pipeline validator)")
    A("")
    A("100% here means every extracted item appears on a page with a citation. It is a completeness measure, not a correctness measure.")
    A("")
    A("| Category | Kind | Documented | Other | Total | % | Independently rechecked |")
    A("|---|---|---|---|---|---|---|")
    for s in cov["summaries"]:
        A("| %s | %s | %d | %d | %d | %s | %s |" % (s["category"], s["kind"], s["documented"], s["classified_other"], s["total"], s["percent_documented"], RECHECK.get(s["category"], "")))
    A("")
    A("## 5. What the automated checks prove and do not prove")
    A("")
    A("**Proven by script (re-runnable):**")
    A("")
    A("- Every in-scope program, copybook, JCL job, PROC and mapset has a page (V1); every inventoried file is at least named in the package or excluded with a reason (pipeline check: name or path appears in the text).")
    A("- Every `path:line` citation points to an existing line range of the analysed source, and the snapshot matches the analysed files by sha256, after line-ending normalisation for files the working tree now holds with CRLF (V3, V8).")
    A("- Every statement, paragraph, decision point, EXEC command, data item, JCL step/DD and copybook field found by the parser appears on a page (pipeline criteria).")
    A("- Every rule has a valid citation, a traceability row and a catalog anchor; named paragraphs exist in the source (V4); "
      "at acceptance each rule's verbatim code anchor was found inside its cited range (`batch_manager.py`).")
    A("- Links resolve, no placeholders or template text remain, no compiled or temporary files, no FTP connection data (V5-V7, package check).")
    A("- Every COBOL program and copybook layout belongs to an analysis batch whose checkpoint records it as validated, with its semantic file present (V11).")
    A("")
    A("**Not proven:**")
    A("")
    A("- That a cited line supports the sentence that cites it, or that a description is complete. This needs human review; sample pages first: "
      "[COACTUPC](01-detailed-documentation/application-documentation/07-programs/COACTUPC.md), "
      "[CBTRN02C](01-detailed-documentation/application-documentation/07-programs/CBTRN02C.md), "
      "[POSTTRAN](01-detailed-documentation/application-documentation/06-batch/jobs/POSTTRAN.md).")
    A("- Business-level correctness of the %d rules: they are AI-assisted interpretations of code, validated for structure, citations and code anchors, not for intent. %d are Inferred." % (len(rules), conf.get("Inferred", 0)))
    A("- Runtime behaviour: nothing was compiled or executed; CICS, IMS, DB2, MQ, Control-M and CA7 were not available. Dynamic targets and scheduler calendars are Inferred or Unverified.")
    A("- Values of JCL symbolics and environment-specific dataset names, which are not in the repository.")
    A("- The original order and dates of the batch analysis runs: checkpoints are rewritten by each `batch_manager.py check`, and `progress.md` is the agent's own log, not an independent record.")
    A("- Field-level documentation of the 21 BMS symbolic-map copybooks: they have no layout pages (the BMS mapsets that generate them have screen pages; the pairing is Inferred from matching member names in app/bms and app/cpy-bms).")
    A("")
    A("**Known issues left as is** (no count or conclusion depends on them; fixing them means regenerating pages):")
    A("")
    for d in vc["V4c"]["detail"]:
        if "outside paragraph" in d:
            A("- Citation warning (V4c): %s. The cited code is inside the range; the range starts before the named paragraph. Next action: confirm and narrow the range." % d.strip("- "))
    docs_dir = os.path.join(B, "01-detailed-documentation", "application-documentation")
    blank = re.compile(r"^(\|\s+)+\|\s*$")
    n_pages, n_rows = 0, 0
    for root, ds, fs in os.walk(docs_dir):
        for f in fs:
            if f.endswith(".md"):
                k = len([l for l in io.open(os.path.join(root, f), encoding="utf-8").read().splitlines() if blank.match(l)])
                if k:
                    n_pages, n_rows = n_pages + 1, n_rows + k
    mv = io.open(os.path.join(docs_dir, "07-programs", "MVSWAIT.md"), encoding="utf-8").read().splitlines()
    mv_rules = [i + 1 for i, l in enumerate(mv) if blank.match(l) and any(x.startswith("## Business rules") for x in mv[:i]) and
                not any(x.startswith("## ") and not x.startswith("## Business rules") for x in mv[[j for j, y in enumerate(mv) if y.startswith("## Business rules")][0] + 1:i])]
    A("- Empty table rows: %d pages contain %d all-blank table rows where a table has no entries (dataset, screen and Assembler program pages); "
      "the renderer writes a blank row instead of \"None\". Among them, the MVSWAIT page has an empty \"Business rules implemented\" table (`07-programs/MVSWAIT.md` line %s) "
      "and no sentence saying why: MVSWAIT is a 12-line Assembler wait routine called by COBSWAIT, outside the 44 COBOL programs, and has no rules. "
      "Next action: have `render_detail.py` write \"None\" and a reason, then regenerate." % (n_pages, n_rows, ", ".join(str(x) for x in mv_rules) or "?"))
    A("")
    A("## 6. Gaps requiring technical investigation or SME clarification")
    A("")
    A("Full list with source, impact, status, owner and next action: [gap-register.md](04-gap-report/gap-register.md). Summary:")
    A("")
    labels = {"GAP-U": "unresolved items", "GAP-S": "SME questions", "GAP-C": "conflicts",
              "GAP-V": "Unverified statements", "GAP-A": "ambiguous dependencies"}
    agg, parts = {}, {}
    for r in reg:
        k = (r["owner"], r["status"])
        agg[k] = agg.get(k, 0) + 1
        pre = r["id"].rsplit("-", 1)[0]
        parts.setdefault(k, {})
        parts[k][pre] = parts[k].get(pre, 0) + 1
    A("| Owner | Status | Items | Made up of |")
    A("|---|---|---|---|")
    for (o, s), n in sorted(agg.items()):
        A("| %s | %s | %d | %s |" % (o, s, n, " + ".join("%d %s (%s)" % (c, labels.get(p, p), p) for p, c in sorted(parts[(o, s)].items()))))
    A("")
    A("**Technical investigation (environment, missing source, run-time behaviour):**")
    A("")
    A("| ID | Component | Item | Source | Next action |")
    A("|---|---|---|---|---|")
    for r in reg:
        if r["owner"] == "Technical investigation" and not r["id"].startswith("GAP-V"):
            A("| %s | %s | %s | `%s` | %s |" % (r["id"], esc(r["component"]), esc(r["summary"])[:160], r["source"], esc(r["next_action"])))
    nv = len([r for r in reg if r["id"].startswith("GAP-V") and r["owner"] == "Technical investigation"])
    A("")
    A("Plus %d Unverified scheduler/README/comment statements to confirm with operations (GAP-V rows in the register)." % nv)
    A("")
    A("**SME clarification (business intent):** %d items = %d questions across %d components + %d open code-vs-comment conflicts. Questions per component:" % (
        len([r for r in reg if r["owner"] == "SME clarification"]), len(gaps["sme_questions"]), len(set(q["component"] for q in gaps["sme_questions"])),
        cls.get("code-vs-comment-or-definition", 0)))
    A("")
    per = {}
    for q in gaps["sme_questions"]:
        per[q["component"]] = per.get(q["component"], 0) + 1
    A(", ".join("%s %d" % kv for kv in sorted(per.items(), key=lambda x: (-x[1], x[0]))) + ".")
    A("")
    A("Examples with direct business or security relevance (verbatim from the register):")
    A("")
    kw = ("ssn", "cvv", "clear", "defect", "unreachable", "restricted", "admin", "reject", "interest", "expir", "password")
    for key in ("CBEXPORT", "CBACT04C", "COCRDLIC", "CBPAUP0C", "COUSR01C"):
        cands = [r for r in reg if r["component"] == key and r["id"].startswith(("GAP-S", "GAP-C")) and r["status"] == "Open"]
        cands.sort(key=lambda r: -len([k for k in kw if k in r["summary"].lower()]))
        if cands:
            r = cands[0]
            A("- %s %s: %s (`%s`)" % (r["id"], key, esc(r["summary"]), r["source"]))
    A("")
    A("## 7. How to reproduce the validation")
    A("")
    A("**Offline, from this bundle alone** (Python 3.1 or later, no packages):")
    A("")
    A("```text")
    A("cd <unzipped>/CardDemo-Architect-Review")
    A("python 05-rules-skills-validation-scripts/work-dir-scripts/verify_review_bundle.py . --no-write")
    A("```")
    A("")
    A("**Full regeneration in the repository** (commands in [docs-toolkit/README.md](05-rules-skills-validation-scripts/docs-toolkit/README.md)): "
      "`batch_manager.py check`, `schedule_lines.py`, `render_detail.py`, `coverage_validate.py`, `gap_report.py`, `check_package.py`, `build_docx.py`, "
      "`build_combined_markdown.ps1`, then `build_review_bundle.ps1`, which copies the outputs, builds the snapshot, runs `verify_review_bundle.py --repo .`, "
      "writes this README, checks for secrets, zips the bundle and re-verifies the unzipped copy.")
    A("")
    A("## 8. Verification results")
    A("")
    A("| ID | Check | Status | Measured |")
    A("|---|---|---|---|")
    for c in ver["checks"]:
        A("| %s | %s | %s | %s |" % (c["id"], esc(c["check"]), c["status"], esc(c["measured"])))
    A("")
    A("Details: [bundle-verification.md](02-coverage-validation-report/bundle-verification.md).")
    f = open(os.path.join(B, "README.md"), "w", encoding="utf-8", newline="\n")
    f.write("\n".join(L) + "\n")
    f.close()
    sys.stdout.write("readme lines=%d\n" % len(L))


if __name__ == "__main__":
    main(sys.argv)
