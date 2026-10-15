### REPORT-NAME-HEADER (length 115)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | REPORT-NAME-HEADER | 1 | 115 | 115 |  |  |  |  | 4 |
| 05 | &nbsp;&nbsp;REPT-SHORT-NAME | 1 | 38 | 38 |  | X(38) | DISPLAY |  | 5 |
| 05 | &nbsp;&nbsp;REPT-LONG-NAME | 39 | 79 | 41 |  | X(41) | DISPLAY |  | 7 |
| 05 | &nbsp;&nbsp;REPT-DATE-HEADER | 80 | 91 | 12 |  | X(12) | DISPLAY |  | 9 |
| 05 | &nbsp;&nbsp;REPT-START-DATE | 92 | 101 | 10 |  | X(10) | DISPLAY |  | 11 |
| 05 | &nbsp;&nbsp;FILLER | 102 | 105 | 4 |  | X(04) | DISPLAY |  | 12 |
| 05 | &nbsp;&nbsp;REPT-END-DATE | 106 | 115 | 10 |  | X(10) | DISPLAY |  | 13 |

### TRANSACTION-DETAIL-REPORT (length 114)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | TRANSACTION-DETAIL-REPORT | 1 | 114 | 114 |  |  |  |  | 15 |
| 05 | &nbsp;&nbsp;TRAN-REPORT-TRANS-ID | 1 | 16 | 16 |  | X(16) | DISPLAY |  | 16 |
| 05 | &nbsp;&nbsp;FILLER | 17 | 17 | 1 |  | X(01) | DISPLAY |  | 17 |
| 05 | &nbsp;&nbsp;TRAN-REPORT-ACCOUNT-ID | 18 | 28 | 11 |  | X(11) | DISPLAY |  | 18 |
| 05 | &nbsp;&nbsp;FILLER | 29 | 29 | 1 |  | X(01) | DISPLAY |  | 19 |
| 05 | &nbsp;&nbsp;TRAN-REPORT-TYPE-CD | 30 | 31 | 2 |  | X(02) | DISPLAY |  | 20 |
| 05 | &nbsp;&nbsp;FILLER | 32 | 32 | 1 |  | X(01) | DISPLAY |  | 21 |
| 05 | &nbsp;&nbsp;TRAN-REPORT-TYPE-DESC | 33 | 47 | 15 |  | X(15) | DISPLAY |  | 22 |
| 05 | &nbsp;&nbsp;FILLER | 48 | 48 | 1 |  | X(01) | DISPLAY |  | 23 |
| 05 | &nbsp;&nbsp;TRAN-REPORT-CAT-CD | 49 | 52 | 4 |  | 9(04) | DISPLAY |  | 24 |
| 05 | &nbsp;&nbsp;FILLER | 53 | 53 | 1 |  | X(01) | DISPLAY |  | 25 |
| 05 | &nbsp;&nbsp;TRAN-REPORT-CAT-DESC | 54 | 82 | 29 |  | X(29) | DISPLAY |  | 26 |
| 05 | &nbsp;&nbsp;FILLER | 83 | 83 | 1 |  | X(01) | DISPLAY |  | 27 |
| 05 | &nbsp;&nbsp;TRAN-REPORT-SOURCE | 84 | 93 | 10 |  | X(10) | DISPLAY |  | 28 |
| 05 | &nbsp;&nbsp;FILLER | 94 | 97 | 4 |  | X(04) | DISPLAY |  | 29 |
| 05 | &nbsp;&nbsp;TRAN-REPORT-AMT | 98 | 112 | 15 |  | -ZZZ,ZZZ,ZZZ.ZZ | DISPLAY |  | 30 |
| 05 | &nbsp;&nbsp;FILLER | 113 | 114 | 2 |  | X(02) | DISPLAY |  | 31 |

### TRANSACTION-HEADER-1 (length 114)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | TRANSACTION-HEADER-1 | 1 | 114 | 114 |  |  |  |  | 33 |
| 05 | &nbsp;&nbsp;FILLER | 1 | 17 | 17 |  | X(17) | DISPLAY |  | 34 |
| 05 | &nbsp;&nbsp;FILLER | 18 | 29 | 12 |  | X(12) | DISPLAY |  | 36 |
| 05 | &nbsp;&nbsp;FILLER | 30 | 48 | 19 |  | X(19) | DISPLAY |  | 38 |
| 05 | &nbsp;&nbsp;FILLER | 49 | 83 | 35 |  | X(35) | DISPLAY |  | 40 |
| 05 | &nbsp;&nbsp;FILLER | 84 | 97 | 14 |  | X(14) | DISPLAY |  | 42 |
| 05 | &nbsp;&nbsp;FILLER | 98 | 98 | 1 |  | X | DISPLAY |  | 44 |
| 05 | &nbsp;&nbsp;FILLER | 99 | 114 | 16 |  | X(16) | DISPLAY |  | 45 |

### TRANSACTION-HEADER-2 (length 133)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | TRANSACTION-HEADER-2 | 1 | 133 | 133 |  | X(133) | DISPLAY |  | 48 |

### REPORT-PAGE-TOTALS (length 112)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | REPORT-PAGE-TOTALS | 1 | 112 | 112 |  |  |  |  | 50 |
| 05 | &nbsp;&nbsp;FILLER | 1 | 11 | 11 |  | X(11) | DISPLAY |  | 51 |
| 05 | &nbsp;&nbsp;FILLER | 12 | 97 | 86 |  | X(86) | DISPLAY |  | 53 |
| 05 | &nbsp;&nbsp;REPT-PAGE-TOTAL | 98 | 112 | 15 |  | +ZZZ,ZZZ,ZZZ.ZZ | DISPLAY |  | 54 |

### REPORT-ACCOUNT-TOTALS (length 112)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | REPORT-ACCOUNT-TOTALS | 1 | 112 | 112 |  |  |  |  | 56 |
| 05 | &nbsp;&nbsp;FILLER | 1 | 13 | 13 |  | X(13) | DISPLAY |  | 57 |
| 05 | &nbsp;&nbsp;FILLER | 14 | 97 | 84 |  | X(84) | DISPLAY |  | 59 |
| 05 | &nbsp;&nbsp;REPT-ACCOUNT-TOTAL | 98 | 112 | 15 |  | +ZZZ,ZZZ,ZZZ.ZZ | DISPLAY |  | 60 |

### REPORT-GRAND-TOTALS (length 112)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | REPORT-GRAND-TOTALS | 1 | 112 | 112 |  |  |  |  | 62 |
| 05 | &nbsp;&nbsp;FILLER | 1 | 11 | 11 |  | X(11) | DISPLAY |  | 63 |
| 05 | &nbsp;&nbsp;FILLER | 12 | 97 | 86 |  | X(86) | DISPLAY |  | 65 |
| 05 | &nbsp;&nbsp;REPT-GRAND-TOTAL | 98 | 112 | 15 |  | +ZZZ,ZZZ,ZZZ.ZZ | DISPLAY |  | 66 |

