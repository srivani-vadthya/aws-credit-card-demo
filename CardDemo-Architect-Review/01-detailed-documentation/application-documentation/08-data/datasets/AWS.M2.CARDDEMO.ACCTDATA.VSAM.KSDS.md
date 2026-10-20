# Dataset AWS.M2.CARDDEMO.ACCTDATA.VSAM.KSDS

| Item | Value |
|---|---|
| DSN | AWS.M2.CARDDEMO.ACCTDATA.VSAM.KSDS |
| Organisation | vsam-ksds |
| Key offset | 0 |
| Key length | 11 |
| Defined by | app/jcl/ACCTFILE.jcl:36 |
| Layout | CVACT01Y |
| Record | ACCOUNT-RECORD |
| Record length | 300 |
| CICS FILE | ACCTDAT (app/csd/CARDDEMO.CSD:1) |
| Catalog as of | 09/01/22 |
| Catalog rec total | 50 |

## Purpose

This name is recorded with store kind vsam-ksds.
 The length check names copybook CVACT01Y.

## Access

| Program / job step | Access | Via | Evidence |
|---|---|---|---|
| ACCTFILE.STEP15 | R | jcl-dd | app/jcl/ACCTFILE.jcl:58 |
| CBEXPORT.STEP02 | R | jcl-dd | app/jcl/CBEXPORT.jcl:51 |
| CREASTMT.STEP040 | R | jcl-dd | app/jcl/CREASTMT.JCL:85 |
| INTCALC.STEP15 | R | jcl-dd | app/jcl/INTCALC.jcl:33 |
| POSTTRAN.STEP15 | R | jcl-dd | app/jcl/POSTTRAN.jcl:39 |
| READACCT.STEP05 | R | jcl-dd | app/jcl/READACCT.jcl:35 |

## Lifecycle

Accessors above are the JCL and CICS references recorded for this name. A shared record length was not used to invent extra links.

## Consistency

| Length | Agrees | Source |
|---|---|---|
| 300 | True | app/jcl/ACCTFILE.jcl:36 |

## Sources

- `app/jcl/ACCTFILE.jcl:36`
- `app/csd/CARDDEMO.CSD:1`
- `app/catlg/LISTCAT.txt:22`
- `docs/_work/datasets/AWS.M2.CARDDEMO.ACCTDATA.VSAM.KSDS.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
