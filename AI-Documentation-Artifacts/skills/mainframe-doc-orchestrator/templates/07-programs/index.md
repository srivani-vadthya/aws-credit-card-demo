# Program Specifications

| Program | Type | Module | Function | Transaction / job | Calls / transfers to | Doc |
|---|---|---|---|---|---|---|
{{program_rows}}

## Call graph

```mermaid
flowchart LR
    {{call_graph}}
```
<!-- guide: Static CALL, resolved dynamic CALL, XCTL, LINK edges; label edge with mechanism. Split by module if large. -->

## Shared components

| Component | Kind (copybook/subprogram/ASM routine) | Used by | Doc |
|---|---|---|---|
{{shared_rows}}

## Sources

{{sources}}

## Confidence

{{confidence_summary}}
