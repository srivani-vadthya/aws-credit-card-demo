# Job DISCGRP

| Item | Value |
|---|---|
| Source | `app/jcl/DISCGRP.jcl` |
| Member | DISCGRP |
| Job card | `app/jcl/DISCGRP.jcl:1-2` |
| CLASS / MSGCLASS | A / 0 |
| NOTIFY | &SYSUID |
| Job COND |  |
| Steps | 3 |
| Module | base |

## Purpose

Comment in the JCL (Unverified, `app/jcl/DISCGRP.jcl:20`): DELETE DISCLOSURE GROUP VSAM FILE IF ONE ALREADY EXISTS

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
| EXEC | `app/jcl/DISCGRP.jcl:22` |
| Program | IDCAMS |
| PROC |  |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) | IDCAMS delete |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| SYSPRINT | SYSOUT=* |  |  |  |  | `app/jcl/DISCGRP.jcl:23` |
| SYSIN | * |  |  |  | in-stream lines 25-27; statements: DELETE SET | `app/jcl/DISCGRP.jcl:24` |

### STEP10

| Item | Value |
|---|---|
| EXEC | `app/jcl/DISCGRP.jcl:33` |
| Program | IDCAMS |
| PROC |  |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) | IDCAMS define VSAM cluster |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| SYSPRINT | SYSOUT=* |  |  |  |  | `app/jcl/DISCGRP.jcl:34` |
| SYSIN | * |  |  |  | in-stream lines 36-49; statements: DEFINE; NAME(): AWS.M2.CARDDEMO.DISCGRP.VSAM.KSDS AWS.M2.CARDDEMO.DISCGRP.VSAM.KSDS.DATA AWS.M2.CARDDEMO.DISCGRP.VSAM.KSDS.INDEX | `app/jcl/DISCGRP.jcl:35` |

### STEP15

| Item | Value |
|---|---|
| EXEC | `app/jcl/DISCGRP.jcl:54` |
| Program | IDCAMS |
| PROC |  |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) | IDCAMS REPRO copy |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| SYSPRINT | SYSOUT=* |  |  |  |  | `app/jcl/DISCGRP.jcl:55` |
| DISCGRP | AWS.M2.CARDDEMO.DISCGRP.PS | SHR |  |  |  | `app/jcl/DISCGRP.jcl:56-57` |
| DISCVSAM | AWS.M2.CARDDEMO.DISCGRP.VSAM.KSDS | OLD |  |  |  | `app/jcl/DISCGRP.jcl:58-59` |
| SYSIN | * |  |  |  | in-stream lines 61-61; statements: REPRO | `app/jcl/DISCGRP.jcl:60` |

## Scheduling and dependencies

| Mechanism | From | To | Evidence |
|---|---|---|---|
| Control-M condition WEEKLY-DisclosureGroupsRefresh-CLOSEFIL | CLOSEFIL | DISCGRP | `app/scheduler/CardDemo.controlm:35` (OUTCOND), `app/scheduler/CardDemo.controlm:39` (INCOND) |
| Control-M condition WEEKLY-DisclosureGroupsRefresh-DISCGRP | DISCGRP | WAITSTEP | `app/scheduler/CardDemo.controlm:41` (OUTCOND), `app/scheduler/CardDemo.controlm:45` (INCOND) |
| Shell submit | scripts/remote_refresh.sh | DISCGRP | `scripts/remote_refresh.sh:32` |
| Shell submit | scripts/run_full_batch.sh | DISCGRP | `scripts/run_full_batch.sh:32` |

## Parameters

Symbols left as parameters (not resolved): `&SYSUID`.

## Sources

- `app/jcl/DISCGRP.jcl`
- `docs/_work/structure/jcl/DISCGRP.json`
- `docs/_work/jobs/DISCGRP.json`

## Confidence

Steps, DDs, conditions and control-data summaries are Confirmed from the JCL. OPEN modes come from the program source. Comments are Unverified.
