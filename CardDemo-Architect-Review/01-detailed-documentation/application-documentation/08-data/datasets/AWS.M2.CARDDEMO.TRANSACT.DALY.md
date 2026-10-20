# Dataset AWS.M2.CARDDEMO.TRANSACT.DALY

| Item | Value |
|---|---|
| DSN | AWS.M2.CARDDEMO.TRANSACT.DALY |
| Organisation | gdg-base |
| Key offset |  |
| Key length |  |
| Defined by | app/jcl/DEFGDGB.jcl:30 |
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
| TRANREPT.STEP05R | C, D | jcl-dd | app/jcl/TRANREPT.jcl:51 |
| TRANREPT.STEP10R | R | jcl-dd | app/jcl/TRANREPT.jcl:65 |
| SORTTEST.STEP05R | C, D | jcl-dd | samples/jcl/SORTTEST.jcl:31 |

## Lifecycle

Accessors above are the JCL and CICS references recorded for this name. A shared record length was not used to invent extra links.

## Consistency

No length check was recorded.

## Sources

- `app/jcl/DEFGDGB.jcl:30`
- `docs/_work/datasets/AWS.M2.CARDDEMO.TRANSACT.DALY.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
