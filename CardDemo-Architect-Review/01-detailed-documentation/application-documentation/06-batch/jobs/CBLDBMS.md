# Job CBLDBMS

| Item | Value |
|---|---|
| Source | `samples/jcl/BMSCMP.jcl` |
| Member | BMSCMP |
| Job card | `samples/jcl/BMSCMP.jcl:1-2` |
| CLASS / MSGCLASS | A / H |
| NOTIFY | &SYSUID |
| Job COND |  |
| Steps | 2 |
| Module | build |

## Purpose

Comment in the JCL (Unverified, `samples/jcl/BMSCMP.jcl:4`): Change CICSMAP to your map name everywhere

## Step flow

```mermaid
flowchart TD
    S0["STEP1: PROC BUILDBMS"]
    S1["SDSF1: SDSF"]
    S0 --> S1
```

## Steps

### STEP1

| Item | Value |
|---|---|
| EXEC | `samples/jcl/BMSCMP.jcl:38` |
| Program |  |
| PROC | BUILDBMS |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) | Executes procedure BUILDBMS |

No DD statements.

### SDSF1

| Item | Value |
|---|---|
| EXEC | `samples/jcl/BMSCMP.jcl:42` |
| Program | SDSF |
| PROC |  |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) | Operator command |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| ISFOUT | SYSOUT=* |  |  |  |  | `samples/jcl/BMSCMP.jcl:43` |
| CMDOUT | SYSOUT=* |  |  |  |  | `samples/jcl/BMSCMP.jcl:44` |
| ISFIN | * |  |  |  | in-stream lines 46-46 | `samples/jcl/BMSCMP.jcl:45` |

## Scheduling and dependencies

Not referenced by the CA7 or Control-M exports or the shell scripts (see the gap report).

## JCL library, INCLUDE and SET

| Statement | Text | Line |
|---|---|---|
| JCLLIB | ORDER=&HLQ..CARDDEMO.PRC.UTIL | `samples/jcl/BMSCMP.jcl:37` |
| SET | HLQ=AWS.M2 | `samples/jcl/BMSCMP.jcl:32` |

## Parameters

Symbols left as parameters (not resolved): `&HLQ`, `&SYSUID`.

## Sources

- `samples/jcl/BMSCMP.jcl`
- `docs/_work/structure/jcl/BMSCMP.json`
- `docs/_work/jobs/CBLDBMS.json`

## Confidence

Steps, DDs, conditions and control-data summaries are Confirmed from the JCL. OPEN modes come from the program source. Comments are Unverified.
