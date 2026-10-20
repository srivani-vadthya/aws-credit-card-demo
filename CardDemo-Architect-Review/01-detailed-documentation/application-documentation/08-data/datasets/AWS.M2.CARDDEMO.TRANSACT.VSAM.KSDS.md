# Dataset AWS.M2.CARDDEMO.TRANSACT.VSAM.KSDS

| Item | Value |
|---|---|
| DSN | AWS.M2.CARDDEMO.TRANSACT.VSAM.KSDS |
| Organisation | vsam-ksds |
| Key offset | 0 |
| Key length | 16 |
| Defined by | app/jcl/TRANBKP.jcl:54, app/jcl/TRANFILE.jcl:49 |
| Layout |  |
| Record |  |
| Record length |  |
| CICS FILE | TRANSACT (app/csd/CARDDEMO.CSD:76) |
| Catalog as of | 09/01/22 |
| Catalog rec total | 311 |

## Purpose

This name is recorded with store kind vsam-ksds.

## Access

| Program / job step | Access | Via | Evidence |
|---|---|---|---|
| CBEXPORT.STEP02 | R | jcl-dd | app/jcl/CBEXPORT.jcl:55 |
| COMBTRAN.STEP10 | R | jcl-dd | app/jcl/COMBTRAN.jcl:45 |
| CREASTMT.STEP010 | R | jcl-dd | app/jcl/CREASTMT.JCL:45 |
| POSTTRAN.STEP15 | R | jcl-dd | app/jcl/POSTTRAN.jcl:28 |
| TRANBKP.STEP05R | R | jcl-dd | app/jcl/TRANBKP.jcl:26 |
| TRANFILE.STEP15 | R | jcl-dd | app/jcl/TRANFILE.jcl:71 |
| TRANREPT.STEP05R | R | jcl-dd | app/jcl/TRANREPT.jcl:26 |
| REPRTEST.STEP05 | R | jcl-dd | samples/jcl/REPRTEST.jcl:26 |

## Lifecycle

Accessors above are the JCL and CICS references recorded for this name. A shared record length was not used to invent extra links.

## Consistency

| Length | Agrees | Source |
|---|---|---|
| 350 | False | app/jcl/TRANBKP.jcl:54 |

## Sources

- `app/jcl/TRANBKP.jcl:54`
- `app/jcl/TRANFILE.jcl:49`
- `app/jcl/TRANFILE.jcl:82`
- `app/jcl/TRANIDX.jcl:25`
- `app/csd/CARDDEMO.CSD:76`
- `app/catlg/LISTCAT.txt:3555`
- `docs/_work/datasets/AWS.M2.CARDDEMO.TRANSACT.VSAM.KSDS.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
