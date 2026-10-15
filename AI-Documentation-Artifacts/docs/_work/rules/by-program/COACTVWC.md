# COACTVWC

Draft from `docs/_work/rules/rules.json`.

## BR-BASE-003

Each field edit writes its message only when no message is set yet, so the screen shows the first failing edit.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COACTVWC.cbl:118`

## BR-BASE-COACTVWC-001

An account-view filter of low-values or spaces is reported as not provided, and the message becomes No input received. A supplied account number that is not numeric or is zeros is rejected. An asterisk or spaces on the screen field is treated as not supplied.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COACTVWC.cbl:627-642`, `app/cbl/COACTVWC.cbl:649-680`, `app/cbl/COACTVWC.cbl:121-124`
- Note: A zero account number is rejected by the numeric-or-zero test at app/cbl/COACTVWC.cbl:666-667. It is not in the not-provided test at app/cbl/COACTVWC.cbl:653-654. COCRDSLC puts zero in the not-provided test (app/cbl/COCRDSLC.cbl:651-653).
