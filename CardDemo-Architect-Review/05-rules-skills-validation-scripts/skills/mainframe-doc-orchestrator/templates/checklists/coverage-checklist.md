# Coverage Checklist

Use during Phase A to make sure every artifact family was analyzed. Tick
only when the corresponding work_dir output exists for **all** items of
that type (counts from `inventory.json` summary).

| Artifact type | Count in inventory | Analyzed | Output location | Done |
|---|---|---|---|---|
| cobol-program | | | programs/*.json | [ ] |
| asm-program / asm-macro / asm-copybook | | | programs/*.json | [ ] |
| cobol-copybook | | | layouts/*.json, xref/copybook-usage.json | [ ] |
| bms-symbolic-map | | | online/screens/*.json (linked) | [ ] |
| db2-dclgen | | | datasets/db2 facts | [ ] |
| bms-mapset | | | online/screens/*.json | [ ] |
| cics-csd | | | online/transactions.json | [ ] |
| jcl-job | | | jobs/*.json | [ ] |
| jcl-proc / jcl-template | | | jobs/*.json (expansion), ops/build.json | [ ] |
| control-cards | | | jobs/*.json (step control) | [ ] |
| ims-dbd / ims-psb | | | datasets/ims facts | [ ] |
| db2-ddl | | | datasets/db2 facts | [ ] |
| mq-definition | | | integration/interfaces.json | [ ] |
| scheduler-* | | | batch/schedule.json | [ ] |
| script-* | | | ops/deploy.json, batch/schedule.json | [ ] |
| catalog-listing | | | datasets/*.json (catalog facts) | [ ] |
| data-text / data-binary | | | data/samples profile | [ ] |
| documentation / diagram | | | existing_docs cross-check notes | [ ] |
| unclassified | must be 0 | | gaps.md | [ ] |

## Cross-cutting

- [ ] Every program has runtime type and invoker(s) (or flagged orphan)
- [ ] Every dynamic transfer target resolved or listed as a gap
- [ ] Every DD in every job mapped to a program file or utility use
- [ ] Every CICS FILE mapped to a dataset and a layout
- [ ] Every dataset/table/segment/queue has at least one accessor in the CRUD matrix (or flagged)
- [ ] Every record copybook length verified against at least one other source
- [ ] Every scheduler edge has provenance
- [ ] Every validation message literal is linked to a rule or error-catalog entry
- [ ] Technologies per module recorded in the profile with evidence

## Measured acceptance (Phase S and B, from `coverage_validate.py`)

Copy the "Measured" column from `18-coverage/coverage-report.md`; do not
estimate.

| Criterion | Target | Measured | Pass |
|---|---|---|---|
| Programs: page + validated semantics | 100% | | [ ] |
| Paragraphs listed with line range | 100% | | [ ] |
| Paragraphs with validated logic | 100% | | [ ] |
| EXEC CICS/SQL/DLI, CALL, SELECT cited | 100% | | [ ] |
| Programs with rules or no-rule reason | 100% | | [ ] |
| Business-candidate decisions linked to a rule or reason | 100% | | [ ] |
| Copybook fields, 88-levels, COPY edges documented | 100% | | [ ] |
| JCL jobs, PROCs, steps, DDs, conditions documented | 100% | | [ ] |
| CICS resources documented; transactions documented or unresolved | 0 missing | | [ ] |
| Data definitions, datasets, dependencies documented | 100% | | [ ] |
| Inventory artifacts documented or excluded with reason | 0 missing | | [ ] |
| Source references resolve | 0 invalid | | [ ] |
| Gap report: missing / unanalyzed | 0 / 0 | | [ ] |
| `check_package.py` issues | 0 | | [ ] |
