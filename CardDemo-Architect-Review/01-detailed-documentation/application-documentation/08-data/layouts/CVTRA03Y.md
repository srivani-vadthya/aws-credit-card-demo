# Layout CVTRA03Y

| Item | Value |
|---|---|
| Source | `app/cpy/CVTRA03Y.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 10 |
| Data items | 4 (88-levels: 0) |
| Semantic analysis | validated (batch B03) |

## Purpose

CVTRA03Y defines TRAN-TYPE-RECORD, the 60-byte transaction type reference record (header comment states RECLN = 60, which matches the PIC sizes 2 + 50 + 8). It maps a 2-character transaction type code to a 50-character description. In the application source it is copied only by the batch report program CBTRN03C, which reads the TRANTYPE KSDS by type code to print the type description and abends if the type is not found. (Confirmed)

Evidence: `app/cpy/CVTRA03Y.cpy:1-7`, `app/cbl/CBTRN03C.cbl:103`, `app/cbl/CBTRN03C.cbl:494-502`, `app/cbl/CBTRN03C.cbl:366`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | TRAN-TYPE-RECORD |  |  | 1 | 60 | 60 |  |  |  | 4 |
| 05 | &nbsp;&nbsp;TRAN-TYPE | X(02) | DISPLAY | 1 | 2 | 2 |  |  |  | 5 |
| 05 | &nbsp;&nbsp;TRAN-TYPE-DESC | X(50) | DISPLAY | 3 | 52 | 50 |  |  |  | 6 |
| 05 | &nbsp;&nbsp;FILLER | X(08) | DISPLAY | 53 | 60 | 8 |  |  |  | 7 |

## Level-88 conditions

None.

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [CBTRN03C](../../07-programs/CBTRN03C.md) | cobol-program | COPY | active |  | `app/cbl/CBTRN03C.cbl:103` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| TRAN-TYPE-RECORD | 4 | CBTRN03C (1): `app/cbl/CBTRN03C.cbl:495` |
| TRAN-TYPE-DESC | 6 | CBTRN03C (1): `app/cbl/CBTRN03C.cbl:366` |

Named in no procedure statement of the copying programs (may still be moved as part of a group): TRAN-TYPE (line 5).

## Key fields

| Field | Meaning | Source |
|---|---|---|
| TRAN-TYPE-RECORD | 60-byte transaction type reference record (2 + 50 + 8 bytes); CBTRN03C reads the TRANTYPE KSDS into it. | `app/cpy/CVTRA03Y.cpy:4` |
| TRAN-TYPE | 2-character transaction type code; the record key (CBTRN03C keys TRANTYPE-FILE by FD-TRAN-TYPE in the same position). | `app/cpy/CVTRA03Y.cpy:5` |
| TRAN-TYPE-DESC | 50-character description of the transaction type; printed (truncated to 15 characters) in the transaction report detail line. | `app/cpy/CVTRA03Y.cpy:6` |

## Observations

- anomaly: Only CBTRN03C copies this member in the application source; the 50-character TRAN-TYPE-DESC is moved into the 15-character TRAN-REPORT-TYPE-DESC, so descriptions are truncated on the report. (`app/cbl/CBTRN03C.cbl:366`)

## Sources

- `app/cpy/CVTRA03Y.cpy`
- `docs/_work/structure/copybooks/CVTRA03Y.json`
- `docs/_work/layouts/CVTRA03Y.json`
- `docs/_work/semantic/copybooks/CVTRA03Y.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
