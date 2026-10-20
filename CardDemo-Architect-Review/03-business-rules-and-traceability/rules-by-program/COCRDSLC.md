# COCRDSLC

Draft from `docs/_work/rules/rules.json`.

## BR-BASE-003

Each field edit writes its message only when no message is set yet, so the screen shows the first failing edit.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COCRDSLC.cbl:135`

## BR-BASE-COCRDSLC-001

A card-list account filter of low-values, spaces or zero is reported as not provided. A supplied account number that is not numeric is rejected. An asterisk or spaces on the screen field is treated as not supplied.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COCRDSLC.cbl:608-620`, `app/cbl/COCRDSLC.cbl:647-679`, `app/cbl/COCRDSLC.cbl:138-139`

## BR-BASE-COCRDSLC-002

A card-list card filter of low-values, spaces or zero is reported as not provided. A supplied card number that is not numeric is rejected. An asterisk or spaces on the screen field is treated as not supplied.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COCRDSLC.cbl:622-634`, `app/cbl/COCRDSLC.cbl:685-719`, `app/cbl/COCRDSLC.cbl:140-141`

## BR-BASE-COCRDSLC-003

When both the account filter and the card filter are blank, the card list screen reports that no input was received.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COCRDSLC.cbl:636-640`, `app/cbl/COCRDSLC.cbl:142-143`
