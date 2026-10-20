# Job dependencies

Programs, PROCs, datasets and scheduler links for every JCL job.

## ACCTFILE

Page: [ACCTFILE](../../01-detailed-documentation/application-documentation/06-batch/jobs/ACCTFILE.md). Source `app/jcl/ACCTFILE.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP05 | IDCAMS | `app/jcl/ACCTFILE.jcl:22` |
| STEP10 | IDCAMS | `app/jcl/ACCTFILE.jcl:33` |
| STEP15 | IDCAMS | `app/jcl/ACCTFILE.jcl:54` |
| STEP15.ACCTDATA | AWS.M2.CARDDEMO.ACCTDATA.PS DISP=SHR | `app/jcl/ACCTFILE.jcl:56-57` |
| STEP15.ACCTVSAM | AWS.M2.CARDDEMO.ACCTDATA.VSAM.KSDS DISP=SHR | `app/jcl/ACCTFILE.jcl:58-59` |

## CARDFILE

Page: [CARDFILE](../../01-detailed-documentation/application-documentation/06-batch/jobs/CARDFILE.md). Source `app/jcl/CARDFILE.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| CLCIFIL | SDSF | `app/jcl/CARDFILE.jcl:22` |
| STEP05 | IDCAMS | `app/jcl/CARDFILE.jcl:33` |
| STEP10 | IDCAMS | `app/jcl/CARDFILE.jcl:47` |
| STEP15 | IDCAMS | `app/jcl/CARDFILE.jcl:68` |
| STEP15.CARDDATA | AWS.M2.CARDDEMO.CARDDATA.PS DISP=SHR | `app/jcl/CARDFILE.jcl:70-71` |
| STEP15.CARDVSAM | AWS.M2.CARDDEMO.CARDDATA.VSAM.KSDS DISP=SHR | `app/jcl/CARDFILE.jcl:72-73` |
| STEP40 | IDCAMS | `app/jcl/CARDFILE.jcl:80` |
| STEP50 | IDCAMS | `app/jcl/CARDFILE.jcl:97` |
| STEP60 | IDCAMS | `app/jcl/CARDFILE.jcl:107` |
| OPCIFIL | SDSF | `app/jcl/CARDFILE.jcl:118` |

## CBADMCDJ

Page: [CBADMCDJ](../../01-detailed-documentation/application-documentation/06-batch/jobs/CBADMCDJ.md). Source `app/jcl/CBADMCDJ.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP1 | DFHCSDUP | `app/jcl/CBADMCDJ.jcl:27-28` |
| STEP1.DFHCSD | OEM.CICSTS.DFHCSD DISP=SHR | `app/jcl/CBADMCDJ.jcl:30` |

## CBEXPORT

Page: [CBEXPORT](../../01-detailed-documentation/application-documentation/06-batch/jobs/CBEXPORT.md). Source `app/jcl/CBEXPORT.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP01 | IDCAMS | `app/jcl/CBEXPORT.jcl:24` |
| STEP02 | CBEXPORT | `app/jcl/CBEXPORT.jcl:43` |
| STEP02.CUSTFILE | AWS.M2.CARDDEMO.CUSTDATA.VSAM.KSDS DISP=SHR | `app/jcl/CBEXPORT.jcl:49-50` |
| STEP02.ACCTFILE | AWS.M2.CARDDEMO.ACCTDATA.VSAM.KSDS DISP=SHR | `app/jcl/CBEXPORT.jcl:51-52` |
| STEP02.XREFFILE | AWS.M2.CARDDEMO.CARDXREF.VSAM.KSDS DISP=SHR | `app/jcl/CBEXPORT.jcl:53-54` |
| STEP02.TRANSACT | AWS.M2.CARDDEMO.TRANSACT.VSAM.KSDS DISP=SHR | `app/jcl/CBEXPORT.jcl:55-56` |
| STEP02.CARDFILE | AWS.M2.CARDDEMO.CARDDATA.VSAM.KSDS DISP=SHR | `app/jcl/CBEXPORT.jcl:57-58` |
| STEP02.EXPFILE | AWS.M2.CARDDEMO.EXPORT.DATA DISP=SHR | `app/jcl/CBEXPORT.jcl:62-63` |

## CBIMPORT

Page: [CBIMPORT](../../01-detailed-documentation/application-documentation/06-batch/jobs/CBIMPORT.md). Source `app/jcl/CBIMPORT.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP01 | CBIMPORT | `app/jcl/CBIMPORT.jcl:22` |
| STEP01.EXPFILE | AWS.M2.CARDDEMO.EXPORT.DATA DISP=SHR | `app/jcl/CBIMPORT.jcl:28-29` |
| STEP01.CUSTOUT | AWS.M2.CARDDEMO.CUSTDATA.IMPORT DISP=(NEW,CATLG,DELETE) | `app/jcl/CBIMPORT.jcl:33-37` |
| STEP01.ACCTOUT | AWS.M2.CARDDEMO.ACCTDATA.IMPORT DISP=(NEW,CATLG,DELETE) | `app/jcl/CBIMPORT.jcl:38-42` |
| STEP01.XREFOUT | AWS.M2.CARDDEMO.CARDXREF.IMPORT DISP=(NEW,CATLG,DELETE) | `app/jcl/CBIMPORT.jcl:43-47` |
| STEP01.TRNXOUT | AWS.M2.CARDDEMO.TRANSACT.IMPORT DISP=(NEW,CATLG,DELETE) | `app/jcl/CBIMPORT.jcl:48-52` |
| STEP01.ERROUT | AWS.M2.CARDDEMO.IMPORT.ERRORS DISP=(NEW,CATLG,DELETE) | `app/jcl/CBIMPORT.jcl:56-60` |

## CBLDBMS

Page: [CBLDBMS](../../01-detailed-documentation/application-documentation/06-batch/jobs/CBLDBMS.md). Source `samples/jcl/BMSCMP.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP1 | PROC BUILDBMS | `samples/jcl/BMSCMP.jcl:38` |
| SDSF1 | SDSF | `samples/jcl/BMSCMP.jcl:42` |

## CBPAUP0J

Page: [CBPAUP0J](../../01-detailed-documentation/application-documentation/06-batch/jobs/CBPAUP0J.md). Source `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP01 | DFSRRC00 -> CBPAUP0C | `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:24-25` |
| STEP01.DFSRESLB | IMS.SDFSRESL DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:28` |
| STEP01.PROCLIB | IMS.PROCLIB DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:29` |
| STEP01.DFSSEL | IMS.SDFSRESL DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:31` |
| STEP01.IMS | IMS.PSBLIB DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:33` |
| STEP01.IMS | IMS.DBDLIB DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:34` |
| predecessor | CLOSEFIL | `app/scheduler/CardDemo.ca7:43` |
| successor | POSTTRAN | `app/scheduler/CardDemo.ca7:70` |

## CICCMP

Page: [CICCMP](../../01-detailed-documentation/application-documentation/06-batch/jobs/CICCMP.md). Source `samples/jcl/CICCMP.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| CICSCMP | PROC BUILDONL | `samples/jcl/CICCMP.jcl:41` |
| NEWCOPY | SDSF | `samples/jcl/CICCMP.jcl:45` |

## CIDBCMP

Page: [CIDBCMP](../../01-detailed-documentation/application-documentation/06-batch/jobs/CIDBCMP.md). Source `samples/jcl/CICDBCMP.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| CICSCMP | PROC BLDCIDB2 | `samples/jcl/CICDBCMP.jcl:54` |

## CLOSEFIL

