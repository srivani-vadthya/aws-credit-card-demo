# Program MVSWAIT

| Item | Value |
|---|---|
| Source | app/asm/MVSWAIT.asm |
| Lines | code 12, comments 16, total 30 |
| Format | fixed |
| Language | Assembler |
| Runtime | asm-routine |
| Module | base |
| Invoked by | CALL-static app/cbl/COBSWAIT.cbl:38 |
| Transaction or job step |  |
| Header description | No application description comment. A code comment questions the MVI of the save area. (Unverified) |
| Version banner |  |

## Purpose

The program header describes this member as follows. That text is Unverified: No application description comment. A code comment questions the MVI of the save area..

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
| ASMWAIT | Application macro that starts the interval timer |  | app/asm/MVSWAIT.asm:23 |

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

Read in full. Called from COBSWAIT (app/cbl/COBSWAIT.cbl:38).

## Embedded commands

| Kind | Command | Resource | Options | Response handling | Line |
|---|---|---|---|---|---|
|   |   |   |   |   |   |

## Business rules implemented

| Rule | Summary | Lines |
|---|---|---|
|   |   |   |

## Error handling

| Condition | Action | Code | Message | Lines |
|---|---|---|---|---|
|   |   |   |   |   |

## Data CRUD

| Store | C | R | U | D | Browse | Notes |
|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |

## Observations

- Comment asks whether the MVI that marks the save area can be removed. Unverified. (Unverified, `app/asm/MVSWAIT.asm:25`)

## Sources

- `app/asm/MVSWAIT.asm`
- `docs/_work/programs/MVSWAIT.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
