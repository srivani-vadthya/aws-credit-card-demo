### DIS-GROUP-RECORD (length 50)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | DIS-GROUP-RECORD | 1 | 50 | 50 |  |  |  |  | 4 |
| 05 | &nbsp;&nbsp;DIS-GROUP-KEY | 1 | 16 | 16 |  |  |  |  | 5 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;DIS-ACCT-GROUP-ID | 1 | 10 | 10 |  | X(10) | DISPLAY |  | 6 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;DIS-TRAN-TYPE-CD | 11 | 12 | 2 |  | X(02) | DISPLAY |  | 7 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;DIS-TRAN-CAT-CD | 13 | 16 | 4 |  | 9(04) | DISPLAY |  | 8 |
| 05 | &nbsp;&nbsp;DIS-INT-RATE | 17 | 22 | 6 |  | S9(04)V99 | DISPLAY |  | 9 |
| 05 | &nbsp;&nbsp;FILLER | 23 | 50 | 28 |  | X(28) | DISPLAY |  | 10 |

