### CARDDEMO-ADMIN-MENU-OPTIONS (length 407)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | CARDDEMO-ADMIN-MENU-OPTIONS | 1 | 407 | 407 |  |  |  |  | 19 |
| 05 | &nbsp;&nbsp;CDEMO-ADMIN-OPT-COUNT | 1 | 2 | 2 |  | 9(02) | DISPLAY |  | 22 |
| 05 | &nbsp;&nbsp;CDEMO-ADMIN-OPTIONS-DATA | 3 | 272 | 270 |  |  |  |  | 24 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 3 | 4 | 2 |  | 9(02) | DISPLAY |  | 26 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 5 | 39 | 35 |  | X(35) | DISPLAY |  | 27 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 40 | 47 | 8 |  | X(08) | DISPLAY |  | 29 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 48 | 49 | 2 |  | 9(02) | DISPLAY |  | 31 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 50 | 84 | 35 |  | X(35) | DISPLAY |  | 32 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 85 | 92 | 8 |  | X(08) | DISPLAY |  | 34 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 93 | 94 | 2 |  | 9(02) | DISPLAY |  | 36 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 95 | 129 | 35 |  | X(35) | DISPLAY |  | 37 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 130 | 137 | 8 |  | X(08) | DISPLAY |  | 39 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 138 | 139 | 2 |  | 9(02) | DISPLAY |  | 41 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 140 | 174 | 35 |  | X(35) | DISPLAY |  | 42 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 175 | 182 | 8 |  | X(08) | DISPLAY |  | 44 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 183 | 184 | 2 |  | 9(02) | DISPLAY |  | 46 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 185 | 219 | 35 |  | X(35) | DISPLAY |  | 47 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 220 | 227 | 8 |  | X(08) | DISPLAY |  | 49 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 228 | 229 | 2 |  | 9(02) | DISPLAY |  | 50 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 230 | 264 | 35 |  | X(35) | DISPLAY |  | 51 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 265 | 272 | 8 |  | X(08) | DISPLAY |  | 53 |
| 05 | &nbsp;&nbsp;CDEMO-ADMIN-OPTIONS | 3 | 407 | 405 |  |  |  | CDEMO-ADMIN-OPTIONS-DATA | 55 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-ADMIN-OPT | 3 | 407 | 45 | 9 |  |  |  | 56 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CDEMO-ADMIN-OPT-NUM | 3 | 4 | 2 |  | 9(02) | DISPLAY |  | 57 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CDEMO-ADMIN-OPT-NAME | 5 | 39 | 35 |  | X(35) | DISPLAY |  | 58 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CDEMO-ADMIN-OPT-PGMNAME | 40 | 47 | 8 |  | X(08) | DISPLAY |  | 59 |