Page: [CLOSEFIL](../../01-detailed-documentation/application-documentation/06-batch/jobs/CLOSEFIL.md). Source `app/jcl/CLOSEFIL.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| CLCIFIL | SDSF | `app/jcl/CLOSEFIL.jcl:22` |
| successor | CBPAUP0J | `app/scheduler/CardDemo.ca7:43` |
| successor | TRANTYPE | `app/scheduler/CardDemo.ca7:162` |
| predecessor | WAITSTEP | `app/scheduler/CardDemo.ca7:303` |
| predecessor | WAITSTEP | `app/scheduler/CardDemo.ca7:335` |
| successor | READACCT | `app/scheduler/CardDemo.ca7:340` |
| successor | CREASTMT | `app/scheduler/CardDemo.ca7:468` |
| predecessor | OPENFIL | `app/scheduler/CardDemo.ca7:532` |
| successor | PRTCATBL | `app/scheduler/CardDemo.ca7:537` |
| successor | TRANBKP | `app/scheduler/CardDemo.controlm:5`, `app/scheduler/CardDemo.controlm:9` |
| successor | INTCALC | `app/scheduler/CardDemo.controlm:66`, `app/scheduler/CardDemo.controlm:70` |
| predecessor | MNTTRDB2 | `app/scheduler/CardDemo.controlm:28`, `app/scheduler/CardDemo.controlm:34` |
| successor | DISCGRP | `app/scheduler/CardDemo.controlm:35`, `app/scheduler/CardDemo.controlm:39` |

## CNJBATMP

Page: [CNJBATMP](../../01-detailed-documentation/application-documentation/06-batch/jobs/CNJBATMP.md). Source `samples/jcl/BATCMP.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| BATCMP | PROC BUILDBAT | `samples/jcl/BATCMP.jcl:42` |

## COMBTRAN

Page: [COMBTRAN](../../01-detailed-documentation/application-documentation/06-batch/jobs/COMBTRAN.md). Source `app/jcl/COMBTRAN.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP05R | SORT | `app/jcl/COMBTRAN.jcl:22` |
| STEP05R.SORTIN | AWS.M2.CARDDEMO.TRANSACT.BKUP(0) DISP=SHR | `app/jcl/COMBTRAN.jcl:23-24` |
| STEP05R.SORTIN | AWS.M2.CARDDEMO.SYSTRAN(0) DISP=SHR | `app/jcl/COMBTRAN.jcl:25-26` |
| STEP05R.SORTOUT | AWS.M2.CARDDEMO.TRANSACT.COMBINED(+1) DISP=(NEW,CATLG,DELETE) | `app/jcl/COMBTRAN.jcl:33-37` |
| STEP10 | IDCAMS | `app/jcl/COMBTRAN.jcl:41` |
| STEP10.TRANSACT | AWS.M2.CARDDEMO.TRANSACT.COMBINED(+1) DISP=SHR | `app/jcl/COMBTRAN.jcl:43-44` |
| STEP10.TRANVSAM | AWS.M2.CARDDEMO.TRANSACT.VSAM.KSDS DISP=SHR | `app/jcl/COMBTRAN.jcl:45-46` |
| predecessor | INTCALC | `app/scheduler/CardDemo.controlm:72`, `app/scheduler/CardDemo.controlm:76` |
| successor | WAITSTEP | `app/scheduler/CardDemo.controlm:78`, `app/scheduler/CardDemo.controlm:82` |

## CREADB2

Page: [CREADB2](../../01-detailed-documentation/application-documentation/06-batch/jobs/CREADB2.md). Source `app/app-transaction-type-db2/jcl/CREADB21.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| FREEPLN | IKJEFT01 | `app/app-transaction-type-db2/jcl/CREADB21.jcl:40` |
| FREEPLN.SYSTSIN | &LBNM..CNTL(DB2FREE) DISP=SHR | `app/app-transaction-type-db2/jcl/CREADB21.jcl:46` |
| CRCRDDB | IKJEFT01 | `app/app-transaction-type-db2/jcl/CREADB21.jcl:52` |
| CRCRDDB.SYSTSIN | &LBNM..CNTL(DB2TIAD1) DISP=SHR | `app/app-transaction-type-db2/jcl/CREADB21.jcl:58` |
| CRCRDDB.SYSIN | &LBNM..CNTL(DB2CREAT) DISP=SHR | `app/app-transaction-type-db2/jcl/CREADB21.jcl:59` |
| LDTTYPE | IEFBR14 | `app/app-transaction-type-db2/jcl/CREADB21.jcl:64` |
| RUNTEP2 | IKJEFT01 | `app/app-transaction-type-db2/jcl/CREADB21.jcl:65` |
| RUNTEP2.SYSTSIN | &LBNM..CNTL(DB2TEP41) DISP=SHR | `app/app-transaction-type-db2/jcl/CREADB21.jcl:71` |
| RUNTEP2.SYSIN | &LBNM..CNTL(DB2LTTYP) DISP=SHR | `app/app-transaction-type-db2/jcl/CREADB21.jcl:72` |
| LDTCCAT | IKJEFT01 | `app/app-transaction-type-db2/jcl/CREADB21.jcl:77` |
| LDTCCAT.SYSTSIN | &LBNM..CNTL(DB2TEP41) DISP=SHR | `app/app-transaction-type-db2/jcl/CREADB21.jcl:83` |
| LDTCCAT.SYSIN | &LBNM..CNTL(DB2LTCAT) DISP=SHR | `app/app-transaction-type-db2/jcl/CREADB21.jcl:84` |

## CREASTMT

Page: [CREASTMT](../../01-detailed-documentation/application-documentation/06-batch/jobs/CREASTMT.md). Source `app/jcl/CREASTMT.JCL`.

| Step / relation | Target | Evidence |
|---|---|---|
| DELDEF01 | IDCAMS | `app/jcl/CREASTMT.JCL:22` |
| STEP010 | SORT | `app/jcl/CREASTMT.JCL:44` |
| STEP010.SORTIN | AWS.M2.CARDDEMO.TRANSACT.VSAM.KSDS DISP=SHR | `app/jcl/CREASTMT.JCL:45` |
| STEP010.SORTOUT | AWS.M2.CARDDEMO.TRXFL.SEQ DISP=(NEW,CATLG,DELETE) | `app/jcl/CREASTMT.JCL:48-51` |
| STEP020 | IDCAMS | `app/jcl/CREASTMT.JCL:56` |
| STEP020.INFILE | AWS.M2.CARDDEMO.TRXFL.SEQ DISP=SHR | `app/jcl/CREASTMT.JCL:58` |
| STEP020.OUTFILE | AWS.M2.CARDDEMO.TRXFL.VSAM.KSDS DISP=SHR | `app/jcl/CREASTMT.JCL:59` |
| STEP030 | IEFBR14 | `app/jcl/CREASTMT.JCL:66` |
| STEP030.HTMLFILE | AWS.M2.CARDDEMO.STATEMNT.HTML DISP=(MOD,DELETE,DELETE) | `app/jcl/CREASTMT.JCL:67-71` |
| STEP030.STMTFILE | AWS.M2.CARDDEMO.STATEMNT.PS DISP=(MOD,DELETE,DELETE) | `app/jcl/CREASTMT.JCL:72-75` |
| STEP040 | CBSTM03A | `app/jcl/CREASTMT.JCL:79` |
| STEP040.TRNXFILE | AWS.M2.CARDDEMO.TRXFL.VSAM.KSDS DISP=SHR | `app/jcl/CREASTMT.JCL:83` |
| STEP040.XREFFILE | AWS.M2.CARDDEMO.CARDXREF.VSAM.KSDS DISP=SHR | `app/jcl/CREASTMT.JCL:84` |
| STEP040.ACCTFILE | AWS.M2.CARDDEMO.ACCTDATA.VSAM.KSDS DISP=SHR | `app/jcl/CREASTMT.JCL:85` |
| STEP040.CUSTFILE | AWS.M2.CARDDEMO.CUSTDATA.VSAM.KSDS DISP=SHR | `app/jcl/CREASTMT.JCL:86` |
| STEP040.STMTFILE | AWS.M2.CARDDEMO.STATEMNT.PS DISP=(NEW,CATLG,DELETE) | `app/jcl/CREASTMT.JCL:87-91` |
| STEP040.HTMLFILE | AWS.M2.CARDDEMO.STATEMNT.HTML DISP=(NEW,CATLG,DELETE) | `app/jcl/CREASTMT.JCL:92-96` |
| predecessor | CLOSEFIL | `app/scheduler/CardDemo.ca7:468` |
| successor | TXT2PDF1 | `app/scheduler/CardDemo.ca7:495` |

## CUSTFILE

