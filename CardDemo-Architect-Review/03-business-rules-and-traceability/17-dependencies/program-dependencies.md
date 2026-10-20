# Program dependencies

For each COBOL program: what starts it, what it calls or transfers to, the copybooks it copies, and the data stores it touches.

## CBACT01C

Page: [CBACT01C](../../01-detailed-documentation/application-documentation/07-programs/CBACT01C.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | job [READACCT](../../01-detailed-documentation/application-documentation/06-batch/jobs/READACCT.md) step STEP05 | `app/jcl/READACCT.jcl:32` |
| calls/transfers to | COBDATFT (CALL-static) | `app/cbl/CBACT01C.cbl:231` |
| calls/transfers to | CEE3ABD (CALL-static) | `app/cbl/CBACT01C.cbl:410` |
| copies | CVACT01Y | `app/cbl/CBACT01C.cbl:89` |
| copies | CODATECN | `app/cbl/CBACT01C.cbl:90` |
| data store | VBRC-FILE [C] | `app/cbl/CBACT01C.cbl:290-305` |
| data store | ACCTFILE-FILE [R] | `app/cbl/CBACT01C.cbl:166-319` |
| data store | ARRY-FILE [C] | `app/cbl/CBACT01C.cbl:264` |
| data store | OUT-FILE [C] | `app/cbl/CBACT01C.cbl:243` |

## CBACT02C

Page: [CBACT02C](../../01-detailed-documentation/application-documentation/07-programs/CBACT02C.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | job [READCARD](../../01-detailed-documentation/application-documentation/06-batch/jobs/READCARD.md) step STEP05 | `app/jcl/READCARD.jcl:22` |
| calls/transfers to | CEE3ABD (CALL-static) | `app/cbl/CBACT02C.cbl:158` |
| copies | CVACT02Y | `app/cbl/CBACT02C.cbl:45` |
| data store | CARDFILE-FILE [R] | `app/cbl/CBACT02C.cbl:93-120` |

## CBACT03C

Page: [CBACT03C](../../01-detailed-documentation/application-documentation/07-programs/CBACT03C.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | job [READXREF](../../01-detailed-documentation/application-documentation/06-batch/jobs/READXREF.md) step STEP05 | `app/jcl/READXREF.jcl:22` |
| calls/transfers to | CEE3ABD (CALL-static) | `app/cbl/CBACT03C.cbl:158` |
| copies | CVACT03Y | `app/cbl/CBACT03C.cbl:45` |
| data store | XREFFILE-FILE [R] | `app/cbl/CBACT03C.cbl:93-120` |

## CBACT04C

Page: [CBACT04C](../../01-detailed-documentation/application-documentation/07-programs/CBACT04C.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | job [INTCALC](../../01-detailed-documentation/application-documentation/06-batch/jobs/INTCALC.md) step STEP15 | `app/jcl/INTCALC.jcl:22` |
| calls/transfers to | CEE3ABD (CALL-static) | `app/cbl/CBACT04C.cbl:632` |
| copies | CVTRA01Y | `app/cbl/CBACT04C.cbl:97` |
| copies | CVACT03Y | `app/cbl/CBACT04C.cbl:102` |
| copies | CVTRA02Y | `app/cbl/CBACT04C.cbl:107` |
| copies | CVACT01Y | `app/cbl/CBACT04C.cbl:112` |
| copies | CVTRA05Y | `app/cbl/CBACT04C.cbl:117` |
| data store | TRANSACT-FILE [C] | `app/cbl/CBACT04C.cbl:309` |
| data store | TCATBAL-FILE [R] | `app/cbl/CBACT04C.cbl:236-326` |
| data store | XREF-FILE [R] | `app/cbl/CBACT04C.cbl:254-394` |
| data store | ACCOUNT-FILE [R, U] | `app/cbl/CBACT04C.cbl:291-373` |
| data store | DISCGRP-FILE [R] | `app/cbl/CBACT04C.cbl:272-444` |

## CBCUS01C

Page: [CBCUS01C](../../01-detailed-documentation/application-documentation/07-programs/CBCUS01C.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | job [READCUST](../../01-detailed-documentation/application-documentation/06-batch/jobs/READCUST.md) step STEP05 | `app/jcl/READCUST.jcl:21` |
| calls/transfers to | CEE3ABD (CALL-static) | `app/cbl/CBCUS01C.cbl:158` |
| copies | CVCUS01Y | `app/cbl/CBCUS01C.cbl:45` |
| data store | CUSTFILE-FILE [R] | `app/cbl/CBCUS01C.cbl:93-120` |

## CBEXPORT

Page: [CBEXPORT](../../01-detailed-documentation/application-documentation/07-programs/CBEXPORT.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | job [CBEXPORT](../../01-detailed-documentation/application-documentation/06-batch/jobs/CBEXPORT.md) step STEP02 | `app/jcl/CBEXPORT.jcl:43` |
| calls/transfers to | CEE3ABD (CALL-static) | `app/cbl/CBEXPORT.cbl:579` |
| copies | CVCUS01Y | `app/cbl/CBEXPORT.cbl:75` |
| copies | CVACT01Y | `app/cbl/CBEXPORT.cbl:78` |
| copies | CVACT03Y | `app/cbl/CBEXPORT.cbl:81` |
| copies | CVTRA05Y | `app/cbl/CBEXPORT.cbl:84` |
| copies | CVACT02Y | `app/cbl/CBEXPORT.cbl:87` |
| copies | CVEXPORT | `app/cbl/CBEXPORT.cbl:96` |
| data store | CUSTOMER-INPUT [R] | `app/cbl/CBEXPORT.cbl:200-260` |
| data store | ACCOUNT-INPUT [R] | `app/cbl/CBEXPORT.cbl:207-329` |
| data store | XREF-INPUT [R] | `app/cbl/CBEXPORT.cbl:214-393` |
| data store | CARD-INPUT [R] | `app/cbl/CBEXPORT.cbl:228-513` |
| data store | EXPORT-OUTPUT [C] | `app/cbl/CBEXPORT.cbl:235` |
| data store | TRANSACTION-INPUT [R] | `app/cbl/CBEXPORT.cbl:221-448` |

## CBIMPORT

Page: [CBIMPORT](../../01-detailed-documentation/application-documentation/07-programs/CBIMPORT.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | job [CBIMPORT](../../01-detailed-documentation/application-documentation/06-batch/jobs/CBIMPORT.md) step STEP01 | `app/jcl/CBIMPORT.jcl:22` |
| calls/transfers to | CEE3ABD (CALL-static) | `app/cbl/CBIMPORT.cbl:484` |
| copies | CVCUS01Y | `app/cbl/CBIMPORT.cbl:84` |
| copies | CVACT01Y | `app/cbl/CBIMPORT.cbl:89` |
| copies | CVACT03Y | `app/cbl/CBIMPORT.cbl:94` |
| copies | CVTRA05Y | `app/cbl/CBIMPORT.cbl:99` |
| copies | CVACT02Y | `app/cbl/CBIMPORT.cbl:104` |
| copies | CVEXPORT | `app/cbl/CBIMPORT.cbl:113` |
| data store | EXPORT-INPUT [R] | `app/cbl/CBIMPORT.cbl:198-261` |
| data store | ACCOUNT-OUTPUT [C] | `app/cbl/CBIMPORT.cbl:212` |
| data store | TRANSACTION-OUTPUT [C] | `app/cbl/CBIMPORT.cbl:226` |
| data store | XREF-OUTPUT [C] | `app/cbl/CBIMPORT.cbl:219` |
| data store | ERROR-OUTPUT [C] | `app/cbl/CBIMPORT.cbl:439` |
| data store | CUSTOMER-OUTPUT [C] | `app/cbl/CBIMPORT.cbl:205` |
| data store | CARD-OUTPUT [C] | `app/cbl/CBIMPORT.cbl:233` |

## CBPAUP0C

Page: [CBPAUP0C](../../01-detailed-documentation/application-documentation/07-programs/CBPAUP0C.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | job [CBPAUP0J](../../01-detailed-documentation/application-documentation/06-batch/jobs/CBPAUP0J.md) step STEP01 | `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:24-25` |
| copies | CIPAUSMY | `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:117` |
| copies | CIPAUDTY | `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:121` |
| data store | DLI-DLET [D] | `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:310` |
| data store | DLI-GNP [R] | `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:255` |
| data store | DLI-GN [R] | `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:223` |
| DL/I GN | PAUTSUM0 | `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:223-226` |
| DL/I GNP | PAUTDTL1 | `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:255-258` |
| DL/I DLET | PAUTDTL1 | `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:310-313` |
| DL/I DLET | PAUTSUM0 | `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:335-338` |
| DL/I CHKP |  | `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:355-356` |

## CBSTM03A

Page: [CBSTM03A](../../01-detailed-documentation/application-documentation/07-programs/CBSTM03A.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | job [CREASTMT](../../01-detailed-documentation/application-documentation/06-batch/jobs/CREASTMT.md) step STEP040 | `app/jcl/CREASTMT.JCL:79` |
| calls/transfers to | CBSTM03B (CALL-static) | `app/cbl/CBSTM03A.CBL:351` |
| calls/transfers to | CBSTM03B (CALL-static) | `app/cbl/CBSTM03A.CBL:377` |
| calls/transfers to | CBSTM03B (CALL-static) | `app/cbl/CBSTM03A.CBL:401` |
| calls/transfers to | CBSTM03B (CALL-static) | `app/cbl/CBSTM03A.CBL:734` |
| calls/transfers to | CBSTM03B (CALL-static) | `app/cbl/CBSTM03A.CBL:746` |
| calls/transfers to | CBSTM03B (CALL-static) | `app/cbl/CBSTM03A.CBL:769` |
| calls/transfers to | CBSTM03B (CALL-static) | `app/cbl/CBSTM03A.CBL:787` |
| calls/transfers to | CBSTM03B (CALL-static) | `app/cbl/CBSTM03A.CBL:805` |
| calls/transfers to | CBSTM03B (CALL-static) | `app/cbl/CBSTM03A.CBL:835` |
| calls/transfers to | CBSTM03B (CALL-static) | `app/cbl/CBSTM03A.CBL:860` |
| calls/transfers to | CBSTM03B (CALL-static) | `app/cbl/CBSTM03A.CBL:877` |
| calls/transfers to | CBSTM03B (CALL-static) | `app/cbl/CBSTM03A.CBL:893` |
| calls/transfers to | CBSTM03B (CALL-static) | `app/cbl/CBSTM03A.CBL:909` |
| calls/transfers to | CEE3ABD (CALL-static) | `app/cbl/CBSTM03A.CBL:923` |
| copies | COSTM01 | `app/cbl/CBSTM03A.CBL:51` |
| copies | CVACT03Y | `app/cbl/CBSTM03A.CBL:53` |
| copies | CUSTREC | `app/cbl/CBSTM03A.CBL:55` |
| copies | CVACT01Y | `app/cbl/CBSTM03A.CBL:57` |
| data store | HTML-FILE [C] | `app/cbl/CBSTM03A.CBL:440-721` |
| data store | STMT-FILE [C] | `app/cbl/CBSTM03A.CBL:293` |

## CBSTM03B

Page: [CBSTM03B](../../01-detailed-documentation/application-documentation/07-programs/CBSTM03B.md).

| Relation | Target | Evidence |
|---|---|---|
| called/transferred by | CBSTM03A (CALL-static) | `app/cbl/CBSTM03A.CBL:351` |
| called/transferred by | CBSTM03A (CALL-static) | `app/cbl/CBSTM03A.CBL:377` |
| called/transferred by | CBSTM03A (CALL-static) | `app/cbl/CBSTM03A.CBL:401` |
| called/transferred by | CBSTM03A (CALL-static) | `app/cbl/CBSTM03A.CBL:734` |
| called/transferred by | CBSTM03A (CALL-static) | `app/cbl/CBSTM03A.CBL:746` |
| called/transferred by | CBSTM03A (CALL-static) | `app/cbl/CBSTM03A.CBL:769` |
| called/transferred by | CBSTM03A (CALL-static) | `app/cbl/CBSTM03A.CBL:787` |
| called/transferred by | CBSTM03A (CALL-static) | `app/cbl/CBSTM03A.CBL:805` |
| called/transferred by | CBSTM03A (CALL-static) | `app/cbl/CBSTM03A.CBL:835` |
| called/transferred by | CBSTM03A (CALL-static) | `app/cbl/CBSTM03A.CBL:860` |
| called/transferred by | CBSTM03A (CALL-static) | `app/cbl/CBSTM03A.CBL:877` |
| called/transferred by | CBSTM03A (CALL-static) | `app/cbl/CBSTM03A.CBL:893` |
| called/transferred by | CBSTM03A (CALL-static) | `app/cbl/CBSTM03A.CBL:909` |
| data store | ACCT-FILE [R] | `app/cbl/CBSTM03B.CBL:209-215` |
| data store | XREF-FILE [R] | `app/cbl/CBSTM03B.CBL:160-165` |
| data store | CUST-FILE [R] | `app/cbl/CBSTM03B.CBL:184-190` |
| data store | TRNX-FILE [R] | `app/cbl/CBSTM03B.CBL:136-141` |

## CBTRN01C

Page: [CBTRN01C](../../01-detailed-documentation/application-documentation/07-programs/CBTRN01C.md).

| Relation | Target | Evidence |
|---|---|---|
| calls/transfers to | CEE3ABD (CALL-static) | `app/cbl/CBTRN01C.cbl:473` |
| copies | CVTRA06Y | `app/cbl/CBTRN01C.cbl:99` |
| copies | CVCUS01Y | `app/cbl/CBTRN01C.cbl:104` |
| copies | CVACT03Y | `app/cbl/CBTRN01C.cbl:109` |
| copies | CVACT02Y | `app/cbl/CBTRN01C.cbl:114` |
| copies | CVACT01Y | `app/cbl/CBTRN01C.cbl:119` |
| copies | CVTRA05Y | `app/cbl/CBTRN01C.cbl:124` |
| data store | TRANSACT-FILE [R] | `app/cbl/CBTRN01C.cbl:345` |
| data store | XREF-FILE [R] | `app/cbl/CBTRN01C.cbl:229-291` |
| data store | CARD-FILE [R] | `app/cbl/CBTRN01C.cbl:309` |
| data store | ACCOUNT-FILE [R] | `app/cbl/CBTRN01C.cbl:243-327` |
| data store | CUSTOMER-FILE [R] | `app/cbl/CBTRN01C.cbl:273` |
| data store | DALYTRAN-FILE [R] | `app/cbl/CBTRN01C.cbl:203-254` |

## CBTRN02C

Page: [CBTRN02C](../../01-detailed-documentation/application-documentation/07-programs/CBTRN02C.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | job [POSTTRAN](../../01-detailed-documentation/application-documentation/06-batch/jobs/POSTTRAN.md) step STEP15 | `app/jcl/POSTTRAN.jcl:23` |
| calls/transfers to | CEE3ABD (CALL-static) | `app/cbl/CBTRN02C.cbl:711` |
| copies | CVTRA06Y | `app/cbl/CBTRN02C.cbl:102` |
| copies | CVTRA05Y | `app/cbl/CBTRN02C.cbl:107` |
| copies | CVACT03Y | `app/cbl/CBTRN02C.cbl:112` |
| copies | CVACT01Y | `app/cbl/CBTRN02C.cbl:121` |
| copies | CVTRA01Y | `app/cbl/CBTRN02C.cbl:126` |
| data store | TRANSACT-FILE [C] | `app/cbl/CBTRN02C.cbl:256` |
| data store | DALYREJS-FILE [C] | `app/cbl/CBTRN02C.cbl:293` |
| data store | XREF-FILE [R] | `app/cbl/CBTRN02C.cbl:275-383` |
| data store | ACCOUNT-FILE [R, U] | `app/cbl/CBTRN02C.cbl:311-395` |
| data store | TCATBAL-FILE [C, R, U] | `app/cbl/CBTRN02C.cbl:329-474` |
| data store | DALYTRAN-FILE [R] | `app/cbl/CBTRN02C.cbl:238-346` |

## CBTRN03C

Page: [CBTRN03C](../../01-detailed-documentation/application-documentation/07-programs/CBTRN03C.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | job [TRANREPT](../../01-detailed-documentation/application-documentation/06-batch/jobs/TRANREPT.md) step STEP10R | `app/jcl/TRANREPT.jcl:59` |
| calls/transfers to | CEE3ABD (CALL-static) | `app/cbl/CBTRN03C.cbl:630` |
| copies | CVTRA05Y | `app/cbl/CBTRN03C.cbl:93` |
| copies | CVACT03Y | `app/cbl/CBTRN03C.cbl:98` |
| copies | CVTRA03Y | `app/cbl/CBTRN03C.cbl:103` |
| copies | CVTRA04Y | `app/cbl/CBTRN03C.cbl:108` |
| copies | CVTRA07Y | `app/cbl/CBTRN03C.cbl:113` |
| data store | TRANSACT-FILE [R] | `app/cbl/CBTRN03C.cbl:249-378` |
| data store | XREF-FILE [R] | `app/cbl/CBTRN03C.cbl:414-485` |
| data store | TRANCATG-FILE [R] | `app/cbl/CBTRN03C.cbl:450-505` |
| data store | REPORT-FILE [C] | `app/cbl/CBTRN03C.cbl:345` |
| data store | DATE-PARMS-FILE [R] | `app/cbl/CBTRN03C.cbl:221-468` |
| data store | TRANTYPE-FILE [R] | `app/cbl/CBTRN03C.cbl:432-495` |

## COACCT01

Page: [COACCT01](../../01-detailed-documentation/application-documentation/07-programs/COACCT01.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | CICS transaction CDRA | `app/app-vsam-mq/csd/CRDDEMOM.csd:17-26` |
| calls/transfers to | MQOPEN (CALL-static) | `app/app-vsam-mq/cbl/COACCT01.cbl:233` |
| calls/transfers to | MQOPEN (CALL-static) | `app/app-vsam-mq/cbl/COACCT01.cbl:267` |
| calls/transfers to | MQOPEN (CALL-static) | `app/app-vsam-mq/cbl/COACCT01.cbl:302` |
| calls/transfers to | MQGET (CALL-static) | `app/app-vsam-mq/cbl/COACCT01.cbl:352` |
| calls/transfers to | MQPUT (CALL-static) | `app/app-vsam-mq/cbl/COACCT01.cbl:479` |
| calls/transfers to | MQPUT (CALL-static) | `app/app-vsam-mq/cbl/COACCT01.cbl:516` |
| calls/transfers to | MQCLOSE (CALL-static) | `app/app-vsam-mq/cbl/COACCT01.cbl:557` |
| calls/transfers to | MQCLOSE (CALL-static) | `app/app-vsam-mq/cbl/COACCT01.cbl:579` |
| calls/transfers to | MQCLOSE (CALL-static) | `app/app-vsam-mq/cbl/COACCT01.cbl:602` |
| copies | CMQGMOV (system) | `app/app-vsam-mq/cbl/COACCT01.cbl:71` |
| copies | CMQPMOV (system) | `app/app-vsam-mq/cbl/COACCT01.cbl:75` |
| copies | CMQMDV (system) | `app/app-vsam-mq/cbl/COACCT01.cbl:79` |
| copies | CMQODV (system) | `app/app-vsam-mq/cbl/COACCT01.cbl:83` |
| copies | CMQV (system) | `app/app-vsam-mq/cbl/COACCT01.cbl:87` |
| copies | CMQTML (system) | `app/app-vsam-mq/cbl/COACCT01.cbl:90` |
| copies | CVACT01Y | `app/app-vsam-mq/cbl/COACCT01.cbl:171` |
| data store | ACCTDAT [R] | `app/app-vsam-mq/cbl/COACCT01.cbl:396` |
| data store | MQ-GET [R] | `app/app-vsam-mq/cbl/COACCT01.cbl:352` |
| data store | MQ-PUT [C] | `app/app-vsam-mq/cbl/COACCT01.cbl:479` |

## COACTUPC

Page: [COACTUPC](../../01-detailed-documentation/application-documentation/07-programs/COACTUPC.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | CICS transaction CAUP | `app/csd/CARDDEMO.CSD:306-316` |
| called/transferred by | COMEN01C (XCTL) | `app/cbl/COMEN01C.cbl:185` |
| calls/transfers to | COMEN01C (XCTL) | `app/cbl/COACTUPC.cbl:956` |
| calls/transfers to | CAUP (RETURN-TRANSID) | `app/cbl/COACTUPC.cbl:1015` |
| copies | CSUTLDWY | `app/cbl/COACTUPC.cbl:166` |
| copies | CVCRD01Y | `app/cbl/COACTUPC.cbl:597` |
| copies | CSLKPCDY | `app/cbl/COACTUPC.cbl:602` |
| copies | DFHBMSCA (system) | `app/cbl/COACTUPC.cbl:615` |
| copies | DFHAID (system) | `app/cbl/COACTUPC.cbl:616` |
| copies | COTTL01Y | `app/cbl/COACTUPC.cbl:620` |
| copies | COACTUP | `app/cbl/COACTUPC.cbl:623` |
| copies | CSDAT01Y | `app/cbl/COACTUPC.cbl:626` |
| copies | CSMSG01Y | `app/cbl/COACTUPC.cbl:629` |
| copies | CSMSG02Y | `app/cbl/COACTUPC.cbl:632` |
| copies | CSUSR01Y | `app/cbl/COACTUPC.cbl:635` |
| copies | CVACT01Y | `app/cbl/COACTUPC.cbl:640` |
| copies | CVACT03Y | `app/cbl/COACTUPC.cbl:643` |
| copies | CVCUS01Y | `app/cbl/COACTUPC.cbl:646` |
| copies | COCOM01Y | `app/cbl/COACTUPC.cbl:650` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3208-3211` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3214-3217` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3220-3223` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3226-3229` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3232-3235` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3238-3241` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3244-3247` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3250-3253` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3256-3259` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3262-3265` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3268-3271` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3274-3277` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3280-3283` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3286-3289` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3292-3295` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3298-3301` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3304-3307` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3310-3313` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3316-3319` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3322-3325` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3328-3331` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3334-3337` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3340-3343` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3346-3349` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3352-3355` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3358-3361` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3364-3367` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3370-3373` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3376-3379` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3382-3385` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3388-3391` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3394-3397` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3400-3403` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3405-3408` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3411-3414` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3417-3420` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3422-3425` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3427-3430` |
| copies | CSSETATY | `app/cbl/COACTUPC.cbl:3432-3435` |
| copies | CSSTRPFY | `app/cbl/COACTUPC.cbl:4199` |
| copies | CSUTLDPY | `app/cbl/COACTUPC.cbl:4232` |

## COACTVWC

Page: [COACTVWC](../../01-detailed-documentation/application-documentation/07-programs/COACTVWC.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | CICS transaction CAVW | `app/csd/CARDDEMO.CSD:317-326` |
| called/transferred by | COMEN01C (XCTL) | `app/cbl/COMEN01C.cbl:185` |
| calls/transfers to | COMEN01C (XCTL) | `app/cbl/COACTVWC.cbl:349` |
| calls/transfers to | CAVW (RETURN-TRANSID) | `app/cbl/COACTVWC.cbl:402` |
| copies | CVCRD01Y | `app/cbl/COACTVWC.cbl:207` |
| copies | COCOM01Y | `app/cbl/COACTVWC.cbl:211` |
| copies | DFHBMSCA (system) | `app/cbl/COACTVWC.cbl:221` |
| copies | DFHAID (system) | `app/cbl/COACTVWC.cbl:222` |
| copies | COTTL01Y | `app/cbl/COACTVWC.cbl:226` |
| copies | COACTVW | `app/cbl/COACTVWC.cbl:229` |
| copies | CSDAT01Y | `app/cbl/COACTVWC.cbl:232` |
| copies | CSMSG01Y | `app/cbl/COACTVWC.cbl:235` |
| copies | CSMSG02Y | `app/cbl/COACTVWC.cbl:238` |
| copies | CSUSR01Y | `app/cbl/COACTVWC.cbl:241` |
| copies | CVACT01Y | `app/cbl/COACTVWC.cbl:244` |
| copies | CVACT02Y | `app/cbl/COACTVWC.cbl:248` |
| copies | CVACT03Y | `app/cbl/COACTVWC.cbl:251` |
| copies | CVCUS01Y | `app/cbl/COACTVWC.cbl:254` |
| copies | CSSTRPFY | `app/cbl/COACTVWC.cbl:913` |

## COADM01C

Page: [COADM01C](../../01-detailed-documentation/application-documentation/07-programs/COADM01C.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | CICS transaction CA00 | `app/csd/CARDDEMO.CSD:327-336` |
| called/transferred by | COSGN00C (XCTL) | `app/cbl/COSGN00C.cbl:231` |
| called/transferred by | COTRTLIC (XCTL) | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:620` |
| called/transferred by | COTRTUPC (XCTL) | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:457` |
| called/transferred by | COUSR00C (XCTL) | `app/cbl/COUSR00C.cbl:514` |
| called/transferred by | COUSR01C (XCTL) | `app/cbl/COUSR01C.cbl:175` |
| called/transferred by | COUSR02C (XCTL) | `app/cbl/COUSR02C.cbl:258` |
| called/transferred by | COUSR03C (XCTL) | `app/cbl/COUSR03C.cbl:205` |
| calls/transfers to | CA00 (RETURN-TRANSID) | `app/cbl/COADM01C.cbl:111` |
| calls/transfers to | COSGN00C (XCTL) | `app/cbl/COADM01C.cbl:168` |
| calls/transfers to | CA00 (RETURN-TRANSID) | `app/cbl/COADM01C.cbl:280` |
| calls/transfers to | COUSR00C (XCTL) | `app/cbl/COADM01C.cbl:146` |
| calls/transfers to | COUSR01C (XCTL) | `app/cbl/COADM01C.cbl:146` |
| calls/transfers to | COUSR02C (XCTL) | `app/cbl/COADM01C.cbl:146` |
| calls/transfers to | COUSR03C (XCTL) | `app/cbl/COADM01C.cbl:146` |
| calls/transfers to | COTRTLIC (XCTL) | `app/cbl/COADM01C.cbl:146` |
| calls/transfers to | COTRTUPC (XCTL) | `app/cbl/COADM01C.cbl:146` |
| calls/transfers to | COSGN00C (XCTL) | `app/cbl/COADM01C.cbl:166` |
| copies | COCOM01Y | `app/cbl/COADM01C.cbl:50` |
| copies | COADM02Y | `app/cbl/COADM01C.cbl:51` |
| copies | COADM01 | `app/cbl/COADM01C.cbl:53` |
| copies | COTTL01Y | `app/cbl/COADM01C.cbl:55` |
| copies | CSDAT01Y | `app/cbl/COADM01C.cbl:56` |
| copies | CSMSG01Y | `app/cbl/COADM01C.cbl:57` |
| copies | CSUSR01Y | `app/cbl/COADM01C.cbl:58` |
| copies | DFHAID (system) | `app/cbl/COADM01C.cbl:60` |
| copies | DFHBMSCA (system) | `app/cbl/COADM01C.cbl:61` |

## COBIL00C

Page: [COBIL00C](../../01-detailed-documentation/application-documentation/07-programs/COBIL00C.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | CICS transaction CB00 | `app/csd/CARDDEMO.CSD:337-346` |
| called/transferred by | COMEN01C (XCTL) | `app/cbl/COMEN01C.cbl:185` |
| calls/transfers to | CB00 (RETURN-TRANSID) | `app/cbl/COBIL00C.cbl:146` |
| calls/transfers to | COMEN01C, COSGN00C (XCTL) | `app/cbl/COBIL00C.cbl:281` |
| copies | COCOM01Y | `app/cbl/COBIL00C.cbl:63` |
| copies | COBIL00 | `app/cbl/COBIL00C.cbl:74` |
| copies | COTTL01Y | `app/cbl/COBIL00C.cbl:76` |
| copies | CSDAT01Y | `app/cbl/COBIL00C.cbl:77` |
| copies | CSMSG01Y | `app/cbl/COBIL00C.cbl:78` |
| copies | CVACT01Y | `app/cbl/COBIL00C.cbl:80` |
| copies | CVACT03Y | `app/cbl/COBIL00C.cbl:81` |
| copies | CVTRA05Y | `app/cbl/COBIL00C.cbl:82` |
| copies | DFHAID (system) | `app/cbl/COBIL00C.cbl:84` |
| copies | DFHBMSCA (system) | `app/cbl/COBIL00C.cbl:85` |
| data store | TRANSACT [B, C] | `app/cbl/COBIL00C.cbl:443-512` |
| data store | ACCTDAT [R, U] | `app/cbl/COBIL00C.cbl:345-379` |
| data store | CXACAIX [R] | `app/cbl/COBIL00C.cbl:410` |

## COBSWAIT

Page: [COBSWAIT](../../01-detailed-documentation/application-documentation/07-programs/COBSWAIT.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | job [WAITSTEP](../../01-detailed-documentation/application-documentation/06-batch/jobs/WAITSTEP.md) step WAIT | `app/jcl/WAITSTEP.jcl:22` |
| calls/transfers to | MVSWAIT (CALL-static) | `app/cbl/COBSWAIT.cbl:38` |

## COBTUPDT

Page: [COBTUPDT](../../01-detailed-documentation/application-documentation/07-programs/COBTUPDT.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | job [MNTTRDB2](../../01-detailed-documentation/application-documentation/06-batch/jobs/MNTTRDB2.md) step STEP1 | `app/app-transaction-type-db2/jcl/MNTTRDB2.jcl:21` |
| copies | SQLCA (system) | `app/app-transaction-type-db2/cbl/COBTUPDT.cbl:50-52` |
| copies | DCLTRTYP | `app/app-transaction-type-db2/cbl/COBTUPDT.cbl:54` |
| data store | CARDDEMO.TRANSACTION_TYPE [C, D, U] | `app/app-transaction-type-db2/cbl/COBTUPDT.cbl:137` |
| SQL INSERT | CARDDEMO.TRANSACTION_TYPE | `app/app-transaction-type-db2/cbl/COBTUPDT.cbl:137-148` |
| SQL UPDATE | CARDDEMO.TRANSACTION_TYPE | `app/app-transaction-type-db2/cbl/COBTUPDT.cbl:171-175` |
| SQL DELETE | CARDDEMO.TRANSACTION_TYPE | `app/app-transaction-type-db2/cbl/COBTUPDT.cbl:201-204` |

## COCRDLIC

Page: [COCRDLIC](../../01-detailed-documentation/application-documentation/07-programs/COCRDLIC.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | CICS transaction CCLI | `app/csd/CARDDEMO.CSD:357-366` |
| called/transferred by | COCRDSLC (XCTL) | `app/cbl/COCRDSLC.cbl:331` |
| called/transferred by | COCRDUPC (XCTL) | `app/cbl/COCRDUPC.cbl:473` |
| called/transferred by | COMEN01C (XCTL) | `app/cbl/COMEN01C.cbl:185` |
| calls/transfers to | COMEN01C (XCTL) | `app/cbl/COCRDLIC.cbl:402` |
| calls/transfers to | COCRDSLC (XCTL) | `app/cbl/COCRDLIC.cbl:538` |
| calls/transfers to | COCRDUPC (XCTL) | `app/cbl/COCRDLIC.cbl:566` |
| calls/transfers to | CCLI (RETURN-TRANSID) | `app/cbl/COCRDLIC.cbl:615` |
| copies | CVCRD01Y | `app/cbl/COCRDLIC.cbl:221` |
| copies | COCOM01Y | `app/cbl/COCRDLIC.cbl:227` |
| copies | DFHBMSCA (system) | `app/cbl/COCRDLIC.cbl:267` |
| copies | DFHAID (system) | `app/cbl/COCRDLIC.cbl:268` |
| copies | COTTL01Y | `app/cbl/COCRDLIC.cbl:272` |
| copies | COCRDLI | `app/cbl/COCRDLIC.cbl:276` |
| copies | CSDAT01Y | `app/cbl/COCRDLIC.cbl:279` |
| copies | CSMSG01Y | `app/cbl/COCRDLIC.cbl:281` |
| copies | CSUSR01Y | `app/cbl/COCRDLIC.cbl:285` |
| copies | CVACT02Y | `app/cbl/COCRDLIC.cbl:290` |
| copies | CSSTRPFY | `app/cbl/COCRDLIC.cbl:1416` |

## COCRDSLC

Page: [COCRDSLC](../../01-detailed-documentation/application-documentation/07-programs/COCRDSLC.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | CICS transaction CCDL | `app/csd/CARDDEMO.CSD:347-356` |
| called/transferred by | COCRDLIC (XCTL) | `app/cbl/COCRDLIC.cbl:538` |
| called/transferred by | COMEN01C (XCTL) | `app/cbl/COMEN01C.cbl:185` |
| calls/transfers to | COCRDLIC, COMEN01C (XCTL) | `app/cbl/COCRDSLC.cbl:331` |
| calls/transfers to | CCDL (RETURN-TRANSID) | `app/cbl/COCRDSLC.cbl:402` |
| copies | CVCRD01Y | `app/cbl/COCRDSLC.cbl:194` |
| copies | COCOM01Y | `app/cbl/COCRDSLC.cbl:198` |
| copies | DFHBMSCA (system) | `app/cbl/COCRDSLC.cbl:208` |
| copies | DFHAID (system) | `app/cbl/COCRDSLC.cbl:209` |
| copies | COTTL01Y | `app/cbl/COCRDSLC.cbl:213` |
| copies | COCRDSL | `app/cbl/COCRDSLC.cbl:215` |
| copies | CSDAT01Y | `app/cbl/COCRDSLC.cbl:218` |
| copies | CSMSG01Y | `app/cbl/COCRDSLC.cbl:221` |
| copies | CSMSG02Y | `app/cbl/COCRDSLC.cbl:224` |
| copies | CSUSR01Y | `app/cbl/COCRDSLC.cbl:227` |
| copies | CVACT02Y | `app/cbl/COCRDSLC.cbl:234` |
| copies | CVCUS01Y | `app/cbl/COCRDSLC.cbl:240` |
| copies | CSSTRPFY | `app/cbl/COCRDSLC.cbl:855` |

## COCRDUPC

Page: [COCRDUPC](../../01-detailed-documentation/application-documentation/07-programs/COCRDUPC.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | CICS transaction CCUP | `app/csd/CARDDEMO.CSD:367-377` |
| called/transferred by | COCRDLIC (XCTL) | `app/cbl/COCRDLIC.cbl:566` |
| called/transferred by | COMEN01C (XCTL) | `app/cbl/COMEN01C.cbl:185` |
| calls/transfers to | COCRDLIC, COMEN01C (XCTL) | `app/cbl/COCRDUPC.cbl:473` |
| calls/transfers to | CCUP (RETURN-TRANSID) | `app/cbl/COCRDUPC.cbl:554` |
| copies | CVCRD01Y | `app/cbl/COCRDUPC.cbl:268` |
| copies | COCOM01Y | `app/cbl/COCRDUPC.cbl:272` |
| copies | DFHBMSCA (system) | `app/cbl/COCRDUPC.cbl:327` |
| copies | DFHAID (system) | `app/cbl/COCRDUPC.cbl:328` |
| copies | COTTL01Y | `app/cbl/COCRDUPC.cbl:332` |
| copies | COCRDUP | `app/cbl/COCRDUPC.cbl:334` |
| copies | CSDAT01Y | `app/cbl/COCRDUPC.cbl:337` |
| copies | CSMSG01Y | `app/cbl/COCRDUPC.cbl:340` |
| copies | CSMSG02Y | `app/cbl/COCRDUPC.cbl:343` |
| copies | CSUSR01Y | `app/cbl/COCRDUPC.cbl:346` |
| copies | CVACT02Y | `app/cbl/COCRDUPC.cbl:353` |
| copies | CVCUS01Y | `app/cbl/COCRDUPC.cbl:359` |
| copies | CSSTRPFY | `app/cbl/COCRDUPC.cbl:1528` |

## CODATE01

Page: [CODATE01](../../01-detailed-documentation/application-documentation/07-programs/CODATE01.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | CICS transaction CDRD | `app/app-vsam-mq/csd/CRDDEMOM.csd:27-36` |
| calls/transfers to | MQOPEN (CALL-static) | `app/app-vsam-mq/cbl/CODATE01.cbl:182` |
| calls/transfers to | MQOPEN (CALL-static) | `app/app-vsam-mq/cbl/CODATE01.cbl:216` |
| calls/transfers to | MQOPEN (CALL-static) | `app/app-vsam-mq/cbl/CODATE01.cbl:251` |
| calls/transfers to | MQGET (CALL-static) | `app/app-vsam-mq/cbl/CODATE01.cbl:301` |
| calls/transfers to | MQPUT (CALL-static) | `app/app-vsam-mq/cbl/CODATE01.cbl:383` |
| calls/transfers to | MQPUT (CALL-static) | `app/app-vsam-mq/cbl/CODATE01.cbl:420` |
| calls/transfers to | MQCLOSE (CALL-static) | `app/app-vsam-mq/cbl/CODATE01.cbl:461` |
| calls/transfers to | MQCLOSE (CALL-static) | `app/app-vsam-mq/cbl/CODATE01.cbl:483` |
| calls/transfers to | MQCLOSE (CALL-static) | `app/app-vsam-mq/cbl/CODATE01.cbl:506` |
| copies | CMQGMOV (system) | `app/app-vsam-mq/cbl/CODATE01.cbl:71` |
| copies | CMQPMOV (system) | `app/app-vsam-mq/cbl/CODATE01.cbl:75` |
| copies | CMQMDV (system) | `app/app-vsam-mq/cbl/CODATE01.cbl:79` |
| copies | CMQODV (system) | `app/app-vsam-mq/cbl/CODATE01.cbl:83` |
| copies | CMQV (system) | `app/app-vsam-mq/cbl/CODATE01.cbl:87` |
| copies | CMQTML (system) | `app/app-vsam-mq/cbl/CODATE01.cbl:90` |
| data store | MQ-GET [R] | `app/app-vsam-mq/cbl/CODATE01.cbl:301` |
| data store | MQ-PUT [C] | `app/app-vsam-mq/cbl/CODATE01.cbl:383` |

## COMEN01C

Page: [COMEN01C](../../01-detailed-documentation/application-documentation/07-programs/COMEN01C.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | CICS transaction CM00 | `app/csd/CARDDEMO.CSD:399-408` |
| called/transferred by | COACTUPC (XCTL) | `app/cbl/COACTUPC.cbl:956` |
| called/transferred by | COACTVWC (XCTL) | `app/cbl/COACTVWC.cbl:349` |
| called/transferred by | COBIL00C (XCTL) | `app/cbl/COBIL00C.cbl:281` |
| called/transferred by | COCRDLIC (XCTL) | `app/cbl/COCRDLIC.cbl:402` |
| called/transferred by | COCRDSLC (XCTL) | `app/cbl/COCRDSLC.cbl:331` |
| called/transferred by | COCRDUPC (XCTL) | `app/cbl/COCRDUPC.cbl:473` |
| called/transferred by | COPAUS0C (XCTL) | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:674` |
| called/transferred by | CORPT00C (XCTL) | `app/cbl/CORPT00C.cbl:548` |
| called/transferred by | COSGN00C (XCTL) | `app/cbl/COSGN00C.cbl:236` |
| called/transferred by | COTRN00C (XCTL) | `app/cbl/COTRN00C.cbl:518` |
| called/transferred by | COTRN01C (XCTL) | `app/cbl/COTRN01C.cbl:205` |
| called/transferred by | COTRN02C (XCTL) | `app/cbl/COTRN02C.cbl:508` |
| calls/transfers to | CM00 (RETURN-TRANSID) | `app/cbl/COMEN01C.cbl:107` |
| calls/transfers to | COSGN00C (XCTL) | `app/cbl/COMEN01C.cbl:201` |
| calls/transfers to | COACTVWC (XCTL) | `app/cbl/COMEN01C.cbl:185` |
| calls/transfers to | COACTUPC (XCTL) | `app/cbl/COMEN01C.cbl:185` |
| calls/transfers to | COCRDLIC (XCTL) | `app/cbl/COMEN01C.cbl:185` |
| calls/transfers to | COCRDSLC (XCTL) | `app/cbl/COMEN01C.cbl:185` |
| calls/transfers to | COCRDUPC (XCTL) | `app/cbl/COMEN01C.cbl:185` |
| calls/transfers to | COTRN00C (XCTL) | `app/cbl/COMEN01C.cbl:185` |
| calls/transfers to | COTRN01C (XCTL) | `app/cbl/COMEN01C.cbl:185` |
| calls/transfers to | COTRN02C (XCTL) | `app/cbl/COMEN01C.cbl:185` |
| calls/transfers to | CORPT00C (XCTL) | `app/cbl/COMEN01C.cbl:185` |
| calls/transfers to | COBIL00C (XCTL) | `app/cbl/COMEN01C.cbl:185` |
| calls/transfers to | COPAUS0C (XCTL) | `app/cbl/COMEN01C.cbl:185` |
| calls/transfers to | COSGN00C (XCTL) | `app/cbl/COMEN01C.cbl:199` |
| copies | COCOM01Y | `app/cbl/COMEN01C.cbl:50` |
| copies | COMEN02Y | `app/cbl/COMEN01C.cbl:51` |
| copies | COMEN01 | `app/cbl/COMEN01C.cbl:53` |
| copies | COTTL01Y | `app/cbl/COMEN01C.cbl:55` |
| copies | CSDAT01Y | `app/cbl/COMEN01C.cbl:56` |
| copies | CSMSG01Y | `app/cbl/COMEN01C.cbl:57` |
| copies | CSUSR01Y | `app/cbl/COMEN01C.cbl:58` |
| copies | DFHAID (system) | `app/cbl/COMEN01C.cbl:60` |
| copies | DFHBMSCA (system) | `app/cbl/COMEN01C.cbl:61` |

## COPAUA0C

Page: [COPAUA0C](../../01-detailed-documentation/application-documentation/07-programs/COPAUA0C.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | CICS transaction CP00 | `app/app-authorization-ims-db2-mq/csd/CRDDEMO2.csd:59-68` |
| calls/transfers to | MQOPEN (CALL-static) | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:262` |
| calls/transfers to | MQGET (CALL-static) | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:400` |
| calls/transfers to | MQPUT1 (CALL-static) | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:758` |
| calls/transfers to | MQCLOSE (CALL-static) | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:956` |
| copies | CMQODV (system) | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:149` |
| copies | CMQMDV (system) | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:152` |
| copies | CMQODV (system) | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:155` |
| copies | CMQMDV (system) | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:158` |
| copies | CMQV (system) | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:161` |
| copies | CMQTML (system) | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:164` |
| copies | CMQPMOV (system) | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:167` |
| copies | CMQGMOV (system) | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:170` |
| copies | CCPAURQY | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:178` |
| copies | CCPAURLY | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:182` |
| copies | CCPAUERY | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:185` |
| copies | CIPAUSMY | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:193` |
| copies | CIPAUDTY | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:197` |
| copies | CVACT03Y | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:203` |
| copies | CVACT01Y | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:206` |
| copies | CVCUS01Y | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:209` |
| data store | MQ-GET [R] | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:400` |
| data store | CCXREF [R] | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:477` |
| data store | DLI-REPL [U] | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:825` |
| data store | CUSTDAT [R] | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:573` |
| data store | DLI-ISRT [C] | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:830` |
| data store | MQ-PUT [C] | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:758` |
| data store | ACCTDAT [R] | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:525` |
| data store | DLI-GU [R] | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:620` |
| data store | CSSL [C] | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:1001` |
| DL/I SCHD |  | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:293-296` |
| DL/I TERM |  | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:299-300` |
| DL/I SCHD |  | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:302-305` |
| DL/I GU | PAUTSUM0 | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:620-624` |
| DL/I REPL | PAUTSUM0 | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:825-828` |
| DL/I ISRT | PAUTSUM0 | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:830-833` |
| DL/I ISRT | PAUTSUM0, PAUTDTL1 | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:913-919` |
| DL/I TERM |  | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:944` |

## COPAUS0C

Page: [COPAUS0C](../../01-detailed-documentation/application-documentation/07-programs/COPAUS0C.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | CICS transaction CPVS | `app/app-authorization-ims-db2-mq/csd/CRDDEMO2.csd:49-58` |
| called/transferred by | COMEN01C (XCTL) | `app/cbl/COMEN01C.cbl:185` |
| called/transferred by | COPAUS1C (XCTL) | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:367` |
| calls/transfers to | CPVS (RETURN-TRANSID) | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:254` |
| calls/transfers to | COPAUS1C (XCTL) | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:322` |
| calls/transfers to | COMEN01C, COSGN00C (XCTL) | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:674` |
| copies | COCOM01Y | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:116` |
| copies | COPAU00 | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:129` |
| copies | COTTL01Y | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:132` |
| copies | CSDAT01Y | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:135` |
| copies | CSMSG01Y | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:138` |
| copies | CSMSG02Y | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:141` |
| copies | CVACT01Y | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:144` |
| copies | CVACT02Y | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:147` |
| copies | CVACT03Y | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:150` |
| copies | CVCUS01Y | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:153` |
| copies | CIPAUSMY | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:161` |
| copies | CIPAUDTY | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:165` |
| copies | DFHAID (system) | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:168` |
| copies | DFHBMSCA (system) | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:169` |
| data store | DLI-GU [R] | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:973` |
| data store | ACCTDAT [R] | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:869` |
| data store | DLI-GNP [R] | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:461` |
| data store | CXACAIX [R] | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:818` |
| data store | CUSTDAT [R] | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:920` |
| DL/I GNP | PAUTDTL1 | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:461-464` |
| DL/I GNP | PAUTDTL1 | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:493-497` |
| DL/I GU | PAUTSUM0 | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:973-977` |
| DL/I SCHD |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:1002-1005` |
| DL/I TERM |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:1008-1009` |
| DL/I SCHD |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:1011-1014` |

## COPAUS1C

Page: [COPAUS1C](../../01-detailed-documentation/application-documentation/07-programs/COPAUS1C.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | CICS transaction CPVD | `app/app-authorization-ims-db2-mq/csd/CRDDEMO2.csd:39-48` |
| called/transferred by | COPAUS0C (XCTL) | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:322` |
| calls/transfers to | CPVD (RETURN-TRANSID) | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:202` |
| calls/transfers to | COPAUS2C (LINK) | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:248` |
| calls/transfers to | COPAUS0C (XCTL) | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:367` |
| copies | COCOM01Y | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:109` |
| copies | COPAU01 | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:122` |
| copies | COTTL01Y | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:126` |
| copies | CSDAT01Y | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:129` |
| copies | CSMSG01Y | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:132` |
| copies | CSMSG02Y | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:135` |
| copies | CIPAUSMY | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:142` |
| copies | CIPAUDTY | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:146` |
| copies | DFHAID (system) | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:148` |
| copies | DFHBMSCA (system) | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:149` |
| data store | DLI-GNP [R] | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:465` |
| data store | DLI-GU [R] | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:439` |
| data store | DLI-REPL [U] | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:525` |
| DL/I GU | PAUTSUM0 | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:439-443` |
| DL/I GNP | PAUTDTL1 | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:465-469` |
| DL/I GNP | PAUTDTL1 | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:495-498` |
| DL/I REPL | PAUTDTL1 | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:525-528` |
| DL/I SCHD |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:575-578` |
| DL/I TERM |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:581-582` |
| DL/I SCHD |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:584-587` |

## COPAUS2C

Page: [COPAUS2C](../../01-detailed-documentation/application-documentation/07-programs/COPAUS2C.md).

| Relation | Target | Evidence |
|---|---|---|
| called/transferred by | COPAUS1C (LINK) | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:248` |
| copies | SQLCA (system) | `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:65-67` |
| copies | AUTHFRDS | `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:68-70` |
| copies | CIPAUDTY | `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:78` |
| data store | CARDDEMO.AUTHFRDS [C, U] | `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:141` |
| SQL INSERT | CARDDEMO.AUTHFRDS | `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:141-198` |
| SQL UPDATE | CARDDEMO.AUTHFRDS | `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:222-229` |

## CORPT00C

Page: [CORPT00C](../../01-detailed-documentation/application-documentation/07-programs/CORPT00C.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | CICS transaction CR00 | `app/csd/CARDDEMO.CSD:409-418` |
| called/transferred by | COMEN01C (XCTL) | `app/cbl/COMEN01C.cbl:185` |
| calls/transfers to | CR00 (RETURN-TRANSID) | `app/cbl/CORPT00C.cbl:199` |
| calls/transfers to | CSUTLDTC (CALL-static) | `app/cbl/CORPT00C.cbl:392` |
| calls/transfers to | CSUTLDTC (CALL-static) | `app/cbl/CORPT00C.cbl:412` |
| calls/transfers to | COMEN01C, COSGN00C (XCTL) | `app/cbl/CORPT00C.cbl:548` |
| calls/transfers to | CR00 (RETURN-TRANSID) | `app/cbl/CORPT00C.cbl:587` |
| copies | COCOM01Y | `app/cbl/CORPT00C.cbl:138` |
| copies | CORPT00 | `app/cbl/CORPT00C.cbl:140` |
| copies | COTTL01Y | `app/cbl/CORPT00C.cbl:142` |
| copies | CSDAT01Y | `app/cbl/CORPT00C.cbl:143` |
| copies | CSMSG01Y | `app/cbl/CORPT00C.cbl:144` |
| copies | CVTRA05Y | `app/cbl/CORPT00C.cbl:146` |
| copies | DFHAID (system) | `app/cbl/CORPT00C.cbl:148` |
| copies | DFHBMSCA (system) | `app/cbl/CORPT00C.cbl:149` |
| data store | JOBS [C] | `app/cbl/CORPT00C.cbl:517` |

## COSGN00C

Page: [COSGN00C](../../01-detailed-documentation/application-documentation/07-programs/COSGN00C.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | CICS transaction CC00 | `app/csd/CARDDEMO.CSD:378-387` |
| called/transferred by | COADM01C (XCTL) | `app/cbl/COADM01C.cbl:168` |
| called/transferred by | COADM01C (XCTL) | `app/cbl/COADM01C.cbl:166` |
| called/transferred by | COBIL00C (XCTL) | `app/cbl/COBIL00C.cbl:281` |
| called/transferred by | COMEN01C (XCTL) | `app/cbl/COMEN01C.cbl:201` |
| called/transferred by | COMEN01C (XCTL) | `app/cbl/COMEN01C.cbl:199` |
| called/transferred by | COPAUS0C (XCTL) | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:674` |
| called/transferred by | CORPT00C (XCTL) | `app/cbl/CORPT00C.cbl:548` |
| called/transferred by | COTRN00C (XCTL) | `app/cbl/COTRN00C.cbl:518` |
| called/transferred by | COTRN01C (XCTL) | `app/cbl/COTRN01C.cbl:205` |
| called/transferred by | COTRN02C (XCTL) | `app/cbl/COTRN02C.cbl:508` |
| called/transferred by | COUSR00C (XCTL) | `app/cbl/COUSR00C.cbl:514` |
| called/transferred by | COUSR01C (XCTL) | `app/cbl/COUSR01C.cbl:175` |
| called/transferred by | COUSR02C (XCTL) | `app/cbl/COUSR02C.cbl:258` |
| called/transferred by | COUSR03C (XCTL) | `app/cbl/COUSR03C.cbl:205` |
| calls/transfers to | CC00 (RETURN-TRANSID) | `app/cbl/COSGN00C.cbl:98` |
| calls/transfers to | COADM01C (XCTL) | `app/cbl/COSGN00C.cbl:231` |
| calls/transfers to | COMEN01C (XCTL) | `app/cbl/COSGN00C.cbl:236` |
| copies | COCOM01Y | `app/cbl/COSGN00C.cbl:48` |
| copies | COSGN00 | `app/cbl/COSGN00C.cbl:50` |
| copies | COTTL01Y | `app/cbl/COSGN00C.cbl:52` |
| copies | CSDAT01Y | `app/cbl/COSGN00C.cbl:53` |
| copies | CSMSG01Y | `app/cbl/COSGN00C.cbl:54` |
| copies | CSUSR01Y | `app/cbl/COSGN00C.cbl:55` |
| copies | DFHAID (system) | `app/cbl/COSGN00C.cbl:57` |
| copies | DFHBMSCA (system) | `app/cbl/COSGN00C.cbl:58` |
| data store | USRSEC [R] | `app/cbl/COSGN00C.cbl:211` |

## COTRN00C

Page: [COTRN00C](../../01-detailed-documentation/application-documentation/07-programs/COTRN00C.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | CICS transaction CT00 | `app/csd/CARDDEMO.CSD:419-428` |
| called/transferred by | COMEN01C (XCTL) | `app/cbl/COMEN01C.cbl:185` |
| called/transferred by | COTRN01C (XCTL) | `app/cbl/COTRN01C.cbl:205` |
| calls/transfers to | CT00 (RETURN-TRANSID) | `app/cbl/COTRN00C.cbl:138` |
| calls/transfers to | COTRN01C (XCTL) | `app/cbl/COTRN00C.cbl:192` |
| calls/transfers to | COMEN01C, COSGN00C (XCTL) | `app/cbl/COTRN00C.cbl:518` |
| copies | COCOM01Y | `app/cbl/COTRN00C.cbl:61` |
| copies | COTRN00 | `app/cbl/COTRN00C.cbl:72` |
| copies | COTTL01Y | `app/cbl/COTRN00C.cbl:74` |
| copies | CSDAT01Y | `app/cbl/COTRN00C.cbl:75` |
| copies | CSMSG01Y | `app/cbl/COTRN00C.cbl:76` |
| copies | CVTRA05Y | `app/cbl/COTRN00C.cbl:78` |
| copies | DFHAID (system) | `app/cbl/COTRN00C.cbl:80` |
| copies | DFHBMSCA (system) | `app/cbl/COTRN00C.cbl:81` |
| data store | TRANSACT [B] | `app/cbl/COTRN00C.cbl:593-694` |

## COTRN01C

Page: [COTRN01C](../../01-detailed-documentation/application-documentation/07-programs/COTRN01C.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | CICS transaction CT01 | `app/csd/CARDDEMO.CSD:429-438` |
| called/transferred by | COMEN01C (XCTL) | `app/cbl/COMEN01C.cbl:185` |
| called/transferred by | COTRN00C (XCTL) | `app/cbl/COTRN00C.cbl:192` |
| calls/transfers to | CT01 (RETURN-TRANSID) | `app/cbl/COTRN01C.cbl:136` |
| calls/transfers to | COMEN01C, COSGN00C, COTRN00C (XCTL) | `app/cbl/COTRN01C.cbl:205` |
| copies | COCOM01Y | `app/cbl/COTRN01C.cbl:52` |
| copies | COTRN01 | `app/cbl/COTRN01C.cbl:63` |
| copies | COTTL01Y | `app/cbl/COTRN01C.cbl:65` |
| copies | CSDAT01Y | `app/cbl/COTRN01C.cbl:66` |
| copies | CSMSG01Y | `app/cbl/COTRN01C.cbl:67` |
| copies | CVTRA05Y | `app/cbl/COTRN01C.cbl:69` |
| copies | DFHAID (system) | `app/cbl/COTRN01C.cbl:71` |
| copies | DFHBMSCA (system) | `app/cbl/COTRN01C.cbl:72` |
| data store | TRANSACT [R, U] | `app/cbl/COTRN01C.cbl:269` |

## COTRN02C

Page: [COTRN02C](../../01-detailed-documentation/application-documentation/07-programs/COTRN02C.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | CICS transaction CT02 | `app/csd/CARDDEMO.CSD:439-448` |
| called/transferred by | COMEN01C (XCTL) | `app/cbl/COMEN01C.cbl:185` |
| calls/transfers to | CT02 (RETURN-TRANSID) | `app/cbl/COTRN02C.cbl:156` |
| calls/transfers to | CSUTLDTC (CALL-static) | `app/cbl/COTRN02C.cbl:393` |
| calls/transfers to | CSUTLDTC (CALL-static) | `app/cbl/COTRN02C.cbl:413` |
| calls/transfers to | COMEN01C, COSGN00C (XCTL) | `app/cbl/COTRN02C.cbl:508` |
| calls/transfers to | CT02 (RETURN-TRANSID) | `app/cbl/COTRN02C.cbl:530` |
| copies | COCOM01Y | `app/cbl/COTRN02C.cbl:71` |
| copies | COTRN02 | `app/cbl/COTRN02C.cbl:82` |
| copies | COTTL01Y | `app/cbl/COTRN02C.cbl:84` |
| copies | CSDAT01Y | `app/cbl/COTRN02C.cbl:85` |
| copies | CSMSG01Y | `app/cbl/COTRN02C.cbl:86` |
| copies | CVTRA05Y | `app/cbl/COTRN02C.cbl:88` |
| copies | CVACT01Y | `app/cbl/COTRN02C.cbl:89` |
| copies | CVACT03Y | `app/cbl/COTRN02C.cbl:90` |
| copies | DFHAID (system) | `app/cbl/COTRN02C.cbl:92` |
| copies | DFHBMSCA (system) | `app/cbl/COTRN02C.cbl:93` |
| data store | TRANSACT [B, C] | `app/cbl/COTRN02C.cbl:644-713` |
| data store | CXACAIX [R] | `app/cbl/COTRN02C.cbl:578` |
| data store | CCXREF [R] | `app/cbl/COTRN02C.cbl:611` |

## COTRTLIC

Page: [COTRTLIC](../../01-detailed-documentation/application-documentation/07-programs/COTRTLIC.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | CICS transaction CTLI | `app/app-transaction-type-db2/csd/CRDDEMOD.csd:25-34` |
| called/transferred by | COADM01C (XCTL) | `app/cbl/COADM01C.cbl:146` |
| called/transferred by | COTRTUPC (XCTL) | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:457` |
| calls/transfers to | COADM01C (XCTL) | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:620` |
| calls/transfers to | COTRTUPC (XCTL) | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:648` |
| calls/transfers to | CTLI (RETURN-TRANSID) | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:910` |
| calls/transfers to | DSNTIAC (CALL-dynamic) | `app/app-transaction-type-db2/cpy/CSDB2RPY.cpy:57` |
| copies | CSDB2RWY | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:304` |
| copies | CVCRD01Y | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:327` |
| copies | SQLCA (system) | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:331` |
| copies | DCLTRTYP | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:333` |
| copies | COCOM01Y | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:375` |
| copies | DFHBMSCA (system) | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:425` |
| copies | DFHAID (system) | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:426` |
| copies | COTTL01Y | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:430` |
| copies | COTRTLI | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:433` |
| copies | CSDAT01Y | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:480` |
| copies | CSMSG01Y | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:482` |
| copies | CSUSR01Y | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:485` |
| copies | CVACT02Y | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:490` |
| copies | CSDB2RPY | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:2055` |
| copies | CSSTRPFY | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:2060` |
| data store | CARDDEMO.TRANSACTION_TYPE [D, R, U] | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1803` |
| SQL SELECT | CARDDEMO.TRANSACTION_TYPE | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1803-1815` |
| SQL UPDATE | CARDDEMO.TRANSACTION_TYPE | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1846-1850` |
| SQL DELETE | CARDDEMO.TRANSACTION_TYPE | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1900-1903` |

## COTRTUPC

Page: [COTRTUPC](../../01-detailed-documentation/application-documentation/07-programs/COTRTUPC.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | CICS transaction CTTU | `app/app-transaction-type-db2/csd/CRDDEMOD.csd:35-44` |
| called/transferred by | COADM01C (XCTL) | `app/cbl/COADM01C.cbl:146` |
| called/transferred by | COTRTLIC (XCTL) | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:648` |
| calls/transfers to | COADM01C, COTRTLIC (XCTL) | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:457` |
| calls/transfers to | CTTU (RETURN-TRANSID) | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:567` |
| copies | CSUTLDWY | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:76` |
| copies | CVCRD01Y | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:241` |
| copies | DFHBMSCA (system) | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:257` |
| copies | DFHAID (system) | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:258` |
| copies | COTTL01Y | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:262` |
| copies | COTRTUP | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:265` |
| copies | CSDAT01Y | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:268` |
| copies | CSMSG01Y | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:271` |
| copies | CSMSG02Y | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:274` |
| copies | CSUSR01Y | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:277` |
| copies | SQLCA (system) | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:282-284` |
| copies | DCLTRTYP | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:286` |
| copies | DCLTRCAT | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:288` |
| copies | COCOM01Y | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:292` |
| copies | CSSETATY | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1358-1361` |
| copies | CSSTRPFY | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1671` |
| data store | CARDDEMO.TRANSACTION_TYPE [C, D, R, U] | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1475` |
| SQL SELECT | CARDDEMO.TRANSACTION_TYPE | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1475-1482` |
| SQL UPDATE | CARDDEMO.TRANSACTION_TYPE | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1544-1548` |
| SQL INSERT | CARDDEMO.TRANSACTION_TYPE | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1597-1602` |
| SQL DELETE | CARDDEMO.TRANSACTION_TYPE | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1627-1630` |

## COUSR00C

Page: [COUSR00C](../../01-detailed-documentation/application-documentation/07-programs/COUSR00C.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | CICS transaction CU00 | `app/csd/CARDDEMO.CSD:449-458` |
| called/transferred by | COADM01C (XCTL) | `app/cbl/COADM01C.cbl:146` |
| calls/transfers to | CU00 (RETURN-TRANSID) | `app/cbl/COUSR00C.cbl:141` |
| calls/transfers to | COUSR02C (XCTL) | `app/cbl/COUSR00C.cbl:196` |
| calls/transfers to | COUSR03C (XCTL) | `app/cbl/COUSR00C.cbl:206` |
| calls/transfers to | COADM01C, COSGN00C (XCTL) | `app/cbl/COUSR00C.cbl:514` |
| copies | COCOM01Y | `app/cbl/COUSR00C.cbl:66` |
| copies | COUSR00 | `app/cbl/COUSR00C.cbl:76` |
| copies | COTTL01Y | `app/cbl/COUSR00C.cbl:78` |
| copies | CSDAT01Y | `app/cbl/COUSR00C.cbl:79` |
| copies | CSMSG01Y | `app/cbl/COUSR00C.cbl:80` |
| copies | CSUSR01Y | `app/cbl/COUSR00C.cbl:81` |
| copies | DFHAID (system) | `app/cbl/COUSR00C.cbl:83` |
| copies | DFHBMSCA (system) | `app/cbl/COUSR00C.cbl:84` |
| data store | USRSEC [B] | `app/cbl/COUSR00C.cbl:588-689` |

## COUSR01C

Page: [COUSR01C](../../01-detailed-documentation/application-documentation/07-programs/COUSR01C.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | CICS transaction CU01 | `app/csd/CARDDEMO.CSD:459-468` |
| called/transferred by | COADM01C (XCTL) | `app/cbl/COADM01C.cbl:146` |
| calls/transfers to | CU01 (RETURN-TRANSID) | `app/cbl/COUSR01C.cbl:107` |
| calls/transfers to | COADM01C, COSGN00C (XCTL) | `app/cbl/COUSR01C.cbl:175` |
| copies | COCOM01Y | `app/cbl/COUSR01C.cbl:46` |
| copies | COUSR01 | `app/cbl/COUSR01C.cbl:48` |
| copies | COTTL01Y | `app/cbl/COUSR01C.cbl:50` |
| copies | CSDAT01Y | `app/cbl/COUSR01C.cbl:51` |
| copies | CSMSG01Y | `app/cbl/COUSR01C.cbl:52` |
| copies | CSUSR01Y | `app/cbl/COUSR01C.cbl:53` |
| copies | DFHAID (system) | `app/cbl/COUSR01C.cbl:55` |
| copies | DFHBMSCA (system) | `app/cbl/COUSR01C.cbl:56` |
| data store | USRSEC [C] | `app/cbl/COUSR01C.cbl:240` |

## COUSR02C

Page: [COUSR02C](../../01-detailed-documentation/application-documentation/07-programs/COUSR02C.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | CICS transaction CU02 | `app/csd/CARDDEMO.CSD:469-478` |
| called/transferred by | COADM01C (XCTL) | `app/cbl/COADM01C.cbl:146` |
| called/transferred by | COUSR00C (XCTL) | `app/cbl/COUSR00C.cbl:196` |
| calls/transfers to | CU02 (RETURN-TRANSID) | `app/cbl/COUSR02C.cbl:135` |
| calls/transfers to | COADM01C, COSGN00C (XCTL) | `app/cbl/COUSR02C.cbl:258` |
| copies | COCOM01Y | `app/cbl/COUSR02C.cbl:49` |
| copies | COUSR02 | `app/cbl/COUSR02C.cbl:60` |
| copies | COTTL01Y | `app/cbl/COUSR02C.cbl:62` |
| copies | CSDAT01Y | `app/cbl/COUSR02C.cbl:63` |
| copies | CSMSG01Y | `app/cbl/COUSR02C.cbl:64` |
| copies | CSUSR01Y | `app/cbl/COUSR02C.cbl:65` |
| copies | DFHAID (system) | `app/cbl/COUSR02C.cbl:67` |
| copies | DFHBMSCA (system) | `app/cbl/COUSR02C.cbl:68` |
| data store | USRSEC [R, U] | `app/cbl/COUSR02C.cbl:322-360` |

## COUSR03C

Page: [COUSR03C](../../01-detailed-documentation/application-documentation/07-programs/COUSR03C.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | CICS transaction CU03 | `app/csd/CARDDEMO.CSD:479-488` |
| called/transferred by | COADM01C (XCTL) | `app/cbl/COADM01C.cbl:146` |
| called/transferred by | COUSR00C (XCTL) | `app/cbl/COUSR00C.cbl:206` |
| calls/transfers to | CU03 (RETURN-TRANSID) | `app/cbl/COUSR03C.cbl:134` |
| calls/transfers to | COADM01C, COSGN00C (XCTL) | `app/cbl/COUSR03C.cbl:205` |
| copies | COCOM01Y | `app/cbl/COUSR03C.cbl:49` |
| copies | COUSR03 | `app/cbl/COUSR03C.cbl:60` |
| copies | COTTL01Y | `app/cbl/COUSR03C.cbl:62` |
| copies | CSDAT01Y | `app/cbl/COUSR03C.cbl:63` |
| copies | CSMSG01Y | `app/cbl/COUSR03C.cbl:64` |
| copies | CSUSR01Y | `app/cbl/COUSR03C.cbl:65` |
| copies | DFHAID (system) | `app/cbl/COUSR03C.cbl:67` |
| copies | DFHBMSCA (system) | `app/cbl/COUSR03C.cbl:68` |
| data store | USRSEC [D, R, U] | `app/cbl/COUSR03C.cbl:269-307` |

## CSUTLDTC

Page: [CSUTLDTC](../../01-detailed-documentation/application-documentation/07-programs/CSUTLDTC.md).

| Relation | Target | Evidence |
|---|---|---|
| called/transferred by | CORPT00C (CALL-static) | `app/cbl/CORPT00C.cbl:392` |
| called/transferred by | CORPT00C (CALL-static) | `app/cbl/CORPT00C.cbl:412` |
| called/transferred by | COTRN02C (CALL-static) | `app/cbl/COTRN02C.cbl:393` |
| called/transferred by | COTRN02C (CALL-static) | `app/cbl/COTRN02C.cbl:413` |

## DBUNLDGS

Page: [DBUNLDGS](../../01-detailed-documentation/application-documentation/07-programs/DBUNLDGS.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | job [UNLDGSAM](../../01-detailed-documentation/application-documentation/06-batch/jobs/UNLDGSAM.md) step STEP01 | `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:26-27` |
| calls/transfers to | CBLTDLI (CALL-static) | `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:222` |
| calls/transfers to | CBLTDLI (CALL-static) | `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:267` |
| calls/transfers to | CBLTDLI (CALL-static) | `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:302` |
| calls/transfers to | CBLTDLI (CALL-static) | `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:321` |
| copies | IMSFUNCS | `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:136` |
| copies | CIPAUSMY | `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:143` |
| copies | CIPAUDTY | `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:147` |
| copies | PAUTBPCB | `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:154` |
| copies | PASFLPCB | `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:155` |
| copies | PADFLPCB | `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:156` |

## PAUDBLOD

Page: [PAUDBLOD](../../01-detailed-documentation/application-documentation/07-programs/PAUDBLOD.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | job [LOADPADB](../../01-detailed-documentation/application-documentation/06-batch/jobs/LOADPADB.md) step STEP01 | `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL:26-27` |
| calls/transfers to | CBLTDLI (CALL-static) | `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:244` |
| calls/transfers to | CBLTDLI (CALL-static) | `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:296` |
| calls/transfers to | CBLTDLI (CALL-static) | `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:321` |
| copies | IMSFUNCS | `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:142` |
| copies | CIPAUSMY | `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:149` |
| copies | CIPAUDTY | `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:153` |
| copies | PAUTBPCB | `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:161` |

## PAUDBUNL

Page: [PAUDBUNL](../../01-detailed-documentation/application-documentation/07-programs/PAUDBUNL.md).

| Relation | Target | Evidence |
|---|---|---|
| started by | job [UNLDPADB](../../01-detailed-documentation/application-documentation/06-batch/jobs/UNLDPADB.md) step STEP01 | `app/app-authorization-ims-db2-mq/jcl/UNLDPADB.JCL:38-39` |
| calls/transfers to | CBLTDLI (CALL-static) | `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:213` |
| calls/transfers to | CBLTDLI (CALL-static) | `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:257` |
| copies | IMSFUNCS | `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:132` |
| copies | CIPAUSMY | `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:139` |
| copies | CIPAUDTY | `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:143` |
| copies | PAUTBPCB | `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:150` |

## Sources

- `docs/_work/structure/`
- `docs/_work/xref/call-graph.json`
- `docs/_work/xref/crud-matrix.json`

## Confidence

Confirmed except resolved dynamic transfers, which keep the confidence recorded in the call graph.
