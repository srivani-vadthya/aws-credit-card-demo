# Data definitions

Every DB2 DDL object (from DDL members and DB2 control cards), IMS DBD segment and PSB PCB, parsed by `extract_structure.py`. Table pages in [db2/](db2/) and database pages in [ims/](ims/) carry the earlier narrative.

## DB2 objects

| Object | Name | Defined in | Details | Programs with SQL on it | Source |
|---|---|---|---|---|---|
| TABLE | CARDDEMO.AUTHFRDS | db2-ddl | columns: CARD_NUM CHAR(16), AUTH_TS TIMESTAMP, AUTH_TYPE CHAR(4), CARD_EXPIRY_DATE CHAR(4), MESSAGE_TYPE CHAR(6), MESSAGE_SOURCE CHAR(6), AUTH_ID_CODE CHAR(6), AUTH_RESP_CODE CHAR(2), AUTH_RESP_REASON CHAR(4), PROCESSING_CODE CHAR(6), TRANSACTION_AMT DECIMAL(12,2), APPROVED_AMT DECIMAL(12,2), MERCHANT_CATAGORY_CODE CHAR(4), ACQR_COUNTRY_CODE CHAR(3), POS_ENTRY_MODE SMALLINT, MERCHANT_ID CHAR(15), MERCHANT_NAME VARCHAR(22), MERCHANT_CITY CHAR(13), MERCHANT_STATE CHAR(02), MERCHANT_ZIP CHAR(09), TRANSACTION_ID CHAR(15), MATCH_STATUS CHAR(1), AUTH_FRAUD CHAR(1), FRAUD_RPT_DATE DATE, ACCT_ID DECIMAL(11), CUST_ID DECIMAL(9); primary key (CARD_NUM, AUTH_TS) | COPAUS2C | `app/app-authorization-ims-db2-mq/ddl/AUTHFRDS.ddl:1` |
| UNIQUE INDEX | CARDDEMO.XAUTHFRD | db2-ddl | on CARDDEMO.AUTHFRDS |  | `app/app-authorization-ims-db2-mq/ddl/XAUTHFRD.ddl:1` |
| DATABASE | CARDDEMO | db2-ddl |  |  | `app/app-transaction-type-db2/ctl/DB2CREAT.ctl:17` |
| TABLESPACE | CARDSPC1 | db2-ddl |  |  | `app/app-transaction-type-db2/ctl/DB2CREAT.ctl:24` |
| TABLE | CARDDEMO.TRANSACTION_TYPE | db2-ddl | columns: TR_TYPE CHAR(2), TR_DESCRIPTION VARCHAR(50); primary key (TR_TYPE) | COBTUPDT, COTRTLIC, COTRTUPC | `app/app-transaction-type-db2/ctl/DB2CREAT.ctl:35` |
| UNIQUE INDEX | CARDDEMO.XTRAN_TYPE | db2-ddl | on CARDDEMO.TRANSACTION_TYPE |  | `app/app-transaction-type-db2/ctl/DB2CREAT.ctl:44` |
| TABLESPACE | CARDSTTC | db2-ddl |  |  | `app/app-transaction-type-db2/ctl/DB2CREAT.ctl:61` |
| TABLE | CARDDEMO.TRANSACTION_TYPE_CATEGORY | db2-ddl | columns: TRC_TYPE_CODE CHAR(2), TRC_TYPE_CATEGORY CHAR(4), TRC_CAT_DATA VARCHAR(50); primary key (TRC_TYPE_CODE, TRC_TYPE_CATEGORY) |  | `app/app-transaction-type-db2/ctl/DB2CREAT.ctl:75` |
| UNIQUE INDEX | CARDDEMO.X_TRAN_TYPE_CATG | db2-ddl | on CARDDEMO.TRANSACTION_TYPE_CATEGORY |  | `app/app-transaction-type-db2/ctl/DB2CREAT.ctl:85` |
| TABLE | CARDDEMO.TRANSACTION_TYPE_CATEGORY | db2-ddl | columns: TRC_TYPE_CODE CHAR(2), TRC_TYPE_CATEGORY CHAR(4), TRC_CAT_DATA VARCHAR(50); primary key (TRC_TYPE_CODE, TRC_TYPE_CATEGORY) |  | `app/app-transaction-type-db2/ddl/TRNTYCAT.ddl:1` |
| TABLE | CARDDEMO.TRANSACTION_TYPE | db2-ddl | columns: TR_TYPE CHAR(2), TR_DESCRIPTION VARCHAR(50); primary key (TR_TYPE) | COBTUPDT, COTRTLIC, COTRTUPC | `app/app-transaction-type-db2/ddl/TRNTYPE.ddl:1` |
| UNIQUE INDEX | CARDDEMO.X_TRAN_TYPE_CATG | db2-ddl | on CARDDEMO.TRANSACTION_TYPE_CATEGORY |  | `app/app-transaction-type-db2/ddl/XTRNTYCAT.ddl:1` |
| UNIQUE INDEX | CARDDEMO.XTRAN_TYPE | db2-ddl | on CARDDEMO.TRANSACTION_TYPE |  | `app/app-transaction-type-db2/ddl/XTRNTYPE.ddl:1` |