Page: [CUSTFILE](../../01-detailed-documentation/application-documentation/06-batch/jobs/CUSTFILE.md). Source `app/jcl/CUSTFILE.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| CLCIFIL | SDSF | `app/jcl/CUSTFILE.jcl:22` |
| STEP05 | IDCAMS | `app/jcl/CUSTFILE.jcl:32` |
| STEP10 | IDCAMS | `app/jcl/CUSTFILE.jcl:43` |
| STEP15 | IDCAMS | `app/jcl/CUSTFILE.jcl:64` |
| STEP15.CUSTDATA | AWS.M2.CARDDEMO.CUSTDATA.PS DISP=SHR | `app/jcl/CUSTFILE.jcl:66-67` |
| STEP15.CUSTVSAM | AWS.M2.CARDDEMO.CUSTDATA.VSAM.KSDS DISP=SHR | `app/jcl/CUSTFILE.jcl:68-69` |
| OPCIFIL | SDSF | `app/jcl/CUSTFILE.jcl:76` |

## DALYREJS

Page: [DALYREJS](../../01-detailed-documentation/application-documentation/06-batch/jobs/DALYREJS.md). Source `app/jcl/DALYREJS.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP05 | IDCAMS | `app/jcl/DALYREJS.jcl:21` |

## DBPAUTP0

Page: [DBPAUTP0](../../01-detailed-documentation/application-documentation/06-batch/jobs/DBPAUTP0.md). Source `app/app-authorization-ims-db2-mq/jcl/DBPAUTP0.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEPDEL | IEFBR14 | `app/app-authorization-ims-db2-mq/jcl/DBPAUTP0.jcl:7` |
| STEPDEL.SYSUT1 | AWS.M2.CARDDEMO.IMSDATA.DBPAUTP0 DISP=(MOD,DELETE) | `app/app-authorization-ims-db2-mq/jcl/DBPAUTP0.jcl:9-10` |
| UNLOAD | DFSRRC00 -> DFSURGU0 | `app/app-authorization-ims-db2-mq/jcl/DBPAUTP0.jcl:15-16` |
| UNLOAD.DFSRESLB | OEMA.IMS.IMSP.SDFSRESL DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/DBPAUTP0.jcl:20` |
| UNLOAD.IMS | OEM.IMS.IMSP.PSBLIB DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/DBPAUTP0.jcl:21` |
| UNLOAD.IMS | OEM.IMS.IMSP.DBDLIB DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/DBPAUTP0.jcl:22` |
| UNLOAD.DFSURGU1 | AWS.M2.CARDDEMO.IMSDATA.DBPAUTP0 DISP=(,CATLG,DELETE) | `app/app-authorization-ims-db2-mq/jcl/DBPAUTP0.jcl:25-29` |
| UNLOAD.DDPAUTP0 | OEM.IMS.IMSP.PAUTHDB DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/DBPAUTP0.jcl:31` |
| UNLOAD.DDPAUTX0 | OEM.IMS.IMSP.PAUTHDBX DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/DBPAUTP0.jcl:32` |
| UNLOAD.DFSVSAMP | OEMPP.IMS.V15R01MB.PROCLIB(DFSVSMDB) DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/DBPAUTP0.jcl:33` |
| UNLOAD.RECON1 | OEM.IMS.IMSP.RECON1 DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/DBPAUTP0.jcl:40` |
| UNLOAD.RECON2 | OEM.IMS.IMSP.RECON2 DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/DBPAUTP0.jcl:41` |
| UNLOAD.RECON3 | OEM.IMS.IMSP.RECON3 DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/DBPAUTP0.jcl:42` |

## DEFCUST

Page: [DEFCUST](../../01-detailed-documentation/application-documentation/06-batch/jobs/DEFCUST.md). Source `app/jcl/DEFCUST.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP05 | IDCAMS | `app/jcl/DEFCUST.jcl:22` |
| STEP05 | IDCAMS | `app/jcl/DEFCUST.jcl:32` |

## DEFGDGB

Page: [DEFGDGB](../../01-detailed-documentation/application-documentation/06-batch/jobs/DEFGDGB.md). Source `app/jcl/DEFGDGB.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP05 | IDCAMS | `app/jcl/DEFGDGB.jcl:21` |

## DEFGDGD

Page: [DEFGDGD](../../01-detailed-documentation/application-documentation/06-batch/jobs/DEFGDGD.md). Source `app/jcl/DEFGDGD.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP10 | IDCAMS | `app/jcl/DEFGDGD.jcl:24` |
| STEP20 | IEBGENER | `app/jcl/DEFGDGD.jcl:36` |
| STEP20.SYSUT1 | AWS.M2.CARDDEMO.TRANTYPE.PS DISP=SHR | `app/jcl/DEFGDGD.jcl:39` |
| STEP20.SYSUT2 | AWS.M2.CARDDEMO.TRANTYPE.BKUP(+1) DISP=(NEW,CATLG) | `app/jcl/DEFGDGD.jcl:40-43` |
| STEP30 | IDCAMS | `app/jcl/DEFGDGD.jcl:47` |
| STEP40 | IEBGENER | `app/jcl/DEFGDGD.jcl:59` |
| STEP40.SYSUT1 | AWS.M2.CARDDEMO.TRANCATG.PS DISP=SHR | `app/jcl/DEFGDGD.jcl:62` |
| STEP40.SYSUT2 | AWS.M2.CARDDEMO.TRANCATG.PS.BKUP(+1) DISP=(NEW,CATLG) | `app/jcl/DEFGDGD.jcl:63-66` |
| STEP50 | IDCAMS | `app/jcl/DEFGDGD.jcl:70` |
| STEP60 | IEBGENER | `app/jcl/DEFGDGD.jcl:82` |
| STEP60.SYSUT1 | AWS.M2.CARDDEMO.DISCGRP.PS DISP=SHR | `app/jcl/DEFGDGD.jcl:85` |
| STEP60.SYSUT2 | AWS.M2.CARDDEMO.DISCGRP.BKUP(+1) DISP=(NEW,CATLG) | `app/jcl/DEFGDGD.jcl:86-89` |

## DISCGRP

Page: [DISCGRP](../../01-detailed-documentation/application-documentation/06-batch/jobs/DISCGRP.md). Source `app/jcl/DISCGRP.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP05 | IDCAMS | `app/jcl/DISCGRP.jcl:22` |
| STEP10 | IDCAMS | `app/jcl/DISCGRP.jcl:33` |
| STEP15 | IDCAMS | `app/jcl/DISCGRP.jcl:54` |
| STEP15.DISCGRP | AWS.M2.CARDDEMO.DISCGRP.PS DISP=SHR | `app/jcl/DISCGRP.jcl:56-57` |
| STEP15.DISCVSAM | AWS.M2.CARDDEMO.DISCGRP.VSAM.KSDS DISP=OLD | `app/jcl/DISCGRP.jcl:58-59` |
| predecessor | CLOSEFIL | `app/scheduler/CardDemo.controlm:35`, `app/scheduler/CardDemo.controlm:39` |
| successor | WAITSTEP | `app/scheduler/CardDemo.controlm:41`, `app/scheduler/CardDemo.controlm:45` |

## DUSRSECJ

