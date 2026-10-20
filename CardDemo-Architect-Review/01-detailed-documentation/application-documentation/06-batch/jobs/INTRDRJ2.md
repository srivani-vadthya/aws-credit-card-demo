# Job INTRDRJ2

| Item | Value |
|---|---|
| Source | `app/jcl/INTRDRJ2.JCL` |
| Member | INTRDRJ2 |
| Job card | `app/jcl/INTRDRJ2.JCL:1-2` |
| CLASS / MSGCLASS | A / H |
| NOTIFY | &SYSUID |
| Job COND |  |
| Steps | 1 |
| Module | base |

## Purpose

Comment in the JCL (Unverified, `app/jcl/INTRDRJ2.JCL:4`): THIS JOB IS TO CREATE PHYSICAL VSAM FILE FOR IMS DEMODB    ****

## Step flow

```mermaid
flowchart TD
    S0["IDCAMS: IDCAMS"]
```

## Steps

### IDCAMS

| Item | Value |
|---|---|
| EXEC | `app/jcl/INTRDRJ2.JCL:7` |
| Program | IDCAMS |
| PROC |  |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) | IDCAMS REPRO copy |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| SYSPRINT | SYSOUT=* |  |  |  |  | `app/jcl/INTRDRJ2.JCL:8` |
| IN | AWS.M2.CARDEMO.FTP.TEST.BKUP | SHR |  |  |  | `app/jcl/INTRDRJ2.JCL:9` |
| OUT | AWS.M2.CARDEMO.FTP.TEST.BKUP.INTRDR | SHR |  |  |  | `app/jcl/INTRDRJ2.JCL:10` |
| SYSIN | * |  |  |  | in-stream lines 12-12; statements: REPRO | `app/jcl/INTRDRJ2.JCL:11` |

## Scheduling and dependencies

Not referenced by the CA7 or Control-M exports or the shell scripts (see the gap report).

## Parameters

Symbols left as parameters (not resolved): `&SYSUID`.

## Sources

- `app/jcl/INTRDRJ2.JCL`
- `docs/_work/structure/jcl/INTRDRJ2.json`
- `docs/_work/jobs/INTRDRJ2.json`

## Confidence

Steps, DDs, conditions and control-data summaries are Confirmed from the JCL. OPEN modes come from the program source. Comments are Unverified.
