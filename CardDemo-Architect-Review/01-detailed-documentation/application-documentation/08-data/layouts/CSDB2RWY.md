# Layout CSDB2RWY

| Item | Value |
|---|---|
| Source | `app/app-transaction-type-db2/cpy/CSDB2RWY.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 46 |
| Data items | 14 (88-levels: 2) |
| Semantic analysis | validated (batch B08) |

## Purpose

Common DB2 working storage for CardDemo CICS/DB2 programs. It defines the SQLCODE display field, a dummy integer for the connectivity priming query, the WS-DB2-OK / WS-DB2-ERROR processing flag, the current-action message prefix, and the buffers used to call IBM's DSNTIAC message formatter. It is the data counterpart of CSDB2RPY and is included by COTRTLIC (EXEC SQL INCLUDE CSDB2RWY). (Confirmed)

Evidence: `app/app-transaction-type-db2/cpy/CSDB2RWY.cpy:18-28`, `app/app-transaction-type-db2/cpy/CSDB2RWY.cpy:30-45`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:304`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 05 | &nbsp;&nbsp;WS-DB2-COMMON-VARS |  |  | 1 | 81 | 81 |  |  |  | 21 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-DISP-SQLCODE | ----9 | DISPLAY | 1 | 5 | 5 |  |  |  | 22 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-DUMMY-DB2-INT | S9(4) | COMP-3 | 6 | 8 | 3 |  |  | 0 | 23 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-DB2-PROCESSING-FLAG | X(1) | DISPLAY | 9 | 9 | 1 |  |  |  | 25 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-DB2-CURRENT-ACTION | X(72) | DISPLAY | 10 | 81 | 72 |  |  | SPACES | 28 |
| 05 | &nbsp;&nbsp;WS-DSNTIAC-FORMATTED |  |  | 82 | 803 | 722 |  |  |  | 33 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-DSNTIAC-MESG-LEN | S9(4) | COMP | 82 | 83 | 2 |  |  | +720 | 34 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-DSNTIAC-FMTD-TEXT |  |  | 84 | 803 | 720 |  |  |  | 35 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-DSNTIAC-FMTD-TEXT-LINE | X(72) | DISPLAY | 84 | 803 | 720 | 10 |  | SPACES | 36 |
| 05 | &nbsp;&nbsp;WS-DSNTIAC-LRECL | S9(4) | COMP | 804 | 805 | 2 |  |  | +72 | 41 |
| 05 | &nbsp;&nbsp;WS-DSNTIAC-ERROR |  |  | 806 | 817 | 12 |  |  |  | 42 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-DSNTIAC-ERR-MSG | X(10) | DISPLAY | 806 | 815 | 10 |  |  | 'DSNTIAC CD' | 43 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-DSNTIAC-ERR-CD-X | X(02) | DISPLAY | 816 | 817 | 2 |  |  | SPACES | 44 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;WS-DSNTIAC-ERR-CD | 9(02) | DISPLAY | 816 | 817 | 2 |  | WS-DSNTIAC-ERR-CD-X |  | 45 |

## Level-88 conditions