Page: [DUSRSECJ](../../01-detailed-documentation/application-documentation/06-batch/jobs/DUSRSECJ.md). Source `app/jcl/DUSRSECJ.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| PREDEL | IEFBR14 | `app/jcl/DUSRSECJ.jcl:23` |
| PREDEL.DD01 | AWS.M2.CARDDEMO.USRSEC.PS DISP=(MOD,DELETE,DELETE) | `app/jcl/DUSRSECJ.jcl:25-26` |
| STEP01 | IEBGENER | `app/jcl/DUSRSECJ.jcl:32` |
| STEP01.SYSUT2 | AWS.M2.CARDDEMO.USRSEC.PS DISP=(NEW,CATLG,DELETE) | `app/jcl/DUSRSECJ.jcl:46-49` |
| STEP02 | IDCAMS | `app/jcl/DUSRSECJ.jcl:58` |
| STEP03 | IDCAMS | `app/jcl/DUSRSECJ.jcl:80` |
| STEP03.IN | AWS.M2.CARDDEMO.USRSEC.PS DISP=SHR | `app/jcl/DUSRSECJ.jcl:82` |
| STEP03.OUT | AWS.M2.CARDDEMO.USRSEC.VSAM.KSDS DISP=SHR | `app/jcl/DUSRSECJ.jcl:83` |

## ESDSRRDS

Page: [ESDSRRDS](../../01-detailed-documentation/application-documentation/06-batch/jobs/ESDSRRDS.md). Source `app/jcl/ESDSRRDS.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| PREDEL | IEFBR14 | `app/jcl/ESDSRRDS.jcl:24` |
| PREDEL.DD01 | AWS.M2.CARDDEMO.ESDSRRDS.PS DISP=(MOD,DELETE,DELETE) | `app/jcl/ESDSRRDS.jcl:26-27` |
| STEP01 | IEBGENER | `app/jcl/ESDSRRDS.jcl:33` |
| STEP01.SYSUT2 | AWS.M2.CARDDEMO.ESDSRRDS.PS DISP=(NEW,CATLG,DELETE) | `app/jcl/ESDSRRDS.jcl:47-50` |
| STEP02 | IDCAMS | `app/jcl/ESDSRRDS.jcl:59` |
| STEP03 | IDCAMS | `app/jcl/ESDSRRDS.jcl:79` |
| STEP03.IN | AWS.M2.CARDDEMO.ESDSRRDS.PS DISP=SHR | `app/jcl/ESDSRRDS.jcl:81` |
| STEP03.OUT | AWS.M2.CARDDEMO.USRSEC.VSAM.ESDS DISP=SHR | `app/jcl/ESDSRRDS.jcl:82` |
| STEP04 | IDCAMS | `app/jcl/ESDSRRDS.jcl:93` |
| STEP05 | IDCAMS | `app/jcl/ESDSRRDS.jcl:113` |
| STEP05.IN | AWS.M2.CARDDEMO.ESDSRRDS.PS DISP=SHR | `app/jcl/ESDSRRDS.jcl:115` |
| STEP05.OUT | AWS.M2.CARDDEMO.USRSEC.VSAM.RRDS DISP=SHR | `app/jcl/ESDSRRDS.jcl:116` |

## FTPJCLS

Page: [FTPJCLS](../../01-detailed-documentation/application-documentation/06-batch/jobs/FTPJCLS.md). Source `app/jcl/FTPJCL.JCL`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP1 | FTP | `app/jcl/FTPJCL.JCL:30` |

## IMSMQCMP

Page: [IMSMQCMP](../../01-detailed-documentation/application-documentation/06-batch/jobs/IMSMQCMP.md). Source `samples/jcl/IMSMQCMP.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| TRN | DFHECP1$ | `samples/jcl/IMSMQCMP.jcl:28` |
| TRN.SYSIN | &HLQ..COBOL.SRC(IMSMQPGM) DISP=SHR | `samples/jcl/IMSMQCMP.jcl:30` |
| TRN.SYSPUNCH | &&SYSCIN DISP=(,PASS) | `samples/jcl/IMSMQCMP.jcl:32-35` |
| COBOL | IGYCRCTL | `samples/jcl/IMSMQCMP.jcl:37-38` |
| COBOL.SYSLIN | &&LOADSET DISP=(MOD,PASS) | `samples/jcl/IMSMQCMP.jcl:43-45` |
| COBOL.SYSLIB | CEE.SCEESAMP DISP=SHR | `samples/jcl/IMSMQCMP.jcl:62` |
| COBOL.SYSLIB | &CICSHLQ..CICS.SDFHCOB DISP=SHR | `samples/jcl/IMSMQCMP.jcl:63` |
| COBOL.SYSLIB | &MQHLQ..SCSQCOBC DISP=SHR | `samples/jcl/IMSMQCMP.jcl:64` |
| COBOL.SYSLIB | &HLQ..COBCOPY DISP=SHR | `samples/jcl/IMSMQCMP.jcl:65` |
| COBOL.SYSIN | &&SYSCIN DISP=(OLD,DELETE) | `samples/jcl/IMSMQCMP.jcl:66` |
| COPYIMS | IEBGENER | `samples/jcl/IMSMQCMP.jcl:71` |
| COPYIMS.SYSUT2 | &&COPYIMS DISP=(NEW,PASS) | `samples/jcl/IMSMQCMP.jcl:76-78` |
| COPYLINK | IEBGENER | `samples/jcl/IMSMQCMP.jcl:82` |
| COPYLINK.SYSUT2 | &&COPYLINK DISP=(NEW,PASS) | `samples/jcl/IMSMQCMP.jcl:85-87` |
| COPYMQ | IEBGENER | `samples/jcl/IMSMQCMP.jcl:91` |
| COPYMQ.SYSUT2 | &&COPYMQ DISP=(NEW,PASS) | `samples/jcl/IMSMQCMP.jcl:94-96` |
| LKED | IEWL | `samples/jcl/IMSMQCMP.jcl:100` |
| LKED.SYSLIB | &MQHLQ..SCSQLOAD DISP=SHR | `samples/jcl/IMSMQCMP.jcl:101` |
| LKED.SYSLIB | SYS1.LINKLIB DISP=SHR | `samples/jcl/IMSMQCMP.jcl:102` |
| LKED.SYSLIB | CEE.SCEELKED DISP=SHR | `samples/jcl/IMSMQCMP.jcl:103` |
| LKED.SYSLIB | &CICSHLQ..CICS.SDFHLOAD DISP=SHR | `samples/jcl/IMSMQCMP.jcl:104` |
| LKED.SYSLIB | &IMSHLQ..SDFSRESL DISP=SHR | `samples/jcl/IMSMQCMP.jcl:105` |
| LKED.CSQSTUB | &MQHLQ..SCSQLOAD DISP=SHR | `samples/jcl/IMSMQCMP.jcl:106` |
| LKED.SYSLIN | &&COPYLINK DISP=(OLD,DELETE) | `samples/jcl/IMSMQCMP.jcl:107` |
| LKED.SYSLIN | &&COPYMQ DISP=(OLD,DELETE) | `samples/jcl/IMSMQCMP.jcl:108` |
| LKED.SYSLIN | &&LOADSET DISP=(OLD,DELETE) | `samples/jcl/IMSMQCMP.jcl:109` |
| LKED.SYSLIN | &&COPYIMS DISP=(OLD,DELETE) | `samples/jcl/IMSMQCMP.jcl:110` |
| LKED.SYSLMOD | &HLQ..CICSLOAD(IMSMQPGM) DISP=SHR | `samples/jcl/IMSMQCMP.jcl:112-113` |

## INTCALC

Page: [INTCALC](../../01-detailed-documentation/application-documentation/06-batch/jobs/INTCALC.md). Source `app/jcl/INTCALC.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP15 | CBACT04C | `app/jcl/INTCALC.jcl:22` |
| STEP15.TCATBALF | AWS.M2.CARDDEMO.TCATBALF.VSAM.KSDS DISP=SHR | `app/jcl/INTCALC.jcl:27-28` |
| STEP15.XREFFILE | AWS.M2.CARDDEMO.CARDXREF.VSAM.KSDS DISP=SHR | `app/jcl/INTCALC.jcl:29-30` |
| STEP15.XREFFIL1 | AWS.M2.CARDDEMO.CARDXREF.VSAM.AIX.PATH DISP=SHR | `app/jcl/INTCALC.jcl:31-32` |
| STEP15.ACCTFILE | AWS.M2.CARDDEMO.ACCTDATA.VSAM.KSDS DISP=SHR | `app/jcl/INTCALC.jcl:33-34` |
| STEP15.DISCGRP | AWS.M2.CARDDEMO.DISCGRP.VSAM.KSDS DISP=SHR | `app/jcl/INTCALC.jcl:35-36` |
| STEP15.TRANSACT | AWS.M2.CARDDEMO.SYSTRAN(+1) DISP=(NEW,CATLG,DELETE) | `app/jcl/INTCALC.jcl:37-41` |
| predecessor | CLOSEFIL | `app/scheduler/CardDemo.controlm:66`, `app/scheduler/CardDemo.controlm:70` |
| successor | COMBTRAN | `app/scheduler/CardDemo.controlm:72`, `app/scheduler/CardDemo.controlm:76` |

## INTRDRJ1

Page: [INTRDRJ1](../../01-detailed-documentation/application-documentation/06-batch/jobs/INTRDRJ1.md). Source `app/jcl/INTRDRJ1.JCL`.

