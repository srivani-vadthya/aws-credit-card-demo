# DB2 Table {{table_name}}

<!-- guide: Output to 08-data/db2/<TABLE>.md. Keep schema/database placeholders as parameters. -->

| Item | Value |
|---|---|
| Qualified name | `{{qualified_name}}` |
| Tablespace / database | {{tablespace}} |
| DDL source | `{{ddl_path}}` |
| DCLGEN | {{dclgen}} |
| Plans / packages | {{plans}} |

## Columns

| Column | Type | Null | Default | Key | Host variable (DCLGEN) | Meaning |
|---|---|---|---|---|---|---|
{{column_rows}}

## Keys and indexes

| Name | Kind (PK/unique/index/FK) | Columns (order) | Source |
|---|---|---|---|
{{index_rows}}

## Access by programs

| Program | Statement (SELECT/INSERT/UPDATE/DELETE/cursor) | Predicates / columns | SQLCODE handling | Lines |
|---|---|---|---|---|
{{access_rows}}

## Loading and extraction

{{load_extract}}
<!-- guide: Jobs that create, load (DSNTEP*/LOAD), unload (DSNTIAUL/UNLOAD) or maintain the table. -->

## Consistency

{{consistency}}

## Sources

{{sources}}

## Confidence

{{confidence_summary}}
