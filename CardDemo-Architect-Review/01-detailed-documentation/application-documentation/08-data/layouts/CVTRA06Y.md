# Layout CVTRA06Y

| Item | Value |
|---|---|
| Source | `app/cpy/CVTRA06Y.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 21 |
| Data items | 15 (88-levels: 0) |
| Semantic analysis | validated (batch B02) |

## Purpose

CVTRA06Y defines DALYTRAN-RECORD, the 350-byte daily transaction input record with the same fields as the posted transaction (CVTRA05Y). It is read from the sequential DALYTRAN file by CBTRN01C (verification) and CBTRN02C (posting). (Confirmed)

Evidence: `app/cpy/CVTRA06Y.cpy:1-18`, `app/cbl/CBTRN01C.cbl:170-183`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | DALYTRAN-RECORD |  |  | 1 | 350 | 350 |  |  |  | 4 |
| 05 | &nbsp;&nbsp;DALYTRAN-ID | X(16) | DISPLAY | 1 | 16 | 16 |  |  |  | 5 |
| 05 | &nbsp;&nbsp;DALYTRAN-TYPE-CD | X(02) | DISPLAY | 17 | 18 | 2 |  |  |  | 6 |
| 05 | &nbsp;&nbsp;DALYTRAN-CAT-CD | 9(04) | DISPLAY | 19 | 22 | 4 |  |  |  | 7 |
| 05 | &nbsp;&nbsp;DALYTRAN-SOURCE | X(10) | DISPLAY | 23 | 32 | 10 |  |  |  | 8 |
| 05 | &nbsp;&nbsp;DALYTRAN-DESC | X(100) | DISPLAY | 33 | 132 | 100 |  |  |  | 9 |
| 05 | &nbsp;&nbsp;DALYTRAN-AMT | S9(09)V99 | DISPLAY | 133 | 143 | 11 |  |  |  | 10 |
| 05 | &nbsp;&nbsp;DALYTRAN-MERCHANT-ID | 9(09) | DISPLAY | 144 | 152 | 9 |  |  |  | 11 |
| 05 | &nbsp;&nbsp;DALYTRAN-MERCHANT-NAME | X(50) | DISPLAY | 153 | 202 | 50 |  |  |  | 12 |
| 05 | &nbsp;&nbsp;DALYTRAN-MERCHANT-CITY | X(50) | DISPLAY | 203 | 252 | 50 |  |  |  | 13 |
| 05 | &nbsp;&nbsp;DALYTRAN-MERCHANT-ZIP | X(10) | DISPLAY | 253 | 262 | 10 |  |  |  | 14 |
| 05 | &nbsp;&nbsp;DALYTRAN-CARD-NUM | X(16) | DISPLAY | 263 | 278 | 16 |  |  |  | 15 |
| 05 | &nbsp;&nbsp;DALYTRAN-ORIG-TS | X(26) | DISPLAY | 279 | 304 | 26 |  |  |  | 16 |
| 05 | &nbsp;&nbsp;DALYTRAN-PROC-TS | X(26) | DISPLAY | 305 | 330 | 26 |  |  |  | 17 |
| 05 | &nbsp;&nbsp;FILLER | X(20) | DISPLAY | 331 | 350 | 20 |  |  |  | 18 |

## Level-88 conditions

None.

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [CBTRN01C](../../07-programs/CBTRN01C.md) | cobol-program | COPY | active |  | `app/cbl/CBTRN01C.cbl:99` |
| [CBTRN02C](../../07-programs/CBTRN02C.md) | cobol-program | COPY | active |  | `app/cbl/CBTRN02C.cbl:102` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| DALYTRAN-RECORD | 4 | CBTRN01C (2): `app/cbl/CBTRN01C.cbl:168`, `app/cbl/CBTRN01C.cbl:203`; CBTRN02C (2): `app/cbl/CBTRN02C.cbl:346`, `app/cbl/CBTRN02C.cbl:447` |
| DALYTRAN-ID | 5 | CBTRN01C (1): `app/cbl/CBTRN01C.cbl:183`; CBTRN02C (1): `app/cbl/CBTRN02C.cbl:425` |
| DALYTRAN-TYPE-CD | 6 | CBTRN02C (3): `app/cbl/CBTRN02C.cbl:426`, `app/cbl/CBTRN02C.cbl:470`, `app/cbl/CBTRN02C.cbl:506` |
| DALYTRAN-CAT-CD | 7 | CBTRN02C (3): `app/cbl/CBTRN02C.cbl:427`, `app/cbl/CBTRN02C.cbl:471`, `app/cbl/CBTRN02C.cbl:507` |
| DALYTRAN-SOURCE | 8 | CBTRN02C (1): `app/cbl/CBTRN02C.cbl:428` |
| DALYTRAN-DESC | 9 | CBTRN02C (1): `app/cbl/CBTRN02C.cbl:429` |
| DALYTRAN-AMT | 10 | CBTRN02C (8): `app/cbl/CBTRN02C.cbl:405`, `app/cbl/CBTRN02C.cbl:430`, `app/cbl/CBTRN02C.cbl:508`, ... |
| DALYTRAN-MERCHANT-ID | 11 | CBTRN02C (1): `app/cbl/CBTRN02C.cbl:431` |
| DALYTRAN-MERCHANT-NAME | 12 | CBTRN02C (1): `app/cbl/CBTRN02C.cbl:432` |
| DALYTRAN-MERCHANT-CITY | 13 | CBTRN02C (1): `app/cbl/CBTRN02C.cbl:433` |
| DALYTRAN-MERCHANT-ZIP | 14 | CBTRN02C (1): `app/cbl/CBTRN02C.cbl:434` |
| DALYTRAN-CARD-NUM | 15 | CBTRN01C (2): `app/cbl/CBTRN01C.cbl:171`, `app/cbl/CBTRN01C.cbl:181`; CBTRN02C (2): `app/cbl/CBTRN02C.cbl:382`, `app/cbl/CBTRN02C.cbl:435` |
| DALYTRAN-ORIG-TS | 16 | CBTRN02C (2): `app/cbl/CBTRN02C.cbl:414`, `app/cbl/CBTRN02C.cbl:436` |

Named in no procedure statement of the copying programs (may still be moved as part of a group): DALYTRAN-PROC-TS (line 17).

## Key fields

| Field | Meaning | Source |
|---|---|---|
| DALYTRAN-RECORD | 350-byte daily (unposted) transaction record (comment RECLN 350; field sizes add up to 350). | `app/cpy/CVTRA06Y.cpy:4` |
| DALYTRAN-ID | 16-byte transaction id. | `app/cpy/CVTRA06Y.cpy:5` |
| DALYTRAN-TYPE-CD | 2-character transaction type code. | `app/cpy/CVTRA06Y.cpy:6` |
| DALYTRAN-CAT-CD | 4-digit transaction category code. | `app/cpy/CVTRA06Y.cpy:7` |
| DALYTRAN-AMT | Signed amount S9(09)V99. | `app/cpy/CVTRA06Y.cpy:10` |
| DALYTRAN-CARD-NUM | Card number; CBTRN01C verifies it against the card cross-reference. | `app/cpy/CVTRA06Y.cpy:15` |
| DALYTRAN-ORIG-TS | 26-byte origination timestamp. | `app/cpy/CVTRA06Y.cpy:16` |

## Observations

- anomaly: Field-for-field identical to CVTRA05Y apart from the DALYTRAN- prefix; the daily and posted transaction layouts are maintained as two separate copybooks. (`app/cpy/CVTRA06Y.cpy:4-18`)

## Sources

- `app/cpy/CVTRA06Y.cpy`
- `docs/_work/structure/copybooks/CVTRA06Y.json`
- `docs/_work/layouts/CVTRA06Y.json`
- `docs/_work/semantic/copybooks/CVTRA06Y.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
