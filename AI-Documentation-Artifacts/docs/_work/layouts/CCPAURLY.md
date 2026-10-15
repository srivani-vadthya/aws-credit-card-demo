### (FRAGMENT) (length 57)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | (FRAGMENT) | 1 | 57 | 57 |  |  |  |  | 19 |
| 05 | &nbsp;&nbsp;PA-RL-CARD-NUM | 1 | 16 | 16 |  | X(16) | DISPLAY |  | 19 |
| 05 | &nbsp;&nbsp;PA-RL-TRANSACTION-ID | 17 | 31 | 15 |  | X(15) | DISPLAY |  | 20 |
| 05 | &nbsp;&nbsp;PA-RL-AUTH-ID-CODE | 32 | 37 | 6 |  | X(06) | DISPLAY |  | 21 |
| 05 | &nbsp;&nbsp;PA-RL-AUTH-RESP-CODE | 38 | 39 | 2 |  | X(02) | DISPLAY |  | 22 |
| 05 | &nbsp;&nbsp;PA-RL-AUTH-RESP-REASON | 40 | 43 | 4 |  | X(04) | DISPLAY |  | 23 |
| 05 | &nbsp;&nbsp;PA-RL-APPROVED-AMT | 44 | 57 | 14 |  | +9(10).99 | DISPLAY |  | 24 |

Notes: Copybook has no 01 level; offsets are relative to the COPY position
