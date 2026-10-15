### PASFLPCB (length 136)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | PASFLPCB | 1 | 136 | 136 |  |  |  |  | 17 |
| 05 | &nbsp;&nbsp;PASFL-DBDNAME | 1 | 8 | 8 |  | X(08) | DISPLAY |  | 18 |
| 05 | &nbsp;&nbsp;PASFL-SEG-LEVEL | 9 | 10 | 2 |  | X(02) | DISPLAY |  | 19 |
| 05 | &nbsp;&nbsp;PASFL-PCB-STATUS | 11 | 12 | 2 |  | X(02) | DISPLAY |  | 20 |
| 05 | &nbsp;&nbsp;PASFL-PCB-PROCOPT | 13 | 16 | 4 |  | X(04) | DISPLAY |  | 21 |
| 05 | &nbsp;&nbsp;FILLER | 17 | 20 | 4 |  | S9(05) | COMP |  | 22 |
| 05 | &nbsp;&nbsp;PASFL-SEG-NAME | 21 | 28 | 8 |  | X(08) | DISPLAY |  | 23 |
| 05 | &nbsp;&nbsp;PASFL-KEYFB-NAME | 29 | 32 | 4 |  | S9(05) | COMP |  | 24 |
| 05 | &nbsp;&nbsp;PASFL-NUM-SENSEGS | 33 | 36 | 4 |  | S9(05) | COMP |  | 25 |
| 05 | &nbsp;&nbsp;PASFL-KEYFB | 37 | 136 | 100 |  | X(100) | DISPLAY |  | 26 |

