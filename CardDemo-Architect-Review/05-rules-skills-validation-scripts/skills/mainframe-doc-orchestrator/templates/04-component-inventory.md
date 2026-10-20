# Component Inventory

<!-- guide: Generated from inventory.json. Every analyzable artifact appears exactly once in a table below. Link each name to its detail doc. -->

## Summary by type and module

| Type | {{module_columns}} | Total |
|---|---|---|
{{type_module_matrix}}

## Programs

| Program | Module | Type (batch/online/sub/ASM) | Function (one line) | Invoked by | Doc |
|---|---|---|---|---|---|
{{program_rows}}

## Copybooks

| Copybook | Module | Kind (record layout / COMMAREA / table / map / PCB / DCLGEN / procedure) | Length | Used by | Doc |
|---|---|---|---|---|---|
{{copybook_rows}}

## BMS mapsets

| Mapset | Maps | Used by program(s) | Transaction | Doc |
|---|---|---|---|---|
{{mapset_rows}}

## CICS resource definitions

| Resource type | Name | Group | Source file | Key attributes |
|---|---|---|---|---|
{{csd_rows}}

## JCL jobs and procedures

| Member | Kind (job/proc/template) | Module | Programs/utilities | Scheduled | Doc |
|---|---|---|---|---|---|
{{jcl_rows}}

## Control cards

| Member | Utility | Used by job(s) | Purpose |
|---|---|---|---|
{{ctl_rows}}

## Database definitions

| Member | Kind (DDL/DCLGEN/DBD/PSB/MQSC) | Objects defined | Doc |
|---|---|---|---|
{{dbdef_rows}}

## Scheduler definitions, scripts, other

| File | Kind | Purpose | Doc |
|---|---|---|---|
{{other_rows}}

## Sample data and non-source content

| Path | Kind | Encoding | Described by layout | Notes |
|---|---|---|---|---|
{{data_rows}}

## Orphans and anomalies

{{orphans}}
<!-- guide: Copybooks never copied, programs never invoked, jobs never scheduled, CSD entries without source, source without CSD entries. These are findings, not errors. -->

## Sources

- `{{work_dir}}/inventory.json`, `{{work_dir}}/references.json`

## Confidence

{{confidence_summary}}
