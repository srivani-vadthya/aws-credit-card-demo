# Layout CSMSG01Y

| Item | Value |
|---|---|
| Source | `app/cpy/CSMSG01Y.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 24 |
| Data items | 3 (88-levels: 0) |
| Semantic analysis | validated (batch B04) |

## Purpose

Defines CCDA-COMMON-MESSAGES, two 50-byte common message literals (thank-you and invalid-key) shared by CardDemo online programs. COACTUPC copies it but does not use either message. (Confirmed)

Evidence: `app/cpy/CSMSG01Y.cpy:17-21`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | CCDA-COMMON-MESSAGES |  |  | 1 | 50 | 50 |  |  |  | 17 |
| 05 | &nbsp;&nbsp;CCDA-MSG-THANK-YOU | X(50) | DISPLAY | 1 | 50 | 50 |  |  | 'Thank you for using CardDemo application... ' | 18 |
| 05 | CCDA-MSG-INVALID-KEY | X(50) | DISPLAY |  |  | 50 |  |  | 'Invalid key pressed. Please see below... ' | 20 |

## Level-88 conditions

None.

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [COPAUS0C](../../07-programs/COPAUS0C.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:138` |
| [COPAUS1C](../../07-programs/COPAUS1C.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:132` |
| [COTRTLIC](../../07-programs/COTRTLIC.md) | cobol-program | COPY | active |  | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:482` |
| [COTRTUPC](../../07-programs/COTRTUPC.md) | cobol-program | COPY | active |  | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:271` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active |  | `app/cbl/COACTUPC.cbl:629` |
| [COACTVWC](../../07-programs/COACTVWC.md) | cobol-program | COPY | active |  | `app/cbl/COACTVWC.cbl:235` |
| [COADM01C](../../07-programs/COADM01C.md) | cobol-program | COPY | active |  | `app/cbl/COADM01C.cbl:57` |
| [COBIL00C](../../07-programs/COBIL00C.md) | cobol-program | COPY | active |  | `app/cbl/COBIL00C.cbl:78` |
| [COCRDLIC](../../07-programs/COCRDLIC.md) | cobol-program | COPY | active |  | `app/cbl/COCRDLIC.cbl:281` |
| [COCRDSLC](../../07-programs/COCRDSLC.md) | cobol-program | COPY | active |  | `app/cbl/COCRDSLC.cbl:221` |
| [COCRDUPC](../../07-programs/COCRDUPC.md) | cobol-program | COPY | active |  | `app/cbl/COCRDUPC.cbl:340` |
| [COMEN01C](../../07-programs/COMEN01C.md) | cobol-program | COPY | active |  | `app/cbl/COMEN01C.cbl:57` |
| [CORPT00C](../../07-programs/CORPT00C.md) | cobol-program | COPY | active |  | `app/cbl/CORPT00C.cbl:144` |
| [COSGN00C](../../07-programs/COSGN00C.md) | cobol-program | COPY | active |  | `app/cbl/COSGN00C.cbl:54` |
| [COTRN00C](../../07-programs/COTRN00C.md) | cobol-program | COPY | active |  | `app/cbl/COTRN00C.cbl:76` |
| [COTRN01C](../../07-programs/COTRN01C.md) | cobol-program | COPY | active |  | `app/cbl/COTRN01C.cbl:67` |
| [COTRN02C](../../07-programs/COTRN02C.md) | cobol-program | COPY | active |  | `app/cbl/COTRN02C.cbl:86` |
| [COUSR00C](../../07-programs/COUSR00C.md) | cobol-program | COPY | active |  | `app/cbl/COUSR00C.cbl:80` |
| [COUSR01C](../../07-programs/COUSR01C.md) | cobol-program | COPY | active |  | `app/cbl/COUSR01C.cbl:52` |
| [COUSR02C](../../07-programs/COUSR02C.md) | cobol-program | COPY | active |  | `app/cbl/COUSR02C.cbl:64` |
| [COUSR03C](../../07-programs/COUSR03C.md) | cobol-program | COPY | active |  | `app/cbl/COUSR03C.cbl:64` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| CCDA-MSG-THANK-YOU | 18 | COSGN00C (1): `app/cbl/COSGN00C.cbl:89` |
| CCDA-MSG-INVALID-KEY | 20 | COADM01C (1): `app/cbl/COADM01C.cbl:105`; COBIL00C (1): `app/cbl/COBIL00C.cbl:140`; COMEN01C (1): `app/cbl/COMEN01C.cbl:101`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:248`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:196`; CORPT00C (1): `app/cbl/CORPT00C.cbl:193`; COSGN00C (1): `app/cbl/COSGN00C.cbl:93`; COTRN00C (1): `app/cbl/COTRN00C.cbl:132`; COTRN01C (1): `app/cbl/COTRN01C.cbl:130`; COTRN02C (1): `app/cbl/COTRN02C.cbl:150`; COUSR00C (1): `app/cbl/COUSR00C.cbl:135`; COUSR01C (1): `app/cbl/COUSR01C.cbl:101`; COUSR02C (1): `app/cbl/COUSR02C.cbl:129`; COUSR03C (1): `app/cbl/COUSR03C.cbl:128` |

Named in no procedure statement of the copying programs (may still be moved as part of a group): CCDA-COMMON-MESSAGES (line 17).

## Key fields

| Field | Meaning | Source |
|---|---|---|
| CCDA-MSG-THANK-YOU | Exit message 'Thank you for using CardDemo application...'. | `app/cpy/CSMSG01Y.cpy:18-19` |
| CCDA-MSG-INVALID-KEY | Message 'Invalid key pressed. Please see below...'. | `app/cpy/CSMSG01Y.cpy:20-21` |

## Observations

- dead-code: COACTUPC copies CSMSG01Y but references neither message; invalid keys are silently treated as Enter (app/cbl/COACTUPC.cbl:914-916). (`app/cbl/COACTUPC.cbl:629`)

## Sources

- `app/cpy/CSMSG01Y.cpy`
- `docs/_work/structure/copybooks/CSMSG01Y.json`
- `docs/_work/layouts/CSMSG01Y.json`
- `docs/_work/semantic/copybooks/CSMSG01Y.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
