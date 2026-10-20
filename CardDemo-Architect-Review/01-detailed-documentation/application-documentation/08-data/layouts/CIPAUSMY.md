# Layout CIPAUSMY

| Item | Value |
|---|---|
| Source | `app/app-authorization-ims-db2-mq/cpy/CIPAUSMY.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 31 |
| Data items | 13 (88-levels: 0) |
| Semantic analysis | validated (batch B01) |

## Purpose

Defines the 100-byte IMS pending authorization summary root segment PAUTSUM0 (one per account), copied under 01 PENDING-AUTH-SUMMARY. It holds the account and customer ids, account status codes, credit and cash limits and balances, and running counts and amounts of approved and declined authorizations. COPAUA0C creates and updates it per authorization, COPAUS0C/COPAUS1C read it for display, CBPAUP0C reduces/deletes it when purging expired details, and PAUDBUNL/DBUNLDGS/PAUDBLOD unload and reload it. (Confirmed)

Evidence: `app/app-authorization-ims-db2-mq/cpy/CIPAUSMY.cpy:1-31`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:798-834`, `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:286-292`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 05 | &nbsp;&nbsp;PA-ACCT-ID | S9(11) | COMP-3 | 1 | 6 | 6 |  |  |  | 19 |
| 05 | &nbsp;&nbsp;PA-CUST-ID | 9(09) | DISPLAY | 7 | 15 | 9 |  |  |  | 20 |
| 05 | &nbsp;&nbsp;PA-AUTH-STATUS | X(01) | DISPLAY | 16 | 16 | 1 |  |  |  | 21 |
| 05 | &nbsp;&nbsp;PA-ACCOUNT-STATUS | X(02) | DISPLAY | 17 | 26 | 10 | 5 |  |  | 22 |
| 05 | &nbsp;&nbsp;PA-CREDIT-LIMIT | S9(09)V99 | COMP-3 | 27 | 32 | 6 |  |  |  | 23 |
| 05 | &nbsp;&nbsp;PA-CASH-LIMIT | S9(09)V99 | COMP-3 | 33 | 38 | 6 |  |  |  | 24 |
| 05 | &nbsp;&nbsp;PA-CREDIT-BALANCE | S9(09)V99 | COMP-3 | 39 | 44 | 6 |  |  |  | 25 |
| 05 | &nbsp;&nbsp;PA-CASH-BALANCE | S9(09)V99 | COMP-3 | 45 | 50 | 6 |  |  |  | 26 |
| 05 | &nbsp;&nbsp;PA-APPROVED-AUTH-CNT | S9(04) | COMP | 51 | 52 | 2 |  |  |  | 27 |
| 05 | &nbsp;&nbsp;PA-DECLINED-AUTH-CNT | S9(04) | COMP | 53 | 54 | 2 |  |  |  | 28 |
| 05 | &nbsp;&nbsp;PA-APPROVED-AUTH-AMT | S9(09)V99 | COMP-3 | 55 | 60 | 6 |  |  |  | 29 |
| 05 | &nbsp;&nbsp;PA-DECLINED-AUTH-AMT | S9(09)V99 | COMP-3 | 61 | 66 | 6 |  |  |  | 30 |
| 05 | &nbsp;&nbsp;FILLER | X(34) | DISPLAY | 67 | 100 | 34 |  |  |  | 31 |

## Level-88 conditions

