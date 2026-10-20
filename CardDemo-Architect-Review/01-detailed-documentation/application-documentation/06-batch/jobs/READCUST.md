# Job READCUST

| Item | Value |
|---|---|
| Source | `app/jcl/READCUST.jcl` |
| Member | READCUST |
| Job card | `app/jcl/READCUST.jcl:1-2` |
| CLASS / MSGCLASS | A / 0 |
| NOTIFY | &SYUID |
| Job COND |  |
| Steps | 1 |
| Module | base |

## Purpose

No descriptive comment in the JCL.

Application programs run by this job: [CBCUS01C](../../07-programs/CBCUS01C.md).

CBCUS01C: CBCUS01C is a batch COBOL utility that prints the customer master file. It opens the indexed file CUSTFILE (500-byte records keyed by 9-digit customer id, layout CVCUS01Y) for sequential input, reads every record into CUSTOMER-RECORD and DISPLAYs it to SYSOUT until end of file. It writes no files. Any open, read or close error displays the file status as NNNN and abends with code 999 via CEE3ABD. (Inferred, from the program analysis)

## Step flow

```mermaid
flowchart TD
    S0["STEP05: CBCUS01C"]
```

## Steps

### STEP05

| Item | Value |
|---|---|
| EXEC | `app/jcl/READCUST.jcl:21` |
| Program | [CBCUS01C](../../07-programs/CBCUS01C.md) |
| PROC |  |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) | Executes program CBCUS01C |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| STEPLIB | AWS.M2.CARDDEMO.LOADLIB | SHR |  |  |  | `app/jcl/READCUST.jcl:22-23` |
| CUSTFILE | AWS.M2.CARDDEMO.CUSTDATA.VSAM.KSDS | SHR |  | CUSTFILE-FILE OPEN INPUT (`app/cbl/CBCUS01C.cbl:29-33`) |  | `app/jcl/READCUST.jcl:24-25` |
| SYSOUT | SYSOUT=* |  |  |  |  | `app/jcl/READCUST.jcl:26` |
| SYSPRINT | SYSOUT=* |  |  |  |  | `app/jcl/READCUST.jcl:27` |

Return codes and abends set by CBCUS01C: abend via CEE3ABD (`app/cbl/CBCUS01C.cbl:158`).

## Scheduling and dependencies

| Mechanism | From | To | Evidence |
|---|---|---|---|
| CA7 trigger | READCARD | READCUST | `app/scheduler/CardDemo.ca7:394` |
| CA7 trigger | READCUST | READXREF | `app/scheduler/CardDemo.ca7:421` |

## Parameters

Symbols left as parameters (not resolved): `&SYUID`.

## Sources

- `app/jcl/READCUST.jcl`
- `docs/_work/structure/jcl/READCUST.json`
- `docs/_work/jobs/READCUST.json`

## Confidence

Steps, DDs, conditions and control-data summaries are Confirmed from the JCL. OPEN modes come from the program source. Comments are Unverified.
