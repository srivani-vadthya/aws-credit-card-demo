# Dataset {{dataset_name}}

<!-- guide: Output to 08-data/datasets/<NAME>.md. NAME = DSN with placeholders kept (or a stable short name, stated). One per distinct physical dataset/cluster/GDG base. -->

| Item | Value |
|---|---|
| DSN | `{{dsn}}` |
| Organisation | {{organisation}} |
| Key (offset, length) / AIX | {{keys}} |
| Record format / length | {{recfm}} / {{lrecl}} |
| Layout copybook | {{layout}} |
| Defined by | {{defined_by}} |
| CICS FILE name(s) | {{cics_files}} |
| GDG limit / options | {{gdg}} |
| Catalog facts (point in time) | {{listcat}} |
| Sample data | {{sample}} |

## Purpose

{{purpose}}

## Access

| Program / job step | Access (C/R/U/D/B) | Via (DD / FILE / AIX path) | Evidence |
|---|---|---|---|
{{access_rows}}

## Lifecycle

{{lifecycle}}
<!-- guide: Created / loaded by, refreshed by, backed up by, deleted/redefined by; online availability windows (CICS open/close). -->

## Consistency

{{consistency}}

## Sources

{{sources}}

## Confidence

{{confidence_summary}}
