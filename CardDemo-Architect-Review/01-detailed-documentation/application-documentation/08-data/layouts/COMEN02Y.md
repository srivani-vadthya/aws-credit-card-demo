# Layout COMEN02Y

| Item | Value |
|---|---|
| Source | `app/cpy/COMEN02Y.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 101 |
| Data items | 53 (88-levels: 0) |
| Semantic analysis | validated (batch B05) |

## Purpose

COMEN02Y defines CARDDEMO-MAIN-MENU-OPTIONS, the static option table of the regular-user main menu. It holds an option count (11) and a literal table of 46-byte entries (option number, 35-character display name, 8-character target program, 1-character allowed user type), redefined as the array CDEMO-MENU-OPT OCCURS 12. COMEN01C uses it to build the menu lines, to validate the entered option number against the count, to block admin-only entries for regular users and to resolve the XCTL target program. (Confirmed)

Evidence: `app/cpy/COMEN02Y.cpy:19-98`, `app/cbl/COMEN01C.cbl:51`, `app/cbl/COMEN01C.cbl:127-187`, `app/cbl/COMEN01C.cbl:264-272`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | CARDDEMO-MAIN-MENU-OPTIONS |  |  | 1 | 554 | 554 |  |  |  | 19 |
| 05 | &nbsp;&nbsp;CDEMO-MENU-OPT-COUNT | 9(02) | DISPLAY | 1 | 2 | 2 |  |  | 11 | 21 |
| 05 | &nbsp;&nbsp;CDEMO-MENU-OPTIONS-DATA |  |  | 3 | 508 | 506 |  |  |  | 23 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 9(02) | DISPLAY | 3 | 4 | 2 |  |  | 1 | 25 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(35) | DISPLAY | 5 | 39 | 35 |  |  | 'Account View ' | 26 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(08) | DISPLAY | 40 | 47 | 8 |  |  | 'COACTVWC' | 28 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(01) | DISPLAY | 48 | 48 | 1 |  |  | 'U' | 29 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 9(02) | DISPLAY | 49 | 50 | 2 |  |  | 2 | 31 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(35) | DISPLAY | 51 | 85 | 35 |  |  | 'Account Update ' | 32 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(08) | DISPLAY | 86 | 93 | 8 |  |  | 'COACTUPC' | 34 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(01) | DISPLAY | 94 | 94 | 1 |  |  | 'U' | 35 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 9(02) | DISPLAY | 95 | 96 | 2 |  |  | 3 | 37 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(35) | DISPLAY | 97 | 131 | 35 |  |  | 'Credit Card List ' | 38 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(08) | DISPLAY | 132 | 139 | 8 |  |  | 'COCRDLIC' | 40 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(01) | DISPLAY | 140 | 140 | 1 |  |  | 'U' | 41 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 9(02) | DISPLAY | 141 | 142 | 2 |  |  | 4 | 43 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(35) | DISPLAY | 143 | 177 | 35 |  |  | 'Credit Card View ' | 44 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(08) | DISPLAY | 178 | 185 | 8 |  |  | 'COCRDSLC' | 46 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(01) | DISPLAY | 186 | 186 | 1 |  |  | 'U' | 47 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 9(02) | DISPLAY | 187 | 188 | 2 |  |  | 5 | 49 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(35) | DISPLAY | 189 | 223 | 35 |  |  | 'Credit Card Update ' | 50 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(08) | DISPLAY | 224 | 231 | 8 |  |  | 'COCRDUPC' | 52 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(01) | DISPLAY | 232 | 232 | 1 |  |  | 'U' | 53 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 9(02) | DISPLAY | 233 | 234 | 2 |  |  | 6 | 55 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(35) | DISPLAY | 235 | 269 | 35 |  |  | 'Transaction List ' | 56 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(08) | DISPLAY | 270 | 277 | 8 |  |  | 'COTRN00C' | 58 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(01) | DISPLAY | 278 | 278 | 1 |  |  | 'U' | 59 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 9(02) | DISPLAY | 279 | 280 | 2 |  |  | 7 | 61 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(35) | DISPLAY | 281 | 315 | 35 |  |  | 'Transaction View ' | 62 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(08) | DISPLAY | 316 | 323 | 8 |  |  | 'COTRN01C' | 64 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(01) | DISPLAY | 324 | 324 | 1 |  |  | 'U' | 65 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 9(02) | DISPLAY | 325 | 326 | 2 |  |  | 8 | 67 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(35) | DISPLAY | 327 | 361 | 35 |  |  | 'Transaction Add ' | 68 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(08) | DISPLAY | 362 | 369 | 8 |  |  | 'COTRN02C' | 71 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(01) | DISPLAY | 370 | 370 | 1 |  |  | 'U' | 72 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 9(02) | DISPLAY | 371 | 372 | 2 |  |  | 9 | 74 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(35) | DISPLAY | 373 | 407 | 35 |  |  | 'Transaction Reports ' | 75 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(08) | DISPLAY | 408 | 415 | 8 |  |  | 'CORPT00C' | 77 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(01) | DISPLAY | 416 | 416 | 1 |  |  | 'U' | 78 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 9(02) | DISPLAY | 417 | 418 | 2 |  |  | 10 | 80 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(35) | DISPLAY | 419 | 453 | 35 |  |  | 'Bill Payment ' | 81 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(08) | DISPLAY | 454 | 461 | 8 |  |  | 'COBIL00C' | 83 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(01) | DISPLAY | 462 | 462 | 1 |  |  | 'U' | 84 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 9(02) | DISPLAY | 463 | 464 | 2 |  |  | 11 | 86 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(35) | DISPLAY | 465 | 499 | 35 |  |  | 'Pending Authorization View ' | 87 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(08) | DISPLAY | 500 | 507 | 8 |  |  | 'COPAUS0C' | 89 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(01) | DISPLAY | 508 | 508 | 1 |  |  | 'U' | 90 |
| 05 | &nbsp;&nbsp;CDEMO-MENU-OPTIONS |  |  | 3 | 554 | 552 |  | CDEMO-MENU-OPTIONS-DATA |  | 93 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-MENU-OPT |  |  | 3 | 554 | 552 | 12 |  |  | 94 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CDEMO-MENU-OPT-NUM | 9(02) | DISPLAY | 3 | 4 | 2 |  |  |  | 95 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CDEMO-MENU-OPT-NAME | X(35) | DISPLAY | 5 | 39 | 35 |  |  |  | 96 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CDEMO-MENU-OPT-PGMNAME | X(08) | DISPLAY | 40 | 47 | 8 |  |  |  | 97 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CDEMO-MENU-OPT-USRTYPE | X(01) | DISPLAY | 48 | 48 | 1 |  |  |  | 98 |

## Level-88 conditions

None.

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [COMEN01C](../../07-programs/COMEN01C.md) | cobol-program | COPY | active |  | `app/cbl/COMEN01C.cbl:51` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| CDEMO-MENU-OPT-COUNT | 21 | COMEN01C (2): `app/cbl/COMEN01C.cbl:128`, `app/cbl/COMEN01C.cbl:265` |
| CDEMO-MENU-OPT-NUM | 95 | COMEN01C (1): `app/cbl/COMEN01C.cbl:269` |
| CDEMO-MENU-OPT-NAME | 96 | COMEN01C (3): `app/cbl/COMEN01C.cbl:164`, `app/cbl/COMEN01C.cbl:173`, `app/cbl/COMEN01C.cbl:271` |
| CDEMO-MENU-OPT-PGMNAME | 97 | COMEN01C (5): `app/cbl/COMEN01C.cbl:147`, `app/cbl/COMEN01C.cbl:149`, `app/cbl/COMEN01C.cbl:157`, ... |
| CDEMO-MENU-OPT-USRTYPE | 98 | COMEN01C (1): `app/cbl/COMEN01C.cbl:137` |

Named in no procedure statement of the copying programs (may still be moved as part of a group): CARDDEMO-MAIN-MENU-OPTIONS (line 19), CDEMO-MENU-OPTIONS-DATA (line 23), CDEMO-MENU-OPTIONS (line 93), CDEMO-MENU-OPT (line 94).

## Key fields

| Field | Meaning | Source |
|---|---|---|
| CDEMO-MENU-OPT-COUNT | Number of active main-menu options (VALUE 11); upper bound for option validation and menu-building loop in COMEN01C. | `app/cpy/COMEN02Y.cpy:21` |
| CDEMO-MENU-OPTIONS-DATA | Literal table: 1 Account View COACTVWC, 2 Account Update COACTUPC, 3 Credit Card List COCRDLIC, 4 Credit Card View COCRDSLC, 5 Credit Card Update COCRDUPC, 6 Transaction List COTRN00C, 7 Transaction View COTRN01C, 8 Transaction Add COTRN02C, 9 Transaction Reports CORPT00C, 10 Bill Payment COBIL00C, 11 Pending Authorization View COPAUS0C; all with user type 'U'. | `app/cpy/COMEN02Y.cpy:23-90` |
| CDEMO-MENU-OPT | Array view (OCCURS 12) over the literal table, subscripted by the option number. | `app/cpy/COMEN02Y.cpy:93-94` |
| CDEMO-MENU-OPT-NUM | Option number shown on the menu line. | `app/cpy/COMEN02Y.cpy:95` |
| CDEMO-MENU-OPT-NAME | Option description shown on the menu and used in 'not installed'/'coming soon' messages. | `app/cpy/COMEN02Y.cpy:96` |
| CDEMO-MENU-OPT-PGMNAME | CICS program XCTLed to when the option is chosen; 'DUMMY' prefix means placeholder, COPAUS0C is checked with INQUIRE PROGRAM first. | `app/cpy/COMEN02Y.cpy:97` |
| CDEMO-MENU-OPT-USRTYPE | User type allowed for the option; 'A' marks admin-only (blocked for CDEMO-USRTYP-USER in COMEN01C), 'U' available to regular users. | `app/cpy/COMEN02Y.cpy:98` |

## Observations

- anomaly: The redefining array CDEMO-MENU-OPT OCCURS 12 (552 bytes) is larger than the 11-entry literal table it redefines (506 bytes); entry 12 has no defined content and a REDEFINES larger than the redefined item below level 01 is non-standard. (`app/cpy/COMEN02Y.cpy:93-94`)
- conflict: Header comment says 'CardDemo - Admin Menu Options' although the copybook defines the main (user) menu. (`app/cpy/COMEN02Y.cpy:2`)
- dead-code: Option 8 originally read 'Transaction Add (Admin Only)' (commented out) and is now flagged 'U'; no option uses user type 'A', so the admin-only check in COMEN01C never fires. (`app/cpy/COMEN02Y.cpy:67-72`)

## Sources

- `app/cpy/COMEN02Y.cpy`
- `docs/_work/structure/copybooks/COMEN02Y.json`
- `docs/_work/layouts/COMEN02Y.json`
- `docs/_work/semantic/copybooks/COMEN02Y.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
