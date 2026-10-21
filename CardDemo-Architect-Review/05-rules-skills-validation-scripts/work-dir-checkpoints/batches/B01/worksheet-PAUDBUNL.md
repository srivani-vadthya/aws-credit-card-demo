# Worksheet PAUDBUNL (app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL)

Lines: 317. Paragraphs: 11. Decision points: 11 (business candidates: 1).

Fill `docs/_work/semantic/programs/PAUDBUNL.json`. Read the whole source; this list only indexes it.

## Paragraphs

| Paragraph | Lines | Performs | Performed by |
|---|---|---|---|
| MAIN-PARA | 157-170 | 1000-INITIALIZE, 2000-FIND-NEXT-AUTH-SUMMARY, 4000-FILE-CLOSE |  |
| 1000-INITIALIZE | 173-200 | 9999-ABEND | MAIN-PARA |
| 1000-EXIT | 203-204 |  | MAIN-PARA |
| 2000-FIND-NEXT-AUTH-SUMMARY | 207-247 | 3000-FIND-NEXT-AUTH-DTL, 9999-ABEND | MAIN-PARA |
| 2000-EXIT | 248-249 |  | MAIN-PARA |
| 3000-FIND-NEXT-AUTH-DTL | 253-284 | 9999-ABEND | 2000-FIND-NEXT-AUTH-SUMMARY |
| 3000-EXIT | 285-286 |  | 2000-FIND-NEXT-AUTH-SUMMARY |
| 4000-FILE-CLOSE | 289-304 |  | MAIN-PARA |
| 4000-EXIT | 305-306 |  | MAIN-PARA |
| 9999-ABEND | 308-314 |  | 1000-INITIALIZE, 2000-FIND-NEXT-AUTH-SUMMARY, 3000-FIND-NEXT-AUTH-DTL |
| 9999-EXIT | 316-317 |  |  |

## Decision points that look like business logic

Each line below must fall inside a rule `source` range or a `no_rule_decisions` range.

| Line | Paragraph | Type | Condition |
|---|---|---|---|
| 232 | 2000-FIND-NEXT-AUTH-SUMMARY | IF | `PA-ACCT-ID IS NUMERIC` |

## Calculations

- 225 (2000-FIND-NEXT-AUTH-SUMMARY): `ADD 1 TO WS-NO-SUMRY-READ`
- 226 (2000-FIND-NEXT-AUTH-SUMMARY): `ADD 1 TO WS-AUTH-SMRY-PROC-CNT`
- 268 (3000-FIND-NEXT-AUTH-DTL): `ADD 1 TO WS-NO-SUMRY-READ`
- 269 (3000-FIND-NEXT-AUTH-DTL): `ADD 1 TO WS-AUTH-SMRY-PROC-CNT`
