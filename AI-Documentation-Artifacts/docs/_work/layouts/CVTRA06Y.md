### DALYTRAN-RECORD (length 350)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | DALYTRAN-RECORD | 1 | 350 | 350 |  |  |  |  | 4 |
| 05 | &nbsp;&nbsp;DALYTRAN-ID | 1 | 16 | 16 |  | X(16) | DISPLAY |  | 5 |
| 05 | &nbsp;&nbsp;DALYTRAN-TYPE-CD | 17 | 18 | 2 |  | X(02) | DISPLAY |  | 6 |
| 05 | &nbsp;&nbsp;DALYTRAN-CAT-CD | 19 | 22 | 4 |  | 9(04) | DISPLAY |  | 7 |
| 05 | &nbsp;&nbsp;DALYTRAN-SOURCE | 23 | 32 | 10 |  | X(10) | DISPLAY |  | 8 |
| 05 | &nbsp;&nbsp;DALYTRAN-DESC | 33 | 132 | 100 |  | X(100) | DISPLAY |  | 9 |
| 05 | &nbsp;&nbsp;DALYTRAN-AMT | 133 | 143 | 11 |  | S9(09)V99 | DISPLAY |  | 10 |
| 05 | &nbsp;&nbsp;DALYTRAN-MERCHANT-ID | 144 | 152 | 9 |  | 9(09) | DISPLAY |  | 11 |
| 05 | &nbsp;&nbsp;DALYTRAN-MERCHANT-NAME | 153 | 202 | 50 |  | X(50) | DISPLAY |  | 12 |
| 05 | &nbsp;&nbsp;DALYTRAN-MERCHANT-CITY | 203 | 252 | 50 |  | X(50) | DISPLAY |  | 13 |
| 05 | &nbsp;&nbsp;DALYTRAN-MERCHANT-ZIP | 253 | 262 | 10 |  | X(10) | DISPLAY |  | 14 |
| 05 | &nbsp;&nbsp;DALYTRAN-CARD-NUM | 263 | 278 | 16 |  | X(16) | DISPLAY |  | 15 |
| 05 | &nbsp;&nbsp;DALYTRAN-ORIG-TS | 279 | 304 | 26 |  | X(26) | DISPLAY |  | 16 |
| 05 | &nbsp;&nbsp;DALYTRAN-PROC-TS | 305 | 330 | 26 |  | X(26) | DISPLAY |  | 17 |
| 05 | &nbsp;&nbsp;FILLER | 331 | 350 | 20 |  | X(20) | DISPLAY |  | 18 |

