# Documentation Toolkit

This folder configures the mainframe reverse-engineering documentation
pipeline for this repository. The pipeline itself is generic and lives in the
personal Cursor skills (`mainframe-doc-orchestrator` and related skills). This
repository contributes only:

| Item | Purpose |
|---|---|
| `docs-toolkit/project-profile.yaml` | Repo-specific facts: modules, source roots, excludes, placeholders, output paths, with evidence |
| `.cursor/rules/*.mdc` | Generic reading and documentation rules, installed from the orchestrator skill |

The pipeline writes facts to `docs/_work/` and the published package to
`docs/application-documentation/`. Both folders are excluded from discovery.

## Running the pipeline

Ask the agent to "document this mainframe application using the
mainframe-doc-orchestrator skill". It follows the phases below and tracks
progress in `docs/_work/progress.md`.

| Phase | Skill | Output |
|---|---|---|
| A1 Inventory | mainframe-inventory-discovery | `docs/_work/inventory.json`, `references.json` |
| A2 Programs | cobol-program-analysis | `docs/_work/programs/*.json` |
| A3 Online | cics-online-analysis | `docs/_work/online/*` |
| A4 Batch | batch-jcl-analysis | `docs/_work/jobs/*`, `batch/*` |
| A5 Data | mainframe-data-model-analysis | `docs/_work/datasets/*`, `layouts/*` |
| A6 Integration | mainframe-integration-analysis | `docs/_work/integration/*` |
| A7 Rules | business-rules-extraction | `docs/_work/rules/*` |
| A8 Ops/security | build-deploy-security-analysis | `docs/_work/ops/*` |
| A9 Cross-reference | mainframe-doc-orchestrator | `docs/_work/xref/*` |
| S1 Structure | mainframe-doc-orchestrator (`extract_structure.py`) | `docs/_work/structure/**` |
| S2-S4 Batched semantics | mainframe-doc-orchestrator (`batch_manager.py`, `batch-analysis.md`) | `docs/_work/batches/**`, `docs/_work/semantic/**` |
| B Assembly + QA | mainframe-doc-assembly-qa | `docs/application-documentation/**` |
| B Detail, coverage, gaps | mainframe-doc-orchestrator (`render_detail.py`, `coverage_validate.py`, `gap_report.py`) | detailed pages, `18-coverage/**`, `docs/_work/coverage/**` |

### Phase S and validation commands for this repo

Run from the repository root in PowerShell. `$S` is the orchestrator
`scripts` folder.

```powershell
$env:PYTHONIOENCODING = 'utf-8'
$S = "$env:LOCALAPPDATA\Cursor\AgentStores\cursor_agent_stores\t32020737-u455266838\files\skills\mainframe-doc-orchestrator\scripts"
python "$S\extract_structure.py" docs/_work/inventory.json docs/_work
python "$S\batch_manager.py" init docs/_work --budget 4500     # only for a new plan
python "$S\batch_manager.py" worksheets docs/_work all
python "$S\batch_manager.py" status docs/_work                  # resume point
python "$S\batch_manager.py" check docs/_work all               # after batches; updates manifest; also runs check-reviews
python "$S\batch_manager.py" check-reviews docs/_work           # legacy rules of non-COBOL members (semantic/reviews/)
python "$S\schedule_lines.py" docs/_work                       # Control-M OUTCOND/INCOND/JOB line numbers
python "$S\render_detail.py" docs/_work docs/application-documentation
python "$S\coverage_validate.py" docs/_work docs/application-documentation
python "$S\gap_report.py" docs/_work docs/application-documentation --claimed-pages 404
$Q = "$S\..\..\mainframe-doc-assembly-qa\scripts"
python "$Q\check_package.py" docs/_work/inventory.json docs/application-documentation --json docs/_work/coverage/check_package.json
python "$Q\build_docx.py" docs/application-documentation docs/application-documentation/CardDemo-complete-documentation.docx --title "CardDemo application documentation (complete)"
powershell -File docs/_work/build_combined_markdown.ps1          # COMBINED_DOCUMENTATION.md (skills, rules, all pages)
powershell -File docs/_work/build_review_bundle.ps1              # CardDemo-Architect-Review/ + .zip (five review deliverables)
```

`build_review_bundle.ps1` copies the validated package into five folders
(detailed documentation, coverage validation, business rules and
traceability, gap report, rules/skills/scripts), then:

- `prepare_review_bundle.py` adds `06-source-snapshot/` (in-scope source,
  FTP connection lines of `app/jcl/FTPJCL.JCL` redacted in place), points the
  report copies' links into folder 01 and removes compiled files;
- `verify_review_bundle.py --repo .` runs ten independent checks (source
  recount by extension and JOB card, page counts, every citation against the
  snapshot, rule paragraphs by Area A label scan, links and anchors, hygiene,
  secrets including the DOCX, snapshot sha256, report consistency, duplicates);
- `write_review_readme.py` writes the architect README from the JSON reports;
- `check_instream_secrets.py` stops the build if FTP connection data appears;
- the ZIP is unzipped to a temporary folder and verified again offline.

`gap_report.py` runs twice in the chain above when the gap register page is
new, so that `coverage_validate.py` also checks the register's citations:
`coverage_validate.py`, `gap_report.py`, `coverage_validate.py`, `gap_report.py`.

`build_docx.py` writes every page of the package into one Word file; the
older `PROJECT_DOCUMENTATION.docx` at the repository root is a summary from
13 October 2026 and does not contain the detailed pages.

`init` replaces the batch plan. Do not run it on a work folder whose
batches are in progress; use `status` and `next` to resume instead.

### Discovery commands for this repo

`<skills>` is the personal skills folder that contains the toolkit skills.
The scripts need only Python 3.1 or later, with no extra packages.

```bash
python <skills>/mainframe-inventory-discovery/scripts/classify_inventory.py . \
    --out docs/_work/inventory.json \
    --exclude "**/*.zip" \
    --exclude ".mfdoc-tmp/**" \
    --exclude "docs/_work/**" \
    --exclude "docs/application-documentation/**" \
    --module base=app/** \
    --module auth=app/app-authorization-ims-db2-mq/** \
    --module trantype=app/app-transaction-type-db2/** \
    --module vsammq=app/app-vsam-mq/** \
    --module "build={samples,scripts}/**"

python <skills>/mainframe-inventory-discovery/scripts/scan_references.py \
    docs/_work/inventory.json --out docs/_work/references.json
```

## Using the toolkit on another repository

1. Follow `mainframe-doc-orchestrator/bootstrap.md`: copy the rules into
   `.cursor/rules/` and create `docs-toolkit/project-profile.yaml` from the
   profile template.
2. Fill the profile from evidence in that repository only.
3. If discovery reports unclassified files, extend
   `mainframe-inventory-discovery/scripts/signatures.json` instead of
   special-casing the repo.

## Snapshot of this repository (at toolkit setup)

The default signatures leave no file unclassified. Module split: base 169,
auth 40, trantype 27, vsammq 4, build 71, plus root-level docs and diagrams.
Counts by type:
44 COBOL programs, 41 copybooks, 21 BMS mapsets, 21 BMS symbolic maps,
3 DCLGENs, 4 CSD files, 55 JCL jobs, 6 PROCs, 1 JCL template, 7 control-card
members, 7 DDL members, 4 DBDs, 4 PSBs, 2 Assembler programs, 1 Assembler
macro, 1 Assembler copy member, 1 LISTCAT report, 2 scheduler exports, and
10 scripts, plus data, docs and diagrams. These counts are a baseline;
re-run discovery before generating the documentation.
