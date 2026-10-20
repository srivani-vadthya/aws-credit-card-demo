# Job CBPAUP0J

| Item | Value |
|---|---|
| Source | `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl` |
| Member | CBPAUP0J |
| Job card | `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:1-2` |
| CLASS / MSGCLASS | A / H |
| NOTIFY | &SYSUID |
| Job COND |  |
| Steps | 1 |
| Module | auth |

## Purpose

Comment in the JCL (Unverified, `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:21`): EXECUTE IMS PROGRAM TO DELETE EXPIRED AUTHORIZATIONS

Application programs run by this job: [CBPAUP0C](../../07-programs/CBPAUP0C.md).

CBPAUP0C: CBPAUP0C is a batch IMS DL/I program (PSB name PSBPAUTB in working storage, PCB number 2) that purges expired pending authorizations from the pending-authorization IMS database. It reads a SYSIN parameter card (expiry days, checkpoint frequency, checkpoint display frequency, debug flag) and applies defaults when values are missing. It walks every PAUTSUM0 summary root segment with GN and, for each, every PAUTDTL1 child detail with GNP; a detail whose age in days (current YYDDD minus the un-complemented authorization date) reaches the expiry threshold is deleted with DLET and its amount/count is backed out of the in-memory summary counters. After the children are processed, the summary is deleted when its approved count is zero or less. IMS checkpoints (CHKP with id 'RMAD'+counter) are taken every P-CHKP-FREQ summaries and at end of run; read/delete totals are displayed and any unexpected DL/I status ends the run with RETURN-CODE 16. (Inferred, from the program analysis)

## Step flow

```mermaid
flowchart TD
    S0["STEP01: DFSRRC00"]
```

## Steps

### STEP01

| Item | Value |
|---|---|
| EXEC | `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:24-25` |
| Program | DFSRRC00 |
| PROC |  |
| Application program | [CBPAUP0C](../../07-programs/CBPAUP0C.md) via DFSRRC00 PARM |
| PARM | `'BMP,CBPAUP0C,PSBPAUTB'` |
| COND |  |
| Function (earlier pass) | IMS BMP program CBPAUP0C PSB PSBPAUTB |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| STEPLIB | IMS.SDFSRESL | SHR |  |  |  | `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:26` |
| STEPLIB (concat) | XXXXXXXX.PROD.LOADLIB | SHR |  |  |  | `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:27` |
| DFSRESLB | IMS.SDFSRESL | SHR |  |  |  | `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:28` |
| PROCLIB | IMS.PROCLIB | SHR |  |  |  | `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:29` |
| DFSSEL | IMS.SDFSRESL | SHR |  |  |  | `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:31` |
| IMS | IMS.PSBLIB | SHR |  |  |  | `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:33` |
| IMS (concat) | IMS.DBDLIB | SHR |  |  |  | `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:34` |
| SYSIN | * |  |  |  | in-stream lines 37-37 | `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:36` |
| SYSOUX | SYSOUT=* |  |  |  |  | `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:39` |
| SYSOUT | SYSOUT=* |  |  |  |  | `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:40` |
| SYSABOUT | SYSOUT=* |  |  |  |  | `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:41` |
| ABENDAID | SYSOUT=* |  |  |  |  | `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:42` |
| IEFRDER | DUMMY |  |  |  |  | `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:43` |
| IMSLOGR | DUMMY |  |  |  |  | `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:44` |
| SYSPRINT | SYSOUT=* |  |  |  |  | `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:45` |
| SYSUDUMP | SYSOUT=* |  |  |  |  | `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:46` |
| IMSERR | SYSOUT=* |  |  |  |  | `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:47` |

Return codes and abends set by CBPAUP0C: RETURN-CODE 16 (`app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:382`).

## Scheduling and dependencies

| Mechanism | From | To | Evidence |
|---|---|---|---|
| CA7 trigger | CLOSEFIL | CBPAUP0J | `app/scheduler/CardDemo.ca7:43` |
| CA7 trigger | CBPAUP0J | POSTTRAN | `app/scheduler/CardDemo.ca7:70` |

## Parameters

Symbols left as parameters (not resolved): `&SYSUID`.

## Sources

- `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl`
- `docs/_work/structure/jcl/CBPAUP0J.json`
- `docs/_work/jobs/CBPAUP0J.json`

## Confidence

Steps, DDs, conditions and control-data summaries are Confirmed from the JCL. OPEN modes come from the program source. Comments are Unverified.
