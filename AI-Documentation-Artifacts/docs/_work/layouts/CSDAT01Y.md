### WS-DATE-TIME (length 58)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | WS-DATE-TIME | 1 | 58 | 58 |  |  |  |  | 17 |
| 05 | &nbsp;&nbsp;WS-CURDATE-DATA | 1 | 16 | 16 |  |  |  |  | 18 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-CURDATE | 1 | 8 | 8 |  |  |  |  | 19 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-CURDATE-YEAR | 1 | 4 | 4 |  | 9(04) | DISPLAY |  | 20 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-CURDATE-MONTH | 5 | 6 | 2 |  | 9(02) | DISPLAY |  | 21 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-CURDATE-DAY | 7 | 8 | 2 |  | 9(02) | DISPLAY |  | 22 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-CURDATE-N | 1 | 8 | 8 |  | 9(08) | DISPLAY | WS-CURDATE | 23 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-CURTIME | 9 | 16 | 8 |  |  |  |  | 24 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-CURTIME-HOURS | 9 | 10 | 2 |  | 9(02) | DISPLAY |  | 25 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-CURTIME-MINUTE | 11 | 12 | 2 |  | 9(02) | DISPLAY |  | 26 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-CURTIME-SECOND | 13 | 14 | 2 |  | 9(02) | DISPLAY |  | 27 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-CURTIME-MILSEC | 15 | 16 | 2 |  | 9(02) | DISPLAY |  | 28 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-CURTIME-N | 9 | 16 | 8 |  | 9(08) | DISPLAY | WS-CURTIME | 29 |
| 05 | &nbsp;&nbsp;WS-CURDATE-MM-DD-YY | 17 | 24 | 8 |  |  |  |  | 30 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-CURDATE-MM | 17 | 18 | 2 |  | 9(02) | DISPLAY |  | 31 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 19 | 19 | 1 |  | X(01) | DISPLAY |  | 32 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-CURDATE-DD | 20 | 21 | 2 |  | 9(02) | DISPLAY |  | 33 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 22 | 22 | 1 |  | X(01) | DISPLAY |  | 34 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-CURDATE-YY | 23 | 24 | 2 |  | 9(02) | DISPLAY |  | 35 |
| 05 | &nbsp;&nbsp;WS-CURTIME-HH-MM-SS | 25 | 32 | 8 |  |  |  |  | 36 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-CURTIME-HH | 25 | 26 | 2 |  | 9(02) | DISPLAY |  | 37 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 27 | 27 | 1 |  | X(01) | DISPLAY |  | 38 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-CURTIME-MM | 28 | 29 | 2 |  | 9(02) | DISPLAY |  | 39 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 30 | 30 | 1 |  | X(01) | DISPLAY |  | 40 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-CURTIME-SS | 31 | 32 | 2 |  | 9(02) | DISPLAY |  | 41 |
| 05 | &nbsp;&nbsp;WS-TIMESTAMP | 33 | 58 | 26 |  |  |  |  | 42 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-TIMESTAMP-DT-YYYY | 33 | 36 | 4 |  | 9(04) | DISPLAY |  | 43 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 37 | 37 | 1 |  | X(01) | DISPLAY |  | 44 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-TIMESTAMP-DT-MM | 38 | 39 | 2 |  | 9(02) | DISPLAY |  | 45 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 40 | 40 | 1 |  | X(01) | DISPLAY |  | 46 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-TIMESTAMP-DT-DD | 41 | 42 | 2 |  | 9(02) | DISPLAY |  | 47 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 43 | 43 | 1 |  | X(01) | DISPLAY |  | 48 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-TIMESTAMP-TM-HH | 44 | 45 | 2 |  | 9(02) | DISPLAY |  | 49 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 46 | 46 | 1 |  | X(01) | DISPLAY |  | 50 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-TIMESTAMP-TM-MM | 47 | 48 | 2 |  | 9(02) | DISPLAY |  | 51 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 49 | 49 | 1 |  | X(01) | DISPLAY |  | 52 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-TIMESTAMP-TM-SS | 50 | 51 | 2 |  | 9(02) | DISPLAY |  | 53 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 52 | 52 | 1 |  | X(01) | DISPLAY |  | 54 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-TIMESTAMP-TM-MS6 | 53 | 58 | 6 |  | 9(06) | DISPLAY |  | 55 |

