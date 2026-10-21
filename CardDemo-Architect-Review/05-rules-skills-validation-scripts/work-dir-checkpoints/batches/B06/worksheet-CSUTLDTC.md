# Worksheet CSUTLDTC (app/cbl/CSUTLDTC.cbl)

Lines: 157. Paragraphs: 3. Decision points: 11 (business candidates: 11).

Fill `docs/_work/semantic/programs/CSUTLDTC.json`. Read the whole source; this list only indexes it.

## Paragraphs

| Paragraph | Lines | Performs | Performed by |
|---|---|---|---|
| (PROCEDURE DIVISION entry) | 90-102 | A000-MAIN |  |
| A000-MAIN | 103-151 |  | (PROCEDURE DIVISION entry) |
| A000-MAIN-EXIT | 152-154 |  | (PROCEDURE DIVISION entry) |

## Decision points that look like business logic

Each line below must fall inside a rule `source` range or a `no_rule_decisions` range.

| Line | Paragraph | Type | Condition |
|---|---|---|---|
| 128 | A000-MAIN | EVALUATE | `TRUE` |
| 129 | A000-MAIN | WHEN | `FC-INVALID-DATE` |
| 131 | A000-MAIN | WHEN | `FC-INSUFFICIENT-DATA` |
| 133 | A000-MAIN | WHEN | `FC-BAD-DATE-VALUE` |
| 135 | A000-MAIN | WHEN | `FC-INVALID-ERA` |
| 137 | A000-MAIN | WHEN | `FC-UNSUPP-RANGE` |
| 139 | A000-MAIN | WHEN | `FC-INVALID-MONTH` |
| 141 | A000-MAIN | WHEN | `FC-BAD-PIC-STRING` |
| 143 | A000-MAIN | WHEN | `FC-NON-NUMERIC-DATA` |
| 145 | A000-MAIN | WHEN | `FC-YEAR-IN-ERA-ZERO` |
| 147 | A000-MAIN | WHEN | `OTHER` |

## Calculations

