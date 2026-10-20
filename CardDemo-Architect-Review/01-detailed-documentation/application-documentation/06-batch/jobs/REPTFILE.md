# Job REPTFILE

| Item | Value |
|---|---|
| Source | `app/jcl/REPTFILE.jcl` |
| Member | REPTFILE |
| Job card | `app/jcl/REPTFILE.jcl:1-2` |
| CLASS / MSGCLASS | A / 0 |
| NOTIFY | &SYSUID |
| Job COND |  |
| Steps | 1 |
| Module | base |

## Purpose

Comment in the JCL (Unverified, `app/jcl/REPTFILE.jcl:20`): DELETE TRANSACATION MASTER VSAM FILE IF ONE ALREADY EXISTS

## Step flow

```mermaid
flowchart TD
    S0["STEP05: IDCAMS"]
```

## Steps

### STEP05

| Item | Value |
|---|---|
| EXEC | `app/jcl/REPTFILE.jcl:22` |
| Program | IDCAMS |
| PROC |  |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) | IDCAMS define GDG |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| SYSPRINT | SYSOUT=* |  |  |  |  | `app/jcl/REPTFILE.jcl:23` |
| SYSIN | * |  |  |  | in-stream lines 25-28; statements: DEFINE; NAME(): AWS.M2.CARDDEMO.TRANREPT | `app/jcl/REPTFILE.jcl:24` |

## Scheduling and dependencies

Not referenced by the CA7 or Control-M exports or the shell scripts (see the gap report).

## Parameters

Symbols left as parameters (not resolved): `&SYSUID`.

## Sources

- `app/jcl/REPTFILE.jcl`
- `docs/_work/structure/jcl/REPTFILE.json`
- `docs/_work/jobs/REPTFILE.json`

## Confidence

Steps, DDs, conditions and control-data summaries are Confirmed from the JCL. OPEN modes come from the program source. Comments are Unverified.
