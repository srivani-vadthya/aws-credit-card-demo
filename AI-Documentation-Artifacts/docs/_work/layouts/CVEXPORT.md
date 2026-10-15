### EXPORT-RECORD (length 500)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | EXPORT-RECORD | 1 | 500 | 500 |  |  |  |  | 9 |
| 05 | &nbsp;&nbsp;EXPORT-REC-TYPE | 1 | 1 | 1 |  | X(1) | DISPLAY |  | 10 |
| 05 | &nbsp;&nbsp;EXPORT-TIMESTAMP | 2 | 27 | 26 |  | X(26) | DISPLAY |  | 11 |
| 05 | &nbsp;&nbsp;EXPORT-TIMESTAMP-R | 2 | 27 | 26 |  |  |  | EXPORT-TIMESTAMP | 12 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXPORT-DATE | 2 | 11 | 10 |  | X(10) | DISPLAY |  | 13 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXPORT-DATE-TIME-SEP | 12 | 12 | 1 |  | X(1) | DISPLAY |  | 14 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXPORT-TIME | 13 | 27 | 15 |  | X(15) | DISPLAY |  | 15 |
| 05 | &nbsp;&nbsp;EXPORT-SEQUENCE-NUM | 28 | 31 | 4 |  | 9(9) | COMP |  | 16 |
| 05 | &nbsp;&nbsp;EXPORT-BRANCH-ID | 32 | 35 | 4 |  | X(4) | DISPLAY |  | 17 |
| 05 | &nbsp;&nbsp;EXPORT-REGION-CODE | 36 | 40 | 5 |  | X(5) | DISPLAY |  | 18 |
| 05 | &nbsp;&nbsp;EXPORT-RECORD-DATA | 41 | 500 | 460 |  | X(460) | DISPLAY |  | 19 |
| 05 | &nbsp;&nbsp;EXPORT-CUSTOMER-DATA | 41 | 500 | 460 |  |  |  | EXPORT-RECORD-DATA | 24 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-ID | 41 | 44 | 4 |  | 9(09) | COMP |  | 25 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-FIRST-NAME | 45 | 69 | 25 |  | X(25) | DISPLAY |  | 26 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-MIDDLE-NAME | 70 | 94 | 25 |  | X(25) | DISPLAY |  | 27 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-LAST-NAME | 95 | 119 | 25 |  | X(25) | DISPLAY |  | 28 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-ADDR-LINES | 120 | 269 | 50 | 3 |  |  |  | 29 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-ADDR-LINE | 120 | 169 | 50 |  | X(50) | DISPLAY |  | 30 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-ADDR-STATE-CD | 270 | 271 | 2 |  | X(02) | DISPLAY |  | 31 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-ADDR-COUNTRY-CD | 272 | 274 | 3 |  | X(03) | DISPLAY |  | 32 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-ADDR-ZIP | 275 | 284 | 10 |  | X(10) | DISPLAY |  | 33 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-PHONE-NUMS | 285 | 314 | 15 | 2 |  |  |  | 34 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-PHONE-NUM | 285 | 299 | 15 |  | X(15) | DISPLAY |  | 35 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-SSN | 315 | 323 | 9 |  | 9(09) | DISPLAY |  | 36 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-GOVT-ISSUED-ID | 324 | 343 | 20 |  | X(20) | DISPLAY |  | 37 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-DOB-YYYY-MM-DD | 344 | 353 | 10 |  | X(10) | DISPLAY |  | 38 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-EFT-ACCOUNT-ID | 354 | 363 | 10 |  | X(10) | DISPLAY |  | 39 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-PRI-CARD-HOLDER-IND | 364 | 364 | 1 |  | X(01) | DISPLAY |  | 40 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-FICO-CREDIT-SCORE | 365 | 366 | 2 |  | 9(03) | COMP-3 |  | 41 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 367 | 500 | 134 |  | X(134) | DISPLAY |  | 42 |
| 05 | &nbsp;&nbsp;EXPORT-ACCOUNT-DATA | 41 | 500 | 460 |  |  |  | EXPORT-RECORD-DATA | 47 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-ACCT-ID | 41 | 51 | 11 |  | 9(11) | DISPLAY |  | 48 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-ACCT-ACTIVE-STATUS | 52 | 52 | 1 |  | X(01) | DISPLAY |  | 49 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-ACCT-CURR-BAL | 53 | 59 | 7 |  | S9(10)V99 | COMP-3 |  | 50 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-ACCT-CREDIT-LIMIT | 60 | 71 | 12 |  | S9(10)V99 | DISPLAY |  | 51 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-ACCT-CASH-CREDIT-LIMIT | 72 | 78 | 7 |  | S9(10)V99 | COMP-3 |  | 52 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-ACCT-OPEN-DATE | 79 | 88 | 10 |  | X(10) | DISPLAY |  | 53 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-ACCT-EXPIRAION-DATE | 89 | 98 | 10 |  | X(10) | DISPLAY |  | 54 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-ACCT-REISSUE-DATE | 99 | 108 | 10 |  | X(10) | DISPLAY |  | 55 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-ACCT-CURR-CYC-CREDIT | 109 | 120 | 12 |  | S9(10)V99 | DISPLAY |  | 56 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-ACCT-CURR-CYC-DEBIT | 121 | 128 | 8 |  | S9(10)V99 | COMP |  | 57 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-ACCT-ADDR-ZIP | 129 | 138 | 10 |  | X(10) | DISPLAY |  | 58 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-ACCT-GROUP-ID | 139 | 148 | 10 |  | X(10) | DISPLAY |  | 59 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 149 | 500 | 352 |  | X(352) | DISPLAY |  | 60 |
| 05 | &nbsp;&nbsp;EXPORT-TRANSACTION-DATA | 41 | 500 | 460 |  |  |  | EXPORT-RECORD-DATA | 65 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-TRAN-ID | 41 | 56 | 16 |  | X(16) | DISPLAY |  | 66 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-TRAN-TYPE-CD | 57 | 58 | 2 |  | X(02) | DISPLAY |  | 67 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-TRAN-CAT-CD | 59 | 62 | 4 |  | 9(04) | DISPLAY |  | 68 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-TRAN-SOURCE | 63 | 72 | 10 |  | X(10) | DISPLAY |  | 69 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-TRAN-DESC | 73 | 172 | 100 |  | X(100) | DISPLAY |  | 70 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-TRAN-AMT | 173 | 178 | 6 |  | S9(09)V99 | COMP-3 |  | 71 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-TRAN-MERCHANT-ID | 179 | 182 | 4 |  | 9(09) | COMP |  | 72 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-TRAN-MERCHANT-NAME | 183 | 232 | 50 |  | X(50) | DISPLAY |  | 73 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-TRAN-MERCHANT-CITY | 233 | 282 | 50 |  | X(50) | DISPLAY |  | 74 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-TRAN-MERCHANT-ZIP | 283 | 292 | 10 |  | X(10) | DISPLAY |  | 75 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-TRAN-CARD-NUM | 293 | 308 | 16 |  | X(16) | DISPLAY |  | 76 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-TRAN-ORIG-TS | 309 | 334 | 26 |  | X(26) | DISPLAY |  | 77 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-TRAN-PROC-TS | 335 | 360 | 26 |  | X(26) | DISPLAY |  | 78 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 361 | 500 | 140 |  | X(140) | DISPLAY |  | 79 |
| 05 | &nbsp;&nbsp;EXPORT-CARD-XREF-DATA | 41 | 500 | 460 |  |  |  | EXPORT-RECORD-DATA | 84 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-XREF-CARD-NUM | 41 | 56 | 16 |  | X(16) | DISPLAY |  | 85 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-XREF-CUST-ID | 57 | 65 | 9 |  | 9(09) | DISPLAY |  | 86 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-XREF-ACCT-ID | 66 | 73 | 8 |  | 9(11) | COMP |  | 87 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 74 | 500 | 427 |  | X(427) | DISPLAY |  | 88 |
| 05 | &nbsp;&nbsp;EXPORT-CARD-DATA | 41 | 500 | 460 |  |  |  | EXPORT-RECORD-DATA | 93 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CARD-NUM | 41 | 56 | 16 |  | X(16) | DISPLAY |  | 94 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CARD-ACCT-ID | 57 | 64 | 8 |  | 9(11) | COMP |  | 95 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CARD-CVV-CD | 65 | 66 | 2 |  | 9(03) | COMP |  | 96 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CARD-EMBOSSED-NAME | 67 | 116 | 50 |  | X(50) | DISPLAY |  | 97 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CARD-EXPIRAION-DATE | 117 | 126 | 10 |  | X(10) | DISPLAY |  | 98 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CARD-ACTIVE-STATUS | 127 | 127 | 1 |  | X(01) | DISPLAY |  | 99 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 128 | 500 | 373 |  | X(373) | DISPLAY |  | 100 |

