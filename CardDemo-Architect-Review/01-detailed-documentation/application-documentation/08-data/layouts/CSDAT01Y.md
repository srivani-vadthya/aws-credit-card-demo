# Layout CSDAT01Y

| Item | Value |
|---|---|
| Source | `app/cpy/CSDAT01Y.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 58 |
| Data items | 39 (88-levels: 0) |
| Semantic analysis | validated (batch B04) |

## Purpose

Defines WS-DATE-TIME, working storage for the current date and time: a raw area that receives FUNCTION CURRENT-DATE, numeric redefinitions, and edited MM/DD/YY, HH:MM:SS and timestamp layouts. COACTUPC uses it only in 3100-SCREEN-INIT to put the current date and time in the screen header. (Confirmed)

Evidence: `app/cpy/CSDAT01Y.cpy:17-55`, `app/cbl/COACTUPC.cbl:2671-2690`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | WS-DATE-TIME |  |  | 1 | 58 | 58 |  |  |  | 17 |
| 05 | &nbsp;&nbsp;WS-CURDATE-DATA |  |  | 1 | 16 | 16 |  |  |  | 18 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-CURDATE |  |  | 1 | 8 | 8 |  |  |  | 19 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-CURDATE-YEAR | 9(04) | DISPLAY | 1 | 4 | 4 |  |  |  | 20 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-CURDATE-MONTH | 9(02) | DISPLAY | 5 | 6 | 2 |  |  |  | 21 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-CURDATE-DAY | 9(02) | DISPLAY | 7 | 8 | 2 |  |  |  | 22 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-CURDATE-N | 9(08) | DISPLAY | 1 | 8 | 8 |  | WS-CURDATE |  | 23 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-CURTIME |  |  | 9 | 16 | 8 |  |  |  | 24 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-CURTIME-HOURS | 9(02) | DISPLAY | 9 | 10 | 2 |  |  |  | 25 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-CURTIME-MINUTE | 9(02) | DISPLAY | 11 | 12 | 2 |  |  |  | 26 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-CURTIME-SECOND | 9(02) | DISPLAY | 13 | 14 | 2 |  |  |  | 27 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-CURTIME-MILSEC | 9(02) | DISPLAY | 15 | 16 | 2 |  |  |  | 28 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-CURTIME-N | 9(08) | DISPLAY | 9 | 16 | 8 |  | WS-CURTIME |  | 29 |
| 05 | &nbsp;&nbsp;WS-CURDATE-MM-DD-YY |  |  | 17 | 24 | 8 |  |  |  | 30 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-CURDATE-MM | 9(02) | DISPLAY | 17 | 18 | 2 |  |  |  | 31 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(01) | DISPLAY | 19 | 19 | 1 |  |  | '/' | 32 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-CURDATE-DD | 9(02) | DISPLAY | 20 | 21 | 2 |  |  |  | 33 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(01) | DISPLAY | 22 | 22 | 1 |  |  | '/' | 34 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-CURDATE-YY | 9(02) | DISPLAY | 23 | 24 | 2 |  |  |  | 35 |
| 05 | &nbsp;&nbsp;WS-CURTIME-HH-MM-SS |  |  | 25 | 32 | 8 |  |  |  | 36 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-CURTIME-HH | 9(02) | DISPLAY | 25 | 26 | 2 |  |  |  | 37 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(01) | DISPLAY | 27 | 27 | 1 |  |  | ':' | 38 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-CURTIME-MM | 9(02) | DISPLAY | 28 | 29 | 2 |  |  |  | 39 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(01) | DISPLAY | 30 | 30 | 1 |  |  | ':' | 40 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-CURTIME-SS | 9(02) | DISPLAY | 31 | 32 | 2 |  |  |  | 41 |
| 05 | &nbsp;&nbsp;WS-TIMESTAMP |  |  | 33 | 58 | 26 |  |  |  | 42 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-TIMESTAMP-DT-YYYY | 9(04) | DISPLAY | 33 | 36 | 4 |  |  |  | 43 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(01) | DISPLAY | 37 | 37 | 1 |  |  | '-' | 44 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-TIMESTAMP-DT-MM | 9(02) | DISPLAY | 38 | 39 | 2 |  |  |  | 45 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(01) | DISPLAY | 40 | 40 | 1 |  |  | '-' | 46 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-TIMESTAMP-DT-DD | 9(02) | DISPLAY | 41 | 42 | 2 |  |  |  | 47 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(01) | DISPLAY | 43 | 43 | 1 |  |  | ' ' | 48 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-TIMESTAMP-TM-HH | 9(02) | DISPLAY | 44 | 45 | 2 |  |  |  | 49 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(01) | DISPLAY | 46 | 46 | 1 |  |  | ':' | 50 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-TIMESTAMP-TM-MM | 9(02) | DISPLAY | 47 | 48 | 2 |  |  |  | 51 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(01) | DISPLAY | 49 | 49 | 1 |  |  | ':' | 52 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-TIMESTAMP-TM-SS | 9(02) | DISPLAY | 50 | 51 | 2 |  |  |  | 53 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(01) | DISPLAY | 52 | 52 | 1 |  |  | '.' | 54 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-TIMESTAMP-TM-MS6 | 9(06) | DISPLAY | 53 | 58 | 6 |  |  |  | 55 |

## Level-88 conditions

None.

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [COPAUS0C](../../07-programs/COPAUS0C.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:135` |
| [COPAUS1C](../../07-programs/COPAUS1C.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:129` |
| [COTRTLIC](../../07-programs/COTRTLIC.md) | cobol-program | COPY | active |  | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:480` |
| [COTRTUPC](../../07-programs/COTRTUPC.md) | cobol-program | COPY | active |  | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:268` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active |  | `app/cbl/COACTUPC.cbl:626` |
| [COACTVWC](../../07-programs/COACTVWC.md) | cobol-program | COPY | active |  | `app/cbl/COACTVWC.cbl:232` |
| [COADM01C](../../07-programs/COADM01C.md) | cobol-program | COPY | active |  | `app/cbl/COADM01C.cbl:56` |
| [COBIL00C](../../07-programs/COBIL00C.md) | cobol-program | COPY | active |  | `app/cbl/COBIL00C.cbl:77` |
| [COCRDLIC](../../07-programs/COCRDLIC.md) | cobol-program | COPY | active |  | `app/cbl/COCRDLIC.cbl:279` |
| [COCRDSLC](../../07-programs/COCRDSLC.md) | cobol-program | COPY | active |  | `app/cbl/COCRDSLC.cbl:218` |
| [COCRDUPC](../../07-programs/COCRDUPC.md) | cobol-program | COPY | active |  | `app/cbl/COCRDUPC.cbl:337` |
| [COMEN01C](../../07-programs/COMEN01C.md) | cobol-program | COPY | active |  | `app/cbl/COMEN01C.cbl:56` |
| [CORPT00C](../../07-programs/CORPT00C.md) | cobol-program | COPY | active |  | `app/cbl/CORPT00C.cbl:143` |
| [COSGN00C](../../07-programs/COSGN00C.md) | cobol-program | COPY | active |  | `app/cbl/COSGN00C.cbl:53` |
| [COTRN00C](../../07-programs/COTRN00C.md) | cobol-program | COPY | active |  | `app/cbl/COTRN00C.cbl:75` |
| [COTRN01C](../../07-programs/COTRN01C.md) | cobol-program | COPY | active |  | `app/cbl/COTRN01C.cbl:66` |
| [COTRN02C](../../07-programs/COTRN02C.md) | cobol-program | COPY | active |  | `app/cbl/COTRN02C.cbl:85` |
| [COUSR00C](../../07-programs/COUSR00C.md) | cobol-program | COPY | active |  | `app/cbl/COUSR00C.cbl:79` |
| [COUSR01C](../../07-programs/COUSR01C.md) | cobol-program | COPY | active |  | `app/cbl/COUSR01C.cbl:51` |
| [COUSR02C](../../07-programs/COUSR02C.md) | cobol-program | COPY | active |  | `app/cbl/COUSR02C.cbl:63` |
| [COUSR03C](../../07-programs/COUSR03C.md) | cobol-program | COPY | active |  | `app/cbl/COUSR03C.cbl:63` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| WS-CURDATE-DATA | 18 | COACTUPC (2): `app/cbl/COACTUPC.cbl:2671`, `app/cbl/COACTUPC.cbl:2678`; COACTVWC (2): `app/cbl/COACTVWC.cbl:434`, `app/cbl/COACTVWC.cbl:441`; COADM01C (1): `app/cbl/COADM01C.cbl:207`; COBIL00C (1): `app/cbl/COBIL00C.cbl:321`; COCRDLIC (2): `app/cbl/COCRDLIC.cbl:645`, `app/cbl/COCRDLIC.cbl:652`; COCRDSLC (2): `app/cbl/COCRDSLC.cbl:430`, `app/cbl/COCRDSLC.cbl:437`; COCRDUPC (2): `app/cbl/COCRDUPC.cbl:1055`, `app/cbl/COCRDUPC.cbl:1062`; COMEN01C (1): `app/cbl/COMEN01C.cbl:240`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:729`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:411`; CORPT00C (3): `app/cbl/CORPT00C.cbl:215`, `app/cbl/CORPT00C.cbl:241`, `app/cbl/CORPT00C.cbl:611`; COSGN00C (1): `app/cbl/COSGN00C.cbl:179`; COTRN00C (1): `app/cbl/COTRN00C.cbl:569`; COTRN01C (1): `app/cbl/COTRN01C.cbl:245`; COTRN02C (1): `app/cbl/COTRN02C.cbl:554`; COTRTLIC (2): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1296`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1303`; COTRTUPC (2): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1113`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1120`; COUSR00C (1): `app/cbl/COUSR00C.cbl:564`; COUSR01C (1): `app/cbl/COUSR01C.cbl:216`; COUSR02C (1): `app/cbl/COUSR02C.cbl:298`; COUSR03C (1): `app/cbl/COUSR03C.cbl:245` |
| WS-CURDATE-YEAR | 20 | COACTUPC (1): `app/cbl/COACTUPC.cbl:2682`; COACTVWC (1): `app/cbl/COACTVWC.cbl:445`; COADM01C (1): `app/cbl/COADM01C.cbl:216`; COBIL00C (1): `app/cbl/COBIL00C.cbl:330`; COCRDLIC (1): `app/cbl/COCRDLIC.cbl:656`; COCRDSLC (1): `app/cbl/COCRDSLC.cbl:441`; COCRDUPC (1): `app/cbl/COCRDUPC.cbl:1066`; COMEN01C (1): `app/cbl/COMEN01C.cbl:249`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:738`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:420`; CORPT00C (5): `app/cbl/CORPT00C.cbl:217`, `app/cbl/CORPT00C.cbl:226`, `app/cbl/CORPT00C.cbl:232`, ...; COSGN00C (1): `app/cbl/COSGN00C.cbl:188`; COTRN00C (1): `app/cbl/COTRN00C.cbl:578`; COTRN01C (1): `app/cbl/COTRN01C.cbl:254`; COTRN02C (1): `app/cbl/COTRN02C.cbl:563`; COTRTLIC (1): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1307`; COTRTUPC (1): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1124`; COUSR00C (1): `app/cbl/COUSR00C.cbl:573`; COUSR01C (1): `app/cbl/COUSR01C.cbl:225`; COUSR02C (1): `app/cbl/COUSR02C.cbl:307`; COUSR03C (1): `app/cbl/COUSR03C.cbl:254` |
| WS-CURDATE-MONTH | 21 | COACTUPC (1): `app/cbl/COACTUPC.cbl:2680`; COACTVWC (1): `app/cbl/COACTVWC.cbl:443`; COADM01C (1): `app/cbl/COADM01C.cbl:214`; COBIL00C (1): `app/cbl/COBIL00C.cbl:328`; COCRDLIC (1): `app/cbl/COCRDLIC.cbl:654`; COCRDSLC (1): `app/cbl/COCRDSLC.cbl:439`; COCRDUPC (1): `app/cbl/COCRDUPC.cbl:1064`; COMEN01C (1): `app/cbl/COMEN01C.cbl:247`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:736`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:418`; CORPT00C (6): `app/cbl/CORPT00C.cbl:218`, `app/cbl/CORPT00C.cbl:224`, `app/cbl/CORPT00C.cbl:225`, ...; COSGN00C (1): `app/cbl/COSGN00C.cbl:186`; COTRN00C (1): `app/cbl/COTRN00C.cbl:576`; COTRN01C (1): `app/cbl/COTRN01C.cbl:252`; COTRN02C (1): `app/cbl/COTRN02C.cbl:561`; COTRTLIC (1): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1305`; COTRTUPC (1): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1122`; COUSR00C (1): `app/cbl/COUSR00C.cbl:571`; COUSR01C (1): `app/cbl/COUSR01C.cbl:223`; COUSR02C (1): `app/cbl/COUSR02C.cbl:305`; COUSR03C (1): `app/cbl/COUSR03C.cbl:252` |
| WS-CURDATE-DAY | 22 | COACTUPC (1): `app/cbl/COACTUPC.cbl:2681`; COACTVWC (1): `app/cbl/COACTVWC.cbl:444`; COADM01C (1): `app/cbl/COADM01C.cbl:215`; COBIL00C (1): `app/cbl/COBIL00C.cbl:329`; COCRDLIC (1): `app/cbl/COCRDLIC.cbl:655`; COCRDSLC (1): `app/cbl/COCRDSLC.cbl:440`; COCRDUPC (1): `app/cbl/COCRDUPC.cbl:1065`; COMEN01C (1): `app/cbl/COMEN01C.cbl:248`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:737`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:419`; CORPT00C (3): `app/cbl/CORPT00C.cbl:223`, `app/cbl/CORPT00C.cbl:234`, `app/cbl/CORPT00C.cbl:619`; COSGN00C (1): `app/cbl/COSGN00C.cbl:187`; COTRN00C (1): `app/cbl/COTRN00C.cbl:577`; COTRN01C (1): `app/cbl/COTRN01C.cbl:253`; COTRN02C (1): `app/cbl/COTRN02C.cbl:562`; COTRTLIC (1): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1306`; COTRTUPC (1): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1123`; COUSR00C (1): `app/cbl/COUSR00C.cbl:572`; COUSR01C (1): `app/cbl/COUSR01C.cbl:224`; COUSR02C (1): `app/cbl/COUSR02C.cbl:306`; COUSR03C (1): `app/cbl/COUSR03C.cbl:253` |
| WS-CURDATE-N | 23 | CORPT00C (2): `app/cbl/CORPT00C.cbl:229`, `app/cbl/CORPT00C.cbl:230` |
| WS-CURTIME-HOURS | 25 | COACTUPC (1): `app/cbl/COACTUPC.cbl:2686`; COACTVWC (1): `app/cbl/COACTVWC.cbl:449`; COADM01C (1): `app/cbl/COADM01C.cbl:220`; COBIL00C (1): `app/cbl/COBIL00C.cbl:334`; COCRDLIC (1): `app/cbl/COCRDLIC.cbl:660`; COCRDSLC (1): `app/cbl/COCRDSLC.cbl:445`; COCRDUPC (1): `app/cbl/COCRDUPC.cbl:1070`; COMEN01C (1): `app/cbl/COMEN01C.cbl:253`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:742`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:424`; CORPT00C (1): `app/cbl/CORPT00C.cbl:624`; COSGN00C (1): `app/cbl/COSGN00C.cbl:192`; COTRN00C (1): `app/cbl/COTRN00C.cbl:582`; COTRN01C (1): `app/cbl/COTRN01C.cbl:258`; COTRN02C (1): `app/cbl/COTRN02C.cbl:567`; COTRTLIC (1): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1311`; COTRTUPC (1): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1128`; COUSR00C (1): `app/cbl/COUSR00C.cbl:577`; COUSR01C (1): `app/cbl/COUSR01C.cbl:229`; COUSR02C (1): `app/cbl/COUSR02C.cbl:311`; COUSR03C (1): `app/cbl/COUSR03C.cbl:258` |
| WS-CURTIME-MINUTE | 26 | COACTUPC (1): `app/cbl/COACTUPC.cbl:2687`; COACTVWC (1): `app/cbl/COACTVWC.cbl:450`; COADM01C (1): `app/cbl/COADM01C.cbl:221`; COBIL00C (1): `app/cbl/COBIL00C.cbl:335`; COCRDLIC (1): `app/cbl/COCRDLIC.cbl:661`; COCRDSLC (1): `app/cbl/COCRDSLC.cbl:446`; COCRDUPC (1): `app/cbl/COCRDUPC.cbl:1071`; COMEN01C (1): `app/cbl/COMEN01C.cbl:254`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:743`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:425`; CORPT00C (1): `app/cbl/CORPT00C.cbl:625`; COSGN00C (1): `app/cbl/COSGN00C.cbl:193`; COTRN00C (1): `app/cbl/COTRN00C.cbl:583`; COTRN01C (1): `app/cbl/COTRN01C.cbl:259`; COTRN02C (1): `app/cbl/COTRN02C.cbl:568`; COTRTLIC (1): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1312`; COTRTUPC (1): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1129`; COUSR00C (1): `app/cbl/COUSR00C.cbl:578`; COUSR01C (1): `app/cbl/COUSR01C.cbl:230`; COUSR02C (1): `app/cbl/COUSR02C.cbl:312`; COUSR03C (1): `app/cbl/COUSR03C.cbl:259` |
| WS-CURTIME-SECOND | 27 | COACTUPC (1): `app/cbl/COACTUPC.cbl:2688`; COACTVWC (1): `app/cbl/COACTVWC.cbl:451`; COADM01C (1): `app/cbl/COADM01C.cbl:222`; COBIL00C (1): `app/cbl/COBIL00C.cbl:336`; COCRDLIC (1): `app/cbl/COCRDLIC.cbl:662`; COCRDSLC (1): `app/cbl/COCRDSLC.cbl:447`; COCRDUPC (1): `app/cbl/COCRDUPC.cbl:1072`; COMEN01C (1): `app/cbl/COMEN01C.cbl:255`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:744`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:426`; CORPT00C (1): `app/cbl/CORPT00C.cbl:626`; COSGN00C (1): `app/cbl/COSGN00C.cbl:194`; COTRN00C (1): `app/cbl/COTRN00C.cbl:584`; COTRN01C (1): `app/cbl/COTRN01C.cbl:260`; COTRN02C (1): `app/cbl/COTRN02C.cbl:569`; COTRTLIC (1): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1313`; COTRTUPC (1): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1130`; COUSR00C (1): `app/cbl/COUSR00C.cbl:579`; COUSR01C (1): `app/cbl/COUSR01C.cbl:231`; COUSR02C (1): `app/cbl/COUSR02C.cbl:313`; COUSR03C (1): `app/cbl/COUSR03C.cbl:260` |
| WS-CURDATE-MM-DD-YY | 30 | COACTUPC (1): `app/cbl/COACTUPC.cbl:2684`; COACTVWC (1): `app/cbl/COACTVWC.cbl:447`; COADM01C (1): `app/cbl/COADM01C.cbl:218`; COBIL00C (1): `app/cbl/COBIL00C.cbl:332`; COCRDLIC (1): `app/cbl/COCRDLIC.cbl:658`; COCRDSLC (1): `app/cbl/COCRDSLC.cbl:443`; COCRDUPC (1): `app/cbl/COCRDUPC.cbl:1068`; COMEN01C (1): `app/cbl/COMEN01C.cbl:251`; COPAUS0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:534`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:740`; COPAUS1C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:300`, `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:422`; CORPT00C (1): `app/cbl/CORPT00C.cbl:622`; COSGN00C (1): `app/cbl/COSGN00C.cbl:190`; COTRN00C (2): `app/cbl/COTRN00C.cbl:388`, `app/cbl/COTRN00C.cbl:580`; COTRN01C (1): `app/cbl/COTRN01C.cbl:256`; COTRN02C (1): `app/cbl/COTRN02C.cbl:565`; COTRTLIC (1): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1309`; COTRTUPC (1): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1126`; COUSR00C (1): `app/cbl/COUSR00C.cbl:575`; COUSR01C (1): `app/cbl/COUSR01C.cbl:227`; COUSR02C (1): `app/cbl/COUSR02C.cbl:309`; COUSR03C (1): `app/cbl/COUSR03C.cbl:256` |
| WS-CURDATE-MM | 31 | COACTUPC (1): `app/cbl/COACTUPC.cbl:2680`; COACTVWC (1): `app/cbl/COACTVWC.cbl:443`; COADM01C (1): `app/cbl/COADM01C.cbl:214`; COBIL00C (1): `app/cbl/COBIL00C.cbl:328`; COCRDLIC (1): `app/cbl/COCRDLIC.cbl:654`; COCRDSLC (1): `app/cbl/COCRDSLC.cbl:439`; COCRDUPC (1): `app/cbl/COCRDUPC.cbl:1064`; COMEN01C (1): `app/cbl/COMEN01C.cbl:247`; COPAUS0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:532`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:736`; COPAUS1C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:298`, `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:418`; CORPT00C (1): `app/cbl/CORPT00C.cbl:618`; COSGN00C (1): `app/cbl/COSGN00C.cbl:186`; COTRN00C (2): `app/cbl/COTRN00C.cbl:386`, `app/cbl/COTRN00C.cbl:576`; COTRN01C (1): `app/cbl/COTRN01C.cbl:252`; COTRN02C (1): `app/cbl/COTRN02C.cbl:561`; COTRTLIC (1): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1305`; COTRTUPC (1): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1122`; COUSR00C (1): `app/cbl/COUSR00C.cbl:571`; COUSR01C (1): `app/cbl/COUSR01C.cbl:223`; COUSR02C (1): `app/cbl/COUSR02C.cbl:305`; COUSR03C (1): `app/cbl/COUSR03C.cbl:252` |
| WS-CURDATE-DD | 33 | COACTUPC (1): `app/cbl/COACTUPC.cbl:2681`; COACTVWC (1): `app/cbl/COACTVWC.cbl:444`; COADM01C (1): `app/cbl/COADM01C.cbl:215`; COBIL00C (1): `app/cbl/COBIL00C.cbl:329`; COCRDLIC (1): `app/cbl/COCRDLIC.cbl:655`; COCRDSLC (1): `app/cbl/COCRDSLC.cbl:440`; COCRDUPC (1): `app/cbl/COCRDUPC.cbl:1065`; COMEN01C (1): `app/cbl/COMEN01C.cbl:248`; COPAUS0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:533`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:737`; COPAUS1C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:299`, `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:419`; CORPT00C (1): `app/cbl/CORPT00C.cbl:619`; COSGN00C (1): `app/cbl/COSGN00C.cbl:187`; COTRN00C (2): `app/cbl/COTRN00C.cbl:387`, `app/cbl/COTRN00C.cbl:577`; COTRN01C (1): `app/cbl/COTRN01C.cbl:253`; COTRN02C (1): `app/cbl/COTRN02C.cbl:562`; COTRTLIC (1): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1306`; COTRTUPC (1): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1123`; COUSR00C (1): `app/cbl/COUSR00C.cbl:572`; COUSR01C (1): `app/cbl/COUSR01C.cbl:224`; COUSR02C (1): `app/cbl/COUSR02C.cbl:306`; COUSR03C (1): `app/cbl/COUSR03C.cbl:253` |
| WS-CURDATE-YY | 35 | COACTUPC (1): `app/cbl/COACTUPC.cbl:2682`; COACTVWC (1): `app/cbl/COACTVWC.cbl:445`; COADM01C (1): `app/cbl/COADM01C.cbl:216`; COBIL00C (1): `app/cbl/COBIL00C.cbl:330`; COCRDLIC (1): `app/cbl/COCRDLIC.cbl:656`; COCRDSLC (1): `app/cbl/COCRDSLC.cbl:441`; COCRDUPC (1): `app/cbl/COCRDUPC.cbl:1066`; COMEN01C (1): `app/cbl/COMEN01C.cbl:249`; COPAUS0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:531`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:738`; COPAUS1C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:297`, `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:420`; CORPT00C (1): `app/cbl/CORPT00C.cbl:620`; COSGN00C (1): `app/cbl/COSGN00C.cbl:188`; COTRN00C (2): `app/cbl/COTRN00C.cbl:385`, `app/cbl/COTRN00C.cbl:578`; COTRN01C (1): `app/cbl/COTRN01C.cbl:254`; COTRN02C (1): `app/cbl/COTRN02C.cbl:563`; COTRTLIC (1): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1307`; COTRTUPC (1): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1124`; COUSR00C (1): `app/cbl/COUSR00C.cbl:573`; COUSR01C (1): `app/cbl/COUSR01C.cbl:225`; COUSR02C (1): `app/cbl/COUSR02C.cbl:307`; COUSR03C (1): `app/cbl/COUSR03C.cbl:254` |
| WS-CURTIME-HH-MM-SS | 36 | COACTUPC (1): `app/cbl/COACTUPC.cbl:2690`; COACTVWC (1): `app/cbl/COACTVWC.cbl:453`; COADM01C (1): `app/cbl/COADM01C.cbl:224`; COBIL00C (1): `app/cbl/COBIL00C.cbl:338`; COCRDLIC (1): `app/cbl/COCRDLIC.cbl:664`; COCRDSLC (1): `app/cbl/COCRDSLC.cbl:449`; COCRDUPC (1): `app/cbl/COCRDUPC.cbl:1074`; COMEN01C (1): `app/cbl/COMEN01C.cbl:257`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:746`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:428`; CORPT00C (1): `app/cbl/CORPT00C.cbl:628`; COSGN00C (1): `app/cbl/COSGN00C.cbl:196`; COTRN00C (1): `app/cbl/COTRN00C.cbl:586`; COTRN01C (1): `app/cbl/COTRN01C.cbl:262`; COTRN02C (1): `app/cbl/COTRN02C.cbl:571`; COTRTLIC (1): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1315`; COTRTUPC (1): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1132`; COUSR00C (1): `app/cbl/COUSR00C.cbl:581`; COUSR01C (1): `app/cbl/COUSR01C.cbl:233`; COUSR02C (1): `app/cbl/COUSR02C.cbl:315`; COUSR03C (1): `app/cbl/COUSR03C.cbl:262` |
| WS-CURTIME-HH | 37 | COACTUPC (1): `app/cbl/COACTUPC.cbl:2686`; COACTVWC (1): `app/cbl/COACTVWC.cbl:449`; COADM01C (1): `app/cbl/COADM01C.cbl:220`; COBIL00C (1): `app/cbl/COBIL00C.cbl:334`; COCRDLIC (1): `app/cbl/COCRDLIC.cbl:660`; COCRDSLC (1): `app/cbl/COCRDSLC.cbl:445`; COCRDUPC (1): `app/cbl/COCRDUPC.cbl:1070`; COMEN01C (1): `app/cbl/COMEN01C.cbl:253`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:742`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:424`; CORPT00C (1): `app/cbl/CORPT00C.cbl:624`; COSGN00C (1): `app/cbl/COSGN00C.cbl:192`; COTRN00C (1): `app/cbl/COTRN00C.cbl:582`; COTRN01C (1): `app/cbl/COTRN01C.cbl:258`; COTRN02C (1): `app/cbl/COTRN02C.cbl:567`; COTRTLIC (1): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1311`; COTRTUPC (1): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1128`; COUSR00C (1): `app/cbl/COUSR00C.cbl:577`; COUSR01C (1): `app/cbl/COUSR01C.cbl:229`; COUSR02C (1): `app/cbl/COUSR02C.cbl:311`; COUSR03C (1): `app/cbl/COUSR03C.cbl:258` |
| WS-CURTIME-MM | 39 | COACTUPC (1): `app/cbl/COACTUPC.cbl:2687`; COACTVWC (1): `app/cbl/COACTVWC.cbl:450`; COADM01C (1): `app/cbl/COADM01C.cbl:221`; COBIL00C (1): `app/cbl/COBIL00C.cbl:335`; COCRDLIC (1): `app/cbl/COCRDLIC.cbl:661`; COCRDSLC (1): `app/cbl/COCRDSLC.cbl:446`; COCRDUPC (1): `app/cbl/COCRDUPC.cbl:1071`; COMEN01C (1): `app/cbl/COMEN01C.cbl:254`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:743`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:425`; CORPT00C (1): `app/cbl/CORPT00C.cbl:625`; COSGN00C (1): `app/cbl/COSGN00C.cbl:193`; COTRN00C (1): `app/cbl/COTRN00C.cbl:583`; COTRN01C (1): `app/cbl/COTRN01C.cbl:259`; COTRN02C (1): `app/cbl/COTRN02C.cbl:568`; COTRTLIC (1): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1312`; COTRTUPC (1): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1129`; COUSR00C (1): `app/cbl/COUSR00C.cbl:578`; COUSR01C (1): `app/cbl/COUSR01C.cbl:230`; COUSR02C (1): `app/cbl/COUSR02C.cbl:312`; COUSR03C (1): `app/cbl/COUSR03C.cbl:259` |
| WS-CURTIME-SS | 41 | COACTUPC (1): `app/cbl/COACTUPC.cbl:2688`; COACTVWC (1): `app/cbl/COACTVWC.cbl:451`; COADM01C (1): `app/cbl/COADM01C.cbl:222`; COBIL00C (1): `app/cbl/COBIL00C.cbl:336`; COCRDLIC (1): `app/cbl/COCRDLIC.cbl:662`; COCRDSLC (1): `app/cbl/COCRDSLC.cbl:447`; COCRDUPC (1): `app/cbl/COCRDUPC.cbl:1072`; COMEN01C (1): `app/cbl/COMEN01C.cbl:255`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:744`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:426`; CORPT00C (1): `app/cbl/CORPT00C.cbl:626`; COSGN00C (1): `app/cbl/COSGN00C.cbl:194`; COTRN00C (1): `app/cbl/COTRN00C.cbl:584`; COTRN01C (1): `app/cbl/COTRN01C.cbl:260`; COTRN02C (1): `app/cbl/COTRN02C.cbl:569`; COTRTLIC (1): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1313`; COTRTUPC (1): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1130`; COUSR00C (1): `app/cbl/COUSR00C.cbl:579`; COUSR01C (1): `app/cbl/COUSR01C.cbl:231`; COUSR02C (1): `app/cbl/COUSR02C.cbl:313`; COUSR03C (1): `app/cbl/COUSR03C.cbl:260` |
| WS-TIMESTAMP | 42 | COBIL00C (4): `app/cbl/COBIL00C.cbl:231`, `app/cbl/COBIL00C.cbl:263`, `app/cbl/COBIL00C.cbl:264`, ...; COTRN00C (1): `app/cbl/COTRN00C.cbl:384` |
| WS-TIMESTAMP-DT-YYYY | 43 | COTRN00C (1): `app/cbl/COTRN00C.cbl:385` |
| WS-TIMESTAMP-DT-MM | 45 | COTRN00C (1): `app/cbl/COTRN00C.cbl:386` |
| WS-TIMESTAMP-DT-DD | 47 | COTRN00C (1): `app/cbl/COTRN00C.cbl:387` |
| WS-TIMESTAMP-TM-MS6 | 55 | COBIL00C (1): `app/cbl/COBIL00C.cbl:266` |

Named in no procedure statement of the copying programs (may still be moved as part of a group): WS-DATE-TIME (line 17), WS-CURDATE (line 19), WS-CURTIME (line 24), WS-CURTIME-MILSEC (line 28), WS-CURTIME-N (line 29), WS-TIMESTAMP-TM-HH (line 49), WS-TIMESTAMP-TM-MM (line 51), WS-TIMESTAMP-TM-SS (line 53).

## Key fields

| Field | Meaning | Source |
|---|---|---|
| WS-CURDATE-DATA | Receives FUNCTION CURRENT-DATE: date CCYYMMDD followed by time HHMMSShh. | `app/cpy/CSDAT01Y.cpy:18-29` |
| WS-CURDATE-MM-DD-YY | Display date MM/DD/YY moved to the screen header. | `app/cpy/CSDAT01Y.cpy:30-35` |
| WS-CURTIME-HH-MM-SS | Display time HH:MM:SS moved to the screen header. | `app/cpy/CSDAT01Y.cpy:36-41` |
| WS-TIMESTAMP | YYYY-MM-DD HH:MM:SS.ffffff timestamp layout; not referenced by COACTUPC. | `app/cpy/CSDAT01Y.cpy:42-55` |

## Sources

- `app/cpy/CSDAT01Y.cpy`
- `docs/_work/structure/copybooks/CSDAT01Y.json`
- `docs/_work/layouts/CSDAT01Y.json`
- `docs/_work/semantic/copybooks/CSDAT01Y.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
