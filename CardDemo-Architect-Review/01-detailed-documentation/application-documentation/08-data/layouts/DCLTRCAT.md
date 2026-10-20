# Layout DCLTRCAT

| Item | Value |
|---|---|
| Source | `app/app-transaction-type-db2/dcl/DCLTRCAT.dcl` |
| Type | db2-dclgen |
| Content | data |
| Lines | 54 |
| Data items | 6 (88-levels: 0) |
| Semantic analysis | validated (batch B08) |

## Purpose

DB2 DCLGEN output for table CARDDEMO.TRANSACTION_TYPE_CATEGORY: an EXEC SQL DECLARE TABLE with columns TRC_TYPE_CODE CHAR(2), TRC_TYPE_CATEGORY CHAR(4) and TRC_CAT_DATA VARCHAR(50), all NOT NULL, and the COBOL host structure DCLTRANSACTION-TYPE-CATEGORY. In this module it is included only by COTRTUPC (EXEC SQL INCLUDE DCLTRCAT); it describes the child category rows keyed by transaction type code. (Confirmed)

Evidence: `app/app-transaction-type-db2/dcl/DCLTRCAT.dcl:17-27`, `app/app-transaction-type-db2/dcl/DCLTRCAT.dcl:28-32`, `app/app-transaction-type-db2/dcl/DCLTRCAT.dcl:36-51`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:288`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | DCLTRANSACTION-TYPE-CATEGORY |  |  | 1 | 58 | 58 |  |  |  | 36 |
| 10 | &nbsp;&nbsp;DCL-TRC-TYPE-CODE | X(2) | DISPLAY | 1 | 2 | 2 |  |  |  | 39 |
| 10 | &nbsp;&nbsp;DCL-TRC-TYPE-CATEGORY | X(4) | DISPLAY | 3 | 6 | 4 |  |  |  | 42 |
| 10 | &nbsp;&nbsp;DCL-TRC-CAT-DATA |  |  | 7 | 58 | 52 |  |  |  | 45 |
| 49 | &nbsp;&nbsp;&nbsp;&nbsp;DCL-TRC-CAT-DATA-LEN | S9(4) | COMP | 7 | 8 | 2 |  |  |  | 47 |
| 49 | &nbsp;&nbsp;&nbsp;&nbsp;DCL-TRC-CAT-DATA-TEXT | X(50) | DISPLAY | 9 | 58 | 50 |  |  |  | 50 |

## Level-88 conditions

None.

## DB2 table declaration

Table `CARDDEMO.TRANSACTION_TYPE_CATEGORY` (`app/app-transaction-type-db2/dcl/DCLTRCAT.dcl:28-32`):

| Column | Type | NOT NULL |
|---|---|---|
| TRC_TYPE_CODE | CHAR(2) | yes |
| TRC_TYPE_CATEGORY | CHAR(4) | yes |
| TRC_CAT_DATA | VARCHAR(50) | yes |

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [COTRTUPC](../../07-programs/COTRTUPC.md) | cobol-program | EXEC SQL INCLUDE | active |  | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:288` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

No field of this member is named in procedure code.

Named in no procedure statement of the copying programs (may still be moved as part of a group): DCLTRANSACTION-TYPE-CATEGORY (line 36), DCL-TRC-TYPE-CODE (line 39), DCL-TRC-TYPE-CATEGORY (line 42), DCL-TRC-CAT-DATA (line 45), DCL-TRC-CAT-DATA-LEN (line 47), DCL-TRC-CAT-DATA-TEXT (line 50).

## Key fields

| Field | Meaning | Source |
|---|---|---|
| DCLTRANSACTION-TYPE-CATEGORY | DCLGEN host structure for one row of CARDDEMO.TRANSACTION_TYPE_CATEGORY. | `app/app-transaction-type-db2/dcl/DCLTRCAT.dcl:36` |
| DCL-TRC-TYPE-CODE | Host variable for TRC_TYPE_CODE CHAR(2) NOT NULL - the transaction type code the category belongs to. | `app/app-transaction-type-db2/dcl/DCLTRCAT.dcl:39` |
| DCL-TRC-TYPE-CATEGORY | Host variable for TRC_TYPE_CATEGORY CHAR(4) NOT NULL - the category code within the type. | `app/app-transaction-type-db2/dcl/DCLTRCAT.dcl:42-43` |
| DCL-TRC-CAT-DATA | VARCHAR host group for TRC_CAT_DATA VARCHAR(50) NOT NULL - category description. | `app/app-transaction-type-db2/dcl/DCLTRCAT.dcl:45` |
| DCL-TRC-CAT-DATA-LEN | Binary length prefix (S9(4) COMP) of the VARCHAR category data. | `app/app-transaction-type-db2/dcl/DCLTRCAT.dcl:47-48` |
| DCL-TRC-CAT-DATA-TEXT | Category description text, up to 50 characters. | `app/app-transaction-type-db2/dcl/DCLTRCAT.dcl:50-51` |

## Observations

- hardcoded-value: Table qualified with the literal schema CARDDEMO; DCLGEN library comment names a personal dataset (SNJARAO.AWS.DCL). (`app/app-transaction-type-db2/dcl/DCLTRCAT.dcl:18-19`)

## Sources

- `app/app-transaction-type-db2/dcl/DCLTRCAT.dcl`
- `docs/_work/structure/copybooks/DCLTRCAT.json`
- `docs/_work/layouts/DCLTRCAT.json`
- `docs/_work/semantic/copybooks/DCLTRCAT.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
