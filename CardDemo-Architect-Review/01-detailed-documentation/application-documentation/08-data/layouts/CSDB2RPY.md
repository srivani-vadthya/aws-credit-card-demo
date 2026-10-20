# Layout CSDB2RPY

| Item | Value |
|---|---|
| Source | `app/app-transaction-type-db2/cpy/CSDB2RPY.cpy` |
| Type | cobol-copybook |
| Content | procedure |
| Lines | 89 |
| Data items | 0 (88-levels: 0) |
| Semantic analysis | validated (batch B08) |

## Purpose

Common DB2 procedure-division paragraphs for CardDemo CICS/DB2 programs, used with the working storage in CSDB2RWY. 9998-PRIMING-QUERY checks DB2 connectivity with a dummy SELECT from SYSIBM.SYSDUMMY1, and 9999-FORMAT-DB2-MESSAGE turns the current SQLCA into a readable message (via IBM DSNTIAC) stored in WS-RETURN-MSG. It is included at the end of COTRTLIC's procedure division (EXEC SQL INCLUDE CSDB2RPY). (Confirmed)

Evidence: `app/app-transaction-type-db2/cpy/CSDB2RPY.cpy:21-48`, `app/app-transaction-type-db2/cpy/CSDB2RPY.cpy:57-88`, `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:2055`

## Procedure paragraphs

This copybook contains procedure-division code copied into programs.

| Paragraph | Lines | Decisions | Calculations | Performs |
|---|---|---|---|---|
| 9998-PRIMING-QUERY | `app/app-transaction-type-db2/cpy/CSDB2RPY.cpy:21-45` | 3 | 0 | 9999-FORMAT-DB2-MESSAGE |
| 9998-PRIMING-QUERY-EXIT | `app/app-transaction-type-db2/cpy/CSDB2RPY.cpy:46-48` | 0 | 0 |  |
| 9999-FORMAT-DB2-MESSAGE | `app/app-transaction-type-db2/cpy/CSDB2RPY.cpy:53-85` | 1 | 1 |  |
| 9999-FORMAT-DB2-MESSAGE-EXIT | `app/app-transaction-type-db2/cpy/CSDB2RPY.cpy:87-89` | 0 | 0 |  |

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [COTRTLIC](../../07-programs/COTRTLIC.md) | cobol-program | EXEC SQL INCLUDE | active |  | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:2055` |

## Key fields

| Field | Meaning | Source |
|---|---|---|
| 9998-PRIMING-QUERY | Connectivity check: SELECT 1 INTO WS-DUMMY-DB2-INT FROM SYSIBM.SYSDUMMY1; any SQLCODE other than 0 sets WS-DB2-ERROR, sets action 'Db2 access failure. ' and formats the message. | `app/app-transaction-type-db2/cpy/CSDB2RPY.cpy:21-46` |
| 9998-PRIMING-QUERY-EXIT | Exit paragraph for the PERFORM THRU range of the priming query. | `app/app-transaction-type-db2/cpy/CSDB2RPY.cpy:47-49` |
| 9999-FORMAT-DB2-MESSAGE | Calls DSNTIAC (via LIT-DSNTIAC) with DFHEIBLK, DFHCOMMAREA, SQLCA, WS-DSNTIAC-FORMATTED and WS-DSNTIAC-LRECL; on a non-zero DSNTIAC return code substitutes the WS-DSNTIAC-ERROR text; builds WS-LONG-MSG = trimmed WS-DB2-CURRENT-ACTION + ' SQLCODE:' + WS-DISP-SQLCODE + formatted text and moves it to WS-RETURN-MSG. | `app/app-transaction-type-db2/cpy/CSDB2RPY.cpy:57-86` |
| 9999-FORMAT-DB2-MESSAGE-EXIT | Exit paragraph for the PERFORM THRU range of the message formatter. | `app/app-transaction-type-db2/cpy/CSDB2RPY.cpy:87-89` |

## Observations

- anomaly: Line 63 has a malformed sequence area (' 06400') and several lines (58, 60, 64-66) lack sequence numbers; harmless in columns 1-6 but indicates hand edits. (`app/app-transaction-type-db2/cpy/CSDB2RPY.cpy:58-66`)
- anomaly: MOVE 'DSNTIAC CD: ' (12 characters) into WS-DSNTIAC-ERR-MSG (PIC X(10)) truncates to 'DSNTIAC CD'. (`app/app-transaction-type-db2/cpy/CSDB2RPY.cpy:70`)
- anomaly: The procedures depend on data items not defined in CSDB2RWY: LIT-DSNTIAC, WS-LONG-MSG and WS-RETURN-MSG must be defined by the including program, and DFHEIBLK/DFHCOMMAREA make the copybook CICS-only. (`app/app-transaction-type-db2/cpy/CSDB2RPY.cpy:59-63`)
- anomaly: 9998-PRIMING-QUERY treats any non-zero SQLCODE, including positive warnings, as a DB2 error. (`app/app-transaction-type-db2/cpy/CSDB2RPY.cpy:35-46`)

## Sources

- `app/app-transaction-type-db2/cpy/CSDB2RPY.cpy`
- `docs/_work/structure/copybooks/CSDB2RPY.json`
- `docs/_work/layouts/CSDB2RPY.json`
- `docs/_work/semantic/copybooks/CSDB2RPY.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
