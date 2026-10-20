# Batch Schedule and Data Flow

## Schedule sources

| Source | Kind (CA7/Control-M/TWS/script/README) | Jobs covered | Evidence |
|---|---|---|---|
{{schedule_sources}}

## Schedules

<!-- guide: One section per scheduler folder/application/script. Keep provenance; do not merge sources silently. -->

### {{schedule_name}}

| Item | Value |
|---|---|
| Source | {{source}} |
| Calendar / days | {{calendar}} |
| Time window | {{time_window}} |
| Cyclic | {{cyclic}} |

```mermaid
flowchart LR
    {{schedule_diagram}}
```

| Predecessor | Successor | Condition / trigger | Evidence |
|---|---|---|---|
{{edge_rows}}

## Source agreement

{{agreement}}
<!-- guide: Where sources agree/disagree on order or membership. -->

## End-to-end batch data flow

```mermaid
flowchart LR
    {{dataflow_diagram}}
```
<!-- guide: Jobs (rectangles) and datasets (cylinders "[(DSN)]") with create/read/update edges, from work_dir/batch/dataflow.json. -->

## Online / batch interplay

{{online_batch}}
<!-- guide: Files closed/opened in CICS around batch, online-submitted jobs, shared datasets updated by both. -->

## Sources

{{sources}}

## Confidence

{{confidence_summary}}
