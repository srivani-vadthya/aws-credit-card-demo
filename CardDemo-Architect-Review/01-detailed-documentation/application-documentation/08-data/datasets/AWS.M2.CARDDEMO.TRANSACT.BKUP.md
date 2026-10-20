# Dataset AWS.M2.CARDDEMO.TRANSACT.BKUP

| Item | Value |
|---|---|
| DSN | AWS.M2.CARDDEMO.TRANSACT.BKUP |
| Organisation | gdg-base |
| Key offset |  |
| Key length |  |
| Defined by | app/jcl/DEFGDGB.jcl:24 |
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
| COMBTRAN.STEP05R | R | jcl-dd | app/jcl/COMBTRAN.jcl:23 |
| TRANBKP.STEP05R | C, D | jcl-dd | app/jcl/TRANBKP.jcl:29 |
| TRANREPT.STEP05R | C, D | jcl-dd | app/jcl/TRANREPT.jcl:29 |
| TRANREPT.STEP05R | R | jcl-dd | app/jcl/TRANREPT.jcl:38 |
| REPRTEST.STEP05 | C, D | jcl-dd | samples/jcl/REPRTEST.jcl:29 |
| SORTTEST.STEP05R | R | jcl-dd | samples/jcl/SORTTEST.jcl:20 |

## Lifecycle

Accessors above are the JCL and CICS references recorded for this name. A shared record length was not used to invent extra links.

## Consistency

No length check was recorded.

## Sources

- `app/jcl/DEFGDGB.jcl:24`
- `docs/_work/datasets/AWS.M2.CARDDEMO.TRANSACT.BKUP.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
