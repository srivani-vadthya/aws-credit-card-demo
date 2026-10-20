# PROC TRANREPT

| Item | Value |
|---|---|
| Source | `app/proc/TRANREPT.prc` |
| Member | TRANREPT |
| Job card | `` |
| CLASS / MSGCLASS |  /  |
| NOTIFY |  |
| Job COND |  |
| Steps | 3 |
| Module |  |

PROC/PEND statements: PROC REPROC `app/proc/TRANREPT.prc:1`, PEND  `app/proc/TRANREPT.prc:79`

Executed by: no EXEC PROC= reference in the repository JCL

## Purpose

No descriptive comment in the JCL.

Application programs run by this job: [CBTRN03C](../../07-programs/CBTRN03C.md).

CBTRN03C: CBTRN03C is a batch COBOL program (job TRANREPT, step STEP10R) that prints the 'Daily Transaction Report' (DALYREPT). It reads a start/end date from the DATEPARM file and then reads the posted transaction file TRANFILE sequentially (in TRANREPT.jcl a backup of the transaction master, filtered by date and sorted by card number). For each transaction in the date range it looks up the account id in the card cross-reference (CARDXREF) and the type and category descriptions (TRANTYPE, TRANCATG), and writes a 133-byte detail line to TRANREPT. It prints headers, page totals every 20 lines, an 'Account Total' on every card-number change and a final page total and grand total. Missing reference data or any file error abends the step with code 999. (Inferred, from the program analysis)

## Step flow

```mermaid
flowchart TD
    S0["STEP01R: PROC REPROC"]
    S1["STEP05R: SORT"]
    S0 --> S1
    S2["STEP10R: CBTRN03C"]
    S1 --> S2
```

## Steps

### STEP01R

| Item | Value |
|---|---|
| EXEC | `app/proc/TRANREPT.prc:21-22` |
| Program |  |
| PROC | REPROC |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) |  |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| PRC001.FILEIN | AWS.M2.CARDDEMO.TRANSACT.VSAM.KSDS | SHR |  |  |  | `app/proc/TRANREPT.prc:24-25` |
| PRC001.FILEOUT | AWS.M2.CARDDEMO.TRANSACT.BKUP(+1) | (NEW,CATLG,DELETE) | (LRECL=350,RECFM=FB,BLKSIZE=0) |  |  | `app/proc/TRANREPT.prc:27-31` |

### STEP05R

| Item | Value |
|---|---|
| EXEC | `app/proc/TRANREPT.prc:35` |
| Program | SORT |
| PROC |  |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) |  |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| SORTIN | AWS.M2.CARDDEMO.TRANSACT.BKUP(+1) | SHR |  |  |  | `app/proc/TRANREPT.prc:36-37` |
| SYMNAMES | * |  |  |  | in-stream lines 39-42 | `app/proc/TRANREPT.prc:38` |
| SYSIN | * |  |  |  | in-stream lines 44-46; statements: SORT INCLUDE | `app/proc/TRANREPT.prc:43` |
| SYSOUT | SYSOUT=* |  |  |  |  | `app/proc/TRANREPT.prc:48` |
| SORTOUT | AWS.M2.CARDDEMO.TRANSACT.DALY(+1) | (NEW,CATLG,DELETE) | (*.SORTIN) |  |  | `app/proc/TRANREPT.prc:49-53` |

Datasets supplied by PROC  for this step:

| Dataset | Usage | Line |
|---|---|---|
| AWS.M2.CARDDEMO.TRANSACT.VSAM.KSDS | R | `app/jcl/TRANREPT.jcl:26` |
| AWS.M2.CARDDEMO.TRANSACT.BKUP(+1) | C/D | `app/jcl/TRANREPT.jcl:29` |
| AWS.M2.CARDDEMO.TRANSACT.BKUP(+1) | R | `app/jcl/TRANREPT.jcl:38` |
| AWS.M2.CARDDEMO.TRANSACT.DALY(+1) | C/D | `app/jcl/TRANREPT.jcl:51` |
| AWS.M2.CARDDEMO.CNTL(REPROCT) | R | `app/proc/REPROC.prc:27-28` |

