---
name: business-rules-extraction
description: >-
  Extracts, classifies and documents business rules embedded in legacy
  mainframe code (COBOL, CICS, batch, SQL, JCL/SORT logic): validations,
  calculations, decisions, routing, authorization, data integrity,
  reference-data lookups and messages, each with a stable ID, plain-language
  statement, conditions, outcomes, source traceability and confidence. Use
  when building a business rules catalog or explaining what a legacy
  program does in business terms.
disable-model-invocation: true
---

# Business Rules Extraction

Output: `<work_dir>/rules/rules.json` (schema `rule.schema.json`) and
`<work_dir>/rules/by-program/<PROGRAM>.md` drafts. Inputs: program facts
(candidate rules section), online facts (validation per field), batch facts
(SORT INCLUDE/OMIT, IDCAMS IF LASTCC), data facts (88-levels).

## What counts as a rule

| Category | Code signals |
|---|---|
| validation | IF/EVALUATE on input fields followed by error message / error flag / reject |
| calculation | COMPUTE, ADD/SUBTRACT/MULTIPLY/DIVIDE on monetary/quantity fields, ROUNDED |
| decision | EVALUATE TRUE / nested IF choosing different processing |
| routing | XCTL/LINK/CALL target selection, menu option tables, user-type checks |
| authorization | user type/role checks, approve/decline logic, limits |
| data-integrity | existence checks before update, duplicate checks, READ UPDATE + REWRITE sequences, cross-file consistency |
| lifecycle | status field transitions (open/closed/active/expired) |
| reference-data | table lookups (SEARCH, READ of code files/tables) that drive behaviour |
| temporal | date comparisons (expiry, cycle, age, purge windows) |
| batch-selection | SORT INCLUDE/OMIT, record filtering, reject criteria |

Not rules: pure technical plumbing (screen attribute setting, RESP checks
without business meaning) - document those in program specs instead.

## Procedure per program

1. Walk the paragraph graph from the mainline; for each decision point
   classify as rule / technical.
2. For each rule capture:
   - `id`: `BR-<MODULE>-<PROGRAM>-NNN` (stable; never renumber, retire
     instead). MODULE = profile module id upper-cased, letters/digits only;
     rules spanning programs use `BR-<MODULE>-NNN`.
   - `statement`: one sentence in business language ("A transaction is
     rejected when the card's account is not found in the cross-reference").
   - `conditions` and `outcomes` in structured form (field, operator,
     value/field) using source field names plus business names.
   - `data`: fields/stores involved; `messages`: literal texts shown/logged.
   - `trigger`: screen action, batch step, message arrival.
   - `source`: `path:start-end` (decision lines + action lines).
   - `confidence`: Confirmed (literal code logic) / Inferred (business
     meaning derived from names or context - say why) / Unverified.
3. Deduplicate: identical logic in several programs -> one rule with
   multiple `implementations`; note inconsistencies between copies as
   findings (e.g. different limits or messages).
4. Calculations: give the formula with field names, rounding, precision
   (PIC scale), order of operations, and a worked example only if all inputs
   are defined by code or sample data.
5. Constants: magic numbers/literals in conditions are listed with their
   location as candidate parameters.
6. Decision tables: for EVALUATE with 3+ branches, render a table
   (condition columns -> outcome).

## Review checklist

- [ ] Every validation message literal in the program appears in some rule or in the error catalog
- [ ] Every COMPUTE on business fields is covered
- [ ] Every 88-level used in a condition has its meaning stated
- [ ] Rules reference data dictionary fields by exact name
- [ ] No rule without `source` lines
