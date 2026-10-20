# Program COBDATFT

| Item | Value |
|---|---|
| Source | app/asm/COBDATFT.asm |
| Lines | code 60, comments 18, total 84 |
| Format | fixed |
| Language | Assembler |
| Runtime | asm-routine |
| Module | base |
| Invoked by | CALL-static app/cbl/CBACT01C.cbl:231 |
| Transaction or job step |  |
| Header description | Date format conversion routine. Input type 1 and 2 are tested in the code. (Unverified) |
| Version banner |  |

## Purpose

The program header describes this member as follows. That text is Unverified: Date format conversion routine. Input type 1 and 2 are tested in the code..

Confirmed rules implemented here:

- BR-BASE-COBDATFT-001: Date input type 1 is rejected when character 5 of the input is a hyphen or the requested output type is 2. Otherwise hyphens are inserted after the year and after the month.
- BR-BASE-COBDATFT-002: Date input type 2 is rejected when the requested output type is 1. Otherwise characters are copied while skipping the hyphen positions. The hyphen-position check for type 2 is present only as a comment.
- BR-BASE-COBDATFT-003: A date input type other than 1 or 2 moves INVALID INPUT into the error message field.

## Interfaces

### Inputs and outputs

| Resource | Kind | Logical name | Physical name | Access | Layout | Evidence |
|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |

### Linkage / COMMAREA

COMMAREA copybook: .

### Called programs and services

| Target | Mechanism | When | Parameters | Evidence |
|---|---|---|---|---|
|   |   |   |   |   |

## Copybooks

| Copybook | Purpose | REPLACING | Evidence |
|---|---|---|---|
| COCDATFT | DSECT for the date conversion parameter area |  | app/asm/COBDATFT.asm:66 |

## Processing logic

### Control flow

```mermaid
flowchart TD
    N0["none"]
```

### Paragraphs

| Paragraph | Lines | Purpose | Performs | Rules |
|---|---|---|---|---|
|   |   |   |   |   |

### Narrative

Read in full. Called from CBACT01C (app/cbl/CBACT01C.cbl:231).

## Embedded commands

| Kind | Command | Resource | Options | Response handling | Line |
|---|---|---|---|---|---|
|   |   |   |   |   |   |

## Business rules implemented

| Rule | Summary | Lines |
|---|---|---|
| BR-BASE-COBDATFT-001 | Date input type 1 is rejected when character 5 of the input is a hyphen or the requested output type is 2. Otherwise hyphens are inserted after the year and after the month. | app/asm/COBDATFT.asm:30-45 |
| BR-BASE-COBDATFT-002 | Date input type 2 is rejected when the requested output type is 1. Otherwise characters are copied while skipping the hyphen positions. The hyphen-position check for type 2 is present only as a comment. | app/asm/COBDATFT.asm:46-54 |
| BR-BASE-COBDATFT-003 | A date input type other than 1 or 2 moves INVALID INPUT into the error message field. | app/asm/COBDATFT.asm:34-56 |

## Error handling

| Condition | Action | Code | Message | Lines |
|---|---|---|---|---|
|   |   |   |   |   |

## Data CRUD

| Store | C | R | U | D | Browse | Notes |
|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |

## Observations

- The hyphen check for input type 2 is commented out, so a type-2 date is not rejected for a missing hyphen. (Confirmed, `app/asm/COBDATFT.asm:47-48`)

## Sources

- `app/asm/COBDATFT.asm`
- `docs/_work/programs/COBDATFT.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
