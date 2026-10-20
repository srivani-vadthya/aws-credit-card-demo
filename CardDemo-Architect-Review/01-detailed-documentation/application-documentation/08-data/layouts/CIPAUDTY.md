# Layout CIPAUDTY

| Item | Value |
|---|---|
| Source | `app/app-authorization-ims-db2-mq/cpy/CIPAUDTY.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 54 |
| Data items | 29 (88-levels: 7) |
| Semantic analysis | validated (batch B01) |

## Purpose

Defines the 200-byte IMS pending authorization detail child segment PAUTDTL1 (one per authorization request), copied under 01 PENDING-AUTH-DETAILS and, in COPAUS2C, inside the LINK commarea. It carries the descending date/time key, the original request data (card, type, amounts, merchant), the decision (response code and reason, approved amount), the match status lifecycle and fraud flags. COPAUA0C inserts it, COPAUS0C/COPAUS1C display it, COPAUS1C/COPAUS2C update its fraud fields, CBPAUP0C deletes expired ones, and the unload/load utilities copy it. (Confirmed)

Evidence: `app/app-authorization-ims-db2-mq/cpy/CIPAUDTY.cpy:1-54`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:871-918`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:74-78`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 05 | &nbsp;&nbsp;PA-AUTHORIZATION-KEY |  |  | 1 | 8 | 8 |  |  |  | 19 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;PA-AUTH-DATE-9C | S9(05) | COMP-3 | 1 | 3 | 3 |  |  |  | 20 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;PA-AUTH-TIME-9C | S9(09) | COMP-3 | 4 | 8 | 5 |  |  |  | 21 |
| 05 | &nbsp;&nbsp;PA-AUTH-ORIG-DATE | X(06) | DISPLAY | 9 | 14 | 6 |  |  |  | 22 |
| 05 | &nbsp;&nbsp;PA-AUTH-ORIG-TIME | X(06) | DISPLAY | 15 | 20 | 6 |  |  |  | 23 |
| 05 | &nbsp;&nbsp;PA-CARD-NUM | X(16) | DISPLAY | 21 | 36 | 16 |  |  |  | 24 |
| 05 | &nbsp;&nbsp;PA-AUTH-TYPE | X(04) | DISPLAY | 37 | 40 | 4 |  |  |  | 25 |
| 05 | &nbsp;&nbsp;PA-CARD-EXPIRY-DATE | X(04) | DISPLAY | 41 | 44 | 4 |  |  |  | 26 |
| 05 | &nbsp;&nbsp;PA-MESSAGE-TYPE | X(06) | DISPLAY | 45 | 50 | 6 |  |  |  | 27 |
| 05 | &nbsp;&nbsp;PA-MESSAGE-SOURCE | X(06) | DISPLAY | 51 | 56 | 6 |  |  |  | 28 |
| 05 | &nbsp;&nbsp;PA-AUTH-ID-CODE | X(06) | DISPLAY | 57 | 62 | 6 |  |  |  | 29 |
| 05 | &nbsp;&nbsp;PA-AUTH-RESP-CODE | X(02) | DISPLAY | 63 | 64 | 2 |  |  |  | 30 |
| 05 | &nbsp;&nbsp;PA-AUTH-RESP-REASON | X(04) | DISPLAY | 65 | 68 | 4 |  |  |  | 32 |
| 05 | &nbsp;&nbsp;PA-PROCESSING-CODE | 9(06) | DISPLAY | 69 | 74 | 6 |  |  |  | 33 |
| 05 | &nbsp;&nbsp;PA-TRANSACTION-AMT | S9(10)V99 | COMP-3 | 75 | 81 | 7 |  |  |  | 34 |
| 05 | &nbsp;&nbsp;PA-APPROVED-AMT | S9(10)V99 | COMP-3 | 82 | 88 | 7 |  |  |  | 35 |
| 05 | &nbsp;&nbsp;PA-MERCHANT-CATAGORY-CODE | X(04) | DISPLAY | 89 | 92 | 4 |  |  |  | 36 |
| 05 | &nbsp;&nbsp;PA-ACQR-COUNTRY-CODE | X(03) | DISPLAY | 93 | 95 | 3 |  |  |  | 37 |
| 05 | &nbsp;&nbsp;PA-POS-ENTRY-MODE | 9(02) | DISPLAY | 96 | 97 | 2 |  |  |  | 38 |
| 05 | &nbsp;&nbsp;PA-MERCHANT-ID | X(15) | DISPLAY | 98 | 112 | 15 |  |  |  | 39 |
| 05 | &nbsp;&nbsp;PA-MERCHANT-NAME | X(22) | DISPLAY | 113 | 134 | 22 |  |  |  | 40 |
| 05 | &nbsp;&nbsp;PA-MERCHANT-CITY | X(13) | DISPLAY | 135 | 147 | 13 |  |  |  | 41 |
| 05 | &nbsp;&nbsp;PA-MERCHANT-STATE | X(02) | DISPLAY | 148 | 149 | 2 |  |  |  | 42 |
| 05 | &nbsp;&nbsp;PA-MERCHANT-ZIP | X(09) | DISPLAY | 150 | 158 | 9 |  |  |  | 43 |
| 05 | &nbsp;&nbsp;PA-TRANSACTION-ID | X(15) | DISPLAY | 159 | 173 | 15 |  |  |  | 44 |
| 05 | &nbsp;&nbsp;PA-MATCH-STATUS | X(01) | DISPLAY | 174 | 174 | 1 |  |  |  | 45 |
| 05 | &nbsp;&nbsp;PA-AUTH-FRAUD | X(01) | DISPLAY | 175 | 175 | 1 |  |  |  | 50 |
| 05 | &nbsp;&nbsp;PA-FRAUD-RPT-DATE | X(08) | DISPLAY | 176 | 183 | 8 |  |  |  | 53 |
| 05 | &nbsp;&nbsp;FILLER | X(17) | DISPLAY | 184 | 200 | 17 |  |  |  | 54 |

## Level-88 conditions

| Field | Condition | Values | Line |
|---|---|---|---|
| PA-AUTH-RESP-CODE | PA-AUTH-APPROVED | '00' | 31 |
| PA-MATCH-STATUS | PA-MATCH-PENDING | 'P' | 46 |
| PA-MATCH-STATUS | PA-MATCH-AUTH-DECLINED | 'D' | 47 |
| PA-MATCH-STATUS | PA-MATCH-PENDING-EXPIRED | 'E' | 48 |
| PA-MATCH-STATUS | PA-MATCHED-WITH-TRAN | 'M' | 49 |
| PA-AUTH-FRAUD | PA-FRAUD-CONFIRMED | 'F' | 51 |
| PA-AUTH-FRAUD | PA-FRAUD-REMOVED | 'R' | 52 |

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [CBPAUP0C](../../07-programs/CBPAUP0C.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:121` |
| [COPAUA0C](../../07-programs/COPAUA0C.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:197` |
| [COPAUS0C](../../07-programs/COPAUS0C.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:165` |
| [COPAUS1C](../../07-programs/COPAUS1C.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:146` |
| [COPAUS2C](../../07-programs/COPAUS2C.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:78` |
| [DBUNLDGS](../../07-programs/DBUNLDGS.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:147` |
| [PAUDBLOD](../../07-programs/PAUDBLOD.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:153` |
| [PAUDBUNL](../../07-programs/PAUDBUNL.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:143` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| PA-AUTHORIZATION-KEY | 19 | COPAUS0C (9): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:434`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:439`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:491`, ...; COPAUS1C (4): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:264`, `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:286`, `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:437`, ... |
| PA-AUTH-DATE-9C | 20 | CBPAUP0C (1): `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:280`; COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:874` |
| PA-AUTH-TIME-9C | 21 | COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:875`; COPAUS2C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:107` |
| PA-AUTH-ORIG-DATE | 22 | COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:877`; COPAUS0C (3): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:531`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:532`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:533`; COPAUS1C (3): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:297`, `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:298`, `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:299`; COPAUS2C (3): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:103`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:104`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:105` |
| PA-AUTH-ORIG-TIME | 23 | COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:878`; COPAUS0C (3): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:527`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:528`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:529`; COPAUS1C (3): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:303`, `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:304`, `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:305` |
| PA-CARD-NUM | 24 | COPAUA0C (6): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:428`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:638`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:777`, ...; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:295`; COPAUS2C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:113` |
| PA-AUTH-TYPE | 25 | COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:880`; COPAUS0C (5): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:550`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:562`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:574`, ...; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:340`; COPAUS2C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:115` |
| PA-CARD-EXPIRY-DATE | 26 | COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:881`; COPAUS1C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:336`, `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:338`; COPAUS2C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:116` |
| PA-MESSAGE-TYPE | 27 | COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:882`; COPAUS2C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:117` |
| PA-MESSAGE-SOURCE | 28 | COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:883`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:333`; COPAUS2C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:118` |
| PA-AUTH-ID-CODE | 29 | COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:897`; COPAUS2C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:119` |
| PA-AUTH-RESP-CODE | 30 | CBPAUP0C (1): `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:287`; COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:898`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:536`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:311`; COPAUS2C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:120` |
| PA-AUTH-RESP-REASON | 32 | COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:899`; COPAUS1C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:324`, `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:325`; COPAUS2C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:121` |
| PA-PROCESSING-CODE | 33 | COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:884`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:331`; COPAUS2C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:122` |
| PA-TRANSACTION-AMT | 34 | CBPAUP0C (1): `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:292`; COPAUA0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:821`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:885`; COPAUS2C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:123` |
| PA-APPROVED-AMT | 35 | CBPAUP0C (1): `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:289`; COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:900`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:525`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:308`; COPAUS2C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:124` |
| PA-MERCHANT-CATAGORY-CODE | 36 | COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:887`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:334`; COPAUS2C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:125` |
| PA-ACQR-COUNTRY-CODE | 37 | COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:888`; COPAUS2C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:127` |
| PA-POS-ENTRY-MODE | 38 | COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:889`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:332`; COPAUS2C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:128` |
| PA-MERCHANT-ID | 39 | COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:890`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:353`; COPAUS2C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:129` |
| PA-MERCHANT-NAME | 40 | COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:891`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:352`; COPAUS2C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:130`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:131` |
| PA-MERCHANT-CITY | 41 | COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:892`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:354`; COPAUS2C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:132` |
| PA-MERCHANT-STATE | 42 | COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:893`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:355`; COPAUS2C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:133` |
| PA-MERCHANT-ZIP | 43 | COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:894`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:356`; COPAUS2C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:134` |
| PA-TRANSACTION-ID | 44 | COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:895`; COPAUS0C (5): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:547`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:559`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:571`, ...; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:341`; COPAUS2C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:135` |
| PA-MATCH-STATUS | 45 | COPAUS0C (5): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:552`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:564`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:576`, ...; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:342`; COPAUS2C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:136` |
| PA-MATCH-PENDING | 46 | COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:903` |
| PA-MATCH-AUTH-DECLINED | 47 | COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:905` |
| PA-AUTH-FRAUD | 50 | COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:908`; COPAUS1C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:345` |
| PA-FRAUD-CONFIRMED | 51 | COPAUS1C (3): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:236`, `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:240`, `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:344` |
| PA-FRAUD-REMOVED | 52 | COPAUS1C (3): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:237`, `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:344`, `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:534` |
| PA-FRAUD-RPT-DATE | 53 | COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:909`; COPAUS1C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:347`, `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:523`; COPAUS2C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:101` |

Named in no procedure statement of the copying programs (may still be moved as part of a group): PA-AUTH-APPROVED (line 31), PA-MATCH-PENDING-EXPIRED (line 48), PA-MATCHED-WITH-TRAN (line 49).

## Key fields

| Field | Meaning | Source |
|---|---|---|
| PA-AUTHORIZATION-KEY | 8-byte segment key (PAUT9CTS) composed of complemented date and time so newest sorts first. | `app/app-authorization-ims-db2-mq/cpy/CIPAUDTY.cpy:19-21` |
| PA-AUTH-DATE-9C | 99999 minus YYDDD processing date (set by COPAUA0C, reversed by CBPAUP0C). | `app/app-authorization-ims-db2-mq/cpy/CIPAUDTY.cpy:20` |
| PA-AUTH-TIME-9C | 999999999 minus HHMMSSmmm processing time. | `app/app-authorization-ims-db2-mq/cpy/CIPAUDTY.cpy:21` |
| PA-AUTH-ORIG-DATE | Original request date YYMMDD from the MQ request. | `app/app-authorization-ims-db2-mq/cpy/CIPAUDTY.cpy:22` |
| PA-CARD-NUM | 16-digit card number. | `app/app-authorization-ims-db2-mq/cpy/CIPAUDTY.cpy:24` |
| PA-AUTH-RESP-CODE | Response code; '00' approved, otherwise declined ('05' from COPAUA0C). | `app/app-authorization-ims-db2-mq/cpy/CIPAUDTY.cpy:30` |
| PA-AUTH-APPROVED | 88-level: response code '00'. | `app/app-authorization-ims-db2-mq/cpy/CIPAUDTY.cpy:31` |
| PA-AUTH-RESP-REASON | 4-character decline reason code (3100, 4100, ... 9000; 0000 when approved). | `app/app-authorization-ims-db2-mq/cpy/CIPAUDTY.cpy:32` |
| PA-TRANSACTION-AMT | Requested transaction amount. | `app/app-authorization-ims-db2-mq/cpy/CIPAUDTY.cpy:34` |
| PA-APPROVED-AMT | Approved amount (full request amount or 0). | `app/app-authorization-ims-db2-mq/cpy/CIPAUDTY.cpy:35` |
| PA-MATCH-STATUS | Lifecycle: P pending, D declined, E pending expired, M matched with transaction. | `app/app-authorization-ims-db2-mq/cpy/CIPAUDTY.cpy:45-49` |
| PA-AUTH-FRAUD | Fraud flag: F confirmed, R removed, space none. | `app/app-authorization-ims-db2-mq/cpy/CIPAUDTY.cpy:50-52` |
| PA-FRAUD-RPT-DATE | Date the fraud action was recorded (MM/DD/YY from COPAUS2C). | `app/app-authorization-ims-db2-mq/cpy/CIPAUDTY.cpy:53` |

## Observations

- anomaly: Computed length is 200 bytes, matching CHILD-SEG-REC PIC X(200) in the unload/load programs. (`app/app-authorization-ims-db2-mq/cpy/CIPAUDTY.cpy:19-54`)
- dead-code: 88-levels PA-MATCH-PENDING-EXPIRED ('E') and PA-MATCHED-WITH-TRAN ('M') are never set by any B01 program; CBPAUP0C deletes expired details instead of marking them 'E'. (`app/app-authorization-ims-db2-mq/cpy/CIPAUDTY.cpy:47-49`)
- anomaly: Field name PA-MERCHANT-CATAGORY-CODE is misspelled (CATAGORY); the same spelling is used in DB2 AUTHFRDS. (`app/app-authorization-ims-db2-mq/cpy/CIPAUDTY.cpy:36`)

## Sources

- `app/app-authorization-ims-db2-mq/cpy/CIPAUDTY.cpy`
- `docs/_work/structure/copybooks/CIPAUDTY.json`
- `docs/_work/layouts/CIPAUDTY.json`
- `docs/_work/semantic/copybooks/CIPAUDTY.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
