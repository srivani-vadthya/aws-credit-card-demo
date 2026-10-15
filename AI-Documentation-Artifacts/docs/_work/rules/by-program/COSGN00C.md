# COSGN00C

Draft from `docs/_work/rules/rules.json`.

## BR-BASE-COSGN00C-001

Sign-on stops before the password is checked when the entered user id is spaces or low-values, and the screen is redisplayed with 'Please enter User ID ...'.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COSGN00C.cbl:118-122`

## BR-BASE-COSGN00C-002

Sign-on stops when a user id is present and the password is spaces or low-values, and the screen is redisplayed with 'Please enter Password ...'.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COSGN00C.cbl:123-127`

## BR-BASE-COSGN00C-003

The entered user id and password are converted to upper case before the user-security file is read and the password is compared.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COSGN00C.cbl:132-136`

## BR-BASE-COSGN00C-004

Sign-on is refused when the stored password does not equal the upper-cased entered password, and the screen is redisplayed with 'Wrong Password. Try again ...'.

- Category: authorization
- Confidence: Confirmed
- Source: `app/cbl/COSGN00C.cbl:241-246`

## BR-BASE-COSGN00C-005

A matching password transfers an admin user to COADM01C and any other user to COMEN01C. Admin means CDEMO-USER-TYPE equals 'A'.

- Category: routing
- Confidence: Confirmed
- Source: `app/cbl/COSGN00C.cbl:223-239`

## BR-BASE-COSGN00C-006

A user-security read response of 13 redisplays sign-on with 'User not found. Try again ...'. Any other non-zero response redisplays sign-on with 'Unable to verify the User ...'.

- Category: validation
- Confidence: Confirmed
- Source: `app/cbl/COSGN00C.cbl:221-256`
