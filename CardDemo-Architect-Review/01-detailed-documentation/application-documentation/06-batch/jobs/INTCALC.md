# Job INTCALC

| Item | Value |
|---|---|
| Source | `app/jcl/INTCALC.jcl` |
| Member | INTCALC |
| Job card | `app/jcl/INTCALC.jcl:1-2` |
| CLASS / MSGCLASS | A / 0 |
| NOTIFY | &SYSUID |
| Job COND |  |
| Steps | 1 |
| Module | base |

## Purpose

Comment in the JCL (Unverified, `app/jcl/INTCALC.jcl:20`): Process transaction balance file and compute interest and fees.

Application programs run by this job: [CBACT04C](../../07-programs/CBACT04C.md).

CBACT04C: CBACT04C is the batch interest calculator. It reads the transaction category balance file TCATBALF sequentially (records grouped by account id) and, for each category, looks up the annual interest rate in the disclosure group file DISCGRP by account group, transaction type and category, falling back to the 'DEFAULT' group. For non-zero rates it computes monthly interest as balance x rate / 1200 and writes an interest transaction (type '01', category 5) to the sequential TRANSACT file, using the run date passed in PARM-DATE to build transaction ids. At each change of account it adds the accumulated interest to the account balance in ACCTFILE (opened I-O), resets the cycle credit and debit totals and rewrites the account. Missing accounts, cross-references or default rates and any I/O error abend the job with code 999. (Inferred, from the program analysis)

## Step flow

```mermaid
flowchart TD
    S0["STEP15: CBACT04C"]
```

## Steps

### STEP15

| Item | Value |
|---|---|
| EXEC | `app/jcl/INTCALC.jcl:22` |
| Program | [CBACT04C](../../07-programs/CBACT04C.md) |
| PROC |  |
| Application program |  |
| PARM | `'2022071800'` |
| COND |  |
| Function (earlier pass) | Executes program CBACT04C |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| STEPLIB | AWS.M2.CARDDEMO.LOADLIB | SHR |  |  |  | `app/jcl/INTCALC.jcl:23-24` |
| SYSPRINT | SYSOUT=* |  |  |  |  | `app/jcl/INTCALC.jcl:25` |
| SYSOUT | SYSOUT=* |  |  |  |  | `app/jcl/INTCALC.jcl:26` |
| TCATBALF | AWS.M2.CARDDEMO.TCATBALF.VSAM.KSDS | SHR |  | TCATBAL-FILE OPEN INPUT (`app/cbl/CBACT04C.cbl:28-32`) |  | `app/jcl/INTCALC.jcl:27-28` |
| XREFFILE | AWS.M2.CARDDEMO.CARDXREF.VSAM.KSDS | SHR |  | XREF-FILE OPEN INPUT (`app/cbl/CBACT04C.cbl:34-39`) |  | `app/jcl/INTCALC.jcl:29-30` |
| XREFFIL1 | AWS.M2.CARDDEMO.CARDXREF.VSAM.AIX.PATH | SHR |  |  |  | `app/jcl/INTCALC.jcl:31-32` |
| ACCTFILE | AWS.M2.CARDDEMO.ACCTDATA.VSAM.KSDS | SHR |  | ACCOUNT-FILE OPEN I-O (`app/cbl/CBACT04C.cbl:41-45`) |  | `app/jcl/INTCALC.jcl:33-34` |
| DISCGRP | AWS.M2.CARDDEMO.DISCGRP.VSAM.KSDS | SHR |  | DISCGRP-FILE OPEN INPUT (`app/cbl/CBACT04C.cbl:47-51`) |  | `app/jcl/INTCALC.jcl:35-36` |
| TRANSACT | AWS.M2.CARDDEMO.SYSTRAN(+1) | (NEW,CATLG,DELETE) | (RECFM=F,LRECL=350,BLKSIZE=0) | TRANSACT-FILE OPEN OUTPUT (`app/cbl/CBACT04C.cbl:53-56`) |  | `app/jcl/INTCALC.jcl:37-41` |

Return codes and abends set by CBACT04C: abend via CEE3ABD (`app/cbl/CBACT04C.cbl:632`).

## Scheduling and dependencies

| Mechanism | From | To | Evidence |
|---|---|---|---|
| Control-M condition MONTHLY-InterestCalculation-CLOSEFIL | CLOSEFIL | INTCALC | `app/scheduler/CardDemo.controlm:66` (OUTCOND), `app/scheduler/CardDemo.controlm:70` (INCOND) |
| Control-M condition MONTHLY-InterestCalculation-INTCALC | INTCALC | COMBTRAN | `app/scheduler/CardDemo.controlm:72` (OUTCOND), `app/scheduler/CardDemo.controlm:76` (INCOND) |
| Shell submit | scripts/run_full_batch.sh | INTCALC | `scripts/run_full_batch.sh:51` |
| Shell submit | scripts/run_interest_calc.sh | INTCALC | `scripts/run_interest_calc.sh:19` |

## Parameters

Symbols left as parameters (not resolved): `&SYSUID`.

## Sources

- `app/jcl/INTCALC.jcl`
- `docs/_work/structure/jcl/INTCALC.json`
- `docs/_work/jobs/INTCALC.json`

## Confidence

Steps, DDs, conditions and control-data summaries are Confirmed from the JCL. OPEN modes come from the program source. Comments are Unverified.
