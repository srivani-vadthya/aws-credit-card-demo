# CRUD matrix

Stores are logical SELECT names, CICS file names, or other store ids recorded on the program. They are not renamed to physical dataset names here.

| Program | Store | Kind | Ops | Evidence |
|---|---|---|---|---|
| CBACT01C | VBRC-FILE | logical | C | app/cbl/CBACT01C.cbl:290-305 |
| CBACT01C | ACCTFILE-FILE | logical | R | app/cbl/CBACT01C.cbl:166-319 |
| CBACT01C | ARRY-FILE | logical | C | app/cbl/CBACT01C.cbl:264 |
| CBACT01C | OUT-FILE | logical | C | app/cbl/CBACT01C.cbl:243 |
| CBACT02C | CARDFILE-FILE | logical | R | app/cbl/CBACT02C.cbl:93-120 |
| CBACT03C | XREFFILE-FILE | logical | R | app/cbl/CBACT03C.cbl:93-120 |
| CBACT04C | TRANSACT-FILE | logical | C | app/cbl/CBACT04C.cbl:309 |
| CBACT04C | TCATBAL-FILE | logical | R | app/cbl/CBACT04C.cbl:236-326 |
| CBACT04C | XREF-FILE | logical | R | app/cbl/CBACT04C.cbl:254-394 |
| CBACT04C | ACCOUNT-FILE | logical | R, U | app/cbl/CBACT04C.cbl:291-373 |
| CBACT04C | DISCGRP-FILE | logical | R | app/cbl/CBACT04C.cbl:272-444 |
| CBCUS01C | CUSTFILE-FILE | logical | R | app/cbl/CBCUS01C.cbl:93-120 |
| CBEXPORT | CUSTOMER-INPUT | logical | R | app/cbl/CBEXPORT.cbl:200-260 |
| CBEXPORT | ACCOUNT-INPUT | logical | R | app/cbl/CBEXPORT.cbl:207-329 |
| CBEXPORT | XREF-INPUT | logical | R | app/cbl/CBEXPORT.cbl:214-393 |
| CBEXPORT | CARD-INPUT | logical | R | app/cbl/CBEXPORT.cbl:228-513 |
| CBEXPORT | EXPORT-OUTPUT | logical | C | app/cbl/CBEXPORT.cbl:235 |
| CBEXPORT | TRANSACTION-INPUT | logical | R | app/cbl/CBEXPORT.cbl:221-448 |
| CBIMPORT | EXPORT-INPUT | logical | R | app/cbl/CBIMPORT.cbl:198-261 |
| CBIMPORT | ACCOUNT-OUTPUT | logical | C | app/cbl/CBIMPORT.cbl:212 |
| CBIMPORT | TRANSACTION-OUTPUT | logical | C | app/cbl/CBIMPORT.cbl:226 |
| CBIMPORT | XREF-OUTPUT | logical | C | app/cbl/CBIMPORT.cbl:219 |
| CBIMPORT | ERROR-OUTPUT | logical | C | app/cbl/CBIMPORT.cbl:439 |
| CBIMPORT | CUSTOMER-OUTPUT | logical | C | app/cbl/CBIMPORT.cbl:205 |
| CBIMPORT | CARD-OUTPUT | logical | C | app/cbl/CBIMPORT.cbl:233 |
| CBPAUP0C | DLI-DLET | logical | D | app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:310 |
| CBPAUP0C | DLI-GNP | logical | R | app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:255 |
| CBPAUP0C | DLI-GN | logical | R | app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:223 |
| CBSTM03A | HTML-FILE | logical | C | app/cbl/CBSTM03A.CBL:440-721 |
| CBSTM03A | STMT-FILE | logical | C | app/cbl/CBSTM03A.CBL:293 |
| CBSTM03B | ACCT-FILE | logical | R | app/cbl/CBSTM03B.CBL:209-215 |
| CBSTM03B | XREF-FILE | logical | R | app/cbl/CBSTM03B.CBL:160-165 |
| CBSTM03B | CUST-FILE | logical | R | app/cbl/CBSTM03B.CBL:184-190 |
| CBSTM03B | TRNX-FILE | logical | R | app/cbl/CBSTM03B.CBL:136-141 |
| CBTRN01C | TRANSACT-FILE | logical | R | app/cbl/CBTRN01C.cbl:345 |
| CBTRN01C | XREF-FILE | logical | R | app/cbl/CBTRN01C.cbl:229-291 |
| CBTRN01C | CARD-FILE | logical | R | app/cbl/CBTRN01C.cbl:309 |
| CBTRN01C | ACCOUNT-FILE | logical | R | app/cbl/CBTRN01C.cbl:243-327 |
| CBTRN01C | CUSTOMER-FILE | logical | R | app/cbl/CBTRN01C.cbl:273 |
| CBTRN01C | DALYTRAN-FILE | logical | R | app/cbl/CBTRN01C.cbl:203-254 |
| CBTRN02C | TRANSACT-FILE | logical | C | app/cbl/CBTRN02C.cbl:256 |
| CBTRN02C | DALYREJS-FILE | logical | C | app/cbl/CBTRN02C.cbl:293 |
| CBTRN02C | XREF-FILE | logical | R | app/cbl/CBTRN02C.cbl:275-383 |
| CBTRN02C | ACCOUNT-FILE | logical | R, U | app/cbl/CBTRN02C.cbl:311-395 |
| CBTRN02C | TCATBAL-FILE | logical | C, R, U | app/cbl/CBTRN02C.cbl:329-474 |
| CBTRN02C | DALYTRAN-FILE | logical | R | app/cbl/CBTRN02C.cbl:238-346 |
| CBTRN03C | TRANSACT-FILE | logical | R | app/cbl/CBTRN03C.cbl:249-378 |
| CBTRN03C | XREF-FILE | logical | R | app/cbl/CBTRN03C.cbl:414-485 |
| CBTRN03C | TRANCATG-FILE | logical | R | app/cbl/CBTRN03C.cbl:450-505 |
| CBTRN03C | REPORT-FILE | logical | C | app/cbl/CBTRN03C.cbl:345 |
| CBTRN03C | DATE-PARMS-FILE | logical | R | app/cbl/CBTRN03C.cbl:221-468 |
| CBTRN03C | TRANTYPE-FILE | logical | R | app/cbl/CBTRN03C.cbl:432-495 |
| COACCT01 | ACCTDAT | cics-file | R | app/app-vsam-mq/cbl/COACCT01.cbl:396 |
| COACCT01 | MQ-GET | logical | R | app/app-vsam-mq/cbl/COACCT01.cbl:352 |
| COACCT01 | MQ-PUT | logical | C | app/app-vsam-mq/cbl/COACCT01.cbl:479 |
| COBIL00C | TRANSACT | cics-file | B, C | app/cbl/COBIL00C.cbl:443-512 |
| COBIL00C | ACCTDAT | cics-file | R, U | app/cbl/COBIL00C.cbl:345-379 |
| COBIL00C | CXACAIX | cics-file | R | app/cbl/COBIL00C.cbl:410 |
| COBTUPDT | CARDDEMO.TRANSACTION_TYPE | logical | C, D, U | app/app-transaction-type-db2/cbl/COBTUPDT.cbl:137 |
| CODATE01 | MQ-GET | logical | R | app/app-vsam-mq/cbl/CODATE01.cbl:301 |
| CODATE01 | MQ-PUT | logical | C | app/app-vsam-mq/cbl/CODATE01.cbl:383 |
| COPAUA0C | MQ-GET | logical | R | app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:400 |
| COPAUA0C | CCXREF | logical | R | app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:477 |
| COPAUA0C | DLI-REPL | logical | U | app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:825 |
| COPAUA0C | CUSTDAT | logical | R | app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:573 |
| COPAUA0C | DLI-ISRT | logical | C | app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:830 |
| COPAUA0C | MQ-PUT | logical | C | app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:758 |
| COPAUA0C | ACCTDAT | logical | R | app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:525 |
| COPAUA0C | DLI-GU | logical | R | app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:620 |
| COPAUA0C | CSSL | logical | C | app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:1001 |
| COPAUS0C | DLI-GU | logical | R | app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:973 |
| COPAUS0C | ACCTDAT | logical | R | app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:869 |
| COPAUS0C | DLI-GNP | logical | R | app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:461 |
| COPAUS0C | CXACAIX | logical | R | app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:818 |
| COPAUS0C | CUSTDAT | logical | R | app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:920 |
| COPAUS1C | DLI-GNP | logical | R | app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:465 |
| COPAUS1C | DLI-GU | logical | R | app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:439 |
| COPAUS1C | DLI-REPL | logical | U | app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:525 |
| COPAUS2C | CARDDEMO.AUTHFRDS | logical | C, U | app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:141 |
| CORPT00C | JOBS | cics-td-queue | C | app/cbl/CORPT00C.cbl:517 |
| COSGN00C | USRSEC | cics-file | R | app/cbl/COSGN00C.cbl:211 |
| COTRN00C | TRANSACT | cics-file | B | app/cbl/COTRN00C.cbl:593-694 |
| COTRN01C | TRANSACT | cics-file | R, U | app/cbl/COTRN01C.cbl:269 |
| COTRN02C | TRANSACT | cics-file | B, C | app/cbl/COTRN02C.cbl:644-713 |
| COTRN02C | CXACAIX | cics-file | R | app/cbl/COTRN02C.cbl:578 |
| COTRN02C | CCXREF | cics-file | R | app/cbl/COTRN02C.cbl:611 |
| COTRTLIC | CARDDEMO.TRANSACTION_TYPE | logical | D, R, U | app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1803 |
| COTRTUPC | CARDDEMO.TRANSACTION_TYPE | logical | C, D, R, U | app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1475 |
| COUSR00C | USRSEC | cics-file | B | app/cbl/COUSR00C.cbl:588-689 |
| COUSR01C | USRSEC | cics-file | C | app/cbl/COUSR01C.cbl:240 |
| COUSR02C | USRSEC | cics-file | R, U | app/cbl/COUSR02C.cbl:322-360 |
| COUSR03C | USRSEC | cics-file | D, R, U | app/cbl/COUSR03C.cbl:269-307 |

## Sources

- `docs/_work/xref/crud-matrix.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
