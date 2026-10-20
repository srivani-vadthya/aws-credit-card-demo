# Layout CVCUS01Y

| Item | Value |
|---|---|
| Source | `app/cpy/CVCUS01Y.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 26 |
| Data items | 20 (88-levels: 0) |
| Semantic analysis | validated (batch B02) |

## Purpose

CVCUS01Y defines CUSTOMER-RECORD, the standard 500-byte customer master entity: id, names, address, phones, SSN, government id, date of birth, EFT account id, primary card holder indicator and FICO score. It is used by the print utility CBCUS01C, migration programs CBEXPORT and CBIMPORT, CBTRN01C and online programs (COACTUPC, COACTVWC, COCRDSLC, COCRDUPC, COPAUA0C, COPAUS0C). (Confirmed)

Evidence: `app/cpy/CVCUS01Y.cpy:1-23`, `app/cbl/CBCUS01C.cbl:28-45`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | CUSTOMER-RECORD |  |  | 1 | 500 | 500 |  |  |  | 4 |
| 05 | &nbsp;&nbsp;CUST-ID | 9(09) | DISPLAY | 1 | 9 | 9 |  |  |  | 5 |
| 05 | &nbsp;&nbsp;CUST-FIRST-NAME | X(25) | DISPLAY | 10 | 34 | 25 |  |  |  | 6 |
| 05 | &nbsp;&nbsp;CUST-MIDDLE-NAME | X(25) | DISPLAY | 35 | 59 | 25 |  |  |  | 7 |
| 05 | &nbsp;&nbsp;CUST-LAST-NAME | X(25) | DISPLAY | 60 | 84 | 25 |  |  |  | 8 |
| 05 | &nbsp;&nbsp;CUST-ADDR-LINE-1 | X(50) | DISPLAY | 85 | 134 | 50 |  |  |  | 9 |
| 05 | &nbsp;&nbsp;CUST-ADDR-LINE-2 | X(50) | DISPLAY | 135 | 184 | 50 |  |  |  | 10 |
| 05 | &nbsp;&nbsp;CUST-ADDR-LINE-3 | X(50) | DISPLAY | 185 | 234 | 50 |  |  |  | 11 |
| 05 | &nbsp;&nbsp;CUST-ADDR-STATE-CD | X(02) | DISPLAY | 235 | 236 | 2 |  |  |  | 12 |
| 05 | &nbsp;&nbsp;CUST-ADDR-COUNTRY-CD | X(03) | DISPLAY | 237 | 239 | 3 |  |  |  | 13 |
| 05 | &nbsp;&nbsp;CUST-ADDR-ZIP | X(10) | DISPLAY | 240 | 249 | 10 |  |  |  | 14 |
| 05 | &nbsp;&nbsp;CUST-PHONE-NUM-1 | X(15) | DISPLAY | 250 | 264 | 15 |  |  |  | 15 |
| 05 | &nbsp;&nbsp;CUST-PHONE-NUM-2 | X(15) | DISPLAY | 265 | 279 | 15 |  |  |  | 16 |
| 05 | &nbsp;&nbsp;CUST-SSN | 9(09) | DISPLAY | 280 | 288 | 9 |  |  |  | 17 |
| 05 | &nbsp;&nbsp;CUST-GOVT-ISSUED-ID | X(20) | DISPLAY | 289 | 308 | 20 |  |  |  | 18 |
| 05 | &nbsp;&nbsp;CUST-DOB-YYYY-MM-DD | X(10) | DISPLAY | 309 | 318 | 10 |  |  |  | 19 |
| 05 | &nbsp;&nbsp;CUST-EFT-ACCOUNT-ID | X(10) | DISPLAY | 319 | 328 | 10 |  |  |  | 20 |
| 05 | &nbsp;&nbsp;CUST-PRI-CARD-HOLDER-IND | X(01) | DISPLAY | 329 | 329 | 1 |  |  |  | 21 |
| 05 | &nbsp;&nbsp;CUST-FICO-CREDIT-SCORE | 9(03) | DISPLAY | 330 | 332 | 3 |  |  |  | 22 |
| 05 | &nbsp;&nbsp;FILLER | X(168) | DISPLAY | 333 | 500 | 168 |  |  |  | 23 |

## Level-88 conditions

None.

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [COPAUA0C](../../07-programs/COPAUA0C.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:209` |
| [COPAUS0C](../../07-programs/COPAUS0C.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:153` |
| [CBCUS01C](../../07-programs/CBCUS01C.md) | cobol-program | COPY | active |  | `app/cbl/CBCUS01C.cbl:45` |
| [CBEXPORT](../../07-programs/CBEXPORT.md) | cobol-program | COPY | active |  | `app/cbl/CBEXPORT.cbl:75` |
| [CBIMPORT](../../07-programs/CBIMPORT.md) | cobol-program | COPY | active |  | `app/cbl/CBIMPORT.cbl:84` |
| [CBTRN01C](../../07-programs/CBTRN01C.md) | cobol-program | COPY | active |  | `app/cbl/CBTRN01C.cbl:104` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active |  | `app/cbl/COACTUPC.cbl:646` |
| [COACTVWC](../../07-programs/COACTVWC.md) | cobol-program | COPY | active |  | `app/cbl/COACTVWC.cbl:254` |
| [COCRDSLC](../../07-programs/COCRDSLC.md) | cobol-program | COPY | active |  | `app/cbl/COCRDSLC.cbl:240` |
| [COCRDUPC](../../07-programs/COCRDUPC.md) | cobol-program | COPY | active |  | `app/cbl/COCRDUPC.cbl:359` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| CUSTOMER-RECORD | 4 | CBCUS01C (3): `app/cbl/CBCUS01C.cbl:78`, `app/cbl/CBCUS01C.cbl:93`, `app/cbl/CBCUS01C.cbl:96`; CBIMPORT (2): `app/cbl/CBIMPORT.cbl:290`, `app/cbl/CBIMPORT.cbl:312`; COACTUPC (4): `app/cbl/COACTUPC.cbl:3757`, `app/cbl/COACTUPC.cbl:3758`, `app/cbl/COACTUPC.cbl:3926`, ...; COACTVWC (2): `app/cbl/COACTVWC.cbl:830`, `app/cbl/COACTVWC.cbl:831`; COPAUA0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:577`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:578`; COPAUS0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:924`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:925` |
| CUST-ID | 5 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:282`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:293`; COACTUPC (2): `app/cbl/COACTUPC.cbl:3806`, `app/cbl/COACTUPC.cbl:3852`; COACTVWC (1): `app/cbl/COACTVWC.cbl:494`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:757` |
| CUST-FIRST-NAME | 6 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:283`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:294`; COACTUPC (3): `app/cbl/COACTUPC.cbl:3807`, `app/cbl/COACTUPC.cbl:3863`, `app/cbl/COACTUPC.cbl:4152`; COACTVWC (1): `app/cbl/COACTVWC.cbl:508`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:758` |
| CUST-MIDDLE-NAME | 7 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:284`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:295`; COACTUPC (3): `app/cbl/COACTUPC.cbl:3808`, `app/cbl/COACTUPC.cbl:3865`, `app/cbl/COACTUPC.cbl:4154`; COACTVWC (1): `app/cbl/COACTVWC.cbl:509`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:760` |
| CUST-LAST-NAME | 8 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:285`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:296`; COACTUPC (3): `app/cbl/COACTUPC.cbl:3809`, `app/cbl/COACTUPC.cbl:3867`, `app/cbl/COACTUPC.cbl:4156`; COACTVWC (1): `app/cbl/COACTVWC.cbl:510`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:762` |
| CUST-ADDR-LINE-1 | 9 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:286`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:297`; COACTUPC (2): `app/cbl/COACTUPC.cbl:3869`, `app/cbl/COACTUPC.cbl:4158`; COACTVWC (1): `app/cbl/COACTVWC.cbl:511`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:766` |
| CUST-ADDR-LINE-2 | 10 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:287`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:298`; COACTUPC (2): `app/cbl/COACTUPC.cbl:3870`, `app/cbl/COACTUPC.cbl:4160`; COACTVWC (1): `app/cbl/COACTVWC.cbl:512`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:768` |
| CUST-ADDR-LINE-3 | 11 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:288`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:299`; COACTUPC (2): `app/cbl/COACTUPC.cbl:3871`, `app/cbl/COACTUPC.cbl:4162`; COACTVWC (1): `app/cbl/COACTVWC.cbl:513`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:771` |
| CUST-ADDR-STATE-CD | 12 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:289`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:300`; COACTUPC (2): `app/cbl/COACTUPC.cbl:3872`, `app/cbl/COACTUPC.cbl:4164`; COACTVWC (1): `app/cbl/COACTVWC.cbl:514`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:773` |
| CUST-ADDR-COUNTRY-CD | 13 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:290`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:301`; COACTUPC (2): `app/cbl/COACTUPC.cbl:3873`, `app/cbl/COACTUPC.cbl:4166`; COACTVWC (1): `app/cbl/COACTVWC.cbl:516` |
| CUST-ADDR-ZIP | 14 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:291`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:302`; COACTUPC (2): `app/cbl/COACTUPC.cbl:3875`, `app/cbl/COACTUPC.cbl:4168`; COACTVWC (1): `app/cbl/COACTVWC.cbl:515`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:775` |
| CUST-PHONE-NUM-1 | 15 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:292`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:303`; COACTUPC (2): `app/cbl/COACTUPC.cbl:3876`, `app/cbl/COACTUPC.cbl:4169`; COACTVWC (1): `app/cbl/COACTVWC.cbl:517`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:779` |
| CUST-PHONE-NUM-2 | 16 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:293`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:304`; COACTUPC (2): `app/cbl/COACTUPC.cbl:3877`, `app/cbl/COACTUPC.cbl:4170`; COACTVWC (1): `app/cbl/COACTVWC.cbl:518` |
| CUST-SSN | 17 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:294`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:305`; COACTUPC (2): `app/cbl/COACTUPC.cbl:3854`, `app/cbl/COACTUPC.cbl:4171`; COACTVWC (3): `app/cbl/COACTVWC.cbl:497`, `app/cbl/COACTVWC.cbl:499`, `app/cbl/COACTVWC.cbl:501` |
| CUST-GOVT-ISSUED-ID | 18 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:295`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:306`; COACTUPC (2): `app/cbl/COACTUPC.cbl:3879`, `app/cbl/COACTUPC.cbl:4172`; COACTVWC (1): `app/cbl/COACTVWC.cbl:519` |
| CUST-DOB-YYYY-MM-DD | 19 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:296`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:307`; COACTUPC (6): `app/cbl/COACTUPC.cbl:3857`, `app/cbl/COACTUPC.cbl:3858`, `app/cbl/COACTUPC.cbl:3859`, ...; COACTVWC (1): `app/cbl/COACTVWC.cbl:507` |
| CUST-EFT-ACCOUNT-ID | 20 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:297`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:308`; COACTUPC (2): `app/cbl/COACTUPC.cbl:3881`, `app/cbl/COACTUPC.cbl:4181`; COACTVWC (1): `app/cbl/COACTVWC.cbl:520` |
| CUST-PRI-CARD-HOLDER-IND | 21 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:298`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:309`; COACTUPC (2): `app/cbl/COACTUPC.cbl:3883`, `app/cbl/COACTUPC.cbl:4183`; COACTVWC (1): `app/cbl/COACTVWC.cbl:521` |
| CUST-FICO-CREDIT-SCORE | 22 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:299`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:310`; COACTUPC (2): `app/cbl/COACTUPC.cbl:3861`, `app/cbl/COACTUPC.cbl:4186`; COACTVWC (1): `app/cbl/COACTVWC.cbl:505` |

## Key fields

| Field | Meaning | Source |
|---|---|---|
| CUSTOMER-RECORD | 500-byte customer master record (comment RECLN 500; field sizes add up to 500). | `app/cpy/CVCUS01Y.cpy:4` |
| CUST-ID | 9-digit customer id, key of the customer file. | `app/cpy/CVCUS01Y.cpy:5` |
| CUST-LAST-NAME | Customer last name (with CUST-FIRST-NAME and CUST-MIDDLE-NAME, 25 bytes each). | `app/cpy/CVCUS01Y.cpy:6-8` |
| CUST-ADDR-ZIP | ZIP code; together with three address lines, state and country codes forms the postal address. | `app/cpy/CVCUS01Y.cpy:9-14` |
| CUST-SSN | 9-digit social security number (sensitive). | `app/cpy/CVCUS01Y.cpy:17` |
| CUST-GOVT-ISSUED-ID | Government-issued id (sensitive). | `app/cpy/CVCUS01Y.cpy:18` |
| CUST-DOB-YYYY-MM-DD | Date of birth in YYYY-MM-DD text form. | `app/cpy/CVCUS01Y.cpy:19` |
| CUST-PRI-CARD-HOLDER-IND | Primary card holder indicator (1 byte, no 88-levels). | `app/cpy/CVCUS01Y.cpy:21` |
| CUST-FICO-CREDIT-SCORE | 3-digit FICO credit score. | `app/cpy/CVCUS01Y.cpy:22` |

## Observations

- conflict: CUSTREC defines the same layout under the same 01 name but calls the birth-date field CUST-DOB-YYYYMMDD; the two copybooks are near-duplicates. (`app/cpy/CVCUS01Y.cpy:19`)

## Sources

- `app/cpy/CVCUS01Y.cpy`
- `docs/_work/structure/copybooks/CVCUS01Y.json`
- `docs/_work/layouts/CVCUS01Y.json`
- `docs/_work/semantic/copybooks/CVCUS01Y.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
