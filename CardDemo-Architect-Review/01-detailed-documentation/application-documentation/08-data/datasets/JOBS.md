# Dataset JOBS

| Item | Value |
|---|---|
| DSN | JOBS |
| Organisation | cics-tdq |
| Key offset |  |
| Key length |  |
| Defined by |  |
| Layout |  |
| Record |  |
| Record length |  |
| CICS FILE |  |
| Catalog as of |  |
| Catalog rec total |  |

## Purpose

This name is recorded with store kind cics-tdq. It is an extrapartition transient data queue: `TYPE(EXTRA) DDNAME(INREADER) TYPEFILE(OUTPUT) RECORDSIZE(80) RECORDFORMAT(FIXED)` (`app/csd/CARDDEMO.CSD:499-503`). Confirmed.

It receives the 80-byte JCL lines of job `TRNRPT00`, which executes PROC `TRANREPT` (`app/cbl/CORPT00C.cbl:83-94`, `app/cbl/CORPT00C.cbl:497-520`). Confirmed. The CICS region JCL that defines DD `INREADER` is not in the repository. The CSD description `SUBMIT JOBS FROM CICS` (`app/csd/CARDDEMO.CSD:500`) is Unverified.

## Access

| Program / job step | Access | Via | Evidence |
|---|---|---|---|
| [CORPT00C](../../07-programs/CORPT00C.md) | C | WRITEQ TD, one line per write, job `TRNRPT00` | app/cbl/CORPT00C.cbl:517 |

## Lifecycle

Accessors above are the JCL and CICS references recorded for this name. A shared record length was not used to invent extra links.

## Consistency

No length check was recorded.

## Sources

- `app/csd/CARDDEMO.CSD:499-503`
- `app/cbl/CORPT00C.cbl:83-94`
- `app/cbl/CORPT00C.cbl:497-520`
- `docs/_work/datasets/JOBS.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
