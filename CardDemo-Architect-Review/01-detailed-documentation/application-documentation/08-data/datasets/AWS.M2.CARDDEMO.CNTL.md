# Dataset AWS.M2.CARDDEMO.CNTL

| Item | Value |
|---|---|
| DSN | AWS.M2.CARDDEMO.CNTL |
| Organisation | sequential |
| Key offset |  |
| Key length |  |
| Defined by |  |
| Layout |  |
| Record |  |
| Record length |  |
| CICS FILE |  |
| Catalog as of | 09/01/22 |
| Catalog rec total |  |

## Purpose

This name is recorded with store kind sequential. LISTCAT lists it as `NONVSAM` (`app/catlg/LISTCAT.txt:552`). JCL refers to it with a member name, `(REPROCT)` (`app/proc/REPROC.prc:28`), so it is used as a partitioned data set. Inferred from those two facts.

It holds the IDCAMS control member `REPROCT`, read as `SYSIN` by the `REPROC` procedure. The statement is `REPRO INFILE(FILEIN) OUTFILE(FILEOUT)` (`app/ctl/REPROCT.ctl:15`). An identical copy is `app/app-transaction-type-db2/ctl/REPROCT.ctl:15`. Which repository file is loaded into this library is not stated; see [gaps](../../16-gaps-assumptions-open-questions.md).

## Access

| Program / job step | Access | Via | Evidence |
|---|---|---|---|
| [TRANBKP](../../06-batch/jobs/TRANBKP.md) STEP05R, DD PRC001.SYSIN | R | PROC REPROC, `CNTLLIB` override | `app/jcl/TRANBKP.jcl:24`, `app/proc/REPROC.prc:27-28` |
| [TRANREPT](../../06-batch/jobs/TRANREPT.md) STEP05R (line 23), DD PRC001.SYSIN | R | PROC REPROC, `CNTLLIB` override | `app/jcl/TRANREPT.jcl:24`, `app/proc/REPROC.prc:27-28` |
| [PRTCATBL](../../06-batch/jobs/PRTCATBL.md) STEP05R, DD PRC001.SYSIN | R | PROC REPROC, `CNTLLIB` override | `app/jcl/PRTCATBL.jcl:30`, `app/proc/REPROC.prc:27-28` |
| [REPRTEST](../../06-batch/jobs/REPRTEST.md) STEP05, DD PRC001.SYSIN | R | PROC REPROC, `CNTLLIB` override | `samples/jcl/REPRTEST.jcl:24`, `app/proc/REPROC.prc:27-28` |

The PROC member `TRANREPT` (`app/proc/TRANREPT.prc`) also executes `REPROC` with `CNTLLIB=AWS.M2.CARDDEMO.CNTL` (`app/proc/TRANREPT.prc:21-22`). That PROC is run by job `TRNRPT00`, whose JCL lines [CORPT00C](../../07-programs/CORPT00C.md) writes to TD queue `JOBS` (`app/cbl/CORPT00C.cbl:94`). Confirmed.

## Lifecycle

Accessors above are the JCL and CICS references recorded for this name. A shared record length was not used to invent extra links.

## Consistency

No length check was recorded.

## Sources

- `app/catlg/LISTCAT.txt:552`
- `app/proc/REPROC.prc:27-28`
- `app/proc/TRANREPT.prc:21-22`
- `app/ctl/REPROCT.ctl:15`
- `app/app-transaction-type-db2/ctl/REPROCT.ctl:15`
- `app/jcl/TRANBKP.jcl:24`
- `app/jcl/TRANREPT.jcl:24`
- `app/jcl/PRTCATBL.jcl:30`
- `samples/jcl/REPRTEST.jcl:24`
- `docs/_work/datasets/AWS.M2.CARDDEMO.CNTL.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
