### (FRAGMENT) (length 100)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | (FRAGMENT) | 1 | 100 | 100 |  |  |  |  | 19 |
| 05 | &nbsp;&nbsp;PA-ACCT-ID | 1 | 6 | 6 |  | S9(11) | COMP-3 |  | 19 |
| 05 | &nbsp;&nbsp;PA-CUST-ID | 7 | 15 | 9 |  | 9(09) | DISPLAY |  | 20 |
| 05 | &nbsp;&nbsp;PA-AUTH-STATUS | 16 | 16 | 1 |  | X(01) | DISPLAY |  | 21 |
| 05 | &nbsp;&nbsp;PA-ACCOUNT-STATUS | 17 | 26 | 2 | 5 | X(02) | DISPLAY |  | 22 |
| 05 | &nbsp;&nbsp;PA-CREDIT-LIMIT | 27 | 32 | 6 |  | S9(09)V99 | COMP-3 |  | 23 |
| 05 | &nbsp;&nbsp;PA-CASH-LIMIT | 33 | 38 | 6 |  | S9(09)V99 | COMP-3 |  | 24 |
| 05 | &nbsp;&nbsp;PA-CREDIT-BALANCE | 39 | 44 | 6 |  | S9(09)V99 | COMP-3 |  | 25 |
| 05 | &nbsp;&nbsp;PA-CASH-BALANCE | 45 | 50 | 6 |  | S9(09)V99 | COMP-3 |  | 26 |
| 05 | &nbsp;&nbsp;PA-APPROVED-AUTH-CNT | 51 | 52 | 2 |  | S9(04) | COMP |  | 27 |
| 05 | &nbsp;&nbsp;PA-DECLINED-AUTH-CNT | 53 | 54 | 2 |  | S9(04) | COMP |  | 28 |
| 05 | &nbsp;&nbsp;PA-APPROVED-AUTH-AMT | 55 | 60 | 6 |  | S9(09)V99 | COMP-3 |  | 29 |
| 05 | &nbsp;&nbsp;PA-DECLINED-AUTH-AMT | 61 | 66 | 6 |  | S9(09)V99 | COMP-3 |  | 30 |
| 05 | &nbsp;&nbsp;FILLER | 67 | 100 | 34 |  | X(34) | DISPLAY |  | 31 |

Notes: Copybook has no 01 level; offsets are relative to the COPY position
