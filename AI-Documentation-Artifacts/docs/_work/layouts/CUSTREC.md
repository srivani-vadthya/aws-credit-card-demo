### CUSTOMER-RECORD (length 500)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | CUSTOMER-RECORD | 1 | 500 | 500 |  |  |  |  | 4 |
| 05 | &nbsp;&nbsp;CUST-ID | 1 | 9 | 9 |  | 9(09) | DISPLAY |  | 5 |
| 05 | &nbsp;&nbsp;CUST-FIRST-NAME | 10 | 34 | 25 |  | X(25) | DISPLAY |  | 6 |
| 05 | &nbsp;&nbsp;CUST-MIDDLE-NAME | 35 | 59 | 25 |  | X(25) | DISPLAY |  | 7 |
| 05 | &nbsp;&nbsp;CUST-LAST-NAME | 60 | 84 | 25 |  | X(25) | DISPLAY |  | 8 |
| 05 | &nbsp;&nbsp;CUST-ADDR-LINE-1 | 85 | 134 | 50 |  | X(50) | DISPLAY |  | 9 |
| 05 | &nbsp;&nbsp;CUST-ADDR-LINE-2 | 135 | 184 | 50 |  | X(50) | DISPLAY |  | 10 |
| 05 | &nbsp;&nbsp;CUST-ADDR-LINE-3 | 185 | 234 | 50 |  | X(50) | DISPLAY |  | 11 |
| 05 | &nbsp;&nbsp;CUST-ADDR-STATE-CD | 235 | 236 | 2 |  | X(02) | DISPLAY |  | 12 |
| 05 | &nbsp;&nbsp;CUST-ADDR-COUNTRY-CD | 237 | 239 | 3 |  | X(03) | DISPLAY |  | 13 |
| 05 | &nbsp;&nbsp;CUST-ADDR-ZIP | 240 | 249 | 10 |  | X(10) | DISPLAY |  | 14 |
| 05 | &nbsp;&nbsp;CUST-PHONE-NUM-1 | 250 | 264 | 15 |  | X(15) | DISPLAY |  | 15 |
| 05 | &nbsp;&nbsp;CUST-PHONE-NUM-2 | 265 | 279 | 15 |  | X(15) | DISPLAY |  | 16 |
| 05 | &nbsp;&nbsp;CUST-SSN | 280 | 288 | 9 |  | 9(09) | DISPLAY |  | 17 |
| 05 | &nbsp;&nbsp;CUST-GOVT-ISSUED-ID | 289 | 308 | 20 |  | X(20) | DISPLAY |  | 18 |
| 05 | &nbsp;&nbsp;CUST-DOB-YYYYMMDD | 309 | 318 | 10 |  | X(10) | DISPLAY |  | 19 |
| 05 | &nbsp;&nbsp;CUST-EFT-ACCOUNT-ID | 319 | 328 | 10 |  | X(10) | DISPLAY |  | 20 |
| 05 | &nbsp;&nbsp;CUST-PRI-CARD-HOLDER-IND | 329 | 329 | 1 |  | X(01) | DISPLAY |  | 21 |
| 05 | &nbsp;&nbsp;CUST-FICO-CREDIT-SCORE | 330 | 332 | 3 |  | 9(03) | DISPLAY |  | 22 |
| 05 | &nbsp;&nbsp;FILLER | 333 | 500 | 168 |  | X(168) | DISPLAY |  | 23 |

