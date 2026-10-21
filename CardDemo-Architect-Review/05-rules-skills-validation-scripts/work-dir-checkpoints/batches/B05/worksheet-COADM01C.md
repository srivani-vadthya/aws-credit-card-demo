# Worksheet COADM01C (app/cbl/COADM01C.cbl)

Lines: 288. Paragraphs: 8. Decision points: 24 (business candidates: 16).

Fill `docs/_work/semantic/programs/COADM01C.json`. Read the whole source; this list only indexes it.

## Paragraphs

| Paragraph | Lines | Performs | Performed by |
|---|---|---|---|
| MAIN-PARA | 75-114 | PROCESS-ENTER-KEY, RECEIVE-MENU-SCREEN, RETURN-TO-SIGNON-SCREEN, SEND-MENU-SCREEN |  |
| PROCESS-ENTER-KEY | 119-158 | SEND-MENU-SCREEN | MAIN-PARA |
| RETURN-TO-SIGNON-SCREEN | 163-170 |  | MAIN-PARA |
| SEND-MENU-SCREEN | 175-187 | BUILD-MENU-OPTIONS, POPULATE-HEADER-INFO | MAIN-PARA, PGMIDERR-ERR-PARA, PROCESS-ENTER-KEY |
| RECEIVE-MENU-SCREEN | 192-200 |  | MAIN-PARA |
| POPULATE-HEADER-INFO | 205-224 |  | SEND-MENU-SCREEN |
| BUILD-MENU-OPTIONS | 229-266 |  | SEND-MENU-SCREEN |
| PGMIDERR-ERR-PARA | 270-284 | SEND-MENU-SCREEN |  |

## Decision points that look like business logic

Each line below must fall inside a rule `source` range or a `no_rule_decisions` range.

| Line | Paragraph | Type | Condition |
|---|---|---|---|
| 131 | PROCESS-ENTER-KEY | IF | `WS-OPTION IS NOT NUMERIC OR WS-OPTION > CDEMO-ADMIN-OPT-COUNT OR WS-OPTION = ZEROS` |
| 141 | PROCESS-ENTER-KEY | IF | `CDEMO-ADMIN-OPT-PGMNAME(WS-OPTION)(1:5) NOT = 'DUMMY'` |
| 165 | RETURN-TO-SIGNON-SCREEN | IF | `CDEMO-TO-PROGRAM = LOW-VALUES OR SPACES` |
| 231 | BUILD-MENU-OPTIONS | LOOP | `VARYING WS-IDX FROM 1 BY 1 UNTIL WS-IDX > CDEMO-ADMIN-OPT-COUNT` |
| 241 | BUILD-MENU-OPTIONS | EVALUATE | `WS-IDX` |
| 242 | BUILD-MENU-OPTIONS | WHEN | `1` |
| 244 | BUILD-MENU-OPTIONS | WHEN | `2` |
| 246 | BUILD-MENU-OPTIONS | WHEN | `3` |
| 248 | BUILD-MENU-OPTIONS | WHEN | `4` |
| 250 | BUILD-MENU-OPTIONS | WHEN | `5` |
| 252 | BUILD-MENU-OPTIONS | WHEN | `6` |
| 254 | BUILD-MENU-OPTIONS | WHEN | `7` |
| 256 | BUILD-MENU-OPTIONS | WHEN | `8` |
| 258 | BUILD-MENU-OPTIONS | WHEN | `9` |
| 260 | BUILD-MENU-OPTIONS | WHEN | `10` |
| 262 | BUILD-MENU-OPTIONS | WHEN | `OTHER` |

## Calculations


## Existing rules to review (record a verdict and anchor for each)

- BR-BASE-001: When the return target is spaces or low-values, the user menu and the admin menu both set it to COSGN00C before the transfer. (app/cbl/COMEN01C.cbl:198-200, app/cbl/COADM01C.cbl:165-167)
- BR-BASE-002: PF3 on the user menu and on the admin menu sets the return target to COSGN00C and returns to sign-on. (app/cbl/COMEN01C.cbl:96-98, app/cbl/COADM01C.cbl:100-102)
- BR-BASE-COADM01C-001: An admin-menu option is started when its program name does not begin with DUMMY. (app/cbl/COADM01C.cbl:141-146)
