# Job FTPJCLS

| Item | Value |
|---|---|
| Source | `app/jcl/FTPJCL.JCL` |
| Member | FTPJCL |
| Job card | `app/jcl/FTPJCL.JCL:1-2` |
| CLASS / MSGCLASS | A / H |
| NOTIFY | &SYSUID |
| Job COND |  |
| Steps | 1 |
| Module | base |

## Purpose

Comment in the JCL (Unverified, `app/jcl/FTPJCL.JCL:22`): FTP JOB TO RECEIVE A FILE

## Step flow

```mermaid
flowchart TD
    S0["STEP1: FTP"]
```

## Steps

### STEP1

| Item | Value |
|---|---|
| EXEC | `app/jcl/FTPJCL.JCL:30` |
| Program | FTP |
| PROC |  |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) | Utility step FTP |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| SYSIN | * |  |  |  | in-stream lines 33-41; statements: CD PUT QUIT | `app/jcl/FTPJCL.JCL:32` |

## Scheduling and dependencies

Not referenced by the CA7 or Control-M exports or the shell scripts (see the gap report).

## Parameters

Symbols left as parameters (not resolved): `&SYSUID`.

## Sources

- `app/jcl/FTPJCL.JCL`
- `docs/_work/structure/jcl/FTPJCL.json`
- `docs/_work/jobs/FTPJCLS.json`

## Confidence

Steps, DDs, conditions and control-data summaries are Confirmed from the JCL. OPEN modes come from the program source. Comments are Unverified.
