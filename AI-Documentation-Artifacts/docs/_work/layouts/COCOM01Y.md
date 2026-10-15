### CARDDEMO-COMMAREA (length 160)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | CARDDEMO-COMMAREA | 1 | 160 | 160 |  |  |  |  | 19 |
| 05 | &nbsp;&nbsp;CDEMO-GENERAL-INFO | 1 | 34 | 34 |  |  |  |  | 20 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-FROM-TRANID | 1 | 4 | 4 |  | X(04) | DISPLAY |  | 21 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-FROM-PROGRAM | 5 | 12 | 8 |  | X(08) | DISPLAY |  | 22 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-TO-TRANID | 13 | 16 | 4 |  | X(04) | DISPLAY |  | 23 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-TO-PROGRAM | 17 | 24 | 8 |  | X(08) | DISPLAY |  | 24 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-USER-ID | 25 | 32 | 8 |  | X(08) | DISPLAY |  | 25 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-USER-TYPE | 33 | 33 | 1 |  | X(01) | DISPLAY |  | 26 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CDEMO-USRTYP-ADMIN = 'A' |  |  |  |  |  |  |  | 27 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CDEMO-USRTYP-USER = 'U' |  |  |  |  |  |  |  | 28 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-PGM-CONTEXT | 34 | 34 | 1 |  | 9(01) | DISPLAY |  | 29 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CDEMO-PGM-ENTER = 0 |  |  |  |  |  |  |  | 30 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CDEMO-PGM-REENTER = 1 |  |  |  |  |  |  |  | 31 |
| 05 | &nbsp;&nbsp;CDEMO-CUSTOMER-INFO | 35 | 118 | 84 |  |  |  |  | 32 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-CUST-ID | 35 | 43 | 9 |  | 9(09) | DISPLAY |  | 33 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-CUST-FNAME | 44 | 68 | 25 |  | X(25) | DISPLAY |  | 34 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-CUST-MNAME | 69 | 93 | 25 |  | X(25) | DISPLAY |  | 35 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-CUST-LNAME | 94 | 118 | 25 |  | X(25) | DISPLAY |  | 36 |
| 05 | &nbsp;&nbsp;CDEMO-ACCOUNT-INFO | 119 | 130 | 12 |  |  |  |  | 37 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-ACCT-ID | 119 | 129 | 11 |  | 9(11) | DISPLAY |  | 38 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-ACCT-STATUS | 130 | 130 | 1 |  | X(01) | DISPLAY |  | 39 |
| 05 | &nbsp;&nbsp;CDEMO-CARD-INFO | 131 | 146 | 16 |  |  |  |  | 40 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-CARD-NUM | 131 | 146 | 16 |  | 9(16) | DISPLAY |  | 41 |
| 05 | &nbsp;&nbsp;CDEMO-MORE-INFO | 147 | 160 | 14 |  |  |  |  | 42 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-LAST-MAP | 147 | 153 | 7 |  | X(7) | DISPLAY |  | 43 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-LAST-MAPSET | 154 | 160 | 7 |  | X(7) | DISPLAY |  | 44 |

