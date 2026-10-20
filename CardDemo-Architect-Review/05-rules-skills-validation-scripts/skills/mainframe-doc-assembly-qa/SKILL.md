---
name: mainframe-doc-assembly-qa
description: >-
  Assembles the final mainframe application documentation package from
  extracted fact inventories using the orchestrator's Markdown + Mermaid
  templates, then validates it: artifact coverage against the inventory,
  cross-reference and link integrity, Mermaid syntax conventions, evidence
  and confidence tagging, and the gaps register. Use in the final phase of
  legacy application documentation or when checking a generated package
  for completeness.
disable-model-invocation: true
---

# Documentation Assembly and QA

Inputs: everything under `<work_dir>`; templates from the orchestrator
skill (`templates/`, or `template_overrides` from the profile). Output:
`<output_dir>/` package as defined by `templates/00-index.md`.

## Assembly order

```
- [ ] 1 Copy package skeleton from templates/00-index.md (folders + file list)
- [ ] 2 Reference docs first: 15-glossary, 04-component-inventory, 08-data/*
- [ ] 3 Per-artifact docs: 07-programs/<PGM>.md, 06-batch/jobs/<JOB>.md, 05-online/screens/<MAP>.md, 08-data/datasets/<DS>.md
- [ ] 4 Cross-cutting docs: 05-online flows, 06-batch schedule, 09 rules, 10 integration, 11 security, 12 errors, 13 ops
- [ ] 5 Traceability: 14-cross-reference-traceability (matrices from xref/*)
- [ ] 6 Overview docs last: 01-executive-summary, 02-architecture, 03-technology-stack
- [ ] 7 16-gaps-assumptions-open-questions from work_dir/gaps.md
- [ ] 8 Run QA (below) until clean
```

Rules for rendering:
- Replace every `{{placeholder}}` in templates; delete template guidance
  blocks (`<!-- guide: ... -->`) after use.
- Keep optional sections; fill with `Not applicable - <reason>`.
- Per-artifact files are generated for **every** inventory item of that
  type; use the per-artifact template (`*.template.md`).
- Diagrams: Mermaid only, following the `doc-output-standards` rule;
  split large graphs by module.
- Write overview text only from facts already rendered in detail docs.

## QA

Run the coverage checker:

```bash
python <skill_dir>/scripts/check_package.py <work_dir>/inventory.json <output_dir>
```

It reports:
- inventory artifacts (analyzable types) never mentioned in the package,
- broken relative Markdown links,
- leftover `{{placeholders}}` and template guide comments,
- Mermaid blocks with risky syntax (spaces in node IDs, styling, click,
  reserved IDs),
- files without a `## Sources` section.

`check_package.py` only proves that names and links are present. Measured
coverage comes from the orchestrator scripts:

```bash
python <orchestrator>/scripts/render_detail.py <work_dir> <output_dir>
python <orchestrator>/scripts/coverage_validate.py <work_dir> <output_dir>
python <orchestrator>/scripts/gap_report.py <work_dir> <output_dir> [--claimed-pages N]
```

`coverage_validate.py` checks every paragraph, EXEC block, CALL, SELECT,
data item, copybook field and 88-level, COPY edge, JCL step, DD and
condition, CICS resource, data definition, dataset and dependency against
the page that should document it, resolves every `path:line` reference,
and counts semantic coverage only from validated batches. It writes
`<work_dir>/coverage/coverage.json` and `<output_dir>/18-coverage/coverage-report.md`
and exits 1 if any acceptance criterion fails. `gap_report.py` assigns
each component one status (missing, unanalyzed, partially documented,
unresolved, requires SME clarification, documented) and lists conflicts,
ambiguous dependencies and SME questions.

Then complete [../mainframe-doc-orchestrator/templates/checklists/qa-checklist.md](../mainframe-doc-orchestrator/templates/checklists/qa-checklist.md)
manually (semantic checks the script cannot do) and record the result in
`<output_dir>/16-gaps-assumptions-open-questions.md` under "QA results".

## Exit criteria

- `coverage_validate.py` passes every acceptance criterion; gap report has
  0 missing and 0 unanalyzed components.
- Checker reports 0 uncovered artifacts (or each justified in the gaps doc).
- 0 broken links, 0 placeholders, 0 Mermaid warnings.
- Every business rule, interface and dataset referenced from at least one
  program or job doc, and vice versa.
- Gaps register lists every Unverified item that affects understanding.
