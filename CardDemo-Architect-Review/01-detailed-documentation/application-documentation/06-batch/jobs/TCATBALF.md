# Job TCATBALF

| Item | Value |
|---|---|
| Source | `app/jcl/TCATBALF.jcl` |
| Member | TCATBALF |
| Job card | `app/jcl/TCATBALF.jcl:1-2` |
| CLASS / MSGCLASS | A / 0 |
| NOTIFY | &SYSUID |
| Job COND |  |
| Steps | 3 |
| Module | base |

## Purpose

Comment in the JCL (Unverified, `app/jcl/TCATBALF.jcl:20`): DELETE TRANSACTION CATEGORY BALANCE VSAM FILE IF ONE ALREADY EXISTS

## Step flow

```mermaid
flowchart TD
    S0["STEP05: IDCAMS"]
    S1["STEP10: IDCAMS"]
    S0 --> S1
    S2["STEP15: IDCAMS"]
    S1 --> S2
```

## Steps

### STEP05

| Item | Value |
|---|---|
| EXEC | `app/jcl/TCATBALF.jcl:22` |
| Program | IDCAMS |
| PROC |  |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) | IDCAMS delete |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| SYSPRINT | SYSOUT=* |  |  |  |  | `app/jcl/TCATBALF.jcl:23` |
| SYSIN | * |  |  |  | in-stream lines 25-27; statements: DELETE SET | `app/jcl/TCATBALF.jcl:24` |

### STEP10

| Item | Value |
|---|---|
| EXEC | `app/jcl/TCATBALF.jcl:33` |
| Program | IDCAMS |
| PROC |  |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) | IDCAMS define VSAM cluster |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| SYSPRINT | SYSOUT=* |  |  |  |  | `app/jcl/TCATBALF.jcl:34` |
| SYSIN | * |  |  |  | in-stream lines 36-49; statements: DEFINE; NAME(): AWS.M2.CARDDEMO.TCATBALF.VSAM.KSDS AWS.M2.CARDDEMO.TCATBALF.VSAM.KSDS.DATA AWS.M2.CARDDEMO.TCATBALF.VSAM.KSDS.INDEX | `app/jcl/TCATBALF.jcl:35` |

### STEP15

| Item | Value |
|---|---|
| EXEC | `app/jcl/TCATBALF.jcl:54` |
| Program | IDCAMS |
| PROC |  |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) | IDCAMS REPRO copy |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| SYSPRINT | SYSOUT=* |  |  |  |  | `app/jcl/TCATBALF.jcl:55` |
| TCATBAL | AWS.M2.CARDDEMO.TCATBALF.PS | SHR |  |  |  | `app/jcl/TCATBALF.jcl:56-57` |
| TCATBALV | AWS.M2.CARDDEMO.TCATBALF.VSAM.KSDS | OLD |  |  |  | `app/jcl/TCATBALF.jcl:58-59` |
| SYSIN | * |  |  |  | in-stream lines 61-61; statements: REPRO | `app/jcl/TCATBALF.jcl:60` |

## Scheduling and dependencies

| Mechanism | From | To | Evidence |
|---|---|---|---|
| CA7 trigger | CLOSEFIL2 | TCATBALF | `app/scheduler/CardDemo.ca7:271` |
| CA7 trigger | TCATBALF | WAITSTEP | `app/scheduler/CardDemo.ca7:330` |
| Shell submit | scripts/remote_refresh.sh | TCATBALF | `scripts/remote_refresh.sh:35` |
| Shell submit | scripts/run_full_batch.sh | TCATBALF | `scripts/run_full_batch.sh:35` |
| Shell submit | scripts/run_posting.sh | TCATBALF | `scripts/run_posting.sh:20` |

## Parameters

Symbols left as parameters (not resolved): `&SYSUID`.

## Sources

- `app/jcl/TCATBALF.jcl`
- `docs/_work/structure/jcl/TCATBALF.json`
- `docs/_work/jobs/TCATBALF.json`

## Confidence

Steps, DDs, conditions and control-data summaries are Confirmed from the JCL. OPEN modes come from the program source. Comments are Unverified.
