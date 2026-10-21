# Worksheet CBPAUP0C (app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl)

Lines: 386. Paragraphs: 17. Decision points: 28 (business candidates: 14).

Fill `docs/_work/semantic/programs/CBPAUP0C.json`. Read the whole source; this list only indexes it.

## Paragraphs

| Paragraph | Lines | Performs | Performed by |
|---|---|---|---|
| MAIN-PARA | 136-180 | 1000-INITIALIZE, 2000-FIND-NEXT-AUTH-SUMMARY, 3000-FIND-NEXT-AUTH-DTL, 4000-CHECK-IF-EXPIRED, 5000-DELETE-AUTH-DTL, 6000-DELETE-AUTH-SUMMARY, 9000-TAKE-CHECKPOINT |  |
| 1000-INITIALIZE | 183-210 |  | MAIN-PARA |
| 1000-EXIT | 212-213 |  | MAIN-PARA |
| 2000-FIND-NEXT-AUTH-SUMMARY | 216-242 | 9999-ABEND | MAIN-PARA |
| 2000-EXIT | 243-244 |  | MAIN-PARA |
| 3000-FIND-NEXT-AUTH-DTL | 248-272 | 9999-ABEND | MAIN-PARA |
| 3000-EXIT | 273-274 |  | MAIN-PARA |
| 4000-CHECK-IF-EXPIRED | 277-298 |  | MAIN-PARA |
| 4000-EXIT | 299-300 |  | MAIN-PARA |
| 5000-DELETE-AUTH-DTL | 303-323 | 9999-ABEND | MAIN-PARA |
| 5000-EXIT | 324-325 |  | MAIN-PARA |
| 6000-DELETE-AUTH-SUMMARY | 328-347 | 9999-ABEND | MAIN-PARA |
| 6000-EXIT | 348-349 |  | MAIN-PARA |
| 9000-TAKE-CHECKPOINT | 352-372 | 9999-ABEND | MAIN-PARA |
| 9000-EXIT | 373-374 |  | MAIN-PARA |
| 9999-ABEND | 377-383 |  | 2000-FIND-NEXT-AUTH-SUMMARY, 3000-FIND-NEXT-AUTH-DTL, 5000-DELETE-AUTH-DTL, 6000-DELETE-AUTH-SUMMARY, 9000-TAKE-CHECKPOINT |
| 9999-EXIT | 385-386 |  |  |

## Decision points that look like business logic

Each line below must fall inside a rule `source` range or a `no_rule_decisions` range.

| Line | Paragraph | Type | Condition |
|---|---|---|---|
| 146 | MAIN-PARA | LOOP | `UNTIL NO-MORE-AUTHS` |
| 149 | MAIN-PARA | IF | `QUALIFIED-FOR-DELETE` |
| 156 | MAIN-PARA | IF | `PA-APPROVED-AUTH-CNT <= 0 AND PA-APPROVED-AUTH-CNT <= 0` |
| 160 | MAIN-PARA | IF | `WS-AUTH-SMRY-PROC-CNT > P-CHKP-FREQ` |
| 196 | 1000-INITIALIZE | IF | `P-EXPIRY-DAYS IS NUMERIC` |
| 201 | 1000-INITIALIZE | IF | `P-CHKP-FREQ = SPACES OR 0 OR LOW-VALUES` |
| 204 | 1000-INITIALIZE | IF | `P-CHKP-DIS-FREQ = SPACES OR 0 OR LOW-VALUES` |
| 207 | 1000-INITIALIZE | IF | `P-DEBUG-FLAG NOT = 'Y'` |
| 219 | 2000-FIND-NEXT-AUTH-SUMMARY | IF | `DEBUG-ON` |
| 251 | 3000-FIND-NEXT-AUTH-DTL | IF | `DEBUG-ON` |
| 284 | 4000-CHECK-IF-EXPIRED | IF | `WS-DAY-DIFF >= WS-EXPIRY-DAYS` |
| 306 | 5000-DELETE-AUTH-DTL | IF | `DEBUG-ON` |
| 331 | 6000-DELETE-AUTH-SUMMARY | IF | `DEBUG-ON` |
| 360 | 9000-TAKE-CHECKPOINT | IF | `WS-NO-CHKP >= P-CHKP-DIS-FREQ` |

## Calculations

- 231 (2000-FIND-NEXT-AUTH-SUMMARY): `ADD 1 TO WS-NO-SUMRY-READ`
- 232 (2000-FIND-NEXT-AUTH-SUMMARY): `ADD 1 TO WS-AUTH-SMRY-PROC-CNT`
- 262 (3000-FIND-NEXT-AUTH-DTL): `ADD 1 TO WS-NO-DTL-READ`
- 280 (4000-CHECK-IF-EXPIRED): `COMPUTE WS-AUTH-DATE = 99999 - PA-AUTH-DATE-9C`
- 282 (4000-CHECK-IF-EXPIRED): `COMPUTE WS-DAY-DIFF = CURRENT-YYDDD - WS-AUTH-DATE`
- 288 (4000-CHECK-IF-EXPIRED): `SUBTRACT 1 FROM PA-APPROVED-AUTH-CNT`
- 289 (4000-CHECK-IF-EXPIRED): `SUBTRACT PA-APPROVED-AMT FROM PA-APPROVED-AUTH-AMT`
- 291 (4000-CHECK-IF-EXPIRED): `SUBTRACT 1 FROM PA-DECLINED-AUTH-CNT`
- 292 (4000-CHECK-IF-EXPIRED): `SUBTRACT PA-TRANSACTION-AMT FROM PA-DECLINED-AUTH-AMT`
- 316 (5000-DELETE-AUTH-DTL): `ADD 1 TO WS-NO-DTL-DELETED`
- 341 (6000-DELETE-AUTH-SUMMARY): `ADD 1 TO WS-NO-SUMRY-DELETED`
- 359 (9000-TAKE-CHECKPOINT): `ADD 1 TO WS-NO-CHKP`

## Existing rules to review (record a verdict and anchor for each)

- BR-AUTH-CBPAUP0C-001: A pending authorization qualifies for delete when the computed day difference is greater than or equal to the expiry days. Expiry days are the numeric parm value, or 5 when that parm is not numeric. (app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:280-286, app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:196-199)
- BR-AUTH-CBPAUP0C-002: When a pending authorization qualifies for delete and its response code is 00, the approved count and approved amount are reduced. Any other response code reduces the declined count and the declined amount. (app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:287-293)
