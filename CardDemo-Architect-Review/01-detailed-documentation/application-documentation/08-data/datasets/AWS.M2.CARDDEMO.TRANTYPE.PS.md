# Dataset AWS.M2.CARDDEMO.TRANTYPE.PS

| Item | Value |
|---|---|
| DSN | AWS.M2.CARDDEMO.TRANTYPE.PS |
| Organisation | sequential |
| Key offset |  |
| Key length |  |
| Defined by |  |
| Layout |  |
| Record |  |
| Record length |  |
| CICS FILE |  |
| Catalog as of | 09/01/22 |
| Catalog rec total |  |

## Purpose

This name is recorded with store kind sequential.

## Access

| Program / job step | Access | Via | Evidence |
|---|---|---|---|
| DEFGDGD.STEP20 | R | jcl-dd | app/jcl/DEFGDGD.jcl:39 |
| TRANTYPE.STEP15 | R | jcl-dd | app/jcl/TRANTYPE.jcl:56 |

## Lifecycle

Accessors above are the JCL and CICS references recorded for this name. A shared record length was not used to invent extra links.

## Consistency

No length check was recorded.

## Sources

- `app/catlg/LISTCAT.txt:3727`
- `docs/_work/datasets/AWS.M2.CARDDEMO.TRANTYPE.PS.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
