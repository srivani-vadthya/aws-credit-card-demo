# Job DEFCUST

| Item | Value |
|---|---|
| Source | `app/jcl/DEFCUST.jcl` |
| Member | DEFCUST |
| Job card | `app/jcl/DEFCUST.jcl:1-2` |
| CLASS / MSGCLASS | A / 0 |
| NOTIFY | &SYSUID |
| Job COND |  |
| Steps | 2 |
| Module | base |

## Purpose

Comment in the JCL (Unverified, `app/jcl/DEFCUST.jcl:20`): DELETE CUSTOMER VSAM FILE IF ONE ALREADY EXISTS

## Step flow

```mermaid
flowchart TD
    S0["STEP05: IDCAMS"]
    S1["STEP05: IDCAMS"]
    S0 --> S1
```

## Steps

### STEP05

| Item | Value |
|---|---|
| EXEC | `app/jcl/DEFCUST.jcl:22` |
| Program | IDCAMS |
| PROC |  |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) | IDCAMS delete |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| SYSPRINT | SYSOUT=* |  |  |  |  | `app/jcl/DEFCUST.jcl:23` |
| SYSIN | * |  |  |  | in-stream lines 25-26; statements: DELETE | `app/jcl/DEFCUST.jcl:24` |

### STEP05

| Item | Value |
|---|---|
| EXEC | `app/jcl/DEFCUST.jcl:32` |
| Program | IDCAMS |
| PROC |  |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) | IDCAMS define VSAM cluster |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| SYSPRINT | SYSOUT=* |  |  |  |  | `app/jcl/DEFCUST.jcl:33` |
| SYSIN | * |  |  |  | in-stream lines 35-46; statements: DEFINE; NAME(): AWS.CUSTDATA.CLUSTER AWS.CUSTDATA.CLUSTER.DATA AWS.CUSTDATA.CLUSTER.INDEX | `app/jcl/DEFCUST.jcl:34` |

## Scheduling and dependencies

Not referenced by the CA7 or Control-M exports or the shell scripts (see the gap report).

## Parameters

Symbols left as parameters (not resolved): `&SYSUID`.

## Sources

- `app/jcl/DEFCUST.jcl`
- `docs/_work/structure/jcl/DEFCUST.json`
- `docs/_work/jobs/DEFCUST.json`

## Confidence

Steps, DDs, conditions and control-data summaries are Confirmed from the JCL. OPEN modes come from the program source. Comments are Unverified.
