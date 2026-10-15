---
name: mainframe-doc-orchestrator
description: >-
  Orchestrates evidence-based reverse engineering and documentation of legacy
  mainframe applications (COBOL, PL/I, Assembler, CICS, IMS, DB2, VSAM, MQ, JCL,
  schedulers). Coordinates discovery, analysis and assembly skills, intermediate
  fact inventories and documentation templates. Use when the user asks to
  document, reverse-engineer, inventory, or analyze a mainframe / legacy
  application or repository, or to prepare a modernization documentation package.
---

# Mainframe Documentation Orchestrator

Drives a two-stage pipeline: **Phase A** extracts facts from source into
machine-readable inventories; **Phase B** renders those facts into a
Markdown + Mermaid documentation package using the templates in this skill.
Nothing in the final package may be stated without source evidence.

## Inputs

1. `docs-toolkit/project-profile.yaml` in the target repo. If missing, run the
   bootstrap in [bootstrap.md](bootstrap.md) first.
2. Templates: [templates/](templates/) (override per repo via
   `template_overrides` in the profile).
3. Schemas for intermediate facts: [schemas/](schemas/).

## Non-negotiable principles

- Evidence first: every fact carries `source: path:line[-line]`.
- No hardcoded assumptions: names, prefixes, HLQs, modules, and technologies
  are discovered, then recorded in the profile or inventories. Naming
  conventions (e.g. `CO*` = online) may be *observed* and reported, never
  used as the sole classification signal.
- Confidence tag on every derived statement: `Confirmed` (directly in code),
  `Inferred` (derived from multiple facts; state the reasoning), `Unverified`
  (from comments/READMEs only, or unresolved).
- Unknowns go to the gaps register (`docs/_work/gaps.md`), never guessed.
- Never edit application source. Write only to the profile's `work_dir` and
  `output_dir`.
- Environment placeholders (`&HLQ`, `&SYSUID`, `<<schema>>`, `&&SYSPARM`) are
  documented as parameters, never resolved to invented values.

## Workflow

Copy this checklist into `docs/_work/progress.md` and update it as you go:

```
Phase 0  Setup
- [ ] 0.1 Profile exists and validated (bootstrap.md)
- [ ] 0.2 Rules installed in .cursor/rules
Phase A  Extraction (write to work_dir)
- [ ] A1 Inventory + classification       -> mainframe-inventory-discovery
- [ ] A2 Program facts (COBOL/ASM/PLI)    -> cobol-program-analysis
- [ ] A3 Online facts (CSD/BMS/flows)     -> cics-online-analysis
- [ ] A4 Batch facts (JCL/PROC/sched)     -> batch-jcl-analysis
- [ ] A5 Data facts (layouts/VSAM/DB2/IMS/MQ) -> mainframe-data-model-analysis
- [ ] A6 Integration facts (MQ/DLI/SQL/FTP)   -> mainframe-integration-analysis
- [ ] A7 Business rules                   -> business-rules-extraction
- [ ] A8 Build/deploy/security/ops        -> build-deploy-security-analysis
- [ ] A9 Cross-reference + CRUD matrix consolidation
Phase B  Assembly (write to output_dir)
- [ ] B1 Render templates                 -> mainframe-doc-assembly-qa
- [ ] B2 Coverage check (100% artifacts referenced)
- [ ] B3 QA checklist + gaps register published
```

### Ordering and dependencies

- A1 must finish before anything else; all later steps iterate over
  `inventory.json`, not over ad-hoc directory listings.
- A2 before A3/A4/A6/A7 (they consume program facts).
- A5 can run in parallel with A2; A9 requires A2-A6.
- For large repos, process one module (from the profile) at a time and
  checkpoint each artifact's status in `inventory.json` (`analysis_status`).

### Work directory layout (`work_dir`)

```
inventory.json            # every file, type, module, status (schemas/inventory.schema.json)
references.json           # raw cross-reference scan (discovery)
programs/<NAME>.json      # schemas/program-facts.schema.json
jobs/<NAME>.json          # schemas/job-facts.schema.json
batch/schedule.json, batch/dataflow.json
datasets/<NAME>.json      # schemas/dataset-facts.schema.json
layouts/<COPYBOOK>.json|.md   # copybook_layout.py output
data/entities.json
online/transactions.json, online/screens/<MAPSET>.json, online/navigation.json,
online/commarea.json, online/queues.json
integration/interfaces.json, integration/sequences/*.md
rules/rules.json          # schemas/rule.schema.json
ops/build.json, ops/deploy.json, ops/security.json, ops/runbook.json
xref/crud-matrix.json, xref/call-graph.json, xref/copybook-usage.json
gaps.md, progress.md
```

### Bundled tools (Python 3.1+, standard library only)

| Script | Skill | Purpose |
|---|---|---|
| `scripts/classify_inventory.py` | mainframe-inventory-discovery | content-signature classification -> inventory.json |
| `scripts/scan_references.py` | mainframe-inventory-discovery | baseline cross-references -> references.json |
| `scripts/copybook_layout.py` | mainframe-data-model-analysis | byte offsets/lengths for copybooks |
| `scripts/check_package.py` | mainframe-doc-assembly-qa | coverage, links, placeholders, Mermaid lint |

Script output is a baseline: always confirm against the source before
stating a fact as Confirmed.

### Resume / incremental runs

- Re-read `progress.md` and `inventory.json`; skip artifacts whose
  `analysis_status` is `done` and whose `sha256` is unchanged.
- If a source changed, re-run its analysis and every dependent step listed
  in `xref/*` (callers, jobs, screens using it).

## Scope adaptation

Technologies are enabled by what discovery finds, not by assumption. For each
template section whose technology is absent, keep the heading and write
`Not applicable - no <technology> artifacts found (see inventory.json)`.

## Output package

Rendered into `output_dir` using [templates/](templates/) (structure in
`templates/00-index.md`). Diagrams are Mermaid; follow the conventions in the
`doc-output-standards` rule.

## Related skills

mainframe-inventory-discovery, cobol-program-analysis, cics-online-analysis,
batch-jcl-analysis, mainframe-data-model-analysis,
mainframe-integration-analysis, business-rules-extraction,
build-deploy-security-analysis, mainframe-doc-assembly-qa.
