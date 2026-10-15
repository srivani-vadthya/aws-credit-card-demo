### CARD-RECORD (length 150)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | CARD-RECORD | 1 | 150 | 150 |  |  |  |  | 4 |
| 05 | &nbsp;&nbsp;CARD-NUM | 1 | 16 | 16 |  | X(16) | DISPLAY |  | 5 |
| 05 | &nbsp;&nbsp;CARD-ACCT-ID | 17 | 27 | 11 |  | 9(11) | DISPLAY |  | 6 |
| 05 | &nbsp;&nbsp;CARD-CVV-CD | 28 | 30 | 3 |  | 9(03) | DISPLAY |  | 7 |
| 05 | &nbsp;&nbsp;CARD-EMBOSSED-NAME | 31 | 80 | 50 |  | X(50) | DISPLAY |  | 8 |
| 05 | &nbsp;&nbsp;CARD-EXPIRAION-DATE | 81 | 90 | 10 |  | X(10) | DISPLAY |  | 9 |
| 05 | &nbsp;&nbsp;CARD-ACTIVE-STATUS | 91 | 91 | 1 |  | X(01) | DISPLAY |  | 10 |
| 05 | &nbsp;&nbsp;FILLER | 92 | 150 | 59 |  | X(59) | DISPLAY |  | 11 |

