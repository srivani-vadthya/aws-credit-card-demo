# Layout DCLTRTYP

| Item | Value |
|---|---|
| Source | `app/app-transaction-type-db2/dcl/DCLTRTYP.dcl` |
| Type | db2-dclgen |
| Content | data |
| Lines | 49 |
| Data items | 5 (88-levels: 0) |
| Semantic analysis | validated (batch B08) |

## Purpose

DB2 DCLGEN output for table CARDDEMO.TRANSACTION_TYPE: an EXEC SQL DECLARE TABLE statement with columns TR_TYPE CHAR(2) and TR_DESCRIPTION VARCHAR(50), both NOT NULL, plus the COBOL host structure DCLTRANSACTION-TYPE. It is included (EXEC SQL INCLUDE DCLTRTYP) by the transaction type maintenance programs COBTUPDT, COTRTLIC and COTRTUPC as the host-variable layout for the reference table of transaction type codes and their descriptions. (Confirmed)

Evidence: `app/app-transaction-type-db2/dcl/DCLTRTYP.dcl:17-27`, `app/app-transaction-type-db2/dcl/DCLTRTYP.dcl:28-31`, `app/app-transaction-type-db2/dcl/DCLTRTYP.dcl:35-46`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | DCLTRANSACTION-TYPE |  |  | 1 | 54 | 54 |  |  |  | 35 |
| 10 | &nbsp;&nbsp;DCL-TR-TYPE | X(2) | DISPLAY | 1 | 2 | 2 |  |  |  | 38 |
| 10 | &nbsp;&nbsp;DCL-TR-DESCRIPTION |  |  | 3 | 54 | 52 |  |  |  | 40 |
| 49 | &nbsp;&nbsp;&nbsp;&nbsp;DCL-TR-DESCRIPTION-LEN | S9(4) | COMP | 3 | 4 | 2 |  |  |  | 42 |
| 49 | &nbsp;&nbsp;&nbsp;&nbsp;DCL-TR-DESCRIPTION-TEXT | X(50) | DISPLAY | 5 | 54 | 50 |  |  |  | 45 |

## Level-88 conditions

None.

## DB2 table declaration

Table `CARDDEMO.TRANSACTION_TYPE` (`app/app-transaction-type-db2/dcl/DCLTRTYP.dcl:28-31`):

| Column | Type | NOT NULL |
|---|---|---|
| TR_TYPE | CHAR(2) | yes |
| TR_DESCRIPTION | VARCHAR(50) | yes |

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [COBTUPDT](../../07-programs/COBTUPDT.md) | cobol-program | EXEC SQL INCLUDE | active |  | `app/app-transaction-type-db2/cbl/COBTUPDT.cbl:54` |
| [COTRTLIC](../../07-programs/COTRTLIC.md) | cobol-program | EXEC SQL INCLUDE | active |  | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:333` |
| [COTRTUPC](../../07-programs/COTRTUPC.md) | cobol-program | EXEC SQL INCLUDE | active |  | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:286` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| DCLTRANSACTION-TYPE | 35 | COTRTLIC (2): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1624`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1751` |
| DCL-TR-TYPE | 38 | COTRTLIC (14): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1628`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1638`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1645`, ...; COTRTUPC (9): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1473`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1478`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1481`, ... |
| DCL-TR-DESCRIPTION | 40 | COTRTLIC (4): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1629`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1664`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1756`, ...; COTRTUPC (3): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1479`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1546`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1601` |
| DCL-TR-DESCRIPTION-LEN | 42 | COTRTLIC (1): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1843`; COTRTUPC (2): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1524`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1541` |
| DCL-TR-DESCRIPTION-TEXT | 45 | COTRTLIC (3): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1641`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1765`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1842`; COTRTUPC (2): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1524`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1540` |

## Key fields

| Field | Meaning | Source |
|---|---|---|
| DCLTRANSACTION-TYPE | DCLGEN host structure for one row of CARDDEMO.TRANSACTION_TYPE. | `app/app-transaction-type-db2/dcl/DCLTRTYP.dcl:35` |
| DCL-TR-TYPE | Host variable for column TR_TYPE CHAR(2) NOT NULL - the 2-character transaction type code (table key per usage in WHERE clauses). | `app/app-transaction-type-db2/dcl/DCLTRTYP.dcl:38` |
| DCL-TR-DESCRIPTION | VARCHAR host group for column TR_DESCRIPTION VARCHAR(50) NOT NULL. | `app/app-transaction-type-db2/dcl/DCLTRTYP.dcl:40` |
| DCL-TR-DESCRIPTION-LEN | Binary length prefix (S9(4) COMP) of the VARCHAR description. | `app/app-transaction-type-db2/dcl/DCLTRTYP.dcl:42-43` |
| DCL-TR-DESCRIPTION-TEXT | Description text, up to 50 characters. | `app/app-transaction-type-db2/dcl/DCLTRTYP.dcl:45-46` |

## Observations

- hardcoded-value: The table is qualified with the literal schema CARDDEMO and the DCLGEN library comment names a personal dataset (SNJARAO.AWS.DCL); the schema is not parameterised. (`app/app-transaction-type-db2/dcl/DCLTRTYP.dcl:18-19`)
- anomaly: COBTUPDT includes this copybook but binds its own X(50) working-storage fields instead of DCL-TR-DESCRIPTION-LEN/TEXT, so the length prefix is not used there. (`app/app-transaction-type-db2/cbl/COBTUPDT.cbl:54`)

## Sources

- `app/app-transaction-type-db2/dcl/DCLTRTYP.dcl`
- `docs/_work/structure/copybooks/DCLTRTYP.json`
- `docs/_work/layouts/DCLTRTYP.json`
- `docs/_work/semantic/copybooks/DCLTRTYP.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
