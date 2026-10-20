# Layout CCPAURQY

| Item | Value |
|---|---|
| Source | `app/app-authorization-ims-db2-mq/cpy/CCPAURQY.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 36 |
| Data items | 18 (88-levels: 0) |
| Semantic analysis | validated (batch B01) |

## Purpose

Defines the pending authorization request fields (PA-RQ- prefix) copied under 01 PENDING-AUTH-REQUEST in COPAUA0C. The MQ request is a comma-delimited text string that COPAUA0C UNSTRINGs into these 18 fields in order; the amount arrives as text and is converted with NUMVAL into PA-RQ-TRANSACTION-AMT. The fields are later copied into the PAUTDTL1 detail segment. (Confirmed)

Evidence: `app/app-authorization-ims-db2-mq/cpy/CCPAURQY.cpy:19-36`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:354-379`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 05 | &nbsp;&nbsp;PA-RQ-AUTH-DATE | X(06) | DISPLAY | 1 | 6 | 6 |  |  |  | 19 |
| 05 | &nbsp;&nbsp;PA-RQ-AUTH-TIME | X(06) | DISPLAY | 7 | 12 | 6 |  |  |  | 20 |
| 05 | &nbsp;&nbsp;PA-RQ-CARD-NUM | X(16) | DISPLAY | 13 | 28 | 16 |  |  |  | 21 |
| 05 | &nbsp;&nbsp;PA-RQ-AUTH-TYPE | X(04) | DISPLAY | 29 | 32 | 4 |  |  |  | 22 |
| 05 | &nbsp;&nbsp;PA-RQ-CARD-EXPIRY-DATE | X(04) | DISPLAY | 33 | 36 | 4 |  |  |  | 23 |
| 05 | &nbsp;&nbsp;PA-RQ-MESSAGE-TYPE | X(06) | DISPLAY | 37 | 42 | 6 |  |  |  | 24 |
| 05 | &nbsp;&nbsp;PA-RQ-MESSAGE-SOURCE | X(06) | DISPLAY | 43 | 48 | 6 |  |  |  | 25 |
| 05 | &nbsp;&nbsp;PA-RQ-PROCESSING-CODE | 9(06) | DISPLAY | 49 | 54 | 6 |  |  |  | 26 |
| 05 | &nbsp;&nbsp;PA-RQ-TRANSACTION-AMT | +9(10).99 | DISPLAY | 55 | 68 | 14 |  |  |  | 27 |
| 05 | &nbsp;&nbsp;PA-RQ-MERCHANT-CATAGORY-CODE | X(04) | DISPLAY | 69 | 72 | 4 |  |  |  | 28 |
| 05 | &nbsp;&nbsp;PA-RQ-ACQR-COUNTRY-CODE | X(03) | DISPLAY | 73 | 75 | 3 |  |  |  | 29 |
| 05 | &nbsp;&nbsp;PA-RQ-POS-ENTRY-MODE | 9(02) | DISPLAY | 76 | 77 | 2 |  |  |  | 30 |
| 05 | &nbsp;&nbsp;PA-RQ-MERCHANT-ID | X(15) | DISPLAY | 78 | 92 | 15 |  |  |  | 31 |
| 05 | &nbsp;&nbsp;PA-RQ-MERCHANT-NAME | X(22) | DISPLAY | 93 | 114 | 22 |  |  |  | 32 |
| 05 | &nbsp;&nbsp;PA-RQ-MERCHANT-CITY | X(13) | DISPLAY | 115 | 127 | 13 |  |  |  | 33 |
| 05 | &nbsp;&nbsp;PA-RQ-MERCHANT-STATE | X(02) | DISPLAY | 128 | 129 | 2 |  |  |  | 34 |
| 05 | &nbsp;&nbsp;PA-RQ-MERCHANT-ZIP | X(09) | DISPLAY | 130 | 138 | 9 |  |  |  | 35 |
| 05 | &nbsp;&nbsp;PA-RQ-TRANSACTION-ID | X(15) | DISPLAY | 139 | 153 | 15 |  |  |  | 36 |

## Level-88 conditions

None.

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [COPAUA0C](../../07-programs/COPAUA0C.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:178` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| PA-RQ-AUTH-DATE | 19 | COPAUA0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:356`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:877` |
| PA-RQ-AUTH-TIME | 20 | COPAUA0C (3): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:357`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:662`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:878` |
| PA-RQ-CARD-NUM | 21 | COPAUA0C (4): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:358`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:475`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:660`, ... |
| PA-RQ-AUTH-TYPE | 22 | COPAUA0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:359`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:880` |
| PA-RQ-CARD-EXPIRY-DATE | 23 | COPAUA0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:360`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:881` |
| PA-RQ-MESSAGE-TYPE | 24 | COPAUA0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:361`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:882` |
| PA-RQ-MESSAGE-SOURCE | 25 | COPAUA0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:362`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:883` |
| PA-RQ-PROCESSING-CODE | 26 | COPAUA0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:363`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:884` |
| PA-RQ-TRANSACTION-AMT | 27 | COPAUA0C (4): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:376`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:379`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:694`, ... |
| PA-RQ-MERCHANT-CATAGORY-CODE | 28 | COPAUA0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:365`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:886` |
| PA-RQ-ACQR-COUNTRY-CODE | 29 | COPAUA0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:366`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:888` |
| PA-RQ-POS-ENTRY-MODE | 30 | COPAUA0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:367`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:889` |
| PA-RQ-MERCHANT-ID | 31 | COPAUA0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:368`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:890` |
| PA-RQ-MERCHANT-NAME | 32 | COPAUA0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:369`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:891` |
| PA-RQ-MERCHANT-CITY | 33 | COPAUA0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:370`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:892` |
| PA-RQ-MERCHANT-STATE | 34 | COPAUA0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:371`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:893` |
| PA-RQ-MERCHANT-ZIP | 35 | COPAUA0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:372`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:894` |
| PA-RQ-TRANSACTION-ID | 36 | COPAUA0C (3): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:373`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:661`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:895` |

## Key fields

| Field | Meaning | Source |
|---|---|---|
| PA-RQ-AUTH-DATE | Request date (YYMMDD), stored as PA-AUTH-ORIG-DATE. | `app/app-authorization-ims-db2-mq/cpy/CCPAURQY.cpy:19` |
| PA-RQ-AUTH-TIME | Request time; also echoed as the response auth id code. | `app/app-authorization-ims-db2-mq/cpy/CCPAURQY.cpy:20` |
| PA-RQ-CARD-NUM | Card number used to read the card cross-reference. | `app/app-authorization-ims-db2-mq/cpy/CCPAURQY.cpy:21` |
| PA-RQ-TRANSACTION-AMT | Requested amount, numeric-edited +9(10).99, compared with available credit. | `app/app-authorization-ims-db2-mq/cpy/CCPAURQY.cpy:27` |
| PA-RQ-TRANSACTION-ID | Transaction id echoed in the response. | `app/app-authorization-ims-db2-mq/cpy/CCPAURQY.cpy:36` |

## Observations

- anomaly: PA-RQ-TRANSACTION-AMT is a numeric-edited field (+9(10).99) that receives a COMPUTE result and is then moved to numeric fields; correct but unusual. (`app/app-authorization-ims-db2-mq/cpy/CCPAURQY.cpy:27`)

## Sources

- `app/app-authorization-ims-db2-mq/cpy/CCPAURQY.cpy`
- `docs/_work/structure/copybooks/CCPAURQY.json`
- `docs/_work/layouts/CCPAURQY.json`
- `docs/_work/semantic/copybooks/CCPAURQY.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