None.

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [CBPAUP0C](../../07-programs/CBPAUP0C.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:117` |
| [COPAUA0C](../../07-programs/COPAUA0C.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:193` |
| [COPAUS0C](../../07-programs/COPAUS0C.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:161` |
| [COPAUS1C](../../07-programs/COPAUS1C.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:142` |
| [DBUNLDGS](../../07-programs/DBUNLDGS.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:143` |
| [PAUDBLOD](../../07-programs/PAUDBLOD.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:149` |
| [PAUDBUNL](../../07-programs/PAUDBUNL.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:139` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| PA-ACCT-ID | 19 | CBPAUP0C (6): `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:233`, `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:268`, `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:307`, ...; COPAUA0C (5): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:619`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:623`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:805`, ...; COPAUS0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:971`, `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:976`; COPAUS1C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:436`, `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:442`; DBUNLDGS (2): `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:239`, `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:241`; PAUDBUNL (2): `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:230`, `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:232` |
| PA-CUST-ID | 20 | COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:806` |
| PA-CREDIT-LIMIT | 23 | COPAUA0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:666`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:810` |
| PA-CASH-LIMIT | 24 | COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:811` |
| PA-CREDIT-BALANCE | 25 | COPAUA0C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:667`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:817`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:792` |
| PA-CASH-BALANCE | 26 | COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:818`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:794` |
| PA-APPROVED-AUTH-CNT | 27 | CBPAUP0C (2): `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:156`, `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:288`; COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:814`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:788` |
| PA-DECLINED-AUTH-CNT | 28 | CBPAUP0C (1): `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:291`; COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:820`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:790` |
| PA-APPROVED-AUTH-AMT | 29 | CBPAUP0C (1): `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:289`; COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:815`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:796` |
| PA-DECLINED-AUTH-AMT | 30 | CBPAUP0C (1): `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:292`; COPAUA0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:821`; COPAUS0C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:798` |

Named in no procedure statement of the copying programs (may still be moved as part of a group): PA-AUTH-STATUS (line 21), PA-ACCOUNT-STATUS (line 22).

## Key fields

| Field | Meaning | Source |
|---|---|---|
| PA-ACCT-ID | Account id, packed S9(11); segment key (ACCNTID in DL/I WHERE clauses). | `app/app-authorization-ims-db2-mq/cpy/CIPAUSMY.cpy:19` |
| PA-CUST-ID | Customer id from the card cross-reference. | `app/app-authorization-ims-db2-mq/cpy/CIPAUSMY.cpy:20` |
| PA-ACCOUNT-STATUS | Five 2-byte account status codes (OCCURS 5); not set or tested by any batch B01 program. | `app/app-authorization-ims-db2-mq/cpy/CIPAUSMY.cpy:22` |
| PA-CREDIT-LIMIT | Credit limit, refreshed from ACCT-CREDIT-LIMIT on each authorization; used for available credit. | `app/app-authorization-ims-db2-mq/cpy/CIPAUSMY.cpy:23` |
| PA-CREDIT-BALANCE | Credit balance including approved pending authorizations; available credit = limit - balance. | `app/app-authorization-ims-db2-mq/cpy/CIPAUSMY.cpy:25` |
| PA-APPROVED-AUTH-CNT | Count of approved pending authorizations (binary S9(4)). | `app/app-authorization-ims-db2-mq/cpy/CIPAUSMY.cpy:27` |
| PA-DECLINED-AUTH-CNT | Count of declined authorizations (binary S9(4)). | `app/app-authorization-ims-db2-mq/cpy/CIPAUSMY.cpy:28` |
| PA-APPROVED-AUTH-AMT | Total approved authorization amount. | `app/app-authorization-ims-db2-mq/cpy/CIPAUSMY.cpy:29` |
| PA-DECLINED-AUTH-AMT | Total declined authorization amount. | `app/app-authorization-ims-db2-mq/cpy/CIPAUSMY.cpy:30` |

## Observations

- anomaly: Computed length is 100 bytes (6+9+1+10+4x6+2x2+2x6+34), matching PAUDBUNL/PAUDBLOD OPFIL1-REC/INFIL1-REC PIC X(100). (`app/app-authorization-ims-db2-mq/cpy/CIPAUSMY.cpy:19-31`)
- dead-code: PA-AUTH-STATUS, PA-ACCOUNT-STATUS and PA-CASH-BALANCE (other than being zeroed by COPAUA0C) carry no business logic in the B01 programs. (`app/app-authorization-ims-db2-mq/cpy/CIPAUSMY.cpy:21-26`)

## Sources

- `app/app-authorization-ims-db2-mq/cpy/CIPAUSMY.cpy`
- `docs/_work/structure/copybooks/CIPAUSMY.json`
- `docs/_work/layouts/CIPAUSMY.json`
- `docs/_work/semantic/copybooks/CIPAUSMY.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
