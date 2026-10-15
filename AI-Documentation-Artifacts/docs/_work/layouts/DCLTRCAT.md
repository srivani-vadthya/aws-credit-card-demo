### DCLTRANSACTION-TYPE-CATEGORY (length 58)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | DCLTRANSACTION-TYPE-CATEGORY | 1 | 58 | 58 |  |  |  |  | 36 |
| 10 | &nbsp;&nbsp;DCL-TRC-TYPE-CODE | 1 | 2 | 2 |  | X(2) | DISPLAY |  | 39 |
| 10 | &nbsp;&nbsp;DCL-TRC-TYPE-CATEGORY | 3 | 6 | 4 |  | X(4) | DISPLAY |  | 42 |
| 10 | &nbsp;&nbsp;DCL-TRC-CAT-DATA | 7 | 58 | 52 |  |  |  |  | 45 |
| 49 | &nbsp;&nbsp;&nbsp;&nbsp;DCL-TRC-CAT-DATA-LEN | 7 | 8 | 2 |  | S9(4) | COMP |  | 47 |
| 49 | &nbsp;&nbsp;&nbsp;&nbsp;DCL-TRC-CAT-DATA-TEXT | 9 | 58 | 50 |  | X(50) | DISPLAY |  | 50 |

