# Layout AUTHFRDS

| Item | Value |
|---|---|
| Source | `app/app-authorization-ims-db2-mq/dcl/AUTHFRDS.dcl` |
| Type | db2-dclgen |
| Content | data |
| Lines | 89 |
| Data items | 29 (88-levels: 0) |
| Semantic analysis | validated (batch B01) |

## Purpose

DCLGEN for DB2 table CARDDEMO.AUTHFRDS (authorization fraud records): the EXEC SQL DECLARE TABLE with 26 columns and the COBOL host structure DCLAUTHFRDS. It is included by COPAUS2C, which inserts a copy of a pending authorization detail with its fraud flag when a user reports or removes fraud in COPAUS1C, or updates the flag and report date when the row already exists. The primary key per the DDL is (CARD_NUM, AUTH_TS). (Confirmed)

Evidence: `app/app-authorization-ims-db2-mq/dcl/AUTHFRDS.dcl:24-86`, `app/app-authorization-ims-db2-mq/ddl/AUTHFRDS.ddl:1-28`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:68-70`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | DCLAUTHFRDS |  |  | 1 | 204 | 204 |  |  |  | 55 |
| 10 | &nbsp;&nbsp;CARD-NUM | X(16) | DISPLAY | 1 | 16 | 16 |  |  |  | 56 |
| 10 | &nbsp;&nbsp;AUTH-TS | X(26) | DISPLAY | 17 | 42 | 26 |  |  |  | 57 |
| 10 | &nbsp;&nbsp;AUTH-TYPE | X(4) | DISPLAY | 43 | 46 | 4 |  |  |  | 58 |
| 10 | &nbsp;&nbsp;CARD-EXPIRY-DATE | X(4) | DISPLAY | 47 | 50 | 4 |  |  |  | 59 |
| 10 | &nbsp;&nbsp;MESSAGE-TYPE | X(6) | DISPLAY | 51 | 56 | 6 |  |  |  | 60 |
| 10 | &nbsp;&nbsp;MESSAGE-SOURCE | X(6) | DISPLAY | 57 | 62 | 6 |  |  |  | 61 |
| 10 | &nbsp;&nbsp;AUTH-ID-CODE | X(6) | DISPLAY | 63 | 68 | 6 |  |  |  | 62 |
| 10 | &nbsp;&nbsp;AUTH-RESP-CODE | X(2) | DISPLAY | 69 | 70 | 2 |  |  |  | 63 |
| 10 | &nbsp;&nbsp;AUTH-RESP-REASON | X(4) | DISPLAY | 71 | 74 | 4 |  |  |  | 64 |
| 10 | &nbsp;&nbsp;PROCESSING-CODE | X(6) | DISPLAY | 75 | 80 | 6 |  |  |  | 65 |
| 10 | &nbsp;&nbsp;TRANSACTION-AMT | S9(10)V9(2) | COMP-3 | 81 | 87 | 7 |  |  |  | 66 |
| 10 | &nbsp;&nbsp;APPROVED-AMT | S9(10)V9(2) | COMP-3 | 88 | 94 | 7 |  |  |  | 67 |
| 10 | &nbsp;&nbsp;MERCHANT-CATAGORY-CODE | X(4) | DISPLAY | 95 | 98 | 4 |  |  |  | 68 |
| 10 | &nbsp;&nbsp;ACQR-COUNTRY-CODE | X(3) | DISPLAY | 99 | 101 | 3 |  |  |  | 70 |
| 10 | &nbsp;&nbsp;POS-ENTRY-MODE | S9(4) | COMP | 102 | 103 | 2 |  |  |  | 71 |
| 10 | &nbsp;&nbsp;MERCHANT-ID | X(15) | DISPLAY | 104 | 118 | 15 |  |  |  | 72 |
| 10 | &nbsp;&nbsp;MERCHANT-NAME |  |  | 119 | 142 | 24 |  |  |  | 73 |
| 49 | &nbsp;&nbsp;&nbsp;&nbsp;MERCHANT-NAME-LEN | S9(4) | COMP | 119 | 120 | 2 |  |  |  | 74 |
| 49 | &nbsp;&nbsp;&nbsp;&nbsp;MERCHANT-NAME-TEXT | X(22) | DISPLAY | 121 | 142 | 22 |  |  |  | 76 |
| 10 | &nbsp;&nbsp;MERCHANT-CITY | X(13) | DISPLAY | 143 | 155 | 13 |  |  |  | 78 |
| 10 | &nbsp;&nbsp;MERCHANT-STATE | X(2) | DISPLAY | 156 | 157 | 2 |  |  |  | 79 |
| 10 | &nbsp;&nbsp;MERCHANT-ZIP | X(9) | DISPLAY | 158 | 166 | 9 |  |  |  | 80 |
| 10 | &nbsp;&nbsp;TRANSACTION-ID | X(15) | DISPLAY | 167 | 181 | 15 |  |  |  | 81 |
| 10 | &nbsp;&nbsp;MATCH-STATUS | X(1) | DISPLAY | 182 | 182 | 1 |  |  |  | 82 |
| 10 | &nbsp;&nbsp;AUTH-FRAUD | X(1) | DISPLAY | 183 | 183 | 1 |  |  |  | 83 |
| 10 | &nbsp;&nbsp;FRAUD-RPT-DATE | X(10) | DISPLAY | 184 | 193 | 10 |  |  |  | 84 |
| 10 | &nbsp;&nbsp;ACCT-ID | S9(11)V | COMP-3 | 194 | 199 | 6 |  |  |  | 85 |
| 10 | &nbsp;&nbsp;CUST-ID | S9(9)V | COMP-3 | 200 | 204 | 5 |  |  |  | 86 |

## Level-88 conditions

None.

## DB2 table declaration

Table `CARDDEMO.AUTHFRDS` (`app/app-authorization-ims-db2-mq/dcl/AUTHFRDS.dcl:24-51`):

| Column | Type | NOT NULL |
|---|---|---|
| CARD_NUM | CHAR(16) | yes |
| AUTH_TS | TIMESTAMP | yes |
| AUTH_TYPE | CHAR(4) |  |
| CARD_EXPIRY_DATE | CHAR(4) |  |
| MESSAGE_TYPE | CHAR(6) |  |
| MESSAGE_SOURCE | CHAR(6) |  |
| AUTH_ID_CODE | CHAR(6) |  |
| AUTH_RESP_CODE | CHAR(2) |  |
| AUTH_RESP_REASON | CHAR(4) |  |
| PROCESSING_CODE | CHAR(6) |  |
| TRANSACTION_AMT | DECIMAL(12, 2) |  |
| APPROVED_AMT | DECIMAL(12, 2) |  |
| MERCHANT_CATAGORY_CODE | CHAR(4) |  |
| ACQR_COUNTRY_CODE | CHAR(3) |  |
| POS_ENTRY_MODE | SMALLINT |  |
| MERCHANT_ID | CHAR(15) |  |
| MERCHANT_NAME | VARCHAR(22) |  |
| MERCHANT_CITY | CHAR(13) |  |
| MERCHANT_STATE | CHAR(2) |  |
| MERCHANT_ZIP | CHAR(9) |  |
| TRANSACTION_ID | CHAR(15) |  |
| MATCH_STATUS | CHAR(1) |  |
| AUTH_FRAUD | CHAR(1) |  |
| FRAUD_RPT_DATE | DATE |  |
| ACCT_ID | DECIMAL(11, 0) |  |
| CUST_ID | DECIMAL(9, 0) |  |

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [COPAUS2C](../../07-programs/COPAUS2C.md) | cobol-program | EXEC SQL INCLUDE | active |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:68-70` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| CARD-NUM | 56 | COPAUS2C (3): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:113`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:170`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:226` |
| AUTH-TS | 57 | COPAUS2C (3): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:114`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:171`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:227` |
| AUTH-TYPE | 58 | COPAUS2C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:115`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:173` |
| CARD-EXPIRY-DATE | 59 | COPAUS2C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:116`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:174` |
| MESSAGE-TYPE | 60 | COPAUS2C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:117`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:175` |
| MESSAGE-SOURCE | 61 | COPAUS2C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:118`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:176` |
| AUTH-ID-CODE | 62 | COPAUS2C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:119`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:177` |
| AUTH-RESP-CODE | 63 | COPAUS2C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:120`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:178` |
| AUTH-RESP-REASON | 64 | COPAUS2C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:121`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:179` |
| PROCESSING-CODE | 65 | COPAUS2C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:122`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:180` |
| TRANSACTION-AMT | 66 | COPAUS2C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:123`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:181` |
| APPROVED-AMT | 67 | COPAUS2C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:124`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:182` |
| MERCHANT-CATAGORY-CODE | 68 | COPAUS2C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:126`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:183` |
| ACQR-COUNTRY-CODE | 70 | COPAUS2C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:127`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:184` |
| POS-ENTRY-MODE | 71 | COPAUS2C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:128`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:185` |
| MERCHANT-ID | 72 | COPAUS2C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:129`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:186` |
| MERCHANT-NAME | 73 | COPAUS2C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:187` |
| MERCHANT-NAME-LEN | 74 | COPAUS2C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:130` |
| MERCHANT-NAME-TEXT | 76 | COPAUS2C (1): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:131` |
| MERCHANT-CITY | 78 | COPAUS2C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:132`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:188` |
| MERCHANT-STATE | 79 | COPAUS2C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:133`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:189` |
| MERCHANT-ZIP | 80 | COPAUS2C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:134`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:190` |
| TRANSACTION-ID | 81 | COPAUS2C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:135`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:191` |
| MATCH-STATUS | 82 | COPAUS2C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:136`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:192` |
| AUTH-FRAUD | 83 | COPAUS2C (3): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:137`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:193`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:224` |
| ACCT-ID | 85 | COPAUS2C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:138`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:195` |
| CUST-ID | 86 | COPAUS2C (2): `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:139`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:196` |

Named in no procedure statement of the copying programs (may still be moved as part of a group): DCLAUTHFRDS (line 55), FRAUD-RPT-DATE (line 84).

## Key fields

| Field | Meaning | Source |
|---|---|---|
| CARD-NUM | Host variable for CARD_NUM CHAR(16), first primary-key column. | `app/app-authorization-ims-db2-mq/dcl/AUTHFRDS.dcl:56` |
| AUTH-TS | Host variable X(26) for AUTH_TS TIMESTAMP, second primary-key column; COPAUS2C fills it via TIMESTAMP_FORMAT. | `app/app-authorization-ims-db2-mq/dcl/AUTHFRDS.dcl:57` |
| AUTH-FRAUD | Fraud flag CHAR(1): 'F' reported, 'R' removed. | `app/app-authorization-ims-db2-mq/dcl/AUTHFRDS.dcl:83` |
| FRAUD-RPT-DATE | Fraud report DATE; COPAUS2C uses CURRENT DATE rather than this host variable. | `app/app-authorization-ims-db2-mq/dcl/AUTHFRDS.dcl:84` |
| MERCHANT-NAME | VARCHAR(22) group with 49-level length and text. | `app/app-authorization-ims-db2-mq/dcl/AUTHFRDS.dcl:73-77` |
| ACCT-ID | Account id DECIMAL(11,0). | `app/app-authorization-ims-db2-mq/dcl/AUTHFRDS.dcl:85` |
| CUST-ID | Customer id DECIMAL(9,0). | `app/app-authorization-ims-db2-mq/dcl/AUTHFRDS.dcl:86` |

## Observations

- conflict: DCLGEN header comments name table AWSTSSC.AUTHFRDS while the DECLARE and the DDL use CARDDEMO.AUTHFRDS; the library name is a placeholder (XXXXXXX.DB2.DCLGEN). (`app/app-authorization-ims-db2-mq/dcl/AUTHFRDS.dcl:2-3`)
- anomaly: PROCESSING_CODE is CHAR(6) in DB2 while the IMS detail field PA-PROCESSING-CODE is PIC 9(06); POS_ENTRY_MODE is SMALLINT vs 9(02) in IMS. Conversions happen via MOVE in COPAUS2C. (`app/app-authorization-ims-db2-mq/dcl/AUTHFRDS.dcl:34-39`)

## Sources

- `app/app-authorization-ims-db2-mq/dcl/AUTHFRDS.dcl`
- `docs/_work/structure/copybooks/AUTHFRDS.json`
- `docs/_work/layouts/AUTHFRDS.json`
- `docs/_work/semantic/copybooks/AUTHFRDS.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
