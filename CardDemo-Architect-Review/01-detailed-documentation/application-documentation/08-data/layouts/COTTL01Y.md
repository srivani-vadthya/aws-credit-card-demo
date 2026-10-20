# Layout COTTL01Y

| Item | Value |
|---|---|
| Source | `app/cpy/COTTL01Y.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 27 |
| Data items | 4 (88-levels: 0) |
| Semantic analysis | validated (batch B04) |

## Purpose

Defines CCDA-SCREEN-TITLE, three 40-byte literal texts used as screen header titles across the CardDemo online programs. COACTUPC moves CCDA-TITLE01 and CCDA-TITLE02 into the TITLE01O and TITLE02O fields of its map in 3100-SCREEN-INIT. (Confirmed)

Evidence: `app/cpy/COTTL01Y.cpy:17-23`, `app/cbl/COACTUPC.cbl:2672-2673`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | CCDA-SCREEN-TITLE |  |  | 1 | 120 | 120 |  |  |  | 17 |
| 05 | &nbsp;&nbsp;CCDA-TITLE01 | X(40) | DISPLAY | 1 | 40 | 40 |  |  | ' AWS Mainframe Modernization ' | 18 |
| 05 | &nbsp;&nbsp;CCDA-TITLE02 | X(40) | DISPLAY | 41 | 80 | 40 |  |  | ' CardDemo ' | 20 |
| 05 | &nbsp;&nbsp;CCDA-THANK-YOU | X(40) | DISPLAY | 81 | 120 | 40 |  |  | 'Thank you for using CCDA application... ' | 23 |

## Level-88 conditions

None.

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [COPAUS0C](../../07-programs/COPAUS0C.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:132` |
| [COPAUS1C](../../07-programs/COPAUS1C.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:126` |
| [COTRTLIC](../../07-programs/COTRTLIC.md) | cobol-program | COPY | active |  | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:430` |
| [COTRTUPC](../../07-programs/COTRTUPC.md) | cobol-program | COPY | active |  | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:262` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active |  | `app/cbl/COACTUPC.cbl:620` |
| [COACTVWC](../../07-programs/COACTVWC.md) | cobol-program | COPY | active |  | `app/cbl/COACTVWC.cbl:226` |
| [COADM01C](../../07-programs/COADM01C.md) | cobol-program | COPY | active |  | `app/cbl/COADM01C.cbl:55` |
| [COBIL00C](../../07-programs/COBIL00C.md) | cobol-program | COPY | active |  | `app/cbl/COBIL00C.cbl:76` |
| [COCRDLIC](../../07-programs/COCRDLIC.md) | cobol-program | COPY | active |  | `app/cbl/COCRDLIC.cbl:272` |
| [COCRDSLC](../../07-programs/COCRDSLC.md) | cobol-program | COPY | active |  | `app/cbl/COCRDSLC.cbl:213` |
| [COCRDUPC](../../07-programs/COCRDUPC.md) | cobol-program | COPY | active |  | `app/cbl/COCRDUPC.cbl:332` |
| [COMEN01C](../../07-programs/COMEN01C.md) | cobol-program | COPY | active |  | `app/cbl/COMEN01C.cbl:55` |
| [CORPT00C](../../07-programs/CORPT00C.md) | cobol-program | COPY | active |  | `app/cbl/CORPT00C.cbl:142` |
| [COSGN00C](../../07-programs/COSGN00C.md) | cobol-program | COPY | active |  | `app/cbl/COSGN00C.cbl:52` |
| [COTRN00C](../../07-programs/COTRN00C.md) | cobol-program | COPY | active |  | `app/cbl/COTRN00C.cbl:74` |
| [COTRN01C](../../07-programs/COTRN01C.md) | cobol-program | COPY | active |  | `app/cbl/COTRN01C.cbl:65` |
| [COTRN02C](../../07-programs/COTRN02C.md) | cobol-program | COPY | active |  | `app/cbl/COTRN02C.cbl:84` |
| [COUSR00C](../../07-programs/COUSR00C.md) | cobol-program | COPY | active |  | `app/cbl/COUSR00C.cbl:78` |
| [COUSR01C](../../07-programs/COUSR01C.md) | cobol-program | COPY | active |  | `app/cbl/COUSR01C.cbl:50` |
| [COUSR02C](../../07-programs/COUSR02C.md) | cobol-program | COPY | active |  | `app/cbl/COUSR02C.cbl:62` |
| [COUSR03C](../../07-programs/COUSR03C.md) | cobol-program | COPY | active |  | `app/cbl/COUSR03C.cbl:62` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| CCDA-TITLE01 | 18 | COACTUPC (1): `app/cbl/COACTUPC.cbl:2673`; COACTVWC (1): `app/cbl/COACTVWC.cbl:436`; COADM01C (1): `app/cbl/COADM01C.cbl:209`; COBIL00C (1): `app/cbl/COBIL00C.cbl:323`; COCRDLIC (1): `app/cbl/COCRDLIC.cbl:647`; COCRDSLC (1): `app/cbl/COCRDSLC.cbl:432`; COCRDUPC (1): `app/cbl/COCRDUPC.cbl:1057`; COMEN01C (1): `app/cbl/COMEN01C.cbl:242`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:731`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:413`; CORPT00C (1): `app/cbl/CORPT00C.cbl:613`; COSGN00C (1): `app/cbl/COSGN00C.cbl:181`; COTRN00C (1): `app/cbl/COTRN00C.cbl:571`; COTRN01C (1): `app/cbl/COTRN01C.cbl:247`; COTRN02C (1): `app/cbl/COTRN02C.cbl:556`; COTRTLIC (1): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1298`; COTRTUPC (1): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1115`; COUSR00C (1): `app/cbl/COUSR00C.cbl:566`; COUSR01C (1): `app/cbl/COUSR01C.cbl:218`; COUSR02C (1): `app/cbl/COUSR02C.cbl:300`; COUSR03C (1): `app/cbl/COUSR03C.cbl:247` |
| CCDA-TITLE02 | 20 | COACTUPC (1): `app/cbl/COACTUPC.cbl:2674`; COACTVWC (1): `app/cbl/COACTVWC.cbl:437`; COADM01C (1): `app/cbl/COADM01C.cbl:210`; COBIL00C (1): `app/cbl/COBIL00C.cbl:324`; COCRDLIC (1): `app/cbl/COCRDLIC.cbl:648`; COCRDSLC (1): `app/cbl/COCRDSLC.cbl:433`; COCRDUPC (1): `app/cbl/COCRDUPC.cbl:1058`; COMEN01C (1): `app/cbl/COMEN01C.cbl:243`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:732`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:414`; CORPT00C (1): `app/cbl/CORPT00C.cbl:614`; COSGN00C (1): `app/cbl/COSGN00C.cbl:182`; COTRN00C (1): `app/cbl/COTRN00C.cbl:572`; COTRN01C (1): `app/cbl/COTRN01C.cbl:248`; COTRN02C (1): `app/cbl/COTRN02C.cbl:557`; COTRTLIC (1): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1299`; COTRTUPC (1): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1116`; COUSR00C (1): `app/cbl/COUSR00C.cbl:567`; COUSR01C (1): `app/cbl/COUSR01C.cbl:219`; COUSR02C (1): `app/cbl/COUSR02C.cbl:301`; COUSR03C (1): `app/cbl/COUSR03C.cbl:248` |

Named in no procedure statement of the copying programs (may still be moved as part of a group): CCDA-SCREEN-TITLE (line 17), CCDA-THANK-YOU (line 23).

## Key fields

| Field | Meaning | Source |
|---|---|---|
| CCDA-TITLE01 | First screen title line, '      AWS Mainframe Modernization       '. | `app/cpy/COTTL01Y.cpy:18-19` |
| CCDA-TITLE02 | Second screen title line, '              CardDemo                  '. | `app/cpy/COTTL01Y.cpy:20-22` |
| CCDA-THANK-YOU | Closing text 'Thank you for using CCDA application... '; not referenced by COACTUPC. | `app/cpy/COTTL01Y.cpy:23-24` |

## Observations

- hardcoded-value: An older title value 'Credit Card Demo Application (CCDA)' is kept as a comment above the active CardDemo title. (`app/cpy/COTTL01Y.cpy:21`)

## Sources

- `app/cpy/COTTL01Y.cpy`
- `docs/_work/structure/copybooks/COTTL01Y.json`
- `docs/_work/layouts/COTTL01Y.json`
- `docs/_work/semantic/copybooks/COTTL01Y.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
