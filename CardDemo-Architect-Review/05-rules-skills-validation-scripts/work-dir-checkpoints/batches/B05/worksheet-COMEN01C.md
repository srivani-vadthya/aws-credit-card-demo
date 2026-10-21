# Worksheet COMEN01C (app/cbl/COMEN01C.cbl)

Lines: 308. Paragraphs: 7. Decision points: 31 (business candidates: 22).

Fill `docs/_work/semantic/programs/COMEN01C.json`. Read the whole source; this list only indexes it.

## Paragraphs

| Paragraph | Lines | Performs | Performed by |
|---|---|---|---|
| MAIN-PARA | 75-110 | PROCESS-ENTER-KEY, RECEIVE-MENU-SCREEN, RETURN-TO-SIGNON-SCREEN, SEND-MENU-SCREEN |  |
| PROCESS-ENTER-KEY | 115-191 | SEND-MENU-SCREEN | MAIN-PARA |
| RETURN-TO-SIGNON-SCREEN | 196-203 |  | MAIN-PARA |
| SEND-MENU-SCREEN | 208-220 | BUILD-MENU-OPTIONS, POPULATE-HEADER-INFO | MAIN-PARA, PROCESS-ENTER-KEY |
| RECEIVE-MENU-SCREEN | 225-233 |  | MAIN-PARA |
| POPULATE-HEADER-INFO | 238-257 |  | SEND-MENU-SCREEN |
| BUILD-MENU-OPTIONS | 262-303 |  | SEND-MENU-SCREEN |

## Decision points that look like business logic

Each line below must fall inside a rule `source` range or a `no_rule_decisions` range.

| Line | Paragraph | Type | Condition |
|---|---|---|---|
| 127 | PROCESS-ENTER-KEY | IF | `WS-OPTION IS NOT NUMERIC OR WS-OPTION > CDEMO-MENU-OPT-COUNT OR WS-OPTION = ZEROS` |
| 136 | PROCESS-ENTER-KEY | IF | `CDEMO-USRTYP-USER AND CDEMO-MENU-OPT-USRTYPE(WS-OPTION) = 'A'` |
| 146 | PROCESS-ENTER-KEY | EVALUATE | `TRUE` |
| 147 | PROCESS-ENTER-KEY | WHEN | `CDEMO-MENU-OPT-PGMNAME(WS-OPTION) = 'COPAUS0C'` |
| 169 | PROCESS-ENTER-KEY | WHEN | `CDEMO-MENU-OPT-PGMNAME(WS-OPTION)(1:5) = 'DUMMY'` |
| 177 | PROCESS-ENTER-KEY | WHEN | `OTHER` |
| 198 | RETURN-TO-SIGNON-SCREEN | IF | `CDEMO-TO-PROGRAM = LOW-VALUES OR SPACES` |
| 264 | BUILD-MENU-OPTIONS | LOOP | `VARYING WS-IDX FROM 1 BY 1 UNTIL WS-IDX > CDEMO-MENU-OPT-COUNT` |
| 274 | BUILD-MENU-OPTIONS | EVALUATE | `WS-IDX` |
| 275 | BUILD-MENU-OPTIONS | WHEN | `1` |
| 277 | BUILD-MENU-OPTIONS | WHEN | `2` |
| 279 | BUILD-MENU-OPTIONS | WHEN | `3` |
| 281 | BUILD-MENU-OPTIONS | WHEN | `4` |
| 283 | BUILD-MENU-OPTIONS | WHEN | `5` |
| 285 | BUILD-MENU-OPTIONS | WHEN | `6` |
| 287 | BUILD-MENU-OPTIONS | WHEN | `7` |
| 289 | BUILD-MENU-OPTIONS | WHEN | `8` |
| 291 | BUILD-MENU-OPTIONS | WHEN | `9` |
| 293 | BUILD-MENU-OPTIONS | WHEN | `10` |
| 295 | BUILD-MENU-OPTIONS | WHEN | `11` |
| 297 | BUILD-MENU-OPTIONS | WHEN | `12` |
| 299 | BUILD-MENU-OPTIONS | WHEN | `OTHER` |

## Calculations


## Existing rules to review (record a verdict and anchor for each)

- BR-BASE-001: When the return target is spaces or low-values, the user menu and the admin menu both set it to COSGN00C before the transfer. (app/cbl/COMEN01C.cbl:198-200, app/cbl/COADM01C.cbl:165-167)
- BR-BASE-002: PF3 on the user menu and on the admin menu sets the return target to COSGN00C and returns to sign-on. (app/cbl/COMEN01C.cbl:96-98, app/cbl/COADM01C.cbl:100-102)
- BR-BASE-COMEN01C-001: Menu option COPAUS0C is started only when INQUIRE PROGRAM returns a normal response. Otherwise the menu shows that the option is not installed. (app/cbl/COMEN01C.cbl:147-168)
- BR-BASE-COMEN01C-002: A user-menu option whose program name begins with DUMMY is not started. The menu shows that the option is coming soon. (app/cbl/COMEN01C.cbl:169-176)
