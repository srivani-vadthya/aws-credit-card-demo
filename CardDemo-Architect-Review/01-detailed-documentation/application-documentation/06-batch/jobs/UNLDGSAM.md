# Job UNLDGSAM

| Item | Value |
|---|---|
| Source | `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL` |
| Member | UNLDGSAM |
| Job card | `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:1-2` |
| CLASS / MSGCLASS | A / H |
| NOTIFY | &SYSUID |
| Job COND |  |
| Steps | 1 |
| Module | auth |

## Purpose

Comment in the JCL (Unverified, `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:23`): EXECUTE IMS PROGRAM

Application programs run by this job: [DBUNLDGS](../../07-programs/DBUNLDGS.md).

DBUNLDGS: DBUNLDGS is a batch IMS DL/I utility (entry DLITCBL with PCB masks PAUTBPCB, PASFLPCB and PADFLPCB; run by UNLDGSAM.JCL as DLI with PSB DLIGSAMP) that unloads the pending authorization database to two GSAM datasets. It reads every PAUTSUM0 summary root with unqualified GN calls and, for each summary with a numeric account id, inserts the summary into the summary GSAM PCB (PASFLPCB) and then reads every PAUTDTL1 child with GNP and inserts each into the detail GSAM PCB (PADFLPCB). It stops at end of database ('GB'); any other unexpected status displays diagnostics and ends with RETURN-CODE 16. The sequential-file output variant (OPFILE1/OPFILE2) is commented out. (Inferred, from the program analysis)

## Step flow

```mermaid
flowchart TD
    S0["STEP01: DFSRRC00"]
```

## Steps

### STEP01

| Item | Value |
|---|---|
| EXEC | `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:26-27` |
| Program | DFSRRC00 |
| PROC |  |
| Application program | [DBUNLDGS](../../07-programs/DBUNLDGS.md) via DFSRRC00 PARM |
| PARM | `'DLI,DBUNLDGS,DLIGSAMP,,,,,,,,,,,N'` |
| COND |  |
| Function (earlier pass) | IMS DLI program DBUNLDGS PSB DLIGSAMP |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| STEPLIB | OEMA.IMS.IMSP.SDFSRESL | SHR |  |  |  | `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:28` |
| STEPLIB (concat) | OEMA.IMS.IMSP.SDFSRESL.V151 | SHR |  |  |  | `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:29` |
| STEPLIB (concat) | AWS.M2.CARDDEMO.LOADLIB | SHR |  |  |  | `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:30` |
| DFSRESLB | OEMA.IMS.IMSP.SDFSRESL | SHR |  |  |  | `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:31` |
| IMS | OEM.IMS.IMSP.PSBLIB | SHR |  |  |  | `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:33` |
| IMS (concat) | OEM.IMS.IMSP.DBDLIB | SHR |  |  |  | `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:34` |
| PASFILOP | AWS.M2.CARDDEMO.PAUTDB.ROOT.GSAM | (OLD,KEEP,KEEP) |  |  |  | `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:36-37` |
| PADFILOP | AWS.M2.CARDDEMO.PAUTDB.CHILD.GSAM | (OLD,KEEP,KEEP) |  |  |  | `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:39-40` |
| DDPAUTP0 | OEM.IMS.IMSP.PAUTHDB | SHR |  |  |  | `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:42` |
| DDPAUTX0 | OEM.IMS.IMSP.PAUTHDBX | SHR |  |  |  | `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:43` |
| DFSVSAMP | OEMPP.IMS.V15R01MB.PROCLIB(DFSVSMDB) | SHR |  |  |  | `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:46-47` |
| IMSLOGR | DUMMY |  |  |  |  | `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:48` |
| IEFRDER | DUMMY |  |  |  |  | `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:49` |
| SYSPRINT | SYSOUT=* |  |  |  |  | `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:50` |
| SYSUDUMP | SYSOUT=* |  |  |  |  | `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:51` |
| IMSERR | SYSOUT=* |  |  |  |  | `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:52` |

Return codes and abends set by DBUNLDGS: RETURN-CODE 16 (`app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:362`).

## Scheduling and dependencies

Not referenced by the CA7 or Control-M exports or the shell scripts (see the gap report).

## Parameters

Symbols left as parameters (not resolved): `&SYSUID`.

## Sources

- `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL`
- `docs/_work/structure/jcl/UNLDGSAM.json`
- `docs/_work/jobs/UNLDGSAM.json`

## Confidence

Steps, DDs, conditions and control-data summaries are Confirmed from the JCL. OPEN modes come from the program source. Comments are Unverified.
