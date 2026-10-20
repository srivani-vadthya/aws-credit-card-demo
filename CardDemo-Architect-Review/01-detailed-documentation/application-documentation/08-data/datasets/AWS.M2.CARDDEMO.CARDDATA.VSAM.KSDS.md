# Dataset AWS.M2.CARDDEMO.CARDDATA.VSAM.KSDS

| Item | Value |
|---|---|
| DSN | AWS.M2.CARDDEMO.CARDDATA.VSAM.KSDS |
| Organisation | vsam-ksds |
| Key offset | 0 |
| Key length | 16 |
| Defined by | app/jcl/CARDFILE.jcl:50 |
| Layout | CVACT02Y |
| Record | CARD-RECORD |
| Record length | 150 |
| CICS FILE | CARDDAT (app/csd/CARDDEMO.CSD:25) |
| Catalog as of | 09/01/22 |
| Catalog rec total | 50 |

## Purpose

This name is recorded with store kind vsam-ksds.
 The length check names copybook CVACT02Y.

## Access

| Program / job step | Access | Via | Evidence |
|---|---|---|---|
| CARDFILE.STEP15 | R | jcl-dd | app/jcl/CARDFILE.jcl:72 |
| CBEXPORT.STEP02 | R | jcl-dd | app/jcl/CBEXPORT.jcl:57 |
| READCARD.STEP05 | R | jcl-dd | app/jcl/READCARD.jcl:25 |

## Lifecycle

Accessors above are the JCL and CICS references recorded for this name. A shared record length was not used to invent extra links.

## Consistency

| Length | Agrees | Source |
|---|---|---|
| 150 | True | app/jcl/CARDFILE.jcl:50 |

## Sources

- `app/jcl/CARDFILE.jcl:50`
- `app/jcl/CARDFILE.jcl:83`
- `app/csd/CARDDEMO.CSD:25`
- `app/catlg/LISTCAT.txt:164`
- `docs/_work/datasets/AWS.M2.CARDDEMO.CARDDATA.VSAM.KSDS.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