| Step / relation | Target | Evidence |
|---|---|---|
| IDCAMS | IDCAMS | `app/jcl/INTRDRJ1.JCL:6` |
| IDCAMS.IN | AWS.M2.CARDEMO.FTP.TEST DISP=SHR | `app/jcl/INTRDRJ1.JCL:8` |
| IDCAMS.OUT | AWS.M2.CARDEMO.FTP.TEST.BKUP DISP=SHR | `app/jcl/INTRDRJ1.JCL:9` |
| STEP01 | IEBGENER | `app/jcl/INTRDRJ1.JCL:14` |
| STEP01.SYSUT1 | AWS.M2.CARDDEMO.JCL(INTRDRJ2) DISP=SHR | `app/jcl/INTRDRJ1.JCL:17` |

## INTRDRJ2

Page: [INTRDRJ2](../../01-detailed-documentation/application-documentation/06-batch/jobs/INTRDRJ2.md). Source `app/jcl/INTRDRJ2.JCL`.

| Step / relation | Target | Evidence |
|---|---|---|
| IDCAMS | IDCAMS | `app/jcl/INTRDRJ2.JCL:7` |
| IDCAMS.IN | AWS.M2.CARDEMO.FTP.TEST.BKUP DISP=SHR | `app/jcl/INTRDRJ2.JCL:9` |
| IDCAMS.OUT | AWS.M2.CARDEMO.FTP.TEST.BKUP.INTRDR DISP=SHR | `app/jcl/INTRDRJ2.JCL:10` |

## LISTFILS

Page: [LISTFILS](../../01-detailed-documentation/application-documentation/06-batch/jobs/LISTFILS.md). Source `samples/jcl/LISTCAT.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP01 | IEFBR14 | `samples/jcl/LISTCAT.jcl:21` |
| STEP01.DD1 | AWS.M2.CARDDEMO.LISTCAT DISP=(MOD,DELETE,DELETE) | `samples/jcl/LISTCAT.jcl:22-26` |
| STEP05 | IDCAMS | `samples/jcl/LISTCAT.jcl:27` |
| STEP05.SYSPRINT | AWS.M2.CARDDEMO.LISTCAT DISP=(NEW,CATLG,DELETE) | `samples/jcl/LISTCAT.jcl:28-32` |

## LOADPADB

Page: [LOADPADB](../../01-detailed-documentation/application-documentation/06-batch/jobs/LOADPADB.md). Source `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP01 | DFSRRC00 -> PAUDBLOD | `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL:26-27` |
| STEP01.DFSRESLB | OEMA.IMS.IMSP.SDFSRESL DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL:31` |
| STEP01.IMS | OEM.IMS.IMSP.PSBLIB DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL:33` |
| STEP01.IMS | OEM.IMS.IMSP.DBDLIB DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL:34` |
| STEP01.INFILE1 | AWS.M2.CARDDEMO.PAUTDB.ROOT.FILEO DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL:36` |
| STEP01.INFILE2 | AWS.M2.CARDDEMO.PAUTDB.CHILD.FILEO DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL:38` |
| STEP01.DFSVSAMP | OEMPP.IMS.V15R01MB.PROCLIB(DFSVSMDB) DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL:44-45` |

## MNTTRDB2

Page: [MNTTRDB2](../../01-detailed-documentation/application-documentation/06-batch/jobs/MNTTRDB2.md). Source `app/app-transaction-type-db2/jcl/MNTTRDB2.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP1 | IKJEFT01 -> COBTUPDT | `app/app-transaction-type-db2/jcl/MNTTRDB2.jcl:21` |
| STEP1.DBRMLIB | AWS.M2.CARDDEMO.DBRMLIB DISP=SHR | `app/app-transaction-type-db2/jcl/MNTTRDB2.jcl:25` |
| STEP1.INPFILE | INPFILE DISP=SHR | `app/app-transaction-type-db2/jcl/MNTTRDB2.jcl:27` |
| successor | CLOSEFIL | `app/scheduler/CardDemo.controlm:28`, `app/scheduler/CardDemo.controlm:34` |
| successor | TRANEXTR | `app/scheduler/CardDemo.controlm:28`, `app/scheduler/CardDemo.controlm:59` |

## OPENFIL

Page: [OPENFIL](../../01-detailed-documentation/application-documentation/06-batch/jobs/OPENFIL.md). Source `app/jcl/OPENFIL.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| OPCIFIL | SDSF | `app/jcl/OPENFIL.jcl:22` |
| predecessor | WAITSTEP | `app/scheduler/CardDemo.ca7:124` |
| predecessor | WAITSTEP | `app/scheduler/CardDemo.ca7:453` |
| predecessor | WAITSTEP | `app/scheduler/CardDemo.ca7:527` |
| successor | CLOSEFIL | `app/scheduler/CardDemo.ca7:532` |
| predecessor | WAITSTEP | `app/scheduler/CardDemo.ca7:569` |
| predecessor | WAITSTEP | `app/scheduler/CardDemo.controlm:17`, `app/scheduler/CardDemo.controlm:21` |
| predecessor | WAITSTEP | `app/scheduler/CardDemo.controlm:84`, `app/scheduler/CardDemo.controlm:88` |
| predecessor | WAITSTEP | `app/scheduler/CardDemo.controlm:47`, `app/scheduler/CardDemo.controlm:51` |

## POSTTRAN

Page: [POSTTRAN](../../01-detailed-documentation/application-documentation/06-batch/jobs/POSTTRAN.md). Source `app/jcl/POSTTRAN.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP15 | CBTRN02C | `app/jcl/POSTTRAN.jcl:23` |
| STEP15.TRANFILE | AWS.M2.CARDDEMO.TRANSACT.VSAM.KSDS DISP=SHR | `app/jcl/POSTTRAN.jcl:28-29` |
| STEP15.DALYTRAN | AWS.M2.CARDDEMO.DALYTRAN.PS DISP=SHR | `app/jcl/POSTTRAN.jcl:30-31` |
| STEP15.XREFFILE | AWS.M2.CARDDEMO.CARDXREF.VSAM.KSDS DISP=SHR | `app/jcl/POSTTRAN.jcl:32-33` |
| STEP15.DALYREJS | AWS.M2.CARDDEMO.DALYREJS(+1) DISP=(NEW,CATLG,DELETE) | `app/jcl/POSTTRAN.jcl:34-38` |
| STEP15.ACCTFILE | AWS.M2.CARDDEMO.ACCTDATA.VSAM.KSDS DISP=SHR | `app/jcl/POSTTRAN.jcl:39-40` |
| STEP15.TCATBALF | AWS.M2.CARDDEMO.TCATBALF.VSAM.KSDS DISP=SHR | `app/jcl/POSTTRAN.jcl:41-42` |
| predecessor | CBPAUP0J | `app/scheduler/CardDemo.ca7:70` |
| successor | WAITSTEP | `app/scheduler/CardDemo.ca7:97` |

## PRTCATBL

Page: [PRTCATBL](../../01-detailed-documentation/application-documentation/06-batch/jobs/PRTCATBL.md). Source `app/jcl/PRTCATBL.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| DELDEF | IEFBR14 | `app/jcl/PRTCATBL.jcl:21` |
| DELDEF.THEFILE | AWS.M2.CARDDEMO.TCATBALF.REPT DISP=(MOD,DELETE) | `app/jcl/PRTCATBL.jcl:22-25` |
| STEP05R | PROC REPROC | `app/jcl/PRTCATBL.jcl:29-30` |
| STEP05R.PRC001.FILEIN | AWS.M2.CARDDEMO.TCATBALF.VSAM.KSDS DISP=SHR | `app/jcl/PRTCATBL.jcl:32-33` |
| STEP05R.PRC001.FILEOUT | AWS.M2.CARDDEMO.TCATBALF.BKUP(+1) DISP=(NEW,CATLG,DELETE) | `app/jcl/PRTCATBL.jcl:35-39` |
| STEP10R | SORT | `app/jcl/PRTCATBL.jcl:43` |
| STEP10R.SORTIN | AWS.M2.CARDDEMO.TCATBALF.BKUP(+1) DISP=SHR | `app/jcl/PRTCATBL.jcl:44-45` |
| STEP10R.SORTOUT | AWS.M2.CARDDEMO.TCATBALF.REPT DISP=(NEW,CATLG,DELETE) | `app/jcl/PRTCATBL.jcl:59-63` |
| predecessor | CLOSEFIL | `app/scheduler/CardDemo.ca7:537` |
| successor | WAITSTEP | `app/scheduler/CardDemo.ca7:564` |

