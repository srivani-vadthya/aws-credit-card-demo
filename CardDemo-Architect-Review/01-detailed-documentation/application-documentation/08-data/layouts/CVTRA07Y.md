# Layout CVTRA07Y

| Item | Value |
|---|---|
| Source | `app/cpy/CVTRA07Y.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 73 |
| Data items | 45 (88-levels: 0) |
| Semantic analysis | validated (batch B03) |

## Purpose

CVTRA07Y defines the print-line layouts of the Daily Transaction Report (DALYREPT): the title line with the date range, the column heading and dashed separator lines, the transaction detail line, and the page, account and grand total lines with edited amounts. It contains no record read from a file; it is working storage moved into the 133-byte report record. In the application source it is copied only by CBTRN03C, which fills the date range, detail and total fields and writes the lines to the TRANREPT dataset. (Confirmed)

Evidence: `app/cpy/CVTRA07Y.cpy:1-66`, `app/cbl/CBTRN03C.cbl:113`, `app/cbl/CBTRN03C.cbl:293-341`, `app/cbl/CBTRN03C.cbl:361-374`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | REPORT-NAME-HEADER |  |  | 1 | 115 | 115 |  |  |  | 4 |
| 05 | &nbsp;&nbsp;REPT-SHORT-NAME | X(38) | DISPLAY | 1 | 38 | 38 |  |  | 'DALYREPT' | 5 |
| 05 | &nbsp;&nbsp;REPT-LONG-NAME | X(41) | DISPLAY | 39 | 79 | 41 |  |  | 'Daily Transaction Report' | 7 |
| 05 | &nbsp;&nbsp;REPT-DATE-HEADER | X(12) | DISPLAY | 80 | 91 | 12 |  |  | 'Date Range: ' | 9 |
| 05 | &nbsp;&nbsp;REPT-START-DATE | X(10) | DISPLAY | 92 | 101 | 10 |  |  | SPACES | 11 |
| 05 | &nbsp;&nbsp;FILLER | X(04) | DISPLAY | 102 | 105 | 4 |  |  | ' to ' | 12 |
| 05 | &nbsp;&nbsp;REPT-END-DATE | X(10) | DISPLAY | 106 | 115 | 10 |  |  | SPACES | 13 |
| 01 | TRANSACTION-DETAIL-REPORT |  |  | 1 | 114 | 114 |  |  |  | 15 |
| 05 | &nbsp;&nbsp;TRAN-REPORT-TRANS-ID | X(16) | DISPLAY | 1 | 16 | 16 |  |  |  | 16 |
| 05 | &nbsp;&nbsp;FILLER | X(01) | DISPLAY | 17 | 17 | 1 |  |  | SPACES | 17 |
| 05 | &nbsp;&nbsp;TRAN-REPORT-ACCOUNT-ID | X(11) | DISPLAY | 18 | 28 | 11 |  |  |  | 18 |
| 05 | &nbsp;&nbsp;FILLER | X(01) | DISPLAY | 29 | 29 | 1 |  |  | SPACES | 19 |
| 05 | &nbsp;&nbsp;TRAN-REPORT-TYPE-CD | X(02) | DISPLAY | 30 | 31 | 2 |  |  |  | 20 |
| 05 | &nbsp;&nbsp;FILLER | X(01) | DISPLAY | 32 | 32 | 1 |  |  | '-' | 21 |
| 05 | &nbsp;&nbsp;TRAN-REPORT-TYPE-DESC | X(15) | DISPLAY | 33 | 47 | 15 |  |  |  | 22 |
| 05 | &nbsp;&nbsp;FILLER | X(01) | DISPLAY | 48 | 48 | 1 |  |  | SPACES | 23 |
| 05 | &nbsp;&nbsp;TRAN-REPORT-CAT-CD | 9(04) | DISPLAY | 49 | 52 | 4 |  |  |  | 24 |
| 05 | &nbsp;&nbsp;FILLER | X(01) | DISPLAY | 53 | 53 | 1 |  |  | '-' | 25 |
| 05 | &nbsp;&nbsp;TRAN-REPORT-CAT-DESC | X(29) | DISPLAY | 54 | 82 | 29 |  |  |  | 26 |
| 05 | &nbsp;&nbsp;FILLER | X(01) | DISPLAY | 83 | 83 | 1 |  |  | SPACES | 27 |
| 05 | &nbsp;&nbsp;TRAN-REPORT-SOURCE | X(10) | DISPLAY | 84 | 93 | 10 |  |  |  | 28 |
| 05 | &nbsp;&nbsp;FILLER | X(04) | DISPLAY | 94 | 97 | 4 |  |  | SPACES | 29 |
| 05 | &nbsp;&nbsp;TRAN-REPORT-AMT | -ZZZ,ZZZ,ZZZ.ZZ | DISPLAY | 98 | 112 | 15 |  |  |  | 30 |
| 05 | &nbsp;&nbsp;FILLER | X(02) | DISPLAY | 113 | 114 | 2 |  |  | SPACES | 31 |
| 01 | TRANSACTION-HEADER-1 |  |  | 1 | 114 | 114 |  |  |  | 33 |
| 05 | &nbsp;&nbsp;FILLER | X(17) | DISPLAY | 1 | 17 | 17 |  |  | 'Transaction ID' | 34 |
| 05 | &nbsp;&nbsp;FILLER | X(12) | DISPLAY | 18 | 29 | 12 |  |  | 'Account ID' | 36 |
| 05 | &nbsp;&nbsp;FILLER | X(19) | DISPLAY | 30 | 48 | 19 |  |  | 'Transaction Type' | 38 |
| 05 | &nbsp;&nbsp;FILLER | X(35) | DISPLAY | 49 | 83 | 35 |  |  | 'Tran Category' | 40 |
| 05 | &nbsp;&nbsp;FILLER | X(14) | DISPLAY | 84 | 97 | 14 |  |  | 'Tran Source' | 42 |
| 05 | &nbsp;&nbsp;FILLER | X | DISPLAY | 98 | 98 | 1 |  |  | SPACES | 44 |
| 05 | &nbsp;&nbsp;FILLER | X(16) | DISPLAY | 99 | 114 | 16 |  |  | ' Amount' | 45 |
| 01 | TRANSACTION-HEADER-2 | X(133) | DISPLAY | 1 | 133 | 133 |  |  | ALL '-' | 48 |
| 01 | REPORT-PAGE-TOTALS |  |  | 1 | 112 | 112 |  |  |  | 50 |
| 05 | &nbsp;&nbsp;FILLER | X(11) | DISPLAY | 1 | 11 | 11 |  |  | 'Page Total' | 51 |
| 05 | &nbsp;&nbsp;FILLER | X(86) | DISPLAY | 12 | 97 | 86 |  |  | ALL '.' | 53 |
| 05 | &nbsp;&nbsp;REPT-PAGE-TOTAL | +ZZZ,ZZZ,ZZZ.ZZ | DISPLAY | 98 | 112 | 15 |  |  |  | 54 |
| 01 | REPORT-ACCOUNT-TOTALS |  |  | 1 | 112 | 112 |  |  |  | 56 |
| 05 | &nbsp;&nbsp;FILLER | X(13) | DISPLAY | 1 | 13 | 13 |  |  | 'Account Total' | 57 |
| 05 | &nbsp;&nbsp;FILLER | X(84) | DISPLAY | 14 | 97 | 84 |  |  | ALL '.' | 59 |
| 05 | &nbsp;&nbsp;REPT-ACCOUNT-TOTAL | +ZZZ,ZZZ,ZZZ.ZZ | DISPLAY | 98 | 112 | 15 |  |  |  | 60 |
| 01 | REPORT-GRAND-TOTALS |  |  | 1 | 112 | 112 |  |  |  | 62 |
| 05 | &nbsp;&nbsp;FILLER | X(11) | DISPLAY | 1 | 11 | 11 |  |  | 'Grand Total' | 63 |
| 05 | &nbsp;&nbsp;FILLER | X(86) | DISPLAY | 12 | 97 | 86 |  |  | ALL '.' | 65 |
| 05 | &nbsp;&nbsp;REPT-GRAND-TOTAL | +ZZZ,ZZZ,ZZZ.ZZ | DISPLAY | 98 | 112 | 15 |  |  |  | 66 |

## Level-88 conditions

None.

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [CBTRN03C](../../07-programs/CBTRN03C.md) | cobol-program | COPY | active |  | `app/cbl/CBTRN03C.cbl:113` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| REPORT-NAME-HEADER | 4 | CBTRN03C (1): `app/cbl/CBTRN03C.cbl:325` |
| REPT-START-DATE | 11 | CBTRN03C (1): `app/cbl/CBTRN03C.cbl:277` |
| REPT-END-DATE | 13 | CBTRN03C (1): `app/cbl/CBTRN03C.cbl:278` |
| TRANSACTION-DETAIL-REPORT | 15 | CBTRN03C (2): `app/cbl/CBTRN03C.cbl:362`, `app/cbl/CBTRN03C.cbl:371` |
| TRAN-REPORT-TRANS-ID | 16 | CBTRN03C (1): `app/cbl/CBTRN03C.cbl:363` |
| TRAN-REPORT-ACCOUNT-ID | 18 | CBTRN03C (1): `app/cbl/CBTRN03C.cbl:364` |
| TRAN-REPORT-TYPE-CD | 20 | CBTRN03C (1): `app/cbl/CBTRN03C.cbl:365` |
| TRAN-REPORT-TYPE-DESC | 22 | CBTRN03C (1): `app/cbl/CBTRN03C.cbl:366` |
| TRAN-REPORT-CAT-CD | 24 | CBTRN03C (1): `app/cbl/CBTRN03C.cbl:367` |
| TRAN-REPORT-CAT-DESC | 26 | CBTRN03C (1): `app/cbl/CBTRN03C.cbl:368` |
| TRAN-REPORT-SOURCE | 28 | CBTRN03C (1): `app/cbl/CBTRN03C.cbl:369` |
| TRAN-REPORT-AMT | 30 | CBTRN03C (1): `app/cbl/CBTRN03C.cbl:370` |
| TRANSACTION-HEADER-1 | 33 | CBTRN03C (1): `app/cbl/CBTRN03C.cbl:333` |
| TRANSACTION-HEADER-2 | 48 | CBTRN03C (3): `app/cbl/CBTRN03C.cbl:300`, `app/cbl/CBTRN03C.cbl:312`, `app/cbl/CBTRN03C.cbl:337` |
| REPORT-PAGE-TOTALS | 50 | CBTRN03C (1): `app/cbl/CBTRN03C.cbl:295` |
| REPT-PAGE-TOTAL | 54 | CBTRN03C (1): `app/cbl/CBTRN03C.cbl:294` |
| REPORT-ACCOUNT-TOTALS | 56 | CBTRN03C (1): `app/cbl/CBTRN03C.cbl:308` |
| REPT-ACCOUNT-TOTAL | 60 | CBTRN03C (1): `app/cbl/CBTRN03C.cbl:307` |
| REPORT-GRAND-TOTALS | 62 | CBTRN03C (1): `app/cbl/CBTRN03C.cbl:320` |
| REPT-GRAND-TOTAL | 66 | CBTRN03C (1): `app/cbl/CBTRN03C.cbl:319` |

Named in no procedure statement of the copying programs (may still be moved as part of a group): REPT-SHORT-NAME (line 5), REPT-LONG-NAME (line 7), REPT-DATE-HEADER (line 9).

## Key fields

| Field | Meaning | Source |
|---|---|---|
| REPORT-NAME-HEADER | Report title line: short name 'DALYREPT', long name 'Daily Transaction Report' and 'Date Range: <start> to <end>'. | `app/cpy/CVTRA07Y.cpy:4-13` |
| REPT-START-DATE | 10-character report start date, filled by CBTRN03C from the DATEPARM start date. | `app/cpy/CVTRA07Y.cpy:11` |
| REPT-END-DATE | 10-character report end date, filled from the DATEPARM end date. | `app/cpy/CVTRA07Y.cpy:13` |
| TRANSACTION-DETAIL-REPORT | 114-byte detail line: transaction id, account id, type code-description, category code-description, source and edited amount. | `app/cpy/CVTRA07Y.cpy:15-31` |
| TRAN-REPORT-TYPE-DESC | 15-character transaction type description column (source description is 50 characters). | `app/cpy/CVTRA07Y.cpy:22` |
| TRAN-REPORT-CAT-DESC | 29-character category description column (source description is 50 characters). | `app/cpy/CVTRA07Y.cpy:26` |
| TRAN-REPORT-AMT | Edited transaction amount -ZZZ,ZZZ,ZZZ.ZZ (leading minus sign for negatives, 9 integer digits). | `app/cpy/CVTRA07Y.cpy:30` |
| TRANSACTION-HEADER-1 | Column heading line: Transaction ID, Account ID, Transaction Type, Tran Category, Tran Source, Amount. | `app/cpy/CVTRA07Y.cpy:33-46` |
| TRANSACTION-HEADER-2 | 133-character line of dashes used as separator after headings and totals. | `app/cpy/CVTRA07Y.cpy:48` |
| REPT-PAGE-TOTAL | Edited page total +ZZZ,ZZZ,ZZZ.ZZ in the 'Page Total' line REPORT-PAGE-TOTALS. | `app/cpy/CVTRA07Y.cpy:50-54` |
| REPT-ACCOUNT-TOTAL | Edited account total in the 'Account Total' line REPORT-ACCOUNT-TOTALS (CBTRN03C breaks it on card number). | `app/cpy/CVTRA07Y.cpy:56-60` |
| REPT-GRAND-TOTAL | Edited grand total in the 'Grand Total' line REPORT-GRAND-TOTALS. | `app/cpy/CVTRA07Y.cpy:62-66` |

## Observations

- anomaly: All report lines are shorter than the 133-byte report record (title 115, detail and column header 114, total lines 112 bytes by PIC sizes); CBTRN03C moves them into FD-REPTFILE-REC PIC X(133), so they are space-padded. There is no carriage-control byte. Confirmed from PIC sizes and app/cbl/CBTRN03C.cbl:85. (`app/cpy/CVTRA07Y.cpy:4-66`)
- hardcoded-value: The report identifiers 'DALYREPT' and 'Daily Transaction Report' and all column headings are VALUE literals in the copybook. (`app/cpy/CVTRA07Y.cpy:5-8`)

## Sources

- `app/cpy/CVTRA07Y.cpy`
- `docs/_work/structure/copybooks/CVTRA07Y.json`
- `docs/_work/layouts/CVTRA07Y.json`
- `docs/_work/semantic/copybooks/CVTRA07Y.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
