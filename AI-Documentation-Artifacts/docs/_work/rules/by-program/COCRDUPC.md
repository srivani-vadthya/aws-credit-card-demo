# COCRDUPC

Draft from `docs/_work/rules/rules.json`.

## BR-BASE-003

The card update and account update programs run every field edit, but each edit writes its message only when no message is set yet. The screen therefore shows the first failing edit in edit order.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COCRDUPC.cbl:173-174`, `app/cbl/COCRDUPC.cbl:730-732`

## BR-BASE-004

When no field edit sets INPUT-ERROR, the card update and account update programs mark the changes as validated but not yet confirmed.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COCRDUPC.cbl:710-714`

## BR-BASE-COCRDUPC-001

Before card details are fetched, an account number that is low-values, spaces or zero is reported as not provided. A supplied account number that is not numeric is rejected.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COCRDUPC.cbl:721-756`, `app/cbl/COCRDUPC.cbl:176-177`
- Note: A zero account number gets the not-provided message here, while COACTUPC rejects zero with the non-zero message (app/cbl/COACTUPC.cbl:1802-1808).

## BR-BASE-COCRDUPC-002

Before card details are fetched, a card number that is low-values, spaces or zero is reported as not provided. A supplied card number that is not numeric is rejected.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COCRDUPC.cbl:762-800`, `app/cbl/COCRDUPC.cbl:178-180`

## BR-BASE-COCRDUPC-003

Before card details are fetched, only the account and card search keys are edited. When both are blank the message is No input received.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COCRDUPC.cbl:644-662`, `app/cbl/COCRDUPC.cbl:184-185`

## BR-BASE-COCRDUPC-004

When the new card data equals the fetched card data after both are converted to upper case, no change is reported and the card detail edits are skipped.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COCRDUPC.cbl:680-693`, `app/cbl/COCRDUPC.cbl:186-187`

## BR-BASE-COCRDUPC-005

The embossed card name is required and may contain only letters A-Z, a-z and spaces. A name of low-values, spaces or zeros counts as not provided.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COCRDUPC.cbl:806-840`, `app/cbl/COCRDUPC.cbl:255-260`, `app/cbl/COCRDUPC.cbl:181-184`

## BR-BASE-COCRDUPC-006

The card active status must be Y or N. A blank status gets the same message.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COCRDUPC.cbl:845-873`, `app/cbl/COCRDUPC.cbl:89-91`, `app/cbl/COCRDUPC.cbl:194-195`

## BR-BASE-COCRDUPC-007

The card expiry month is required and must be 1 through 12.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COCRDUPC.cbl:877-908`, `app/cbl/COCRDUPC.cbl:92-95`, `app/cbl/COCRDUPC.cbl:196-197`
- Note: The comment at app/cbl/COCRDUPC.cbl:894 says must be numeric, but the code tests only the 88-level VALID-MONTH on a PIC 9(2) redefinition of the PIC X(2) input. No IS NUMERIC test is present.

## BR-BASE-COCRDUPC-008

The card expiry year is required and must be 1950 through 2099.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COCRDUPC.cbl:913-944`, `app/cbl/COCRDUPC.cbl:96-99`, `app/cbl/COCRDUPC.cbl:198-200`
- Note: The comment at app/cbl/COCRDUPC.cbl:928-929 says must be numeric and must be 1 to 12. The code uses VALID-YEAR 1950 thru 2099 (app/cbl/COCRDUPC.cbl:99). Code wins.
