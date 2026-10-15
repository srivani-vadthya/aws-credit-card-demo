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
| B Assembly + QA | mainframe-doc-assembly-qa | `docs/application-documentation/**` |

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
