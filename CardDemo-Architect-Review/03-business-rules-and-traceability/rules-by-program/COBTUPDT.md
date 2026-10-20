# COBTUPDT

Draft from `docs/_work/rules/rules.json`.

## BR-TRANTYPE-COBTUPDT-001

A transaction-type maintenance record inserts when the type is A, updates when the type is U, deletes when the type is D, and is ignored when the type is asterisk. Any other type abends with message ERROR: TYPE NOT VALID.

- Category: decision
- Confidence: Confirmed
- Source: `app/app-transaction-type-db2/cbl/COBTUPDT.cbl:111-128`
