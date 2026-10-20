# Dataset AWS.M2.CARDDEMO.TCATBALF.VSAM.KSDS

| Item | Value |
|---|---|
| DSN | AWS.M2.CARDDEMO.TCATBALF.VSAM.KSDS |
| Organisation | vsam-ksds |
| Key offset | 0 |
| Key length | 17 |
| Defined by | app/jcl/TCATBALF.jcl:36 |
| Layout |  |
| Record |  |
| Record length |  |
| CICS FILE |  |
| Catalog as of | 09/01/22 |
| Catalog rec total | 100 |

## Purpose

This name is recorded with store kind vsam-ksds.

## Access

| Program / job step | Access | Via | Evidence |
|---|---|---|---|
| INTCALC.STEP15 | R | jcl-dd | app/jcl/INTCALC.jcl:27 |
| POSTTRAN.STEP15 | R | jcl-dd | app/jcl/POSTTRAN.jcl:41 |
| PRTCATBL.STEP05R | R | jcl-dd | app/jcl/PRTCATBL.jcl:32 |
| TCATBALF.STEP15 | U | jcl-dd | app/jcl/TCATBALF.jcl:58 |

## Lifecycle

Accessors above are the JCL and CICS references recorded for this name. A shared record length was not used to invent extra links.

## Consistency

| Length | Agrees | Source |
|---|---|---|
| 50 | False | app/jcl/TCATBALF.jcl:36 |

## Sources

- `app/jcl/TCATBALF.jcl:36`
- `app/catlg/LISTCAT.txt:1334`
- `docs/_work/datasets/AWS.M2.CARDDEMO.TCATBALF.VSAM.KSDS.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
