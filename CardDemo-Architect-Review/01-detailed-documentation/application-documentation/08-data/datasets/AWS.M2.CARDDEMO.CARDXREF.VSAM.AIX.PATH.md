# Dataset AWS.M2.CARDDEMO.CARDXREF.VSAM.AIX.PATH

| Item | Value |
|---|---|
| DSN | AWS.M2.CARDDEMO.CARDXREF.VSAM.AIX.PATH |
| Organisation | vsam-path |
| Key offset |  |
| Key length |  |
| Defined by | app/jcl/XREFFILE.jcl:90 |
| Layout |  |
| Record |  |
| Record length |  |
| CICS FILE | CXACAIX (app/csd/CARDDEMO.CSD:63) |
| Catalog as of | 09/01/22 |
| Catalog rec total |  |

## Purpose

This name is recorded with store kind vsam-path.

## Access

| Program / job step | Access | Via | Evidence |
|---|---|---|---|
| INTCALC.STEP15 | R | jcl-dd | app/jcl/INTCALC.jcl:31 |

## Lifecycle

Accessors above are the JCL and CICS references recorded for this name. A shared record length was not used to invent extra links.

## Consistency

No length check was recorded.

## Sources

- `app/jcl/XREFFILE.jcl:90`
- `app/csd/CARDDEMO.CSD:63`
- `app/catlg/LISTCAT.txt:351`
- `docs/_work/datasets/AWS.M2.CARDDEMO.CARDXREF.VSAM.AIX.PATH.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
