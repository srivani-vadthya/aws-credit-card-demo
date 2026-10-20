# Dataset AWS.M2.CARDDEMO.SYSTRAN

| Item | Value |
|---|---|
| DSN | AWS.M2.CARDDEMO.SYSTRAN |
| Organisation | gdg-base |
| Key offset |  |
| Key length |  |
| Defined by | app/jcl/DEFGDGB.jcl:48 |
| Layout |  |
| Record |  |
| Record length |  |
| CICS FILE |  |
| Catalog as of |  |
| Catalog rec total |  |

## Purpose

This name is recorded with store kind gdg-base.

## Access

| Program / job step | Access | Via | Evidence |
|---|---|---|---|
| COMBTRAN.STEP05R | R | jcl-dd | app/jcl/COMBTRAN.jcl:25 |
| INTCALC.STEP15 | C, D | jcl-dd | app/jcl/INTCALC.jcl:37 |

## Lifecycle

Accessors above are the JCL and CICS references recorded for this name. A shared record length was not used to invent extra links.

## Consistency

No length check was recorded.

## Sources

- `app/jcl/DEFGDGB.jcl:48`
- `docs/_work/datasets/AWS.M2.CARDDEMO.SYSTRAN.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
