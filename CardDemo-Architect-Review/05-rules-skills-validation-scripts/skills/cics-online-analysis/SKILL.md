---
name: cics-online-analysis
description: >-
  Reverse-engineers the online (CICS) layer of a mainframe application: CSD
  resource definitions, transaction-to-program mapping, BMS mapsets into
  screen specifications and mockups, PF-key behavior, pseudo-conversational
  state and COMMAREA contracts, menu/option tables and the full navigation
  graph, plus TS/TD queue and START usage. Use when documenting CICS
  transactions, screens, or user navigation flows of a legacy application.
disable-model-invocation: true
---

# CICS Online Analysis

Inputs: inventory, references, program facts. Outputs under
`<work_dir>/online/`: `transactions.json`, `screens/<MAPSET>.json`,
`navigation.json`, `commarea.json`, `queues.json`. Follow the
`cics-bms-csd-reading` rule.

## Steps

```
- [ ] 1 Resource catalog from every CSD file (all DEFINE types, group, source file)
- [ ] 2 Transaction catalog: TRANSID -> PROGRAM (CSD) cross-checked with programs' own TRANSID usage
- [ ] 3 Screens: per mapset/map, field table + 24x80 (or SIZE) mockup
- [ ] 4 Screen <-> program binding: SEND/RECEIVE MAP/MAPSET per program
- [ ] 5 Interaction model per program: first-time vs re-entry, AID keys handled
- [ ] 6 COMMAREA contract(s): layout, who sets/reads each field
- [ ] 7 Navigation graph: XCTL/LINK/RETURN TRANSID/START edges with conditions
- [ ] 8 Queues and async: TSQ/TDQ names, purpose, START/RETRIEVE, internal reader submission
- [ ] 9 Consistency check: CSD vs code vs docs (missing/extra resources -> gaps)
```

### 1-2 Resources and transactions
- Parse all CSD files (base and modules). For each TRANSACTION record its
  PROGRAM and group; for each PROGRAM its language/attributes; FILE ->
  DSNAME and allowed operations; LIBRARY -> load library DSNs; TDQUEUE ->
  destination; DB2ENTRY/DB2TRAN -> plan and transids.
- A program that is invoked only via XCTL/LINK may have no TRANSACTION -
  record this, don't treat it as an error.
- Transactions in docs but not in CSD (or vice versa) -> gaps register.

### 3 Screen specification
For each map: title literals, every field (name, row, col, length,
attributes, color, initial text, input/output/protected/hidden), plus a
monospace mockup built strictly from POS/LENGTH/INITIAL. Unnamed literal
fields go in the mockup; named fields appear as placeholders of their
length (`_` for input, `X`/`9` for output).
Link each field to the program logic that fills or validates it (from the
symbolic map suffix references in program facts).

### 5 Interaction model
For each online program, document:
- Entry detection (`EIBCALEN = 0`, COMMAREA context flags such as a
  "re-enter" 88-level).
- AID handling: `EIBAID` / `DFHENTER`, `DFHPFn`, `DFHCLEAR`, `DFHPAn` - one
  row per key with resulting action and target.
- Validation sequence and messages per field (feed to business rules).
- Exit: `RETURN TRANSID(...) COMMAREA(...)` (pseudo-conversational), plain
  `RETURN`, `XCTL`, `SEND TEXT`.

### 7 Navigation graph
- Edges: `from program -> to program/transaction`, mechanism (XCTL, LINK,
  RETURN TRANSID, START), trigger (key/option/condition), evidence.
- Resolve variable targets through COMMAREA fields set by the caller and
  through option-table copybooks (OCCURS of program names/option text,
  often with user-type restrictions). Each resolved edge cites the VALUE
  line it came from.
- Produce per-role views when the code distinguishes user types (e.g.
  admin vs regular), with evidence of the check.

### 8 Async / queues
- `WRITEQ TD QUEUE(x)` where x maps to an internal reader TDQUEUE ->
  online-submitted batch job; capture the JCL written (often literal lines
  in working storage) and link to the batch job docs.
- `START TRANSID ... INTERVAL/TIME`, `RETRIEVE` -> async tasks, MQ triggers.

## Additional resources

- Mockup conventions, attribute byte meanings, AID constants:
  [reference.md](reference.md)
