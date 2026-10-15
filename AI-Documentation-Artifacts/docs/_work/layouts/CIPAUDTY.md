### (FRAGMENT) (length 200)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | (FRAGMENT) | 1 | 200 | 200 |  |  |  |  | 19 |
| 05 | &nbsp;&nbsp;PA-AUTHORIZATION-KEY | 1 | 8 | 8 |  |  |  |  | 19 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;PA-AUTH-DATE-9C | 1 | 3 | 3 |  | S9(05) | COMP-3 |  | 20 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;PA-AUTH-TIME-9C | 4 | 8 | 5 |  | S9(09) | COMP-3 |  | 21 |
| 05 | &nbsp;&nbsp;PA-AUTH-ORIG-DATE | 9 | 14 | 6 |  | X(06) | DISPLAY |  | 22 |
| 05 | &nbsp;&nbsp;PA-AUTH-ORIG-TIME | 15 | 20 | 6 |  | X(06) | DISPLAY |  | 23 |
| 05 | &nbsp;&nbsp;PA-CARD-NUM | 21 | 36 | 16 |  | X(16) | DISPLAY |  | 24 |
| 05 | &nbsp;&nbsp;PA-AUTH-TYPE | 37 | 40 | 4 |  | X(04) | DISPLAY |  | 25 |
| 05 | &nbsp;&nbsp;PA-CARD-EXPIRY-DATE | 41 | 44 | 4 |  | X(04) | DISPLAY |  | 26 |
| 05 | &nbsp;&nbsp;PA-MESSAGE-TYPE | 45 | 50 | 6 |  | X(06) | DISPLAY |  | 27 |
| 05 | &nbsp;&nbsp;PA-MESSAGE-SOURCE | 51 | 56 | 6 |  | X(06) | DISPLAY |  | 28 |
| 05 | &nbsp;&nbsp;PA-AUTH-ID-CODE | 57 | 62 | 6 |  | X(06) | DISPLAY |  | 29 |
| 05 | &nbsp;&nbsp;PA-AUTH-RESP-CODE | 63 | 64 | 2 |  | X(02) | DISPLAY |  | 30 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;PA-AUTH-APPROVED = '00' |  |  |  |  |  |  |  | 31 |
| 05 | &nbsp;&nbsp;PA-AUTH-RESP-REASON | 65 | 68 | 4 |  | X(04) | DISPLAY |  | 32 |
| 05 | &nbsp;&nbsp;PA-PROCESSING-CODE | 69 | 74 | 6 |  | 9(06) | DISPLAY |  | 33 |
| 05 | &nbsp;&nbsp;PA-TRANSACTION-AMT | 75 | 81 | 7 |  | S9(10)V99 | COMP-3 |  | 34 |
| 05 | &nbsp;&nbsp;PA-APPROVED-AMT | 82 | 88 | 7 |  | S9(10)V99 | COMP-3 |  | 35 |
| 05 | &nbsp;&nbsp;PA-MERCHANT-CATAGORY-CODE | 89 | 92 | 4 |  | X(04) | DISPLAY |  | 36 |
| 05 | &nbsp;&nbsp;PA-ACQR-COUNTRY-CODE | 93 | 95 | 3 |  | X(03) | DISPLAY |  | 37 |
| 05 | &nbsp;&nbsp;PA-POS-ENTRY-MODE | 96 | 97 | 2 |  | 9(02) | DISPLAY |  | 38 |
| 05 | &nbsp;&nbsp;PA-MERCHANT-ID | 98 | 112 | 15 |  | X(15) | DISPLAY |  | 39 |
| 05 | &nbsp;&nbsp;PA-MERCHANT-NAME | 113 | 134 | 22 |  | X(22) | DISPLAY |  | 40 |
| 05 | &nbsp;&nbsp;PA-MERCHANT-CITY | 135 | 147 | 13 |  | X(13) | DISPLAY |  | 41 |
| 05 | &nbsp;&nbsp;PA-MERCHANT-STATE | 148 | 149 | 2 |  | X(02) | DISPLAY |  | 42 |
| 05 | &nbsp;&nbsp;PA-MERCHANT-ZIP | 150 | 158 | 9 |  | X(09) | DISPLAY |  | 43 |
| 05 | &nbsp;&nbsp;PA-TRANSACTION-ID | 159 | 173 | 15 |  | X(15) | DISPLAY |  | 44 |
| 05 | &nbsp;&nbsp;PA-MATCH-STATUS | 174 | 174 | 1 |  | X(01) | DISPLAY |  | 45 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;PA-MATCH-PENDING = 'P' |  |  |  |  |  |  |  | 46 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;PA-MATCH-AUTH-DECLINED = 'D' |  |  |  |  |  |  |  | 47 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;PA-MATCH-PENDING-EXPIRED = 'E' |  |  |  |  |  |  |  | 48 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;PA-MATCHED-WITH-TRAN = 'M' |  |  |  |  |  |  |  | 49 |
| 05 | &nbsp;&nbsp;PA-AUTH-FRAUD | 175 | 175 | 1 |  | X(01) | DISPLAY |  | 50 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;PA-FRAUD-CONFIRMED = 'F' |  |  |  |  |  |  |  | 51 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;PA-FRAUD-REMOVED = 'R' |  |  |  |  |  |  |  | 52 |
| 05 | &nbsp;&nbsp;PA-FRAUD-RPT-DATE | 176 | 183 | 8 |  | X(08) | DISPLAY |  | 53 |
| 05 | &nbsp;&nbsp;FILLER | 184 | 200 | 17 |  | X(17) | DISPLAY |  | 54 |

Notes: Copybook has no 01 level; offsets are relative to the COPY position
