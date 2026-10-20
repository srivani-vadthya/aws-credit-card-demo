# Layout CVTRA05Y

| Item | Value |
|---|---|
| Source | `app/cpy/CVTRA05Y.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 21 |
| Data items | 15 (88-levels: 0) |
| Semantic analysis | validated (batch B02) |

## Purpose

CVTRA05Y defines TRAN-RECORD, the 350-byte posted transaction entity: id, type and category codes, source, description, amount, merchant details, card number and origination/processing timestamps. It is written by CBACT04C (interest) and CBTRN02C (posting), read by reporting and migration programs (CBTRN03C, CBEXPORT, CBIMPORT) and by online programs COBIL00C, CORPT00C, COTRN00C, COTRN01C and COTRN02C. (Confirmed)

Evidence: `app/cpy/CVTRA05Y.cpy:1-18`, `app/cbl/CBACT04C.cbl:473-500`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | TRAN-RECORD |  |  | 1 | 350 | 350 |  |  |  | 4 |
| 05 | &nbsp;&nbsp;TRAN-ID | X(16) | DISPLAY | 1 | 16 | 16 |  |  |  | 5 |
| 05 | &nbsp;&nbsp;TRAN-TYPE-CD | X(02) | DISPLAY | 17 | 18 | 2 |  |  |  | 6 |
| 05 | &nbsp;&nbsp;TRAN-CAT-CD | 9(04) | DISPLAY | 19 | 22 | 4 |  |  |  | 7 |
| 05 | &nbsp;&nbsp;TRAN-SOURCE | X(10) | DISPLAY | 23 | 32 | 10 |  |  |  | 8 |
| 05 | &nbsp;&nbsp;TRAN-DESC | X(100) | DISPLAY | 33 | 132 | 100 |  |  |  | 9 |
| 05 | &nbsp;&nbsp;TRAN-AMT | S9(09)V99 | DISPLAY | 133 | 143 | 11 |  |  |  | 10 |
| 05 | &nbsp;&nbsp;TRAN-MERCHANT-ID | 9(09) | DISPLAY | 144 | 152 | 9 |  |  |  | 11 |
| 05 | &nbsp;&nbsp;TRAN-MERCHANT-NAME | X(50) | DISPLAY | 153 | 202 | 50 |  |  |  | 12 |
| 05 | &nbsp;&nbsp;TRAN-MERCHANT-CITY | X(50) | DISPLAY | 203 | 252 | 50 |  |  |  | 13 |
| 05 | &nbsp;&nbsp;TRAN-MERCHANT-ZIP | X(10) | DISPLAY | 253 | 262 | 10 |  |  |  | 14 |
| 05 | &nbsp;&nbsp;TRAN-CARD-NUM | X(16) | DISPLAY | 263 | 278 | 16 |  |  |  | 15 |
| 05 | &nbsp;&nbsp;TRAN-ORIG-TS | X(26) | DISPLAY | 279 | 304 | 26 |  |  |  | 16 |
| 05 | &nbsp;&nbsp;TRAN-PROC-TS | X(26) | DISPLAY | 305 | 330 | 26 |  |  |  | 17 |
| 05 | &nbsp;&nbsp;FILLER | X(20) | DISPLAY | 331 | 350 | 20 |  |  |  | 18 |

## Level-88 conditions

None.

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [CBACT04C](../../07-programs/CBACT04C.md) | cobol-program | COPY | active |  | `app/cbl/CBACT04C.cbl:117` |
| [CBEXPORT](../../07-programs/CBEXPORT.md) | cobol-program | COPY | active |  | `app/cbl/CBEXPORT.cbl:84` |
| [CBIMPORT](../../07-programs/CBIMPORT.md) | cobol-program | COPY | active |  | `app/cbl/CBIMPORT.cbl:99` |
| [CBTRN01C](../../07-programs/CBTRN01C.md) | cobol-program | COPY | active |  | `app/cbl/CBTRN01C.cbl:124` |
| [CBTRN02C](../../07-programs/CBTRN02C.md) | cobol-program | COPY | active |  | `app/cbl/CBTRN02C.cbl:107` |
| [CBTRN03C](../../07-programs/CBTRN03C.md) | cobol-program | COPY | active |  | `app/cbl/CBTRN03C.cbl:93` |
| [COBIL00C](../../07-programs/COBIL00C.md) | cobol-program | COPY | active |  | `app/cbl/COBIL00C.cbl:82` |
| [CORPT00C](../../07-programs/CORPT00C.md) | cobol-program | COPY | active |  | `app/cbl/CORPT00C.cbl:146` |
| [COTRN00C](../../07-programs/COTRN00C.md) | cobol-program | COPY | active |  | `app/cbl/COTRN00C.cbl:78` |
| [COTRN01C](../../07-programs/COTRN01C.md) | cobol-program | COPY | active |  | `app/cbl/COTRN01C.cbl:69` |
| [COTRN02C](../../07-programs/COTRN02C.md) | cobol-program | COPY | active |  | `app/cbl/COTRN02C.cbl:88` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| TRAN-RECORD | 4 | CBACT04C (1): `app/cbl/CBACT04C.cbl:500`; CBIMPORT (2): `app/cbl/CBIMPORT.cbl:374`, `app/cbl/CBIMPORT.cbl:391`; CBTRN02C (1): `app/cbl/CBTRN02C.cbl:564`; CBTRN03C (7): `app/cbl/CBTRN03C.cbl:180`, `app/cbl/CBTRN03C.cbl:189`, `app/cbl/CBTRN03C.cbl:191`, ...; COBIL00C (5): `app/cbl/COBIL00C.cbl:218`, `app/cbl/COBIL00C.cbl:476`, `app/cbl/COBIL00C.cbl:477`, ...; COTRN00C (4): `app/cbl/COTRN00C.cbl:628`, `app/cbl/COTRN00C.cbl:629`, `app/cbl/COTRN00C.cbl:662`, ...; COTRN01C (2): `app/cbl/COTRN01C.cbl:271`, `app/cbl/COTRN01C.cbl:272`; COTRN02C (5): `app/cbl/COTRN02C.cbl:450`, `app/cbl/COTRN02C.cbl:677`, `app/cbl/COTRN02C.cbl:678`, ... |
| TRAN-ID | 5 | CBACT04C (1): `app/cbl/CBACT04C.cbl:479`; CBEXPORT (1): `app/cbl/CBEXPORT.cbl:470`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:377`; CBTRN02C (1): `app/cbl/CBTRN02C.cbl:425`; CBTRN03C (1): `app/cbl/CBTRN03C.cbl:363`; COBIL00C (11): `app/cbl/COBIL00C.cbl:212`, `app/cbl/COBIL00C.cbl:216`, `app/cbl/COBIL00C.cbl:219`, ...; COTRN00C (22): `app/cbl/COTRN00C.cbl:207`, `app/cbl/COTRN00C.cbl:210`, `app/cbl/COTRN00C.cbl:237`, ...; COTRN01C (4): `app/cbl/COTRN01C.cbl:172`, `app/cbl/COTRN01C.cbl:178`, `app/cbl/COTRN01C.cbl:273`, ...; COTRN02C (12): `app/cbl/COTRN02C.cbl:444`, `app/cbl/COTRN02C.cbl:448`, `app/cbl/COTRN02C.cbl:451`, ... |
| TRAN-TYPE-CD | 6 | CBACT04C (1): `app/cbl/CBACT04C.cbl:482`; CBEXPORT (1): `app/cbl/CBEXPORT.cbl:471`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:378`; CBTRN02C (1): `app/cbl/CBTRN02C.cbl:426`; CBTRN03C (3): `app/cbl/CBTRN03C.cbl:189`, `app/cbl/CBTRN03C.cbl:191`, `app/cbl/CBTRN03C.cbl:365`; COBIL00C (1): `app/cbl/COBIL00C.cbl:220`; COTRN01C (1): `app/cbl/COTRN01C.cbl:180`; COTRN02C (2): `app/cbl/COTRN02C.cbl:452`, `app/cbl/COTRN02C.cbl:482` |
| TRAN-CAT-CD | 7 | CBACT04C (1): `app/cbl/CBACT04C.cbl:483`; CBEXPORT (1): `app/cbl/CBEXPORT.cbl:472`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:379`; CBTRN02C (1): `app/cbl/CBTRN02C.cbl:427`; CBTRN03C (2): `app/cbl/CBTRN03C.cbl:193`, `app/cbl/CBTRN03C.cbl:367`; COBIL00C (1): `app/cbl/COBIL00C.cbl:221`; COTRN01C (1): `app/cbl/COTRN01C.cbl:181`; COTRN02C (2): `app/cbl/COTRN02C.cbl:453`, `app/cbl/COTRN02C.cbl:483` |
| TRAN-SOURCE | 8 | CBACT04C (1): `app/cbl/CBACT04C.cbl:484`; CBEXPORT (1): `app/cbl/CBEXPORT.cbl:473`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:380`; CBTRN02C (1): `app/cbl/CBTRN02C.cbl:428`; CBTRN03C (1): `app/cbl/CBTRN03C.cbl:369`; COBIL00C (1): `app/cbl/COBIL00C.cbl:222`; COTRN01C (1): `app/cbl/COTRN01C.cbl:182`; COTRN02C (2): `app/cbl/COTRN02C.cbl:454`, `app/cbl/COTRN02C.cbl:484` |
| TRAN-DESC | 9 | CBACT04C (1): `app/cbl/CBACT04C.cbl:488`; CBEXPORT (1): `app/cbl/CBEXPORT.cbl:474`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:381`; CBTRN02C (1): `app/cbl/CBTRN02C.cbl:429`; COBIL00C (1): `app/cbl/COBIL00C.cbl:223`; COTRN00C (10): `app/cbl/COTRN00C.cbl:395`, `app/cbl/COTRN00C.cbl:400`, `app/cbl/COTRN00C.cbl:405`, ...; COTRN01C (1): `app/cbl/COTRN01C.cbl:184`; COTRN02C (2): `app/cbl/COTRN02C.cbl:455`, `app/cbl/COTRN02C.cbl:486` |
| TRAN-AMT | 10 | CBACT04C (1): `app/cbl/CBACT04C.cbl:490`; CBEXPORT (1): `app/cbl/CBEXPORT.cbl:475`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:382`; CBTRN02C (1): `app/cbl/CBTRN02C.cbl:430`; CBTRN03C (4): `app/cbl/CBTRN03C.cbl:198`, `app/cbl/CBTRN03C.cbl:200`, `app/cbl/CBTRN03C.cbl:287`, ...; COBIL00C (2): `app/cbl/COBIL00C.cbl:224`, `app/cbl/COBIL00C.cbl:234`; COTRN00C (1): `app/cbl/COTRN00C.cbl:383`; COTRN01C (1): `app/cbl/COTRN01C.cbl:177`; COTRN02C (2): `app/cbl/COTRN02C.cbl:458`, `app/cbl/COTRN02C.cbl:481` |
| TRAN-MERCHANT-ID | 11 | CBACT04C (1): `app/cbl/CBACT04C.cbl:491`; CBEXPORT (1): `app/cbl/CBEXPORT.cbl:476`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:383`; CBTRN02C (1): `app/cbl/CBTRN02C.cbl:431`; COBIL00C (1): `app/cbl/COBIL00C.cbl:226`; COTRN01C (1): `app/cbl/COTRN01C.cbl:187`; COTRN02C (2): `app/cbl/COTRN02C.cbl:460`, `app/cbl/COTRN02C.cbl:489` |
| TRAN-MERCHANT-NAME | 12 | CBACT04C (1): `app/cbl/CBACT04C.cbl:492`; CBEXPORT (1): `app/cbl/CBEXPORT.cbl:477`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:384`; CBTRN02C (1): `app/cbl/CBTRN02C.cbl:432`; COBIL00C (1): `app/cbl/COBIL00C.cbl:227`; COTRN01C (1): `app/cbl/COTRN01C.cbl:188`; COTRN02C (2): `app/cbl/COTRN02C.cbl:461`, `app/cbl/COTRN02C.cbl:490` |
| TRAN-MERCHANT-CITY | 13 | CBACT04C (1): `app/cbl/CBACT04C.cbl:493`; CBEXPORT (1): `app/cbl/CBEXPORT.cbl:478`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:385`; CBTRN02C (1): `app/cbl/CBTRN02C.cbl:433`; COBIL00C (1): `app/cbl/COBIL00C.cbl:228`; COTRN01C (1): `app/cbl/COTRN01C.cbl:189`; COTRN02C (2): `app/cbl/COTRN02C.cbl:462`, `app/cbl/COTRN02C.cbl:491` |
| TRAN-MERCHANT-ZIP | 14 | CBACT04C (1): `app/cbl/CBACT04C.cbl:494`; CBEXPORT (1): `app/cbl/CBEXPORT.cbl:479`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:386`; CBTRN02C (1): `app/cbl/CBTRN02C.cbl:434`; COBIL00C (1): `app/cbl/COBIL00C.cbl:229`; COTRN01C (1): `app/cbl/COTRN01C.cbl:190`; COTRN02C (2): `app/cbl/COTRN02C.cbl:463`, `app/cbl/COTRN02C.cbl:492` |
| TRAN-CARD-NUM | 15 | CBACT04C (1): `app/cbl/CBACT04C.cbl:495`; CBEXPORT (1): `app/cbl/CBEXPORT.cbl:480`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:387`; CBTRN02C (1): `app/cbl/CBTRN02C.cbl:435`; CBTRN03C (3): `app/cbl/CBTRN03C.cbl:181`, `app/cbl/CBTRN03C.cbl:185`, `app/cbl/CBTRN03C.cbl:186`; COBIL00C (1): `app/cbl/COBIL00C.cbl:225`; COTRN01C (1): `app/cbl/COTRN01C.cbl:179`; COTRN02C (1): `app/cbl/COTRN02C.cbl:459` |
| TRAN-ORIG-TS | 16 | CBACT04C (1): `app/cbl/CBACT04C.cbl:497`; CBEXPORT (1): `app/cbl/CBEXPORT.cbl:481`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:388`; CBTRN02C (1): `app/cbl/CBTRN02C.cbl:436`; COBIL00C (1): `app/cbl/COBIL00C.cbl:231`; COTRN00C (1): `app/cbl/COTRN00C.cbl:384`; COTRN01C (1): `app/cbl/COTRN01C.cbl:185`; COTRN02C (2): `app/cbl/COTRN02C.cbl:464`, `app/cbl/COTRN02C.cbl:487` |
| TRAN-PROC-TS | 17 | CBACT04C (1): `app/cbl/CBACT04C.cbl:498`; CBEXPORT (1): `app/cbl/CBEXPORT.cbl:482`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:389`; CBTRN02C (1): `app/cbl/CBTRN02C.cbl:438`; CBTRN03C (2): `app/cbl/CBTRN03C.cbl:173`, `app/cbl/CBTRN03C.cbl:174`; COBIL00C (1): `app/cbl/COBIL00C.cbl:232`; COTRN01C (1): `app/cbl/COTRN01C.cbl:186`; COTRN02C (2): `app/cbl/COTRN02C.cbl:465`, `app/cbl/COTRN02C.cbl:488` |

