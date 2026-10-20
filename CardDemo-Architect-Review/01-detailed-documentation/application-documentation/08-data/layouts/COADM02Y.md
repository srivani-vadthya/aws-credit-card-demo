# Layout COADM02Y

| Item | Value |
|---|---|
| Source | `app/cpy/COADM02Y.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 62 |
| Data items | 26 (88-levels: 0) |
| Semantic analysis | validated (batch B05) |

## Purpose

COADM02Y defines CARDDEMO-ADMIN-MENU-OPTIONS, the static option table of the administrator menu. It holds an option count (6, raised from 4 for the Db2 release) and a literal table of 45-byte entries (option number, 35-character display name, 8-character target program), redefined as the array CDEMO-ADMIN-OPT OCCURS 9. COADM01C uses it to build the menu lines, validate the entered option number and resolve the XCTL target program. (Confirmed)

Evidence: `app/cpy/COADM02Y.cpy:19-59`, `app/cbl/COADM01C.cbl:51`, `app/cbl/COADM01C.cbl:131-149`, `app/cbl/COADM01C.cbl:231-239`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | CARDDEMO-ADMIN-MENU-OPTIONS |  |  | 1 | 407 | 407 |  |  |  | 19 |
| 05 | &nbsp;&nbsp;CDEMO-ADMIN-OPT-COUNT | 9(02) | DISPLAY | 1 | 2 | 2 |  |  | 6 | 22 |
| 05 | &nbsp;&nbsp;CDEMO-ADMIN-OPTIONS-DATA |  |  | 3 | 272 | 270 |  |  |  | 24 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 9(02) | DISPLAY | 3 | 4 | 2 |  |  | 1 | 26 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(35) | DISPLAY | 5 | 39 | 35 |  |  | 'User List (Security) ' | 27 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(08) | DISPLAY | 40 | 47 | 8 |  |  | 'COUSR00C' | 29 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 9(02) | DISPLAY | 48 | 49 | 2 |  |  | 2 | 31 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(35) | DISPLAY | 50 | 84 | 35 |  |  | 'User Add (Security) ' | 32 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(08) | DISPLAY | 85 | 92 | 8 |  |  | 'COUSR01C' | 34 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 9(02) | DISPLAY | 93 | 94 | 2 |  |  | 3 | 36 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(35) | DISPLAY | 95 | 129 | 35 |  |  | 'User Update (Security) ' | 37 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(08) | DISPLAY | 130 | 137 | 8 |  |  | 'COUSR02C' | 39 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 9(02) | DISPLAY | 138 | 139 | 2 |  |  | 4 | 41 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(35) | DISPLAY | 140 | 174 | 35 |  |  | 'User Delete (Security) ' | 42 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(08) | DISPLAY | 175 | 182 | 8 |  |  | 'COUSR03C' | 44 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 9(02) | DISPLAY | 183 | 184 | 2 |  |  | 5 | 46 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(35) | DISPLAY | 185 | 219 | 35 |  |  | 'Transaction Type List/Update (Db2) ' | 47 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(08) | DISPLAY | 220 | 227 | 8 |  |  | 'COTRTLIC' | 49 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | 9(02) | DISPLAY | 228 | 229 | 2 |  |  | 6 | 50 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(35) | DISPLAY | 230 | 264 | 35 |  |  | 'Transaction Type Maintenance (Db2) ' | 51 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(08) | DISPLAY | 265 | 272 | 8 |  |  | 'COTRTUPC' | 53 |
| 05 | &nbsp;&nbsp;CDEMO-ADMIN-OPTIONS |  |  | 3 | 407 | 405 |  | CDEMO-ADMIN-OPTIONS-DATA |  | 55 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-ADMIN-OPT |  |  | 3 | 407 | 405 | 9 |  |  | 56 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CDEMO-ADMIN-OPT-NUM | 9(02) | DISPLAY | 3 | 4 | 2 |  |  |  | 57 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CDEMO-ADMIN-OPT-NAME | X(35) | DISPLAY | 5 | 39 | 35 |  |  |  | 58 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CDEMO-ADMIN-OPT-PGMNAME | X(08) | DISPLAY | 40 | 47 | 8 |  |  |  | 59 |

## Level-88 conditions

None.

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [COADM01C](../../07-programs/COADM01C.md) | cobol-program | COPY | active |  | `app/cbl/COADM01C.cbl:51` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| CDEMO-ADMIN-OPT-COUNT | 22 | COADM01C (2): `app/cbl/COADM01C.cbl:132`, `app/cbl/COADM01C.cbl:232` |
| CDEMO-ADMIN-OPT-NUM | 57 | COADM01C (1): `app/cbl/COADM01C.cbl:236` |
| CDEMO-ADMIN-OPT-NAME | 58 | COADM01C (1): `app/cbl/COADM01C.cbl:238` |
| CDEMO-ADMIN-OPT-PGMNAME | 59 | COADM01C (2): `app/cbl/COADM01C.cbl:141`, `app/cbl/COADM01C.cbl:146` |

Named in no procedure statement of the copying programs (may still be moved as part of a group): CARDDEMO-ADMIN-MENU-OPTIONS (line 19), CDEMO-ADMIN-OPTIONS-DATA (line 24), CDEMO-ADMIN-OPTIONS (line 55), CDEMO-ADMIN-OPT (line 56).

## Key fields

| Field | Meaning | Source |
|---|---|---|
| CDEMO-ADMIN-OPT-COUNT | Number of active admin options (VALUE 6); upper bound for option validation and menu building in COADM01C. The previous value 4 is commented out. | `app/cpy/COADM02Y.cpy:21-22` |
| CDEMO-ADMIN-OPTIONS-DATA | Literal table: 1 User List (Security) COUSR00C, 2 User Add (Security) COUSR01C, 3 User Update (Security) COUSR02C, 4 User Delete (Security) COUSR03C, 5 Transaction Type List/Update (Db2) COTRTLIC, 6 Transaction Type Maintenance (Db2) COTRTUPC. | `app/cpy/COADM02Y.cpy:24-53` |
| CDEMO-ADMIN-OPT | Array view (OCCURS 9) over the literal table, subscripted by the option number. | `app/cpy/COADM02Y.cpy:55-56` |
| CDEMO-ADMIN-OPT-NUM | Option number shown on the admin menu line. | `app/cpy/COADM02Y.cpy:57` |
| CDEMO-ADMIN-OPT-NAME | Option description shown on the admin menu. | `app/cpy/COADM02Y.cpy:58` |
| CDEMO-ADMIN-OPT-PGMNAME | CICS program XCTLed to for the option; a 'DUMMY' prefix suppresses the transfer. | `app/cpy/COADM02Y.cpy:59` |

## Observations

- anomaly: The redefining array CDEMO-ADMIN-OPT OCCURS 9 (405 bytes) is larger than the 6-entry literal table it redefines (270 bytes); entries 7-9 have no defined content. (`app/cpy/COADM02Y.cpy:55-56`)
- hardcoded-value: Options 5 and 6 point at Db2-based programs COTRTLIC and COTRTUPC added for the Db2 release; their availability depends on that optional module being installed (COADM01C handles PGMIDERR). (`app/cpy/COADM02Y.cpy:45-54`)
- anomaly: Unlike COMEN02Y there is no user-type column; access control for admin options relies entirely on the sign-on routing. (`app/cpy/COADM02Y.cpy:56-59`)

## Sources

- `app/cpy/COADM02Y.cpy`
- `docs/_work/structure/copybooks/COADM02Y.json`
- `docs/_work/layouts/COADM02Y.json`
- `docs/_work/semantic/copybooks/COADM02Y.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
