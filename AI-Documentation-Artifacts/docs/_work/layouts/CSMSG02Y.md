### ABEND-DATA (length 134)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | ABEND-DATA | 1 | 134 | 134 |  |  |  |  | 21 |
| 05 | &nbsp;&nbsp;ABEND-CODE | 1 | 4 | 4 |  | X(4) | DISPLAY |  | 22 |
| 05 | &nbsp;&nbsp;ABEND-CULPRIT | 5 | 12 | 8 |  | X(8) | DISPLAY |  | 24 |
| 05 | &nbsp;&nbsp;ABEND-REASON | 13 | 62 | 50 |  | X(50) | DISPLAY |  | 26 |
| 05 | &nbsp;&nbsp;ABEND-MSG | 63 | 134 | 72 |  | X(72) | DISPLAY |  | 28 |

