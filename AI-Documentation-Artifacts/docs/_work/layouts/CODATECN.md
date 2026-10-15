### CODATECN-REC (length 80)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | CODATECN-REC | 1 | 80 | 80 |  |  |  |  | 17 |
| 05 | &nbsp;&nbsp;CODATECN-IN-REC | 1 | 21 | 21 |  |  |  |  | 18 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CODATECN-TYPE | 1 | 1 | 1 |  | X | DISPLAY |  | 19 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;YYYYMMDD-IN = "1" |  |  |  |  |  |  |  | 20 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;YYYY-MM-DD-IN = "2" |  |  |  |  |  |  |  | 21 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CODATECN-INP-DATE | 2 | 21 | 20 |  | X(20) | DISPLAY |  | 22 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1INP | 2 | 21 | 20 |  |  |  | CODATECN-INP-DATE | 23 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1YYYY | 2 | 5 | 4 |  | XXXX | DISPLAY |  | 24 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1MM | 6 | 7 | 2 |  | XX | DISPLAY |  | 25 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1DD | 8 | 9 | 2 |  | XX | DISPLAY |  | 26 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1FIL | 10 | 21 | 12 |  | X(12) | DISPLAY |  | 27 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CODATECN-2INP | 2 | 21 | 20 |  |  |  | CODATECN-INP-DATE | 28 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1O-YYYY | 2 | 5 | 4 |  | XXXX | DISPLAY |  | 29 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1I-S1 | 6 | 6 | 1 |  | X | DISPLAY |  | 30 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1MM | 7 | 8 | 2 |  | XX | DISPLAY |  | 31 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1I-S2 | 9 | 9 | 1 |  | X | DISPLAY |  | 32 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-2YY | 10 | 11 | 2 |  | XX | DISPLAY |  | 33 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-2FIL | 12 | 21 | 10 |  | X(10) | DISPLAY |  | 34 |
| 05 | &nbsp;&nbsp;CODATECN-OUT-REC | 22 | 42 | 21 |  |  |  |  | 35 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CODATECN-OUTTYPE | 22 | 22 | 1 |  | X | DISPLAY |  | 36 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;YYYY-MM-DD-OP = "1" |  |  |  |  |  |  |  | 37 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;YYYYMMDD-OP = "2" |  |  |  |  |  |  |  | 38 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CODATECN-0UT-DATE | 23 | 42 | 20 |  | X(20) | DISPLAY |  | 39 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1OUT | 23 | 42 | 20 |  |  |  | CODATECN-0UT-DATE | 40 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1O-YYYY | 23 | 26 | 4 |  | XXXX | DISPLAY |  | 41 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1O-S1 | 27 | 27 | 1 |  | X | DISPLAY |  | 42 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1O-MM | 28 | 29 | 2 |  | XX | DISPLAY |  | 43 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1O-S2 | 30 | 30 | 1 |  | X | DISPLAY |  | 44 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1O-DD | 31 | 32 | 2 |  | XX | DISPLAY |  | 45 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1OFIL | 33 | 42 | 10 |  | X(10) | DISPLAY |  | 46 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CODATECN-2OUT | 23 | 42 | 20 |  |  |  | CODATECN-0UT-DATE | 47 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-2O-YYYY | 23 | 26 | 4 |  | XXXX | DISPLAY |  | 48 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-2O-MM | 27 | 28 | 2 |  | XX | DISPLAY |  | 49 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-2O-DD | 29 | 30 | 2 |  | XX | DISPLAY |  | 50 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-2OFIL | 31 | 42 | 12 |  | X(12) | DISPLAY |  | 51 |
| 05 | &nbsp;&nbsp;CODATECN-ERROR-MSG | 43 | 80 | 38 |  | X(38) | DISPLAY |  | 52 |

