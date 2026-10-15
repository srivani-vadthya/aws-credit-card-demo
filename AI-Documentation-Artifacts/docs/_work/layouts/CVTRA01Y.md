### TRAN-CAT-BAL-RECORD (length 50)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | TRAN-CAT-BAL-RECORD | 1 | 50 | 50 |  |  |  |  | 4 |
| 05 | &nbsp;&nbsp;TRAN-CAT-KEY | 1 | 17 | 17 |  |  |  |  | 5 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRANCAT-ACCT-ID | 1 | 11 | 11 |  | 9(11) | DISPLAY |  | 6 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRANCAT-TYPE-CD | 12 | 13 | 2 |  | X(02) | DISPLAY |  | 7 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRANCAT-CD | 14 | 17 | 4 |  | 9(04) | DISPLAY |  | 8 |
| 05 | &nbsp;&nbsp;TRAN-CAT-BAL | 18 | 28 | 11 |  | S9(09)V99 | DISPLAY |  | 9 |
| 05 | &nbsp;&nbsp;FILLER | 29 | 50 | 22 |  | X(22) | DISPLAY |  | 10 |

