# Layout CVACT03Y

| Item | Value |
|---|---|
| Source | `app/cpy/CVACT03Y.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 11 |
| Data items | 5 (88-levels: 0) |
| Semantic analysis | validated (batch B02) |

## Purpose

CVACT03Y defines CARD-XREF-RECORD, the 50-byte card cross-reference that links a card number to its customer id and account id. Batch programs use it to resolve a card to its account (CBTRN01C, CBTRN02C), an account to a card (CBACT04C via alternate key), to drive statements (CBSTM03A), to print (CBACT03C) and to migrate (CBEXPORT/CBIMPORT); online programs such as COACTUPC, COACTVWC, COBIL00C, COCRDSLC, COCRDUPC and COTRN02C also copy it. (Confirmed)

Evidence: `app/cpy/CVACT03Y.cpy:1-8`, `app/cbl/CBACT04C.cbl:34-39`, `app/cbl/CBTRN01C.cbl:227-239`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | CARD-XREF-RECORD |  |  | 1 | 50 | 50 |  |  |  | 4 |
| 05 | &nbsp;&nbsp;XREF-CARD-NUM | X(16) | DISPLAY | 1 | 16 | 16 |  |  |  | 5 |
| 05 | &nbsp;&nbsp;XREF-CUST-ID | 9(09) | DISPLAY | 17 | 25 | 9 |  |  |  | 6 |
| 05 | &nbsp;&nbsp;XREF-ACCT-ID | 9(11) | DISPLAY | 26 | 36 | 11 |  |  |  | 7 |
| 05 | &nbsp;&nbsp;FILLER | X(14) | DISPLAY | 37 | 50 | 14 |  |  |  | 8 |

## Level-88 conditions

None.

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [COPAUA0C](../../07-programs/COPAUA0C.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:203` |
| [COPAUS0C](../../07-programs/COPAUS0C.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:150` |
| [CBACT03C](../../07-programs/CBACT03C.md) | cobol-program | COPY | active |  | `app/cbl/CBACT03C.cbl:45` |
| [CBACT04C](../../07-programs/CBACT04C.md) | cobol-program | COPY | active |  | `app/cbl/CBACT04C.cbl:102` |
| [CBEXPORT](../../07-programs/CBEXPORT.md) | cobol-program | COPY | active |  | `app/cbl/CBEXPORT.cbl:81` |
| [CBIMPORT](../../07-programs/CBIMPORT.md) | cobol-program | COPY | active |  | `app/cbl/CBIMPORT.cbl:94` |
| [CBSTM03A](../../07-programs/CBSTM03A.md) | cobol-program | COPY | active |  | `app/cbl/CBSTM03A.CBL:53` |
| [CBTRN01C](../../07-programs/CBTRN01C.md) | cobol-program | COPY | active |  | `app/cbl/CBTRN01C.cbl:109` |
| [CBTRN02C](../../07-programs/CBTRN02C.md) | cobol-program | COPY | active |  | `app/cbl/CBTRN02C.cbl:112` |
| [CBTRN03C](../../07-programs/CBTRN03C.md) | cobol-program | COPY | active |  | `app/cbl/CBTRN03C.cbl:98` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active |  | `app/cbl/COACTUPC.cbl:643` |
| [COACTVWC](../../07-programs/COACTVWC.md) | cobol-program | COPY | active |  | `app/cbl/COACTVWC.cbl:251` |
| [COBIL00C](../../07-programs/COBIL00C.md) | cobol-program | COPY | active |  | `app/cbl/COBIL00C.cbl:81` |
| [COCRDSLC](../../07-programs/COCRDSLC.md) | cobol-program | COPY | commented out |  | `app/cbl/COCRDSLC.cbl:237` |
| [COCRDUPC](../../07-programs/COCRDUPC.md) | cobol-program | COPY | commented out |  | `app/cbl/COCRDUPC.cbl:356` |
| [COTRN02C](../../07-programs/COTRN02C.md) | cobol-program | COPY | active |  | `app/cbl/COTRN02C.cbl:90` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| CARD-XREF-RECORD | 4 | CBACT03C (3): `app/cbl/CBACT03C.cbl:78`, `app/cbl/CBACT03C.cbl:93`, `app/cbl/CBACT03C.cbl:96`; CBACT04C (1): `app/cbl/CBACT04C.cbl:394`; CBIMPORT (2): `app/cbl/CBIMPORT.cbl:354`, `app/cbl/CBIMPORT.cbl:361`; CBSTM03A (1): `app/cbl/CBSTM03A.CBL:364`; CBTRN01C (1): `app/cbl/CBTRN01C.cbl:229`; CBTRN02C (1): `app/cbl/CBTRN02C.cbl:383`; CBTRN03C (1): `app/cbl/CBTRN03C.cbl:485`; COACTUPC (2): `app/cbl/COACTUPC.cbl:3658`, `app/cbl/COACTUPC.cbl:3659`; COACTVWC (2): `app/cbl/COACTVWC.cbl:731`, `app/cbl/COACTVWC.cbl:732`; COBIL00C (2): `app/cbl/COBIL00C.cbl:412`, `app/cbl/COBIL00C.cbl:413`; COPAUA0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:479`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:480`; COPAUS0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:822`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:823`; COTRN02C (4): `app/cbl/COTRN02C.cbl:580`, `app/cbl/COTRN02C.cbl:581`, `app/cbl/COTRN02C.cbl:613`, ... |
| XREF-CARD-NUM | 5 | CBACT04C (1): `app/cbl/CBACT04C.cbl:495`; CBEXPORT (1): `app/cbl/CBEXPORT.cbl:415`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:357`; CBSTM03A (2): `app/cbl/CBSTM03A.CBL:419`, `app/cbl/CBSTM03A.CBL:420`; CBTRN01C (3): `app/cbl/CBTRN01C.cbl:171`, `app/cbl/CBTRN01C.cbl:228`, `app/cbl/CBTRN01C.cbl:236`; COACTUPC (2): `app/cbl/COACTUPC.cbl:3667`, `app/cbl/COACTUPC.cbl:3811`; COACTVWC (1): `app/cbl/COACTVWC.cbl:740`; COBIL00C (1): `app/cbl/COBIL00C.cbl:225`; COPAUA0C (5): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:475`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:481`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:482`, ...; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:831`; COTRN02C (4): `app/cbl/COTRN02C.cbl:209`, `app/cbl/COTRN02C.cbl:220`, `app/cbl/COTRN02C.cbl:615`, ... |
| XREF-CUST-ID | 6 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:416`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:358`; CBSTM03A (2): `app/cbl/CBSTM03A.CBL:372`, `app/cbl/CBSTM03A.CBL:374`; CBTRN01C (1): `app/cbl/CBTRN01C.cbl:238`; COACTUPC (1): `app/cbl/COACTUPC.cbl:3666`; COACTVWC (1): `app/cbl/COACTVWC.cbl:739`; COPAUA0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:571`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:806`; COPAUS0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:830`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:918` |
| XREF-ACCT-ID | 7 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:417`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:359`; CBSTM03A (2): `app/cbl/CBSTM03A.CBL:396`, `app/cbl/CBSTM03A.CBL:398`; CBTRN01C (2): `app/cbl/CBTRN01C.cbl:175`, `app/cbl/CBTRN01C.cbl:237`; CBTRN02C (3): `app/cbl/CBTRN02C.cbl:394`, `app/cbl/CBTRN02C.cbl:469`, `app/cbl/CBTRN02C.cbl:505`; CBTRN03C (1): `app/cbl/CBTRN03C.cbl:364`; COBIL00C (3): `app/cbl/COBIL00C.cbl:171`, `app/cbl/COBIL00C.cbl:414`, `app/cbl/COBIL00C.cbl:415`; COPAUA0C (4): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:523`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:619`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:805`, ...; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:868`; COTRN02C (4): `app/cbl/COTRN02C.cbl:206`, `app/cbl/COTRN02C.cbl:223`, `app/cbl/COTRN02C.cbl:582`, ... |

## Key fields

| Field | Meaning | Source |
|---|---|---|
| CARD-XREF-RECORD | 50-byte card cross-reference record (comment RECLN 50; field sizes add up to 50). | `app/cpy/CVACT03Y.cpy:4` |
| XREF-CARD-NUM | 16-character card number, primary key of the cross-reference file. | `app/cpy/CVACT03Y.cpy:5` |
| XREF-CUST-ID | 9-digit customer id owning the card; used by CBSTM03A to read the customer. | `app/cpy/CVACT03Y.cpy:6` |
| XREF-ACCT-ID | 11-digit account id the card is linked to; CBACT04C reads the file by this field as an alternate key. | `app/cpy/CVACT03Y.cpy:7` |

## Sources

- `app/cpy/CVACT03Y.cpy`
- `docs/_work/structure/copybooks/CVACT03Y.json`
- `docs/_work/layouts/CVACT03Y.json`
- `docs/_work/semantic/copybooks/CVACT03Y.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
