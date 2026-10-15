### DCLTRANSACTION-TYPE (length 54)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | DCLTRANSACTION-TYPE | 1 | 54 | 54 |  |  |  |  | 35 |
| 10 | &nbsp;&nbsp;DCL-TR-TYPE | 1 | 2 | 2 |  | X(2) | DISPLAY |  | 38 |
| 10 | &nbsp;&nbsp;DCL-TR-DESCRIPTION | 3 | 54 | 52 |  |  |  |  | 40 |
| 49 | &nbsp;&nbsp;&nbsp;&nbsp;DCL-TR-DESCRIPTION-LEN | 3 | 4 | 2 |  | S9(4) | COMP |  | 42 |
| 49 | &nbsp;&nbsp;&nbsp;&nbsp;DCL-TR-DESCRIPTION-TEXT | 5 | 54 | 50 |  | X(50) | DISPLAY |  | 45 |

