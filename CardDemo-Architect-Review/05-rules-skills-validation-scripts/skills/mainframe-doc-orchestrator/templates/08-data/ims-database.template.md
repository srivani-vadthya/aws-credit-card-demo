# IMS Database {{dbd_name}}

<!-- guide: Output to 08-data/ims/<DBD>.md; include related index DBDs and PSBs. -->

| Item | Value |
|---|---|
| DBD source | `{{dbd_path}}` |
| Access method | {{access}} |
| Dataset group / DD | {{datasets}} |
| Index databases | {{index_dbds}} |
| PSBs referencing it | {{psbs}} |

## Hierarchy

```mermaid
flowchart TD
    {{hierarchy_diagram}}
```

## Segments

| Segment | Parent | Bytes | Sequence field (start, bytes, type, unique) | Layout copybook | Pointers / rules |
|---|---|---|---|---|---|
{{segment_rows}}

## Secondary / index relationships

{{index_relationships}}

## PSB sensitivity

| PSB | PCB (type, DBD) | PROCOPT | Sensitive segments (PROCOPT) | Used by programs | Source |
|---|---|---|---|---|---|
{{psb_rows}}

## Access by programs

| Program | Call / command | Segment(s) and SSA | Status handling | Lines |
|---|---|---|---|---|
{{access_rows}}

## Load, unload and maintenance

{{maintenance}}

## Sources

{{sources}}

## Confidence

{{confidence_summary}}
