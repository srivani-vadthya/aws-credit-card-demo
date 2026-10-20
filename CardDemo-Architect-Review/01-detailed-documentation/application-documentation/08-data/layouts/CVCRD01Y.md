# Layout CVCRD01Y

| Item | Value |
|---|---|
| Source | `app/cpy/CVCRD01Y.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 46 |
| Data items | 14 (88-levels: 17) |
| Semantic analysis | validated (batch B04) |

## Purpose

Defines CC-WORK-AREAS, the common working storage of the card and account online programs: the normalized attention key CCARD-AID with its 88-levels, next program/mapset/map, error and return message areas, and the account, card and customer ids keyed on the screen. COACTUPC uses CCARD-AID for key handling, CC-ACCT-ID as the account key and CCARD-ERROR-MSG for the error message. (Confirmed)

Evidence: `app/cpy/CVCRD01Y.cpy:1-41`, `app/cbl/COACTUPC.cbl:905-916`, `app/cbl/COACTUPC.cbl:1051-1058`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | CC-WORK-AREAS |  |  | 1 | 213 | 213 |  |  |  | 1 |
| 05 | &nbsp;&nbsp;CC-WORK-AREA |  |  | 1 | 213 | 213 |  |  |  | 2 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CCARD-AID | X(5) | DISPLAY | 1 | 5 | 5 |  |  |  | 3 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CCARD-NEXT-PROG | X(8) | DISPLAY | 6 | 13 | 8 |  |  |  | 21 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CCARD-NEXT-MAPSET | X(7) | DISPLAY | 14 | 20 | 7 |  |  |  | 23 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CCARD-NEXT-MAP | X(7) | DISPLAY | 21 | 27 | 7 |  |  |  | 24 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CCARD-ERROR-MSG | X(75) | DISPLAY | 28 | 102 | 75 |  |  |  | 28 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CCARD-RETURN-MSG | X(75) | DISPLAY | 103 | 177 | 75 |  |  |  | 29 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CC-ACCT-ID | X(11) | DISPLAY | 178 | 188 | 11 |  |  | SPACES | 34 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CC-ACCT-ID-N | 9(11) | DISPLAY | 178 | 188 | 11 |  | CC-ACCT-ID |  | 36 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CC-CARD-NUM | X(16) | DISPLAY | 189 | 204 | 16 |  |  | SPACES | 37 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CC-CARD-NUM-N | 9(16) | DISPLAY | 189 | 204 | 16 |  | CC-CARD-NUM |  | 39 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CC-CUST-ID | X(09) | DISPLAY | 205 | 213 | 9 |  |  | SPACES | 40 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CC-CUST-ID-N | 9(9) | DISPLAY | 205 | 213 | 9 |  | CC-CUST-ID |  | 42 |

## Level-88 conditions

| Field | Condition | Values | Line |
|---|---|---|---|
| CCARD-AID | CCARD-AID-ENTER | 'ENTER' | 4 |
| CCARD-AID | CCARD-AID-CLEAR | 'CLEAR' | 5 |
| CCARD-AID | CCARD-AID-PA1 | 'PA1 ' | 6 |
| CCARD-AID | CCARD-AID-PA2 | 'PA2 ' | 7 |
| CCARD-AID | CCARD-AID-PFK01 | 'PFK01' | 8 |
| CCARD-AID | CCARD-AID-PFK02 | 'PFK02' | 9 |
| CCARD-AID | CCARD-AID-PFK03 | 'PFK03' | 10 |
| CCARD-AID | CCARD-AID-PFK04 | 'PFK04' | 11 |
| CCARD-AID | CCARD-AID-PFK05 | 'PFK05' | 12 |
| CCARD-AID | CCARD-AID-PFK06 | 'PFK06' | 13 |
| CCARD-AID | CCARD-AID-PFK07 | 'PFK07' | 14 |
| CCARD-AID | CCARD-AID-PFK08 | 'PFK08' | 15 |
| CCARD-AID | CCARD-AID-PFK09 | 'PFK09' | 16 |
| CCARD-AID | CCARD-AID-PFK10 | 'PFK10' | 17 |
| CCARD-AID | CCARD-AID-PFK11 | 'PFK11' | 18 |
| CCARD-AID | CCARD-AID-PFK12 | 'PFK12' | 19 |
| CCARD-RETURN-MSG | CCARD-RETURN-MSG-OFF | LOW-VALUES | 30 |

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [COTRTLIC](../../07-programs/COTRTLIC.md) | cobol-program | COPY | active |  | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:327` |
| [COTRTUPC](../../07-programs/COTRTUPC.md) | cobol-program | COPY | active |  | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:241` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active |  | `app/cbl/COACTUPC.cbl:597` |
| [COACTVWC](../../07-programs/COACTVWC.md) | cobol-program | COPY | active |  | `app/cbl/COACTVWC.cbl:207` |
| [COCRDLIC](../../07-programs/COCRDLIC.md) | cobol-program | COPY | active |  | `app/cbl/COCRDLIC.cbl:221` |
| [COCRDSLC](../../07-programs/COCRDSLC.md) | cobol-program | COPY | active |  | `app/cbl/COCRDSLC.cbl:194` |
| [COCRDUPC](../../07-programs/COCRDUPC.md) | cobol-program | COPY | active |  | `app/cbl/COCRDUPC.cbl:268` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| CC-WORK-AREA | 2 | COACTUPC (1): `app/cbl/COACTUPC.cbl:866`; COACTVWC (1): `app/cbl/COACTVWC.cbl:268`; COCRDLIC (1): `app/cbl/COCRDLIC.cbl:300`; COCRDSLC (1): `app/cbl/COCRDSLC.cbl:254`; COCRDUPC (1): `app/cbl/COCRDUPC.cbl:374`; COTRTLIC (1): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:500`; COTRTUPC (1): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:352` |
| CCARD-AID-ENTER | 4 | COACTUPC (3): `app/cbl/COACTUPC.cbl:906`, `app/cbl/COACTUPC.cbl:915`, `app/cpy/CSSTRPFY.cpy:23`; COACTVWC (3): `app/cbl/COACTVWC.cbl:307`, `app/cbl/COACTVWC.cbl:313`, `app/cpy/CSSTRPFY.cpy:23`; COCRDLIC (5): `app/cbl/COCRDLIC.cbl:371`, `app/cbl/COCRDLIC.cbl:379`, `app/cbl/COCRDLIC.cbl:517`, ...; COCRDSLC (3): `app/cbl/COCRDSLC.cbl:292`, `app/cbl/COCRDSLC.cbl:298`, `app/cpy/CSSTRPFY.cpy:23`; COCRDUPC (3): `app/cbl/COCRDUPC.cbl:414`, `app/cbl/COCRDUPC.cbl:423`, `app/cpy/CSSTRPFY.cpy:23`; COTRTLIC (9): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:550`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:575`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:586`, ...; COTRTUPC (2): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:583`, `app/cpy/CSSTRPFY.cpy:23` |
| CCARD-AID-CLEAR | 5 | COACTUPC (1): `app/cpy/CSSTRPFY.cpy:25`; COACTVWC (1): `app/cpy/CSSTRPFY.cpy:25`; COCRDLIC (1): `app/cpy/CSSTRPFY.cpy:25`; COCRDSLC (1): `app/cpy/CSSTRPFY.cpy:25`; COCRDUPC (1): `app/cpy/CSSTRPFY.cpy:25`; COTRTLIC (1): `app/cpy/CSSTRPFY.cpy:25`; COTRTUPC (1): `app/cpy/CSSTRPFY.cpy:25` |
| CCARD-AID-PA1 | 6 | COACTUPC (1): `app/cpy/CSSTRPFY.cpy:27`; COACTVWC (1): `app/cpy/CSSTRPFY.cpy:27`; COCRDLIC (1): `app/cpy/CSSTRPFY.cpy:27`; COCRDSLC (1): `app/cpy/CSSTRPFY.cpy:27`; COCRDUPC (1): `app/cpy/CSSTRPFY.cpy:27`; COTRTLIC (1): `app/cpy/CSSTRPFY.cpy:27`; COTRTUPC (1): `app/cpy/CSSTRPFY.cpy:27` |
| CCARD-AID-PA2 | 7 | COACTUPC (1): `app/cpy/CSSTRPFY.cpy:29`; COACTVWC (1): `app/cpy/CSSTRPFY.cpy:29`; COCRDLIC (1): `app/cpy/CSSTRPFY.cpy:29`; COCRDSLC (1): `app/cpy/CSSTRPFY.cpy:29`; COCRDUPC (1): `app/cpy/CSSTRPFY.cpy:29`; COTRTLIC (1): `app/cpy/CSSTRPFY.cpy:29`; COTRTUPC (1): `app/cpy/CSSTRPFY.cpy:29` |
| CCARD-AID-PFK01 | 8 | COACTUPC (2): `app/cpy/CSSTRPFY.cpy:31`, `app/cpy/CSSTRPFY.cpy:55`; COACTVWC (2): `app/cpy/CSSTRPFY.cpy:31`, `app/cpy/CSSTRPFY.cpy:55`; COCRDLIC (2): `app/cpy/CSSTRPFY.cpy:31`, `app/cpy/CSSTRPFY.cpy:55`; COCRDSLC (2): `app/cpy/CSSTRPFY.cpy:31`, `app/cpy/CSSTRPFY.cpy:55`; COCRDUPC (2): `app/cpy/CSSTRPFY.cpy:31`, `app/cpy/CSSTRPFY.cpy:55`; COTRTLIC (2): `app/cpy/CSSTRPFY.cpy:31`, `app/cpy/CSSTRPFY.cpy:55`; COTRTUPC (2): `app/cpy/CSSTRPFY.cpy:31`, `app/cpy/CSSTRPFY.cpy:55` |
| CCARD-AID-PFK02 | 9 | COACTUPC (2): `app/cpy/CSSTRPFY.cpy:33`, `app/cpy/CSSTRPFY.cpy:57`; COACTVWC (2): `app/cpy/CSSTRPFY.cpy:33`, `app/cpy/CSSTRPFY.cpy:57`; COCRDLIC (2): `app/cpy/CSSTRPFY.cpy:33`, `app/cpy/CSSTRPFY.cpy:57`; COCRDSLC (2): `app/cpy/CSSTRPFY.cpy:33`, `app/cpy/CSSTRPFY.cpy:57`; COCRDUPC (2): `app/cpy/CSSTRPFY.cpy:33`, `app/cpy/CSSTRPFY.cpy:57`; COTRTLIC (4): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:576`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:630`, `app/cpy/CSSTRPFY.cpy:33`, ...; COTRTUPC (2): `app/cpy/CSSTRPFY.cpy:33`, `app/cpy/CSSTRPFY.cpy:57` |
| CCARD-AID-PFK03 | 10 | COACTUPC (5): `app/cbl/COACTUPC.cbl:907`, `app/cbl/COACTUPC.cbl:927`, `app/cbl/COACTUPC.cbl:928`, ...; COACTVWC (4): `app/cbl/COACTVWC.cbl:308`, `app/cbl/COACTVWC.cbl:324`, `app/cpy/CSSTRPFY.cpy:35`, ...; COCRDLIC (5): `app/cbl/COCRDLIC.cbl:372`, `app/cbl/COCRDLIC.cbl:384`, `app/cbl/COCRDLIC.cbl:458`, ...; COCRDSLC (4): `app/cbl/COCRDSLC.cbl:293`, `app/cbl/COCRDSLC.cbl:305`, `app/cpy/CSSTRPFY.cpy:35`, ...; COCRDUPC (5): `app/cbl/COCRDUPC.cbl:415`, `app/cbl/COCRDUPC.cbl:435`, `app/cbl/COCRDUPC.cbl:440`, ...; COTRTLIC (6): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:546`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:577`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:591`, ...; COTRTUPC (4): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:429`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:582`, `app/cpy/CSSTRPFY.cpy:35`, ... |
| CCARD-AID-PFK04 | 11 | COACTUPC (2): `app/cpy/CSSTRPFY.cpy:37`, `app/cpy/CSSTRPFY.cpy:61`; COACTVWC (2): `app/cpy/CSSTRPFY.cpy:37`, `app/cpy/CSSTRPFY.cpy:61`; COCRDLIC (2): `app/cpy/CSSTRPFY.cpy:37`, `app/cpy/CSSTRPFY.cpy:61`; COCRDSLC (2): `app/cpy/CSSTRPFY.cpy:37`, `app/cpy/CSSTRPFY.cpy:61`; COCRDUPC (2): `app/cpy/CSSTRPFY.cpy:37`, `app/cpy/CSSTRPFY.cpy:61`; COTRTLIC (2): `app/cpy/CSSTRPFY.cpy:37`, `app/cpy/CSSTRPFY.cpy:61`; COTRTUPC (5): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:482`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:493`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:584`, ... |
| CCARD-AID-PFK05 | 12 | COACTUPC (4): `app/cbl/COACTUPC.cbl:908`, `app/cbl/COACTUPC.cbl:2603`, `app/cpy/CSSTRPFY.cpy:39`, ...; COACTVWC (2): `app/cpy/CSSTRPFY.cpy:39`, `app/cpy/CSSTRPFY.cpy:63`; COCRDLIC (2): `app/cpy/CSSTRPFY.cpy:39`, `app/cpy/CSSTRPFY.cpy:63`; COCRDSLC (2): `app/cpy/CSSTRPFY.cpy:39`, `app/cpy/CSSTRPFY.cpy:63`; COCRDUPC (4): `app/cbl/COCRDUPC.cbl:416`, `app/cbl/COCRDUPC.cbl:989`, `app/cpy/CSSTRPFY.cpy:39`, ...; COTRTLIC (2): `app/cpy/CSSTRPFY.cpy:39`, `app/cpy/CSSTRPFY.cpy:63`; COTRTUPC (8): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:503`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:514`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:588`, ... |
| CCARD-AID-PFK06 | 13 | COACTUPC (2): `app/cpy/CSSTRPFY.cpy:41`, `app/cpy/CSSTRPFY.cpy:65`; COACTVWC (2): `app/cpy/CSSTRPFY.cpy:41`, `app/cpy/CSSTRPFY.cpy:65`; COCRDLIC (2): `app/cpy/CSSTRPFY.cpy:41`, `app/cpy/CSSTRPFY.cpy:65`; COCRDSLC (2): `app/cpy/CSSTRPFY.cpy:41`, `app/cpy/CSSTRPFY.cpy:65`; COCRDUPC (2): `app/cpy/CSSTRPFY.cpy:41`, `app/cpy/CSSTRPFY.cpy:65`; COTRTLIC (2): `app/cpy/CSSTRPFY.cpy:41`, `app/cpy/CSSTRPFY.cpy:65`; COTRTUPC (2): `app/cpy/CSSTRPFY.cpy:41`, `app/cpy/CSSTRPFY.cpy:65` |
| CCARD-AID-PFK07 | 14 | COACTUPC (2): `app/cpy/CSSTRPFY.cpy:43`, `app/cpy/CSSTRPFY.cpy:67`; COACTVWC (2): `app/cpy/CSSTRPFY.cpy:43`, `app/cpy/CSSTRPFY.cpy:67`; COCRDLIC (7): `app/cbl/COCRDLIC.cbl:373`, `app/cbl/COCRDLIC.cbl:439`, `app/cbl/COCRDLIC.cbl:444`, ...; COCRDSLC (2): `app/cpy/CSSTRPFY.cpy:43`, `app/cpy/CSSTRPFY.cpy:67`; COCRDUPC (2): `app/cpy/CSSTRPFY.cpy:43`, `app/cpy/CSSTRPFY.cpy:67`; COTRTLIC (8): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:578`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:721`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:726`, ...; COTRTUPC (2): `app/cpy/CSSTRPFY.cpy:43`, `app/cpy/CSSTRPFY.cpy:67` |
| CCARD-AID-PFK08 | 15 | COACTUPC (2): `app/cpy/CSSTRPFY.cpy:45`, `app/cpy/CSSTRPFY.cpy:69`; COACTVWC (2): `app/cpy/CSSTRPFY.cpy:45`, `app/cpy/CSSTRPFY.cpy:69`; COCRDLIC (7): `app/cbl/COCRDLIC.cbl:374`, `app/cbl/COCRDLIC.cbl:410`, `app/cbl/COCRDLIC.cbl:486`, ...; COCRDSLC (2): `app/cpy/CSSTRPFY.cpy:45`, `app/cpy/CSSTRPFY.cpy:69`; COCRDUPC (2): `app/cpy/CSSTRPFY.cpy:45`, `app/cpy/CSSTRPFY.cpy:69`; COTRTLIC (10): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:579`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:657`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:766`, ...; COTRTUPC (2): `app/cpy/CSSTRPFY.cpy:45`, `app/cpy/CSSTRPFY.cpy:69` |
| CCARD-AID-PFK09 | 16 | COACTUPC (2): `app/cpy/CSSTRPFY.cpy:47`, `app/cpy/CSSTRPFY.cpy:71`; COACTVWC (2): `app/cpy/CSSTRPFY.cpy:47`, `app/cpy/CSSTRPFY.cpy:71`; COCRDLIC (2): `app/cpy/CSSTRPFY.cpy:47`, `app/cpy/CSSTRPFY.cpy:71`; COCRDSLC (2): `app/cpy/CSSTRPFY.cpy:47`, `app/cpy/CSSTRPFY.cpy:71`; COCRDUPC (2): `app/cpy/CSSTRPFY.cpy:47`, `app/cpy/CSSTRPFY.cpy:71`; COTRTLIC (2): `app/cpy/CSSTRPFY.cpy:47`, `app/cpy/CSSTRPFY.cpy:71`; COTRTUPC (2): `app/cpy/CSSTRPFY.cpy:47`, `app/cpy/CSSTRPFY.cpy:71` |
| CCARD-AID-PFK10 | 17 | COACTUPC (2): `app/cpy/CSSTRPFY.cpy:49`, `app/cpy/CSSTRPFY.cpy:73`; COACTVWC (2): `app/cpy/CSSTRPFY.cpy:49`, `app/cpy/CSSTRPFY.cpy:73`; COCRDLIC (2): `app/cpy/CSSTRPFY.cpy:49`, `app/cpy/CSSTRPFY.cpy:73`; COCRDSLC (2): `app/cpy/CSSTRPFY.cpy:49`, `app/cpy/CSSTRPFY.cpy:73`; COCRDUPC (2): `app/cpy/CSSTRPFY.cpy:49`, `app/cpy/CSSTRPFY.cpy:73`; COTRTLIC (7): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:580`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:581`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:666`, ...; COTRTUPC (2): `app/cpy/CSSTRPFY.cpy:49`, `app/cpy/CSSTRPFY.cpy:73` |
| CCARD-AID-PFK11 | 18 | COACTUPC (2): `app/cpy/CSSTRPFY.cpy:51`, `app/cpy/CSSTRPFY.cpy:75`; COACTVWC (2): `app/cpy/CSSTRPFY.cpy:51`, `app/cpy/CSSTRPFY.cpy:75`; COCRDLIC (2): `app/cpy/CSSTRPFY.cpy:51`, `app/cpy/CSSTRPFY.cpy:75`; COCRDSLC (2): `app/cpy/CSSTRPFY.cpy:51`, `app/cpy/CSSTRPFY.cpy:75`; COCRDUPC (2): `app/cpy/CSSTRPFY.cpy:51`, `app/cpy/CSSTRPFY.cpy:75`; COTRTLIC (2): `app/cpy/CSSTRPFY.cpy:51`, `app/cpy/CSSTRPFY.cpy:75`; COTRTUPC (2): `app/cpy/CSSTRPFY.cpy:51`, `app/cpy/CSSTRPFY.cpy:75` |
| CCARD-AID-PFK12 | 19 | COACTUPC (4): `app/cbl/COACTUPC.cbl:910`, `app/cbl/COACTUPC.cbl:2572`, `app/cpy/CSSTRPFY.cpy:53`, ...; COACTVWC (2): `app/cpy/CSSTRPFY.cpy:53`, `app/cpy/CSSTRPFY.cpy:77`; COCRDLIC (2): `app/cpy/CSSTRPFY.cpy:53`, `app/cpy/CSSTRPFY.cpy:77`; COCRDSLC (2): `app/cpy/CSSTRPFY.cpy:53`, `app/cpy/CSSTRPFY.cpy:77`; COCRDUPC (5): `app/cbl/COCRDUPC.cbl:418`, `app/cbl/COCRDUPC.cbl:484`, `app/cbl/COCRDUPC.cbl:958`, ...; COTRTLIC (2): `app/cpy/CSSTRPFY.cpy:53`, `app/cpy/CSSTRPFY.cpy:77`; COTRTUPC (7): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:406`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:524`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:594`, ... |
| CCARD-NEXT-PROG | 21 | COACTUPC (1): `app/cbl/COACTUPC.cbl:1031`; COACTVWC (1): `app/cbl/COACTVWC.cbl:602`; COCRDLIC (7): `app/cbl/COCRDLIC.cbl:428`, `app/cbl/COCRDLIC.cbl:526`, `app/cbl/COCRDLIC.cbl:539`, ...; COCRDSLC (1): `app/cbl/COCRDSLC.cbl:588`; COCRDUPC (1): `app/cbl/COCRDUPC.cbl:570`; COTRTLIC (3): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:708`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:888`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:895`; COTRTUPC (1): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:633` |
| CCARD-NEXT-MAPSET | 23 | COACTUPC (3): `app/cbl/COACTUPC.cbl:1032`, `app/cbl/COACTUPC.cbl:3591`, `app/cbl/COACTUPC.cbl:3595`; COACTVWC (3): `app/cbl/COACTVWC.cbl:579`, `app/cbl/COACTVWC.cbl:584`, `app/cbl/COACTVWC.cbl:603`; COCRDLIC (5): `app/cbl/COCRDLIC.cbl:394`, `app/cbl/COCRDLIC.cbl:429`, `app/cbl/COCRDLIC.cbl:528`, ...; COCRDSLC (3): `app/cbl/COCRDSLC.cbl:565`, `app/cbl/COCRDSLC.cbl:570`, `app/cbl/COCRDSLC.cbl:589`; COCRDUPC (3): `app/cbl/COCRDUPC.cbl:571`, `app/cbl/COCRDUPC.cbl:1326`, `app/cbl/COCRDUPC.cbl:1330`; COTRTLIC (3): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:640`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:709`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:889`; COTRTUPC (3): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:634`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1430`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1434` |
| CCARD-NEXT-MAP | 24 | COACTUPC (3): `app/cbl/COACTUPC.cbl:1033`, `app/cbl/COACTUPC.cbl:3592`, `app/cbl/COACTUPC.cbl:3594`; COACTVWC (3): `app/cbl/COACTVWC.cbl:580`, `app/cbl/COACTVWC.cbl:583`, `app/cbl/COACTVWC.cbl:604`; COCRDLIC (5): `app/cbl/COCRDLIC.cbl:395`, `app/cbl/COCRDLIC.cbl:430`, `app/cbl/COCRDLIC.cbl:529`, ...; COCRDSLC (3): `app/cbl/COCRDSLC.cbl:566`, `app/cbl/COCRDSLC.cbl:569`, `app/cbl/COCRDSLC.cbl:590`; COCRDUPC (3): `app/cbl/COCRDUPC.cbl:572`, `app/cbl/COCRDUPC.cbl:1327`, `app/cbl/COCRDUPC.cbl:1329`; COTRTLIC (3): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:641`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:710`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:890`; COTRTUPC (3): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:635`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1431`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1433` |
| CCARD-ERROR-MSG | 28 | COACTUPC (2): `app/cbl/COACTUPC.cbl:1008`, `app/cbl/COACTUPC.cbl:1030`; COACTVWC (3): `app/cbl/COACTVWC.cbl:388`, `app/cbl/COACTVWC.cbl:395`, `app/cbl/COACTVWC.cbl:601`; COCRDLIC (2): `app/cbl/COCRDLIC.cbl:423`, `app/cbl/COCRDLIC.cbl:587`; COCRDSLC (3): `app/cbl/COCRDSLC.cbl:387`, `app/cbl/COCRDSLC.cbl:395`, `app/cbl/COCRDSLC.cbl:587`; COCRDUPC (2): `app/cbl/COCRDUPC.cbl:547`, `app/cbl/COCRDUPC.cbl:569`; COTRTLIC (2): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:703`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:883`; COTRTUPC (2): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:560`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:632` |
| CC-ACCT-ID | 34 | COACTUPC (10): `app/cbl/COACTUPC.cbl:1053`, `app/cbl/COACTUPC.cbl:1056`, `app/cbl/COACTUPC.cbl:1787`, ...; COACTVWC (8): `app/cbl/COACTVWC.cbl:468`, `app/cbl/COACTVWC.cbl:630`, `app/cbl/COACTVWC.cbl:632`, ...; COCRDLIC (7): `app/cbl/COCRDLIC.cbl:847`, `app/cbl/COCRDLIC.cbl:969`, `app/cbl/COCRDLIC.cbl:1007`, ...; COCRDSLC (7): `app/cbl/COCRDSLC.cbl:465`, `app/cbl/COCRDSLC.cbl:617`, `app/cbl/COCRDSLC.cbl:619`, ...; COCRDUPC (8): `app/cbl/COCRDUPC.cbl:591`, `app/cbl/COCRDUPC.cbl:594`, `app/cbl/COCRDUPC.cbl:725`, ... |
| CC-ACCT-ID-N | 36 | COACTUPC (3): `app/cbl/COACTUPC.cbl:1803`, `app/cbl/COACTUPC.cbl:2703`, `app/cbl/COACTUPC.cbl:2712`; COCRDLIC (1): `app/cbl/COCRDLIC.cbl:1009`; COCRDSLC (2): `app/cbl/COCRDSLC.cbl:342`, `app/cbl/COCRDSLC.cbl:653`; COCRDUPC (4): `app/cbl/COCRDUPC.cbl:490`, `app/cbl/COCRDUPC.cbl:727`, `app/cbl/COCRDUPC.cbl:1087`, ... |
| CC-CARD-NUM | 37 | COCRDLIC (5): `app/cbl/COCRDLIC.cbl:859`, `app/cbl/COCRDLIC.cbl:970`, `app/cbl/COCRDLIC.cbl:1042`, ...; COCRDSLC (7): `app/cbl/COCRDSLC.cbl:471`, `app/cbl/COCRDSLC.cbl:624`, `app/cbl/COCRDSLC.cbl:626`, ...; COCRDUPC (10): `app/cbl/COCRDUPC.cbl:600`, `app/cbl/COCRDUPC.cbl:603`, `app/cbl/COCRDUPC.cbl:768`, ... |
| CC-CARD-NUM-N | 39 | COCRDLIC (3): `app/cbl/COCRDLIC.cbl:1044`, `app/cbl/COCRDLIC.cbl:1064`, `app/cbl/COCRDLIC.cbl:1397`; COCRDSLC (3): `app/cbl/COCRDSLC.cbl:343`, `app/cbl/COCRDSLC.cbl:693`, `app/cbl/COCRDSLC.cbl:717`; COCRDUPC (4): `app/cbl/COCRDUPC.cbl:491`, `app/cbl/COCRDUPC.cbl:770`, `app/cbl/COCRDUPC.cbl:796`, ... |

