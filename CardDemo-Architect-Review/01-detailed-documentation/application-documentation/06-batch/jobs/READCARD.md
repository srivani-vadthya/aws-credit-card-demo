# Job READCARD

| Item | Value |
|---|---|
| Source | `app/jcl/READCARD.jcl` |
| Member | READCARD |
| Job card | `app/jcl/READCARD.jcl:1-2` |
| CLASS / MSGCLASS | A / 0 |
| NOTIFY | &SYSUID |
| Job COND |  |
| Steps | 1 |
| Module | base |

## Purpose

Comment in the JCL (Unverified, `app/jcl/READCARD.jcl:20`): RUN THE PROGRAM THAT READS THE CARD MASTER VSAM FILE

Application programs run by this job: [CBACT02C](../../07-programs/CBACT02C.md).

CBACT02C: CBACT02C is a batch COBOL utility that prints the card master file. It opens the indexed card file CARDFILE (150-byte records keyed by card number, layout CVACT02Y) for sequential input, reads every record into CARD-RECORD and DISPLAYs it to SYSOUT until end of file. It writes no files. Any open, read or close error displays the file status as NNNN and abends with code 999 via CEE3ABD. (Inferred, from the program analysis)

## Step flow

```mermaid
flowchart TD
    S0["STEP05: CBACT02C"]
```

## Steps

### STEP05

| Item | Value |
|---|---|
| EXEC | `app/jcl/READCARD.jcl:22` |
| Program | [CBACT02C](../../07-programs/CBACT02C.md) |
| PROC |  |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) | Executes program CBACT02C |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| STEPLIB | AWS.M2.CARDDEMO.LOADLIB | SHR |  |  |  | `app/jcl/READCARD.jcl:23-24` |
| CARDFILE | AWS.M2.CARDDEMO.CARDDATA.VSAM.KSDS | SHR |  | CARDFILE-FILE OPEN INPUT (`app/cbl/CBACT02C.cbl:29-33`) |  | `app/jcl/READCARD.jcl:25-26` |
| SYSOUT | SYSOUT=* |  |  |  |  | `app/jcl/READCARD.jcl:27` |
| SYSPRINT | SYSOUT=* |  |  |  |  | `app/jcl/READCARD.jcl:28` |

Return codes and abends set by CBACT02C: abend via CEE3ABD (`app/cbl/CBACT02C.cbl:158`).

## Scheduling and dependencies

| Mechanism | From | To | Evidence |
|---|---|---|---|
| CA7 trigger | READACCT | READCARD | `app/scheduler/CardDemo.ca7:367` |
| CA7 trigger | READCARD | READCUST | `app/scheduler/CardDemo.ca7:394` |

## Parameters

Symbols left as parameters (not resolved): `&SYSUID`.

## Sources

- `app/jcl/READCARD.jcl`
- `docs/_work/structure/jcl/READCARD.json`
- `docs/_work/jobs/READCARD.json`

## Confidence

Steps, DDs, conditions and control-data summaries are Confirmed from the JCL. OPEN modes come from the program source. Comments are Unverified.
