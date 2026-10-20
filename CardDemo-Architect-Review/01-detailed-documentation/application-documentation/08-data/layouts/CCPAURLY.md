# Layout CCPAURLY

| Item | Value |
|---|---|
| Source | `app/app-authorization-ims-db2-mq/cpy/CCPAURLY.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 24 |
| Data items | 6 (88-levels: 0) |
| Semantic analysis | validated (batch B01) |

## Purpose

Defines the pending authorization response fields (PA-RL- prefix) copied under 01 PENDING-AUTH-RESPONSE in COPAUA0C. COPAUA0C fills them in 6000-MAKE-DECISION and STRINGs them (with the approved amount re-edited) into a comma-delimited reply sent by MQPUT1 to the requester's reply queue; the code, reason and approved amount are also stored in the PAUTDTL1 detail. (Confirmed)

Evidence: `app/app-authorization-ims-db2-mq/cpy/CCPAURLY.cpy:19-24`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:660-731`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 05 | &nbsp;&nbsp;PA-RL-CARD-NUM | X(16) | DISPLAY | 1 | 16 | 16 |  |  |  | 19 |
| 05 | &nbsp;&nbsp;PA-RL-TRANSACTION-ID | X(15) | DISPLAY | 17 | 31 | 15 |  |  |  | 20 |
| 05 | &nbsp;&nbsp;PA-RL-AUTH-ID-CODE | X(06) | DISPLAY | 32 | 37 | 6 |  |  |  | 21 |
| 05 | &nbsp;&nbsp;PA-RL-AUTH-RESP-CODE | X(02) | DISPLAY | 38 | 39 | 2 |  |  |  | 22 |
| 05 | &nbsp;&nbsp;PA-RL-AUTH-RESP-REASON | X(04) | DISPLAY | 40 | 43 | 4 |  |  |  | 23 |
| 05 | &nbsp;&nbsp;PA-RL-APPROVED-AMT | +9(10).99 | DISPLAY | 44 | 57 | 14 |  |  |  | 24 |

## Level-88 conditions

None.

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [COPAUA0C](../../07-programs/COPAUA0C.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:182` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| PA-RL-CARD-NUM | 19 | COPAUA0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:660`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:722` |
| PA-RL-TRANSACTION-ID | 20 | COPAUA0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:661`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:723` |
| PA-RL-AUTH-ID-CODE | 21 | COPAUA0C (3): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:662`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:724`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:897` |
| PA-RL-AUTH-RESP-CODE | 22 | COPAUA0C (4): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:688`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:693`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:725`, ... |
| PA-RL-AUTH-RESP-REASON | 23 | COPAUA0C (10): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:698`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:704`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:706`, ... |
| PA-RL-APPROVED-AMT | 24 | COPAUA0C (3): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:689`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:694`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:900` |

## Key fields

| Field | Meaning | Source |
|---|---|---|
| PA-RL-CARD-NUM | Card number echoed from the request. | `app/app-authorization-ims-db2-mq/cpy/CCPAURLY.cpy:19` |
| PA-RL-TRANSACTION-ID | Transaction id echoed from the request. | `app/app-authorization-ims-db2-mq/cpy/CCPAURLY.cpy:20` |
| PA-RL-AUTH-ID-CODE | Authorization id code (set to the request auth time). | `app/app-authorization-ims-db2-mq/cpy/CCPAURLY.cpy:21` |
| PA-RL-AUTH-RESP-CODE | '00' approved or '05' declined. | `app/app-authorization-ims-db2-mq/cpy/CCPAURLY.cpy:22` |
| PA-RL-AUTH-RESP-REASON | Decline reason code, '0000' when approved. | `app/app-authorization-ims-db2-mq/cpy/CCPAURLY.cpy:23` |
| PA-RL-APPROVED-AMT | Approved amount, numeric-edited +9(10).99. | `app/app-authorization-ims-db2-mq/cpy/CCPAURLY.cpy:24` |

## Sources

- `app/app-authorization-ims-db2-mq/cpy/CCPAURLY.cpy`
- `docs/_work/structure/copybooks/CCPAURLY.json`
- `docs/_work/layouts/CCPAURLY.json`
- `docs/_work/semantic/copybooks/CCPAURLY.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