## RACFCMDS

Page: [RACFCMDS](../../01-detailed-documentation/application-documentation/06-batch/jobs/RACFCMDS.md). Source `samples/jcl/RACFCMDS.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| TSOBAT | IKJEFT01 | `samples/jcl/RACFCMDS.jcl:19` |

## READACCT

Page: [READACCT](../../01-detailed-documentation/application-documentation/06-batch/jobs/READACCT.md). Source `app/jcl/READACCT.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| PREDEL | IEFBR14 | `app/jcl/READACCT.jcl:22` |
| PREDEL.DD01 | AWS.M2.CARDDEMO.ACCTDATA.PSCOMP DISP=(MOD,DELETE,DELETE) | `app/jcl/READACCT.jcl:23-24` |
| PREDEL.DD02 | AWS.M2.CARDDEMO.ACCTDATA.ARRYPS DISP=(MOD,DELETE,DELETE) | `app/jcl/READACCT.jcl:25-26` |
| PREDEL.DD03 | AWS.M2.CARDDEMO.ACCTDATA.VBPS DISP=(MOD,DELETE,DELETE) | `app/jcl/READACCT.jcl:27-28` |
| STEP05 | CBACT01C | `app/jcl/READACCT.jcl:32` |
| STEP05.ACCTFILE | AWS.M2.CARDDEMO.ACCTDATA.VSAM.KSDS DISP=SHR | `app/jcl/READACCT.jcl:35-36` |
| STEP05.OUTFILE | AWS.M2.CARDDEMO.ACCTDATA.PSCOMP DISP=(NEW,CATLG,DELETE) | `app/jcl/READACCT.jcl:37-40` |
| STEP05.ARRYFILE | AWS.M2.CARDDEMO.ACCTDATA.ARRYPS DISP=(NEW,CATLG,DELETE) | `app/jcl/READACCT.jcl:41-44` |
| STEP05.VBRCFILE | AWS.M2.CARDDEMO.ACCTDATA.VBPS DISP=(NEW,CATLG,DELETE) | `app/jcl/READACCT.jcl:45-48` |
| predecessor | CLOSEFIL | `app/scheduler/CardDemo.ca7:340` |
| successor | READCARD | `app/scheduler/CardDemo.ca7:367` |

## READCARD

Page: [READCARD](../../01-detailed-documentation/application-documentation/06-batch/jobs/READCARD.md). Source `app/jcl/READCARD.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP05 | CBACT02C | `app/jcl/READCARD.jcl:22` |
| STEP05.CARDFILE | AWS.M2.CARDDEMO.CARDDATA.VSAM.KSDS DISP=SHR | `app/jcl/READCARD.jcl:25-26` |
| predecessor | READACCT | `app/scheduler/CardDemo.ca7:367` |
| successor | READCUST | `app/scheduler/CardDemo.ca7:394` |

## READCUST

Page: [READCUST](../../01-detailed-documentation/application-documentation/06-batch/jobs/READCUST.md). Source `app/jcl/READCUST.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP05 | CBCUS01C | `app/jcl/READCUST.jcl:21` |
| STEP05.CUSTFILE | AWS.M2.CARDDEMO.CUSTDATA.VSAM.KSDS DISP=SHR | `app/jcl/READCUST.jcl:24-25` |
| predecessor | READCARD | `app/scheduler/CardDemo.ca7:394` |
| successor | READXREF | `app/scheduler/CardDemo.ca7:421` |

## READXREF

Page: [READXREF](../../01-detailed-documentation/application-documentation/06-batch/jobs/READXREF.md). Source `app/jcl/READXREF.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP05 | CBACT03C | `app/jcl/READXREF.jcl:22` |
| STEP05.XREFFILE | AWS.M2.CARDDEMO.CARDXREF.VSAM.KSDS DISP=SHR | `app/jcl/READXREF.jcl:25-26` |
| predecessor | READCUST | `app/scheduler/CardDemo.ca7:421` |
| successor | WAITSTEP | `app/scheduler/CardDemo.ca7:448` |

## REPRTEST

Page: [REPRTEST](../../01-detailed-documentation/application-documentation/06-batch/jobs/REPRTEST.md). Source `samples/jcl/REPRTEST.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP05 | PROC REPROC | `samples/jcl/REPRTEST.jcl:23-24` |
| STEP05.PRC001.FILEIN | AWS.M2.CARDDEMO.TRANSACT.VSAM.KSDS DISP=SHR | `samples/jcl/REPRTEST.jcl:26-27` |
| STEP05.PRC001.FILEOUT | AWS.M2.CARDDEMO.TRANSACT.BKUP(+1) DISP=(NEW,CATLG,DELETE) | `samples/jcl/REPRTEST.jcl:29-33` |

## REPTFILE

Page: [REPTFILE](../../01-detailed-documentation/application-documentation/06-batch/jobs/REPTFILE.md). Source `app/jcl/REPTFILE.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP05 | IDCAMS | `app/jcl/REPTFILE.jcl:22` |

## SORTTEST

Page: [SORTTEST](../../01-detailed-documentation/application-documentation/06-batch/jobs/SORTTEST.md). Source `samples/jcl/SORTTEST.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP05R | SORT | `samples/jcl/SORTTEST.jcl:19` |
| STEP05R.SORTIN | AWS.M2.CARDDEMO.TRANSACT.BKUP(0) DISP=SHR | `samples/jcl/SORTTEST.jcl:20-21` |
| STEP05R.SORTOUT | AWS.M2.CARDDEMO.TRANSACT.DALY(+1) DISP=(NEW,CATLG,DELETE) | `samples/jcl/SORTTEST.jcl:31-35` |

## TCATBALF

Page: [TCATBALF](../../01-detailed-documentation/application-documentation/06-batch/jobs/TCATBALF.md). Source `app/jcl/TCATBALF.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP05 | IDCAMS | `app/jcl/TCATBALF.jcl:22` |
| STEP10 | IDCAMS | `app/jcl/TCATBALF.jcl:33` |
| STEP15 | IDCAMS | `app/jcl/TCATBALF.jcl:54` |
| STEP15.TCATBAL | AWS.M2.CARDDEMO.TCATBALF.PS DISP=SHR | `app/jcl/TCATBALF.jcl:56-57` |
| STEP15.TCATBALV | AWS.M2.CARDDEMO.TCATBALF.VSAM.KSDS DISP=OLD | `app/jcl/TCATBALF.jcl:58-59` |
| predecessor | CLOSEFIL2 | `app/scheduler/CardDemo.ca7:271` |
| successor | WAITSTEP | `app/scheduler/CardDemo.ca7:330` |

## TRANBKP

Page: [TRANBKP](../../01-detailed-documentation/application-documentation/06-batch/jobs/TRANBKP.md). Source `app/jcl/TRANBKP.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP05R | PROC REPROC | `app/jcl/TRANBKP.jcl:23-24` |
| STEP05R.PRC001.FILEIN | AWS.M2.CARDDEMO.TRANSACT.VSAM.KSDS DISP=SHR | `app/jcl/TRANBKP.jcl:26-27` |
| STEP05R.PRC001.FILEOUT | AWS.M2.CARDDEMO.TRANSACT.BKUP(+1) DISP=(NEW,CATLG,DELETE) | `app/jcl/TRANBKP.jcl:29-33` |
| STEP05 | IDCAMS | `app/jcl/TRANBKP.jcl:37` |
| STEP10 | IDCAMS | `app/jcl/TRANBKP.jcl:51` |
| predecessor | CLOSEFIL | `app/scheduler/CardDemo.controlm:5`, `app/scheduler/CardDemo.controlm:9` |
| successor | WAITSTEP | `app/scheduler/CardDemo.controlm:11`, `app/scheduler/CardDemo.controlm:15` |

## TRANCATG

