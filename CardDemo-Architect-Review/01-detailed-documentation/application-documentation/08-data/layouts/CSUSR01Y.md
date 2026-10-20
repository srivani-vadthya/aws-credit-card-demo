# Layout CSUSR01Y

| Item | Value |
|---|---|
| Source | `app/cpy/CSUSR01Y.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 26 |
| Data items | 7 (88-levels: 0) |
| Semantic analysis | validated (batch B04) |

## Purpose

Defines SEC-USER-DATA, the 80-byte signed-on user security record: user id, first and last name, password, user type and filler. It is the record used by the sign-on and user-maintenance programs; COACTUPC copies it but does not reference any of its fields. (Confirmed)

Evidence: `app/cpy/CSUSR01Y.cpy:17-23`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | SEC-USER-DATA |  |  | 1 | 80 | 80 |  |  |  | 17 |
| 05 | &nbsp;&nbsp;SEC-USR-ID | X(08) | DISPLAY | 1 | 8 | 8 |  |  |  | 18 |
| 05 | &nbsp;&nbsp;SEC-USR-FNAME | X(20) | DISPLAY | 9 | 28 | 20 |  |  |  | 19 |
| 05 | &nbsp;&nbsp;SEC-USR-LNAME | X(20) | DISPLAY | 29 | 48 | 20 |  |  |  | 20 |
| 05 | &nbsp;&nbsp;SEC-USR-PWD | X(08) | DISPLAY | 49 | 56 | 8 |  |  |  | 21 |
| 05 | &nbsp;&nbsp;SEC-USR-TYPE | X(01) | DISPLAY | 57 | 57 | 1 |  |  |  | 22 |
| 05 | &nbsp;&nbsp;SEC-USR-FILLER | X(23) | DISPLAY | 58 | 80 | 23 |  |  |  | 23 |

## Level-88 conditions

None.

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [COTRTLIC](../../07-programs/COTRTLIC.md) | cobol-program | COPY | active |  | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:485` |
| [COTRTUPC](../../07-programs/COTRTUPC.md) | cobol-program | COPY | active |  | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:277` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active |  | `app/cbl/COACTUPC.cbl:635` |
| [COACTVWC](../../07-programs/COACTVWC.md) | cobol-program | COPY | active |  | `app/cbl/COACTVWC.cbl:241` |
| [COADM01C](../../07-programs/COADM01C.md) | cobol-program | COPY | active |  | `app/cbl/COADM01C.cbl:58` |
| [COCRDLIC](../../07-programs/COCRDLIC.md) | cobol-program | COPY | active |  | `app/cbl/COCRDLIC.cbl:285` |
| [COCRDSLC](../../07-programs/COCRDSLC.md) | cobol-program | COPY | active |  | `app/cbl/COCRDSLC.cbl:227` |
| [COCRDUPC](../../07-programs/COCRDUPC.md) | cobol-program | COPY | active |  | `app/cbl/COCRDUPC.cbl:346` |
| [COMEN01C](../../07-programs/COMEN01C.md) | cobol-program | COPY | active |  | `app/cbl/COMEN01C.cbl:58` |
| [COSGN00C](../../07-programs/COSGN00C.md) | cobol-program | COPY | active |  | `app/cbl/COSGN00C.cbl:55` |
| [COUSR00C](../../07-programs/COUSR00C.md) | cobol-program | COPY | active |  | `app/cbl/COUSR00C.cbl:81` |
| [COUSR01C](../../07-programs/COUSR01C.md) | cobol-program | COPY | active |  | `app/cbl/COUSR01C.cbl:53` |
| [COUSR02C](../../07-programs/COUSR02C.md) | cobol-program | COPY | active |  | `app/cbl/COUSR02C.cbl:65` |
| [COUSR03C](../../07-programs/COUSR03C.md) | cobol-program | COPY | active |  | `app/cbl/COUSR03C.cbl:65` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| SEC-USER-DATA | 17 | COSGN00C (2): `app/cbl/COSGN00C.cbl:213`, `app/cbl/COSGN00C.cbl:214`; COUSR00C (4): `app/cbl/COUSR00C.cbl:623`, `app/cbl/COUSR00C.cbl:624`, `app/cbl/COUSR00C.cbl:657`, ...; COUSR01C (2): `app/cbl/COUSR01C.cbl:242`, `app/cbl/COUSR01C.cbl:243`; COUSR02C (4): `app/cbl/COUSR02C.cbl:324`, `app/cbl/COUSR02C.cbl:325`, `app/cbl/COUSR02C.cbl:362`, ...; COUSR03C (2): `app/cbl/COUSR03C.cbl:271`, `app/cbl/COUSR03C.cbl:272` |
| SEC-USR-ID | 18 | COUSR00C (22): `app/cbl/COUSR00C.cbl:219`, `app/cbl/COUSR00C.cbl:221`, `app/cbl/COUSR00C.cbl:240`, ...; COUSR01C (4): `app/cbl/COUSR01C.cbl:154`, `app/cbl/COUSR01C.cbl:244`, `app/cbl/COUSR01C.cbl:245`, ...; COUSR02C (5): `app/cbl/COUSR02C.cbl:162`, `app/cbl/COUSR02C.cbl:216`, `app/cbl/COUSR02C.cbl:326`, ...; COUSR03C (5): `app/cbl/COUSR03C.cbl:160`, `app/cbl/COUSR03C.cbl:189`, `app/cbl/COUSR03C.cbl:273`, ... |
| SEC-USR-FNAME | 19 | COUSR00C (10): `app/cbl/COUSR00C.cbl:390`, `app/cbl/COUSR00C.cbl:395`, `app/cbl/COUSR00C.cbl:400`, ...; COUSR01C (1): `app/cbl/COUSR01C.cbl:155`; COUSR02C (3): `app/cbl/COUSR02C.cbl:167`, `app/cbl/COUSR02C.cbl:219`, `app/cbl/COUSR02C.cbl:220`; COUSR03C (1): `app/cbl/COUSR03C.cbl:165` |
| SEC-USR-LNAME | 20 | COUSR00C (10): `app/cbl/COUSR00C.cbl:391`, `app/cbl/COUSR00C.cbl:396`, `app/cbl/COUSR00C.cbl:401`, ...; COUSR01C (1): `app/cbl/COUSR01C.cbl:156`; COUSR02C (3): `app/cbl/COUSR02C.cbl:168`, `app/cbl/COUSR02C.cbl:223`, `app/cbl/COUSR02C.cbl:224`; COUSR03C (1): `app/cbl/COUSR03C.cbl:166` |
| SEC-USR-PWD | 21 | COSGN00C (1): `app/cbl/COSGN00C.cbl:223`; COUSR01C (1): `app/cbl/COUSR01C.cbl:157`; COUSR02C (3): `app/cbl/COUSR02C.cbl:169`, `app/cbl/COUSR02C.cbl:227`, `app/cbl/COUSR02C.cbl:228` |
| SEC-USR-TYPE | 22 | COSGN00C (1): `app/cbl/COSGN00C.cbl:227`; COUSR00C (10): `app/cbl/COUSR00C.cbl:392`, `app/cbl/COUSR00C.cbl:397`, `app/cbl/COUSR00C.cbl:402`, ...; COUSR01C (1): `app/cbl/COUSR01C.cbl:158`; COUSR02C (3): `app/cbl/COUSR02C.cbl:170`, `app/cbl/COUSR02C.cbl:231`, `app/cbl/COUSR02C.cbl:232`; COUSR03C (1): `app/cbl/COUSR03C.cbl:167` |

Named in no procedure statement of the copying programs (may still be moved as part of a group): SEC-USR-FILLER (line 23).

## Key fields

| Field | Meaning | Source |
|---|---|---|
| SEC-USER-DATA | 80-byte user security record. | `app/cpy/CSUSR01Y.cpy:17` |
| SEC-USR-ID | 8-character user id. | `app/cpy/CSUSR01Y.cpy:18` |
| SEC-USR-PWD | 8-character password stored in clear text in the record layout. | `app/cpy/CSUSR01Y.cpy:21` |
| SEC-USR-TYPE | 1-character user type (admin/user, see CDEMO-USER-TYPE in COCOM01Y). | `app/cpy/CSUSR01Y.cpy:22` |

## Observations

- dead-code: COACTUPC copies CSUSR01Y but references no SEC-USR field. (`app/cbl/COACTUPC.cbl:635`)
- security: The password field is a plain PIC X(08) with no hashing indicated by the layout. (`app/cpy/CSUSR01Y.cpy:21`)

## Sources

- `app/cpy/CSUSR01Y.cpy`
- `docs/_work/structure/copybooks/CSUSR01Y.json`
- `docs/_work/layouts/CSUSR01Y.json`
- `docs/_work/semantic/copybooks/CSUSR01Y.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
