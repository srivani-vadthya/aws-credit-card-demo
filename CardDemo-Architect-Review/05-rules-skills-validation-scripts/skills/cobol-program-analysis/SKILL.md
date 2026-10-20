---
name: cobol-program-analysis
description: >-
  Performs deep, evidence-backed analysis of individual mainframe programs
  (COBOL batch, CICS online, IMS/DB2/MQ variants, Assembler subroutines):
  structure, copybooks, files and DD mapping, data items and flags, paragraph
  control flow, calls, embedded CICS/SQL/DLI/MQ commands, error handling,
  abends and record-level CRUD. Produces program-facts JSON per program. Use
  when reverse-engineering or documenting a specific legacy program.
disable-model-invocation: true
---

# Program Analysis (COBOL / Assembler)

Input: `inventory.json` + `references.json` from discovery. Output:
`<work_dir>/programs/<PROGRAM-ID>.json` matching
`schemas/program-facts.schema.json` (orchestrator skill), plus updates to
`xref/call-graph.json`, `xref/copybook-usage.json`, `xref/crud-matrix.json`.

Read the `cobol-source-reading` rule before starting. Analyze one program at
a time; read the whole source (not just grep hits) for every program.

Detailed (paragraph-level) analysis runs in orchestrator Phase S: the
paragraph, statement, decision and data-item lists come from
`extract_structure.py` (`<work_dir>/structure/programs/<PGM>.json`), and the
analyst fills `<work_dir>/semantic/programs/<PGM>.json` per
[../mainframe-doc-orchestrator/batch-analysis.md](../mainframe-doc-orchestrator/batch-analysis.md),
then runs `batch_manager.py check`. Program facts from this skill remain the
input for call graphs, CRUD and dataset bindings.

## Per-program checklist

```
- [ ] 1 Identity: PROGRAM-ID, file path, header comments (Unverified), version banner
- [ ] 2 Runtime type: batch / CICS / IMS BMP / DLI batch / called subprogram / ASM
- [ ] 3 Interfaces: LINKAGE SECTION, PROCEDURE DIVISION USING, DFHCOMMAREA, PCBs, RETURN-CODE
- [ ] 4 Copybooks: COPY / INCLUDE with REPLACING, purpose of each
- [ ] 5 Files: SELECT/ASSIGN -> ddname, ORGANIZATION, ACCESS, RECORD KEY, ALTERNATE KEY, FILE STATUS, FD record
- [ ] 6 Data: key working-storage groups, level-88 conditions, constants, tables (OCCURS/INDEXED BY)
- [ ] 7 Control flow: paragraph list, PERFORM graph, GO TO, sections, entry/exit points
- [ ] 8 External calls: CALL (static/dynamic + resolved targets), XCTL/LINK/START, MQ, LE services
- [ ] 9 Embedded commands: every EXEC CICS/SQL/DLI with options and handled RESP/SQLCODE/status
- [ ] 10 Data access CRUD: per file/table/segment/queue: Create/Read/Update/Delete/Browse
- [ ] 11 Error handling: FILE STATUS checks, RESP evaluations, HANDLE ABEND/CONDITION, SQLCODE, abend codes, messages
- [ ] 12 Business logic summary + candidate rules (handed to business-rules-extraction)
- [ ] 13 Observations: dead code, unused copybooks/paragraphs, hardcoded values, anomalies
```

## Method

1. **Runtime type** - decide from evidence, in this order: `EXEC CICS` or
   DFHCOMMAREA -> CICS; `EXEC DLI`/`CBLTDLI` + PSB in JCL -> IMS; `EXEC SQL`
   -> DB2 (combinable); `PROCEDURE DIVISION USING` with no JCL `EXEC PGM`
   for it -> subprogram; JCL `EXEC PGM=` -> batch main. Record every
   signal.
2. **Control flow** - list paragraphs/sections in source order with line
   ranges. Build the PERFORM graph (`PERFORM X`, `PERFORM X THRU Y`, inline
   `PERFORM UNTIL/VARYING`), GO TO edges, and fall-through. Identify the
   mainline (first paragraph(s) until `GOBACK`/`STOP RUN`/`EXEC CICS RETURN`).
   Render later as a Mermaid flowchart; keep it at paragraph level.
3. **Dynamic targets** - for each variable XCTL/LINK/CALL target, trace
   every MOVE into the variable and VALUE clauses in copybooks (option
   tables). Output each resolved target with its evidence line.
4. **CRUD** - map each I/O verb to its resource:
   - COBOL: OPEN mode (INPUT/OUTPUT/I-O/EXTEND), READ/READ NEXT/START,
     WRITE, REWRITE, DELETE.
   - CICS: READ (UPDATE), WRITE, REWRITE, DELETE, STARTBR/READNEXT/READPREV,
     WRITEQ/READQ TS/TD.
   - SQL: SELECT/INSERT/UPDATE/DELETE/cursor FETCH.
   - DLI: GU/GN/GNP (read), ISRT (create), REPL (update), DLET (delete).
   - MQ: GET (consume), PUT/PUT1 (produce).
   Resolve logical names to physical: ddname -> JCL DSN, CICS FILE -> CSD
   DSNAME, PCB -> PSB/DBD.
5. **Error handling** - record each check (condition, action, message
   literal, abend code, RETURN-CODE set). Note unchecked I/O as an
   observation.
6. **Assembler programs** - capture CSECT/ENTRY names, AMODE/RMODE,
   register save/linkage convention, parameter list (R1), macros used
   (system macros such as STIMER, WTO, TIME, GETMAIN vs application macros
   in the inventory), SVCs, and the COBOL callers.

## Output quality bar

- Every list entry has `source` with line numbers.
- Paragraph purpose sentences are derived from code, not names; tag
  `Inferred` when summarizing multi-paragraph behavior.
- Do not paraphrase comments as facts; quote and tag `Unverified`.

## Additional resources

- Construct and code tables (USAGE sizes, file status, CICS RESP, SQLCODE,
  DL/I status, LE abend services): [reference.md](reference.md)
