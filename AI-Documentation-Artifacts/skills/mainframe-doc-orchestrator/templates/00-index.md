# {{application_name}} - Application Documentation

<!-- guide: Package root. Keep this structure; per-artifact folders get one file per inventory item. Remove sections only for technologies proven absent, and say so in the "Scope" table. -->

| Item | Value |
|---|---|
| Application | {{application_name}} |
| Repository | {{repo_root}} |
| Inventory snapshot | {{inventory_generated_at}} ({{file_count}} files) |
| Documentation generated | {{generation_date}} |
| Toolkit | mainframe-doc-orchestrator |

## How to read this package

{{reading_guide}}
<!-- guide: 3-5 sentences: start with 01 (business view), 02 (architecture), then drill into 05/06/07/08. Explain confidence tags Confirmed / Inferred / Unverified. -->

## Scope

| Technology | Present | Evidence |
|---|---|---|
{{technology_scope_rows}}
<!-- guide: One row per technology from discovery (CICS, BMS, VSAM, GDG, DB2, IMS DB, IMS DC, MQ, Assembler, schedulers, FTP, ...). Present = Yes/No. -->

## Contents

| # | Document | Purpose |
|---|---|---|
| 01 | [Executive summary](01-executive-summary.md) | Business purpose, capabilities, key facts |
| 02 | [System context and architecture](02-system-context-architecture.md) | Context, layers, modules, main flows |
| 03 | [Technology stack](03-technology-stack.md) | Languages, middleware, utilities, versions |
| 04 | [Component inventory](04-component-inventory.md) | Every artifact by type and module |
| 05 | [Online](05-online/transaction-catalog.md) | Transactions, screens, navigation, COMMAREA |
| 06 | [Batch](06-batch/job-catalog.md) | Jobs, steps, schedule, data flow |
| 07 | [Programs](07-programs/index.md) | One specification per program |
| 08 | [Data](08-data/data-model.md) | Entities, datasets, layouts, DB2, IMS, MQ, CRUD |
| 09 | [Business rules](09-business-rules-catalog.md) | Rule catalog with traceability |
| 10 | [Integration interfaces](10-integration-interfaces.md) | MQ, IMS, DB2, file transfer, job submission |
| 11 | [Security and access](11-security-access.md) | Users, roles, platform security |
| 12 | [Error handling and messages](12-error-handling-messages.md) | Messages, codes, abends |
| 13 | [Build, deploy and operations](13-build-deploy-operations.md) | Build chains, setup, run book |
| 14 | [Cross-reference and traceability](14-cross-reference-traceability.md) | Matrices |
| 15 | [Glossary](15-glossary.md) | Business and technical terms |
| 16 | [Gaps, assumptions, open questions](16-gaps-assumptions-open-questions.md) | Unknowns, conflicts, QA results |

## Package layout

```
00-index.md ... 16-*.md
05-online/   transaction-catalog.md, navigation-flow.md, commarea-contract.md, screens/<MAPSET>.md
06-batch/    job-catalog.md, batch-schedule-flow.md, jobs/<JOBNAME>.md
07-programs/ index.md, <PROGRAM>.md
08-data/     data-model.md, crud-matrix.md, datasets/<NAME>.md, layouts/<COPYBOOK>.md,
             db2/<TABLE>.md, ims/<DBD>.md, mq/<INTERFACE>.md
```

## Sources

- `{{work_dir}}/inventory.json`
