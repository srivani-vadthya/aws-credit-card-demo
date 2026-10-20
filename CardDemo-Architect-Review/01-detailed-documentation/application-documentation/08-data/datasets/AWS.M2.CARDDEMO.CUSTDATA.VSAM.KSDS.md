# Dataset AWS.M2.CARDDEMO.CUSTDATA.VSAM.KSDS

| Item | Value |
|---|---|
| DSN | AWS.M2.CARDDEMO.CUSTDATA.VSAM.KSDS |
| Organisation | vsam-ksds |
| Key offset | 0 |
| Key length | 9 |
| Defined by | app/jcl/CUSTFILE.jcl:46 |
| Layout |  |
| Record |  |
| Record length |  |
| CICS FILE | CUSTDAT (app/csd/CARDDEMO.CSD:50) |
| Catalog as of | 09/01/22 |
| Catalog rec total | 50 |

## Purpose

This name is recorded with store kind vsam-ksds.

## Access

| Program / job step | Access | Via | Evidence |
|---|---|---|---|
| CBEXPORT.STEP02 | R | jcl-dd | app/jcl/CBEXPORT.jcl:49 |
| CREASTMT.STEP040 | R | jcl-dd | app/jcl/CREASTMT.JCL:86 |
| CUSTFILE.STEP15 | R | jcl-dd | app/jcl/CUSTFILE.jcl:68 |
| READCUST.STEP05 | R | jcl-dd | app/jcl/READCUST.jcl:24 |

## Lifecycle

Accessors above are the JCL and CICS references recorded for this name. A shared record length was not used to invent extra links.

## Consistency

| Length | Agrees | Source |
|---|---|---|
| 500 | False | app/jcl/CUSTFILE.jcl:46 |

## Sources

- `app/jcl/CUSTFILE.jcl:46`
- `app/csd/CARDDEMO.CSD:50`
- `app/catlg/LISTCAT.txt:595`
- `docs/_work/datasets/AWS.M2.CARDDEMO.CUSTDATA.VSAM.KSDS.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
