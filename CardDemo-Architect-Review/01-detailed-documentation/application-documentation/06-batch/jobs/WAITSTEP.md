# Job WAITSTEP

| Item | Value |
|---|---|
| Source | `app/jcl/WAITSTEP.jcl` |
| Member | WAITSTEP |
| Job card | `app/jcl/WAITSTEP.jcl:1-2` |
| CLASS / MSGCLASS | A / 0 |
| NOTIFY | &SYSUID |
| Job COND |  |
| Steps | 1 |
| Module | base |

## Purpose

Comment in the JCL (Unverified, `app/jcl/WAITSTEP.jcl:20`): WAIT FOR CENTISECONDS IN THE PARM EG: 00003600  = 36 SECONDS

Application programs run by this job: [COBSWAIT](../../07-programs/COBSWAIT.md).

COBSWAIT: COBSWAIT is a small batch utility that pauses a job step. It ACCEPTs an 8-character value from SYSIN, moves it to the binary field MVSWAIT-TIME and CALLs the external routine MVSWAIT with it, then ends with STOP RUN. The header comment states the value is a wait time in centiseconds. It has no files, no conditions and no business logic; it is executed by job step WAIT in app/jcl/WAITSTEP.jcl. (Inferred, from the program analysis)

## Step flow

```mermaid
flowchart TD
    S0["WAIT: COBSWAIT"]
```

## Steps

### WAIT

| Item | Value |
|---|---|
| EXEC | `app/jcl/WAITSTEP.jcl:22` |
| Program | [COBSWAIT](../../07-programs/COBSWAIT.md) |
| PROC |  |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) | Executes program COBSWAIT |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| STEPLIB | AWS.M2.CARDDEMO.LOADLIB | SHR |  |  |  | `app/jcl/WAITSTEP.jcl:23` |
| SYSOUT | SYSOUT=* |  |  |  |  | `app/jcl/WAITSTEP.jcl:24` |
| SYSIN | * |  |  |  | in-stream lines 26-26 | `app/jcl/WAITSTEP.jcl:25` |

## Scheduling and dependencies

| Mechanism | From | To | Evidence |
|---|---|---|---|
| CA7 trigger | POSTTRAN | WAITSTEP | `app/scheduler/CardDemo.ca7:97` |
| CA7 trigger | WAITSTEP | OPENFIL | `app/scheduler/CardDemo.ca7:124` |
| CA7 trigger | TRANTYPE | WAITSTEP | `app/scheduler/CardDemo.ca7:189` |
| CA7 trigger | WAITSTEP | CLOSEFIL1 | `app/scheduler/CardDemo.ca7:216` |
| CA7 trigger | WAITSTEP | CLOSEFIL2 | `app/scheduler/CardDemo.ca7:217` |
| CA7 trigger | TRANCATG | WAITSTEP | `app/scheduler/CardDemo.ca7:298` |
| CA7 trigger | WAITSTEP | CLOSEFIL | `app/scheduler/CardDemo.ca7:303` |
| CA7 trigger | TCATBALF | WAITSTEP | `app/scheduler/CardDemo.ca7:330` |
| CA7 trigger | WAITSTEP | CLOSEFIL | `app/scheduler/CardDemo.ca7:335` |
| CA7 trigger | READXREF | WAITSTEP | `app/scheduler/CardDemo.ca7:448` |
| CA7 trigger | WAITSTEP | OPENFIL | `app/scheduler/CardDemo.ca7:453` |
| CA7 trigger | TXT2PDF1 | WAITSTEP | `app/scheduler/CardDemo.ca7:522` |
| CA7 trigger | WAITSTEP | OPENFIL | `app/scheduler/CardDemo.ca7:527` |
| CA7 trigger | PRTCATBL | WAITSTEP | `app/scheduler/CardDemo.ca7:564` |
| CA7 trigger | WAITSTEP | OPENFIL | `app/scheduler/CardDemo.ca7:569` |
| Control-M condition DAILY-TransactionBackup-TRANBKP | TRANBKP | WAITSTEP | `app/scheduler/CardDemo.controlm:11` (OUTCOND), `app/scheduler/CardDemo.controlm:15` (INCOND) |
| Control-M condition DAILY-TransactionBackup-WAITSTEP | WAITSTEP | OPENFIL | `app/scheduler/CardDemo.controlm:17` (OUTCOND), `app/scheduler/CardDemo.controlm:21` (INCOND) |
| Control-M condition MONTHLY-InterestCalculation-COMBTRAN | COMBTRAN | WAITSTEP | `app/scheduler/CardDemo.controlm:78` (OUTCOND), `app/scheduler/CardDemo.controlm:82` (INCOND) |
| Control-M condition MONTHLY-InterestCalculation-WAITSTEP | WAITSTEP | OPENFIL | `app/scheduler/CardDemo.controlm:84` (OUTCOND), `app/scheduler/CardDemo.controlm:88` (INCOND) |
| Control-M condition WEEKLY-DisclosureGroupsRefresh-DISCGRP | DISCGRP | WAITSTEP | `app/scheduler/CardDemo.controlm:41` (OUTCOND), `app/scheduler/CardDemo.controlm:45` (INCOND) |
| Control-M condition WEEKLY-DisclosureGroupsRefresh-WAITSTEP | WAITSTEP | OPENFIL | `app/scheduler/CardDemo.controlm:47` (OUTCOND), `app/scheduler/CardDemo.controlm:51` (INCOND) |

## Parameters

Symbols left as parameters (not resolved): `&SYSUID`.

## Sources

- `app/jcl/WAITSTEP.jcl`
- `docs/_work/structure/jcl/WAITSTEP.json`
- `docs/_work/jobs/WAITSTEP.json`

## Confidence

Steps, DDs, conditions and control-data summaries are Confirmed from the JCL. OPEN modes come from the program source. Comments are Unverified.
