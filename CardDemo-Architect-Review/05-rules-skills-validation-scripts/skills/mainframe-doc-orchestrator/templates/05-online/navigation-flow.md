# Online Navigation Flow

## Overall navigation

```mermaid
flowchart TD
    {{navigation_diagram}}
```
<!-- guide: Nodes = transactions/programs (label "TRANSID / PROGRAM"). Edges labelled with trigger (option number, PF key, condition) and mechanism (XCTL/LINK/RETURN TRANSID/START). Split per module or role if > 40 nodes. -->

## Navigation by role

{{role_sections}}
<!-- guide: One diagram or table per user type when code differentiates roles; cite the check (e.g. user-type 88-level evaluation). -->

## Menu and option tables

| Menu program | Option # | Text | Target program | Restriction | Source (VALUE line) |
|---|---|---|---|---|---|
{{menu_rows}}

## Transfer edges

| From | To | Mechanism | Trigger / condition | COMMAREA passed | Evidence |
|---|---|---|---|---|---|
{{edge_rows}}

## Unresolved targets

{{unresolved}}
<!-- guide: Variable targets that could not be traced to values. -->

## Sources

{{sources}}

## Confidence

{{confidence_summary}}