### STEP10R

| Item | Value |
|---|---|
| EXEC | `app/proc/TRANREPT.prc:57` |
| Program | [CBTRN03C](../../07-programs/CBTRN03C.md) |
| PROC |  |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) |  |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| STEPLIB | AWS.M2.CARDDEMO.LOADLIB | SHR |  |  |  | `app/proc/TRANREPT.prc:58-59` |
| SYSOUT | SYSOUT=* |  |  |  |  | `app/proc/TRANREPT.prc:60` |
| SYSPRINT | SYSOUT=* |  |  |  |  | `app/proc/TRANREPT.prc:61` |
| TRANFILE | AWS.M2.CARDDEMO.TRANSACT.DALY(+1) | SHR |  | TRANSACT-FILE OPEN INPUT (`app/cbl/CBTRN03C.cbl:29-31`) |  | `app/proc/TRANREPT.prc:63-64` |
| CARDXREF | AWS.M2.CARDDEMO.CARDXREF.VSAM.KSDS | SHR |  | XREF-FILE OPEN INPUT (`app/cbl/CBTRN03C.cbl:33-37`) |  | `app/proc/TRANREPT.prc:65-66` |
| TRANTYPE | AWS.M2.CARDDEMO.TRANTYPE.VSAM.KSDS | SHR |  | TRANTYPE-FILE OPEN INPUT (`app/cbl/CBTRN03C.cbl:39-43`) |  | `app/proc/TRANREPT.prc:67-68` |
| TRANCATG | AWS.M2.CARDDEMO.TRANCATG.VSAM.KSDS | SHR |  | TRANCATG-FILE OPEN INPUT (`app/cbl/CBTRN03C.cbl:45-49`) |  | `app/proc/TRANREPT.prc:69-70` |
| DATEPARM | AWS.M2.CARDDEMO.DATEPARM | SHR |  | DATE-PARMS-FILE OPEN INPUT (`app/cbl/CBTRN03C.cbl:55-57`) |  | `app/proc/TRANREPT.prc:71-72` |
| TRANREPT | AWS.M2.CARDDEMO.TRANREPT(+1) | (NEW,CATLG,DELETE) | (LRECL=133,RECFM=FB,BLKSIZE=0) | REPORT-FILE OPEN OUTPUT (`app/cbl/CBTRN03C.cbl:51-53`) |  | `app/proc/TRANREPT.prc:74-78` |

Datasets supplied by PROC  for this step:

| Dataset | Usage | Line |
|---|---|---|
| AWS.M2.CARDDEMO.LOADLIB | R | `app/jcl/TRANREPT.jcl:60` |
| AWS.M2.CARDDEMO.TRANSACT.DALY(+1) | R | `app/jcl/TRANREPT.jcl:65` |
| AWS.M2.CARDDEMO.CARDXREF.VSAM.KSDS | R | `app/jcl/TRANREPT.jcl:67` |
| AWS.M2.CARDDEMO.TRANTYPE.VSAM.KSDS | R | `app/jcl/TRANREPT.jcl:69` |
| AWS.M2.CARDDEMO.TRANCATG.VSAM.KSDS | R | `app/jcl/TRANREPT.jcl:71` |
| AWS.M2.CARDDEMO.DATEPARM | R | `app/jcl/TRANREPT.jcl:73` |
| AWS.M2.CARDDEMO.TRANREPT(+1) | C/D | `app/jcl/TRANREPT.jcl:76` |

Return codes and abends set by CBTRN03C: abend via CEE3ABD (`app/cbl/CBTRN03C.cbl:630`).

## Scheduling and dependencies

Not referenced by the CA7 or Control-M exports or the shell scripts (see the gap report).

## Sources

- `app/proc/TRANREPT.prc`
- `docs/_work/structure/jcl/TRANREPT.json`

## Confidence

Steps, DDs, conditions and control-data summaries are Confirmed from the JCL. OPEN modes come from the program source. Comments are Unverified.
