# Layout CCPAUERY

| Item | Value |
|---|---|
| Source | `app/app-authorization-ims-db2-mq/cpy/CCPAUERY.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 40 |
| Data items | 12 (88-levels: 10) |
| Semantic analysis | validated (batch B01) |

## Purpose

Defines ERROR-LOG-RECORD, the 122-byte application error log record of the authorization module. COPAUA0C fills it (date, time, transaction, program, location code, level, subsystem, codes, message, event key) and writes it to the CICS transient data queue CSSL; the ERR-LEVEL value 'C' (critical) makes COPAUA0C terminate the task. (Confirmed)

Evidence: `app/app-authorization-ims-db2-mq/cpy/CCPAUERY.cpy:19-40`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:983-1010`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | ERROR-LOG-RECORD |  |  | 1 | 122 | 122 |  |  |  | 19 |
| 05 | &nbsp;&nbsp;ERR-DATE | X(06) | DISPLAY | 1 | 6 | 6 |  |  |  | 20 |
| 05 | &nbsp;&nbsp;ERR-TIME | X(06) | DISPLAY | 7 | 12 | 6 |  |  |  | 21 |
| 05 | &nbsp;&nbsp;ERR-APPLICATION | X(08) | DISPLAY | 13 | 20 | 8 |  |  |  | 22 |
| 05 | &nbsp;&nbsp;ERR-PROGRAM | X(08) | DISPLAY | 21 | 28 | 8 |  |  |  | 23 |
| 05 | &nbsp;&nbsp;ERR-LOCATION | X(04) | DISPLAY | 29 | 32 | 4 |  |  |  | 24 |
| 05 | &nbsp;&nbsp;ERR-LEVEL | X(01) | DISPLAY | 33 | 33 | 1 |  |  |  | 25 |
| 05 | &nbsp;&nbsp;ERR-SUBSYSTEM | X(01) | DISPLAY | 34 | 34 | 1 |  |  |  | 30 |
| 05 | &nbsp;&nbsp;ERR-CODE-1 | X(09) | DISPLAY | 35 | 43 | 9 |  |  |  | 37 |
| 05 | &nbsp;&nbsp;ERR-CODE-2 | X(09) | DISPLAY | 44 | 52 | 9 |  |  |  | 38 |
| 05 | &nbsp;&nbsp;ERR-MESSAGE | X(50) | DISPLAY | 53 | 102 | 50 |  |  |  | 39 |
| 05 | &nbsp;&nbsp;ERR-EVENT-KEY | X(20) | DISPLAY | 103 | 122 | 20 |  |  |  | 40 |

## Level-88 conditions

| Field | Condition | Values | Line |
|---|---|---|---|
| ERR-LEVEL | ERR-LOG | 'L' | 26 |
| ERR-LEVEL | ERR-INFO | 'I' | 27 |
| ERR-LEVEL | ERR-WARNING | 'W' | 28 |
| ERR-LEVEL | ERR-CRITICAL | 'C' | 29 |
| ERR-SUBSYSTEM | ERR-APP | 'A' | 31 |
| ERR-SUBSYSTEM | ERR-CICS | 'C' | 32 |
| ERR-SUBSYSTEM | ERR-IMS | 'I' | 33 |
| ERR-SUBSYSTEM | ERR-DB2 | 'D' | 34 |
| ERR-SUBSYSTEM | ERR-MQ | 'M' | 35 |
| ERR-SUBSYSTEM | ERR-FILE | 'F' | 36 |

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [COPAUA0C](../../07-programs/COPAUA0C.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:185` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| ERROR-LOG-RECORD | 19 | COPAUA0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:1003`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:1004` |
| ERR-DATE | 20 | COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:998` |
| ERR-TIME | 21 | COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:999` |
| ERR-APPLICATION | 22 | COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:996` |
| ERR-PROGRAM | 23 | COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:997` |
| ERR-LOCATION | 24 | COPAUA0C (14): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:273`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:311`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:419`, ... |
| ERR-WARNING | 28 | COPAUA0C (4): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:495`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:542`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:590`, ... |
| ERR-CRITICAL | 29 | COPAUA0C (11): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:274`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:312`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:420`, ... |
| ERR-APP | 31 | COPAUA0C (3): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:496`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:543`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:591` |
| ERR-CICS | 32 | COPAUA0C (4): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:421`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:504`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:552`, ... |
| ERR-IMS | 33 | COPAUA0C (4): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:313`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:635`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:842`, ... |
| ERR-MQ | 35 | COPAUA0C (3): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:275`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:770`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:968` |
| ERR-CODE-1 | 37 | COPAUA0C (11): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:277`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:314`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:423`, ... |
| ERR-CODE-2 | 38 | COPAUA0C (7): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:279`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:425`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:508`, ... |
| ERR-MESSAGE | 39 | COPAUA0C (14): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:281`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:315`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:427`, ... |
| ERR-EVENT-KEY | 40 | COPAUA0C (11): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:428`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:499`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:511`, ... |

Named in no procedure statement of the copying programs (may still be moved as part of a group): ERR-LEVEL (line 25), ERR-LOG (line 26), ERR-INFO (line 27), ERR-SUBSYSTEM (line 30), ERR-DB2 (line 34), ERR-FILE (line 36).

## Key fields

| Field | Meaning | Source |
|---|---|---|
| ERR-LOCATION | 4-character code of the failing point (e.g. M001, A001, C001, I001). | `app/app-authorization-ims-db2-mq/cpy/CCPAUERY.cpy:24` |
| ERR-LEVEL | Severity: L log, I info, W warning, C critical. | `app/app-authorization-ims-db2-mq/cpy/CCPAUERY.cpy:25-29` |
| ERR-CRITICAL | 88-level 'C'; triggers task termination in COPAUA0C. | `app/app-authorization-ims-db2-mq/cpy/CCPAUERY.cpy:29` |
| ERR-SUBSYSTEM | Subsystem: A app, C CICS, I IMS, D DB2, M MQ, F file. | `app/app-authorization-ims-db2-mq/cpy/CCPAUERY.cpy:30-36` |
| ERR-MESSAGE | 50-character error text. | `app/app-authorization-ims-db2-mq/cpy/CCPAUERY.cpy:39` |
| ERR-EVENT-KEY | Business key of the failing event (card number, account or customer id). | `app/app-authorization-ims-db2-mq/cpy/CCPAUERY.cpy:40` |

## Observations

- dead-code: ERR-LOG, ERR-INFO, ERR-DB2 and ERR-FILE values are never set by COPAUA0C. (`app/app-authorization-ims-db2-mq/cpy/CCPAUERY.cpy:26-36`)

## Sources

- `app/app-authorization-ims-db2-mq/cpy/CCPAUERY.cpy`
- `docs/_work/structure/copybooks/CCPAUERY.json`
- `docs/_work/layouts/CCPAUERY.json`
- `docs/_work/semantic/copybooks/CCPAUERY.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
