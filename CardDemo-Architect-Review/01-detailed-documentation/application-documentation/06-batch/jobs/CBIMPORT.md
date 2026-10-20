# Job CBIMPORT

| Item | Value |
|---|---|
| Source | `app/jcl/CBIMPORT.jcl` |
| Member | CBIMPORT |
| Job card | `app/jcl/CBIMPORT.jcl:1-2` |
| CLASS / MSGCLASS | A / 0 |
| NOTIFY | &SYSUID |
| Job COND |  |
| Steps | 1 |
| Module | base |

## Purpose

No descriptive comment in the JCL.

Application programs run by this job: [CBIMPORT](../../07-programs/CBIMPORT.md).

CBIMPORT: CBIMPORT is the batch counterpart of CBEXPORT for branch migration. It reads the 500-byte multi-record export file EXPFILE (layout CVEXPORT) and splits it by record type into sequential customer (CUSTOUT), account (ACCTOUT), card cross-reference (XREFOUT), transaction (TRNXOUT) and card (CARDOUT) files in the standard CardDemo layouts, unpacking COMP/COMP-3 fields. Records with an unknown type are logged to the 132-byte error file ERROUT and skipped. The validation step is a stub that always reports no errors. It ends by displaying read, import, error and unknown-type counts; open, read and master-file write errors abend the run via CEE3ABD. (Inferred, from the program analysis)

## Step flow

```mermaid
flowchart TD
    S0["STEP01: CBIMPORT"]
```

## Steps

### STEP01

| Item | Value |
|---|---|
| EXEC | `app/jcl/CBIMPORT.jcl:22` |
| Program | [CBIMPORT](../../07-programs/CBIMPORT.md) |
| PROC |  |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) | Executes program CBIMPORT |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| STEPLIB | AWS.M2.CARDDEMO.LOADLIB | SHR |  |  |  | `app/jcl/CBIMPORT.jcl:23-24` |
| EXPFILE | AWS.M2.CARDDEMO.EXPORT.DATA | SHR |  | EXPORT-INPUT OPEN INPUT (`app/cbl/CBIMPORT.cbl:37-41`) |  | `app/jcl/CBIMPORT.jcl:28-29` |
| CUSTOUT | AWS.M2.CARDDEMO.CUSTDATA.IMPORT | (NEW,CATLG,DELETE) | (RECFM=FB,LRECL=500,BLKSIZE=0) | CUSTOMER-OUTPUT OPEN OUTPUT (`app/cbl/CBIMPORT.cbl:43-46`) |  | `app/jcl/CBIMPORT.jcl:33-37` |
| ACCTOUT | AWS.M2.CARDDEMO.ACCTDATA.IMPORT | (NEW,CATLG,DELETE) | (RECFM=FB,LRECL=300,BLKSIZE=0) | ACCOUNT-OUTPUT OPEN OUTPUT (`app/cbl/CBIMPORT.cbl:48-51`) |  | `app/jcl/CBIMPORT.jcl:38-42` |
| XREFOUT | AWS.M2.CARDDEMO.CARDXREF.IMPORT | (NEW,CATLG,DELETE) | (RECFM=FB,LRECL=50,BLKSIZE=0) | XREF-OUTPUT OPEN OUTPUT (`app/cbl/CBIMPORT.cbl:53-56`) |  | `app/jcl/CBIMPORT.jcl:43-47` |
| TRNXOUT | AWS.M2.CARDDEMO.TRANSACT.IMPORT | (NEW,CATLG,DELETE) | (RECFM=FB,LRECL=350,BLKSIZE=0) | TRANSACTION-OUTPUT OPEN OUTPUT (`app/cbl/CBIMPORT.cbl:58-61`) |  | `app/jcl/CBIMPORT.jcl:48-52` |
| ERROUT | AWS.M2.CARDDEMO.IMPORT.ERRORS | (NEW,CATLG,DELETE) | (RECFM=FB,LRECL=132,BLKSIZE=0) | ERROR-OUTPUT OPEN OUTPUT (`app/cbl/CBIMPORT.cbl:68-71`) |  | `app/jcl/CBIMPORT.jcl:56-60` |
| SYSOUT | SYSOUT=* |  |  |  |  | `app/jcl/CBIMPORT.jcl:64` |
| SYSPRINT | SYSOUT=* |  |  |  |  | `app/jcl/CBIMPORT.jcl:65` |

Return codes and abends set by CBIMPORT: abend via CEE3ABD (`app/cbl/CBIMPORT.cbl:484`).

## Scheduling and dependencies

Not referenced by the CA7 or Control-M exports or the shell scripts (see the gap report).

## Parameters

Symbols left as parameters (not resolved): `&SYSUID`.

## Sources

- `app/jcl/CBIMPORT.jcl`
- `docs/_work/structure/jcl/CBIMPORT.json`
- `docs/_work/jobs/CBIMPORT.json`

## Confidence

Steps, DDs, conditions and control-data summaries are Confirmed from the JCL. OPEN modes come from the program source. Comments are Unverified.
