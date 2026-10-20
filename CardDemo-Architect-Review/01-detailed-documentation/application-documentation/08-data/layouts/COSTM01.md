# Layout COSTM01

| Item | Value |
|---|---|
| Source | `app/cpy/COSTM01.CPY` |
| Type | cobol-copybook |
| Content | data |
| Lines | 38 |
| Data items | 17 (88-levels: 0) |
| Semantic analysis | validated (batch B02) |

## Purpose

COSTM01 defines TRNX-RECORD, a 350-byte transaction layout re-ordered for reporting, with a composite key of card number plus transaction id. It is used by the statement program CBSTM03A to receive records read from TRNXFILE (via CBSTM03B), load them into its per-card transaction table and print description and amount on statements. (Confirmed)

Evidence: `app/cpy/COSTM01.CPY:1-3`, `app/cpy/COSTM01.CPY:20-36`, `app/cbl/CBSTM03A.CBL:51`, `app/cbl/CBSTM03B.CBL:58-63`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | TRNX-RECORD |  |  | 1 | 350 | 350 |  |  |  | 20 |
| 05 | &nbsp;&nbsp;TRNX-KEY |  |  | 1 | 32 | 32 |  |  |  | 21 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRNX-CARD-NUM | X(16) | DISPLAY | 1 | 16 | 16 |  |  |  | 22 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRNX-ID | X(16) | DISPLAY | 17 | 32 | 16 |  |  |  | 23 |
| 05 | &nbsp;&nbsp;TRNX-REST |  |  | 33 | 350 | 318 |  |  |  | 24 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRNX-TYPE-CD | X(02) | DISPLAY | 33 | 34 | 2 |  |  |  | 25 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRNX-CAT-CD | 9(04) | DISPLAY | 35 | 38 | 4 |  |  |  | 26 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRNX-SOURCE | X(10) | DISPLAY | 39 | 48 | 10 |  |  |  | 27 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRNX-DESC | X(100) | DISPLAY | 49 | 148 | 100 |  |  |  | 28 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRNX-AMT | S9(09)V99 | DISPLAY | 149 | 159 | 11 |  |  |  | 29 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRNX-MERCHANT-ID | 9(09) | DISPLAY | 160 | 168 | 9 |  |  |  | 30 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRNX-MERCHANT-NAME | X(50) | DISPLAY | 169 | 218 | 50 |  |  |  | 31 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRNX-MERCHANT-CITY | X(50) | DISPLAY | 219 | 268 | 50 |  |  |  | 32 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRNX-MERCHANT-ZIP | X(10) | DISPLAY | 269 | 278 | 10 |  |  |  | 33 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRNX-ORIG-TS | X(26) | DISPLAY | 279 | 304 | 26 |  |  |  | 34 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRNX-PROC-TS | X(26) | DISPLAY | 305 | 330 | 26 |  |  |  | 35 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(20) | DISPLAY | 331 | 350 | 20 |  |  |  | 36 |

## Level-88 conditions

None.

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [CBSTM03A](../../07-programs/CBSTM03A.md) | cobol-program | COPY | active |  | `app/cbl/CBSTM03A.CBL:51` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| TRNX-RECORD | 20 | CBSTM03A (2): `app/cbl/CBSTM03A.CBL:756`, `app/cbl/CBSTM03A.CBL:839` |
| TRNX-CARD-NUM | 22 | CBSTM03A (5): `app/cbl/CBSTM03A.CBL:421`, `app/cbl/CBSTM03A.CBL:757`, `app/cbl/CBSTM03A.CBL:819`, ... |
| TRNX-ID | 23 | CBSTM03A (3): `app/cbl/CBSTM03A.CBL:425`, `app/cbl/CBSTM03A.CBL:676`, `app/cbl/CBSTM03A.CBL:828` |
| TRNX-REST | 24 | CBSTM03A (2): `app/cbl/CBSTM03A.CBL:427`, `app/cbl/CBSTM03A.CBL:829` |
| TRNX-DESC | 28 | CBSTM03A (1): `app/cbl/CBSTM03A.CBL:677` |
| TRNX-AMT | 29 | CBSTM03A (2): `app/cbl/CBSTM03A.CBL:429`, `app/cbl/CBSTM03A.CBL:678` |

Named in no procedure statement of the copying programs (may still be moved as part of a group): TRNX-KEY (line 21), TRNX-TYPE-CD (line 25), TRNX-CAT-CD (line 26), TRNX-SOURCE (line 27), TRNX-MERCHANT-ID (line 30), TRNX-MERCHANT-NAME (line 31), TRNX-MERCHANT-CITY (line 32), TRNX-MERCHANT-ZIP (line 33), TRNX-ORIG-TS (line 34), TRNX-PROC-TS (line 35).

## Key fields

| Field | Meaning | Source |
|---|---|---|
| TRNX-KEY | 32-byte composite key: card number followed by transaction id; matches the TRNXFILE record key FD-TRNXS-ID in CBSTM03B, so records are ordered by card number. | `app/cpy/COSTM01.CPY:21-23` |
| TRNX-CARD-NUM | Card number the transaction belongs to; used by CBSTM03A to group transactions per card. | `app/cpy/COSTM01.CPY:22` |
| TRNX-ID | 16-byte transaction identifier. | `app/cpy/COSTM01.CPY:23` |
| TRNX-REST | Remaining 318 bytes of transaction data (type, category, source, description, amount, merchant, timestamps), stored as a block in the CBSTM03A transaction table. | `app/cpy/COSTM01.CPY:24-36` |
| TRNX-DESC | Transaction description printed on the statement detail line. | `app/cpy/COSTM01.CPY:28` |
| TRNX-AMT | Signed transaction amount S9(09)V99, printed and summed into the statement total. | `app/cpy/COSTM01.CPY:29` |

## Observations

- anomaly: Same 350-byte content as CVTRA05Y but with the card number moved to the front as part of the key ('Transaction altered Layout for use in reporting'); the two layouts are not interchangeable byte-for-byte. (`app/cpy/COSTM01.CPY:2`)

## Sources

- `app/cpy/COSTM01.CPY`
- `docs/_work/structure/copybooks/COSTM01.json`
- `docs/_work/layouts/COSTM01.json`
- `docs/_work/semantic/copybooks/COSTM01.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
