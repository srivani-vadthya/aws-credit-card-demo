# Worksheet CBACT03C (app/cbl/CBACT03C.cbl)

Lines: 178. Paragraphs: 6. Decision points: 12 (business candidates: 0).

Fill `docs/_work/semantic/programs/CBACT03C.json`. Read the whole source; this list only indexes it.

## Paragraphs

| Paragraph | Lines | Performs | Performed by |
|---|---|---|---|
| (PROCEDURE DIVISION entry) | 71-87 | 0000-XREFFILE-OPEN, 1000-XREFFILE-GET-NEXT, 9000-XREFFILE-CLOSE |  |
| 1000-XREFFILE-GET-NEXT | 92-116 | 9910-DISPLAY-IO-STATUS, 9999-ABEND-PROGRAM | (PROCEDURE DIVISION entry) |
| 0000-XREFFILE-OPEN | 118-134 | 9910-DISPLAY-IO-STATUS, 9999-ABEND-PROGRAM | (PROCEDURE DIVISION entry) |
| 9000-XREFFILE-CLOSE | 136-152 | 9910-DISPLAY-IO-STATUS, 9999-ABEND-PROGRAM | (PROCEDURE DIVISION entry) |
| 9999-ABEND-PROGRAM | 154-158 |  | 0000-XREFFILE-OPEN, 1000-XREFFILE-GET-NEXT, 9000-XREFFILE-CLOSE |
| 9910-DISPLAY-IO-STATUS | 161-174 |  | 0000-XREFFILE-OPEN, 1000-XREFFILE-GET-NEXT, 9000-XREFFILE-CLOSE |

## Decision points that look like business logic

Each line below must fall inside a rule `source` range or a `no_rule_decisions` range.

| Line | Paragraph | Type | Condition |
|---|---|---|---|

## Calculations

- 137 (9000-XREFFILE-CLOSE): `ADD 8 TO ZERO GIVING APPL-RESULT`
- 140 (9000-XREFFILE-CLOSE): `SUBTRACT APPL-RESULT FROM APPL-RESULT`
- 142 (9000-XREFFILE-CLOSE): `ADD 12 TO ZERO GIVING APPL-RESULT`
