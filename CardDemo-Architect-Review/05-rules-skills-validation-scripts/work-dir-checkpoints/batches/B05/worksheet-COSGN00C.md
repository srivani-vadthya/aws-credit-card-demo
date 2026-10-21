# Worksheet COSGN00C (app/cbl/COSGN00C.cbl)

Lines: 260. Paragraphs: 6. Decision points: 16 (business candidates: 6).

Fill `docs/_work/semantic/programs/COSGN00C.json`. Read the whole source; this list only indexes it.

## Paragraphs

| Paragraph | Lines | Performs | Performed by |
|---|---|---|---|
| MAIN-PARA | 73-102 | PROCESS-ENTER-KEY, SEND-PLAIN-TEXT, SEND-SIGNON-SCREEN |  |
| PROCESS-ENTER-KEY | 108-140 | READ-USER-SEC-FILE, SEND-SIGNON-SCREEN | MAIN-PARA |
| SEND-SIGNON-SCREEN | 145-157 | POPULATE-HEADER-INFO | MAIN-PARA, PROCESS-ENTER-KEY, READ-USER-SEC-FILE |
| SEND-PLAIN-TEXT | 162-172 |  | MAIN-PARA |
| POPULATE-HEADER-INFO | 177-204 |  | SEND-SIGNON-SCREEN |
| READ-USER-SEC-FILE | 209-257 | SEND-SIGNON-SCREEN | PROCESS-ENTER-KEY |

## Decision points that look like business logic

Each line below must fall inside a rule `source` range or a `no_rule_decisions` range.

| Line | Paragraph | Type | Condition |
|---|---|---|---|
| 117 | PROCESS-ENTER-KEY | EVALUATE | `TRUE` |
| 118 | PROCESS-ENTER-KEY | WHEN | `USERIDI OF COSGN0AI = SPACES OR LOW-VALUES` |
| 123 | PROCESS-ENTER-KEY | WHEN | `PASSWDI OF COSGN0AI = SPACES OR LOW-VALUES` |
| 128 | PROCESS-ENTER-KEY | WHEN | `OTHER` |
| 223 | READ-USER-SEC-FILE | IF | `SEC-USR-PWD = WS-USER-PWD` |
| 230 | READ-USER-SEC-FILE | IF | `CDEMO-USRTYP-ADMIN` |

## Calculations


## Existing rules to review (record a verdict and anchor for each)

- BR-BASE-COSGN00C-001: Sign-on stops before the password is checked when the entered user id is spaces or low-values, and the screen is redisplayed with 'Please enter User ID ...'. (app/cbl/COSGN00C.cbl:118-122)
- BR-BASE-COSGN00C-002: Sign-on stops when a user id is present and the password is spaces or low-values, and the screen is redisplayed with 'Please enter Password ...'. (app/cbl/COSGN00C.cbl:123-127)
- BR-BASE-COSGN00C-003: The entered user id and password are converted to upper case before the user-security file is read and the password is compared. (app/cbl/COSGN00C.cbl:132-136)
- BR-BASE-COSGN00C-004: Sign-on is refused when the stored password does not equal the upper-cased entered password, and the screen is redisplayed with 'Wrong Password. Try again ...'. (app/cbl/COSGN00C.cbl:241-246)
- BR-BASE-COSGN00C-005: A matching password transfers an admin user to COADM01C and any other user to COMEN01C. Admin means CDEMO-USER-TYPE equals 'A'. (app/cbl/COSGN00C.cbl:223-239)
- BR-BASE-COSGN00C-006: A user-security read response of 13 redisplays sign-on with 'User not found. Try again ...'. Any other non-zero response redisplays sign-on with 'Unable to verify the User ...'. (app/cbl/COSGN00C.cbl:221-256)
