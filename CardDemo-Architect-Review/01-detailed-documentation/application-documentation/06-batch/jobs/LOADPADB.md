# Job LOADPADB

| Item | Value |
|---|---|
| Source | `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL` |
| Member | LOADPADB |
| Job card | `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL:1-2` |
| CLASS / MSGCLASS | A / H |
| NOTIFY | &SYSUID |
| Job COND |  |
| Steps | 1 |
| Module | auth |

## Purpose

Comment in the JCL (Unverified, `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL:20`): YLIBS JCLLIB ORDER=VIPINGP.CNTL.PROCLIB

Application programs run by this job: [PAUDBLOD](../../07-programs/PAUDBLOD.md).

PAUDBLOD: PAUDBLOD is a batch IMS DL/I load utility (run by LOADPADB.JCL as BMP with PSB PSBPAUTB) that reloads the pending authorization database from the two sequential files produced by PAUDBUNL. It first reads every summary record from INFILE1 and inserts it as a PAUTSUM0 root, tolerating duplicates ('II'). It then reads every record of INFILE2 (packed account id plus detail); for records with a numeric account key it positions on the parent root with a qualified GU (ACCNTID EQ key) and inserts the PAUTDTL1 child, again tolerating duplicates. Open failures and unexpected insert statuses end the run with RETURN-CODE 16. (Inferred, from the program analysis)

## Step flow

```mermaid
flowchart TD
    S0["STEP01: DFSRRC00"]
```

## Steps

### STEP01

| Item | Value |
|---|---|
| EXEC | `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL:26-27` |
| Program | DFSRRC00 |
| PROC |  |
| Application program | [PAUDBLOD](../../07-programs/PAUDBLOD.md) via DFSRRC00 PARM |
| PARM | `'BMP,PAUDBLOD,PSBPAUTB'` |
| COND |  |
| Function (earlier pass) | IMS BMP program PAUDBLOD PSB PSBPAUTB |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| STEPLIB | OEMA.IMS.IMSP.SDFSRESL | SHR |  |  |  | `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL:28` |
| STEPLIB (concat) | OEMA.IMS.IMSP.SDFSRESL.V151 | SHR |  |  |  | `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL:29` |
| STEPLIB (concat) | AWS.M2.CARDDEMO.LOADLIB | SHR |  |  |  | `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL:30` |
| DFSRESLB | OEMA.IMS.IMSP.SDFSRESL | SHR |  |  |  | `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL:31` |
| IMS | OEM.IMS.IMSP.PSBLIB | SHR |  |  |  | `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL:33` |
| IMS (concat) | OEM.IMS.IMSP.DBDLIB | SHR |  |  |  | `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL:34` |
| INFILE1 | AWS.M2.CARDDEMO.PAUTDB.ROOT.FILEO | SHR |  | INFILE1 OPEN INPUT (`app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:26-29`) |  | `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL:36` |
| INFILE2 | AWS.M2.CARDDEMO.PAUTDB.CHILD.FILEO | SHR |  | INFILE2 OPEN INPUT (`app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:32-35`) |  | `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL:38` |
| DFSVSAMP | OEMPP.IMS.V15R01MB.PROCLIB(DFSVSMDB) | SHR |  |  |  | `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL:44-45` |
| IMSLOGR | DUMMY |  |  |  |  | `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL:46` |
| IEFRDER | DUMMY |  |  |  |  | `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL:47` |
| SYSPRINT | SYSOUT=* |  |  |  |  | `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL:48` |
| SYSUDUMP | SYSOUT=* |  |  |  |  | `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL:49` |
| IMSERR | SYSOUT=* |  |  |  |  | `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL:50` |

Return codes and abends set by PAUDBLOD: RETURN-CODE 16 (`app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:365`).

## Scheduling and dependencies

Not referenced by the CA7 or Control-M exports or the shell scripts (see the gap report).

## Parameters

Symbols left as parameters (not resolved): `&SYSUID`.

## Sources

- `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL`
- `docs/_work/structure/jcl/LOADPADB.json`
- `docs/_work/jobs/LOADPADB.json`

## Confidence

Steps, DDs, conditions and control-data summaries are Confirmed from the JCL. OPEN modes come from the program source. Comments are Unverified.
