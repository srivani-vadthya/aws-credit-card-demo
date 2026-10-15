# Data Model

## Logical entities

```mermaid
erDiagram
    {{er_diagram}}
```
<!-- guide: Entities and relationships with evidence type in the label (shared key, AIX, FK, IMS parent). -->

| Entity | Meaning | Identifier | Physical store(s) | Layout | Evidence |
|---|---|---|---|---|---|
{{entity_rows}}

## Relationships

| From | To | Cardinality | Basis (evidence type) | Evidence |
|---|---|---|---|---|
{{relationship_rows}}

## Physical stores

| Store | Kind (KSDS/ESDS/RRDS/AIX/PATH/PS/GDG/DB2/IMS/MQ/TSQ/TDQ) | Key | Record length | Layout | CICS name | Doc |
|---|---|---|---|---|---|---|
{{store_rows}}

## Data dictionary (key fields)

| Field | Entity | Format | Domain / values | Set by | Validated by | Sensitivity |
|---|---|---|---|---|---|---|
{{dictionary_rows}}
<!-- guide: Full per-field detail lives in layouts/<COPYBOOK>.md; list business-significant fields here. -->

## Consistency checks

| Check | Result | Details | Evidence |
|---|---|---|---|
{{check_rows}}
<!-- guide: Results of mainframe-data-model-analysis mismatch checks. -->

## Sample data profile

{{sample_profile}}

## Related documents

- [CRUD matrix](crud-matrix.md)
- Datasets: {{dataset_links}}
- Layouts: {{layout_links}}
- DB2: {{db2_links}} - IMS: {{ims_links}} - MQ: {{mq_links}}

## Sources

{{sources}}

## Confidence

{{confidence_summary}}
