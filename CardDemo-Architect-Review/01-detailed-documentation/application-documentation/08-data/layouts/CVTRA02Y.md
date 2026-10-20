# Layout CVTRA02Y

| Item | Value |
|---|---|
| Source | `app/cpy/CVTRA02Y.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 13 |
| Data items | 7 (88-levels: 0) |
| Semantic analysis | validated (batch B02) |

## Purpose

CVTRA02Y defines DIS-GROUP-RECORD, the 50-byte disclosure group (interest rate) table keyed by account group, transaction type and transaction category. Its only user in the repository is CBACT04C, which looks up DIS-INT-RATE for each transaction category balance and skips interest when the rate is zero. (Confirmed)

Evidence: `app/cpy/CVTRA02Y.cpy:1-10`, `app/cbl/CBACT04C.cbl:415-440`, `app/cbl/CBACT04C.cbl:464-465`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | DIS-GROUP-RECORD |  |  | 1 | 50 | 50 |  |  |  | 4 |
| 05 | &nbsp;&nbsp;DIS-GROUP-KEY |  |  | 1 | 16 | 16 |  |  |  | 5 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;DIS-ACCT-GROUP-ID | X(10) | DISPLAY | 1 | 10 | 10 |  |  |  | 6 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;DIS-TRAN-TYPE-CD | X(02) | DISPLAY | 11 | 12 | 2 |  |  |  | 7 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;DIS-TRAN-CAT-CD | 9(04) | DISPLAY | 13 | 16 | 4 |  |  |  | 8 |
| 05 | &nbsp;&nbsp;DIS-INT-RATE | S9(04)V99 | DISPLAY | 17 | 22 | 6 |  |  |  | 9 |
| 05 | &nbsp;&nbsp;FILLER | X(28) | DISPLAY | 23 | 50 | 28 |  |  |  | 10 |

## Level-88 conditions

None.

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [CBACT04C](../../07-programs/CBACT04C.md) | cobol-program | COPY | active |  | `app/cbl/CBACT04C.cbl:107` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| DIS-GROUP-RECORD | 4 | CBACT04C (2): `app/cbl/CBACT04C.cbl:416`, `app/cbl/CBACT04C.cbl:444` |
| DIS-INT-RATE | 9 | CBACT04C (2): `app/cbl/CBACT04C.cbl:214`, `app/cbl/CBACT04C.cbl:465` |

Named in no procedure statement of the copying programs (may still be moved as part of a group): DIS-GROUP-KEY (line 5), DIS-ACCT-GROUP-ID (line 6), DIS-TRAN-TYPE-CD (line 7), DIS-TRAN-CAT-CD (line 8).

## Key fields

| Field | Meaning | Source |
|---|---|---|
| DIS-GROUP-RECORD | 50-byte disclosure group record (comment RECLN 50; field sizes add up to 50). | `app/cpy/CVTRA02Y.cpy:4` |
| DIS-GROUP-KEY | Composite key: account group id + transaction type code + category code. CBACT04C falls back to group id 'DEFAULT' when the account's group is not found. | `app/cpy/CVTRA02Y.cpy:5-8` |
| DIS-ACCT-GROUP-ID | 10-byte account group id, matching ACCT-GROUP-ID in CVACT01Y. | `app/cpy/CVTRA02Y.cpy:6` |
| DIS-INT-RATE | Signed interest rate S9(04)V99. CBACT04C divides balance x rate by 1200, which implies an annual percentage rate (Inferred from the formula). | `app/cpy/CVTRA02Y.cpy:9` |

## Sources

- `app/cpy/CVTRA02Y.cpy`
- `docs/_work/structure/copybooks/CVTRA02Y.json`
- `docs/_work/layouts/CVTRA02Y.json`
- `docs/_work/semantic/copybooks/CVTRA02Y.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
