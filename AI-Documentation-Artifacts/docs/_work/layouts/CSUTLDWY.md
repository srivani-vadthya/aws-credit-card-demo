### (FRAGMENT) (length 115)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | (FRAGMENT) | 1 | 115 | 115 |  |  |  |  | 4 |
| 10 | &nbsp;&nbsp;WS-EDIT-DATE-CCYYMMDD | 1 | 8 | 8 |  |  |  |  | 4 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-EDIT-DATE-CCYY | 1 | 4 | 4 |  |  |  |  | 5 |
| 25 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-EDIT-DATE-CC | 1 | 2 | 2 |  | X(2) | DISPLAY |  | 6 |
| 25 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-EDIT-DATE-CC-N | 1 | 2 | 2 |  | 9(2) | DISPLAY | WS-EDIT-DATE-CC | 7 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;THIS-CENTURY = 20 |  |  |  |  |  |  |  | 9 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LAST-CENTURY = 19 |  |  |  |  |  |  |  | 10 |
| 25 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-EDIT-DATE-YY | 3 | 4 | 2 |  | X(2) | DISPLAY |  | 11 |
| 25 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-EDIT-DATE-YY-N | 3 | 4 | 2 |  | 9(2) | DISPLAY | WS-EDIT-DATE-YY | 12 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-EDIT-DATE-CCYY-N | 1 | 4 | 4 |  | 9(4) | DISPLAY | WS-EDIT-DATE-CCYY | 14 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-EDIT-DATE-MM | 5 | 6 | 2 |  | X(2) | DISPLAY |  | 16 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-EDIT-DATE-MM-N | 5 | 6 | 2 |  | 9(2) | DISPLAY | WS-EDIT-DATE-MM | 17 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-VALID-MONTH = 1 THROUGH 12 |  |  |  |  |  |  |  | 19 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-31-DAY-MONTH = 1, 3, 5, 7, 8, 10, 12 |  |  |  |  |  |  |  | 21 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-FEBRUARY = 2 |  |  |  |  |  |  |  | 24 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-EDIT-DATE-DD | 7 | 8 | 2 |  | X(2) | DISPLAY |  | 25 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-EDIT-DATE-DD-N | 7 | 8 | 2 |  | 9(2) | DISPLAY | WS-EDIT-DATE-DD | 26 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-VALID-DAY = 1 THROUGH 31 |  |  |  |  |  |  |  | 28 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-DAY-31 = 31 |  |  |  |  |  |  |  | 30 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-DAY-30 = 30 |  |  |  |  |  |  |  | 31 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-DAY-29 = 29 |  |  |  |  |  |  |  | 32 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-VALID-FEB-DAY = 1 THROUGH 28 |  |  |  |  |  |  |  | 33 |
| 10 | &nbsp;&nbsp;WS-EDIT-DATE-CCYYMMDD-N | 1 | 8 | 8 |  | 9(8) | DISPLAY | WS-EDIT-DATE-CCYYMMDD | 35 |
| 10 | &nbsp;&nbsp;WS-EDIT-DATE-BINARY | 9 | 12 | 4 |  | S9(9) | BINARY |  | 37 |
| 10 | &nbsp;&nbsp;WS-CURRENT-DATE | 13 | 24 | 12 |  |  |  |  | 38 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-CURRENT-DATE-YYYYMMDD | 13 | 20 | 8 |  | X(8) | DISPLAY |  | 39 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-CURRENT-DATE-YYYYMMDD-N | 13 | 20 | 8 |  | 9(8) | DISPLAY | WS-CURRENT-DATE-YYYYMMDD | 40 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-CURRENT-DATE-BINARY | 21 | 24 | 4 |  | S9(9) | BINARY |  | 42 |
| 10 | &nbsp;&nbsp;WS-EDIT-DATE-FLGS | 25 | 27 | 3 |  |  |  |  | 43 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;WS-EDIT-DATE-IS-VALID = LOW-VALUES |  |  |  |  |  |  |  | 44 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;WS-EDIT-DATE-IS-INVALID = '000' |  |  |  |  |  |  |  | 45 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-EDIT-YEAR-FLG | 25 | 25 | 1 |  | X(01) | DISPLAY |  | 46 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FLG-YEAR-ISVALID = LOW-VALUES |  |  |  |  |  |  |  | 47 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FLG-YEAR-NOT-OK = '0' |  |  |  |  |  |  |  | 48 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FLG-YEAR-BLANK = 'B' |  |  |  |  |  |  |  | 49 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-EDIT-MONTH | 26 | 26 | 1 |  | X(01) | DISPLAY |  | 50 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FLG-MONTH-ISVALID = LOW-VALUES |  |  |  |  |  |  |  | 51 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FLG-MONTH-NOT-OK = '0' |  |  |  |  |  |  |  | 52 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FLG-MONTH-BLANK = 'B' |  |  |  |  |  |  |  | 53 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-EDIT-DAY | 27 | 27 | 1 |  | X(01) | DISPLAY |  | 54 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FLG-DAY-ISVALID = LOW-VALUES |  |  |  |  |  |  |  | 55 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FLG-DAY-NOT-OK = '0' |  |  |  |  |  |  |  | 56 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FLG-DAY-BLANK = 'B' |  |  |  |  |  |  |  | 57 |
| 10 | &nbsp;&nbsp;WS-DATE-FORMAT | 28 | 35 | 8 |  | X(08) | DISPLAY |  | 58 |
| 10 | &nbsp;&nbsp;WS-DATE-VALIDATION-RESULT | 36 | 115 | 80 |  |  |  |  | 60 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-SEVERITY | 36 | 39 | 4 |  | X(04) | DISPLAY |  | 61 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-SEVERITY-N | 36 | 39 | 4 |  | 9(4) | DISPLAY | WS-SEVERITY | 62 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 40 | 50 | 11 |  | X(11) | DISPLAY |  | 64 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-MSG-NO | 51 | 54 | 4 |  | X(04) | DISPLAY |  | 66 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-MSG-NO-N | 51 | 54 | 4 |  | 9(4) | DISPLAY | WS-MSG-NO | 67 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 55 | 55 | 1 |  | X(01) | DISPLAY |  | 69 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-RESULT | 56 | 70 | 15 |  | X(15) | DISPLAY |  | 71 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 71 | 71 | 1 |  | X(01) | DISPLAY |  | 72 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 72 | 80 | 9 |  | X(09) | DISPLAY |  | 74 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-DATE | 81 | 90 | 10 |  | X(10) | DISPLAY |  | 76 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 91 | 91 | 1 |  | X(01) | DISPLAY |  | 77 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 92 | 101 | 10 |  | X(10) | DISPLAY |  | 79 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-DATE-FMT | 102 | 111 | 10 |  | X(10) | DISPLAY |  | 81 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 112 | 112 | 1 |  | X(01) | DISPLAY |  | 82 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 113 | 115 | 3 |  | X(03) | DISPLAY |  | 84 |

Notes: Copybook has no 01 level; offsets are relative to the COPY position
