### TRAN-CAT-RECORD (length 60)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | TRAN-CAT-RECORD | 1 | 60 | 60 |  |  |  |  | 4 |
| 05 | &nbsp;&nbsp;TRAN-CAT-KEY | 1 | 6 | 6 |  |  |  |  | 5 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRAN-TYPE-CD | 1 | 2 | 2 |  | X(02) | DISPLAY |  | 6 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRAN-CAT-CD | 3 | 6 | 4 |  | 9(04) | DISPLAY |  | 7 |
| 05 | &nbsp;&nbsp;TRAN-CAT-TYPE-DESC | 7 | 56 | 50 |  | X(50) | DISPLAY |  | 8 |
| 05 | &nbsp;&nbsp;FILLER | 57 | 60 | 4 |  | X(04) | DISPLAY |  | 9 |

