# Dataset AWS.M2.CARDDEMO.EXPORT.DATA

| Item | Value |
|---|---|
| DSN | AWS.M2.CARDDEMO.EXPORT.DATA |
| Organisation | vsam-ksds |
| Key offset | 28 |
| Key length | 4 |
| Defined by | app/jcl/CBEXPORT.jcl:30 |
| Layout |  |
| Record |  |
| Record length |  |
| CICS FILE |  |
| Catalog as of |  |
| Catalog rec total |  |

## Purpose

This name is recorded with store kind vsam-ksds.

## Access

| Program / job step | Access | Via | Evidence |
|---|---|---|---|
| CBEXPORT.STEP02 | R | jcl-dd | app/jcl/CBEXPORT.jcl:62 |
| CBIMPORT.STEP01 | R | jcl-dd | app/jcl/CBIMPORT.jcl:28 |

## Lifecycle

Accessors above are the JCL and CICS references recorded for this name. A shared record length was not used to invent extra links.

## Consistency

| Length | Agrees | Source |
|---|---|---|
| 500 | False | app/jcl/CBEXPORT.jcl:30 |

## Sources

- `app/jcl/CBEXPORT.jcl:30`
- `docs/_work/datasets/AWS.M2.CARDDEMO.EXPORT.DATA.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
