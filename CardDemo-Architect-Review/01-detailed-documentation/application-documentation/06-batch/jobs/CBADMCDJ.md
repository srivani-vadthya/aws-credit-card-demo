# Job CBADMCDJ

| Item | Value |
|---|---|
| Source | `app/jcl/CBADMCDJ.jcl` |
| Member | CBADMCDJ |
| Job card | `app/jcl/CBADMCDJ.jcl:1-2` |
| CLASS / MSGCLASS | A / H |
| NOTIFY | &SYSUID |
| Job COND |  |
| Steps | 1 |
| Module | base |

## Purpose

Comment in the JCL (Unverified, `app/jcl/CBADMCDJ.jcl:20`): Create Resources for Card Demo application               ******

## Step flow

```mermaid
flowchart TD
    S0["STEP1: DFHCSDUP"]
```

## Steps

### STEP1

| Item | Value |
|---|---|
| EXEC | `app/jcl/CBADMCDJ.jcl:27-28` |
| Program | DFHCSDUP |
| PROC |  |
| Application program |  |
| PARM | `'CSD(READWRITE),PAGESIZE(60),NOCOMPAT'` |
| COND |  |
| Function (earlier pass) | Utility step DFHCSDUP |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| STEPLIB | OEM.CICSTS.V05R06M0.CICS.SDFHLOAD | SHR |  |  |  | `app/jcl/CBADMCDJ.jcl:29` |
| DFHCSD | OEM.CICSTS.DFHCSD | SHR |  |  |  | `app/jcl/CBADMCDJ.jcl:30` |
| OUTDD | SYSOUT=* |  |  |  |  | `app/jcl/CBADMCDJ.jcl:31` |
| SYSPRINT | SYSOUT=* |  |  |  |  | `app/jcl/CBADMCDJ.jcl:32` |
| SYSIN | * |  |  |  | in-stream lines 34-162; statements: DEFINE | `app/jcl/CBADMCDJ.jcl:33` |

## Scheduling and dependencies

Not referenced by the CA7 or Control-M exports or the shell scripts (see the gap report).

## JCL library, INCLUDE and SET

| Statement | Text | Line |
|---|---|---|
| SET | HLQ=AWS.M2.CARDDEMO | `app/jcl/CBADMCDJ.jcl:25` |

## Parameters

Symbols left as parameters (not resolved): `&SYSUID`.

## Sources

- `app/jcl/CBADMCDJ.jcl`
- `docs/_work/structure/jcl/CBADMCDJ.json`
- `docs/_work/jobs/CBADMCDJ.json`

## Confidence

Steps, DDs, conditions and control-data summaries are Confirmed from the JCL. OPEN modes come from the program source. Comments are Unverified.
