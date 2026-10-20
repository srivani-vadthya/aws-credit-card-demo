# Layout CVTRA04Y

| Item | Value |
|---|---|
| Source | `app/cpy/CVTRA04Y.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 12 |
| Data items | 6 (88-levels: 0) |
| Semantic analysis | validated (batch B03) |

## Purpose

CVTRA04Y defines TRAN-CAT-RECORD, the 60-byte transaction category reference record (header comment states RECLN = 60, matching PIC sizes 2 + 4 + 50 + 4). Its key TRAN-CAT-KEY combines the 2-character transaction type code and the 4-digit category code, and it carries a 50-character category description. In the application source it is copied only by CBTRN03C, which reads the TRANCATG KSDS by type + category to print the category description and abends if the key is not found. (Confirmed)

Evidence: `app/cpy/CVTRA04Y.cpy:1-9`, `app/cbl/CBTRN03C.cbl:108`, `app/cbl/CBTRN03C.cbl:191-194`, `app/cbl/CBTRN03C.cbl:504-512`, `app/cbl/CBTRN03C.cbl:368`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | TRAN-CAT-RECORD |  |  | 1 | 60 | 60 |  |  |  | 4 |
| 05 | &nbsp;&nbsp;TRAN-CAT-KEY |  |  | 1 | 6 | 6 |  |  |  | 5 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRAN-TYPE-CD | X(02) | DISPLAY | 1 | 2 | 2 |  |  |  | 6 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRAN-CAT-CD | 9(04) | DISPLAY | 3 | 6 | 4 |  |  |  | 7 |
| 05 | &nbsp;&nbsp;TRAN-CAT-TYPE-DESC | X(50) | DISPLAY | 7 | 56 | 50 |  |  |  | 8 |
| 05 | &nbsp;&nbsp;FILLER | X(04) | DISPLAY | 57 | 60 | 4 |  |  |  | 9 |

## Level-88 conditions

None.

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [CBTRN03C](../../07-programs/CBTRN03C.md) | cobol-program | COPY | active |  | `app/cbl/CBTRN03C.cbl:108` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| TRAN-CAT-RECORD | 4 | CBTRN03C (1): `app/cbl/CBTRN03C.cbl:505` |
| TRAN-TYPE-CD | 6 | CBTRN03C (3): `app/cbl/CBTRN03C.cbl:189`, `app/cbl/CBTRN03C.cbl:191`, `app/cbl/CBTRN03C.cbl:365` |
| TRAN-CAT-CD | 7 | CBTRN03C (2): `app/cbl/CBTRN03C.cbl:193`, `app/cbl/CBTRN03C.cbl:367` |
| TRAN-CAT-TYPE-DESC | 8 | CBTRN03C (1): `app/cbl/CBTRN03C.cbl:368` |

Named in no procedure statement of the copying programs (may still be moved as part of a group): TRAN-CAT-KEY (line 5).

## Key fields

| Field | Meaning | Source |
|---|---|---|
| TRAN-CAT-RECORD | 60-byte transaction category reference record (6-byte key + 50 + 4 bytes); CBTRN03C reads the TRANCATG KSDS into it. | `app/cpy/CVTRA04Y.cpy:4` |
| TRAN-CAT-KEY | Composite record key: transaction type code followed by category code. | `app/cpy/CVTRA04Y.cpy:5` |
| TRAN-TYPE-CD | 2-character transaction type code, first part of the category key (same code as TRAN-TYPE in CVTRA03Y). | `app/cpy/CVTRA04Y.cpy:6` |
| TRAN-CAT-CD | 4-digit numeric transaction category code within the type, second part of the key. | `app/cpy/CVTRA04Y.cpy:7` |
| TRAN-CAT-TYPE-DESC | 50-character description of the type/category combination; printed (truncated to 29 characters) in the transaction report detail line. | `app/cpy/CVTRA04Y.cpy:8` |

## Observations

- anomaly: TRAN-TYPE-CD and TRAN-CAT-CD have the same names as fields of TRAN-RECORD in CVTRA05Y, so CBTRN03C, which copies both members, must qualify them with OF TRAN-RECORD / OF FD-TRAN-CAT-KEY. Confirmed. (`app/cbl/CBTRN03C.cbl:189-194`)
- anomaly: The 50-character TRAN-CAT-TYPE-DESC is moved into the 29-character TRAN-REPORT-CAT-DESC, truncating category descriptions on the report. (`app/cbl/CBTRN03C.cbl:368`)

## Sources

- `app/cpy/CVTRA04Y.cpy`
- `docs/_work/structure/copybooks/CVTRA04Y.json`
- `docs/_work/layouts/CVTRA04Y.json`
- `docs/_work/semantic/copybooks/CVTRA04Y.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
