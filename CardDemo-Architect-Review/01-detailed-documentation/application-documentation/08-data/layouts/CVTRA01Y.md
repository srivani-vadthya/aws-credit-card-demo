# Layout CVTRA01Y

| Item | Value |
|---|---|
| Source | `app/cpy/CVTRA01Y.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 13 |
| Data items | 7 (88-levels: 0) |
| Semantic analysis | validated (batch B02) |

## Purpose

CVTRA01Y defines TRAN-CAT-BAL-RECORD, the 50-byte balance per account, transaction type and category. CBTRN02C maintains these balances when posting transactions, and CBACT04C reads them sequentially to compute monthly interest per category using the disclosure group rate. (Confirmed)

Evidence: `app/cpy/CVTRA01Y.cpy:1-10`, `app/cbl/CBACT04C.cbl:187-217`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | TRAN-CAT-BAL-RECORD |  |  | 1 | 50 | 50 |  |  |  | 4 |
| 05 | &nbsp;&nbsp;TRAN-CAT-KEY |  |  | 1 | 17 | 17 |  |  |  | 5 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRANCAT-ACCT-ID | 9(11) | DISPLAY | 1 | 11 | 11 |  |  |  | 6 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRANCAT-TYPE-CD | X(02) | DISPLAY | 12 | 13 | 2 |  |  |  | 7 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRANCAT-CD | 9(04) | DISPLAY | 14 | 17 | 4 |  |  |  | 8 |
| 05 | &nbsp;&nbsp;TRAN-CAT-BAL | S9(09)V99 | DISPLAY | 18 | 28 | 11 |  |  |  | 9 |
| 05 | &nbsp;&nbsp;FILLER | X(22) | DISPLAY | 29 | 50 | 22 |  |  |  | 10 |

## Level-88 conditions

None.

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [CBACT04C](../../07-programs/CBACT04C.md) | cobol-program | COPY | active |  | `app/cbl/CBACT04C.cbl:97` |
| [CBTRN02C](../../07-programs/CBTRN02C.md) | cobol-program | COPY | active |  | `app/cbl/CBTRN02C.cbl:126` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| TRAN-CAT-BAL-RECORD | 4 | CBACT04C (2): `app/cbl/CBACT04C.cbl:193`, `app/cbl/CBACT04C.cbl:326`; CBTRN02C (4): `app/cbl/CBTRN02C.cbl:474`, `app/cbl/CBTRN02C.cbl:504`, `app/cbl/CBTRN02C.cbl:510`, ... |
| TRANCAT-ACCT-ID | 6 | CBACT04C (4): `app/cbl/CBACT04C.cbl:194`, `app/cbl/CBACT04C.cbl:201`, `app/cbl/CBACT04C.cbl:202`, ...; CBTRN02C (1): `app/cbl/CBTRN02C.cbl:505` |
| TRANCAT-TYPE-CD | 7 | CBACT04C (1): `app/cbl/CBACT04C.cbl:212`; CBTRN02C (1): `app/cbl/CBTRN02C.cbl:506` |
| TRANCAT-CD | 8 | CBACT04C (1): `app/cbl/CBACT04C.cbl:211`; CBTRN02C (1): `app/cbl/CBTRN02C.cbl:507` |
| TRAN-CAT-BAL | 9 | CBACT04C (1): `app/cbl/CBACT04C.cbl:465`; CBTRN02C (2): `app/cbl/CBTRN02C.cbl:508`, `app/cbl/CBTRN02C.cbl:527` |

Named in no procedure statement of the copying programs (may still be moved as part of a group): TRAN-CAT-KEY (line 5).

## Key fields

| Field | Meaning | Source |
|---|---|---|
| TRAN-CAT-BAL-RECORD | 50-byte transaction category balance record (comment RECLN 50; field sizes add up to 50). | `app/cpy/CVTRA01Y.cpy:4` |
| TRAN-CAT-KEY | Composite key: account id + transaction type code + category code; CBACT04C processes the file in this order with a control break on account id. | `app/cpy/CVTRA01Y.cpy:5-8` |
| TRANCAT-ACCT-ID | 11-digit account id. | `app/cpy/CVTRA01Y.cpy:6` |
| TRANCAT-TYPE-CD | 2-character transaction type code. | `app/cpy/CVTRA01Y.cpy:7` |
| TRANCAT-CD | 4-digit transaction category code. | `app/cpy/CVTRA01Y.cpy:8` |
| TRAN-CAT-BAL | Signed balance S9(09)V99 accumulated for the account/type/category; the base for monthly interest in CBACT04C. | `app/cpy/CVTRA01Y.cpy:9` |

## Sources

- `app/cpy/CVTRA01Y.cpy`
- `docs/_work/structure/copybooks/CVTRA01Y.json`
- `docs/_work/layouts/CVTRA01Y.json`
- `docs/_work/semantic/copybooks/CVTRA01Y.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
