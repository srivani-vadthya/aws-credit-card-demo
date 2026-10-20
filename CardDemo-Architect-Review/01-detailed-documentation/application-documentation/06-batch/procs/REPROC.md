# PROC REPROC

| Item | Value |
|---|---|
| Source | `app/proc/REPROC.prc` |
| Member | REPROC |
| Job card | `` |
| CLASS / MSGCLASS |  /  |
| NOTIFY |  |
| Job COND |  |
| Steps | 1 |
| Module |  |

PROC/PEND statements: PROC REPROC `app/proc/REPROC.prc:1`, PEND  `app/proc/REPROC.prc:29`

Executed by: PRTCATBL step STEP05R (`app/jcl/PRTCATBL.jcl:29-30`); TRANBKP step STEP05R (`app/jcl/TRANBKP.jcl:23-24`); TRANREPT step STEP05R (`app/jcl/TRANREPT.jcl:23-24`); TRANREPT step STEP01R (`app/proc/TRANREPT.prc:21-22`); REPRTEST step STEP05 (`samples/jcl/REPRTEST.jcl:23-24`)

## Purpose

No descriptive comment in the JCL.

## Step flow

```mermaid
flowchart TD
    S0["PRC001: IDCAMS"]
```

## Steps

### PRC001

| Item | Value |
|---|---|
| EXEC | `app/proc/REPROC.prc:21` |
| Program | IDCAMS |
| PROC |  |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) |  |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| SYSPRINT | SYSOUT=* |  |  |  |  | `app/proc/REPROC.prc:22` |
| FILEIN | NULLFILE | SHR |  |  |  | `app/proc/REPROC.prc:23-24` |
| FILEOUT | NULLFILE | SHR |  |  |  | `app/proc/REPROC.prc:25-26` |
| SYSIN | &CNTLLIB(REPROCT) | SHR |  |  |  | `app/proc/REPROC.prc:27-28` |

## Scheduling and dependencies

Not referenced by the CA7 or Control-M exports or the shell scripts (see the gap report).

## Parameters

Symbols left as parameters (not resolved): `&CNTLLIB`.

## Sources

- `app/proc/REPROC.prc`
- `docs/_work/structure/jcl/REPROC.json`

## Confidence

Steps, DDs, conditions and control-data summaries are Confirmed from the JCL. OPEN modes come from the program source. Comments are Unverified.
