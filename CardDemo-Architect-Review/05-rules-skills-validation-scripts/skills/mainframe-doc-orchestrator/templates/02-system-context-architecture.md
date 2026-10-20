# System Context and Architecture

## System context

```mermaid
flowchart LR
    {{context_diagram}}
```
<!-- guide: Actors (user roles, external systems, schedulers, MQ clients, file partners) around the application boundary. External parties only as evidenced (queue names, FTP targets as parameters). -->

{{context_narrative}}

## Logical architecture

```mermaid
flowchart TB
    {{layer_diagram}}
```
<!-- guide: Layers: presentation (BMS/3270), online logic (CICS programs), batch logic (jobs/programs), data access (VSAM/DB2/IMS/MQ), shared components (copybooks, utilities, ASM). -->

| Layer | Components | Technology | Notes |
|---|---|---|---|
{{layer_rows}}

## Modules

| Module | Scope | Paths | Technologies | Depends on | Evidence |
|---|---|---|---|---|---|
{{module_rows}}

## Key end-to-end flows

<!-- guide: 3-8 flows that matter most (e.g. sign-on and menu, a maintenance transaction, daily batch posting, message-driven processing). One Mermaid diagram + short narrative each, linking to detail docs. -->

{{flow_sections}}

## Runtime environment

| Element | Value / parameter | Evidence |
|---|---|---|
{{runtime_rows}}
<!-- guide: CICS region/applid usage, DB2 subsystem, IMS, MQ queue manager, load libraries, HLQ - values only if in source; otherwise parameter names. -->

## Architectural characteristics

{{characteristics}}
<!-- guide: Pseudo-conversational design, shared COMMAREA contract, file-based integration, batch windows (open/close files), transaction boundaries, reuse via copybooks. Tag Inferred where summarized. -->

## Sources

{{sources}}

## Confidence

{{confidence_summary}}
