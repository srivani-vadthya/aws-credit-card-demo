# Screen {{mapset}} / {{map}} - {{screen_title}}

<!-- guide: One file per mapset (sections per map if several). Output to 05-online/screens/<MAPSET>.md. -->

| Item | Value |
|---|---|
| Mapset / map | {{mapset}} / {{map}} |
| Source | `{{bms_path}}` |
| Symbolic map copybook | {{symbolic_copybook}} |
| Size | {{rows}} x {{cols}} |
| Mapset options | {{dfhmsd_options}} |
| Used by program(s) | {{programs}} |
| Transaction(s) | {{transids}} |

## Purpose

{{purpose}}

## Layout mockup

```text
{{mockup}}
```
<!-- guide: Built strictly from POS/LENGTH/INITIAL per cics-online-analysis reference. Include a column ruler. -->

## Fields

| Field | Row | Col | Len | Kind (input/output/literal/hidden) | Attributes | Color | Initial | Filled / validated by | Rules |
|---|---|---|---|---|---|---|---|---|---|
{{field_rows}}

## Function keys

| Key | Action | Target / result | Evidence |
|---|---|---|---|
{{key_rows}}

## Validation and messages

| Field | Check | Message text | Cursor positioned | Rule | Evidence |
|---|---|---|---|---|---|
{{validation_rows}}

## Behaviour

{{behaviour}}
<!-- guide: First display vs re-display, data retrieval to populate, list paging, selection codes, confirmation steps. -->

## Sources

{{sources}}

## Confidence

{{confidence_summary}}