Named in no procedure statement of the copying programs (may still be moved as part of a group): CC-WORK-AREAS (line 1), CCARD-AID (line 3), CCARD-RETURN-MSG (line 29), CCARD-RETURN-MSG-OFF (line 30), CC-CUST-ID (line 40), CC-CUST-ID-N (line 42).

## Key fields

| Field | Meaning | Source |
|---|---|---|
| CC-WORK-AREA | Common card/account work area initialized at task start. | `app/cpy/CVCRD01Y.cpy:2` |
| CCARD-AID | Normalized attention key with 88-levels CCARD-AID-ENTER, -CLEAR, -PA1, -PA2 and -PFK01..-PFK12, set by YYYY-STORE-PFKEY. | `app/cpy/CVCRD01Y.cpy:3-19` |
| CCARD-AID-PFK05 | PF5; COACTUPC uses it as the save confirmation key. | `app/cpy/CVCRD01Y.cpy:12` |
| CCARD-AID-PFK12 | PF12; COACTUPC uses it to cancel changes and re-read the account. | `app/cpy/CVCRD01Y.cpy:19` |
| CCARD-NEXT-PROG | Next program name recorded by the screen handler. | `app/cpy/CVCRD01Y.cpy:21` |
| CCARD-ERROR-MSG | 75-byte error message area; COACTUPC copies WS-RETURN-MSG here. | `app/cpy/CVCRD01Y.cpy:28` |
| CC-ACCT-ID | 11-character account id entered on the screen, with numeric redefinition CC-ACCT-ID-N; key for the cross-reference and account reads. | `app/cpy/CVCRD01Y.cpy:34-36` |
| CC-CARD-NUM | 16-character card number with numeric redefinition; not referenced by COACTUPC. | `app/cpy/CVCRD01Y.cpy:37-39` |
| CC-CUST-ID | 9-character customer id with numeric redefinition; not referenced by COACTUPC. | `app/cpy/CVCRD01Y.cpy:40-41` |

## Observations

- dead-code: Several former fields (CCARD-LAST-PROG, CCARD-RETURN-TO-PROG, CCARD-RETURN-FLAG, CCARD-FUNCTION) are commented out; the lines carry sequence numbers in columns 1-6 and 73-80. (`app/cpy/CVCRD01Y.cpy:20-33`)

## Sources

- `app/cpy/CVCRD01Y.cpy`
- `docs/_work/structure/copybooks/CVCRD01Y.json`
- `docs/_work/layouts/CVCRD01Y.json`
- `docs/_work/semantic/copybooks/CVCRD01Y.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
