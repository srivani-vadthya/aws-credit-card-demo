# Build, Deployment and Operations

## Build chains

| Source type | Build JCL / PROC | Steps (translator, precompiler, compiler, binder, bind, gen) | Key options | Output library | Evidence |
|---|---|---|---|---|---|
{{build_rows}}

```mermaid
flowchart LR
    {{build_diagram}}
```

## Libraries and naming parameters

| Parameter / library | Purpose | Defined in | Used by |
|---|---|---|---|
{{library_rows}}

## Environment setup sequence

| # | Step | Job / command | Creates / loads | Prerequisites | Evidence |
|---|---|---|---|---|---|
{{setup_rows}}

## CICS resource installation

{{cics_install}}

## Database and middleware setup

{{db_mw_setup}}
<!-- guide: DB2 objects creation/bind, IMS DBDGEN/PSBGEN/ACBGEN and loads, MQ queue definitions - as found. -->

## Automation scripts

| Script | Purpose | Actions (in order) | Targets (parameters) | Evidence |
|---|---|---|---|---|
{{script_rows}}

## Run book

| Task | When | How (job / transaction / command) | Prerequisites | Expected result | On failure | Evidence |
|---|---|---|---|---|---|---|
{{runbook_rows}}

## Configuration parameters

| Token | Meaning | Defined | Used in | Value source |
|---|---|---|---|---|
{{parameter_rows}}

## Alternative runtime packages

{{runtime_packages}}

## Sources

{{sources}}

## Confidence

{{confidence_summary}}
