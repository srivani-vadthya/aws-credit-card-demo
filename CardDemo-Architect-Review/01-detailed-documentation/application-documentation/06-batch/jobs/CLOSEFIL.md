# Job CLOSEFIL

| Item | Value |
|---|---|
| Source | `app/jcl/CLOSEFIL.jcl` |
| Member | CLOSEFIL |
| Job card | `app/jcl/CLOSEFIL.jcl:1-2` |
| CLASS / MSGCLASS | A / 0 |
| NOTIFY | &SYSUID |
| Job COND |  |
| Steps | 1 |
| Module | base |

## Purpose

Comment in the JCL (Unverified, `app/jcl/CLOSEFIL.jcl:20`): Close files in CICS region

## Step flow

```mermaid
flowchart TD
    S0["CLCIFIL: SDSF"]
```

## Steps

### CLCIFIL

| Item | Value |
|---|---|
| EXEC | `app/jcl/CLOSEFIL.jcl:22` |
| Program | SDSF |
| PROC |  |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) | Operator command |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| ISFOUT | SYSOUT=* |  |  |  |  | `app/jcl/CLOSEFIL.jcl:23` |
| CMDOUT | SYSOUT=* |  |  |  |  | `app/jcl/CLOSEFIL.jcl:24` |
| ISFIN | * |  |  |  | in-stream lines 26-30 | `app/jcl/CLOSEFIL.jcl:25` |

## Scheduling and dependencies

| Mechanism | From | To | Evidence |
|---|---|---|---|
| CA7 trigger | CLOSEFIL | CBPAUP0J | `app/scheduler/CardDemo.ca7:43` |
| CA7 trigger | CLOSEFIL | TRANTYPE | `app/scheduler/CardDemo.ca7:162` |
| CA7 trigger | WAITSTEP | CLOSEFIL | `app/scheduler/CardDemo.ca7:303` |
| CA7 trigger | WAITSTEP | CLOSEFIL | `app/scheduler/CardDemo.ca7:335` |
| CA7 trigger | CLOSEFIL | READACCT | `app/scheduler/CardDemo.ca7:340` |
| CA7 trigger | CLOSEFIL | CREASTMT | `app/scheduler/CardDemo.ca7:468` |
| CA7 trigger | OPENFIL | CLOSEFIL | `app/scheduler/CardDemo.ca7:532` |
| CA7 trigger | CLOSEFIL | PRTCATBL | `app/scheduler/CardDemo.ca7:537` |
| Control-M condition DAILY-TransactionBackup-CLOSEFIL | CLOSEFIL | TRANBKP | `app/scheduler/CardDemo.controlm:5` (OUTCOND), `app/scheduler/CardDemo.controlm:9` (INCOND) |
| Control-M condition MONTHLY-InterestCalculation-CLOSEFIL | CLOSEFIL | INTCALC | `app/scheduler/CardDemo.controlm:66` (OUTCOND), `app/scheduler/CardDemo.controlm:70` (INCOND) |
| Control-M condition WEEKLY-TransactionTypesDBRefresh-MNTTRDB2 | MNTTRDB2 | CLOSEFIL | `app/scheduler/CardDemo.controlm:28` (OUTCOND), `app/scheduler/CardDemo.controlm:34` (INCOND) |
| Control-M condition WEEKLY-DisclosureGroupsRefresh-CLOSEFIL | CLOSEFIL | DISCGRP | `app/scheduler/CardDemo.controlm:35` (OUTCOND), `app/scheduler/CardDemo.controlm:39` (INCOND) |
| Shell submit | scripts/remote_refresh.sh | CLOSEFIL | `scripts/remote_refresh.sh:13` |
| Shell submit | scripts/run_full_batch.sh | CLOSEFIL | `scripts/run_full_batch.sh:13` |
| Shell submit | scripts/run_interest_calc.sh | CLOSEFIL | `scripts/run_interest_calc.sh:15` |
| Shell submit | scripts/run_posting.sh | CLOSEFIL | `scripts/run_posting.sh:13` |

## Parameters

Symbols left as parameters (not resolved): `&SYSUID`.

## Sources

- `app/jcl/CLOSEFIL.jcl`
- `docs/_work/structure/jcl/CLOSEFIL.json`
- `docs/_work/jobs/CLOSEFIL.json`

## Confidence

Steps, DDs, conditions and control-data summaries are Confirmed from the JCL. OPEN modes come from the program source. Comments are Unverified.
