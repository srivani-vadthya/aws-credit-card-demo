# Layout CVACT02Y

| Item | Value |
|---|---|
| Source | `app/cpy/CVACT02Y.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 14 |
| Data items | 8 (88-levels: 0) |
| Semantic analysis | validated (batch B02) |

## Purpose

CVACT02Y defines CARD-RECORD, the 150-byte card master entity: card number (key), owning account id, CVV, embossed name, expiration date and active status. It is used by the card print utility CBACT02C, the migration programs CBEXPORT and CBIMPORT, CBTRN01C, and online card/account programs (COACTVWC, COCRDLIC, COCRDSLC, COCRDUPC, COPAUS0C, COTRTLIC). (Confirmed)

Evidence: `app/cpy/CVACT02Y.cpy:1-11`, `app/cbl/CBACT02C.cbl:28-45`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | CARD-RECORD |  |  | 1 | 150 | 150 |  |  |  | 4 |
| 05 | &nbsp;&nbsp;CARD-NUM | X(16) | DISPLAY | 1 | 16 | 16 |  |  |  | 5 |
| 05 | &nbsp;&nbsp;CARD-ACCT-ID | 9(11) | DISPLAY | 17 | 27 | 11 |  |  |  | 6 |
| 05 | &nbsp;&nbsp;CARD-CVV-CD | 9(03) | DISPLAY | 28 | 30 | 3 |  |  |  | 7 |
| 05 | &nbsp;&nbsp;CARD-EMBOSSED-NAME | X(50) | DISPLAY | 31 | 80 | 50 |  |  |  | 8 |
| 05 | &nbsp;&nbsp;CARD-EXPIRAION-DATE | X(10) | DISPLAY | 81 | 90 | 10 |  |  |  | 9 |
| 05 | &nbsp;&nbsp;CARD-ACTIVE-STATUS | X(01) | DISPLAY | 91 | 91 | 1 |  |  |  | 10 |
| 05 | &nbsp;&nbsp;FILLER | X(59) | DISPLAY | 92 | 150 | 59 |  |  |  | 11 |

## Level-88 conditions

None.

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [COPAUS0C](../../07-programs/COPAUS0C.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:147` |
| [COTRTLIC](../../07-programs/COTRTLIC.md) | cobol-program | COPY | active |  | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:490` |
| [CBACT02C](../../07-programs/CBACT02C.md) | cobol-program | COPY | active |  | `app/cbl/CBACT02C.cbl:45` |
| [CBEXPORT](../../07-programs/CBEXPORT.md) | cobol-program | COPY | active |  | `app/cbl/CBEXPORT.cbl:87` |
| [CBIMPORT](../../07-programs/CBIMPORT.md) | cobol-program | COPY | active |  | `app/cbl/CBIMPORT.cbl:104` |
| [CBTRN01C](../../07-programs/CBTRN01C.md) | cobol-program | COPY | active |  | `app/cbl/CBTRN01C.cbl:114` |
| [COACTVWC](../../07-programs/COACTVWC.md) | cobol-program | COPY | active |  | `app/cbl/COACTVWC.cbl:248` |
| [COCRDLIC](../../07-programs/COCRDLIC.md) | cobol-program | COPY | active |  | `app/cbl/COCRDLIC.cbl:290` |
| [COCRDSLC](../../07-programs/COCRDSLC.md) | cobol-program | COPY | active |  | `app/cbl/COCRDSLC.cbl:234` |
| [COCRDUPC](../../07-programs/COCRDUPC.md) | cobol-program | COPY | active |  | `app/cbl/COCRDUPC.cbl:353` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| CARD-RECORD | 4 | CBACT02C (2): `app/cbl/CBACT02C.cbl:78`, `app/cbl/CBACT02C.cbl:93`; CBIMPORT (2): `app/cbl/CBIMPORT.cbl:404`, `app/cbl/CBIMPORT.cbl:414`; COCRDLIC (8): `app/cbl/COCRDLIC.cbl:1148`, `app/cbl/COCRDLIC.cbl:1149`, `app/cbl/COCRDLIC.cbl:1199`, ...; COCRDSLC (4): `app/cbl/COCRDSLC.cbl:746`, `app/cbl/COCRDSLC.cbl:747`, `app/cbl/COCRDSLC.cbl:787`, ...; COCRDUPC (4): `app/cbl/COCRDUPC.cbl:1386`, `app/cbl/COCRDUPC.cbl:1387`, `app/cbl/COCRDUPC.cbl:1432`, ... |
| CARD-NUM | 5 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:535`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:407`; COCRDLIC (8): `app/cbl/COCRDLIC.cbl:1165`, `app/cbl/COCRDLIC.cbl:1176`, `app/cbl/COCRDLIC.cbl:1195`, ... |
| CARD-ACCT-ID | 6 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:536`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:408`; COCRDLIC (8): `app/cbl/COCRDLIC.cbl:1167`, `app/cbl/COCRDLIC.cbl:1174`, `app/cbl/COCRDLIC.cbl:1194`, ... |
| CARD-CVV-CD | 7 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:537`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:409`; COCRDUPC (3): `app/cbl/COCRDUPC.cbl:1354`, `app/cbl/COCRDUPC.cbl:1503`, `app/cbl/COCRDUPC.cbl:1512` |
| CARD-EMBOSSED-NAME | 8 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:538`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:410`; COCRDSLC (1): `app/cbl/COCRDSLC.cbl:475`; COCRDUPC (6): `app/cbl/COCRDUPC.cbl:673`, `app/cbl/COCRDUPC.cbl:1356`, `app/cbl/COCRDUPC.cbl:1360`, ... |
| CARD-EXPIRAION-DATE | 9 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:539`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:411`; COCRDSLC (1): `app/cbl/COCRDSLC.cbl:477`; COCRDUPC (9): `app/cbl/COCRDUPC.cbl:1361`, `app/cbl/COCRDUPC.cbl:1363`, `app/cbl/COCRDUPC.cbl:1365`, ... |
| CARD-ACTIVE-STATUS | 10 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:540`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:412`; COCRDLIC (2): `app/cbl/COCRDLIC.cbl:1169`, `app/cbl/COCRDLIC.cbl:1342`; COCRDSLC (1): `app/cbl/COCRDSLC.cbl:484`; COCRDUPC (4): `app/cbl/COCRDUPC.cbl:674`, `app/cbl/COCRDUPC.cbl:1367`, `app/cbl/COCRDUPC.cbl:1508`, ... |

## Key fields

| Field | Meaning | Source |
|---|---|---|
| CARD-RECORD | 150-byte card master record (comment RECLN 150; field sizes add up to 150). | `app/cpy/CVACT02Y.cpy:4` |
| CARD-NUM | 16-character card number, key of the card file. | `app/cpy/CVACT02Y.cpy:5` |
| CARD-ACCT-ID | 11-digit account number the card belongs to. | `app/cpy/CVACT02Y.cpy:6` |
| CARD-CVV-CD | 3-digit card verification value stored in clear (sensitive). | `app/cpy/CVACT02Y.cpy:7` |
| CARD-EMBOSSED-NAME | Name embossed on the card. | `app/cpy/CVACT02Y.cpy:8` |
| CARD-EXPIRAION-DATE | 10-byte card expiration date (misspelled name). | `app/cpy/CVACT02Y.cpy:9` |
| CARD-ACTIVE-STATUS | 1-byte card active status flag; no 88-level values defined. | `app/cpy/CVACT02Y.cpy:10` |

## Observations

- security: The card verification value is part of the stored card record in plain digits; CBACT02C prints it and CBEXPORT exports it. (`app/cpy/CVACT02Y.cpy:7`)

## Sources

- `app/cpy/CVACT02Y.cpy`
- `docs/_work/structure/copybooks/CVACT02Y.json`
- `docs/_work/layouts/CVACT02Y.json`
- `docs/_work/semantic/copybooks/CVACT02Y.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
