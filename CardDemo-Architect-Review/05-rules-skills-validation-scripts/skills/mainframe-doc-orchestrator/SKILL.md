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
Phase S  Structure and batched semantics (write to work_dir)
- [ ] S1 extract_structure.py             -> structure/ (every paragraph, statement, data item, step, DD)
- [ ] S2 batch_manager.py init + worksheets -> batches/manifest.json, batches/<ID>/worksheet.md, semantic/ skeletons
- [ ] S3 One batch at a time: fill semantic/programs|copybooks/*.json ([batch-analysis.md](batch-analysis.md))
- [ ] S4 batch_manager.py check <ID>      -> batches/<ID>/checkpoint.json; repeat S3 until validated (0 ungrounded paragraphs)
- [ ] S5 semantic/reviews/<MEMBER>.json + batch_manager.py check-reviews -> legacy rules of non-COBOL members (Assembler, PL/I) re-verified
Phase B  Assembly (write to output_dir)
- [ ] B1 Render templates                 -> mainframe-doc-assembly-qa
- [ ] B1b render_detail.py                -> program, layout, job, PROC, CICS, data-definition, dependency pages
- [ ] B2 coverage_validate.py (all acceptance criteria pass) + check_package.py (0 issues)
- [ ] B3 gap_report.py + QA checklist + gaps register published
- [ ] B4 build_docx.py                    -> one DOCX holding every Markdown page (full detail, not a summary)
```

Phase S exists because summary-level analysis silently drops logic once a
program exceeds the context window. The extractor lists every element
deterministically; the analyst only adds meaning, in batches small enough to
read completely, and the validator rejects any batch that leaves a paragraph
undescribed, cites lines outside the paragraph, or quotes an anchor that is
not in the cited code. Never mark a batch complete by editing `status` by
hand; only `batch_manager.py check` sets it.

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
structure/programs/<PGM>.json     # extract_structure.py: divisions, paragraphs, statements, decisions, data items
structure/copybooks/<CPY>.json, structure/copybook-usage.json
structure/jcl/<MEMBER>.json       # PROCs as <MEMBER>__PROC, templates as <MEMBER>__TEMPLATE
structure/csd.json, structure/data-definitions.json, structure/summary.json
batches/manifest.json             # batch plan + status (only batch_manager.py writes status)
batches/<ID>/worksheet.md, batches/<ID>/checkpoint.json
semantic/programs/<PGM>.json      # analyst output: paragraph logic, rules, no-rule reasons, observations
semantic/copybooks/<CPY>.json
semantic/reviews/<MEMBER>.json    # legacy-rule reviews for non-COBOL members (validated by check-reviews)
batches/reviews-checkpoint.json
rules/rules.json (schema rules/2), rules/rules-legacy.json
coverage/coverage.json, coverage/gaps.json, coverage/check_package.json
```

### Bundled tools (Python 3.1+, standard library only)

| Script | Skill | Purpose |
|---|---|---|
| `scripts/classify_inventory.py` | mainframe-inventory-discovery | content-signature classification -> inventory.json |
| `scripts/scan_references.py` | mainframe-inventory-discovery | baseline cross-references -> references.json |
| `scripts/copybook_layout.py` | mainframe-data-model-analysis | byte offsets/lengths for copybooks |
| `scripts/check_package.py` | mainframe-doc-assembly-qa | `<inventory.json> <output_dir> [--json path]`: coverage, links, placeholders, Mermaid lint |
| `scripts/build_docx.py` | mainframe-doc-assembly-qa | `<output_dir> <docx> [--title T] [--date D]`: every Markdown page in one DOCX (headings, tables, lists, code, internal links) |
| `scripts/extract_structure.py` | this skill | `<inventory.json> <work_dir> [--only cobol\|copybook\|jcl\|csd\|data]` -> structure/; records every procedure statement, including field-to-field MOVEs (`data_moves`) and anything it cannot classify (`unclassified`) |
| `scripts/batch_manager.py` | this skill | `init\|worksheets\|check\|check-reviews\|status\|next <work_dir>`: batch plan, validation (anchors, decision coverage, paragraph-logic grounding), checkpoints |
| `scripts/schedule_lines.py` | this skill | `<work_dir> [--repo .]`: adds OUTCOND/INCOND/JOB line numbers to Control-M facts in `batch/schedule.json`; exit 1 lists facts it cannot locate exactly once |
| `scripts/render_detail.py` | this skill | `<work_dir> <output_dir>`: detailed pages from structure + validated semantics; statement inventory, statements in source order, copybook field references by program, PROC-supplied datasets on job steps |
| `scripts/coverage_validate.py` | this skill | `<work_dir> <output_dir>`: coverage.json + 18-coverage/coverage-report.md; exit 1 on any failed criterion. Includes procedure statements, all decision points, logic grounding, rule traceability, scheduler and dataflow edges, data items by name and line |
| `scripts/gap_report.py` | this skill | `<work_dir> <output_dir> [--claimed-pages N]`: gaps.json + 18-coverage/gap-report.md + 18-coverage/gap-register.md; exit line reports `register_without_line` (must be 0) |

Script output is a baseline: always confirm against the source before
stating a fact as Confirmed.

Run Python with `PYTHONIOENCODING=utf-8` on Windows consoles. Scripts read
JSON as `utf-8-sig`; write JSON without a BOM.

### Resume / incremental runs

- Re-read `progress.md` and `inventory.json`; skip artifacts whose
  `analysis_status` is `done` and whose `sha256` is unchanged.
- If a source changed, re-run its analysis and every dependent step listed
  in `xref/*` (callers, jobs, screens using it).
- Phase S resume: `batch_manager.py status <work_dir>` shows every batch;
  `batch_manager.py next <work_dir>` names the first batch that is not
  validated. `check` recomputes source sha256 values, so a changed program
  turns its batch back to `failed` (stale) automatically. Re-run `extract_structure.py`
  first when sources change, then re-check, then re-render.
- Batches can run in parallel (one agent per batch) because each writes only
  its own `semantic/` files and checkpoint. Run `check all` afterwards to
  rewrite the manifest from the checkpoints.
- After any change to `batch/schedule.json`, run `schedule_lines.py` first;
  `coverage_validate.py` marks a scheduler edge partial when its citation
  has no line number.
- After any change: `render_detail.py`, `coverage_validate.py`, `gap_report.py`,
  `check_package.py`, then `build_docx.py`, in that order. Do not report
  coverage that the last `coverage_validate.py` run did not measure.
- A validator category that fails on a correct page is a validator bug: fix
  the matcher and record why, never edit pages or semantics to satisfy it.

## Scope adaptation

Technologies are enabled by what discovery finds, not by assumption. For each
template section whose technology is absent, keep the heading and write
`Not applicable - no <technology> artifacts found (see inventory.json)`.

## Output package

Rendered into `output_dir` using [templates/](templates/) (structure in
`templates/00-index.md`). Diagrams are Mermaid; follow the conventions in the
`doc-output-standards` rule. `render_detail.py` adds `06-batch/procs/`,
`05-online/cics-resources.md`, `08-data/data-definitions.md`,
`17-dependencies/` and `14-cross-reference-traceability.md` (every rule to
program, paragraph, source lines, CICS transactions that start or reach the
program, and JCL steps; online and batch flows) and replaces program, layout
and job pages with the detailed versions; the validators add `18-coverage/`.
`gap_report.py` also lists every Unverified statement found in the work
folder JSON, with its source, and writes `18-coverage/gap-register.md`: one
row per unresolved item, SME question, conflict (with its kind),
Unverified statement and ambiguous dependency, each with evidence class,
line-level source, impact where the work files support it, status, owner
(technical investigation or SME) and next action. In the traceability page,
rules that name no paragraph show the enclosing paragraph or division looked
up from the cited line, marked *(derived)*. `build_docx.py`
writes the whole package as one Word file; a summary DOCX is never a
substitute for the pages.

## Acceptance

The package is accepted only when `coverage_validate.py` reports every
criterion as pass, `check_package.py` reports 0 issues, and the gap report
shows 0 `missing` and 0 `unanalyzed` components. Items classified
`unresolved` or `requires SME clarification` are acceptable only with the
reason recorded. Coverage percentages are measurements of presence and
validated anchors, not of semantic correctness; say so when reporting them.

## Related skills

mainframe-inventory-discovery, cobol-program-analysis, cics-online-analysis,
batch-jcl-analysis, mainframe-data-model-analysis,
mainframe-integration-analysis, business-rules-extraction,
build-deploy-security-analysis, mainframe-doc-assembly-qa.
