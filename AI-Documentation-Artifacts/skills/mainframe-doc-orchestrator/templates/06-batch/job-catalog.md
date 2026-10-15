# Batch Job Catalog

## Jobs

| Job | Purpose | Steps | Programs / utilities | Main inputs | Main outputs | Scheduled (source) | Submitted by | Module | Doc |
|---|---|---|---|---|---|---|---|---|---|
{{job_rows}}

## Job categories

{{categories}}
<!-- guide: Group jobs by role as evidenced: environment setup/definition, data load/refresh, business processing, reporting, maintenance/purge, utilities/samples, build/compile. State the evidence for each grouping. -->

## Procedures (PROCs)

| PROC | Steps | Symbolic parameters (defaults) | Used by | Source |
|---|---|---|---|---|
{{proc_rows}}

## Jobs submitted dynamically

| Job / JCL text | Submitted by | Mechanism (TDQ/INTRDR) | Evidence |
|---|---|---|---|
{{dynamic_rows}}

## Findings

{{findings}}
<!-- guide: Unscheduled jobs, jobs referencing undefined datasets, DD/SELECT mismatches, duplicate purposes. -->

## Related documents

- [Batch schedule and data flow](batch-schedule-flow.md)
- Job specifications: {{job_links}}

## Sources

{{sources}}

## Confidence

{{confidence_summary}}
