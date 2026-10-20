# Job {{job_name}} - {{job_title}}

<!-- guide: Output to 06-batch/jobs/<JOBNAME>.md. One per jcl-job in the inventory. -->

| Item | Value |
|---|---|
| Source | `{{jcl_path}}` |
| Job card | {{job_card}} |
| Module | {{module}} |
| Scheduling | {{schedule_summary}} |
| Predecessors / successors | {{deps}} |
| Restartable | {{restart}} |

## Purpose

{{purpose}}

## Step flow

```mermaid
flowchart TD
    {{step_diagram}}
```

## Steps

### {{step_name}} - {{step_program}}

| Item | Value |
|---|---|
| Program / PROC | {{step_program}} |
| PARM | {{parm}} |
| Condition | {{cond}} |
| Function | {{step_function}} |
<!-- guide: Application program -> link to 07-programs/<PGM>.md. Utility -> summarize control statements in plain language. -->

| DD | Dataset | DISP | DCB / space | Program file (SELECT) | Usage (C/R/U/D) | Layout |
|---|---|---|---|---|---|---|
{{dd_rows}}

{{control_statements}}
<!-- guide: Fenced block of in-stream control cards with an explanation table when non-trivial. -->

<!-- guide: Repeat the step section for each step. -->

## Datasets created / consumed

| Dataset | Role | Generation (GDG) | Downstream consumers |
|---|---|---|---|
{{dataset_rows}}

## Return codes, abends and restart

{{rc_and_restart}}

## Parameters

| Symbol | Value in source | Meaning | Evidence |
|---|---|---|---|
{{param_rows}}

## Sources

{{sources}}

## Confidence

{{confidence_summary}}
