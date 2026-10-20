# Layout CVEXPORT

| Item | Value |
|---|---|
| Source | `app/cpy/CVEXPORT.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 103 |
| Data items | 72 (88-levels: 0) |
| Semantic analysis | validated (batch B02) |

## Purpose

CVEXPORT defines EXPORT-RECORD, the 500-byte multi-record layout of the branch-migration export file. A common header (record type, timestamp, sequence number, branch and region) is followed by a 460-byte data area redefined for customer, account, transaction, card cross-reference and card records, with many numeric fields packed into COMP or COMP-3. It is written by CBEXPORT and read by CBIMPORT, which splits it back into the standard master layouts. (Confirmed)

Evidence: `app/cpy/CVEXPORT.cpy:1-19`, `app/cpy/CVEXPORT.cpy:24-100`, `app/cbl/CBEXPORT.cbl:273-279`, `app/cbl/CBIMPORT.cbl:272-284`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | EXPORT-RECORD |  |  | 1 | 500 | 500 |  |  |  | 9 |
| 05 | &nbsp;&nbsp;EXPORT-REC-TYPE | X(1) | DISPLAY | 1 | 1 | 1 |  |  |  | 10 |
| 05 | &nbsp;&nbsp;EXPORT-TIMESTAMP | X(26) | DISPLAY | 2 | 27 | 26 |  |  |  | 11 |
| 05 | &nbsp;&nbsp;EXPORT-TIMESTAMP-R |  |  | 2 | 27 | 26 |  | EXPORT-TIMESTAMP |  | 12 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXPORT-DATE | X(10) | DISPLAY | 2 | 11 | 10 |  |  |  | 13 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXPORT-DATE-TIME-SEP | X(1) | DISPLAY | 12 | 12 | 1 |  |  |  | 14 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXPORT-TIME | X(15) | DISPLAY | 13 | 27 | 15 |  |  |  | 15 |
| 05 | &nbsp;&nbsp;EXPORT-SEQUENCE-NUM | 9(9) | COMP | 28 | 31 | 4 |  |  |  | 16 |
| 05 | &nbsp;&nbsp;EXPORT-BRANCH-ID | X(4) | DISPLAY | 32 | 35 | 4 |  |  |  | 17 |
| 05 | &nbsp;&nbsp;EXPORT-REGION-CODE | X(5) | DISPLAY | 36 | 40 | 5 |  |  |  | 18 |
| 05 | &nbsp;&nbsp;EXPORT-RECORD-DATA | X(460) | DISPLAY | 41 | 500 | 460 |  |  |  | 19 |
| 05 | &nbsp;&nbsp;EXPORT-CUSTOMER-DATA |  |  | 41 | 500 | 460 |  | EXPORT-RECORD-DATA |  | 24 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-ID | 9(09) | COMP | 41 | 44 | 4 |  |  |  | 25 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-FIRST-NAME | X(25) | DISPLAY | 45 | 69 | 25 |  |  |  | 26 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-MIDDLE-NAME | X(25) | DISPLAY | 70 | 94 | 25 |  |  |  | 27 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-LAST-NAME | X(25) | DISPLAY | 95 | 119 | 25 |  |  |  | 28 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-ADDR-LINES |  |  | 120 | 269 | 150 | 3 |  |  | 29 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-ADDR-LINE | X(50) | DISPLAY | 120 | 169 | 50 |  |  |  | 30 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-ADDR-STATE-CD | X(02) | DISPLAY | 270 | 271 | 2 |  |  |  | 31 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-ADDR-COUNTRY-CD | X(03) | DISPLAY | 272 | 274 | 3 |  |  |  | 32 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-ADDR-ZIP | X(10) | DISPLAY | 275 | 284 | 10 |  |  |  | 33 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-PHONE-NUMS |  |  | 285 | 314 | 30 | 2 |  |  | 34 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-PHONE-NUM | X(15) | DISPLAY | 285 | 299 | 15 |  |  |  | 35 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-SSN | 9(09) | DISPLAY | 315 | 323 | 9 |  |  |  | 36 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-GOVT-ISSUED-ID | X(20) | DISPLAY | 324 | 343 | 20 |  |  |  | 37 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-DOB-YYYY-MM-DD | X(10) | DISPLAY | 344 | 353 | 10 |  |  |  | 38 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-EFT-ACCOUNT-ID | X(10) | DISPLAY | 354 | 363 | 10 |  |  |  | 39 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-PRI-CARD-HOLDER-IND | X(01) | DISPLAY | 364 | 364 | 1 |  |  |  | 40 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CUST-FICO-CREDIT-SCORE | 9(03) | COMP-3 | 365 | 366 | 2 |  |  |  | 41 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(134) | DISPLAY | 367 | 500 | 134 |  |  |  | 42 |
| 05 | &nbsp;&nbsp;EXPORT-ACCOUNT-DATA |  |  | 41 | 500 | 460 |  | EXPORT-RECORD-DATA |  | 47 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-ACCT-ID | 9(11) | DISPLAY | 41 | 51 | 11 |  |  |  | 48 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-ACCT-ACTIVE-STATUS | X(01) | DISPLAY | 52 | 52 | 1 |  |  |  | 49 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-ACCT-CURR-BAL | S9(10)V99 | COMP-3 | 53 | 59 | 7 |  |  |  | 50 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-ACCT-CREDIT-LIMIT | S9(10)V99 | DISPLAY | 60 | 71 | 12 |  |  |  | 51 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-ACCT-CASH-CREDIT-LIMIT | S9(10)V99 | COMP-3 | 72 | 78 | 7 |  |  |  | 52 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-ACCT-OPEN-DATE | X(10) | DISPLAY | 79 | 88 | 10 |  |  |  | 53 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-ACCT-EXPIRAION-DATE | X(10) | DISPLAY | 89 | 98 | 10 |  |  |  | 54 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-ACCT-REISSUE-DATE | X(10) | DISPLAY | 99 | 108 | 10 |  |  |  | 55 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-ACCT-CURR-CYC-CREDIT | S9(10)V99 | DISPLAY | 109 | 120 | 12 |  |  |  | 56 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-ACCT-CURR-CYC-DEBIT | S9(10)V99 | COMP | 121 | 128 | 8 |  |  |  | 57 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-ACCT-ADDR-ZIP | X(10) | DISPLAY | 129 | 138 | 10 |  |  |  | 58 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-ACCT-GROUP-ID | X(10) | DISPLAY | 139 | 148 | 10 |  |  |  | 59 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(352) | DISPLAY | 149 | 500 | 352 |  |  |  | 60 |
| 05 | &nbsp;&nbsp;EXPORT-TRANSACTION-DATA |  |  | 41 | 500 | 460 |  | EXPORT-RECORD-DATA |  | 65 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-TRAN-ID | X(16) | DISPLAY | 41 | 56 | 16 |  |  |  | 66 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-TRAN-TYPE-CD | X(02) | DISPLAY | 57 | 58 | 2 |  |  |  | 67 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-TRAN-CAT-CD | 9(04) | DISPLAY | 59 | 62 | 4 |  |  |  | 68 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-TRAN-SOURCE | X(10) | DISPLAY | 63 | 72 | 10 |  |  |  | 69 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-TRAN-DESC | X(100) | DISPLAY | 73 | 172 | 100 |  |  |  | 70 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-TRAN-AMT | S9(09)V99 | COMP-3 | 173 | 178 | 6 |  |  |  | 71 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-TRAN-MERCHANT-ID | 9(09) | COMP | 179 | 182 | 4 |  |  |  | 72 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-TRAN-MERCHANT-NAME | X(50) | DISPLAY | 183 | 232 | 50 |  |  |  | 73 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-TRAN-MERCHANT-CITY | X(50) | DISPLAY | 233 | 282 | 50 |  |  |  | 74 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-TRAN-MERCHANT-ZIP | X(10) | DISPLAY | 283 | 292 | 10 |  |  |  | 75 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-TRAN-CARD-NUM | X(16) | DISPLAY | 293 | 308 | 16 |  |  |  | 76 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-TRAN-ORIG-TS | X(26) | DISPLAY | 309 | 334 | 26 |  |  |  | 77 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-TRAN-PROC-TS | X(26) | DISPLAY | 335 | 360 | 26 |  |  |  | 78 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(140) | DISPLAY | 361 | 500 | 140 |  |  |  | 79 |
| 05 | &nbsp;&nbsp;EXPORT-CARD-XREF-DATA |  |  | 41 | 500 | 460 |  | EXPORT-RECORD-DATA |  | 84 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-XREF-CARD-NUM | X(16) | DISPLAY | 41 | 56 | 16 |  |  |  | 85 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-XREF-CUST-ID | 9(09) | DISPLAY | 57 | 65 | 9 |  |  |  | 86 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-XREF-ACCT-ID | 9(11) | COMP | 66 | 73 | 8 |  |  |  | 87 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(427) | DISPLAY | 74 | 500 | 427 |  |  |  | 88 |
| 05 | &nbsp;&nbsp;EXPORT-CARD-DATA |  |  | 41 | 500 | 460 |  | EXPORT-RECORD-DATA |  | 93 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CARD-NUM | X(16) | DISPLAY | 41 | 56 | 16 |  |  |  | 94 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CARD-ACCT-ID | 9(11) | COMP | 57 | 64 | 8 |  |  |  | 95 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CARD-CVV-CD | 9(03) | COMP | 65 | 66 | 2 |  |  |  | 96 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CARD-EMBOSSED-NAME | X(50) | DISPLAY | 67 | 116 | 50 |  |  |  | 97 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CARD-EXPIRAION-DATE | X(10) | DISPLAY | 117 | 126 | 10 |  |  |  | 98 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;EXP-CARD-ACTIVE-STATUS | X(01) | DISPLAY | 127 | 127 | 1 |  |  |  | 99 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(373) | DISPLAY | 128 | 500 | 373 |  |  |  | 100 |

## Level-88 conditions

None.

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [CBEXPORT](../../07-programs/CBEXPORT.md) | cobol-program | COPY | active |  | `app/cbl/CBEXPORT.cbl:96` |
| [CBIMPORT](../../07-programs/CBIMPORT.md) | cobol-program | COPY | active |  | `app/cbl/CBIMPORT.cbl:113` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| EXPORT-RECORD | 9 | CBEXPORT (10): `app/cbl/CBEXPORT.cbl:271`, `app/cbl/CBEXPORT.cbl:301`, `app/cbl/CBEXPORT.cbl:340`, ...; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:261` |
| EXPORT-REC-TYPE | 10 | CBEXPORT (5): `app/cbl/CBEXPORT.cbl:274`, `app/cbl/CBEXPORT.cbl:343`, `app/cbl/CBEXPORT.cbl:407`, ...; CBIMPORT (2): `app/cbl/CBIMPORT.cbl:272`, `app/cbl/CBIMPORT.cbl:430` |
| EXPORT-TIMESTAMP | 11 | CBEXPORT (5): `app/cbl/CBEXPORT.cbl:275`, `app/cbl/CBEXPORT.cbl:344`, `app/cbl/CBEXPORT.cbl:408`, ... |
| EXPORT-SEQUENCE-NUM | 16 | CBEXPORT (5): `app/cbl/CBEXPORT.cbl:277`, `app/cbl/CBEXPORT.cbl:346`, `app/cbl/CBEXPORT.cbl:410`, ...; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:431` |
| EXPORT-BRANCH-ID | 17 | CBEXPORT (5): `app/cbl/CBEXPORT.cbl:278`, `app/cbl/CBEXPORT.cbl:347`, `app/cbl/CBEXPORT.cbl:411`, ... |
| EXPORT-REGION-CODE | 18 | CBEXPORT (5): `app/cbl/CBEXPORT.cbl:279`, `app/cbl/CBEXPORT.cbl:348`, `app/cbl/CBEXPORT.cbl:412`, ... |
| EXP-CUST-ID | 25 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:282`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:293` |
| EXP-CUST-FIRST-NAME | 26 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:283`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:294` |
| EXP-CUST-MIDDLE-NAME | 27 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:284`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:295` |
| EXP-CUST-LAST-NAME | 28 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:285`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:296` |
| EXP-CUST-ADDR-LINE | 30 | CBEXPORT (3): `app/cbl/CBEXPORT.cbl:286`, `app/cbl/CBEXPORT.cbl:287`, `app/cbl/CBEXPORT.cbl:288`; CBIMPORT (3): `app/cbl/CBIMPORT.cbl:297`, `app/cbl/CBIMPORT.cbl:298`, `app/cbl/CBIMPORT.cbl:299` |
| EXP-CUST-ADDR-STATE-CD | 31 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:289`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:300` |
| EXP-CUST-ADDR-COUNTRY-CD | 32 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:290`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:301` |
| EXP-CUST-ADDR-ZIP | 33 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:291`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:302` |
| EXP-CUST-PHONE-NUM | 35 | CBEXPORT (2): `app/cbl/CBEXPORT.cbl:292`, `app/cbl/CBEXPORT.cbl:293`; CBIMPORT (2): `app/cbl/CBIMPORT.cbl:303`, `app/cbl/CBIMPORT.cbl:304` |
| EXP-CUST-SSN | 36 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:294`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:305` |
| EXP-CUST-GOVT-ISSUED-ID | 37 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:295`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:306` |
| EXP-CUST-DOB-YYYY-MM-DD | 38 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:296`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:307` |
| EXP-CUST-EFT-ACCOUNT-ID | 39 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:297`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:308` |
| EXP-CUST-PRI-CARD-HOLDER-IND | 40 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:298`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:309` |
| EXP-CUST-FICO-CREDIT-SCORE | 41 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:299`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:310` |
| EXP-ACCT-ID | 48 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:351`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:328` |
| EXP-ACCT-ACTIVE-STATUS | 49 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:352`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:329` |
| EXP-ACCT-CURR-BAL | 50 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:353`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:330` |
| EXP-ACCT-CREDIT-LIMIT | 51 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:354`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:331` |
| EXP-ACCT-CASH-CREDIT-LIMIT | 52 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:355`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:332` |
| EXP-ACCT-OPEN-DATE | 53 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:356`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:333` |
| EXP-ACCT-EXPIRAION-DATE | 54 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:357`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:334` |
| EXP-ACCT-REISSUE-DATE | 55 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:358`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:335` |
| EXP-ACCT-CURR-CYC-CREDIT | 56 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:359`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:336` |
| EXP-ACCT-CURR-CYC-DEBIT | 57 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:360`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:337` |
| EXP-ACCT-ADDR-ZIP | 58 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:361`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:338` |
| EXP-ACCT-GROUP-ID | 59 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:362`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:339` |
| EXP-TRAN-ID | 66 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:470`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:377` |
| EXP-TRAN-TYPE-CD | 67 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:471`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:378` |
| EXP-TRAN-CAT-CD | 68 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:472`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:379` |
| EXP-TRAN-SOURCE | 69 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:473`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:380` |
| EXP-TRAN-DESC | 70 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:474`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:381` |
| EXP-TRAN-AMT | 71 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:475`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:382` |
| EXP-TRAN-MERCHANT-ID | 72 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:476`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:383` |
| EXP-TRAN-MERCHANT-NAME | 73 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:477`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:384` |
| EXP-TRAN-MERCHANT-CITY | 74 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:478`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:385` |
| EXP-TRAN-MERCHANT-ZIP | 75 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:479`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:386` |
| EXP-TRAN-CARD-NUM | 76 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:480`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:387` |
| EXP-TRAN-ORIG-TS | 77 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:481`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:388` |
| EXP-TRAN-PROC-TS | 78 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:482`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:389` |
| EXP-XREF-CARD-NUM | 85 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:415`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:357` |
| EXP-XREF-CUST-ID | 86 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:416`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:358` |
| EXP-XREF-ACCT-ID | 87 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:417`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:359` |
| EXP-CARD-NUM | 94 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:535`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:407` |
| EXP-CARD-ACCT-ID | 95 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:536`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:408` |
| EXP-CARD-CVV-CD | 96 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:537`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:409` |
| EXP-CARD-EMBOSSED-NAME | 97 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:538`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:410` |
| EXP-CARD-EXPIRAION-DATE | 98 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:539`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:411` |
| EXP-CARD-ACTIVE-STATUS | 99 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:540`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:412` |

Named in no procedure statement of the copying programs (may still be moved as part of a group): EXPORT-TIMESTAMP-R (line 12), EXPORT-DATE (line 13), EXPORT-DATE-TIME-SEP (line 14), EXPORT-TIME (line 15), EXPORT-RECORD-DATA (line 19), EXPORT-CUSTOMER-DATA (line 24), EXP-CUST-ADDR-LINES (line 29), EXP-CUST-PHONE-NUMS (line 34), EXPORT-ACCOUNT-DATA (line 47), EXPORT-TRANSACTION-DATA (line 65), EXPORT-CARD-XREF-DATA (line 84), EXPORT-CARD-DATA (line 93).

## Key fields

| Field | Meaning | Source |
|---|---|---|
| EXPORT-RECORD | 500-byte multi-record export layout: 40-byte common header plus 460-byte data area (sizes verified: 1+26+4+4+5+460). | `app/cpy/CVEXPORT.cpy:9-19` |
| EXPORT-REC-TYPE | Record type code set by CBEXPORT and routed by CBIMPORT: 'C' customer, 'A' account, 'X' card xref, 'T' transaction, 'D' card (values are in the programs, not in 88-levels here). | `app/cpy/CVEXPORT.cpy:10` |
| EXPORT-TIMESTAMP | 26-byte export run timestamp, redefined as date, separator and time. | `app/cpy/CVEXPORT.cpy:11-15` |
| EXPORT-SEQUENCE-NUM | Binary (COMP) sequence number across all record types; declared as the record key of EXPFILE in CBEXPORT/CBIMPORT. | `app/cpy/CVEXPORT.cpy:16` |
| EXPORT-BRANCH-ID | 4-byte branch id (CBEXPORT always sets '0001'). | `app/cpy/CVEXPORT.cpy:17` |
| EXPORT-REGION-CODE | 5-byte region code (CBEXPORT always sets 'NORTH'). | `app/cpy/CVEXPORT.cpy:18` |
| EXPORT-CUSTOMER-DATA | Customer view of the data area (from CVCUS01Y) with address lines and phones as OCCURS arrays, CUST-ID as COMP and FICO score as COMP-3. | `app/cpy/CVEXPORT.cpy:24-42` |
| EXPORT-ACCOUNT-DATA | Account view (from CVACT01Y); balance and cash limit COMP-3, cycle debit COMP, others display. | `app/cpy/CVEXPORT.cpy:47-60` |
| EXPORT-TRANSACTION-DATA | Transaction view (from CVTRA05Y); amount COMP-3, merchant id COMP. | `app/cpy/CVEXPORT.cpy:65-79` |
| EXPORT-CARD-XREF-DATA | Card cross-reference view (from CVACT03Y); account id COMP. | `app/cpy/CVEXPORT.cpy:84-88` |
| EXPORT-CARD-DATA | Card view (from CVACT02Y); account id and CVV as COMP. | `app/cpy/CVEXPORT.cpy:93-100` |

## Observations

- anomaly: Numeric storage is mixed inconsistently within one view: in EXPORT-ACCOUNT-DATA the balance and cash limit are COMP-3, the credit limit and cycle credit stay display, and the cycle debit is binary COMP. Any non-COBOL consumer must handle three numeric encodings. (`app/cpy/CVEXPORT.cpy:50-57`)
- security: The customer and card views carry SSN, government id and CVV without masking. (`app/cpy/CVEXPORT.cpy:36-37`)

## Sources

- `app/cpy/CVEXPORT.cpy`
- `docs/_work/structure/copybooks/CVEXPORT.json`
- `docs/_work/layouts/CVEXPORT.json`
- `docs/_work/semantic/copybooks/CVEXPORT.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
