# Layout CVACT01Y

| Item | Value |
|---|---|
| Source | `app/cpy/CVACT01Y.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 20 |
| Data items | 14 (88-levels: 0) |
| Semantic analysis | validated (batch B02) |

## Purpose

CVACT01Y defines ACCOUNT-RECORD, the 300-byte account master entity of CardDemo: account id, active status, current balance, credit and cash limits, open/expiration/reissue dates, current-cycle credit and debit totals, ZIP and account group id. It is one of the most widely used layouts: batch programs CBACT01C, CBACT04C, CBEXPORT, CBIMPORT, CBSTM03A, CBTRN01C, CBTRN02C and many online programs (COACTUPC, COACTVWC, COBIL00C, COCRDSLC, COCRDUPC, COTRN02C, authorization and VSAM-MQ programs) copy it. (Confirmed)

Evidence: `app/cpy/CVACT01Y.cpy:1-17`, `app/cbl/CBACT04C.cbl:350-356`, `app/cbl/CBACT01C.cbl:52-55`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | ACCOUNT-RECORD |  |  | 1 | 300 | 300 |  |  |  | 4 |
| 05 | &nbsp;&nbsp;ACCT-ID | 9(11) | DISPLAY | 1 | 11 | 11 |  |  |  | 5 |
| 05 | &nbsp;&nbsp;ACCT-ACTIVE-STATUS | X(01) | DISPLAY | 12 | 12 | 1 |  |  |  | 6 |
| 05 | &nbsp;&nbsp;ACCT-CURR-BAL | S9(10)V99 | DISPLAY | 13 | 24 | 12 |  |  |  | 7 |
| 05 | &nbsp;&nbsp;ACCT-CREDIT-LIMIT | S9(10)V99 | DISPLAY | 25 | 36 | 12 |  |  |  | 8 |
| 05 | &nbsp;&nbsp;ACCT-CASH-CREDIT-LIMIT | S9(10)V99 | DISPLAY | 37 | 48 | 12 |  |  |  | 9 |
| 05 | &nbsp;&nbsp;ACCT-OPEN-DATE | X(10) | DISPLAY | 49 | 58 | 10 |  |  |  | 10 |
| 05 | &nbsp;&nbsp;ACCT-EXPIRAION-DATE | X(10) | DISPLAY | 59 | 68 | 10 |  |  |  | 11 |
| 05 | &nbsp;&nbsp;ACCT-REISSUE-DATE | X(10) | DISPLAY | 69 | 78 | 10 |  |  |  | 12 |
| 05 | &nbsp;&nbsp;ACCT-CURR-CYC-CREDIT | S9(10)V99 | DISPLAY | 79 | 90 | 12 |  |  |  | 13 |
| 05 | &nbsp;&nbsp;ACCT-CURR-CYC-DEBIT | S9(10)V99 | DISPLAY | 91 | 102 | 12 |  |  |  | 14 |
| 05 | &nbsp;&nbsp;ACCT-ADDR-ZIP | X(10) | DISPLAY | 103 | 112 | 10 |  |  |  | 15 |
| 05 | &nbsp;&nbsp;ACCT-GROUP-ID | X(10) | DISPLAY | 113 | 122 | 10 |  |  |  | 16 |
| 05 | &nbsp;&nbsp;FILLER | X(178) | DISPLAY | 123 | 300 | 178 |  |  |  | 17 |

## Level-88 conditions

None.

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [COPAUA0C](../../07-programs/COPAUA0C.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:206` |
| [COPAUS0C](../../07-programs/COPAUS0C.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:144` |
| [COACCT01](../../07-programs/COACCT01.md) | cobol-program | COPY | active |  | `app/app-vsam-mq/cbl/COACCT01.cbl:171` |
| [CBACT01C](../../07-programs/CBACT01C.md) | cobol-program | COPY | active |  | `app/cbl/CBACT01C.cbl:89` |
| [CBACT04C](../../07-programs/CBACT04C.md) | cobol-program | COPY | active |  | `app/cbl/CBACT04C.cbl:112` |
| [CBEXPORT](../../07-programs/CBEXPORT.md) | cobol-program | COPY | active |  | `app/cbl/CBEXPORT.cbl:78` |
| [CBIMPORT](../../07-programs/CBIMPORT.md) | cobol-program | COPY | active |  | `app/cbl/CBIMPORT.cbl:89` |
| [CBSTM03A](../../07-programs/CBSTM03A.md) | cobol-program | COPY | active |  | `app/cbl/CBSTM03A.CBL:57` |
| [CBTRN01C](../../07-programs/CBTRN01C.md) | cobol-program | COPY | active |  | `app/cbl/CBTRN01C.cbl:119` |
| [CBTRN02C](../../07-programs/CBTRN02C.md) | cobol-program | COPY | active |  | `app/cbl/CBTRN02C.cbl:121` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active |  | `app/cbl/COACTUPC.cbl:640` |
| [COACTVWC](../../07-programs/COACTVWC.md) | cobol-program | COPY | active |  | `app/cbl/COACTVWC.cbl:244` |
| [COBIL00C](../../07-programs/COBIL00C.md) | cobol-program | COPY | active |  | `app/cbl/COBIL00C.cbl:80` |
| [COCRDSLC](../../07-programs/COCRDSLC.md) | cobol-program | COPY | commented out |  | `app/cbl/COCRDSLC.cbl:231` |
| [COCRDUPC](../../07-programs/COCRDUPC.md) | cobol-program | COPY | commented out |  | `app/cbl/COCRDUPC.cbl:350` |
| [COTRN02C](../../07-programs/COTRN02C.md) | cobol-program | COPY | active |  | `app/cbl/COTRN02C.cbl:89` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| ACCOUNT-RECORD | 4 | CBACT01C (2): `app/cbl/CBACT01C.cbl:151`, `app/cbl/CBACT01C.cbl:166`; CBACT04C (2): `app/cbl/CBACT04C.cbl:356`, `app/cbl/CBACT04C.cbl:373`; CBIMPORT (2): `app/cbl/CBIMPORT.cbl:325`, `app/cbl/CBIMPORT.cbl:341`; CBSTM03A (1): `app/cbl/CBSTM03A.CBL:412`; CBTRN01C (1): `app/cbl/CBTRN01C.cbl:243`; CBTRN02C (2): `app/cbl/CBTRN02C.cbl:395`, `app/cbl/CBTRN02C.cbl:554`; COACCT01 (2): `app/app-vsam-mq/cbl/COACCT01.cbl:400`, `app/app-vsam-mq/cbl/COACCT01.cbl:401`; COACTUPC (4): `app/cbl/COACTUPC.cbl:3707`, `app/cbl/COACTUPC.cbl:3708`, `app/cbl/COACTUPC.cbl:3899`, ...; COACTVWC (2): `app/cbl/COACTVWC.cbl:780`, `app/cbl/COACTVWC.cbl:781`; COBIL00C (4): `app/cbl/COBIL00C.cbl:347`, `app/cbl/COBIL00C.cbl:348`, `app/cbl/COBIL00C.cbl:381`, ...; COPAUA0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:529`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:530`; COPAUS0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:873`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:874` |
| ACCT-ID | 5 | CBACT01C (4): `app/cbl/CBACT01C.cbl:201`, `app/cbl/CBACT01C.cbl:216`, `app/cbl/CBACT01C.cbl:254`, ...; CBACT04C (1): `app/cbl/CBACT04C.cbl:486`; CBEXPORT (1): `app/cbl/CBEXPORT.cbl:351`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:328`; CBSTM03A (2): `app/cbl/CBSTM03A.CBL:483`, `app/cbl/CBSTM03A.CBL:529`; CBTRN01C (3): `app/cbl/CBTRN01C.cbl:175`, `app/cbl/CBTRN01C.cbl:178`, `app/cbl/CBTRN01C.cbl:242`; COACCT01 (1): `app/app-vsam-mq/cbl/COACCT01.cbl:408`; COACTUPC (2): `app/cbl/COACTUPC.cbl:3805`, `app/cbl/COACTUPC.cbl:3817`; COBIL00C (3): `app/cbl/COBIL00C.cbl:170`, `app/cbl/COBIL00C.cbl:349`, `app/cbl/COBIL00C.cbl:350` |
| ACCT-ACTIVE-STATUS | 6 | CBACT01C (3): `app/cbl/CBACT01C.cbl:202`, `app/cbl/CBACT01C.cbl:217`, `app/cbl/CBACT01C.cbl:279`; CBEXPORT (1): `app/cbl/CBEXPORT.cbl:352`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:329`; COACCT01 (1): `app/app-vsam-mq/cbl/COACCT01.cbl:409`; COACTUPC (3): `app/cbl/COACTUPC.cbl:3810`, `app/cbl/COACTUPC.cbl:3819`, `app/cbl/COACTUPC.cbl:4115`; COACTVWC (1): `app/cbl/COACTVWC.cbl:473` |
| ACCT-CURR-BAL | 7 | CBACT01C (5): `app/cbl/CBACT01C.cbl:203`, `app/cbl/CBACT01C.cbl:218`, `app/cbl/CBACT01C.cbl:255`, ...; CBACT04C (1): `app/cbl/CBACT04C.cbl:352`; CBEXPORT (1): `app/cbl/CBEXPORT.cbl:353`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:330`; CBSTM03A (1): `app/cbl/CBSTM03A.CBL:484`; CBTRN02C (1): `app/cbl/CBTRN02C.cbl:547`; COACCT01 (1): `app/app-vsam-mq/cbl/COACCT01.cbl:411`; COACTUPC (2): `app/cbl/COACTUPC.cbl:3821`, `app/cbl/COACTUPC.cbl:4117`; COACTVWC (1): `app/cbl/COACTVWC.cbl:475`; COBIL00C (4): `app/cbl/COBIL00C.cbl:193`, `app/cbl/COBIL00C.cbl:198`, `app/cbl/COBIL00C.cbl:224`, ...; COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:675` |
| ACCT-CREDIT-LIMIT | 8 | CBACT01C (3): `app/cbl/CBACT01C.cbl:204`, `app/cbl/CBACT01C.cbl:219`, `app/cbl/CBACT01C.cbl:281`; CBEXPORT (1): `app/cbl/CBEXPORT.cbl:354`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:331`; CBTRN02C (1): `app/cbl/CBTRN02C.cbl:407`; COACCT01 (1): `app/app-vsam-mq/cbl/COACCT01.cbl:412`; COACTUPC (2): `app/cbl/COACTUPC.cbl:3823`, `app/cbl/COACTUPC.cbl:4119`; COACTVWC (1): `app/cbl/COACTVWC.cbl:477`; COPAUA0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:674`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:810`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:780` |
| ACCT-CASH-CREDIT-LIMIT | 9 | CBACT01C (2): `app/cbl/CBACT01C.cbl:205`, `app/cbl/CBACT01C.cbl:220`; CBEXPORT (1): `app/cbl/CBEXPORT.cbl:355`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:332`; COACCT01 (1): `app/app-vsam-mq/cbl/COACCT01.cbl:414`; COACTUPC (2): `app/cbl/COACTUPC.cbl:3825`, `app/cbl/COACTUPC.cbl:4121`; COACTVWC (1): `app/cbl/COACTVWC.cbl:479`; COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:811`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:782` |
| ACCT-OPEN-DATE | 10 | CBACT01C (2): `app/cbl/CBACT01C.cbl:206`, `app/cbl/CBACT01C.cbl:221`; CBEXPORT (1): `app/cbl/CBEXPORT.cbl:356`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:333`; COACCT01 (1): `app/app-vsam-mq/cbl/COACCT01.cbl:416`; COACTUPC (6): `app/cbl/COACTUPC.cbl:3832`, `app/cbl/COACTUPC.cbl:3833`, `app/cbl/COACTUPC.cbl:3834`, ...; COACTVWC (1): `app/cbl/COACTVWC.cbl:487` |
| ACCT-EXPIRAION-DATE | 11 | CBACT01C (2): `app/cbl/CBACT01C.cbl:207`, `app/cbl/CBACT01C.cbl:222`; CBEXPORT (1): `app/cbl/CBEXPORT.cbl:357`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:334`; CBTRN02C (1): `app/cbl/CBTRN02C.cbl:414`; COACCT01 (1): `app/app-vsam-mq/cbl/COACCT01.cbl:417`; COACTUPC (6): `app/cbl/COACTUPC.cbl:3837`, `app/cbl/COACTUPC.cbl:3838`, `app/cbl/COACTUPC.cbl:3839`, ...; COACTVWC (1): `app/cbl/COACTVWC.cbl:488` |
| ACCT-REISSUE-DATE | 12 | CBACT01C (2): `app/cbl/CBACT01C.cbl:208`, `app/cbl/CBACT01C.cbl:223`; CBEXPORT (1): `app/cbl/CBEXPORT.cbl:358`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:335`; COACCT01 (1): `app/app-vsam-mq/cbl/COACCT01.cbl:419`; COACTUPC (7): `app/cbl/COACTUPC.cbl:3843`, `app/cbl/COACTUPC.cbl:3844`, `app/cbl/COACTUPC.cbl:3845`, ...; COACTVWC (1): `app/cbl/COACTVWC.cbl:489` |
| ACCT-CURR-CYC-CREDIT | 13 | CBACT01C (2): `app/cbl/CBACT01C.cbl:209`, `app/cbl/CBACT01C.cbl:235`; CBACT04C (1): `app/cbl/CBACT04C.cbl:353`; CBEXPORT (1): `app/cbl/CBEXPORT.cbl:359`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:336`; CBTRN02C (2): `app/cbl/CBTRN02C.cbl:403`, `app/cbl/CBTRN02C.cbl:549`; COACCT01 (1): `app/app-vsam-mq/cbl/COACCT01.cbl:421`; COACTUPC (2): `app/cbl/COACTUPC.cbl:3827`, `app/cbl/COACTUPC.cbl:4123`; COACTVWC (1): `app/cbl/COACTVWC.cbl:482` |
| ACCT-CURR-CYC-DEBIT | 14 | CBACT01C (2): `app/cbl/CBACT01C.cbl:210`, `app/cbl/CBACT01C.cbl:236`; CBACT04C (1): `app/cbl/CBACT04C.cbl:354`; CBEXPORT (1): `app/cbl/CBEXPORT.cbl:360`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:337`; CBTRN02C (2): `app/cbl/CBTRN02C.cbl:404`, `app/cbl/CBTRN02C.cbl:551`; COACCT01 (1): `app/app-vsam-mq/cbl/COACCT01.cbl:423`; COACTUPC (2): `app/cbl/COACTUPC.cbl:3829`, `app/cbl/COACTUPC.cbl:4125`; COACTVWC (1): `app/cbl/COACTVWC.cbl:485` |
| ACCT-ADDR-ZIP | 15 | CBEXPORT (1): `app/cbl/CBEXPORT.cbl:361`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:338` |
| ACCT-GROUP-ID | 16 | CBACT01C (2): `app/cbl/CBACT01C.cbl:211`, `app/cbl/CBACT01C.cbl:239`; CBACT04C (1): `app/cbl/CBACT04C.cbl:210`; CBEXPORT (1): `app/cbl/CBEXPORT.cbl:362`; CBIMPORT (1): `app/cbl/CBIMPORT.cbl:339`; COACCT01 (1): `app/app-vsam-mq/cbl/COACCT01.cbl:425`; COACTUPC (2): `app/cbl/COACTUPC.cbl:3847`, `app/cbl/COACTUPC.cbl:4139`; COACTVWC (1): `app/cbl/COACTVWC.cbl:490` |

## Key fields

| Field | Meaning | Source |
|---|---|---|
| ACCOUNT-RECORD | 300-byte account master record (comment RECLN 300; field sizes add up to 300). | `app/cpy/CVACT01Y.cpy:4` |
| ACCT-ID | 11-digit account number, key of the account file (FD-ACCT-ID in programs). | `app/cpy/CVACT01Y.cpy:5` |
| ACCT-ACTIVE-STATUS | 1-byte account active status flag; no 88-level values are defined here. | `app/cpy/CVACT01Y.cpy:6` |
| ACCT-CURR-BAL | Signed current balance S9(10)V99; CBACT04C adds monthly interest to it. | `app/cpy/CVACT01Y.cpy:7` |
| ACCT-CREDIT-LIMIT | Signed credit limit S9(10)V99. | `app/cpy/CVACT01Y.cpy:8` |
| ACCT-CASH-CREDIT-LIMIT | Signed cash credit limit S9(10)V99. | `app/cpy/CVACT01Y.cpy:9` |
| ACCT-REISSUE-DATE | 10-byte reissue date; CBACT01C treats it as YYYY-MM-DD when converting with COBDATFT. | `app/cpy/CVACT01Y.cpy:12` |
| ACCT-CURR-CYC-CREDIT | Current-cycle credit total; reset to 0 by CBACT04C at interest posting. | `app/cpy/CVACT01Y.cpy:13` |
| ACCT-CURR-CYC-DEBIT | Current-cycle debit total; reset to 0 by CBACT04C at interest posting. | `app/cpy/CVACT01Y.cpy:14` |
| ACCT-GROUP-ID | Account (disclosure) group id used by CBACT04C as the first part of the DISCGRP key to find the interest rate. | `app/cpy/CVACT01Y.cpy:16` |

## Observations

- anomaly: The expiration date field is misspelled ACCT-EXPIRAION-DATE; the misspelling propagates to programs and to CVEXPORT (EXP-ACCT-EXPIRAION-DATE). (`app/cpy/CVACT01Y.cpy:11`)
- anomaly: Dates (open, expiration, reissue) are stored as 10-byte character fields with no format definition; their YYYY-MM-DD format is only implied by callers. (`app/cpy/CVACT01Y.cpy:10-12`)

## Sources

- `app/cpy/CVACT01Y.cpy`
- `docs/_work/structure/copybooks/CVACT01Y.json`
- `docs/_work/layouts/CVACT01Y.json`
- `docs/_work/semantic/copybooks/CVACT01Y.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
