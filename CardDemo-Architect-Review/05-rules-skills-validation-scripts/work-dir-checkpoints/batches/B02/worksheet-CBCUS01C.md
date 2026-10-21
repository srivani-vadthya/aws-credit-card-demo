# Worksheet CBCUS01C (app/cbl/CBCUS01C.cbl)

Lines: 178. Paragraphs: 6. Decision points: 12 (business candidates: 0).

Fill `docs/_work/semantic/programs/CBCUS01C.json`. Read the whole source; this list only indexes it.

## Paragraphs

| Paragraph | Lines | Performs | Performed by |
|---|---|---|---|
| (PROCEDURE DIVISION entry) | 71-87 | 0000-CUSTFILE-OPEN, 1000-CUSTFILE-GET-NEXT, 9000-CUSTFILE-CLOSE |  |
| 1000-CUSTFILE-GET-NEXT | 92-116 | Z-ABEND-PROGRAM, Z-DISPLAY-IO-STATUS | (PROCEDURE DIVISION entry) |
| 0000-CUSTFILE-OPEN | 118-134 | Z-ABEND-PROGRAM, Z-DISPLAY-IO-STATUS | (PROCEDURE DIVISION entry) |
| 9000-CUSTFILE-CLOSE | 136-152 | Z-ABEND-PROGRAM, Z-DISPLAY-IO-STATUS | (PROCEDURE DIVISION entry) |
| Z-ABEND-PROGRAM | 154-158 |  | 0000-CUSTFILE-OPEN, 1000-CUSTFILE-GET-NEXT, 9000-CUSTFILE-CLOSE |
| Z-DISPLAY-IO-STATUS | 161-174 |  | 0000-CUSTFILE-OPEN, 1000-CUSTFILE-GET-NEXT, 9000-CUSTFILE-CLOSE |

## Decision points that look like business logic

Each line below must fall inside a rule `source` range or a `no_rule_decisions` range.

| Line | Paragraph | Type | Condition |
|---|---|---|---|

## Calculations

- 137 (9000-CUSTFILE-CLOSE): `ADD 8 TO ZERO GIVING APPL-RESULT`
- 140 (9000-CUSTFILE-CLOSE): `SUBTRACT APPL-RESULT FROM APPL-RESULT`
- 142 (9000-CUSTFILE-CLOSE): `ADD 12 TO ZERO GIVING APPL-RESULT`