## Key fields

| Field | Meaning | Source |
|---|---|---|
| TRAN-RECORD | 350-byte posted transaction record (comment RECLN 350; field sizes add up to 350). | `app/cpy/CVTRA05Y.cpy:4` |
| TRAN-ID | 16-byte transaction id, key of the transaction file; CBACT04C builds it from the run date and a 6-digit sequence. | `app/cpy/CVTRA05Y.cpy:5` |
| TRAN-TYPE-CD | 2-character transaction type code (CBACT04C uses '01' for interest). | `app/cpy/CVTRA05Y.cpy:6` |
| TRAN-CAT-CD | 4-digit transaction category code (CBACT04C uses 5 for interest). | `app/cpy/CVTRA05Y.cpy:7` |
| TRAN-SOURCE | 10-byte origin of the transaction (e.g. 'System' for interest). | `app/cpy/CVTRA05Y.cpy:8` |
| TRAN-AMT | Signed amount S9(09)V99. | `app/cpy/CVTRA05Y.cpy:10` |
| TRAN-MERCHANT-ID | 9-digit merchant id, with merchant name, city and ZIP following. | `app/cpy/CVTRA05Y.cpy:11-14` |
| TRAN-CARD-NUM | Card number the transaction is charged to. | `app/cpy/CVTRA05Y.cpy:15` |
| TRAN-ORIG-TS | 26-byte origination timestamp (DB2 format YYYY-MM-DD-HH.MM.SS.nnnnnn in CBACT04C). | `app/cpy/CVTRA05Y.cpy:16` |
| TRAN-PROC-TS | 26-byte processing timestamp. | `app/cpy/CVTRA05Y.cpy:17` |

## Sources

- `app/cpy/CVTRA05Y.cpy`
- `docs/_work/structure/copybooks/CVTRA05Y.json`
- `docs/_work/layouts/CVTRA05Y.json`
- `docs/_work/semantic/copybooks/CVTRA05Y.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
