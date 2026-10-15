### ERROR-LOG-RECORD (length 122)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | ERROR-LOG-RECORD | 1 | 122 | 122 |  |  |  |  | 19 |
| 05 | &nbsp;&nbsp;ERR-DATE | 1 | 6 | 6 |  | X(06) | DISPLAY |  | 20 |
| 05 | &nbsp;&nbsp;ERR-TIME | 7 | 12 | 6 |  | X(06) | DISPLAY |  | 21 |
| 05 | &nbsp;&nbsp;ERR-APPLICATION | 13 | 20 | 8 |  | X(08) | DISPLAY |  | 22 |
| 05 | &nbsp;&nbsp;ERR-PROGRAM | 21 | 28 | 8 |  | X(08) | DISPLAY |  | 23 |
| 05 | &nbsp;&nbsp;ERR-LOCATION | 29 | 32 | 4 |  | X(04) | DISPLAY |  | 24 |
| 05 | &nbsp;&nbsp;ERR-LEVEL | 33 | 33 | 1 |  | X(01) | DISPLAY |  | 25 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;ERR-LOG = 'L' |  |  |  |  |  |  |  | 26 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;ERR-INFO = 'I' |  |  |  |  |  |  |  | 27 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;ERR-WARNING = 'W' |  |  |  |  |  |  |  | 28 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;ERR-CRITICAL = 'C' |  |  |  |  |  |  |  | 29 |
| 05 | &nbsp;&nbsp;ERR-SUBSYSTEM | 34 | 34 | 1 |  | X(01) | DISPLAY |  | 30 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;ERR-APP = 'A' |  |  |  |  |  |  |  | 31 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;ERR-CICS = 'C' |  |  |  |  |  |  |  | 32 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;ERR-IMS = 'I' |  |  |  |  |  |  |  | 33 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;ERR-DB2 = 'D' |  |  |  |  |  |  |  | 34 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;ERR-MQ = 'M' |  |  |  |  |  |  |  | 35 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;ERR-FILE = 'F' |  |  |  |  |  |  |  | 36 |
| 05 | &nbsp;&nbsp;ERR-CODE-1 | 35 | 43 | 9 |  | X(09) | DISPLAY |  | 37 |
| 05 | &nbsp;&nbsp;ERR-CODE-2 | 44 | 52 | 9 |  | X(09) | DISPLAY |  | 38 |
| 05 | &nbsp;&nbsp;ERR-MESSAGE | 53 | 102 | 50 |  | X(50) | DISPLAY |  | 39 |
| 05 | &nbsp;&nbsp;ERR-EVENT-KEY | 103 | 122 | 20 |  | X(20) | DISPLAY |  | 40 |

