### ACCOUNT-RECORD (length 300)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | ACCOUNT-RECORD | 1 | 300 | 300 |  |  |  |  | 4 |
| 05 | &nbsp;&nbsp;ACCT-ID | 1 | 11 | 11 |  | 9(11) | DISPLAY |  | 5 |
| 05 | &nbsp;&nbsp;ACCT-ACTIVE-STATUS | 12 | 12 | 1 |  | X(01) | DISPLAY |  | 6 |
| 05 | &nbsp;&nbsp;ACCT-CURR-BAL | 13 | 24 | 12 |  | S9(10)V99 | DISPLAY |  | 7 |
| 05 | &nbsp;&nbsp;ACCT-CREDIT-LIMIT | 25 | 36 | 12 |  | S9(10)V99 | DISPLAY |  | 8 |
| 05 | &nbsp;&nbsp;ACCT-CASH-CREDIT-LIMIT | 37 | 48 | 12 |  | S9(10)V99 | DISPLAY |  | 9 |
| 05 | &nbsp;&nbsp;ACCT-OPEN-DATE | 49 | 58 | 10 |  | X(10) | DISPLAY |  | 10 |
| 05 | &nbsp;&nbsp;ACCT-EXPIRAION-DATE | 59 | 68 | 10 |  | X(10) | DISPLAY |  | 11 |
| 05 | &nbsp;&nbsp;ACCT-REISSUE-DATE | 69 | 78 | 10 |  | X(10) | DISPLAY |  | 12 |
| 05 | &nbsp;&nbsp;ACCT-CURR-CYC-CREDIT | 79 | 90 | 12 |  | S9(10)V99 | DISPLAY |  | 13 |
| 05 | &nbsp;&nbsp;ACCT-CURR-CYC-DEBIT | 91 | 102 | 12 |  | S9(10)V99 | DISPLAY |  | 14 |
| 05 | &nbsp;&nbsp;ACCT-ADDR-ZIP | 103 | 112 | 10 |  | X(10) | DISPLAY |  | 15 |
| 05 | &nbsp;&nbsp;ACCT-GROUP-ID | 113 | 122 | 10 |  | X(10) | DISPLAY |  | 16 |
| 05 | &nbsp;&nbsp;FILLER | 123 | 300 | 178 |  | X(178) | DISPLAY |  | 17 |

