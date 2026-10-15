### (FRAGMENT) (length 817)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | (FRAGMENT) | 1 | 817 | 817 |  |  |  |  | 21 |
| 05 | &nbsp;&nbsp;WS-DB2-COMMON-VARS | 1 | 81 | 81 |  |  |  |  | 21 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-DISP-SQLCODE | 1 | 5 | 5 |  | ----9 | DISPLAY |  | 22 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-DUMMY-DB2-INT | 6 | 8 | 3 |  | S9(4) | COMP-3 |  | 23 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-DB2-PROCESSING-FLAG | 9 | 9 | 1 |  | X(1) | DISPLAY |  | 25 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-DB2-OK = '0' |  |  |  |  |  |  |  | 26 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-DB2-ERROR = '1' |  |  |  |  |  |  |  | 27 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-DB2-CURRENT-ACTION | 10 | 81 | 72 |  | X(72) | DISPLAY |  | 28 |
| 05 | &nbsp;&nbsp;WS-DSNTIAC-FORMATTED | 82 | 803 | 722 |  |  |  |  | 33 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-DSNTIAC-MESG-LEN | 82 | 83 | 2 |  | S9(4) | COMP |  | 34 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-DSNTIAC-FMTD-TEXT | 84 | 803 | 720 |  |  |  |  | 35 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-DSNTIAC-FMTD-TEXT-LINE | 84 | 803 | 72 | 10 | X(72) | DISPLAY |  | 36 |
| 05 | &nbsp;&nbsp;WS-DSNTIAC-LRECL | 804 | 805 | 2 |  | S9(4) | COMP |  | 41 |
| 05 | &nbsp;&nbsp;WS-DSNTIAC-ERROR | 806 | 817 | 12 |  |  |  |  | 42 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-DSNTIAC-ERR-MSG | 806 | 815 | 10 |  | X(10) | DISPLAY |  | 43 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-DSNTIAC-ERR-CD-X | 816 | 817 | 2 |  | X(02) | DISPLAY |  | 44 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-DSNTIAC-ERR-CD | 816 | 817 | 2 |  | 9(02) | DISPLAY | WS-DSNTIAC-ERR-CD-X | 45 |

Notes: Copybook has no 01 level; offsets are relative to the COPY position
