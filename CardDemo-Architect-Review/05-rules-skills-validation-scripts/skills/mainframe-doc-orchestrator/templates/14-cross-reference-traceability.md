# Cross-Reference and Traceability

<!-- guide: Generated from work_dir/xref/*. Large matrices may be split per module. -->

## Transaction -> program -> map -> data

| Transaction | Program | Mapset | Stores accessed | Rules | Doc |
|---|---|---|---|---|---|
{{online_trace_rows}}

## Job -> step -> program -> data

| Job | Step | Program / utility | Datasets | Rules | Doc |
|---|---|---|---|---|---|
{{batch_trace_rows}}

## Copybook usage

| Copybook | Programs | Copybooks including it |
|---|---|---|
{{copybook_rows}}

## Program call relationships

| Caller | Callee | Mechanism | Evidence |
|---|---|---|---|
{{call_rows}}

## Business rule traceability

| Rule | Programs | Screens / jobs | Data | Lines |
|---|---|---|---|---|
{{rule_rows}}

## Dataset name to logical name

| DSN | DD names (jobs) | CICS FILE names | Program SELECT names |
|---|---|---|---|
{{name_rows}}

## Sources

{{sources}}

## Confidence

{{confidence_summary}}
