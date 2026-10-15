### TRNX-RECORD (length 350)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | TRNX-RECORD | 1 | 350 | 350 |  |  |  |  | 20 |
| 05 | &nbsp;&nbsp;TRNX-KEY | 1 | 32 | 32 |  |  |  |  | 21 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRNX-CARD-NUM | 1 | 16 | 16 |  | X(16) | DISPLAY |  | 22 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRNX-ID | 17 | 32 | 16 |  | X(16) | DISPLAY |  | 23 |
| 05 | &nbsp;&nbsp;TRNX-REST | 33 | 350 | 318 |  |  |  |  | 24 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRNX-TYPE-CD | 33 | 34 | 2 |  | X(02) | DISPLAY |  | 25 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRNX-CAT-CD | 35 | 38 | 4 |  | 9(04) | DISPLAY |  | 26 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRNX-SOURCE | 39 | 48 | 10 |  | X(10) | DISPLAY |  | 27 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRNX-DESC | 49 | 148 | 100 |  | X(100) | DISPLAY |  | 28 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRNX-AMT | 149 | 159 | 11 |  | S9(09)V99 | DISPLAY |  | 29 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRNX-MERCHANT-ID | 160 | 168 | 9 |  | 9(09) | DISPLAY |  | 30 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRNX-MERCHANT-NAME | 169 | 218 | 50 |  | X(50) | DISPLAY |  | 31 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRNX-MERCHANT-CITY | 219 | 268 | 50 |  | X(50) | DISPLAY |  | 32 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRNX-MERCHANT-ZIP | 269 | 278 | 10 |  | X(10) | DISPLAY |  | 33 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRNX-ORIG-TS | 279 | 304 | 26 |  | X(26) | DISPLAY |  | 34 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;TRNX-PROC-TS | 305 | 330 | 26 |  | X(26) | DISPLAY |  | 35 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 331 | 350 | 20 |  | X(20) | DISPLAY |  | 36 |

