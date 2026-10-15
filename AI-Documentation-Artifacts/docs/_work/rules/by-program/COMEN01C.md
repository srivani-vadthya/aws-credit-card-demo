# COMEN01C

Draft from `docs/_work/rules/rules.json`.

## BR-BASE-001

When the return target is spaces or low-values, the user menu and the admin menu both set it to COSGN00C before the transfer.

- Category: routing
- Confidence: Confirmed
- Source: `app/cbl/COMEN01C.cbl:198-200`

## BR-BASE-002

PF3 on the user menu and on the admin menu sets the return target to COSGN00C and returns to sign-on.

- Category: routing
- Confidence: Confirmed
- Source: `app/cbl/COMEN01C.cbl:96-98`

## BR-BASE-COMEN01C-001

Menu option COPAUS0C is started only when INQUIRE PROGRAM returns a normal response. Otherwise the menu shows that the option is not installed.

- Category: routing
- Confidence: Confirmed
- Source: `app/cbl/COMEN01C.cbl:147-168`

## BR-BASE-COMEN01C-002

A user-menu option whose program name begins with DUMMY is not started. The menu shows that the option is coming soon.

- Category: routing
- Confidence: Confirmed
- Source: `app/cbl/COMEN01C.cbl:169-176`