## IMS databases (DBD)

### DBPAUTP0

Access (HIDAM,VSAM), source `app/app-authorization-ims-db2-mq/ims/DBPAUTP0.dbd:18`.

| Segment | Parent | Bytes | Fields | Source |
|---|---|---|---|---|
| PAUTSUM0 | 0 | 100 | (ACCNTID,SEQ,U) start 1 len 6 type P | `app/app-authorization-ims-db2-mq/ims/DBPAUTP0.dbd:28` |
| PAUTDTL1 | PAUTSUM0 | 200 | (PAUT9CTS,SEQ,U) start 1 len 8 type C | `app/app-authorization-ims-db2-mq/ims/DBPAUTP0.dbd:36` |

### DBPAUTX0

Access (INDEX,VSAM,PROT), source `app/app-authorization-ims-db2-mq/ims/DBPAUTX0.dbd:18`.

| Segment | Parent | Bytes | Fields | Source |
|---|---|---|---|---|
| PAUTINDX | 0 | 6 | (INDXSEQ,SEQ,U) start 1 len 6 type P | `app/app-authorization-ims-db2-mq/ims/DBPAUTX0.dbd:27` |

### PADFLDBD

Access (GSAM,BSAM), source `app/app-authorization-ims-db2-mq/ims/PADFLDBD.DBD:22`.

No SEGM statements.

### PASFLDBD

Access (GSAM,BSAM), source `app/app-authorization-ims-db2-mq/ims/PASFLDBD.DBD:22`.

No SEGM statements.

## IMS program specification blocks (PSB)

| PSB | PCB label | Type | DBD | PROCOPT | Sensitive segments | Source |
|---|---|---|---|---|---|---|
| DLIGSAMP | PAUTBPCB | DB | DBPAUTP0 | GOTP | PAUTSUM0, PAUTDTL1 | `app/app-authorization-ims-db2-mq/ims/DLIGSAMP.PSB:18` |
| DLIGSAMP |  | GSAM | PASFLDBD | LS |  | `app/app-authorization-ims-db2-mq/ims/DLIGSAMP.PSB:21` |
| DLIGSAMP |  | GSAM | PADFLDBD | LS |  | `app/app-authorization-ims-db2-mq/ims/DLIGSAMP.PSB:22` |
| PAUTBUNL | PAUTBPCB | DB | DBPAUTP0 | GOTP | PAUTSUM0, PAUTDTL1 | `app/app-authorization-ims-db2-mq/ims/PAUTBUNL.PSB:18` |
| PSBPAUTB | PAUTBPCB | DB | DBPAUTP0 | AP | PAUTSUM0, PAUTDTL1 | `app/app-authorization-ims-db2-mq/ims/PSBPAUTB.psb:17` |
| PSBPAUTL | PAUTLPCB | DB | DBPAUTP0 | L | PAUTSUM0, PAUTDTL1 | `app/app-authorization-ims-db2-mq/ims/PSBPAUTL.psb:17` |

## Sources

- `docs/_work/structure/data-definitions.json`

## Confidence

Confirmed: parsed from DDL, control cards, DBD and PSB sources.
