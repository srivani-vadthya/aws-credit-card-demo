### (FRAGMENT) (length 153)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | (FRAGMENT) | 1 | 153 | 153 |  |  |  |  | 19 |
| 05 | &nbsp;&nbsp;PA-RQ-AUTH-DATE | 1 | 6 | 6 |  | X(06) | DISPLAY |  | 19 |
| 05 | &nbsp;&nbsp;PA-RQ-AUTH-TIME | 7 | 12 | 6 |  | X(06) | DISPLAY |  | 20 |
| 05 | &nbsp;&nbsp;PA-RQ-CARD-NUM | 13 | 28 | 16 |  | X(16) | DISPLAY |  | 21 |
| 05 | &nbsp;&nbsp;PA-RQ-AUTH-TYPE | 29 | 32 | 4 |  | X(04) | DISPLAY |  | 22 |
| 05 | &nbsp;&nbsp;PA-RQ-CARD-EXPIRY-DATE | 33 | 36 | 4 |  | X(04) | DISPLAY |  | 23 |
| 05 | &nbsp;&nbsp;PA-RQ-MESSAGE-TYPE | 37 | 42 | 6 |  | X(06) | DISPLAY |  | 24 |
| 05 | &nbsp;&nbsp;PA-RQ-MESSAGE-SOURCE | 43 | 48 | 6 |  | X(06) | DISPLAY |  | 25 |
| 05 | &nbsp;&nbsp;PA-RQ-PROCESSING-CODE | 49 | 54 | 6 |  | 9(06) | DISPLAY |  | 26 |
| 05 | &nbsp;&nbsp;PA-RQ-TRANSACTION-AMT | 55 | 68 | 14 |  | +9(10).99 | DISPLAY |  | 27 |
| 05 | &nbsp;&nbsp;PA-RQ-MERCHANT-CATAGORY-CODE | 69 | 72 | 4 |  | X(04) | DISPLAY |  | 28 |
| 05 | &nbsp;&nbsp;PA-RQ-ACQR-COUNTRY-CODE | 73 | 75 | 3 |  | X(03) | DISPLAY |  | 29 |
| 05 | &nbsp;&nbsp;PA-RQ-POS-ENTRY-MODE | 76 | 77 | 2 |  | 9(02) | DISPLAY |  | 30 |
| 05 | &nbsp;&nbsp;PA-RQ-MERCHANT-ID | 78 | 92 | 15 |  | X(15) | DISPLAY |  | 31 |
| 05 | &nbsp;&nbsp;PA-RQ-MERCHANT-NAME | 93 | 114 | 22 |  | X(22) | DISPLAY |  | 32 |
| 05 | &nbsp;&nbsp;PA-RQ-MERCHANT-CITY | 115 | 127 | 13 |  | X(13) | DISPLAY |  | 33 |
| 05 | &nbsp;&nbsp;PA-RQ-MERCHANT-STATE | 128 | 129 | 2 |  | X(02) | DISPLAY |  | 34 |
| 05 | &nbsp;&nbsp;PA-RQ-MERCHANT-ZIP | 130 | 138 | 9 |  | X(09) | DISPLAY |  | 35 |
| 05 | &nbsp;&nbsp;PA-RQ-TRANSACTION-ID | 139 | 153 | 15 |  | X(15) | DISPLAY |  | 36 |

Notes: Copybook has no 01 level; offsets are relative to the COPY position
