# Job TRANTYPE

| Item | Value |
|---|---|
| Source | `app/jcl/TRANTYPE.jcl` |
| Member | TRANTYPE |
| Job card | `app/jcl/TRANTYPE.jcl:1-2` |
| CLASS / MSGCLASS | A / 0 |
| NOTIFY | &SYSUID |
| Job COND |  |
| Steps | 3 |
| Module | base |

## Purpose

Comment in the JCL (Unverified, `app/jcl/TRANTYPE.jcl:20`): DELETE TRANSACATION TYPE VSAM FILE IF ONE ALREADY EXISTS

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
| EXEC | `app/jcl/TRANTYPE.jcl:22` |
| Program | IDCAMS |
| PROC |  |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) | IDCAMS delete |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| SYSPRINT | SYSOUT=* |  |  |  |  | `app/jcl/TRANTYPE.jcl:23` |
| SYSIN | * |  |  |  | in-stream lines 25-27; statements: DELETE SET | `app/jcl/TRANTYPE.jcl:24` |

### STEP10

| Item | Value |
|---|---|
| EXEC | `app/jcl/TRANTYPE.jcl:33` |
| Program | IDCAMS |
| PROC |  |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) | IDCAMS define VSAM cluster |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| SYSPRINT | SYSOUT=* |  |  |  |  | `app/jcl/TRANTYPE.jcl:34` |
| SYSIN | * |  |  |  | in-stream lines 36-49; statements: DEFINE; NAME(): AWS.M2.CARDDEMO.TRANTYPE.VSAM.KSDS AWS.M2.CARDDEMO.TRANTYPE.VSAM.KSDS.DATA AWS.M2.CARDDEMO.TRANTYPE.VSAM.KSDS.INDEX | `app/jcl/TRANTYPE.jcl:35` |

### STEP15

| Item | Value |
|---|---|
| EXEC | `app/jcl/TRANTYPE.jcl:54` |
| Program | IDCAMS |
| PROC |  |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) | IDCAMS REPRO copy |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| SYSPRINT | SYSOUT=* |  |  |  |  | `app/jcl/TRANTYPE.jcl:55` |
| TRANTYPE | AWS.M2.CARDDEMO.TRANTYPE.PS | SHR |  |  |  | `app/jcl/TRANTYPE.jcl:56-57` |
| TTYPVSAM | AWS.M2.CARDDEMO.TRANTYPE.VSAM.KSDS | OLD |  |  |  | `app/jcl/TRANTYPE.jcl:58-59` |
| SYSIN | * |  |  |  | in-stream lines 61-61; statements: REPRO | `app/jcl/TRANTYPE.jcl:60` |

## Scheduling and dependencies

| Mechanism | From | To | Evidence |
|---|---|---|---|
| CA7 trigger | CLOSEFIL | TRANTYPE | `app/scheduler/CardDemo.ca7:162` |
| CA7 trigger | TRANTYPE | WAITSTEP | `app/scheduler/CardDemo.ca7:189` |
| Shell submit | scripts/remote_refresh.sh | TRANTYPE | `scripts/remote_refresh.sh:41` |
| Shell submit | scripts/run_full_batch.sh | TRANTYPE | `scripts/run_full_batch.sh:38` |

## Parameters

Symbols left as parameters (not resolved): `&SYSUID`.

## Sources

- `app/jcl/TRANTYPE.jcl`
- `docs/_work/structure/jcl/TRANTYPE.json`
- `docs/_work/jobs/TRANTYPE.json`

## Confidence

Steps, DDs, conditions and control-data summaries are Confirmed from the JCL. OPEN modes come from the program source. Comments are Unverified.
