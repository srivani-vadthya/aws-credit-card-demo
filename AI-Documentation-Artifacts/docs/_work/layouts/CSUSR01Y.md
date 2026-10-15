### SEC-USER-DATA (length 80)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | SEC-USER-DATA | 1 | 80 | 80 |  |  |  |  | 17 |
| 05 | &nbsp;&nbsp;SEC-USR-ID | 1 | 8 | 8 |  | X(08) | DISPLAY |  | 18 |
| 05 | &nbsp;&nbsp;SEC-USR-FNAME | 9 | 28 | 20 |  | X(20) | DISPLAY |  | 19 |
| 05 | &nbsp;&nbsp;SEC-USR-LNAME | 29 | 48 | 20 |  | X(20) | DISPLAY |  | 20 |
| 05 | &nbsp;&nbsp;SEC-USR-PWD | 49 | 56 | 8 |  | X(08) | DISPLAY |  | 21 |
| 05 | &nbsp;&nbsp;SEC-USR-TYPE | 57 | 57 | 1 |  | X(01) | DISPLAY |  | 22 |
| 05 | &nbsp;&nbsp;SEC-USR-FILLER | 58 | 80 | 23 |  | X(23) | DISPLAY |  | 23 |

