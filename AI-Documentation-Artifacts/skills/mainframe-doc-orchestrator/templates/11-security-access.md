# Security and Access

<!-- guide: Never reproduce credentials; reference their location. Report weaknesses neutrally with evidence. -->

## Authentication

{{authentication}}
<!-- guide: Sign-on transaction/program, user store, comparison logic (case handling, format), failure handling, lockout (if any). -->

## Users, roles and authorization

| Role / user type | Identified by | Allowed functions | Enforcement point | Evidence |
|---|---|---|---|---|
{{role_rows}}

## Function access matrix

| Function (transaction/option) | {{role_columns}} | Enforcement |
|---|---|---|
{{access_rows}}

## Platform security

| Mechanism | Definitions found | Scope | Evidence |
|---|---|---|---|
{{platform_rows}}
<!-- guide: RACF commands, CICS RESSEC/CMDSEC, DB2 GRANT, MQ authority, dataset profiles. "None found" is a valid result. -->

## Sensitive data

| Field / store | Kind (PII/PCI/credential) | Protection observed | Evidence |
|---|---|---|---|
{{sensitive_rows}}

## Security observations

{{observations}}

## Sources

{{sources}}

## Confidence

{{confidence_summary}}
