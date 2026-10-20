# Integration interfaces

CICS XCTL and LINK edges are in the navigation flow, not in this list.

| Id | Type | Direction | Endpoint | Confidence | Evidence |
|---|---|---|---|---|---|
| IF-vsammq-001 | MQ | inbound | (MQTM-QNAME) | Confirmed | app/app-vsam-mq/cbl/COACCT01.cbl:191-198, app/app-vsam-mq/cbl/COACCT01.cbl:337-352, app/app-vsam-mq/cbl/CODATE01.cbl:140, app/app-vsam-mq/cbl/CODATE01.cbl:286-296, app/app-vsam-mq/csd/CRDDEMOM.csd:23, app/app-vsam-mq/csd/CRDDEMOM.csd:33 |
| IF-vsammq-002 | MQ | outbound | CARD.DEMO.REPLY.ACCT | Confirmed | app/app-vsam-mq/cbl/COACCT01.cbl:198, app/app-vsam-mq/cbl/COACCT01.cbl:261, app/app-vsam-mq/cbl/COACCT01.cbl:327, app/app-vsam-mq/cbl/COACCT01.cbl:366-372, app/app-vsam-mq/cbl/COACCT01.cbl:469-479 |
| IF-vsammq-003 | MQ | outbound | CARD.DEMO.REPLY.DATE | Confirmed | app/app-vsam-mq/cbl/CODATE01.cbl:147, app/app-vsam-mq/cbl/CODATE01.cbl:276, app/app-vsam-mq/cbl/CODATE01.cbl:379 |
| IF-vsammq-004 | MQ | outbound | CARD.DEMO.ERROR | Confirmed | app/app-vsam-mq/cbl/COACCT01.cbl:294, app/app-vsam-mq/cbl/COACCT01.cbl:512-516, app/app-vsam-mq/cbl/CODATE01.cbl:243, app/app-vsam-mq/cbl/CODATE01.cbl:416 |
| IF-auth-001 | MQ | bidirectional | request (MQTM-QNAME); reply (MQMD-REPLYTOQ) | Confirmed | app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:238, app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:354-374, app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:400-414, app/app-authorization-ims-db2-mq/csd/CRDDEMO2.csd:59-60 |
| IF-auth-002 | IMS-DLI | internal | PSB PSBPAUTB, DBD DBPAUTP0 | Confirmed | app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:75, app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:82, app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:80, app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:201-205, app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:355, app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:567, app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:25, app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL:27 |
| IF-auth-003 | IMS-DLI | internal | PAUDBUNL uses PSB PAUTBUNL. DBUNLDGS uses PSB DLIGSAMP. | Confirmed | app/app-authorization-ims-db2-mq/jcl/UNLDPADB.JCL:39, app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:213, app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:257, app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:27, app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:222, app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:302 |
| IF-trantype-001 | DB2 | internal | CARDDEMO.TRANSACTION_TYPE | Confirmed | app/app-transaction-type-db2/jcl/MNTTRDB2.jcl:30, app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1856, app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1557 |
| IF-trantype-002 | DB2 | inbound | CARDDEMO.TRANSACTION_TYPE_CATEGORY | Confirmed | app/app-transaction-type-db2/jcl/CREADB21.jcl:77-84, app/app-transaction-type-db2/ctl/DB2TEP41.ctl:16-17, app/app-transaction-type-db2/ctl/DB2LTCAT.ctl:15, app/app-transaction-type-db2/ddl/TRNTYCAT.ddl:1 |
| IF-auth-004 | DB2 | internal | CARDDEMO.AUTHFRDS | Confirmed | app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:68, app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:141, app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:222, app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:35 |
| IF-base-001 | TDQ | internal | JOBS | Confirmed | app/cbl/CORPT00C.cbl:517, app/csd/CARDDEMO.CSD:499 |
| IF-base-002 | INTRDR | internal | AWS.M2.CARDDEMO.JCL(INTRDRJ2) written to SYSOUT=(A,INTRDR) | Confirmed | app/jcl/INTRDRJ1.JCL:14-18 |
| IF-base-003 | FILE-TRANSFER | outbound | app/jcl/FTPJCL.JCL:33 | Confirmed | app/jcl/FTPJCL.JCL:22, app/jcl/FTPJCL.JCL:30, app/jcl/FTPJCL.JCL:33, app/jcl/FTPJCL.JCL:36, app/jcl/FTPJCL.JCL:40 |
| IF-build-001 | FILE-TRANSFER | outbound | jcl member named in each put | Confirmed | scripts/run_full_batch.sh:13, docs/_work/batch/schedule.json |

The FTP job SYSIN contains a user id and a password. Those values are not copied.

## Sources

- `docs/_work/integration/interfaces.json`
- `app/jcl/FTPJCL.JCL:33-40`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
