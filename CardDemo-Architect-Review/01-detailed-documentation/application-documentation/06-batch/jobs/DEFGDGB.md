# Job DEFGDGB

| Item | Value |
|---|---|
| Source | `app/jcl/DEFGDGB.jcl` |
| Member | DEFGDGB |
| Job card | `app/jcl/DEFGDGB.jcl:1` |
| CLASS / MSGCLASS | A / 0 |
| NOTIFY | &SYSUID |
| Job COND |  |
| Steps | 1 |
| Module | base |

## Purpose

Comment in the JCL (Unverified, `app/jcl/DEFGDGB.jcl:19`): DEFINE GDG BASES NEEDED BY CARDDEMO PROJECT

## Step flow

```mermaid
flowchart TD
    S0["STEP05: IDCAMS"]
```

## Steps

### STEP05

| Item | Value |
|---|---|
| EXEC | `app/jcl/DEFGDGB.jcl:21` |
| Program | IDCAMS |
| PROC |  |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) | IDCAMS define GDG |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| SYSPRINT | SYSOUT=* |  |  |  |  | `app/jcl/DEFGDGB.jcl:22` |
| SYSIN | * |  |  |  | in-stream lines 24-59; statements: DEFINE; NAME(): AWS.M2.CARDDEMO.SYSTRAN AWS.M2.CARDDEMO.TCATBALF.BKUP AWS.M2.CARDDEMO.TRANREPT AWS.M2.CARDDEMO.TRANSACT.BKUP AWS.M2.CARDDEMO.TRANSACT.COMBINED AWS.M2.CARDDEMO.TRANSACT.DALY | `app/jcl/DEFGDGB.jcl:23` |

## Scheduling and dependencies

Not referenced by the CA7 or Control-M exports or the shell scripts (see the gap report).

## Parameters

Symbols left as parameters (not resolved): `&SYSUID`.

## Sources

- `app/jcl/DEFGDGB.jcl`
- `docs/_work/structure/jcl/DEFGDGB.json`
- `docs/_work/jobs/DEFGDGB.json`

## Confidence

Steps, DDs, conditions and control-data summaries are Confirmed from the JCL. OPEN modes come from the program source. Comments are Unverified.
