# COACTUPC

Draft from `docs/_work/rules/rules.json`.

## BR-BASE-003

The card update and account update programs run every field edit, but each edit writes its message only when no message is set yet. The screen therefore shows the first failing edit in edit order.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COACTUPC.cbl:480`, `app/cbl/COACTUPC.cbl:1805-1812`

## BR-BASE-004

When no field edit sets INPUT-ERROR, the card update and account update programs mark the changes as validated but not yet confirmed.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COACTUPC.cbl:1671-1675`

## BR-BASE-COACTUPC-001

Before account details are fetched, a blank account number is reported as not provided, and the message becomes No input received. A supplied account number that is not numeric or is zero is rejected.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COACTUPC.cbl:1433-1446`, `app/cbl/COACTUPC.cbl:1783-1818`, `app/cbl/COACTUPC.cbl:483-490`

## BR-BASE-COACTUPC-002

No change is reported when every account and customer field equals the fetched value. Text fields are compared after trim and upper case. Amounts, dates, phone parts, SSN, EFT account and FICO score are compared exactly. Field edits are then skipped.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COACTUPC.cbl:1681-1775`, `app/cbl/COACTUPC.cbl:1460-1467`, `app/cbl/COACTUPC.cbl:491-492`

## BR-BASE-COACTUPC-003

Account Status and Primary Card Holder are required and must be Y or N. Low-values, spaces or zeros count as not supplied.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COACTUPC.cbl:1472-1476`, `app/cbl/COACTUPC.cbl:1657-1662`, `app/cbl/COACTUPC.cbl:1856-1892`

## BR-BASE-COACTUPC-004

Credit Limit, Cash Credit Limit, Current Balance, Current Cycle Credit and Current Cycle Debit are required and must pass the TEST-NUMVAL-C numeric test.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COACTUPC.cbl:1484-1527`, `app/cbl/COACTUPC.cbl:2180-2219`

## BR-BASE-COACTUPC-005

A date year is required, must be numeric, and its century must be 19 or 20. The month is required and must be 1 through 12. The day is required and must be 1 through 31.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COACTUPC.cbl:1478-1507`, `app/cbl/COACTUPC.cbl:1533-1538`, `app/cpy/CSUTLDPY.cpy:25-205`, `app/cpy/CSUTLDWY.cpy:9-32`

## BR-BASE-COACTUPC-006

Day 31 is rejected outside months 1, 3, 5, 7, 8, 10 and 12. Day 30 is rejected in February. Day 29 in February is accepted only in a leap year: a year ending in 00 must divide by 400, any other year by 4.

- Category: validation
- Confidence: Confirmed
- Source: `app/cpy/CSUTLDPY.cpy:209-272`, `app/cpy/CSUTLDWY.cpy:21-32`

## BR-BASE-COACTUPC-007

A date that passes the year, month and day edits is checked again by CALL CSUTLDTC with format YYYYMMDD. A non-zero severity rejects the date.

- Category: validation
- Confidence: Confirmed
- Source: `app/cpy/CSUTLDPY.cpy:273-321`
- Note: After a CSUTLDTC failure, GO TO EDIT-DATE-LE-EXIT (app/cpy/CSUTLDPY.cpy:315) falls through to SET WS-EDIT-DATE-IS-VALID (app/cpy/CSUTLDPY.cpy:327), so the date flags read valid although INPUT-ERROR stays set.

## BR-BASE-COACTUPC-008

A date of birth that passes the date edits must be earlier than the current date. A date equal to today is rejected.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COACTUPC.cbl:1533-1543`, `app/cpy/CSUTLDPY.cpy:341-368`

## BR-BASE-COACTUPC-009

The SSN is entered in three parts of 3, 2 and 4 digits. Each part is required, must be numeric and must not be zero. The first part must also not be 000, 666 or 900 through 999.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COACTUPC.cbl:2431-2487`, `app/cbl/COACTUPC.cbl:121-123`, `app/cbl/COACTUPC.cbl:2109-2174`

## BR-BASE-COACTUPC-010

The FICO score is required, must be a 3-digit non-zero number, and must be 300 through 850.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COACTUPC.cbl:1545-1557`, `app/cbl/COACTUPC.cbl:2514-2529`, `app/cbl/COACTUPC.cbl:848-849`

## BR-BASE-COACTUPC-011

First Name and Last Name are required and may contain only letters and spaces, within 25 characters. Middle Name is optional, but when supplied it may contain only letters and spaces.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COACTUPC.cbl:1560-1582`, `app/cbl/COACTUPC.cbl:1898-1949`, `app/cbl/COACTUPC.cbl:2012-2055`

## BR-BASE-COACTUPC-012

Address Line 1 is required. City (address line 3) and Country are required and letters-and-spaces only. State is required, letters only, and must be one of 56 US state and territory codes. Address Line 2 is not edited.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COACTUPC.cbl:1584-1602`, `app/cbl/COACTUPC.cbl:1613-1630`, `app/cbl/COACTUPC.cbl:1824-1850`, `app/cbl/COACTUPC.cbl:2493-2509`, `app/cpy/CSLKPCDY.cpy:1013-1069`

## BR-BASE-COACTUPC-013

Zip is required, must be a 5-digit number and must not be zero. When State and Zip each pass, the state code plus the first two zip digits must be one of 240 listed combinations.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COACTUPC.cbl:1605-1611`, `app/cbl/COACTUPC.cbl:1665-1669`, `app/cbl/COACTUPC.cbl:2536-2556`, `app/cpy/CSLKPCDY.cpy:1073-1313`

## BR-BASE-COACTUPC-014

Phone Number 1 and 2 are optional. When a number is entered, the area code must be a 3-digit non-zero number in the list of 410 North American general purpose area codes, the prefix must be a 3-digit non-zero number, and the line number must be a 4-digit non-zero number.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COACTUPC.cbl:1632-1646`, `app/cbl/COACTUPC.cbl:2225-2423`, `app/cpy/CSLKPCDY.cpy:521-930`
- Note: The not-entered test at app/cbl/COACTUPC.cbl:2238-2239 checks WS-EDIT-US-PHONE-NUMA for spaces where the line-number part NUMC is expected. A number with blank area code and prefix is accepted as not entered even when a line number is keyed.

## BR-BASE-COACTUPC-015

EFT Account Id is required, must be a 10-digit number and must not be zero.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COACTUPC.cbl:1648-1655`, `app/cbl/COACTUPC.cbl:2109-2174`
