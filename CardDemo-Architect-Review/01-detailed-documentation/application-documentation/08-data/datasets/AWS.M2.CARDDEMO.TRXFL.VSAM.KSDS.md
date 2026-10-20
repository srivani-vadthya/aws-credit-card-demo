# Dataset AWS.M2.CARDDEMO.TRXFL.VSAM.KSDS

| Item | Value |
|---|---|
| DSN | AWS.M2.CARDDEMO.TRXFL.VSAM.KSDS |
| Organisation | vsam-ksds |
| Key offset | 0 |
| Key length | 32 |
| Defined by | app/jcl/CREASTMT.JCL:29 |
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
| CREASTMT.STEP020 | R | jcl-dd | app/jcl/CREASTMT.JCL:59 |
| CREASTMT.STEP040 | R | jcl-dd | app/jcl/CREASTMT.JCL:83 |

## Lifecycle

Accessors above are the JCL and CICS references recorded for this name. A shared record length was not used to invent extra links.

## Consistency

| Length | Agrees | Source |
|---|---|---|
| 350 | False | app/jcl/CREASTMT.JCL:29 |

## Sources

- `app/jcl/CREASTMT.JCL:29`
- `docs/_work/datasets/AWS.M2.CARDDEMO.TRXFL.VSAM.KSDS.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
