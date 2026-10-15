# Executive Summary

<!-- guide: Business-readable. Every claim must be backed by detail docs; link to them. No technology jargon in the first two sections. -->

## Purpose of the application

{{business_purpose}}
<!-- guide: 1-2 paragraphs. Derive from what the programs actually do (transactions, jobs, data). Cite README statements as Unverified unless confirmed. -->

## Users and roles

| Role | How identified in the system | Main capabilities | Evidence |
|---|---|---|---|
{{role_rows}}

## Business capabilities

| Capability | Channel (online/batch/message) | Key components | Details |
|---|---|---|---|
{{capability_rows}}

## Key business objects

{{business_objects}}
<!-- guide: Entities from 08-data/data-model.md with one-line meaning each. -->

## Size and composition

| Measure | Value |
|---|---|
| Programs (by type) | {{program_counts}} |
| Online transactions / screens | {{online_counts}} |
| Batch jobs / scheduled jobs | {{batch_counts}} |
| Datasets / DB2 tables / IMS databases / queues | {{data_counts}} |
| Business rules catalogued | {{rule_count}} |
| Lines of code (non-comment) | {{loc}} |

## Optional / extension modules

{{module_summary}}

## Notable findings

{{key_findings}}
<!-- guide: Up to 10 bullets: risks, anomalies, dead code, security observations, data mismatches - each linked to the detailed section. -->

## Modernization observations

{{modernization_observations}}
<!-- guide: Only when profile documentation.include_modernization_observations is true. Neutral, evidence-based (e.g. tight coupling via shared COMMAREA, hardcoded values, batch windows). Tag Inferred. -->

## Sources

{{sources}}

## Confidence

{{confidence_summary}}
