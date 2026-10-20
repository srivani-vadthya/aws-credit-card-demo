# Program {{program_id}} - {{program_title}}

<!-- guide: Output to 07-programs/<PROGRAM-ID>.md, one per program (COBOL, ASM, PL/I). Populate from work_dir/programs/<PGM>.json. -->

| Item | Value |
|---|---|
| Source | `{{source_path}}` ({{loc}} lines, {{format}}) |
| Language / runtime type | {{language}} / {{runtime_type}} |
| Module | {{module}} |
| Invoked by | {{invoked_by}} |
| Transaction / job step | {{entry_points}} |
| Header description | {{header_description}} (Unverified) |
| Version banner | {{version_banner}} |

## Purpose

{{purpose}}
<!-- guide: 1-3 paragraphs in business language, derived from logic. Link rules BR-... -->

## Interfaces

### Inputs and outputs

| Resource | Kind (file/VSAM/table/segment/queue/map/COMMAREA/parm) | Logical name | Physical name | Access | Layout | Evidence |
|---|---|---|---|---|---|---|
{{io_rows}}

### Linkage / COMMAREA

{{linkage}}

### Called programs and services

| Target | Mechanism (CALL static/dynamic, XCTL, LINK, START, MQ, LE) | When | Parameters | Evidence |
|---|---|---|---|---|
{{call_rows}}

## Copybooks

| Copybook | Purpose | REPLACING | Doc |
|---|---|---|---|
{{copybook_rows}}

## Processing logic

### Control flow

```mermaid
flowchart TD
    {{paragraph_flow}}
```

### Paragraphs

| Paragraph / section | Lines | Purpose | Performs / transfers | Rules |
|---|---|---|---|---|
{{paragraph_rows}}

### Narrative

{{logic_narrative}}
<!-- guide: Step-by-step description of mainline, major branches and loops. For online programs: first-time vs re-entry, AID handling. For batch: open, read loop, per-record processing, totals, close. -->

## Embedded commands

| Kind (CICS/SQL/DLI/MQ) | Command | Resource | Options of note | Response handling | Line |
|---|---|---|---|---|---|
{{command_rows}}

## Business rules implemented

| Rule | Summary | Lines |
|---|---|---|
{{rule_rows}}

## Error handling

| Condition | Detection | Action (message/abend/RC/rollback) | Message / code | Lines |
|---|---|---|---|---|
{{error_rows}}

## Data CRUD

| Store | C | R | U | D | Browse | Notes |
|---|---|---|---|---|---|---|
{{crud_rows}}

## Observations

{{observations}}
<!-- guide: Dead code, unused copybooks/paragraphs, hardcoded literals, inconsistent checks, unhandled responses, performance notes. Evidence-based. -->

## Sources

{{sources}}

## Confidence

{{confidence_summary}}
