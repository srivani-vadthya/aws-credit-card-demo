# Dataset AWS.M2.CARDDEMO.LOADLIB

| Item | Value |
|---|---|
| DSN | AWS.M2.CARDDEMO.LOADLIB |
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
| DBPAUTP0.UNLOAD | R | jcl-dd | app/app-authorization-ims-db2-mq/jcl/DBPAUTP0.jcl:19 |
| LOADPADB.STEP01 | R | jcl-dd | app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL:30 |
| UNLDGSAM.STEP01 | R | jcl-dd | app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:30 |
| UNLDPADB.STEP01 | R | jcl-dd | app/app-authorization-ims-db2-mq/jcl/UNLDPADB.JCL:42 |
| MNTTRDB2.STEP1 | R | jcl-dd | app/app-transaction-type-db2/jcl/MNTTRDB2.jcl:24 |
| CBEXPORT.STEP02 | R | jcl-dd | app/jcl/CBEXPORT.jcl:44 |
| CBIMPORT.STEP01 | R | jcl-dd | app/jcl/CBIMPORT.jcl:23 |
| CREASTMT.STEP040 | R | jcl-dd | app/jcl/CREASTMT.JCL:80 |
| INTCALC.STEP15 | R | jcl-dd | app/jcl/INTCALC.jcl:23 |
| POSTTRAN.STEP15 | R | jcl-dd | app/jcl/POSTTRAN.jcl:24 |
| READACCT.STEP05 | R | jcl-dd | app/jcl/READACCT.jcl:33 |
| READCARD.STEP05 | R | jcl-dd | app/jcl/READCARD.jcl:23 |
| READCUST.STEP05 | R | jcl-dd | app/jcl/READCUST.jcl:22 |
| READXREF.STEP05 | R | jcl-dd | app/jcl/READXREF.jcl:23 |
| TRANREPT.STEP10R | R | jcl-dd | app/jcl/TRANREPT.jcl:60 |
| WAITSTEP.WAIT | R | jcl-dd | app/jcl/WAITSTEP.jcl:23 |

## Lifecycle

Accessors above are the JCL and CICS references recorded for this name. A shared record length was not used to invent extra links.

## Consistency

No length check was recorded.

## Sources

- `app/catlg/LISTCAT.txt:1009`
- `docs/_work/datasets/AWS.M2.CARDDEMO.LOADLIB.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
