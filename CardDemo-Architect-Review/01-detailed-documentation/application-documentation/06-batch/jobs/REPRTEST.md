# Job REPRTEST

| Item | Value |
|---|---|
| Source | `samples/jcl/REPRTEST.jcl` |
| Member | REPRTEST |
| Job card | `samples/jcl/REPRTEST.jcl:1-2` |
| CLASS / MSGCLASS | A / 0 |
| NOTIFY | &SYSUID |
| Job COND |  |
| Steps | 1 |
| Module | build |

## Purpose

Comment in the JCL (Unverified, `samples/jcl/REPRTEST.jcl:20`): CALL THE REPRO PROC

## Step flow

```mermaid
flowchart TD
    S0["STEP05: PROC REPROC"]
```

## Steps

### STEP05

| Item | Value |
|---|---|
| EXEC | `samples/jcl/REPRTEST.jcl:23-24` |
| Program |  |
| PROC | REPROC |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) | Executes procedure REPROC (IDCAMS REPRO) |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| PRC001.FILEIN | AWS.M2.CARDDEMO.TRANSACT.VSAM.KSDS | SHR |  |  |  | `samples/jcl/REPRTEST.jcl:26-27` |
| PRC001.FILEOUT | AWS.M2.CARDDEMO.TRANSACT.BKUP(+1) | (NEW,CATLG,DELETE) | (LRECL=350,RECFM=FB,BLKSIZE=0) |  |  | `samples/jcl/REPRTEST.jcl:29-33` |

Datasets supplied by PROC REPROC for this step:

| Dataset | Usage | Line |
|---|---|---|
| AWS.M2.CARDDEMO.CNTL(REPROCT) | R | `app/proc/REPROC.prc:27-28` |

## Scheduling and dependencies

Not referenced by the CA7 or Control-M exports or the shell scripts (see the gap report).

## JCL library, INCLUDE and SET

| Statement | Text | Line |
|---|---|---|
| JCLLIB | ORDER=('AWS.M2.CARDDEMO.PROC') | `samples/jcl/REPRTEST.jcl:22` |

## Parameters

Symbols left as parameters (not resolved): `&SYSUID`.

## Sources

- `samples/jcl/REPRTEST.jcl`
- `docs/_work/structure/jcl/REPRTEST.json`
- `docs/_work/jobs/REPRTEST.json`

## Confidence

Steps, DDs, conditions and control-data summaries are Confirmed from the JCL. OPEN modes come from the program source. Comments are Unverified.
