# Dataset AWS.M2.CARDDEMO.TRANTYPE.VSAM.KSDS

| Item | Value |
|---|---|
| DSN | AWS.M2.CARDDEMO.TRANTYPE.VSAM.KSDS |
| Organisation | vsam-ksds |
| Key offset | 0 |
| Key length | 2 |
| Defined by | app/jcl/TRANTYPE.jcl:36 |
| Layout |  |
| Record |  |
| Record length |  |
| CICS FILE |  |
| Catalog as of | 09/01/22 |
| Catalog rec total | 7 |

## Purpose

This name is recorded with store kind vsam-ksds.

## Access

| Program / job step | Access | Via | Evidence |
|---|---|---|---|
| TRANREPT.STEP10R | R | jcl-dd | app/jcl/TRANREPT.jcl:69 |
| TRANTYPE.STEP15 | U | jcl-dd | app/jcl/TRANTYPE.jcl:58 |

## Lifecycle

Accessors above are the JCL and CICS references recorded for this name. A shared record length was not used to invent extra links.

## Consistency

| Length | Agrees | Source |
|---|---|---|
| 60 | False | app/jcl/TRANTYPE.jcl:36 |

## Sources

- `app/jcl/TRANTYPE.jcl:36`
- `app/catlg/LISTCAT.txt:3742`
- `docs/_work/datasets/AWS.M2.CARDDEMO.TRANTYPE.VSAM.KSDS.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
