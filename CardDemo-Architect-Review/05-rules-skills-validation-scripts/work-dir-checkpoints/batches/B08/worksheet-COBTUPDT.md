# Worksheet COBTUPDT (app/app-transaction-type-db2/cbl/COBTUPDT.cbl)

Lines: 237. Paragraphs: 9. Decision points: 21 (business candidates: 11).

Fill `docs/_work/semantic/programs/COBTUPDT.json`. Read the whole source; this list only indexes it.

## Paragraphs

| Paragraph | Lines | Performs | Performed by |
|---|---|---|---|
| 0001-OPEN-FILES | 82-89 |  |  |
| 1001-READ-NEXT-RECORDS | 91-99 | 1002-READ-RECORDS, 1003-TREAT-RECORD, 2001-CLOSE-STOP |  |
| 1002-READ-RECORDS | 100-107 |  | 1001-READ-NEXT-RECORDS |
| 1003-TREAT-RECORD | 109-130 | 10031-INSERT-DB, 10032-UPDATE-DB, 10033-DELETE-DB, 9999-ABEND | 1001-READ-NEXT-RECORDS |
| 10031-INSERT-DB | 132-164 | 9999-ABEND | 1003-TREAT-RECORD |
| 10032-UPDATE-DB | 166-195 | 9999-ABEND | 1003-TREAT-RECORD |
| 10033-DELETE-DB | 196-226 | 9999-ABEND | 1003-TREAT-RECORD |
| 9999-ABEND | 230-233 |  | 1003-TREAT-RECORD, 10031-INSERT-DB, 10032-UPDATE-DB, 10033-DELETE-DB |
| 2001-CLOSE-STOP | 234-236 |  | 1001-READ-NEXT-RECORDS |

## Decision points that look like business logic

Each line below must fall inside a rule `source` range or a `no_rule_decisions` range.

| Line | Paragraph | Type | Condition |
|---|---|---|---|
| 93 | 1001-READ-NEXT-RECORDS | LOOP | `UNTIL LASTREC = 'Y'` |
| 104 | 1002-READ-RECORDS | IF | `LASTREC NOT EQUAL TO 'Y'` |
| 110 | 1003-TREAT-RECORD | EVALUATE | `INPUT-REC-TYPE` |
| 111 | 1003-TREAT-RECORD | WHEN | `'A'` |
| 114 | 1003-TREAT-RECORD | WHEN | `'U'` |
| 117 | 1003-TREAT-RECORD | WHEN | `'D'` |
| 120 | 1003-TREAT-RECORD | WHEN | `'*'` |
| 122 | 1003-TREAT-RECORD | WHEN | `OTHER` |
| 151 | 10031-INSERT-DB | EVALUATE | `TRUE` |
| 177 | 10032-UPDATE-DB | EVALUATE | `TRUE` |
| 207 | 10033-DELETE-DB | EVALUATE | `TRUE` |

## Calculations


## Existing rules to review (record a verdict and anchor for each)

- BR-TRANTYPE-COBTUPDT-001: A transaction-type maintenance record inserts when the type is A, updates when the type is U, deletes when the type is D, and is ignored when the type is asterisk. Any other type abends with message ERROR: TYPE NOT VALID. (app/app-transaction-type-db2/cbl/COBTUPDT.cbl:111-128)
