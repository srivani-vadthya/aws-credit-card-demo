# COTRTUPC

Draft from `docs/_work/rules/rules.json`.

## BR-BASE-003

Each field edit writes its message only when no message is set yet, so the screen shows the first failing edit.

- Category: validation
- Confidence: Confirmed
- Source: `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:863-868`

## BR-BASE-004

When no field edit sets INPUT-ERROR, the card update, account update and transaction-type update programs mark the changes as validated but not yet confirmed.

- Category: validation
- Confidence: Confirmed
- Source: `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:772-775`

## BR-BASE-COTRTUPC-001

The transaction type code is required, must be numeric, and must not be zero, within 2 characters. A code that passes is rewritten with leading zeros.

- Category: validation
- Confidence: Confirmed
- Source: `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:820-842`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:907-974`

## BR-BASE-COTRTUPC-002

The transaction description is required and may contain only letters, digits and spaces, within 50 characters.

- Category: validation
- Confidence: Confirmed
- Source: `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:755-764`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:849-903`

## BR-BASE-COTRTUPC-003

No change is reported when the type code matches after upper case, and the description matches after trim and upper case and has the same trimmed length. Field edits are then skipped.

- Category: validation
- Confidence: Confirmed
- Source: `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:783-811`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:743-750`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:179-180`
