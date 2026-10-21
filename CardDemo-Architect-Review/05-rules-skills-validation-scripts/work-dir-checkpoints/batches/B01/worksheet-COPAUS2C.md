# Worksheet COPAUS2C (app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl)

Lines: 244. Paragraphs: 2. Decision points: 3 (business candidates: 0).

Fill `docs/_work/semantic/programs/COPAUS2C.json`. Read the whole source; this list only indexes it.

## Paragraphs

| Paragraph | Lines | Performs | Performed by |
|---|---|---|---|
| MAIN-PARA | 89-220 | FRAUD-UPDATE |  |
| FRAUD-UPDATE | 221-244 |  | MAIN-PARA |

## Decision points that look like business logic

Each line below must fall inside a rule `source` range or a `no_rule_decisions` range.

| Line | Paragraph | Type | Condition |
|---|---|---|---|

## Calculations

- 107 (MAIN-PARA): `COMPUTE WS-AUTH-TIME = 999999999 - PA-AUTH-TIME-9C`
