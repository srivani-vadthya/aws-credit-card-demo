### DCLAUTHFRDS (length 204)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | DCLAUTHFRDS | 1 | 204 | 204 |  |  |  |  | 55 |
| 10 | &nbsp;&nbsp;CARD-NUM | 1 | 16 | 16 |  | X(16) | DISPLAY |  | 56 |
| 10 | &nbsp;&nbsp;AUTH-TS | 17 | 42 | 26 |  | X(26) | DISPLAY |  | 57 |
| 10 | &nbsp;&nbsp;AUTH-TYPE | 43 | 46 | 4 |  | X(4) | DISPLAY |  | 58 |
| 10 | &nbsp;&nbsp;CARD-EXPIRY-DATE | 47 | 50 | 4 |  | X(4) | DISPLAY |  | 59 |
| 10 | &nbsp;&nbsp;MESSAGE-TYPE | 51 | 56 | 6 |  | X(6) | DISPLAY |  | 60 |
| 10 | &nbsp;&nbsp;MESSAGE-SOURCE | 57 | 62 | 6 |  | X(6) | DISPLAY |  | 61 |
| 10 | &nbsp;&nbsp;AUTH-ID-CODE | 63 | 68 | 6 |  | X(6) | DISPLAY |  | 62 |
| 10 | &nbsp;&nbsp;AUTH-RESP-CODE | 69 | 70 | 2 |  | X(2) | DISPLAY |  | 63 |
| 10 | &nbsp;&nbsp;AUTH-RESP-REASON | 71 | 74 | 4 |  | X(4) | DISPLAY |  | 64 |
| 10 | &nbsp;&nbsp;PROCESSING-CODE | 75 | 80 | 6 |  | X(6) | DISPLAY |  | 65 |
| 10 | &nbsp;&nbsp;TRANSACTION-AMT | 81 | 87 | 7 |  | S9(10)V9(2) | COMP-3 |  | 66 |
| 10 | &nbsp;&nbsp;APPROVED-AMT | 88 | 94 | 7 |  | S9(10)V9(2) | COMP-3 |  | 67 |
| 10 | &nbsp;&nbsp;MERCHANT-CATAGORY-CODE | 95 | 98 | 4 |  | X(4) | DISPLAY |  | 68 |
| 10 | &nbsp;&nbsp;ACQR-COUNTRY-CODE | 99 | 101 | 3 |  | X(3) | DISPLAY |  | 70 |
| 10 | &nbsp;&nbsp;POS-ENTRY-MODE | 102 | 103 | 2 |  | S9(4) | COMP |  | 71 |
| 10 | &nbsp;&nbsp;MERCHANT-ID | 104 | 118 | 15 |  | X(15) | DISPLAY |  | 72 |
| 10 | &nbsp;&nbsp;MERCHANT-NAME | 119 | 142 | 24 |  |  |  |  | 73 |
| 49 | &nbsp;&nbsp;&nbsp;&nbsp;MERCHANT-NAME-LEN | 119 | 120 | 2 |  | S9(4) | COMP |  | 74 |
| 49 | &nbsp;&nbsp;&nbsp;&nbsp;MERCHANT-NAME-TEXT | 121 | 142 | 22 |  | X(22) | DISPLAY |  | 76 |
| 10 | &nbsp;&nbsp;MERCHANT-CITY | 143 | 155 | 13 |  | X(13) | DISPLAY |  | 78 |
| 10 | &nbsp;&nbsp;MERCHANT-STATE | 156 | 157 | 2 |  | X(2) | DISPLAY |  | 79 |
| 10 | &nbsp;&nbsp;MERCHANT-ZIP | 158 | 166 | 9 |  | X(9) | DISPLAY |  | 80 |
| 10 | &nbsp;&nbsp;TRANSACTION-ID | 167 | 181 | 15 |  | X(15) | DISPLAY |  | 81 |
| 10 | &nbsp;&nbsp;MATCH-STATUS | 182 | 182 | 1 |  | X(1) | DISPLAY |  | 82 |
| 10 | &nbsp;&nbsp;AUTH-FRAUD | 183 | 183 | 1 |  | X(1) | DISPLAY |  | 83 |
| 10 | &nbsp;&nbsp;FRAUD-RPT-DATE | 184 | 193 | 10 |  | X(10) | DISPLAY |  | 84 |
| 10 | &nbsp;&nbsp;ACCT-ID | 194 | 199 | 6 |  | S9(11)V | COMP-3 |  | 85 |
| 10 | &nbsp;&nbsp;CUST-ID | 200 | 204 | 5 |  | S9(9)V | COMP-3 |  | 86 |

