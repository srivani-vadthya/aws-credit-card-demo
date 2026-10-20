# COADM01C

Draft from `docs/_work/rules/rules.json`.

## BR-BASE-001

When the return target is spaces or low-values, the user menu and the admin menu both set it to COSGN00C before the transfer.

- Category: routing
- Confidence: Confirmed
- Source: `app/cbl/COADM01C.cbl:165-167`

## BR-BASE-002

PF3 on the user menu and on the admin menu sets the return target to COSGN00C and returns to sign-on.

- Category: routing
- Confidence: Confirmed
- Source: `app/cbl/COADM01C.cbl:100-102`

## BR-BASE-COADM01C-001

An admin-menu option is started when its program name does not begin with DUMMY.

- Category: routing
- Confidence: Confirmed
- Source: `app/cbl/COADM01C.cbl:141-146`