Page: [TRANCATG](../../01-detailed-documentation/application-documentation/06-batch/jobs/TRANCATG.md). Source `app/jcl/TRANCATG.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP05 | IDCAMS | `app/jcl/TRANCATG.jcl:22` |
| STEP10 | IDCAMS | `app/jcl/TRANCATG.jcl:33` |
| STEP15 | IDCAMS | `app/jcl/TRANCATG.jcl:54` |
| STEP15.TRANCATG | AWS.M2.CARDDEMO.TRANCATG.PS DISP=SHR | `app/jcl/TRANCATG.jcl:56-57` |
| STEP15.TCATVSAM | AWS.M2.CARDDEMO.TRANCATG.VSAM.KSDS DISP=OLD | `app/jcl/TRANCATG.jcl:58-59` |
| predecessor | CLOSEFIL1 | `app/scheduler/CardDemo.ca7:244` |
| successor | WAITSTEP | `app/scheduler/CardDemo.ca7:298` |

## TRANEXTR

Page: [TRANEXTR](../../01-detailed-documentation/application-documentation/06-batch/jobs/TRANEXTR.md). Source `app/app-transaction-type-db2/jcl/TRANEXTR.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP10 | IEBGENER | `app/app-transaction-type-db2/jcl/TRANEXTR.jcl:31` |
| STEP10.SYSUT1 | &HLQ..TRANTYPE.PS DISP=SHR | `app/app-transaction-type-db2/jcl/TRANEXTR.jcl:34` |
| STEP10.SYSUT2 | &HLQ..TRANTYPE.BKUP(+1) DISP=(NEW,CATLG) | `app/app-transaction-type-db2/jcl/TRANEXTR.jcl:35-38` |
| STEP20 | IEBGENER | `app/app-transaction-type-db2/jcl/TRANEXTR.jcl:42` |
| STEP20.SYSUT1 | &HLQ..TRANCATG.PS DISP=SHR | `app/app-transaction-type-db2/jcl/TRANEXTR.jcl:45` |
| STEP20.SYSUT2 | &HLQ..TRANCATG.PS.BKUP(+1) DISP=(NEW,CATLG) | `app/app-transaction-type-db2/jcl/TRANEXTR.jcl:46-49` |
| STEP30 | IEFBR14 | `app/app-transaction-type-db2/jcl/TRANEXTR.jcl:53` |
| STEP30.DD01 | &HLQ..TRANTYPE.PS DISP=(MOD,DELETE,DELETE) | `app/app-transaction-type-db2/jcl/TRANEXTR.jcl:54-57` |
| STEP30.DD02 | &HLQ..TRANCATG.PS DISP=(MOD,DELETE,DELETE) | `app/app-transaction-type-db2/jcl/TRANEXTR.jcl:58-61` |
| STEP40 | IKJEFT01 -> DSNTIAUL | `app/app-transaction-type-db2/jcl/TRANEXTR.jcl:65` |
| STEP40.SYSREC00 | &HLQ..TRANTYPE.PS DISP=(NEW,CATLG,DELETE) | `app/app-transaction-type-db2/jcl/TRANEXTR.jcl:72-74` |
| STEP50 | IKJEFT01 -> DSNTIAUL | `app/app-transaction-type-db2/jcl/TRANEXTR.jcl:95` |
| STEP50.SYSREC00 | &HLQ..TRANCATG.PS DISP=(NEW,CATLG,DELETE) | `app/app-transaction-type-db2/jcl/TRANEXTR.jcl:102-104` |
| predecessor | MNTTRDB2 | `app/scheduler/CardDemo.controlm:28`, `app/scheduler/CardDemo.controlm:59` |

## TRANFILE

Page: [TRANFILE](../../01-detailed-documentation/application-documentation/06-batch/jobs/TRANFILE.md). Source `app/jcl/TRANFILE.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| CLCIFIL | SDSF | `app/jcl/TRANFILE.jcl:22` |
| STEP05 | IDCAMS | `app/jcl/TRANFILE.jcl:32` |
| STEP10 | IDCAMS | `app/jcl/TRANFILE.jcl:46` |
| STEP15 | IDCAMS | `app/jcl/TRANFILE.jcl:67` |
| STEP15.TRANSACT | AWS.M2.CARDDEMO.DALYTRAN.PS.INIT DISP=SHR | `app/jcl/TRANFILE.jcl:69-70` |
| STEP15.TRANVSAM | AWS.M2.CARDDEMO.TRANSACT.VSAM.KSDS DISP=SHR | `app/jcl/TRANFILE.jcl:71-72` |
| STEP20 | IDCAMS | `app/jcl/TRANFILE.jcl:79` |
| STEP25 | IDCAMS | `app/jcl/TRANFILE.jcl:96` |
| STEP30 | IDCAMS | `app/jcl/TRANFILE.jcl:106` |
| OPCIFIL | SDSF | `app/jcl/TRANFILE.jcl:116` |

## TRANIDX

Page: [TRANIDX](../../01-detailed-documentation/application-documentation/06-batch/jobs/TRANIDX.md). Source `app/jcl/TRANIDX.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP20 | IDCAMS | `app/jcl/TRANIDX.jcl:22` |
| STEP25 | IDCAMS | `app/jcl/TRANIDX.jcl:39` |
| STEP30 | IDCAMS | `app/jcl/TRANIDX.jcl:49` |

## TRANREPT

Page: [TRANREPT](../../01-detailed-documentation/application-documentation/06-batch/jobs/TRANREPT.md). Source `app/jcl/TRANREPT.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP05R | PROC REPROC | `app/jcl/TRANREPT.jcl:23-24` |
| STEP05R.PRC001.FILEIN | AWS.M2.CARDDEMO.TRANSACT.VSAM.KSDS DISP=SHR | `app/jcl/TRANREPT.jcl:26-27` |
| STEP05R.PRC001.FILEOUT | AWS.M2.CARDDEMO.TRANSACT.BKUP(+1) DISP=(NEW,CATLG,DELETE) | `app/jcl/TRANREPT.jcl:29-33` |
| STEP05R | SORT | `app/jcl/TRANREPT.jcl:37` |
| STEP05R.SORTIN | AWS.M2.CARDDEMO.TRANSACT.BKUP(+1) DISP=SHR | `app/jcl/TRANREPT.jcl:38-39` |
| STEP05R.SORTOUT | AWS.M2.CARDDEMO.TRANSACT.DALY(+1) DISP=(NEW,CATLG,DELETE) | `app/jcl/TRANREPT.jcl:51-55` |
| STEP10R | CBTRN03C | `app/jcl/TRANREPT.jcl:59` |
| STEP10R.TRANFILE | AWS.M2.CARDDEMO.TRANSACT.DALY(+1) DISP=SHR | `app/jcl/TRANREPT.jcl:65-66` |
| STEP10R.CARDXREF | AWS.M2.CARDDEMO.CARDXREF.VSAM.KSDS DISP=SHR | `app/jcl/TRANREPT.jcl:67-68` |
| STEP10R.TRANTYPE | AWS.M2.CARDDEMO.TRANTYPE.VSAM.KSDS DISP=SHR | `app/jcl/TRANREPT.jcl:69-70` |
| STEP10R.TRANCATG | AWS.M2.CARDDEMO.TRANCATG.VSAM.KSDS DISP=SHR | `app/jcl/TRANREPT.jcl:71-72` |
| STEP10R.DATEPARM | AWS.M2.CARDDEMO.DATEPARM DISP=SHR | `app/jcl/TRANREPT.jcl:73-74` |
| STEP10R.TRANREPT | AWS.M2.CARDDEMO.TRANREPT(+1) DISP=(NEW,CATLG,DELETE) | `app/jcl/TRANREPT.jcl:76-80` |

## TRANTYPE

Page: [TRANTYPE](../../01-detailed-documentation/application-documentation/06-batch/jobs/TRANTYPE.md). Source `app/jcl/TRANTYPE.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP05 | IDCAMS | `app/jcl/TRANTYPE.jcl:22` |
| STEP10 | IDCAMS | `app/jcl/TRANTYPE.jcl:33` |
| STEP15 | IDCAMS | `app/jcl/TRANTYPE.jcl:54` |
| STEP15.TRANTYPE | AWS.M2.CARDDEMO.TRANTYPE.PS DISP=SHR | `app/jcl/TRANTYPE.jcl:56-57` |
| STEP15.TTYPVSAM | AWS.M2.CARDDEMO.TRANTYPE.VSAM.KSDS DISP=OLD | `app/jcl/TRANTYPE.jcl:58-59` |
| predecessor | CLOSEFIL | `app/scheduler/CardDemo.ca7:162` |
| successor | WAITSTEP | `app/scheduler/CardDemo.ca7:189` |

## TXT2PDF1

