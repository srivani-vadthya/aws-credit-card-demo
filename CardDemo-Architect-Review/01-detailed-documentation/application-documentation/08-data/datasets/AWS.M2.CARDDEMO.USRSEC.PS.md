# Dataset AWS.M2.CARDDEMO.USRSEC.PS

| Item | Value |
|---|---|
| DSN | AWS.M2.CARDDEMO.USRSEC.PS |
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
| DUSRSECJ.PREDEL | U, D | jcl-dd | app/jcl/DUSRSECJ.jcl:25 |
| DUSRSECJ.STEP01 | C, D | jcl-dd | app/jcl/DUSRSECJ.jcl:46 |
| DUSRSECJ.STEP03 | R | jcl-dd | app/jcl/DUSRSECJ.jcl:82 |

## Lifecycle

Accessors above are the JCL and CICS references recorded for this name. A shared record length was not used to invent extra links.

## Consistency

No length check was recorded.

## Sources

- `app/catlg/LISTCAT.txt:3831`
- `docs/_work/datasets/AWS.M2.CARDDEMO.USRSEC.PS.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