| Field | Condition | Values | Line |
|---|---|---|---|
| WS-DB2-PROCESSING-FLAG | WS-DB2-OK | '0' | 26 |
| WS-DB2-PROCESSING-FLAG | WS-DB2-ERROR | '1' | 27 |

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [COTRTLIC](../../07-programs/COTRTLIC.md) | cobol-program | EXEC SQL INCLUDE | active |  | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:304` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| WS-DISP-SQLCODE | 22 | COTRTLIC (12): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1632`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1667`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1759`, ... |
| WS-DUMMY-DB2-INT | 23 | COTRTLIC (1): `app/app-transaction-type-db2/cpy/CSDB2RPY.cpy:25` |
| WS-DB2-ERROR | 27 | COTRTLIC (9): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:687`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1612`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1710`, ... |
| WS-DB2-CURRENT-ACTION | 28 | COTRTLIC (15): `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1688`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1713`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1785`, ... |
| WS-DSNTIAC-FORMATTED | 33 | COTRTLIC (1): `app/app-transaction-type-db2/cpy/CSDB2RPY.cpy:60` |
| WS-DSNTIAC-FMTD-TEXT | 35 | COTRTLIC (2): `app/app-transaction-type-db2/cpy/CSDB2RPY.cpy:71`, `app/app-transaction-type-db2/cpy/CSDB2RPY.cpy:80` |
| WS-DSNTIAC-LRECL | 41 | COTRTLIC (2): `app/app-transaction-type-db2/cpy/CSDB2RPY.cpy:55`, `app/app-transaction-type-db2/cpy/CSDB2RPY.cpy:61` |
| WS-DSNTIAC-ERROR | 42 | COTRTLIC (1): `app/app-transaction-type-db2/cpy/CSDB2RPY.cpy:71` |
| WS-DSNTIAC-ERR-MSG | 43 | COTRTLIC (1): `app/app-transaction-type-db2/cpy/CSDB2RPY.cpy:70` |
| WS-DSNTIAC-ERR-CD | 45 | COTRTLIC (2): `app/app-transaction-type-db2/cpy/CSDB2RPY.cpy:64`, `app/app-transaction-type-db2/cpy/CSDB2RPY.cpy:67` |

Named in no procedure statement of the copying programs (may still be moved as part of a group): WS-DB2-COMMON-VARS (line 21), WS-DB2-PROCESSING-FLAG (line 25), WS-DB2-OK (line 26), WS-DSNTIAC-MESG-LEN (line 34), WS-DSNTIAC-FMTD-TEXT-LINE (line 36), WS-DSNTIAC-ERR-CD-X (line 44).

## Key fields

| Field | Meaning | Source |
|---|---|---|
| WS-DB2-COMMON-VARS | Group of common DB2 working variables. | `app/app-transaction-type-db2/cpy/CSDB2RWY.cpy:21` |
| WS-DISP-SQLCODE | Edited (----9) display form of SQLCODE used when building error messages. | `app/app-transaction-type-db2/cpy/CSDB2RWY.cpy:22` |
| WS-DUMMY-DB2-INT | Receiving host variable for the connectivity priming query SELECT 1 FROM SYSIBM.SYSDUMMY1. | `app/app-transaction-type-db2/cpy/CSDB2RWY.cpy:23-24` |
| WS-DB2-PROCESSING-FLAG | DB2 outcome flag. | `app/app-transaction-type-db2/cpy/CSDB2RWY.cpy:25` |
| WS-DB2-OK | 88-level: DB2 call succeeded (value '0'). | `app/app-transaction-type-db2/cpy/CSDB2RWY.cpy:26` |
| WS-DB2-ERROR | 88-level: DB2 call failed (value '1'). | `app/app-transaction-type-db2/cpy/CSDB2RWY.cpy:27` |
| WS-DB2-CURRENT-ACTION | 72-byte description of the DB2 action in progress, used as message prefix. | `app/app-transaction-type-db2/cpy/CSDB2RWY.cpy:28-29` |
| WS-DSNTIAC-FORMATTED | DSNTIAC output area: length (+720) followed by 10 lines of 72 bytes of formatted SQL error text (WS-DSNTIAC-FMTD-TEXT-LINE). | `app/app-transaction-type-db2/cpy/CSDB2RWY.cpy:33-38` |
| WS-DSNTIAC-LRECL | Line length (72) passed to DSNTIAC. | `app/app-transaction-type-db2/cpy/CSDB2RWY.cpy:40` |
| WS-DSNTIAC-ERROR | Fallback text 'DSNTIAC CD' plus 2-digit DSNTIAC return code (WS-DSNTIAC-ERR-CD redefining WS-DSNTIAC-ERR-CD-X), used when DSNTIAC itself fails. | `app/app-transaction-type-db2/cpy/CSDB2RWY.cpy:41-45` |

## Observations

- anomaly: The copybook starts at level 05 with no 01 parent; the including program must place it under its own 01 group. (`app/app-transaction-type-db2/cpy/CSDB2RWY.cpy:21`)
- anomaly: WS-DSNTIAC-ERR-CD is PIC 9(02); RETURN-CODE values above 99 would be truncated when assigned in CSDB2RPY. (`app/app-transaction-type-db2/cpy/CSDB2RWY.cpy:44-45`)

## Sources

- `app/app-transaction-type-db2/cpy/CSDB2RWY.cpy`
- `docs/_work/structure/copybooks/CSDB2RWY.json`
- `docs/_work/layouts/CSDB2RWY.json`
- `docs/_work/semantic/copybooks/CSDB2RWY.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
