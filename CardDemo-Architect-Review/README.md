# CardDemo documentation - architect review bundle

Built by `docs/_work/build_review_bundle.ps1` from repository commit `a1cd6de`. Validation data generated 2026-10-20T03:47:19 (`coverage.json`).
Everything here is a copy of validated pipeline output; no application source was changed. All metrics below are read from the JSON files in this bundle, not typed by hand.

## Contents

| Folder | What it answers | Start with |
|---|---|---|
| `01-detailed-documentation/` | Full detailed documentation: one page per program, copybook, job, proc, screen, dataset, table, IMS database, plus the reading copy and Word file | `application-documentation/README.md` or `COMBINED_DOCUMENTATION.md` |
| `02-coverage-validation-report/` | Coverage of every in-scope COBOL program, copybook, JCL job and proc, CICS resource, dataset and other inventoried component; 33 measured acceptance criteria | `coverage-report.md` |
| `03-business-rules-and-traceability/` | Every business rule mapped to program, paragraph, source lines, CICS transactions and JCL steps; online and batch technical flows; call, copy, data and scheduler dependencies | `14-cross-reference-traceability.md`, then `09-business-rules-catalog.md` |
| `04-gap-report/` | Missing, partially analysed, unresolved, Unverified and SME-dependent items, conflicts and exclusions | `gap-report.md` |
| `05-rules-skills-validation-scripts/` | The Cursor rules, skills, scripts and project profile that produce and validate the package, so the run can be repeated | `docs-toolkit/README.md`, `skills/mainframe-doc-orchestrator/SKILL.md` |

Pages in folders 02 to 04 are copies of pages in `01-detailed-documentation/application-documentation/`. Their links to other pages (for example `07-programs/...`) resolve only inside that folder, so follow links from there.

## Headline results

| Measure | Value |
|---|---|
| Acceptance criteria passed (`coverage_validate.py`) | 33 of 33 |
| Markdown pages in the package | 419 (earlier progress log claimed 404; reconciled in `04-gap-report/gap-report.md`) |
| Package check (`check_package.py`) | 419 documents, 0 issues (uncovered artifacts, broken links, placeholders, template guides, Mermaid warnings, missing Sources sections) |
| Source references (`path:line`) checked against the files | 15808 of 15808 valid |
| Business rules | 392 rules in 40 programs: 39 of 44 COBOL programs plus Assembler COBDATFT. COBOL programs with no business rule (logic documented on their pages, reason in the rules catalog): CBACT02C, CBACT03C, CBCUS01C, CBSTM03B, COBSWAIT |
| Rules by confidence | Confirmed 388, Inferred 4 |
| Rules by category | authorization 1, calculation 23, data-integrity 13, decision 107, error-policy 69, routing 49, security 1, temporal 1, transformation 36, validation 92 |
| Components classified in gap report | 361: documented 298, requires SME clarification 48, unresolved 15 |
| Open items | 120 SME questions, 72 Unverified statements, 14 unresolved items, 74 conflicts, 10 ambiguous dependencies |
| Excluded paths (with reasons) | 55 |

## Coverage by category

From `02-coverage-validation-report/coverage.json`. "Other" counts items deliberately classified outside the category (for example excluded or non-application files); they are listed in the coverage report.

