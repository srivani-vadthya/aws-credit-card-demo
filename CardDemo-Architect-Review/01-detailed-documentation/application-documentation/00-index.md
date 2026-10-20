# CardDemo - Application Documentation

| Item | Value |
|---|---|
| Application | CardDemo |
| Repository | aws-mainframe-modernization-carddemo |
| Inventory snapshot | docs/_work/inventory.json (331 files) |
| Documentation generated | 2026-10-11 |
| Toolkit | mainframe-doc-orchestrator |

## How to read this package

Share [CardDemo, end to end](CardDemo-end-to-end.md) when one document has to describe the whole repository. The same guide as a Word file is `CardDemo-end-to-end.docx` in this folder. Start with the executive summary for what the application does, then the architecture page for how online and batch work fit together. Use the transaction, job, program, and data pages for a single artifact. Confirmed means the code or definition states it. Inferred means it was reasoned from several cited facts. Unverified means it comes from a comment, a README, or a diagram.

## Scope

| Technology | Present | Evidence |
|---|---|---|
| Assembler | Yes | Yes. asm-program count 2. |
| BMS | Yes | Yes. bms-mapset count 21. |
| CA7 | Yes | Yes. scheduler-ca7 count 1. |
| CICS | Yes | Yes. CSD members are in the inventory. |
| Control-M | Yes | Yes. scheduler-controlm count 1. |
| DB2 | Yes | Yes. DDL and DCLGEN members are in the inventory. |
| FTP | Yes | Yes. FTPJCLS and the shell submit scripts. |
| GDG | Yes | Yes. DEFGDGB defines generation data groups. |
| IMS DB | Yes | Yes. DBD and PSB members are in the inventory. |
| MQ | Yes | Yes. Queue literals are in the vsammq programs. |
| VSAM | Yes | Yes. Dataset facts include KSDS, ESDS, RRDS, and AIX. |

## Contents

| # | Document | Purpose |
|---|---|---|
|  | [CardDemo, end to end](CardDemo-end-to-end.md) | One document for the full online and batch flow |
| 01 | [Executive summary](01-executive-summary.md) | What the application does |
| 02 | [System context and architecture](02-system-context-architecture.md) | Online, batch, and modules |
| 03 | [Technology stack](03-technology-stack.md) | Languages and middleware found |
| 04 | [Component inventory](04-component-inventory.md) | Every inventoried file |
| 05 | [Online](05-online/transaction-catalog.md) | Transactions, screens, navigation |
| 06 | [Batch](06-batch/job-catalog.md) | Jobs and schedules |
| 07 | [Programs](07-programs/index.md) | One page per program |
| 08 | [Data](08-data/data-model.md) | Datasets, layouts, CRUD |
| 09 | [Business rules](09-business-rules-catalog.md) | Confirmed rules |
| 10 | [Integration](10-integration-interfaces.md) | MQ, IMS, DB2, file transfer |
| 11 | [Security](11-security-access.md) | Sign-on, roles, platform security |
| 12 | [Messages](12-error-handling-messages.md) | Message literals |
| 13 | [Build and operations](13-build-deploy-operations.md) | Compile, setup, run book |
| 14 | [Cross-reference](14-cross-reference-traceability.md) | Calls, copybooks, rules |
| 15 | [Glossary](15-glossary.md) | Terms used in this package |
| 16 | [Gaps](16-gaps-assumptions-open-questions.md) | Unknowns and QA |
| 17 | [Dependencies](17-dependencies/index.md) | Program, copybook, and job dependencies |
| 18 | [Coverage report](18-coverage/coverage-report.md) | Measured coverage and acceptance criteria |
| 18 | [Gap report](18-coverage/gap-report.md) | Per-component status, conflicts, SME questions |

### Detailed pages

| Area | Index | Pages |
|---|---|---|
| Programs | [07-programs/index.md](07-programs/index.md) | One page per program: divisions, files, EXEC commands, PERFORM graph, paragraph logic, rules, decision coverage |
| Copybooks | [08-data/data-model.md](08-data/data-model.md) | `08-data/layouts/<copybook>.md`: fields, offsets, OCCURS, REDEFINES, 88-levels, users |
| JCL jobs | [06-batch/job-catalog.md](06-batch/job-catalog.md) | `06-batch/jobs/<job>.md`: steps, DD statements, conditions, return codes |
| Procedures | [06-batch/procs/](06-batch/procs/) | One page per PROC and the job template |
| CICS | [05-online/cics-resources.md](05-online/cics-resources.md) | Every CSD resource definition |
| Data definitions | [08-data/data-definitions.md](08-data/data-definitions.md) | DB2 DDL, IMS DBD and PSB objects |

## Sources

- `docs/_work/inventory.json`
- `docs/_work/structure/summary.json`
- `docs/_work/coverage/coverage.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
