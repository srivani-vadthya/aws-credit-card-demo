# Program COBSWAIT

| Item | Value |
|---|---|
| Source | `app/cbl/COBSWAIT.cbl` |
| Lines | 41 total, 13 code, 22 comment, 6 blank |
| PROGRAM-ID | COBSWAIT |
| Author |  |
| Runtime | batch-main |
| Module | base |
| CICS transactions | None in CSD |
| JCL steps | [WAITSTEP](../06-batch/jobs/WAITSTEP.md).WAIT (`app/jcl/WAITSTEP.jcl:22`) |
| Paragraphs | 1 |
| Semantic analysis | validated (batch B05) |
| Version banner |  |

## Summary

COBSWAIT is a small batch utility that pauses a job step. It ACCEPTs an 8-character value from SYSIN, moves it to the binary field MVSWAIT-TIME and CALLs the external routine MVSWAIT with it, then ends with STOP RUN. The header comment states the value is a wait time in centiseconds. It has no files, no conditions and no business logic; it is executed by job step WAIT in app/jcl/WAITSTEP.jcl. (Confirmed)

Evidence: `app/cbl/COBSWAIT.cbl:1-6`, `app/cbl/COBSWAIT.cbl:28-40`, `app/jcl/WAITSTEP.jcl:22`

Header comment (Unverified, `app/cbl/COBSWAIT.cbl:1-8`): PROGRAM     : COBSWAIT.CBL Application : CardDemo Type        : BATCH COBOL Program FUNCTION    : UTILITY PROGRAM TO WAIT (PARM IN CENTISECONDS) All Rights Reserved. http://www.apache.org/licenses/LICENSE-2.0

## Divisions and sections

| Division / section | Lines | Notes |
|---|---|---|
| IDENTIFICATION DIVISION | `app/cbl/COBSWAIT.cbl:22-23` |  |
| ENVIRONMENT DIVISION | `app/cbl/COBSWAIT.cbl:24-25` |  |
| DATA DIVISION | `app/cbl/COBSWAIT.cbl:26-33` |  |
| PROCEDURE DIVISION | `app/cbl/COBSWAIT.cbl:34-41` |  |
| ENVIRONMENT / INPUT-OUTPUT SECTION | `app/cbl/COBSWAIT.cbl:25` |  |
| DATA / WORKING-STORAGE SECTION | `app/cbl/COBSWAIT.cbl:28-33` |  |

## Files and data stores

No SELECT entries (no COBOL file I/O).

## Embedded CICS, SQL and DL/I commands

No EXEC blocks.

## Calls, transfers and callers

| Mechanism | Target | Parameters | Paragraph | Lines |
|---|---|---|---|---|
| CALL static | MVSWAIT | MVSWAIT-TIME | (PROCEDURE DIVISION entry) | `app/cbl/COBSWAIT.cbl:38` |

## Copybooks

No COPY statements.

## Data division items

Every data entry coded in this source (copybook contents are on the copybook pages). Lengths are computed from PIC and USAGE.

| Section | Lvl | Name | PIC | Usage | Len | OCCURS | REDEFINES | VALUE | 88-levels | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| WORKING-STORAGE | 01 | MVSWAIT-TIME | 9(8) | COMP | 4 |  |  |  |  | 30 |
| WORKING-STORAGE | 01 | PARM-VALUE | X(8) |  | 8 |  |  |  |  | 31 |

## Statement inventory

Every procedure statement the parser recorded, by kind. Each one is listed with its line under Paragraph details.

| Kind | Count |
|---|---|
| Decisions (IF, EVALUATE, WHEN, loops, handlers) | 0 |
| Calculations | 0 |
| File I/O | 0 |
| EXEC CICS / SQL / DLI | 0 |
| CALL | 1 |
| PERFORM | 0 |
| GO TO | 0 |
| MOVE literal | 0 |
| MOVE field | 1 |
| SET | 0 |
| STRING, UNSTRING, INSPECT, INITIALIZE, COPY, ENTRY and others | 1 |
| DISPLAY | 0 |
| GOBACK, STOP RUN, RETURN, XCTL | 1 |
| Not classified by the parser | 0 |

## Control flow

```mermaid
flowchart TD
    P0["(PROCEDURE DIVISION entry)"]
```

| Paragraph | Lines | Logic | Performs | Performed by | Reachable |
|---|---|---|---|---|---|
| [(PROCEDURE DIVISION entry)](#para-procedure-division-entry) | 36-40 | ACCEPTs PARM-VALUE (PIC X(8)) from SYSIN, moves it to MVSWAIT-TIME (PIC 9(8) COMP), CALLs 'MVSWAIT' USING MVSWAIT-TIME and issues STOP RUN. (Confirmed) |  |  | yes |

## Paragraph details

### Para (PROCEDURE DIVISION entry)

Lines `app/cbl/COBSWAIT.cbl:36-40`. 

Logic: ACCEPTs PARM-VALUE (PIC X(8)) from SYSIN, moves it to MVSWAIT-TIME (PIC 9(8) COMP), CALLs 'MVSWAIT' USING MVSWAIT-TIME and issues STOP RUN. (Confirmed)

Statements in source order:

- `ACCEPT PARM-VALUE FROM SYSIN` at `app/cbl/COBSWAIT.cbl:36`
- `MOVE PARM-VALUE TO MVSWAIT-TIME` at `app/cbl/COBSWAIT.cbl:37`
- CALL MVSWAIT at `app/cbl/COBSWAIT.cbl:38`
- Ends with STOP RUN at `app/cbl/COBSWAIT.cbl:40`

## Business rules


No business rules identified: COBSWAIT is a technical batch utility: it reads a wait duration from SYSIN and calls the external routine MVSWAIT to suspend the step. It contains no decisions, validations, calculations or data processing with business meaning.

Decision coverage: 0 of 0 business-candidate decision points are linked to a rule or a no-rule reason (0 inside rule ranges).

## Error handling

No status checks, abends or return-code settings were found.

## Observations and SME questions

- anomaly: The SYSIN value is moved from alphanumeric PIC X(8) to numeric PIC 9(8) COMP without a NUMERIC check; a non-numeric or short (space-padded) value gives an unpredictable wait time. (`app/cbl/COBSWAIT.cbl:36-37`)
- conflict: The header says 'PARM IN CENTISECONDS' but the value is read from SYSIN, not from the EXEC PARM; the unit (centiseconds) is stated only in the comment and depends on MVSWAIT. (`app/cbl/COBSWAIT.cbl:5`)
- anomaly: MVSWAIT is an external called routine with no source in the repository (external-or-missing). (`app/cbl/COBSWAIT.cbl:38`)
- SME question: Where does MVSWAIT come from (site or vendor load library) and what unit does it expect for MVSWAIT-TIME? (`app/cbl/COBSWAIT.cbl:38`)

## Sources

- `app/cbl/COBSWAIT.cbl`
- `docs/_work/structure/programs/COBSWAIT.json`
- `docs/_work/semantic/programs/COBSWAIT.json`
- `docs/_work/programs/COBSWAIT.json`

## Confidence

Structure tables (divisions, items, paragraphs, statements, line numbers) are Confirmed: they are parsed from the source. Paragraph logic and rule statements carry their own Confirmed/Inferred tag from the batch analysis, and every rule anchor was checked against the cited lines. Decision-point classes are a keyword heuristic used only for coverage measurement. Header comments are Unverified.
