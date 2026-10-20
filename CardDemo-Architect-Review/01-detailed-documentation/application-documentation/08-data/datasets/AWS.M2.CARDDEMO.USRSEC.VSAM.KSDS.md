# Dataset AWS.M2.CARDDEMO.USRSEC.VSAM.KSDS

| Item | Value |
|---|---|
| DSN | AWS.M2.CARDDEMO.USRSEC.VSAM.KSDS |
| Organisation | vsam-ksds |
| Key offset | 0 |
| Key length | 8 |
| Defined by | app/jcl/DUSRSECJ.jcl:64 |
| Layout |  |
| Record |  |
| Record length |  |
| CICS FILE | USRSEC (app/csd/CARDDEMO.CSD:88) |
| Catalog as of | 09/01/22 |
| Catalog rec total | 10 |

## Purpose

This name is recorded with store kind vsam-ksds.

## Access

| Program / job step | Access | Via | Evidence |
|---|---|---|---|
| DUSRSECJ.STEP03 | R | jcl-dd | app/jcl/DUSRSECJ.jcl:83 |

## Lifecycle

Accessors above are the JCL and CICS references recorded for this name. A shared record length was not used to invent extra links.

## Consistency

| Length | Agrees | Source |
|---|---|---|
| 80 | False | app/jcl/DUSRSECJ.jcl:64 |

## Sources

- `app/jcl/DUSRSECJ.jcl:64`
- `app/csd/CARDDEMO.CSD:88`
- `app/catlg/LISTCAT.txt:3846`
- `docs/_work/datasets/AWS.M2.CARDDEMO.USRSEC.VSAM.KSDS.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
