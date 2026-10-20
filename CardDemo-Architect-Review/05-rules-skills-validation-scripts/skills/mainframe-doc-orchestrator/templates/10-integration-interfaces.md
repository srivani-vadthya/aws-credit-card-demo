# Integration Interfaces

## Interface map

```mermaid
flowchart LR
    {{interface_diagram}}
```

## Catalog

| Id | Type | Direction | Producer | Consumer | Endpoint | Trigger | Format | Doc |
|---|---|---|---|---|---|---|---|---|
{{interface_rows}}
<!-- guide: Types: MQ, IMS-DLI, DB2, CICS-LINK, CICS-START, TDQ, TSQ, FILE-TRANSFER, INTRDR, CALL-API, OTHER. -->

## Units of work and transactional boundaries

| Flow | Resources in the unit of work | Commit point | Rollback / compensation | Evidence |
|---|---|---|---|---|
{{uow_rows}}

## Key interaction sequences

{{sequence_sections}}
<!-- guide: One Mermaid sequenceDiagram per significant flow. -->

## File transfers and job submission

| Id | Mechanism | Local dataset | Remote / target (parameter) | Mode | Evidence |
|---|---|---|---|---|---|
{{transfer_rows}}

## External dependencies

| Dependency | Kind | Required by | Evidence |
|---|---|---|---|
{{dependency_rows}}

## Sources

{{sources}}

## Confidence

{{confidence_summary}}
