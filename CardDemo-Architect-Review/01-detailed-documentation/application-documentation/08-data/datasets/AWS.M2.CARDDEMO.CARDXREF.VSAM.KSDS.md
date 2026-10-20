# Dataset AWS.M2.CARDDEMO.CARDXREF.VSAM.KSDS

| Item | Value |
|---|---|
| DSN | AWS.M2.CARDDEMO.CARDXREF.VSAM.KSDS |
| Organisation | vsam-ksds |
| Key offset | 0 |
| Key length | 16 |
| Defined by | app/jcl/XREFFILE.jcl:39 |
| Layout |  |
| Record |  |
| Record length |  |
| CICS FILE | CCXREF (app/csd/CARDDEMO.CSD:37) |
| Catalog as of | 09/01/22 |
| Catalog rec total | 50 |

## Purpose

This name is recorded with store kind vsam-ksds.

## Access

| Program / job step | Access | Via | Evidence |
|---|---|---|---|
| CBEXPORT.STEP02 | R | jcl-dd | app/jcl/CBEXPORT.jcl:53 |
| CREASTMT.STEP040 | R | jcl-dd | app/jcl/CREASTMT.JCL:84 |
| INTCALC.STEP15 | R | jcl-dd | app/jcl/INTCALC.jcl:29 |
| POSTTRAN.STEP15 | R | jcl-dd | app/jcl/POSTTRAN.jcl:32 |
| READXREF.STEP05 | R | jcl-dd | app/jcl/READXREF.jcl:25 |
| TRANREPT.STEP10R | R | jcl-dd | app/jcl/TRANREPT.jcl:67 |
| XREFFILE.STEP15 | R | jcl-dd | app/jcl/XREFFILE.jcl:61 |

## Lifecycle

Accessors above are the JCL and CICS references recorded for this name. A shared record length was not used to invent extra links.

## Consistency

| Length | Agrees | Source |
|---|---|---|
| 50 | False | app/jcl/XREFFILE.jcl:39 |

## Sources

- `app/jcl/XREFFILE.jcl:39`
- `app/jcl/XREFFILE.jcl:72`
- `app/csd/CARDDEMO.CSD:37`
- `app/catlg/LISTCAT.txt:365`
- `docs/_work/datasets/AWS.M2.CARDDEMO.CARDXREF.VSAM.KSDS.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