Page: [TXT2PDF1](../../01-detailed-documentation/application-documentation/06-batch/jobs/TXT2PDF1.md). Source `app/jcl/TXT2PDF1.JCL`.

| Step / relation | Target | Evidence |
|---|---|---|
| TXT2PDF | IKJEFT1B | `app/jcl/TXT2PDF1.JCL:24-26` |
| TXT2PDF.SYSEXEC | AWS.M2.LBD.TXT2PDF.EXEC DISP=SHR | `app/jcl/TXT2PDF1.JCL:31` |
| TXT2PDF.INDD | AWS.M2.CARDDEMO.STATEMNT.PS DISP=SHR | `app/jcl/TXT2PDF1.JCL:33` |
| predecessor | CREASTMT | `app/scheduler/CardDemo.ca7:495` |
| successor | WAITSTEP | `app/scheduler/CardDemo.ca7:522` |

## UNLDGSAM

Page: [UNLDGSAM](../../01-detailed-documentation/application-documentation/06-batch/jobs/UNLDGSAM.md). Source `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP01 | DFSRRC00 -> DBUNLDGS | `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:26-27` |
| STEP01.DFSRESLB | OEMA.IMS.IMSP.SDFSRESL DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:31` |
| STEP01.IMS | OEM.IMS.IMSP.PSBLIB DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:33` |
| STEP01.IMS | OEM.IMS.IMSP.DBDLIB DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:34` |
| STEP01.PASFILOP | AWS.M2.CARDDEMO.PAUTDB.ROOT.GSAM DISP=(OLD,KEEP,KEEP) | `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:36-37` |
| STEP01.PADFILOP | AWS.M2.CARDDEMO.PAUTDB.CHILD.GSAM DISP=(OLD,KEEP,KEEP) | `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:39-40` |
| STEP01.DDPAUTP0 | OEM.IMS.IMSP.PAUTHDB DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:42` |
| STEP01.DDPAUTX0 | OEM.IMS.IMSP.PAUTHDBX DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:43` |
| STEP01.DFSVSAMP | OEMPP.IMS.V15R01MB.PROCLIB(DFSVSMDB) DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:46-47` |

## UNLDPADB

Page: [UNLDPADB](../../01-detailed-documentation/application-documentation/06-batch/jobs/UNLDPADB.md). Source `app/app-authorization-ims-db2-mq/jcl/UNLDPADB.JCL`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP0 | IEFBR14 | `app/app-authorization-ims-db2-mq/jcl/UNLDPADB.JCL:25` |
| STEP0.DD1 | AWS.M2.CARDDEMO.PAUTDB.ROOT.FILEO DISP=(OLD,DELETE,DELETE) | `app/app-authorization-ims-db2-mq/jcl/UNLDPADB.JCL:33-34` |
| STEP0.DD2 | AWS.M2.CARDDEMO.PAUTDB.CHILD.FILEO DISP=(OLD,DELETE,DELETE) | `app/app-authorization-ims-db2-mq/jcl/UNLDPADB.JCL:35-36` |
| STEP01 | DFSRRC00 -> PAUDBUNL | `app/app-authorization-ims-db2-mq/jcl/UNLDPADB.JCL:38-39` |
| STEP01.DFSRESLB | OEMA.IMS.IMSP.SDFSRESL DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/UNLDPADB.JCL:43` |
| STEP01.IMS | OEM.IMS.IMSP.PSBLIB DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/UNLDPADB.JCL:45` |
| STEP01.IMS | OEM.IMS.IMSP.DBDLIB DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/UNLDPADB.JCL:46` |
| STEP01.OUTFIL1 | AWS.M2.CARDDEMO.PAUTDB.ROOT.FILEO DISP=(NEW,CATLG,DELETE) | `app/app-authorization-ims-db2-mq/jcl/UNLDPADB.JCL:48-51` |
| STEP01.OUTFIL2 | AWS.M2.CARDDEMO.PAUTDB.CHILD.FILEO DISP=(NEW,CATLG,DELETE) | `app/app-authorization-ims-db2-mq/jcl/UNLDPADB.JCL:53-56` |
| STEP01.DDPAUTP0 | OEM.IMS.IMSP.PAUTHDB DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/UNLDPADB.JCL:58` |
| STEP01.DDPAUTX0 | OEM.IMS.IMSP.PAUTHDBX DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/UNLDPADB.JCL:59` |
| STEP01.DFSVSAMP | OEMPP.IMS.V15R01MB.PROCLIB(DFSVSMDB) DISP=SHR | `app/app-authorization-ims-db2-mq/jcl/UNLDPADB.JCL:62-63` |

## WAITSTEP

Page: [WAITSTEP](../../01-detailed-documentation/application-documentation/06-batch/jobs/WAITSTEP.md). Source `app/jcl/WAITSTEP.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| WAIT | COBSWAIT | `app/jcl/WAITSTEP.jcl:22` |
| predecessor | POSTTRAN | `app/scheduler/CardDemo.ca7:97` |
| successor | OPENFIL | `app/scheduler/CardDemo.ca7:124` |
| predecessor | TRANTYPE | `app/scheduler/CardDemo.ca7:189` |
| successor | CLOSEFIL1 | `app/scheduler/CardDemo.ca7:216` |
| successor | CLOSEFIL2 | `app/scheduler/CardDemo.ca7:217` |
| predecessor | TRANCATG | `app/scheduler/CardDemo.ca7:298` |
| successor | CLOSEFIL | `app/scheduler/CardDemo.ca7:303` |
| predecessor | TCATBALF | `app/scheduler/CardDemo.ca7:330` |
| successor | CLOSEFIL | `app/scheduler/CardDemo.ca7:335` |
| predecessor | READXREF | `app/scheduler/CardDemo.ca7:448` |
| successor | OPENFIL | `app/scheduler/CardDemo.ca7:453` |
| predecessor | TXT2PDF1 | `app/scheduler/CardDemo.ca7:522` |
| successor | OPENFIL | `app/scheduler/CardDemo.ca7:527` |
| predecessor | PRTCATBL | `app/scheduler/CardDemo.ca7:564` |
| successor | OPENFIL | `app/scheduler/CardDemo.ca7:569` |
| predecessor | TRANBKP | `app/scheduler/CardDemo.controlm:11`, `app/scheduler/CardDemo.controlm:15` |
| successor | OPENFIL | `app/scheduler/CardDemo.controlm:17`, `app/scheduler/CardDemo.controlm:21` |
| predecessor | COMBTRAN | `app/scheduler/CardDemo.controlm:78`, `app/scheduler/CardDemo.controlm:82` |
| successor | OPENFIL | `app/scheduler/CardDemo.controlm:84`, `app/scheduler/CardDemo.controlm:88` |
| predecessor | DISCGRP | `app/scheduler/CardDemo.controlm:41`, `app/scheduler/CardDemo.controlm:45` |
| successor | OPENFIL | `app/scheduler/CardDemo.controlm:47`, `app/scheduler/CardDemo.controlm:51` |

## XREFFILE

Page: [XREFFILE](../../01-detailed-documentation/application-documentation/06-batch/jobs/XREFFILE.md). Source `app/jcl/XREFFILE.jcl`.

| Step / relation | Target | Evidence |
|---|---|---|
| STEP05 | IDCAMS | `app/jcl/XREFFILE.jcl:22` |
| STEP10 | IDCAMS | `app/jcl/XREFFILE.jcl:36` |
| STEP15 | IDCAMS | `app/jcl/XREFFILE.jcl:57` |
| STEP15.XREFDATA | AWS.M2.CARDDEMO.CARDXREF.PS DISP=SHR | `app/jcl/XREFFILE.jcl:59-60` |
| STEP15.XREFVSAM | AWS.M2.CARDDEMO.CARDXREF.VSAM.KSDS DISP=SHR | `app/jcl/XREFFILE.jcl:61-62` |
| STEP20 | IDCAMS | `app/jcl/XREFFILE.jcl:69` |
| STEP25 | IDCAMS | `app/jcl/XREFFILE.jcl:87` |
| STEP30 | IDCAMS | `app/jcl/XREFFILE.jcl:97` |

## Sources

- `docs/_work/structure/jcl/`
- `docs/_work/batch/schedule.json`

## Confidence

Confirmed from JCL and scheduler exports.
