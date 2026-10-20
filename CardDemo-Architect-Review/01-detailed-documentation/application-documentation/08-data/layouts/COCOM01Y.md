# Layout COCOM01Y

| Item | Value |
|---|---|
| Source | `app/cpy/COCOM01Y.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 47 |
| Data items | 22 (88-levels: 4) |
| Semantic analysis | validated (batch B04) |

## Purpose

Defines CARDDEMO-COMMAREA, the communication area shared by the CardDemo CICS programs: routing fields (from/to transaction and program), signed-on user id and type, program entry context, current customer, account and card, and the last map and mapset sent. COACTUPC restores it from DFHCOMMAREA, uses it to decide first entry and PF3 routing, updates the customer/account/card context after a fetch and returns it on every EXEC CICS RETURN. (Confirmed)

Evidence: `app/cpy/COCOM01Y.cpy:19-44`, `app/cbl/COACTUPC.cbl:880-892`, `app/cbl/COACTUPC.cbl:1007-1019`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | CARDDEMO-COMMAREA |  |  | 1 | 160 | 160 |  |  |  | 19 |
| 05 | &nbsp;&nbsp;CDEMO-GENERAL-INFO |  |  | 1 | 34 | 34 |  |  |  | 20 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-FROM-TRANID | X(04) | DISPLAY | 1 | 4 | 4 |  |  |  | 21 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-FROM-PROGRAM | X(08) | DISPLAY | 5 | 12 | 8 |  |  |  | 22 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-TO-TRANID | X(04) | DISPLAY | 13 | 16 | 4 |  |  |  | 23 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-TO-PROGRAM | X(08) | DISPLAY | 17 | 24 | 8 |  |  |  | 24 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-USER-ID | X(08) | DISPLAY | 25 | 32 | 8 |  |  |  | 25 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-USER-TYPE | X(01) | DISPLAY | 33 | 33 | 1 |  |  |  | 26 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-PGM-CONTEXT | 9(01) | DISPLAY | 34 | 34 | 1 |  |  |  | 29 |
| 05 | &nbsp;&nbsp;CDEMO-CUSTOMER-INFO |  |  | 35 | 118 | 84 |  |  |  | 32 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-CUST-ID | 9(09) | DISPLAY | 35 | 43 | 9 |  |  |  | 33 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-CUST-FNAME | X(25) | DISPLAY | 44 | 68 | 25 |  |  |  | 34 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-CUST-MNAME | X(25) | DISPLAY | 69 | 93 | 25 |  |  |  | 35 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-CUST-LNAME | X(25) | DISPLAY | 94 | 118 | 25 |  |  |  | 36 |
| 05 | &nbsp;&nbsp;CDEMO-ACCOUNT-INFO |  |  | 119 | 130 | 12 |  |  |  | 37 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-ACCT-ID | 9(11) | DISPLAY | 119 | 129 | 11 |  |  |  | 38 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-ACCT-STATUS | X(01) | DISPLAY | 130 | 130 | 1 |  |  |  | 39 |
| 05 | &nbsp;&nbsp;CDEMO-CARD-INFO |  |  | 131 | 146 | 16 |  |  |  | 40 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-CARD-NUM | 9(16) | DISPLAY | 131 | 146 | 16 |  |  |  | 41 |
| 05 | &nbsp;&nbsp;CDEMO-MORE-INFO |  |  | 147 | 160 | 14 |  |  |  | 42 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-LAST-MAP | X(7) | DISPLAY | 147 | 153 | 7 |  |  |  | 43 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CDEMO-LAST-MAPSET | X(7) | DISPLAY | 154 | 160 | 7 |  |  |  | 44 |

## Level-88 conditions

| Field | Condition | Values | Line |
|---|---|---|---|
| CDEMO-USER-TYPE | CDEMO-USRTYP-ADMIN | 'A' | 27 |
| CDEMO-USER-TYPE | CDEMO-USRTYP-USER | 'U' | 28 |
| CDEMO-PGM-CONTEXT | CDEMO-PGM-ENTER | 0 | 30 |
| CDEMO-PGM-CONTEXT | CDEMO-PGM-REENTER | 1 | 31 |

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [COPAUS0C](../../07-programs/COPAUS0C.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:116` |
| [COPAUS1C](../../07-programs/COPAUS1C.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:109` |
| [COTRTLIC](../../07-programs/COTRTLIC.md) | cobol-program | COPY | active |  | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:375` |
| [COTRTUPC](../../07-programs/COTRTUPC.md) | cobol-program | COPY | active |  | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:292` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active |  | `app/cbl/COACTUPC.cbl:650` |
| [COACTVWC](../../07-programs/COACTVWC.md) | cobol-program | COPY | active |  | `app/cbl/COACTVWC.cbl:211` |
| [COADM01C](../../07-programs/COADM01C.md) | cobol-program | COPY | active |  | `app/cbl/COADM01C.cbl:50` |
| [COBIL00C](../../07-programs/COBIL00C.md) | cobol-program | COPY | active |  | `app/cbl/COBIL00C.cbl:63` |
| [COCRDLIC](../../07-programs/COCRDLIC.md) | cobol-program | COPY | active |  | `app/cbl/COCRDLIC.cbl:227` |
| [COCRDSLC](../../07-programs/COCRDSLC.md) | cobol-program | COPY | active |  | `app/cbl/COCRDSLC.cbl:198` |
| [COCRDUPC](../../07-programs/COCRDUPC.md) | cobol-program | COPY | active |  | `app/cbl/COCRDUPC.cbl:272` |
| [COMEN01C](../../07-programs/COMEN01C.md) | cobol-program | COPY | active |  | `app/cbl/COMEN01C.cbl:50` |
| [CORPT00C](../../07-programs/CORPT00C.md) | cobol-program | COPY | active |  | `app/cbl/CORPT00C.cbl:138` |
| [COSGN00C](../../07-programs/COSGN00C.md) | cobol-program | COPY | active |  | `app/cbl/COSGN00C.cbl:48` |
| [COTRN00C](../../07-programs/COTRN00C.md) | cobol-program | COPY | active |  | `app/cbl/COTRN00C.cbl:61` |
| [COTRN01C](../../07-programs/COTRN01C.md) | cobol-program | COPY | active |  | `app/cbl/COTRN01C.cbl:52` |
| [COTRN02C](../../07-programs/COTRN02C.md) | cobol-program | COPY | active |  | `app/cbl/COTRN02C.cbl:71` |
| [COUSR00C](../../07-programs/COUSR00C.md) | cobol-program | COPY | active |  | `app/cbl/COUSR00C.cbl:66` |
| [COUSR01C](../../07-programs/COUSR01C.md) | cobol-program | COPY | active |  | `app/cbl/COUSR01C.cbl:46` |
| [COUSR02C](../../07-programs/COUSR02C.md) | cobol-program | COPY | active |  | `app/cbl/COUSR02C.cbl:49` |
| [COUSR03C](../../07-programs/COUSR03C.md) | cobol-program | COPY | active |  | `app/cbl/COUSR03C.cbl:49` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| CARDDEMO-COMMAREA | 19 | COACTUPC (7): `app/cbl/COACTUPC.cbl:883`, `app/cbl/COACTUPC.cbl:888`, `app/cbl/COACTUPC.cbl:889`, ...; COACTVWC (7): `app/cbl/COACTVWC.cbl:285`, `app/cbl/COACTVWC.cbl:288`, `app/cbl/COACTVWC.cbl:289`, ...; COADM01C (4): `app/cbl/COADM01C.cbl:90`, `app/cbl/COADM01C.cbl:113`, `app/cbl/COADM01C.cbl:147`, ...; COBIL00C (3): `app/cbl/COBIL00C.cbl:111`, `app/cbl/COBIL00C.cbl:148`, `app/cbl/COBIL00C.cbl:283`; COCRDLIC (10): `app/cbl/COCRDLIC.cbl:316`, `app/cbl/COCRDLIC.cbl:327`, `app/cbl/COCRDLIC.cbl:328`, ...; COCRDSLC (7): `app/cbl/COCRDSLC.cbl:271`, `app/cbl/COCRDSLC.cbl:274`, `app/cbl/COCRDSLC.cbl:275`, ...; COCRDUPC (7): `app/cbl/COCRDUPC.cbl:391`, `app/cbl/COCRDUPC.cbl:396`, `app/cbl/COCRDUPC.cbl:397`, ...; COMEN01C (4): `app/cbl/COMEN01C.cbl:86`, `app/cbl/COMEN01C.cbl:109`, `app/cbl/COMEN01C.cbl:158`, ...; COPAUS0C (5): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:191`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:200`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:256`, ...; COPAUS1C (4): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:166`, `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:171`, `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:204`, ...; CORPT00C (4): `app/cbl/CORPT00C.cbl:176`, `app/cbl/CORPT00C.cbl:201`, `app/cbl/CORPT00C.cbl:550`, ...; COSGN00C (4): `app/cbl/COSGN00C.cbl:100`, `app/cbl/COSGN00C.cbl:101`, `app/cbl/COSGN00C.cbl:233`, ...; COTRN00C (4): `app/cbl/COTRN00C.cbl:111`, `app/cbl/COTRN00C.cbl:140`, `app/cbl/COTRN00C.cbl:194`, ...; COTRN01C (3): `app/cbl/COTRN01C.cbl:98`, `app/cbl/COTRN01C.cbl:138`, `app/cbl/COTRN01C.cbl:207`; COTRN02C (4): `app/cbl/COTRN02C.cbl:119`, `app/cbl/COTRN02C.cbl:158`, `app/cbl/COTRN02C.cbl:510`, ...; COTRTLIC (10): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:516`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:527`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:528`, ...; COTRTUPC (7): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:371`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:376`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:377`, ...; COUSR00C (5): `app/cbl/COUSR00C.cbl:114`, `app/cbl/COUSR00C.cbl:143`, `app/cbl/COUSR00C.cbl:198`, ...; COUSR01C (3): `app/cbl/COUSR01C.cbl:82`, `app/cbl/COUSR01C.cbl:109`, `app/cbl/COUSR01C.cbl:177`; COUSR02C (3): `app/cbl/COUSR02C.cbl:94`, `app/cbl/COUSR02C.cbl:137`, `app/cbl/COUSR02C.cbl:260`; COUSR03C (3): `app/cbl/COUSR03C.cbl:94`, `app/cbl/COUSR03C.cbl:136`, `app/cbl/COUSR03C.cbl:207` |
| CDEMO-FROM-TRANID | 21 | COACTUPC (6): `app/cbl/COACTUPC.cbl:930`, `app/cbl/COACTUPC.cbl:931`, `app/cbl/COACTUPC.cbl:934`, ...; COACTVWC (4): `app/cbl/COACTVWC.cbl:328`, `app/cbl/COACTVWC.cbl:329`, `app/cbl/COACTVWC.cbl:332`, ...; COADM01C (1): `app/cbl/COADM01C.cbl:142`; COBIL00C (1): `app/cbl/COBIL00C.cbl:278`; COCRDLIC (6): `app/cbl/COCRDLIC.cbl:318`, `app/cbl/COCRDLIC.cbl:386`, `app/cbl/COCRDLIC.cbl:464`, ...; COCRDSLC (4): `app/cbl/COCRDSLC.cbl:309`, `app/cbl/COCRDSLC.cbl:310`, `app/cbl/COCRDSLC.cbl:313`, ...; COCRDUPC (6): `app/cbl/COCRDUPC.cbl:442`, `app/cbl/COCRDUPC.cbl:443`, `app/cbl/COCRDUPC.cbl:446`, ...; COMEN01C (2): `app/cbl/COMEN01C.cbl:153`, `app/cbl/COMEN01C.cbl:178`; COPAUS0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:317`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:671`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:362`; CORPT00C (1): `app/cbl/CORPT00C.cbl:545`; COSGN00C (1): `app/cbl/COSGN00C.cbl:224`; COTRN00C (2): `app/cbl/COTRN00C.cbl:189`, `app/cbl/COTRN00C.cbl:515`; COTRN01C (1): `app/cbl/COTRN01C.cbl:202`; COTRN02C (1): `app/cbl/COTRN02C.cbl:505`; COTRTLIC (10): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:518`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:547`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:592`, ...; COTRTUPC (6): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:431`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:432`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:435`, ...; COUSR00C (3): `app/cbl/COUSR00C.cbl:193`, `app/cbl/COUSR00C.cbl:203`, `app/cbl/COUSR00C.cbl:511`; COUSR01C (1): `app/cbl/COUSR01C.cbl:170`; COUSR02C (1): `app/cbl/COUSR02C.cbl:255`; COUSR03C (1): `app/cbl/COUSR03C.cbl:202` |
| CDEMO-FROM-PROGRAM | 22 | COACTUPC (6): `app/cbl/COACTUPC.cbl:881`, `app/cbl/COACTUPC.cbl:937`, `app/cbl/COACTUPC.cbl:938`, ...; COACTVWC (5): `app/cbl/COACTVWC.cbl:283`, `app/cbl/COACTVWC.cbl:334`, `app/cbl/COACTVWC.cbl:335`, ...; COADM01C (2): `app/cbl/COADM01C.cbl:87`, `app/cbl/COADM01C.cbl:143`; COBIL00C (3): `app/cbl/COBIL00C.cbl:129`, `app/cbl/COBIL00C.cbl:132`, `app/cbl/COBIL00C.cbl:279`; COCRDLIC (15): `app/cbl/COCRDLIC.cbl:319`, `app/cbl/COCRDLIC.cbl:337`, `app/cbl/COCRDLIC.cbl:358`, ...; COCRDSLC (8): `app/cbl/COCRDSLC.cbl:269`, `app/cbl/COCRDSLC.cbl:316`, `app/cbl/COCRDSLC.cbl:317`, ...; COCRDUPC (8): `app/cbl/COCRDUPC.cbl:389`, `app/cbl/COCRDUPC.cbl:449`, `app/cbl/COCRDUPC.cbl:450`, ...; COMEN01C (4): `app/cbl/COMEN01C.cbl:83`, `app/cbl/COMEN01C.cbl:154`, `app/cbl/COMEN01C.cbl:179`, ...; COPAUS0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:318`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:672`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:363`; CORPT00C (1): `app/cbl/CORPT00C.cbl:546`; COSGN00C (1): `app/cbl/COSGN00C.cbl:225`; COTRN00C (2): `app/cbl/COTRN00C.cbl:190`, `app/cbl/COTRN00C.cbl:516`; COTRN01C (3): `app/cbl/COTRN01C.cbl:116`, `app/cbl/COTRN01C.cbl:119`, `app/cbl/COTRN01C.cbl:203`; COTRN02C (3): `app/cbl/COTRN02C.cbl:137`, `app/cbl/COTRN02C.cbl:140`, `app/cbl/COTRN02C.cbl:506`; COTRTLIC (20): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:519`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:545`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:562`, ...; COTRTUPC (8): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:367`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:369`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:438`, ...; COUSR00C (3): `app/cbl/COUSR00C.cbl:194`, `app/cbl/COUSR00C.cbl:204`, `app/cbl/COUSR00C.cbl:512`; COUSR01C (1): `app/cbl/COUSR01C.cbl:171`; COUSR02C (3): `app/cbl/COUSR02C.cbl:113`, `app/cbl/COUSR02C.cbl:116`, `app/cbl/COUSR02C.cbl:256`; COUSR03C (3): `app/cbl/COUSR03C.cbl:112`, `app/cbl/COUSR03C.cbl:115`, `app/cbl/COUSR03C.cbl:203` |
| CDEMO-TO-TRANID | 23 | COACTUPC (2): `app/cbl/COACTUPC.cbl:932`, `app/cbl/COACTUPC.cbl:934`; COACTVWC (2): `app/cbl/COACTVWC.cbl:330`, `app/cbl/COACTVWC.cbl:332`; COCRDSLC (2): `app/cbl/COCRDSLC.cbl:311`, `app/cbl/COCRDSLC.cbl:313`; COCRDUPC (2): `app/cbl/COCRDUPC.cbl:444`, `app/cbl/COCRDUPC.cbl:446`; COTRTLIC (2): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:595`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:597`; COTRTUPC (2): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:433`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:435` |
| CDEMO-TO-PROGRAM | 24 | COACTUPC (3): `app/cbl/COACTUPC.cbl:939`, `app/cbl/COACTUPC.cbl:941`, `app/cbl/COACTUPC.cbl:957`; COACTVWC (3): `app/cbl/COACTVWC.cbl:336`, `app/cbl/COACTVWC.cbl:338`, `app/cbl/COACTVWC.cbl:350`; COADM01C (4): `app/cbl/COADM01C.cbl:101`, `app/cbl/COADM01C.cbl:165`, `app/cbl/COADM01C.cbl:166`, ...; COBIL00C (6): `app/cbl/COBIL00C.cbl:108`, `app/cbl/COBIL00C.cbl:130`, `app/cbl/COBIL00C.cbl:133`, ...; COCRDLIC (1): `app/cbl/COCRDLIC.cbl:392`; COCRDSLC (3): `app/cbl/COCRDSLC.cbl:318`, `app/cbl/COCRDSLC.cbl:320`, `app/cbl/COCRDSLC.cbl:332`; COCRDUPC (3): `app/cbl/COCRDUPC.cbl:451`, `app/cbl/COCRDUPC.cbl:453`, `app/cbl/COCRDUPC.cbl:474`; COMEN01C (4): `app/cbl/COMEN01C.cbl:97`, `app/cbl/COMEN01C.cbl:198`, `app/cbl/COMEN01C.cbl:199`, ...; COPAUS0C (7): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:192`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:236`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:316`, ...; COPAUS1C (3): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:168`, `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:185`, `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:368`; CORPT00C (5): `app/cbl/CORPT00C.cbl:173`, `app/cbl/CORPT00C.cbl:188`, `app/cbl/CORPT00C.cbl:542`, ...; COTRN00C (7): `app/cbl/COTRN00C.cbl:108`, `app/cbl/COTRN00C.cbl:123`, `app/cbl/COTRN00C.cbl:188`, ...; COTRN01C (7): `app/cbl/COTRN01C.cbl:95`, `app/cbl/COTRN01C.cbl:117`, `app/cbl/COTRN01C.cbl:120`, ...; COTRN02C (6): `app/cbl/COTRN02C.cbl:116`, `app/cbl/COTRN02C.cbl:138`, `app/cbl/COTRN02C.cbl:141`, ...; COTRTLIC (4): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:603`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:605`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:621`, ...; COTRTUPC (3): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:440`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:442`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:458`; COUSR00C (9): `app/cbl/COUSR00C.cbl:111`, `app/cbl/COUSR00C.cbl:126`, `app/cbl/COUSR00C.cbl:192`, ...; COUSR01C (5): `app/cbl/COUSR01C.cbl:79`, `app/cbl/COUSR01C.cbl:94`, `app/cbl/COUSR01C.cbl:167`, ...; COUSR02C (7): `app/cbl/COUSR02C.cbl:91`, `app/cbl/COUSR02C.cbl:114`, `app/cbl/COUSR02C.cbl:117`, ...; COUSR03C (7): `app/cbl/COUSR03C.cbl:91`, `app/cbl/COUSR03C.cbl:113`, `app/cbl/COUSR03C.cbl:116`, ... |
| CDEMO-USER-ID | 25 | COSGN00C (2): `app/cbl/COSGN00C.cbl:134`, `app/cbl/COSGN00C.cbl:226` |
| CDEMO-USER-TYPE | 26 | COSGN00C (1): `app/cbl/COSGN00C.cbl:227` |
| CDEMO-USRTYP-ADMIN | 27 | COSGN00C (1): `app/cbl/COSGN00C.cbl:230`; COTRTLIC (3): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:520`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:611`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:751`; COTRTUPC (1): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:448` |
| CDEMO-USRTYP-USER | 28 | COACTUPC (1): `app/cbl/COACTUPC.cbl:947`; COACTVWC (1): `app/cbl/COACTVWC.cbl:344`; COCRDLIC (5): `app/cbl/COCRDLIC.cbl:320`, `app/cbl/COCRDLIC.cbl:388`, `app/cbl/COCRDLIC.cbl:466`, ...; COCRDSLC (1): `app/cbl/COCRDSLC.cbl:326`; COCRDUPC (1): `app/cbl/COCRDUPC.cbl:464`; COMEN01C (1): `app/cbl/COMEN01C.cbl:136`; COTRTLIC (1): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:634` |
| CDEMO-PGM-CONTEXT | 29 | COADM01C (1): `app/cbl/COADM01C.cbl:144`; COBIL00C (1): `app/cbl/COBIL00C.cbl:280`; COMEN01C (2): `app/cbl/COMEN01C.cbl:155`, `app/cbl/COMEN01C.cbl:183`; COPAUS0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:319`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:673`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:364`; CORPT00C (1): `app/cbl/CORPT00C.cbl:547`; COSGN00C (1): `app/cbl/COSGN00C.cbl:228`; COTRN00C (2): `app/cbl/COTRN00C.cbl:191`, `app/cbl/COTRN00C.cbl:517`; COTRN01C (1): `app/cbl/COTRN01C.cbl:204`; COTRN02C (1): `app/cbl/COTRN02C.cbl:507`; COUSR00C (3): `app/cbl/COUSR00C.cbl:195`, `app/cbl/COUSR00C.cbl:205`, `app/cbl/COUSR00C.cbl:513`; COUSR01C (1): `app/cbl/COUSR01C.cbl:174`; COUSR02C (1): `app/cbl/COUSR02C.cbl:257`; COUSR03C (1): `app/cbl/COUSR03C.cbl:204` |
| CDEMO-PGM-ENTER | 30 | COACTUPC (6): `app/cbl/COACTUPC.cbl:885`, `app/cbl/COACTUPC.cbl:948`, `app/cbl/COACTUPC.cbl:965`, ...; COACTVWC (2): `app/cbl/COACTVWC.cbl:345`, `app/cbl/COACTVWC.cbl:353`; COCRDLIC (9): `app/cbl/COCRDLIC.cbl:321`, `app/cbl/COCRDLIC.cbl:336`, `app/cbl/COCRDLIC.cbl:339`, ...; COCRDSLC (3): `app/cbl/COCRDSLC.cbl:327`, `app/cbl/COCRDSLC.cbl:339`, `app/cbl/COCRDSLC.cbl:349`; COCRDUPC (7): `app/cbl/COCRDUPC.cbl:393`, `app/cbl/COCRDUPC.cbl:465`, `app/cbl/COCRDUPC.cbl:482`, ...; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:320`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:365`; COTRTLIC (9): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:521`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:544`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:549`, ...; COTRTUPC (6): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:373`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:417`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:449`, ... |
| CDEMO-PGM-REENTER | 31 | COACTUPC (5): `app/cbl/COACTUPC.cbl:882`, `app/cbl/COACTUPC.cbl:967`, `app/cbl/COACTUPC.cbl:971`, ...; COACTVWC (4): `app/cbl/COACTVWC.cbl:284`, `app/cbl/COACTVWC.cbl:361`, `app/cbl/COACTVWC.cbl:562`, ...; COADM01C (2): `app/cbl/COADM01C.cbl:91`, `app/cbl/COADM01C.cbl:92`; COBIL00C (2): `app/cbl/COBIL00C.cbl:112`, `app/cbl/COBIL00C.cbl:113`; COCRDLIC (1): `app/cbl/COCRDLIC.cbl:459`; COCRDSLC (5): `app/cbl/COCRDSLC.cbl:270`, `app/cbl/COCRDSLC.cbl:357`, `app/cbl/COCRDSLC.cbl:542`, ...; COCRDUPC (7): `app/cbl/COCRDUPC.cbl:390`, `app/cbl/COCRDUPC.cbl:486`, `app/cbl/COCRDUPC.cbl:505`, ...; COMEN01C (2): `app/cbl/COMEN01C.cbl:87`, `app/cbl/COMEN01C.cbl:88`; COPAUS0C (3): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:194`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:202`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:203`; COPAUS1C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:173`, `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:174`; CORPT00C (2): `app/cbl/CORPT00C.cbl:177`, `app/cbl/CORPT00C.cbl:178`; COTRN00C (2): `app/cbl/COTRN00C.cbl:112`, `app/cbl/COTRN00C.cbl:113`; COTRN01C (2): `app/cbl/COTRN01C.cbl:99`, `app/cbl/COTRN01C.cbl:100`; COTRN02C (2): `app/cbl/COTRN02C.cbl:120`, `app/cbl/COTRN02C.cbl:121`; COTRTLIC (1): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:739`; COTRTUPC (6): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:368`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:370`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:465`, ...; COUSR00C (2): `app/cbl/COUSR00C.cbl:115`, `app/cbl/COUSR00C.cbl:116`; COUSR01C (2): `app/cbl/COUSR01C.cbl:83`, `app/cbl/COUSR01C.cbl:84`; COUSR02C (2): `app/cbl/COUSR02C.cbl:95`, `app/cbl/COUSR02C.cbl:96`; COUSR03C (2): `app/cbl/COUSR03C.cbl:95`, `app/cbl/COUSR03C.cbl:96` |
| CDEMO-CUST-ID | 33 | COACTUPC (4): `app/cbl/COACTUPC.cbl:3631`, `app/cbl/COACTUPC.cbl:3666`, `app/cbl/COACTUPC.cbl:3806`, ...; COACTVWC (2): `app/cbl/COACTVWC.cbl:708`, `app/cbl/COACTVWC.cbl:739`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:830`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:246` |
| CDEMO-CUST-FNAME | 34 | COACTUPC (1): `app/cbl/COACTUPC.cbl:3807` |
| CDEMO-CUST-MNAME | 35 | COACTUPC (1): `app/cbl/COACTUPC.cbl:3808` |
| CDEMO-CUST-LNAME | 36 | COACTUPC (1): `app/cbl/COACTUPC.cbl:3809` |
| CDEMO-ACCT-ID | 38 | COACTUPC (6): `app/cbl/COACTUPC.cbl:983`, `app/cbl/COACTUPC.cbl:1794`, `app/cbl/COACTUPC.cbl:1812`, ...; COACTVWC (4): `app/cbl/COACTVWC.cbl:660`, `app/cbl/COACTVWC.cbl:675`, `app/cbl/COACTVWC.cbl:678`, ...; COCRDLIC (7): `app/cbl/COCRDLIC.cbl:532`, `app/cbl/COCRDLIC.cbl:560`, `app/cbl/COCRDLIC.cbl:849`, ...; COCRDSLC (5): `app/cbl/COCRDSLC.cbl:342`, `app/cbl/COCRDSLC.cbl:462`, `app/cbl/COCRDSLC.cbl:659`, ...; COCRDUPC (8): `app/cbl/COCRDUPC.cbl:460`, `app/cbl/COCRDUPC.cbl:490`, `app/cbl/COCRDUPC.cbl:521`, ...; COPAUS0C (4): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:207`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:208`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:284`, ...; COPAUS1C (5): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:211`, `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:213`, `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:231`, ...; COTRTUPC (2): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:473`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1069` |
| CDEMO-ACCT-STATUS | 39 | COACTUPC (2): `app/cbl/COACTUPC.cbl:2631`, `app/cbl/COACTUPC.cbl:3810`; COCRDUPC (1): `app/cbl/COCRDUPC.cbl:1017`; COTRTUPC (1): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1071` |
| CDEMO-CARD-NUM | 41 | COACTUPC (3): `app/cbl/COACTUPC.cbl:2630`, `app/cbl/COACTUPC.cbl:3667`, `app/cbl/COACTUPC.cbl:3811`; COACTVWC (1): `app/cbl/COACTVWC.cbl:740`; COCRDLIC (7): `app/cbl/COCRDLIC.cbl:534`, `app/cbl/COCRDLIC.cbl:562`, `app/cbl/COCRDLIC.cbl:861`, ...; COCRDSLC (5): `app/cbl/COCRDSLC.cbl:343`, `app/cbl/COCRDSLC.cbl:468`, `app/cbl/COCRDSLC.cbl:700`, ...; COCRDUPC (8): `app/cbl/COCRDUPC.cbl:461`, `app/cbl/COCRDUPC.cbl:491`, `app/cbl/COCRDUPC.cbl:522`, ...; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:831`; COTRTUPC (1): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1070` |
| CDEMO-LAST-MAP | 43 | COACTUPC (1): `app/cbl/COACTUPC.cbl:950`; COACTVWC (1): `app/cbl/COACTVWC.cbl:347`; COCRDLIC (9): `app/cbl/COCRDLIC.cbl:322`, `app/cbl/COCRDLIC.cbl:340`, `app/cbl/COCRDLIC.cbl:391`, ...; COCRDSLC (1): `app/cbl/COCRDSLC.cbl:329`; COCRDUPC (1): `app/cbl/COCRDUPC.cbl:467`; COTRTLIC (8): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:522`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:551`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:614`, ...; COTRTUPC (1): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:451` |
| CDEMO-LAST-MAPSET | 44 | COACTUPC (2): `app/cbl/COACTUPC.cbl:949`, `app/cbl/COACTUPC.cbl:3171`; COACTVWC (1): `app/cbl/COACTVWC.cbl:346`; COCRDLIC (8): `app/cbl/COCRDLIC.cbl:323`, `app/cbl/COCRDLIC.cbl:390`, `app/cbl/COCRDLIC.cbl:425`, ...; COCRDSLC (3): `app/cbl/COCRDSLC.cbl:328`, `app/cbl/COCRDSLC.cbl:505`, `app/cbl/COCRDSLC.cbl:527`; COCRDUPC (5): `app/cbl/COCRDUPC.cbl:437`, `app/cbl/COCRDUPC.cbl:439`, `app/cbl/COCRDUPC.cbl:459`, ...; COTRTLIC (7): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:523`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:613`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:636`, ...; COTRTUPC (1): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:450` |

Named in no procedure statement of the copying programs (may still be moved as part of a group): CDEMO-GENERAL-INFO (line 20), CDEMO-CUSTOMER-INFO (line 32), CDEMO-ACCOUNT-INFO (line 37), CDEMO-CARD-INFO (line 40), CDEMO-MORE-INFO (line 42).

## Key fields

| Field | Meaning | Source |
|---|---|---|
| CARDDEMO-COMMAREA | Shared CICS communication area passed on XCTL and RETURN between CardDemo online programs; COACTUPC places its own program area right after it. | `app/cpy/COCOM01Y.cpy:19` |
| CDEMO-FROM-PROGRAM | Program that transferred control here; used to detect entry from the menu and as the PF3 return target. | `app/cpy/COCOM01Y.cpy:22` |
| CDEMO-FROM-TRANID | Transaction of the calling program; PF3 returns to it, or to CM00 when blank. | `app/cpy/COCOM01Y.cpy:21` |
| CDEMO-TO-PROGRAM | Target program for the next XCTL. | `app/cpy/COCOM01Y.cpy:24` |
| CDEMO-USER-TYPE | Signed-on user type: 'A' admin (CDEMO-USRTYP-ADMIN) or 'U' user (CDEMO-USRTYP-USER). | `app/cpy/COCOM01Y.cpy:26-28` |
| CDEMO-PGM-CONTEXT | 0 = first entry into a program (CDEMO-PGM-ENTER), 1 = re-entry after a screen was sent (CDEMO-PGM-REENTER). | `app/cpy/COCOM01Y.cpy:29-31` |
| CDEMO-CUST-ID | Current customer id; COACTUPC fills it from the card cross-reference and uses it as the CUSTDAT key. | `app/cpy/COCOM01Y.cpy:33` |
| CDEMO-ACCT-ID | Current account id carried between screens. | `app/cpy/COCOM01Y.cpy:38` |
| CDEMO-CARD-NUM | Current card number from the cross-reference. | `app/cpy/COCOM01Y.cpy:41` |
| CDEMO-LAST-MAPSET | Mapset last sent; COACTUPC compares it with the card list mapset to choose the account-id colour. | `app/cpy/COCOM01Y.cpy:44` |

## Observations

- security: COACTUPC sets CDEMO-USRTYP-USER on PF3 exit, overwriting the user type carried in this area. (`app/cbl/COACTUPC.cbl:947`)

## Sources

- `app/cpy/COCOM01Y.cpy`
- `docs/_work/structure/copybooks/COCOM01Y.json`
- `docs/_work/layouts/COCOM01Y.json`
- `docs/_work/semantic/copybooks/COCOM01Y.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
