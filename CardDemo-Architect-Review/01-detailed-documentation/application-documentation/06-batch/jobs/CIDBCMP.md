# Job CIDBCMP

| Item | Value |
|---|---|
| Source | `samples/jcl/CICDBCMP.jcl` |
| Member | CICDBCMP |
| Job card | `samples/jcl/CICDBCMP.jcl:1-2` |
| CLASS / MSGCLASS | A / H |
| NOTIFY | &SYSUID |
| Job COND |  |
| Steps | 1 |
| Module | build |

## Purpose

Comment in the JCL (Unverified, `samples/jcl/CICDBCMP.jcl:4`): change CICSDB2P to your program name everywhere

## Step flow

```mermaid
flowchart TD
    S0["CICSCMP: PROC BLDCIDB2"]
```

## Steps

### CICSCMP

| Item | Value |
|---|---|
| EXEC | `samples/jcl/CICDBCMP.jcl:54` |
| Program |  |
| PROC | BLDCIDB2 |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) | Executes procedure BLDCIDB2 |

No DD statements.

## Scheduling and dependencies

Not referenced by the CA7 or Control-M exports or the shell scripts (see the gap report).

## JCL library, INCLUDE and SET

| Statement | Text | Line |
|---|---|---|
| JCLLIB | ORDER=&HLQ..PROC.UTIL | `samples/jcl/CICDBCMP.jcl:46` |
| SET | HLQ=AWS.M2.CARDDEMO | `samples/jcl/CICDBCMP.jcl:33` |
| SET | SSID=DAZ1 | `samples/jcl/CICDBCMP.jcl:34` |
| SET | MEMNAME=CICSDB2P | `samples/jcl/CICDBCMP.jcl:35` |
| SET | SRCLIB=&HLQ..CBL | `samples/jcl/CICDBCMP.jcl:36` |
| SET | COPYLIB=&HLQ..CPY | `samples/jcl/CICDBCMP.jcl:37` |
| SET | DCLLIB=&HLQ..DCL | `samples/jcl/CICDBCMP.jcl:38` |
| SET | LOADLIB=&HLQ..LOADLIB | `samples/jcl/CICDBCMP.jcl:39` |
| SET | DBRMLIB=&HLQ..DBRMLIB | `samples/jcl/CICDBCMP.jcl:40` |
| SET | SYSLBLK=3200 | `samples/jcl/CICDBCMP.jcl:41` |
| SET | PLAN=CARDDEMO | `samples/jcl/CICDBCMP.jcl:42` |

## Parameters

Symbols left as parameters (not resolved): `&HLQ`, `&MEMNAME`, `&PLAN`, `&SSID`, `&SYSUID`.

## Sources

- `samples/jcl/CICDBCMP.jcl`
- `docs/_work/structure/jcl/CICDBCMP.json`
- `docs/_work/jobs/CIDBCMP.json`

## Confidence

Steps, DDs, conditions and control-data summaries are Confirmed from the JCL. OPEN modes come from the program source. Comments are Unverified.
