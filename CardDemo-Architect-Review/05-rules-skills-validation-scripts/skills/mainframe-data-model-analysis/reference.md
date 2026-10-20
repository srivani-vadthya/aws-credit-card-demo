# Data Model Reference

## VSAM types

| Type | IDCAMS | COBOL | Notes |
|---|---|---|---|
| KSDS | INDEXED | ORGANIZATION INDEXED, RECORD KEY | KEYS(len offset) offset 0-based |
| ESDS | NONINDEXED | ORGANIZATION SEQUENTIAL (VSAM) | RBA access |
| RRDS | NUMBERED | ORGANIZATION RELATIVE, RELATIVE KEY | slot number |
| LDS | LINEAR | n/a | DB2/system use |
| AIX | DEFINE AIX RELATE() | ALTERNATE RECORD KEY [WITH DUPLICATES] | access via PATH |

CICS accesses an AIX through a FILE whose DSNAME is the PATH.

## Sequential datasets

RECFM F/FB/V/VB/FBA/VBA/U; LRECL; BLKSIZE (0 = system-determined).
FBA/VBA = ASA carriage control in byte 1 (reports). VB LRECL includes the
4-byte RDW.

## DB2 to COBOL type mapping

| DB2 | COBOL host variable |
|---|---|
| CHAR(n) | PIC X(n) |
| VARCHAR(n) | 49 LEN PIC S9(4) COMP + 49 TEXT PIC X(n) |
| SMALLINT | PIC S9(4) COMP |
| INTEGER | PIC S9(9) COMP |
| BIGINT | PIC S9(18) COMP |
| DECIMAL(p,s) | PIC S9(p-s)V9(s) COMP-3 |
| DATE / TIME / TIMESTAMP | PIC X(10) / X(8) / X(26) |
Nullable columns need indicator variables (PIC S9(4) COMP); note missing
indicators.

## IMS essentials

- Access methods: HDAM/PHDAM (hashed), HIDAM/PHIDAM (indexed root),
  HISAM, HSAM, GSAM (sequential files via DL/I), DEDB, INDEX.
- `FIELD NAME=(x,SEQ,U|M)` = sequence (key) field, unique or multiple.
- PROCOPT: G get, I insert, R replace, D delete, A all, L load, P path,
  O read-only (no hold), E exclusive.
- Segment search arguments (SSA) in code show the access path; qualified
  SSAs (`SEG(FIELD op value)`) reveal key usage.

## Mismatch checks (record each result)

| Check | Sources compared |
|---|---|
| Record length | copybook total, JCL LRECL, IDCAMS RECORDSIZE max, DBD BYTES, docs |
| Key | IDCAMS KEYS(len off) vs copybook field at offset off+1 with length len |
| AIX key | AIX KEYS vs field; UNIQUEKEY vs program duplicate handling |
| DB2 columns | DDL vs DCLGEN vs program host variables |
| Segment layout | DBD FIELD START/BYTES vs copybook offsets |
| Code values | 88-level values vs sample data distinct values |

## Data dictionary columns

Field, entity, store(s), offset/length, format (PIC/USAGE or SQL type),
domain (88-levels/lookup tables), source of value (program/paragraph that
sets it), validations (BR-ids), sensitivity (PII/PCI candidates such as card
numbers, CVV, SSN, DOB, names, addresses - tag `Inferred` from field names
and confirm via usage).
