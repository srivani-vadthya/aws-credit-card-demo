# Job ACCTFILE

| Item | Value |
|---|---|
| Source | `app/jcl/ACCTFILE.jcl` |
| Member | ACCTFILE |
| Job card | `app/jcl/ACCTFILE.jcl:1-2` |
| CLASS / MSGCLASS | A / 0 |
| NOTIFY | &SYSUID |
| Job COND |  |
| Steps | 3 |
| Module | base |

## Purpose

Comment in the JCL (Unverified, `app/jcl/ACCTFILE.jcl:20`): DELETE ACCOUNT VSAM FILE IF ONE ALREADY EXISTS

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
| EXEC | `app/jcl/ACCTFILE.jcl:22` |
| Program | IDCAMS |
| PROC |  |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) | IDCAMS delete |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| SYSPRINT | SYSOUT=* |  |  |  |  | `app/jcl/ACCTFILE.jcl:23` |
| SYSIN | * |  |  |  | in-stream lines 25-27; statements: DELETE | `app/jcl/ACCTFILE.jcl:24` |

### STEP10

| Item | Value |
|---|---|
| EXEC | `app/jcl/ACCTFILE.jcl:33` |
| Program | IDCAMS |
| PROC |  |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) | IDCAMS define VSAM cluster |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| SYSPRINT | SYSOUT=* |  |  |  |  | `app/jcl/ACCTFILE.jcl:34` |
| SYSIN | * |  |  |  | in-stream lines 36-49; statements: DEFINE; NAME(): AWS.M2.CARDDEMO.ACCTDATA.VSAM.KSDS AWS.M2.CARDDEMO.ACCTDATA.VSAM.KSDS.DATA AWS.M2.CARDDEMO.ACCTDATA.VSAM.KSDS.INDEX | `app/jcl/ACCTFILE.jcl:35` |

### STEP15

| Item | Value |
|---|---|
| EXEC | `app/jcl/ACCTFILE.jcl:54` |
| Program | IDCAMS |
| PROC |  |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) | IDCAMS REPRO copy |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| SYSPRINT | SYSOUT=* |  |  |  |  | `app/jcl/ACCTFILE.jcl:55` |
| ACCTDATA | AWS.M2.CARDDEMO.ACCTDATA.PS | SHR |  |  |  | `app/jcl/ACCTFILE.jcl:56-57` |
| ACCTVSAM | AWS.M2.CARDDEMO.ACCTDATA.VSAM.KSDS | SHR |  |  |  | `app/jcl/ACCTFILE.jcl:58-59` |
| SYSIN | * |  |  |  | in-stream lines 61-61; statements: REPRO | `app/jcl/ACCTFILE.jcl:60` |

## Scheduling and dependencies

| Mechanism | From | To | Evidence |
|---|---|---|---|
| Shell submit | scripts/remote_refresh.sh | ACCTFILE | `scripts/remote_refresh.sh:17` |
| Shell submit | scripts/run_full_batch.sh | ACCTFILE | `scripts/run_full_batch.sh:17` |
| Shell submit | scripts/run_posting.sh | ACCTFILE | `scripts/run_posting.sh:17` |

## Parameters

Symbols left as parameters (not resolved): `&SYSUID`.

## Sources

- `app/jcl/ACCTFILE.jcl`
- `docs/_work/structure/jcl/ACCTFILE.json`
- `docs/_work/jobs/ACCTFILE.json`

## Confidence

Steps, DDs, conditions and control-data summaries are Confirmed from the JCL. OPEN modes come from the program source. Comments are Unverified.
