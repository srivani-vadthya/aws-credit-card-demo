# CardDemo legacy documentation POC - architect review package

Repository commit `e27ca5c`; application source in the working tree is not tracked by this git repository (app/, samples/ and scripts/ are untracked), so the commit does not identify it; the analysed version is identified by the inventory sha256 values, which every snapshot file still matches (V8). Documentation, reports and scripts include the uncommitted changes of the final review pass (see CHANGELOG.md). Pipeline validation run 2026-10-20T04:36:27; bundle verification run 2026-10-20T04:49:33 (13 checks, 0 failed, 1 warning(s)).

## 1. What this POC documents

Evidence-based reverse-engineering documentation of the AWS CardDemo mainframe sample application (CICS online, batch JCL, VSAM, IMS, DB2 and MQ extensions, Control-M and CA7 schedules). In scope, recounted from the source snapshot by `verify_review_bundle.py` (check V1):

| Component | Files in source | Documented on own page |
|---|---|---|
| COBOL programs (.cbl) | 44 | all |
| Assembler programs (.asm) | 2 | all |
| COBOL copybooks (.cpy outside cpy-bms) | 41 | all |
| DB2 DCLGEN members (.dcl) | 3 | all |
| BMS mapsets (.bms) | 21 | all |
| BMS symbolic-map copybooks (cpy-bms/*.cpy) | 21 | no page of their own; listed with the copying program on the copybook-usage page |
| JCL members (.jcl) | 55 | all |
| Catalogued PROCs (.prc) | 6 | all |

Also inventoried and documented: CICS CSD resources, IMS DBD/PSB, DB2 DDL, control cards, scheduler definitions and shell scripts (361 components classified in total, see the gap report). 55 inventory entries are excluded with a reason (placeholders, repository metadata, binaries).

## 2. How the documentation was generated

1. **Discovery** (`mainframe-inventory-discovery` skill, `classify_inventory.py`, `scan_references.py`): every file classified with sha256 into `inventory.json`; COPY/INCLUDE/EXEC PGM/PROC references resolved or recorded as external-or-missing.
2. **Structure extraction** (`extract_structure.py`, deterministic parser): divisions, paragraphs, statements, data items, EXEC CICS/SQL/DLI, JCL steps and DDs, CSD resources, copybook fields.
3. **Semantic analysis** (AI-assisted, Claude in Cursor, guided by the rules and skills in folder 05): purpose, paragraph logic, business rules, SME questions, per program/copybook batch. `batch_manager.py` accepts a semantic file only when every parsed paragraph has a logic description, every rule cites an existing line range and a verbatim code anchor found inside that range, a program without rules states why, and the source sha256 still matches; per-batch checkpoints make the run resumable.
4. **Rendering** (`render_detail.py`, deterministic): all detailed pages from structure + validated semantics; `build_docx.py` and `build_combined_markdown.ps1` produce the Word and single-file copies.
5. **Validation**: `coverage_validate.py` (33 measured criteria), `gap_report.py` (component status and gap register), `check_package.py` (links, placeholders, Sources sections), then this bundle's independent `verify_review_bundle.py`.

Rules applied throughout (folder 05, `cursor-rules/mainframe-doc-core.mdc`): every fact cites `path:line`; statements are tagged Confirmed, Inferred or Unverified; code wins over comments; placeholders are never given invented values; application source is never modified.

## 3. Package contents

| Folder | Contents | Start with |
|---|---|---|
| `01-detailed-documentation/` | 420-page Markdown package (one page per program, copybook, job, PROC, screen, dataset, table, IMS database, plus overviews), the same content as one Word file (`application-documentation/CardDemo-complete-documentation.docx`) and as one Markdown file (`COMBINED_DOCUMENTATION.md`, which also embeds the rules, skills and scripts) | [00-index.md](01-detailed-documentation/application-documentation/00-index.md) |
| `02-coverage-validation-report/` | Pipeline coverage report and JSON, package check, inventory, and the independent bundle verification | [bundle-verification.md](02-coverage-validation-report/bundle-verification.md), [coverage-report.md](02-coverage-validation-report/coverage-report.md) |
| `03-business-rules-and-traceability/` | Rule-to-source traceability (program, paragraph, lines, CICS transactions, JCL steps; online and batch flows), rules catalog, dependency pages, rules JSON | [14-cross-reference-traceability.md](03-business-rules-and-traceability/14-cross-reference-traceability.md) |
| `04-gap-report/` | Gap register (one row per item with evidence, source, impact, status, owner, next action), gap report, narrative gaps register, gaps JSON | [gap-register.md](04-gap-report/gap-register.md) |
| `05-rules-skills-validation-scripts/` | Cursor rules, the ten skills with templates and scripts, project profile, bundle and verification scripts, progress log | [docs-toolkit/README.md](05-rules-skills-validation-scripts/docs-toolkit/README.md) |
| `06-source-snapshot/` | Read-only copy of the in-scope source so every citation can be opened offline; FTP connection lines redacted | [REDACTIONS.md](06-source-snapshot/REDACTIONS.md) |
| `CHANGELOG.md` | Changes made in the final review pass | [CHANGELOG.md](CHANGELOG.md) |

Report pages in folders 02-04 are copies of pages in `01-detailed-documentation/application-documentation/`; their links point back into folder 01. Identical files found by V10 (13 groups), all intended:

- 2 x `docs-toolkit/` files, which are also inventoried repository files and therefore in the snapshot
- 1 x identical files inside the repository itself: app/app-transaction-type-db2/ctl/REPROCT.ctl; app/ctl/REPROCT.ctl
- 2 x report copies in folders 02-04 whose links needed no rewriting
- 8 x rule files: `cursor-rules/` is the installed copy, `skills/mainframe-doc-orchestrator/assets/rules/` the skill's install source

## 4. Coverage metrics and how each was verified

### Headline counts

| Measure | Value | Verified by |
|---|---|---|
| COBOL programs | 44 `.cbl` files = inventory = 44 program pages | V1 recount |
| Copybooks | 44 layout pages = 41 COBOL copybooks (`.cpy`) + 3 DB2 DCLGEN members (`.dcl`, brought in by `EXEC SQL INCLUDE`). A further 21 BMS symbolic-map copybooks have no layout page; each is listed with the program that copies it (copybook-usage page), and the screens are documented from their BMS mapsets | V1 recount |
| JCL jobs | 55 JCL members, each with a job page named by its JOB card (app/ and samples/jcl/) | V1 recount |
| PROCs | 7 PROC pages = 6 catalogued PROCs + 1 JCL template (`scripts/compile_batch.jcl.template`) | V1 recount |
| Markdown pages | 420 (coverage.json, gaps.json and check_package.json agree) | V2 |
| Source citations | 28002 occurrences, 15824 distinct `path:line` ranges in 209 files; 0 invalid; 1 range(s) include redacted FTP lines and resolve to the marker | V3 recheck against the snapshot |
| Business rules | 392 rules (Confirmed 388, Inferred 4) in 40 programs: 39 of 44 COBOL programs plus Assembler COBDATFT. No business rule in: CBACT02C, CBACT03C, CBCUS01C, CBSTM03B, COBSWAIT (their logic is documented on their pages; the catalog states why) | V4a, V4b |
| Rule implementation citations | 658; 415 name a paragraph, of which 414 are confirmed by an independent label scan (1 start outside the named paragraph, 0 labels not found) | V4c |
| Pipeline acceptance criteria | 33 of 33 pass | `coverage_validate.py` |
| Package check | 420 documents; 0 issues | `check_package.py` |
| Bundle links | 10343 relative links in 464 files; 0 broken | V5 |

### Count discrepancies explained

- **41 vs 44 copybooks**: 41 is the number of COBOL `.cpy` copybooks. The package documents 44 record layouts because the 3 DB2 DCLGEN members (`AUTHFRDS`, `DCLTRCAT`, `DCLTRTYP`) are included into programs with `EXEC SQL INCLUDE` and analysed as copybooks. The 21 BMS-generated symbolic maps are counted separately.
- **404 vs 420 pages**: 404 was an earlier progress-log figure; renderer- and validator-only pages added later account for the difference (reconciled in [gap-report.md](04-gap-report/gap-report.md#page-count-reconciliation)).
- **46 vs 55 JCL jobs**: 46 `.jcl` members are under `app/`; 9 more are under `samples/jcl/`.
- **CICS transactions 24 of 25**: transaction CDV1 starts program COCRDSEC, which is defined in the CSD but has no source in the repository (GAP-U-014).
- **Inventory artifacts 276 of 331 (83.4%)**: the other 55 entries are excluded with a reason, not missing.
- **Source references**: the pipeline counts 15824 distinct citations in the documentation folder; the bundle check counts 15824 distinct in the documentation plus the report copies (the counts agree).
- **15 unresolved components vs 14 unresolved items**: CDV1 is unresolved only through COCRDSEC. **48 SME components vs 120 SME questions**: a component can carry several questions.
- **74 conflicting definitions**: code-vs-comment-or-definition 18, dd-reuse-across-jobs 26, parser-reconciliation 24, rule-correction 6. Only the 18 code-vs-comment-or-definition rows are open questions.

### Coverage by category (pipeline validator)

100% here means every extracted item appears on a page with a citation. It is a completeness measure, not a correctness measure.

| Category | Kind | Documented | Other | Total | % | Independently rechecked |
|---|---|---|---|---|---|---|
| programs | structural+semantic | 44 | 0 | 44 | 100.0 | V1 |
| paragraphs-structural | structural | 881 | 0 | 881 | 100.0 |  |
| paragraphs-semantic | semantic | 881 | 0 | 881 | 100.0 |  |
| paragraph-logic-grounding | semantic | 881 | 0 | 881 | 100.0 |  |
| procedure-statements | structural | 10152 | 0 | 10152 | 100.0 |  |
| unclassified-statements | structural | 0 | 0 | 0 | 100.0 |  |
| decision-points-all | structural | 2230 | 0 | 2230 | 100.0 |  |
| exec-commands | structural | 286 | 0 | 286 | 100.0 |  |
| call-statements | structural | 62 | 0 | 62 | 100.0 |  |
| file-selects | structural | 54 | 0 | 54 | 100.0 |  |
| program-data-items | structural | 2327 | 0 | 2327 | 100.0 |  |
| decision-points | semantic | 1242 | 0 | 1242 | 100.0 |  |
| program-rule-analysis | semantic | 44 | 0 | 44 | 100.0 |  |
| copybooks | structural+semantic | 44 | 0 | 44 | 100.0 | V1 |
| copybook-fields | structural | 559 | 0 | 559 | 100.0 |  |
| copybook-88-levels | structural | 70 | 0 | 70 | 100.0 |  |
| copybook-paragraphs | structural | 20 | 0 | 20 | 100.0 |  |
| copy-edges | dependency | 366 | 0 | 366 | 100.0 |  |
| jcl-jobs | structural | 55 | 0 | 55 | 100.0 | V1 |
| jcl-procs | structural | 7 | 0 | 7 | 100.0 | V1 |
| jcl-steps | structural | 163 | 0 | 163 | 100.0 |  |
| jcl-dds | structural | 792 | 0 | 792 | 100.0 |  |
| jcl-conditions | structural | 30 | 0 | 30 | 100.0 |  |
| cics-transactions | structural | 24 | 1 | 25 | 96.0 |  |
| cics-resources | structural | 89 | 0 | 89 | 100.0 |  |
| data-definitions | structural | 22 | 0 | 22 | 100.0 |  |
| datasets | structural | 149 | 0 | 149 | 100.0 |  |
| dependencies | dependency | 175 | 0 | 175 | 100.0 |  |
| rule-traceability | traceability | 392 | 0 | 392 | 100.0 | V4a, V4b |
| scheduler-edges | dependency | 81 | 0 | 81 | 100.0 |  |
| dataflow-edges | dependency | 243 | 0 | 243 | 100.0 |  |
| inventory-artifacts | structural | 276 | 55 | 331 | 83.4 |  |
| source-references | traceability | 15824 | 0 | 15824 | 100.0 | V3 |

## 5. What the automated checks prove and do not prove

**Proven by script (re-runnable):**

- Every in-scope program, copybook, JCL job, PROC and mapset has a page (V1); every inventoried file is at least named in the package or excluded with a reason (pipeline check: name or path appears in the text).
- Every `path:line` citation points to an existing line range of the analysed source, and the snapshot matches the analysed files by sha256, after line-ending normalisation for files the working tree now holds with CRLF (V3, V8).
- Every statement, paragraph, decision point, EXEC command, data item, JCL step/DD and copybook field found by the parser appears on a page (pipeline criteria).
- Every rule has a valid citation, a traceability row and a catalog anchor; named paragraphs exist in the source (V4); at acceptance each rule's verbatim code anchor was found inside its cited range (`batch_manager.py`).
- Links resolve, no placeholders or template text remain, no compiled or temporary files, no FTP connection data (V5-V7, package check).

**Not proven:**

- That a cited line supports the sentence that cites it, or that a description is complete. This needs human review; sample pages first: [COACTUPC](01-detailed-documentation/application-documentation/07-programs/COACTUPC.md), [CBTRN02C](01-detailed-documentation/application-documentation/07-programs/CBTRN02C.md), [POSTTRAN](01-detailed-documentation/application-documentation/06-batch/jobs/POSTTRAN.md).
- Business-level correctness of the 392 rules: they are AI-assisted interpretations of code, validated for structure, citations and code anchors, not for intent. 4 are Inferred.
- Runtime behaviour: nothing was compiled or executed; CICS, IMS, DB2, MQ, Control-M and CA7 were not available. Dynamic targets and scheduler calendars are Inferred or Unverified.
- Values of JCL symbolics and environment-specific dataset names, which are not in the repository.
- Field-level documentation of the 21 BMS symbolic-map copybooks: they have no layout pages (the BMS mapsets that generate them have screen pages; the pairing is Inferred from matching member names in app/bms and app/cpy-bms).

## 6. Gaps requiring technical investigation or SME clarification

Full list with source, impact, status, owner and next action: [gap-register.md](04-gap-report/gap-register.md). Summary:

| Owner | Status | Items |
|---|---|---|
| None | Closed (parser output used) | 24 |
| None | Informational | 26 |
| None required | Open (low) | 55 |
| SME clarification | Open | 138 |
| SME review optional | Closed (corrected) | 6 |
| Technical investigation | Open | 41 |

**Technical investigation (environment, missing source, run-time behaviour):**

| ID | Component | Item | Source | Next action |
|---|---|---|---|---|
| GAP-U-001 | CNJBATMP | Symbolic parameters without a value in the repository: &HLQ, &MEMNAME | `samples/jcl/BATCMP.jcl:38` | Obtain the submit-time values (JCL SET, PROC defaults, scheduler variables) from the target environment and re-run dataset lineage |
| GAP-U-002 | BLDCIDB2 | Symbolic parameters without a value in the repository: &COBLIB, &COPYLIB, &CPYBKS, &DBRMLIB, &DCLLIB, &LIBPRFX, &LOADLIB, &MEMNAME, &SDFHCOB, &SDFHLOAD, &SDFHMA | `samples/proc/BLDCIDB2.prc:48` | Obtain the submit-time values (JCL SET, PROC defaults, scheduler variables) from the target environment and re-run dataset lineage |
| GAP-U-003 | CBLDBMS | Symbolic parameters without a value in the repository: &HLQ | `samples/jcl/BMSCMP.jcl:37` | Obtain the submit-time values (JCL SET, PROC defaults, scheduler variables) from the target environment and re-run dataset lineage |
| GAP-U-004 | BUILDBAT | Symbolic parameters without a value in the repository: &COBLIB, &CPYBKS, &LISTING, &LOADLIB, &MEM, &SOURCE | `samples/proc/BUILDBAT.prc:37` | Obtain the submit-time values (JCL SET, PROC defaults, scheduler variables) from the target environment and re-run dataset lineage |
| GAP-U-005 | BUILDBMS | Symbolic parameters without a value in the repository: &CICSMAC, &CPYBKS, &LISTING, &LOADLIB, &MAPNAME, &SRCCODE | `samples/proc/BUILDBMS.prc:42` | Obtain the submit-time values (JCL SET, PROC defaults, scheduler variables) from the target environment and re-run dataset lineage |
| GAP-U-006 | BUILDONL | Symbolic parameters without a value in the repository: &COBLIB, &CPYBKS, &DFHCOB, &DFHLOAD, &DFHSAMP, &LISTING, &LOADLIB, &MEM, &SOURCE | `samples/proc/BUILDONL.prc:41` | Obtain the submit-time values (JCL SET, PROC defaults, scheduler variables) from the target environment and re-run dataset lineage |
| GAP-U-007 | CICCMP | Symbolic parameters without a value in the repository: &HLQ, &MEMNAME | `samples/jcl/CICCMP.jcl:37` | Obtain the submit-time values (JCL SET, PROC defaults, scheduler variables) from the target environment and re-run dataset lineage |
| GAP-U-008 | CIDBCMP | Symbolic parameters without a value in the repository: &HLQ, &MEMNAME, &PLAN, &SSID | `samples/jcl/CICDBCMP.jcl:36` | Obtain the submit-time values (JCL SET, PROC defaults, scheduler variables) from the target environment and re-run dataset lineage |
| GAP-U-009 | COMPILE_BATCH.JCL | Symbolic parameters without a value in the repository: &MEM | `scripts/compile_batch.jcl.template:13` | Obtain the submit-time values (JCL SET, PROC defaults, scheduler variables) from the target environment and re-run dataset lineage |
| GAP-U-010 | CREADB2 | Symbolic parameters without a value in the repository: &DB2S, &LBNM | `app/app-transaction-type-db2/jcl/CREADB21.jcl:32` | Obtain the submit-time values (JCL SET, PROC defaults, scheduler variables) from the target environment and re-run dataset lineage |
| GAP-U-011 | IMSMQCMP | Symbolic parameters without a value in the repository: &CICSHLQ, &HLQ, &IMSHLQ, &MQHLQ | `samples/jcl/IMSMQCMP.jcl:29` | Obtain the submit-time values (JCL SET, PROC defaults, scheduler variables) from the target environment and re-run dataset lineage |
| GAP-U-012 | REPROC | Symbolic parameters without a value in the repository: &CNTLLIB | `app/proc/REPROC.prc:28` | Obtain the submit-time values (JCL SET, PROC defaults, scheduler variables) from the target environment and re-run dataset lineage |
| GAP-U-013 | TRANEXTR | Symbolic parameters without a value in the repository: &HLQ | `app/app-transaction-type-db2/jcl/TRANEXTR.jcl:34` | Obtain the submit-time values (JCL SET, PROC defaults, scheduler variables) from the target environment and re-run dataset lineage |
| GAP-U-014 | COCRDSEC | CICS PROGRAM definition with no source member in the repository | `app/csd/CARDDEMO.CSD:211-218` | Obtain the source or confirm the program is retired |
| GAP-A-001 | COACTUPC | XCTL CDEMO-TO-PROGRAM: target held in a variable; resolved from MOVEs and caller lists (Inferred) | `app/cbl/COACTUPC.cbl:956` | Confirm targets with a CICS trace (for example CEDX or auxiliary trace) or by review of the MOVE paths |
| GAP-A-002 | COACTVWC | XCTL CDEMO-TO-PROGRAM: target held in a variable; resolved from MOVEs and caller lists (Inferred) | `app/cbl/COACTVWC.cbl:349` | Confirm targets with a CICS trace (for example CEDX or auxiliary trace) or by review of the MOVE paths |
| GAP-A-003 | COCRDSLC | XCTL CDEMO-TO-PROGRAM: target held in a variable; resolved from MOVEs and caller lists (Inferred) | `app/cbl/COCRDSLC.cbl:331` | Confirm targets with a CICS trace (for example CEDX or auxiliary trace) or by review of the MOVE paths |
| GAP-A-004 | COCRDUPC | XCTL CDEMO-TO-PROGRAM: target held in a variable; resolved from MOVEs and caller lists (Inferred) | `app/cbl/COCRDUPC.cbl:473` | Confirm targets with a CICS trace (for example CEDX or auxiliary trace) or by review of the MOVE paths |
| GAP-A-005 | COTRTLIC | XCTL CDEMO-TO-PROGRAM: target held in a variable; resolved from MOVEs and caller lists (Inferred) | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:620` | Confirm targets with a CICS trace (for example CEDX or auxiliary trace) or by review of the MOVE paths |
| GAP-A-006 | COTRTUPC | XCTL CDEMO-TO-PROGRAM: target held in a variable; resolved from MOVEs and caller lists (Inferred) | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:457` | Confirm targets with a CICS trace (for example CEDX or auxiliary trace) or by review of the MOVE paths |
| GAP-A-007 | COTRTLIC | CALL-dynamic DSNTIAC: target held in a variable; resolved from MOVEs and caller lists (Inferred) | `app/app-transaction-type-db2/cpy/CSDB2RPY.cpy:57` | Confirm targets with a CICS trace (for example CEDX or auxiliary trace) or by review of the MOVE paths |
| GAP-A-008 | scheduler | CA7 job CLOSEFIL1: scheduler job name has no job card of that name; it names JCL member CLOSEFIL | `app/scheduler/CardDemo.ca7:225` | Confirm the CA7 job-to-member mapping with the scheduler administrators |
| GAP-A-009 | scheduler | CA7 job CLOSEFIL2: scheduler job name has no job card of that name; it names JCL member CLOSEFIL | `app/scheduler/CardDemo.ca7:252` | Confirm the CA7 job-to-member mapping with the scheduler administrators |
| GAP-A-010 | CORPT00C | TD queue JOBS -> internal reader job stream built in program: submitted JCL is assembled at run time | `app/csd/CARDDEMO.CSD:499-503` | Review the job stream the program writes and confirm the internal reader setup in the target region |

Plus 17 Unverified scheduler/README/comment statements to confirm with operations (GAP-V rows in the register).

**SME clarification (business intent):** 120 questions across 48 components, and 18 open code-vs-comment conflicts. Questions per component:

COACTUPC 8, CBTRN02C 5, COTRN02C 5, COTRTLIC 5, COTRTUPC 5, CBTRN03C 4, COACCT01 4, COBIL00C 4, COCRDUPC 4, COPAUA0C 4, CORPT00C 4, CBACT04C 3, CBEXPORT 3, CBPAUP0C 3, CBSTM03A 3, COCRDLIC 3, COCRDSLC 3, CODATE01 3, COTRN00C 3, COUSR02C 3, CBACT01C 2, CBIMPORT 2, CBTRN01C 2, COACTVWC 2, COBTUPDT 2, COMEN01C 2, COPAUS0C 2, COPAUS1C 2, COTRN01C 2, COUSR00C 2, COUSR01C 2, COUSR03C 2, PAUDBLOD 2, CCPAUERY 1, CIPAUDTY 1, CIPAUSMY 1, COADM01C 1, COBSWAIT 1, COMEN02Y 1, COPAUS2C 1, COSGN00C 1, CSMSG01Y 1, CSUSR01Y 1, CSUTLDTC 1, CVCRD01Y 1, DBUNLDGS 1, IMSFUNCS 1, UNUSED1Y 1.

Examples with direct business or security relevance (verbatim from the register):

- GAP-S-008 CBEXPORT: Is exporting SSN and CVV in clear text acceptable for the migration file, or must they be masked/encrypted? (`app/cbl/CBEXPORT.cbl:536-538`)
- GAP-S-003 CBACT04C: The end-of-file branch that would post interest to the last account is unreachable. Is the last account's balance update handled elsewhere, or is this a known defect? (`app/cbl/CBACT04C.cbl:187-222`)
- GAP-S-050 COCRDLIC: Should non-admin users be restricted to the cards of their own account as the program header states? If yes, where should the user's account come from (commarea CDEMO-ACCT-ID is not set by sign-on)? (`app/cbl/COCRDLIC.cbl:4-7`)
- GAP-S-013 CBPAUP0C: How should expiry be computed across year boundaries (YYDDD arithmetic)? (`app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:280-282`)
- GAP-S-101 COUSR01C: Which user type values are valid (only 'A' admin and 'U' regular?) and should COUSR01C reject other values? (`app/cbl/COUSR01C.cbl:142-147`)

## 7. How to reproduce the validation

**Offline, from this bundle alone** (Python 3.1 or later, no packages):

```text
cd <unzipped>/CardDemo-Architect-Review
python 05-rules-skills-validation-scripts/work-dir-scripts/verify_review_bundle.py . --no-write
```

**Full regeneration in the repository** (commands in [docs-toolkit/README.md](05-rules-skills-validation-scripts/docs-toolkit/README.md)): `batch_manager.py check`, `schedule_lines.py`, `render_detail.py`, `coverage_validate.py`, `gap_report.py`, `check_package.py`, `build_docx.py`, `build_combined_markdown.ps1`, then `build_review_bundle.ps1`, which copies the outputs, builds the snapshot, runs `verify_review_bundle.py --repo .`, writes this README, checks for secrets, zips the bundle and re-verifies the unzipped copy.

## 8. Verification results

| ID | Check | Status | Measured |
|---|---|---|---|
| V1 | Source files recounted by extension match the inventory and each has a page | pass | 8 groups checked, 0 mismatched |
| V2 | Markdown page count agrees across the package, coverage.json, gaps.json and check_package.json | pass | 420 pages; coverage.json 420; gaps.json 420; check_package.json 420; other files: CardDemo-complete-documentation.docx |
| V3 | Every `path:line` citation in the documentation and reports resolves to an existing line range in the source snapshot | pass | 28002 occurrences, 15824 distinct, 209 files cited, 0 invalid, 1 touch redacted lines |
| V4a | Every rule implementation cites an existing line range | pass | 658 implementations of 392 rules, 0 invalid |
| V4b | Every rule appears on the traceability page and links to an existing catalog anchor | pass | 392 rules, 392 rows, 0 missing, 0 bad anchors |
| V4c | Named paragraphs exist in the cited source and contain the first cited line (independent Area A label scan) | warn | 415 named: 414 confirmed, 1 start outside the named paragraph, 0 labels not found |
| V4d | Implementations without a named paragraph, by location (informational) | pass | Assembler source 3, PROCEDURE DIVISION, no paragraph named 160, before PROCEDURE DIVISION (data definitions) 55, copybook without PROCEDURE DIVISION (data definitions) 22, non-COBOL source (.ddl) 2, non-COBOL source (.jcl) 1 |
| V5 | Every relative Markdown link and anchor in the bundle resolves inside the bundle (templates excluded) | pass | 464 files, 10343 relative links, 0 broken |
| V6 | No compiled, temporary or empty files | pass | 0 junk, 0 empty |
| V7 | FTP connection lines from app/jcl/FTPJCL.JCL are absent from the bundle (snapshot copy redacted) | pass | 3 connection lines checked in every text file and inside the DOCX; 0 findings; 3 redaction markers in the snapshot copy |
| V8 | Snapshot files match the analysed sources (inventory sha256 and the repository) | pass | 241 files: 14 identical, 226 identical after CRLF->LF normalisation (the working tree was checked out with CRLF after analysis; line numbers are unaffected), 0 mismatches, 0 differ from repository, 1 redacted (expected to differ) |
| V9 | Reports agree with each other (gap counts, register, criteria, package check, rule totals) | pass | 7 cross-checks |
| V10 | Identical files (informational; intended copies are explained in README.md) | pass | 13 groups of identical files |

Details: [bundle-verification.md](02-coverage-validation-report/bundle-verification.md).
