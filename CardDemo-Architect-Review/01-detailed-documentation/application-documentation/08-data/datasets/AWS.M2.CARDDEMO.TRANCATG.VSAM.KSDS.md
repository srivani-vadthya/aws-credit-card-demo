# Dataset AWS.M2.CARDDEMO.TRANCATG.VSAM.KSDS

| Item | Value |
|---|---|
| DSN | AWS.M2.CARDDEMO.TRANCATG.VSAM.KSDS |
| Organisation | vsam-ksds |
| Key offset | 0 |
| Key length | 6 |
| Defined by | app/jcl/TRANCATG.jcl:36 |
| Layout |  |
| Record |  |
| Record length |  |
| CICS FILE |  |
| Catalog as of | 09/01/22 |
| Catalog rec total | 18 |

## Purpose

This name is recorded with store kind vsam-ksds.

## Access

| Program / job step | Access | Via | Evidence |
|---|---|---|---|
| TRANCATG.STEP15 | U | jcl-dd | app/jcl/TRANCATG.jcl:58 |
| TRANREPT.STEP10R | R | jcl-dd | app/jcl/TRANREPT.jcl:71 |

## Lifecycle

Accessors above are the JCL and CICS references recorded for this name. A shared record length was not used to invent extra links.

## Consistency

| Length | Agrees | Source |
|---|---|---|
| 60 | False | app/jcl/TRANCATG.jcl:36 |

## Sources

- `app/jcl/TRANCATG.jcl:36`
- `app/catlg/LISTCAT.txt:1440`
- `docs/_work/datasets/AWS.M2.CARDDEMO.TRANCATG.VSAM.KSDS.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
