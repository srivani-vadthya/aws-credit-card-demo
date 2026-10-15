### PAUTBPCB (length 291)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | PAUTBPCB | 1 | 291 | 291 |  |  |  |  | 17 |
| 05 | &nbsp;&nbsp;PAUT-DBDNAME | 1 | 8 | 8 |  | X(08) | DISPLAY |  | 18 |
| 05 | &nbsp;&nbsp;PAUT-SEG-LEVEL | 9 | 10 | 2 |  | X(02) | DISPLAY |  | 19 |
| 05 | &nbsp;&nbsp;PAUT-PCB-STATUS | 11 | 12 | 2 |  | X(02) | DISPLAY |  | 20 |
| 05 | &nbsp;&nbsp;PAUT-PCB-PROCOPT | 13 | 16 | 4 |  | X(04) | DISPLAY |  | 21 |
| 05 | &nbsp;&nbsp;FILLER | 17 | 20 | 4 |  | S9(05) | COMP |  | 22 |
| 05 | &nbsp;&nbsp;PAUT-SEG-NAME | 21 | 28 | 8 |  | X(08) | DISPLAY |  | 23 |
| 05 | &nbsp;&nbsp;PAUT-KEYFB-NAME | 29 | 32 | 4 |  | S9(05) | COMP |  | 24 |
| 05 | &nbsp;&nbsp;PAUT-NUM-SENSEGS | 33 | 36 | 4 |  | S9(05) | COMP |  | 25 |
| 05 | &nbsp;&nbsp;PAUT-KEYFB | 37 | 291 | 255 |  | X(255) | DISPLAY |  | 26 |