| Category | Kind | Documented | Partial | Missing | Other | Total | % documented |
|---|---|---|---|---|---|---|---|
| programs | structural+semantic | 44 | 0 | 0 | 0 | 44 | 100.0 |
| paragraphs-structural | structural | 881 | 0 | 0 | 0 | 881 | 100.0 |
| paragraphs-semantic | semantic | 881 | 0 | 0 | 0 | 881 | 100.0 |
| paragraph-logic-grounding | semantic | 881 | 0 | 0 | 0 | 881 | 100.0 |
| procedure-statements | structural | 10152 | 0 | 0 | 0 | 10152 | 100.0 |
| unclassified-statements | structural | 0 | 0 | 0 | 0 | 0 | 100.0 |
| decision-points-all | structural | 2230 | 0 | 0 | 0 | 2230 | 100.0 |
| exec-commands | structural | 286 | 0 | 0 | 0 | 286 | 100.0 |
| call-statements | structural | 62 | 0 | 0 | 0 | 62 | 100.0 |
| file-selects | structural | 54 | 0 | 0 | 0 | 54 | 100.0 |
| program-data-items | structural | 2327 | 0 | 0 | 0 | 2327 | 100.0 |
| decision-points | semantic | 1242 | 0 | 0 | 0 | 1242 | 100.0 |
| program-rule-analysis | semantic | 44 | 0 | 0 | 0 | 44 | 100.0 |
| copybooks | structural+semantic | 44 | 0 | 0 | 0 | 44 | 100.0 |
| copybook-fields | structural | 559 | 0 | 0 | 0 | 559 | 100.0 |
| copybook-88-levels | structural | 70 | 0 | 0 | 0 | 70 | 100.0 |
| copybook-paragraphs | structural | 20 | 0 | 0 | 0 | 20 | 100.0 |
| copy-edges | dependency | 366 | 0 | 0 | 0 | 366 | 100.0 |
| jcl-jobs | structural | 55 | 0 | 0 | 0 | 55 | 100.0 |
| jcl-procs | structural | 7 | 0 | 0 | 0 | 7 | 100.0 |
| jcl-steps | structural | 163 | 0 | 0 | 0 | 163 | 100.0 |
| jcl-dds | structural | 792 | 0 | 0 | 0 | 792 | 100.0 |
| jcl-conditions | structural | 30 | 0 | 0 | 0 | 30 | 100.0 |
| cics-transactions | structural | 24 | 0 | 0 | 1 | 25 | 96.0 |
| cics-resources | structural | 89 | 0 | 0 | 0 | 89 | 100.0 |
| data-definitions | structural | 22 | 0 | 0 | 0 | 22 | 100.0 |
| datasets | structural | 149 | 0 | 0 | 0 | 149 | 100.0 |
| dependencies | dependency | 175 | 0 | 0 | 0 | 175 | 100.0 |
| rule-traceability | traceability | 392 | 0 | 0 | 0 | 392 | 100.0 |
| scheduler-edges | dependency | 81 | 0 | 0 | 0 | 81 | 100.0 |
| dataflow-edges | dependency | 243 | 0 | 0 | 0 | 243 | 100.0 |
| inventory-artifacts | structural | 276 | 0 | 0 | 55 | 331 | 83.4 |
| source-references | traceability | 15808 | 0 | 0 | 0 | 15808 | 100.0 |

## What these numbers do not claim

- 100% in a structural category means every item was extracted and appears on a page with a source citation. It does not mean every behaviour is semantically confirmed.
- 48 components are classified "requires SME clarification" and 15 "unresolved"; the reasons and questions are in `04-gap-report/gap-report.md`.
- 72 statements rest only on comments, READMEs or unresolved symbolics and are tagged Unverified (gap report, section "Unverified statements").
- Placeholders and symbolics (`&HLQ`, `&SYSUID`, schema names) are documented as parameters; no values were invented.
- The FTP host and login values in `app/jcl/FTPJCL.JCL` are not reproduced anywhere in this bundle (checked by `check_instream_secrets.py`, result below).
- `AI-Documentation-Artifacts/` and `AI-Documentation-Artifacts.zip` in the repository root are an older snapshot (2026-10-15) and are superseded by this bundle.

## Repeating the run

The full command sequence is in `05-rules-skills-validation-scripts/docs-toolkit/README.md`. In short, with the skills installed under the Cursor user store and `$env:PYTHONIOENCODING='utf-8'`:

```powershell
$S = "<skills>\mainframe-doc-orchestrator\scripts"; $Q = "<skills>\mainframe-doc-assembly-qa\scripts"
python "$S\batch_manager.py" check docs/_work all
python "$S\schedule_lines.py" docs/_work
python "$S\render_detail.py" docs/_work docs/application-documentation
python "$S\coverage_validate.py" docs/_work docs/application-documentation
python "$S\gap_report.py" docs/_work docs/application-documentation --claimed-pages 404
python "$Q\check_package.py" docs/_work/inventory.json docs/application-documentation --json docs/_work/coverage/check_package.json
python "$Q\build_docx.py" docs/application-documentation docs/application-documentation/CardDemo-complete-documentation.docx --title "CardDemo application documentation (complete)"
powershell -NoProfile -File docs/_work/build_combined_markdown.ps1
powershell -NoProfile -File docs/_work/build_review_bundle.ps1
```

Semantic batches resume from `docs/_work/batches/<id>/checkpoint.json`; `docs/_work/progress.md` (copied to `work-dir-scripts/`) records every pass.

## Secrets check

```text
app/jcl/FTPJCL.JCL:33 hits=0
app/jcl/FTPJCL.JCL:34 hits=0
app/jcl/FTPJCL.JCL:35 hits=0
checked_lines=3 files=536 findings=0
```
