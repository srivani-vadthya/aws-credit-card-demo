### CC-WORK-AREAS (length 213)

| Lvl | Field | Start | End | Len | Occurs | PIC | Usage | Redefines | Line |
|---|---|---|---|---|---|---|---|---|---|
| 01 | CC-WORK-AREAS | 1 | 213 | 213 |  |  |  |  | 1 |
| 05 | &nbsp;&nbsp;CC-WORK-AREA | 1 | 213 | 213 |  |  |  |  | 2 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CCARD-AID | 1 | 5 | 5 |  | X(5) | DISPLAY |  | 3 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CCARD-AID-ENTER = 'ENTER' |  |  |  |  |  |  |  | 4 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CCARD-AID-CLEAR = 'CLEAR' |  |  |  |  |  |  |  | 5 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CCARD-AID-PA1 = 'PA1 ' |  |  |  |  |  |  |  | 6 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CCARD-AID-PA2 = 'PA2 ' |  |  |  |  |  |  |  | 7 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CCARD-AID-PFK01 = 'PFK01' |  |  |  |  |  |  |  | 8 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CCARD-AID-PFK02 = 'PFK02' |  |  |  |  |  |  |  | 9 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CCARD-AID-PFK03 = 'PFK03' |  |  |  |  |  |  |  | 10 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CCARD-AID-PFK04 = 'PFK04' |  |  |  |  |  |  |  | 11 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CCARD-AID-PFK05 = 'PFK05' |  |  |  |  |  |  |  | 12 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CCARD-AID-PFK06 = 'PFK06' |  |  |  |  |  |  |  | 13 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CCARD-AID-PFK07 = 'PFK07' |  |  |  |  |  |  |  | 14 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CCARD-AID-PFK08 = 'PFK08' |  |  |  |  |  |  |  | 15 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CCARD-AID-PFK09 = 'PFK09' |  |  |  |  |  |  |  | 16 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CCARD-AID-PFK10 = 'PFK10' |  |  |  |  |  |  |  | 17 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CCARD-AID-PFK11 = 'PFK11' |  |  |  |  |  |  |  | 18 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CCARD-AID-PFK12 = 'PFK12' |  |  |  |  |  |  |  | 19 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CCARD-NEXT-PROG | 6 | 13 | 8 |  | X(8) | DISPLAY |  | 21 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CCARD-NEXT-MAPSET | 14 | 20 | 7 |  | X(7) | DISPLAY |  | 23 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CCARD-NEXT-MAP | 21 | 27 | 7 |  | X(7) | DISPLAY |  | 24 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CCARD-ERROR-MSG | 28 | 102 | 75 |  | X(75) | DISPLAY |  | 28 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CCARD-RETURN-MSG | 103 | 177 | 75 |  | X(75) | DISPLAY |  | 29 |
| 88 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CCARD-RETURN-MSG-OFF = LOW-VALUES |  |  |  |  |  |  |  | 30 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CC-ACCT-ID | 178 | 188 | 11 |  | X(11) | DISPLAY |  | 34 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CC-ACCT-ID-N | 178 | 188 | 11 |  | 9(11) | DISPLAY | CC-ACCT-ID | 36 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CC-CARD-NUM | 189 | 204 | 16 |  | X(16) | DISPLAY |  | 37 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CC-CARD-NUM-N | 189 | 204 | 16 |  | 9(16) | DISPLAY | CC-CARD-NUM | 39 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CC-CUST-ID | 205 | 213 | 9 |  | X(09) | DISPLAY |  | 40 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CC-CUST-ID-N | 205 | 213 | 9 |  | 9(9) | DISPLAY | CC-CUST-ID | 42 |

