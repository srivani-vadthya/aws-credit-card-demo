# Copybook usage matrix

Every COPY and EXEC SQL INCLUDE edge, including commented-out statements and system copybooks.

| Copybook | Used by | User type | Statement | Resolution | Resolved path | Line |
|---|---|---|---|---|---|---|
| [AUTHFRDS](../08-data/layouts/AUTHFRDS.md) | COPAUS2C | cobol-program | EXEC SQL INCLUDE | inventory | app/app-authorization-ims-db2-mq/dcl/AUTHFRDS.dcl | `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:68-70` |
| [CCPAUERY](../08-data/layouts/CCPAUERY.md) | COPAUA0C | cobol-program | COPY | inventory | app/app-authorization-ims-db2-mq/cpy/CCPAUERY.cpy | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:185` |
| [CCPAURLY](../08-data/layouts/CCPAURLY.md) | COPAUA0C | cobol-program | COPY | inventory | app/app-authorization-ims-db2-mq/cpy/CCPAURLY.cpy | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:182` |
| [CCPAURQY](../08-data/layouts/CCPAURQY.md) | COPAUA0C | cobol-program | COPY | inventory | app/app-authorization-ims-db2-mq/cpy/CCPAURQY.cpy | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:178` |
| [CIPAUDTY](../08-data/layouts/CIPAUDTY.md) | CBPAUP0C | cobol-program | COPY | inventory | app/app-authorization-ims-db2-mq/cpy/CIPAUDTY.cpy | `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:121` |
| [CIPAUDTY](../08-data/layouts/CIPAUDTY.md) | COPAUA0C | cobol-program | COPY | inventory | app/app-authorization-ims-db2-mq/cpy/CIPAUDTY.cpy | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:197` |
| [CIPAUDTY](../08-data/layouts/CIPAUDTY.md) | COPAUS0C | cobol-program | COPY | inventory | app/app-authorization-ims-db2-mq/cpy/CIPAUDTY.cpy | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:165` |
| [CIPAUDTY](../08-data/layouts/CIPAUDTY.md) | COPAUS1C | cobol-program | COPY | inventory | app/app-authorization-ims-db2-mq/cpy/CIPAUDTY.cpy | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:146` |
| [CIPAUDTY](../08-data/layouts/CIPAUDTY.md) | COPAUS2C | cobol-program | COPY | inventory | app/app-authorization-ims-db2-mq/cpy/CIPAUDTY.cpy | `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:78` |
| [CIPAUDTY](../08-data/layouts/CIPAUDTY.md) | DBUNLDGS | cobol-program | COPY | inventory | app/app-authorization-ims-db2-mq/cpy/CIPAUDTY.cpy | `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:147` |
| [CIPAUDTY](../08-data/layouts/CIPAUDTY.md) | PAUDBLOD | cobol-program | COPY | inventory | app/app-authorization-ims-db2-mq/cpy/CIPAUDTY.cpy | `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:153` |
| [CIPAUDTY](../08-data/layouts/CIPAUDTY.md) | PAUDBUNL | cobol-program | COPY | inventory | app/app-authorization-ims-db2-mq/cpy/CIPAUDTY.cpy | `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:143` |
| [CIPAUSMY](../08-data/layouts/CIPAUSMY.md) | CBPAUP0C | cobol-program | COPY | inventory | app/app-authorization-ims-db2-mq/cpy/CIPAUSMY.cpy | `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:117` |
| [CIPAUSMY](../08-data/layouts/CIPAUSMY.md) | COPAUA0C | cobol-program | COPY | inventory | app/app-authorization-ims-db2-mq/cpy/CIPAUSMY.cpy | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:193` |
| [CIPAUSMY](../08-data/layouts/CIPAUSMY.md) | COPAUS0C | cobol-program | COPY | inventory | app/app-authorization-ims-db2-mq/cpy/CIPAUSMY.cpy | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:161` |
| [CIPAUSMY](../08-data/layouts/CIPAUSMY.md) | COPAUS1C | cobol-program | COPY | inventory | app/app-authorization-ims-db2-mq/cpy/CIPAUSMY.cpy | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:142` |
| [CIPAUSMY](../08-data/layouts/CIPAUSMY.md) | DBUNLDGS | cobol-program | COPY | inventory | app/app-authorization-ims-db2-mq/cpy/CIPAUSMY.cpy | `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:143` |
| [CIPAUSMY](../08-data/layouts/CIPAUSMY.md) | PAUDBLOD | cobol-program | COPY | inventory | app/app-authorization-ims-db2-mq/cpy/CIPAUSMY.cpy | `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:149` |
| [CIPAUSMY](../08-data/layouts/CIPAUSMY.md) | PAUDBUNL | cobol-program | COPY | inventory | app/app-authorization-ims-db2-mq/cpy/CIPAUSMY.cpy | `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:139` |
| CMQGMOV | COACCT01 | cobol-program | COPY | system |  | `app/app-vsam-mq/cbl/COACCT01.cbl:71` |
| CMQGMOV | CODATE01 | cobol-program | COPY | system |  | `app/app-vsam-mq/cbl/CODATE01.cbl:71` |
| CMQGMOV | COPAUA0C | cobol-program | COPY | system |  | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:170` |
| CMQMDV | COACCT01 | cobol-program | COPY | system |  | `app/app-vsam-mq/cbl/COACCT01.cbl:79` |
| CMQMDV | CODATE01 | cobol-program | COPY | system |  | `app/app-vsam-mq/cbl/CODATE01.cbl:79` |
| CMQMDV | COPAUA0C | cobol-program | COPY | system |  | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:152` |
| CMQMDV | COPAUA0C | cobol-program | COPY | system |  | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:158` |
| CMQODV | COACCT01 | cobol-program | COPY | system |  | `app/app-vsam-mq/cbl/COACCT01.cbl:83` |
| CMQODV | CODATE01 | cobol-program | COPY | system |  | `app/app-vsam-mq/cbl/CODATE01.cbl:83` |
| CMQODV | COPAUA0C | cobol-program | COPY | system |  | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:149` |
| CMQODV | COPAUA0C | cobol-program | COPY | system |  | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:155` |
| CMQPMOV | COACCT01 | cobol-program | COPY | system |  | `app/app-vsam-mq/cbl/COACCT01.cbl:75` |
| CMQPMOV | CODATE01 | cobol-program | COPY | system |  | `app/app-vsam-mq/cbl/CODATE01.cbl:75` |
| CMQPMOV | COPAUA0C | cobol-program | COPY | system |  | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:167` |
| CMQTML | COACCT01 | cobol-program | COPY | system |  | `app/app-vsam-mq/cbl/COACCT01.cbl:90` |
| CMQTML | CODATE01 | cobol-program | COPY | system |  | `app/app-vsam-mq/cbl/CODATE01.cbl:90` |
| CMQTML | COPAUA0C | cobol-program | COPY | system |  | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:164` |
| CMQV | COACCT01 | cobol-program | COPY | system |  | `app/app-vsam-mq/cbl/COACCT01.cbl:87` |
| CMQV | CODATE01 | cobol-program | COPY | system |  | `app/app-vsam-mq/cbl/CODATE01.cbl:87` |
| CMQV | COPAUA0C | cobol-program | COPY | system |  | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:161` |
| COACTUP | COACTUPC | cobol-program | COPY | inventory | app/cpy-bms/COACTUP.CPY | `app/cbl/COACTUPC.cbl:623` |
| COACTVW | COACTVWC | cobol-program | COPY | inventory | app/cpy-bms/COACTVW.CPY | `app/cbl/COACTVWC.cbl:229` |
| COADM01 | COADM01C | cobol-program | COPY | inventory | app/cpy-bms/COADM01.CPY | `app/cbl/COADM01C.cbl:53` |
| [COADM02Y](../08-data/layouts/COADM02Y.md) | COADM01C | cobol-program | COPY | inventory | app/cpy/COADM02Y.cpy | `app/cbl/COADM01C.cbl:51` |
| COBIL00 | COBIL00C | cobol-program | COPY | inventory | app/cpy-bms/COBIL00.CPY | `app/cbl/COBIL00C.cbl:74` |
| [COCOM01Y](../08-data/layouts/COCOM01Y.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/COCOM01Y.cpy | `app/cbl/COACTUPC.cbl:650` |
| [COCOM01Y](../08-data/layouts/COCOM01Y.md) | COACTVWC | cobol-program | COPY | inventory | app/cpy/COCOM01Y.cpy | `app/cbl/COACTVWC.cbl:211` |
| [COCOM01Y](../08-data/layouts/COCOM01Y.md) | COADM01C | cobol-program | COPY | inventory | app/cpy/COCOM01Y.cpy | `app/cbl/COADM01C.cbl:50` |
| [COCOM01Y](../08-data/layouts/COCOM01Y.md) | COBIL00C | cobol-program | COPY | inventory | app/cpy/COCOM01Y.cpy | `app/cbl/COBIL00C.cbl:63` |
| [COCOM01Y](../08-data/layouts/COCOM01Y.md) | COCRDLIC | cobol-program | COPY | inventory | app/cpy/COCOM01Y.cpy | `app/cbl/COCRDLIC.cbl:227` |
| [COCOM01Y](../08-data/layouts/COCOM01Y.md) | COCRDSLC | cobol-program | COPY | inventory | app/cpy/COCOM01Y.cpy | `app/cbl/COCRDSLC.cbl:198` |
| [COCOM01Y](../08-data/layouts/COCOM01Y.md) | COCRDUPC | cobol-program | COPY | inventory | app/cpy/COCOM01Y.cpy | `app/cbl/COCRDUPC.cbl:272` |
| [COCOM01Y](../08-data/layouts/COCOM01Y.md) | COMEN01C | cobol-program | COPY | inventory | app/cpy/COCOM01Y.cpy | `app/cbl/COMEN01C.cbl:50` |
| [COCOM01Y](../08-data/layouts/COCOM01Y.md) | COPAUS0C | cobol-program | COPY | inventory | app/cpy/COCOM01Y.cpy | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:116` |
| [COCOM01Y](../08-data/layouts/COCOM01Y.md) | COPAUS1C | cobol-program | COPY | inventory | app/cpy/COCOM01Y.cpy | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:109` |
| [COCOM01Y](../08-data/layouts/COCOM01Y.md) | CORPT00C | cobol-program | COPY | inventory | app/cpy/COCOM01Y.cpy | `app/cbl/CORPT00C.cbl:138` |
| [COCOM01Y](../08-data/layouts/COCOM01Y.md) | COSGN00C | cobol-program | COPY | inventory | app/cpy/COCOM01Y.cpy | `app/cbl/COSGN00C.cbl:48` |
| [COCOM01Y](../08-data/layouts/COCOM01Y.md) | COTRN00C | cobol-program | COPY | inventory | app/cpy/COCOM01Y.cpy | `app/cbl/COTRN00C.cbl:61` |
| [COCOM01Y](../08-data/layouts/COCOM01Y.md) | COTRN01C | cobol-program | COPY | inventory | app/cpy/COCOM01Y.cpy | `app/cbl/COTRN01C.cbl:52` |
| [COCOM01Y](../08-data/layouts/COCOM01Y.md) | COTRN02C | cobol-program | COPY | inventory | app/cpy/COCOM01Y.cpy | `app/cbl/COTRN02C.cbl:71` |
| [COCOM01Y](../08-data/layouts/COCOM01Y.md) | COTRTLIC | cobol-program | COPY | inventory | app/cpy/COCOM01Y.cpy | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:375` |
| [COCOM01Y](../08-data/layouts/COCOM01Y.md) | COTRTUPC | cobol-program | COPY | inventory | app/cpy/COCOM01Y.cpy | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:292` |
| [COCOM01Y](../08-data/layouts/COCOM01Y.md) | COUSR00C | cobol-program | COPY | inventory | app/cpy/COCOM01Y.cpy | `app/cbl/COUSR00C.cbl:66` |
| [COCOM01Y](../08-data/layouts/COCOM01Y.md) | COUSR01C | cobol-program | COPY | inventory | app/cpy/COCOM01Y.cpy | `app/cbl/COUSR01C.cbl:46` |
| [COCOM01Y](../08-data/layouts/COCOM01Y.md) | COUSR02C | cobol-program | COPY | inventory | app/cpy/COCOM01Y.cpy | `app/cbl/COUSR02C.cbl:49` |
| [COCOM01Y](../08-data/layouts/COCOM01Y.md) | COUSR03C | cobol-program | COPY | inventory | app/cpy/COCOM01Y.cpy | `app/cbl/COUSR03C.cbl:49` |
| COCRDLI | COCRDLIC | cobol-program | COPY | inventory | app/cpy-bms/COCRDLI.CPY | `app/cbl/COCRDLIC.cbl:276` |
| COCRDSL | COCRDLIC | cobol-program | COPY | inventory (commented out) | app/cpy-bms/COCRDSL.CPY | `app/cbl/COCRDLIC.cbl:274` |
| COCRDSL | COCRDSLC | cobol-program | COPY | inventory | app/cpy-bms/COCRDSL.CPY | `app/cbl/COCRDSLC.cbl:215` |
| COCRDUP | COCRDUPC | cobol-program | COPY | inventory | app/cpy-bms/COCRDUP.CPY | `app/cbl/COCRDUPC.cbl:334` |
| [CODATECN](../08-data/layouts/CODATECN.md) | CBACT01C | cobol-program | COPY | inventory | app/cpy/CODATECN.cpy | `app/cbl/CBACT01C.cbl:90` |
| COMEN01 | COMEN01C | cobol-program | COPY | inventory | app/cpy-bms/COMEN01.CPY | `app/cbl/COMEN01C.cbl:53` |
| [COMEN02Y](../08-data/layouts/COMEN02Y.md) | COMEN01C | cobol-program | COPY | inventory | app/cpy/COMEN02Y.cpy | `app/cbl/COMEN01C.cbl:51` |
| COPAU00 | COPAUS0C | cobol-program | COPY | inventory | app/app-authorization-ims-db2-mq/cpy-bms/COPAU00.cpy | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:129` |
| COPAU01 | COPAUS1C | cobol-program | COPY | inventory | app/app-authorization-ims-db2-mq/cpy-bms/COPAU01.cpy | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:122` |
| CORPT00 | CORPT00C | cobol-program | COPY | inventory | app/cpy-bms/CORPT00.CPY | `app/cbl/CORPT00C.cbl:140` |
| COSGN00 | COSGN00C | cobol-program | COPY | inventory | app/cpy-bms/COSGN00.CPY | `app/cbl/COSGN00C.cbl:50` |
| [COSTM01](../08-data/layouts/COSTM01.md) | CBSTM03A | cobol-program | COPY | inventory | app/cpy/COSTM01.CPY | `app/cbl/CBSTM03A.CBL:51` |
| COTRN00 | COTRN00C | cobol-program | COPY | inventory | app/cpy-bms/COTRN00.CPY | `app/cbl/COTRN00C.cbl:72` |
| COTRN01 | COTRN01C | cobol-program | COPY | inventory | app/cpy-bms/COTRN01.CPY | `app/cbl/COTRN01C.cbl:63` |
| COTRN02 | COTRN02C | cobol-program | COPY | inventory | app/cpy-bms/COTRN02.CPY | `app/cbl/COTRN02C.cbl:82` |
| COTRTLI | COTRTLIC | cobol-program | COPY | inventory | app/app-transaction-type-db2/cpy-bms/COTRTLI.cpy | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:433` |
| COTRTUP | COTRTUPC | cobol-program | COPY | inventory | app/app-transaction-type-db2/cpy-bms/COTRTUP.cpy | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:265` |
| [COTTL01Y](../08-data/layouts/COTTL01Y.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/COTTL01Y.cpy | `app/cbl/COACTUPC.cbl:620` |
| [COTTL01Y](../08-data/layouts/COTTL01Y.md) | COACTVWC | cobol-program | COPY | inventory | app/cpy/COTTL01Y.cpy | `app/cbl/COACTVWC.cbl:226` |
| [COTTL01Y](../08-data/layouts/COTTL01Y.md) | COADM01C | cobol-program | COPY | inventory | app/cpy/COTTL01Y.cpy | `app/cbl/COADM01C.cbl:55` |
| [COTTL01Y](../08-data/layouts/COTTL01Y.md) | COBIL00C | cobol-program | COPY | inventory | app/cpy/COTTL01Y.cpy | `app/cbl/COBIL00C.cbl:76` |
| [COTTL01Y](../08-data/layouts/COTTL01Y.md) | COCRDLIC | cobol-program | COPY | inventory | app/cpy/COTTL01Y.cpy | `app/cbl/COCRDLIC.cbl:272` |
| [COTTL01Y](../08-data/layouts/COTTL01Y.md) | COCRDSLC | cobol-program | COPY | inventory | app/cpy/COTTL01Y.cpy | `app/cbl/COCRDSLC.cbl:213` |
| [COTTL01Y](../08-data/layouts/COTTL01Y.md) | COCRDUPC | cobol-program | COPY | inventory | app/cpy/COTTL01Y.cpy | `app/cbl/COCRDUPC.cbl:332` |
| [COTTL01Y](../08-data/layouts/COTTL01Y.md) | COMEN01C | cobol-program | COPY | inventory | app/cpy/COTTL01Y.cpy | `app/cbl/COMEN01C.cbl:55` |
| [COTTL01Y](../08-data/layouts/COTTL01Y.md) | COPAUS0C | cobol-program | COPY | inventory | app/cpy/COTTL01Y.cpy | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:132` |
| [COTTL01Y](../08-data/layouts/COTTL01Y.md) | COPAUS1C | cobol-program | COPY | inventory | app/cpy/COTTL01Y.cpy | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:126` |
| [COTTL01Y](../08-data/layouts/COTTL01Y.md) | CORPT00C | cobol-program | COPY | inventory | app/cpy/COTTL01Y.cpy | `app/cbl/CORPT00C.cbl:142` |
| [COTTL01Y](../08-data/layouts/COTTL01Y.md) | COSGN00C | cobol-program | COPY | inventory | app/cpy/COTTL01Y.cpy | `app/cbl/COSGN00C.cbl:52` |
| [COTTL01Y](../08-data/layouts/COTTL01Y.md) | COTRN00C | cobol-program | COPY | inventory | app/cpy/COTTL01Y.cpy | `app/cbl/COTRN00C.cbl:74` |
| [COTTL01Y](../08-data/layouts/COTTL01Y.md) | COTRN01C | cobol-program | COPY | inventory | app/cpy/COTTL01Y.cpy | `app/cbl/COTRN01C.cbl:65` |
| [COTTL01Y](../08-data/layouts/COTTL01Y.md) | COTRN02C | cobol-program | COPY | inventory | app/cpy/COTTL01Y.cpy | `app/cbl/COTRN02C.cbl:84` |
| [COTTL01Y](../08-data/layouts/COTTL01Y.md) | COTRTLIC | cobol-program | COPY | inventory | app/cpy/COTTL01Y.cpy | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:430` |
| [COTTL01Y](../08-data/layouts/COTTL01Y.md) | COTRTUPC | cobol-program | COPY | inventory | app/cpy/COTTL01Y.cpy | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:262` |
| [COTTL01Y](../08-data/layouts/COTTL01Y.md) | COUSR00C | cobol-program | COPY | inventory | app/cpy/COTTL01Y.cpy | `app/cbl/COUSR00C.cbl:78` |
| [COTTL01Y](../08-data/layouts/COTTL01Y.md) | COUSR01C | cobol-program | COPY | inventory | app/cpy/COTTL01Y.cpy | `app/cbl/COUSR01C.cbl:50` |
| [COTTL01Y](../08-data/layouts/COTTL01Y.md) | COUSR02C | cobol-program | COPY | inventory | app/cpy/COTTL01Y.cpy | `app/cbl/COUSR02C.cbl:62` |
| [COTTL01Y](../08-data/layouts/COTTL01Y.md) | COUSR03C | cobol-program | COPY | inventory | app/cpy/COTTL01Y.cpy | `app/cbl/COUSR03C.cbl:62` |
| COUSR00 | COUSR00C | cobol-program | COPY | inventory | app/cpy-bms/COUSR00.CPY | `app/cbl/COUSR00C.cbl:76` |
| COUSR01 | COUSR01C | cobol-program | COPY | inventory | app/cpy-bms/COUSR01.CPY | `app/cbl/COUSR01C.cbl:48` |
| COUSR02 | COUSR02C | cobol-program | COPY | inventory | app/cpy-bms/COUSR02.CPY | `app/cbl/COUSR02C.cbl:60` |
| COUSR03 | COUSR03C | cobol-program | COPY | inventory | app/cpy-bms/COUSR03.CPY | `app/cbl/COUSR03C.cbl:60` |
| [CSDAT01Y](../08-data/layouts/CSDAT01Y.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSDAT01Y.cpy | `app/cbl/COACTUPC.cbl:626` |
| [CSDAT01Y](../08-data/layouts/CSDAT01Y.md) | COACTVWC | cobol-program | COPY | inventory | app/cpy/CSDAT01Y.cpy | `app/cbl/COACTVWC.cbl:232` |
| [CSDAT01Y](../08-data/layouts/CSDAT01Y.md) | COADM01C | cobol-program | COPY | inventory | app/cpy/CSDAT01Y.cpy | `app/cbl/COADM01C.cbl:56` |
| [CSDAT01Y](../08-data/layouts/CSDAT01Y.md) | COBIL00C | cobol-program | COPY | inventory | app/cpy/CSDAT01Y.cpy | `app/cbl/COBIL00C.cbl:77` |
| [CSDAT01Y](../08-data/layouts/CSDAT01Y.md) | COCRDLIC | cobol-program | COPY | inventory | app/cpy/CSDAT01Y.cpy | `app/cbl/COCRDLIC.cbl:279` |
| [CSDAT01Y](../08-data/layouts/CSDAT01Y.md) | COCRDSLC | cobol-program | COPY | inventory | app/cpy/CSDAT01Y.cpy | `app/cbl/COCRDSLC.cbl:218` |
| [CSDAT01Y](../08-data/layouts/CSDAT01Y.md) | COCRDUPC | cobol-program | COPY | inventory | app/cpy/CSDAT01Y.cpy | `app/cbl/COCRDUPC.cbl:337` |
| [CSDAT01Y](../08-data/layouts/CSDAT01Y.md) | COMEN01C | cobol-program | COPY | inventory | app/cpy/CSDAT01Y.cpy | `app/cbl/COMEN01C.cbl:56` |
| [CSDAT01Y](../08-data/layouts/CSDAT01Y.md) | COPAUS0C | cobol-program | COPY | inventory | app/cpy/CSDAT01Y.cpy | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:135` |
| [CSDAT01Y](../08-data/layouts/CSDAT01Y.md) | COPAUS1C | cobol-program | COPY | inventory | app/cpy/CSDAT01Y.cpy | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:129` |
| [CSDAT01Y](../08-data/layouts/CSDAT01Y.md) | CORPT00C | cobol-program | COPY | inventory | app/cpy/CSDAT01Y.cpy | `app/cbl/CORPT00C.cbl:143` |
| [CSDAT01Y](../08-data/layouts/CSDAT01Y.md) | COSGN00C | cobol-program | COPY | inventory | app/cpy/CSDAT01Y.cpy | `app/cbl/COSGN00C.cbl:53` |
| [CSDAT01Y](../08-data/layouts/CSDAT01Y.md) | COTRN00C | cobol-program | COPY | inventory | app/cpy/CSDAT01Y.cpy | `app/cbl/COTRN00C.cbl:75` |
| [CSDAT01Y](../08-data/layouts/CSDAT01Y.md) | COTRN01C | cobol-program | COPY | inventory | app/cpy/CSDAT01Y.cpy | `app/cbl/COTRN01C.cbl:66` |
| [CSDAT01Y](../08-data/layouts/CSDAT01Y.md) | COTRN02C | cobol-program | COPY | inventory | app/cpy/CSDAT01Y.cpy | `app/cbl/COTRN02C.cbl:85` |
| [CSDAT01Y](../08-data/layouts/CSDAT01Y.md) | COTRTLIC | cobol-program | COPY | inventory | app/cpy/CSDAT01Y.cpy | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:480` |
| [CSDAT01Y](../08-data/layouts/CSDAT01Y.md) | COTRTUPC | cobol-program | COPY | inventory | app/cpy/CSDAT01Y.cpy | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:268` |
| [CSDAT01Y](../08-data/layouts/CSDAT01Y.md) | COUSR00C | cobol-program | COPY | inventory | app/cpy/CSDAT01Y.cpy | `app/cbl/COUSR00C.cbl:79` |
| [CSDAT01Y](../08-data/layouts/CSDAT01Y.md) | COUSR01C | cobol-program | COPY | inventory | app/cpy/CSDAT01Y.cpy | `app/cbl/COUSR01C.cbl:51` |
| [CSDAT01Y](../08-data/layouts/CSDAT01Y.md) | COUSR02C | cobol-program | COPY | inventory | app/cpy/CSDAT01Y.cpy | `app/cbl/COUSR02C.cbl:63` |
| [CSDAT01Y](../08-data/layouts/CSDAT01Y.md) | COUSR03C | cobol-program | COPY | inventory | app/cpy/CSDAT01Y.cpy | `app/cbl/COUSR03C.cbl:63` |
| [CSDB2RPY](../08-data/layouts/CSDB2RPY.md) | COTRTLIC | cobol-program | EXEC SQL INCLUDE | inventory | app/app-transaction-type-db2/cpy/CSDB2RPY.cpy | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:2055` |
| [CSDB2RWY](../08-data/layouts/CSDB2RWY.md) | COTRTLIC | cobol-program | EXEC SQL INCLUDE | inventory | app/app-transaction-type-db2/cpy/CSDB2RWY.cpy | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:304` |
| [CSLKPCDY](../08-data/layouts/CSLKPCDY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSLKPCDY.cpy | `app/cbl/COACTUPC.cbl:602` |
| [CSMSG01Y](../08-data/layouts/CSMSG01Y.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSMSG01Y.cpy | `app/cbl/COACTUPC.cbl:629` |
| [CSMSG01Y](../08-data/layouts/CSMSG01Y.md) | COACTVWC | cobol-program | COPY | inventory | app/cpy/CSMSG01Y.cpy | `app/cbl/COACTVWC.cbl:235` |
| [CSMSG01Y](../08-data/layouts/CSMSG01Y.md) | COADM01C | cobol-program | COPY | inventory | app/cpy/CSMSG01Y.cpy | `app/cbl/COADM01C.cbl:57` |
| [CSMSG01Y](../08-data/layouts/CSMSG01Y.md) | COBIL00C | cobol-program | COPY | inventory | app/cpy/CSMSG01Y.cpy | `app/cbl/COBIL00C.cbl:78` |
| [CSMSG01Y](../08-data/layouts/CSMSG01Y.md) | COCRDLIC | cobol-program | COPY | inventory | app/cpy/CSMSG01Y.cpy | `app/cbl/COCRDLIC.cbl:281` |
| [CSMSG01Y](../08-data/layouts/CSMSG01Y.md) | COCRDSLC | cobol-program | COPY | inventory | app/cpy/CSMSG01Y.cpy | `app/cbl/COCRDSLC.cbl:221` |
| [CSMSG01Y](../08-data/layouts/CSMSG01Y.md) | COCRDUPC | cobol-program | COPY | inventory | app/cpy/CSMSG01Y.cpy | `app/cbl/COCRDUPC.cbl:340` |
| [CSMSG01Y](../08-data/layouts/CSMSG01Y.md) | COMEN01C | cobol-program | COPY | inventory | app/cpy/CSMSG01Y.cpy | `app/cbl/COMEN01C.cbl:57` |
| [CSMSG01Y](../08-data/layouts/CSMSG01Y.md) | COPAUS0C | cobol-program | COPY | inventory | app/cpy/CSMSG01Y.cpy | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:138` |
| [CSMSG01Y](../08-data/layouts/CSMSG01Y.md) | COPAUS1C | cobol-program | COPY | inventory | app/cpy/CSMSG01Y.cpy | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:132` |
| [CSMSG01Y](../08-data/layouts/CSMSG01Y.md) | CORPT00C | cobol-program | COPY | inventory | app/cpy/CSMSG01Y.cpy | `app/cbl/CORPT00C.cbl:144` |
| [CSMSG01Y](../08-data/layouts/CSMSG01Y.md) | COSGN00C | cobol-program | COPY | inventory | app/cpy/CSMSG01Y.cpy | `app/cbl/COSGN00C.cbl:54` |
| [CSMSG01Y](../08-data/layouts/CSMSG01Y.md) | COTRN00C | cobol-program | COPY | inventory | app/cpy/CSMSG01Y.cpy | `app/cbl/COTRN00C.cbl:76` |
| [CSMSG01Y](../08-data/layouts/CSMSG01Y.md) | COTRN01C | cobol-program | COPY | inventory | app/cpy/CSMSG01Y.cpy | `app/cbl/COTRN01C.cbl:67` |
| [CSMSG01Y](../08-data/layouts/CSMSG01Y.md) | COTRN02C | cobol-program | COPY | inventory | app/cpy/CSMSG01Y.cpy | `app/cbl/COTRN02C.cbl:86` |
| [CSMSG01Y](../08-data/layouts/CSMSG01Y.md) | COTRTLIC | cobol-program | COPY | inventory | app/cpy/CSMSG01Y.cpy | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:482` |
| [CSMSG01Y](../08-data/layouts/CSMSG01Y.md) | COTRTUPC | cobol-program | COPY | inventory | app/cpy/CSMSG01Y.cpy | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:271` |
| [CSMSG01Y](../08-data/layouts/CSMSG01Y.md) | COUSR00C | cobol-program | COPY | inventory | app/cpy/CSMSG01Y.cpy | `app/cbl/COUSR00C.cbl:80` |
| [CSMSG01Y](../08-data/layouts/CSMSG01Y.md) | COUSR01C | cobol-program | COPY | inventory | app/cpy/CSMSG01Y.cpy | `app/cbl/COUSR01C.cbl:52` |
| [CSMSG01Y](../08-data/layouts/CSMSG01Y.md) | COUSR02C | cobol-program | COPY | inventory | app/cpy/CSMSG01Y.cpy | `app/cbl/COUSR02C.cbl:64` |
| [CSMSG01Y](../08-data/layouts/CSMSG01Y.md) | COUSR03C | cobol-program | COPY | inventory | app/cpy/CSMSG01Y.cpy | `app/cbl/COUSR03C.cbl:64` |
| [CSMSG02Y](../08-data/layouts/CSMSG02Y.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSMSG02Y.cpy | `app/cbl/COACTUPC.cbl:632` |
| [CSMSG02Y](../08-data/layouts/CSMSG02Y.md) | COACTVWC | cobol-program | COPY | inventory | app/cpy/CSMSG02Y.cpy | `app/cbl/COACTVWC.cbl:238` |
| [CSMSG02Y](../08-data/layouts/CSMSG02Y.md) | COCRDLIC | cobol-program | COPY | inventory (commented out) | app/cpy/CSMSG02Y.cpy | `app/cbl/COCRDLIC.cbl:283` |
| [CSMSG02Y](../08-data/layouts/CSMSG02Y.md) | COCRDSLC | cobol-program | COPY | inventory | app/cpy/CSMSG02Y.cpy | `app/cbl/COCRDSLC.cbl:224` |
| [CSMSG02Y](../08-data/layouts/CSMSG02Y.md) | COCRDUPC | cobol-program | COPY | inventory | app/cpy/CSMSG02Y.cpy | `app/cbl/COCRDUPC.cbl:343` |
| [CSMSG02Y](../08-data/layouts/CSMSG02Y.md) | COPAUS0C | cobol-program | COPY | inventory | app/cpy/CSMSG02Y.cpy | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:141` |
| [CSMSG02Y](../08-data/layouts/CSMSG02Y.md) | COPAUS1C | cobol-program | COPY | inventory | app/cpy/CSMSG02Y.cpy | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:135` |
| [CSMSG02Y](../08-data/layouts/CSMSG02Y.md) | COTRTUPC | cobol-program | COPY | inventory | app/cpy/CSMSG02Y.cpy | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:274` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3208-3211` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3214-3217` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3220-3223` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3226-3229` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3232-3235` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3238-3241` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3244-3247` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3250-3253` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3256-3259` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3262-3265` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3268-3271` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3274-3277` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3280-3283` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3286-3289` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3292-3295` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3298-3301` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3304-3307` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3310-3313` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3316-3319` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3322-3325` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3328-3331` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3334-3337` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3340-3343` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3346-3349` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3352-3355` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3358-3361` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3364-3367` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3370-3373` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3376-3379` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3382-3385` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3388-3391` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3394-3397` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3400-3403` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3405-3408` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3411-3414` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3417-3420` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3422-3425` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3427-3430` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/cbl/COACTUPC.cbl:3432-3435` |
| [CSSETATY](../08-data/layouts/CSSETATY.md) | COTRTUPC | cobol-program | COPY | inventory | app/cpy/CSSETATY.cpy | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1358-1361` |
| [CSSTRPFY](../08-data/layouts/CSSTRPFY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSSTRPFY.cpy | `app/cbl/COACTUPC.cbl:4199` |
| [CSSTRPFY](../08-data/layouts/CSSTRPFY.md) | COACTVWC | cobol-program | COPY | inventory | app/cpy/CSSTRPFY.cpy | `app/cbl/COACTVWC.cbl:913` |
| [CSSTRPFY](../08-data/layouts/CSSTRPFY.md) | COCRDLIC | cobol-program | COPY | inventory | app/cpy/CSSTRPFY.cpy | `app/cbl/COCRDLIC.cbl:1416` |
| [CSSTRPFY](../08-data/layouts/CSSTRPFY.md) | COCRDSLC | cobol-program | COPY | inventory | app/cpy/CSSTRPFY.cpy | `app/cbl/COCRDSLC.cbl:855` |
| [CSSTRPFY](../08-data/layouts/CSSTRPFY.md) | COCRDUPC | cobol-program | COPY | inventory | app/cpy/CSSTRPFY.cpy | `app/cbl/COCRDUPC.cbl:1528` |
| [CSSTRPFY](../08-data/layouts/CSSTRPFY.md) | COTRTLIC | cobol-program | COPY | inventory | app/cpy/CSSTRPFY.cpy | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:2060` |
| [CSSTRPFY](../08-data/layouts/CSSTRPFY.md) | COTRTUPC | cobol-program | COPY | inventory | app/cpy/CSSTRPFY.cpy | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1671` |
| [CSUSR01Y](../08-data/layouts/CSUSR01Y.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSUSR01Y.cpy | `app/cbl/COACTUPC.cbl:635` |
| [CSUSR01Y](../08-data/layouts/CSUSR01Y.md) | COACTVWC | cobol-program | COPY | inventory | app/cpy/CSUSR01Y.cpy | `app/cbl/COACTVWC.cbl:241` |
| [CSUSR01Y](../08-data/layouts/CSUSR01Y.md) | COADM01C | cobol-program | COPY | inventory | app/cpy/CSUSR01Y.cpy | `app/cbl/COADM01C.cbl:58` |
| [CSUSR01Y](../08-data/layouts/CSUSR01Y.md) | COCRDLIC | cobol-program | COPY | inventory | app/cpy/CSUSR01Y.cpy | `app/cbl/COCRDLIC.cbl:285` |
| [CSUSR01Y](../08-data/layouts/CSUSR01Y.md) | COCRDSLC | cobol-program | COPY | inventory | app/cpy/CSUSR01Y.cpy | `app/cbl/COCRDSLC.cbl:227` |
| [CSUSR01Y](../08-data/layouts/CSUSR01Y.md) | COCRDUPC | cobol-program | COPY | inventory | app/cpy/CSUSR01Y.cpy | `app/cbl/COCRDUPC.cbl:346` |
| [CSUSR01Y](../08-data/layouts/CSUSR01Y.md) | COMEN01C | cobol-program | COPY | inventory | app/cpy/CSUSR01Y.cpy | `app/cbl/COMEN01C.cbl:58` |
| [CSUSR01Y](../08-data/layouts/CSUSR01Y.md) | COSGN00C | cobol-program | COPY | inventory | app/cpy/CSUSR01Y.cpy | `app/cbl/COSGN00C.cbl:55` |
| [CSUSR01Y](../08-data/layouts/CSUSR01Y.md) | COTRTLIC | cobol-program | COPY | inventory | app/cpy/CSUSR01Y.cpy | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:485` |
| [CSUSR01Y](../08-data/layouts/CSUSR01Y.md) | COTRTUPC | cobol-program | COPY | inventory | app/cpy/CSUSR01Y.cpy | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:277` |
| [CSUSR01Y](../08-data/layouts/CSUSR01Y.md) | COUSR00C | cobol-program | COPY | inventory | app/cpy/CSUSR01Y.cpy | `app/cbl/COUSR00C.cbl:81` |
| [CSUSR01Y](../08-data/layouts/CSUSR01Y.md) | COUSR01C | cobol-program | COPY | inventory | app/cpy/CSUSR01Y.cpy | `app/cbl/COUSR01C.cbl:53` |
| [CSUSR01Y](../08-data/layouts/CSUSR01Y.md) | COUSR02C | cobol-program | COPY | inventory | app/cpy/CSUSR01Y.cpy | `app/cbl/COUSR02C.cbl:65` |
| [CSUSR01Y](../08-data/layouts/CSUSR01Y.md) | COUSR03C | cobol-program | COPY | inventory | app/cpy/CSUSR01Y.cpy | `app/cbl/COUSR03C.cbl:65` |
| [CSUTLDPY](../08-data/layouts/CSUTLDPY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSUTLDPY.cpy | `app/cbl/COACTUPC.cbl:4232` |
| [CSUTLDWY](../08-data/layouts/CSUTLDWY.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CSUTLDWY.cpy | `app/cbl/COACTUPC.cbl:166` |
| [CSUTLDWY](../08-data/layouts/CSUTLDWY.md) | COTRTUPC | cobol-program | COPY | inventory | app/cpy/CSUTLDWY.cpy | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:76` |
| [CUSTREC](../08-data/layouts/CUSTREC.md) | CBSTM03A | cobol-program | COPY | inventory | app/cpy/CUSTREC.cpy | `app/cbl/CBSTM03A.CBL:55` |
| [CVACT01Y](../08-data/layouts/CVACT01Y.md) | CBACT01C | cobol-program | COPY | inventory | app/cpy/CVACT01Y.cpy | `app/cbl/CBACT01C.cbl:89` |
| [CVACT01Y](../08-data/layouts/CVACT01Y.md) | CBACT04C | cobol-program | COPY | inventory | app/cpy/CVACT01Y.cpy | `app/cbl/CBACT04C.cbl:112` |
| [CVACT01Y](../08-data/layouts/CVACT01Y.md) | CBEXPORT | cobol-program | COPY | inventory | app/cpy/CVACT01Y.cpy | `app/cbl/CBEXPORT.cbl:78` |
| [CVACT01Y](../08-data/layouts/CVACT01Y.md) | CBIMPORT | cobol-program | COPY | inventory | app/cpy/CVACT01Y.cpy | `app/cbl/CBIMPORT.cbl:89` |
| [CVACT01Y](../08-data/layouts/CVACT01Y.md) | CBSTM03A | cobol-program | COPY | inventory | app/cpy/CVACT01Y.cpy | `app/cbl/CBSTM03A.CBL:57` |
| [CVACT01Y](../08-data/layouts/CVACT01Y.md) | CBTRN01C | cobol-program | COPY | inventory | app/cpy/CVACT01Y.cpy | `app/cbl/CBTRN01C.cbl:119` |
| [CVACT01Y](../08-data/layouts/CVACT01Y.md) | CBTRN02C | cobol-program | COPY | inventory | app/cpy/CVACT01Y.cpy | `app/cbl/CBTRN02C.cbl:121` |
| [CVACT01Y](../08-data/layouts/CVACT01Y.md) | COACCT01 | cobol-program | COPY | inventory | app/cpy/CVACT01Y.cpy | `app/app-vsam-mq/cbl/COACCT01.cbl:171` |
| [CVACT01Y](../08-data/layouts/CVACT01Y.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CVACT01Y.cpy | `app/cbl/COACTUPC.cbl:640` |
| [CVACT01Y](../08-data/layouts/CVACT01Y.md) | COACTVWC | cobol-program | COPY | inventory | app/cpy/CVACT01Y.cpy | `app/cbl/COACTVWC.cbl:244` |
| [CVACT01Y](../08-data/layouts/CVACT01Y.md) | COBIL00C | cobol-program | COPY | inventory | app/cpy/CVACT01Y.cpy | `app/cbl/COBIL00C.cbl:80` |
| [CVACT01Y](../08-data/layouts/CVACT01Y.md) | COCRDSLC | cobol-program | COPY | inventory (commented out) | app/cpy/CVACT01Y.cpy | `app/cbl/COCRDSLC.cbl:231` |
| [CVACT01Y](../08-data/layouts/CVACT01Y.md) | COCRDUPC | cobol-program | COPY | inventory (commented out) | app/cpy/CVACT01Y.cpy | `app/cbl/COCRDUPC.cbl:350` |
| [CVACT01Y](../08-data/layouts/CVACT01Y.md) | COPAUA0C | cobol-program | COPY | inventory | app/cpy/CVACT01Y.cpy | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:206` |
| [CVACT01Y](../08-data/layouts/CVACT01Y.md) | COPAUS0C | cobol-program | COPY | inventory | app/cpy/CVACT01Y.cpy | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:144` |
| [CVACT01Y](../08-data/layouts/CVACT01Y.md) | COTRN02C | cobol-program | COPY | inventory | app/cpy/CVACT01Y.cpy | `app/cbl/COTRN02C.cbl:89` |
| [CVACT02Y](../08-data/layouts/CVACT02Y.md) | CBACT02C | cobol-program | COPY | inventory | app/cpy/CVACT02Y.cpy | `app/cbl/CBACT02C.cbl:45` |
| [CVACT02Y](../08-data/layouts/CVACT02Y.md) | CBEXPORT | cobol-program | COPY | inventory | app/cpy/CVACT02Y.cpy | `app/cbl/CBEXPORT.cbl:87` |
| [CVACT02Y](../08-data/layouts/CVACT02Y.md) | CBIMPORT | cobol-program | COPY | inventory | app/cpy/CVACT02Y.cpy | `app/cbl/CBIMPORT.cbl:104` |
| [CVACT02Y](../08-data/layouts/CVACT02Y.md) | CBTRN01C | cobol-program | COPY | inventory | app/cpy/CVACT02Y.cpy | `app/cbl/CBTRN01C.cbl:114` |
| [CVACT02Y](../08-data/layouts/CVACT02Y.md) | COACTVWC | cobol-program | COPY | inventory | app/cpy/CVACT02Y.cpy | `app/cbl/COACTVWC.cbl:248` |
| [CVACT02Y](../08-data/layouts/CVACT02Y.md) | COCRDLIC | cobol-program | COPY | inventory | app/cpy/CVACT02Y.cpy | `app/cbl/COCRDLIC.cbl:290` |
| [CVACT02Y](../08-data/layouts/CVACT02Y.md) | COCRDSLC | cobol-program | COPY | inventory | app/cpy/CVACT02Y.cpy | `app/cbl/COCRDSLC.cbl:234` |
| [CVACT02Y](../08-data/layouts/CVACT02Y.md) | COCRDUPC | cobol-program | COPY | inventory | app/cpy/CVACT02Y.cpy | `app/cbl/COCRDUPC.cbl:353` |
| [CVACT02Y](../08-data/layouts/CVACT02Y.md) | COPAUS0C | cobol-program | COPY | inventory | app/cpy/CVACT02Y.cpy | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:147` |
| [CVACT02Y](../08-data/layouts/CVACT02Y.md) | COTRTLIC | cobol-program | COPY | inventory | app/cpy/CVACT02Y.cpy | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:490` |
| [CVACT03Y](../08-data/layouts/CVACT03Y.md) | CBACT03C | cobol-program | COPY | inventory | app/cpy/CVACT03Y.cpy | `app/cbl/CBACT03C.cbl:45` |
| [CVACT03Y](../08-data/layouts/CVACT03Y.md) | CBACT04C | cobol-program | COPY | inventory | app/cpy/CVACT03Y.cpy | `app/cbl/CBACT04C.cbl:102` |
| [CVACT03Y](../08-data/layouts/CVACT03Y.md) | CBEXPORT | cobol-program | COPY | inventory | app/cpy/CVACT03Y.cpy | `app/cbl/CBEXPORT.cbl:81` |
| [CVACT03Y](../08-data/layouts/CVACT03Y.md) | CBIMPORT | cobol-program | COPY | inventory | app/cpy/CVACT03Y.cpy | `app/cbl/CBIMPORT.cbl:94` |
| [CVACT03Y](../08-data/layouts/CVACT03Y.md) | CBSTM03A | cobol-program | COPY | inventory | app/cpy/CVACT03Y.cpy | `app/cbl/CBSTM03A.CBL:53` |
| [CVACT03Y](../08-data/layouts/CVACT03Y.md) | CBTRN01C | cobol-program | COPY | inventory | app/cpy/CVACT03Y.cpy | `app/cbl/CBTRN01C.cbl:109` |
| [CVACT03Y](../08-data/layouts/CVACT03Y.md) | CBTRN02C | cobol-program | COPY | inventory | app/cpy/CVACT03Y.cpy | `app/cbl/CBTRN02C.cbl:112` |
| [CVACT03Y](../08-data/layouts/CVACT03Y.md) | CBTRN03C | cobol-program | COPY | inventory | app/cpy/CVACT03Y.cpy | `app/cbl/CBTRN03C.cbl:98` |
| [CVACT03Y](../08-data/layouts/CVACT03Y.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CVACT03Y.cpy | `app/cbl/COACTUPC.cbl:643` |
| [CVACT03Y](../08-data/layouts/CVACT03Y.md) | COACTVWC | cobol-program | COPY | inventory | app/cpy/CVACT03Y.cpy | `app/cbl/COACTVWC.cbl:251` |
| [CVACT03Y](../08-data/layouts/CVACT03Y.md) | COBIL00C | cobol-program | COPY | inventory | app/cpy/CVACT03Y.cpy | `app/cbl/COBIL00C.cbl:81` |
| [CVACT03Y](../08-data/layouts/CVACT03Y.md) | COCRDSLC | cobol-program | COPY | inventory (commented out) | app/cpy/CVACT03Y.cpy | `app/cbl/COCRDSLC.cbl:237` |
| [CVACT03Y](../08-data/layouts/CVACT03Y.md) | COCRDUPC | cobol-program | COPY | inventory (commented out) | app/cpy/CVACT03Y.cpy | `app/cbl/COCRDUPC.cbl:356` |
| [CVACT03Y](../08-data/layouts/CVACT03Y.md) | COPAUA0C | cobol-program | COPY | inventory | app/cpy/CVACT03Y.cpy | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:203` |
| [CVACT03Y](../08-data/layouts/CVACT03Y.md) | COPAUS0C | cobol-program | COPY | inventory | app/cpy/CVACT03Y.cpy | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:150` |
| [CVACT03Y](../08-data/layouts/CVACT03Y.md) | COTRN02C | cobol-program | COPY | inventory | app/cpy/CVACT03Y.cpy | `app/cbl/COTRN02C.cbl:90` |
| [CVCRD01Y](../08-data/layouts/CVCRD01Y.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CVCRD01Y.cpy | `app/cbl/COACTUPC.cbl:597` |
| [CVCRD01Y](../08-data/layouts/CVCRD01Y.md) | COACTVWC | cobol-program | COPY | inventory | app/cpy/CVCRD01Y.cpy | `app/cbl/COACTVWC.cbl:207` |
| [CVCRD01Y](../08-data/layouts/CVCRD01Y.md) | COCRDLIC | cobol-program | COPY | inventory | app/cpy/CVCRD01Y.cpy | `app/cbl/COCRDLIC.cbl:221` |
| [CVCRD01Y](../08-data/layouts/CVCRD01Y.md) | COCRDSLC | cobol-program | COPY | inventory | app/cpy/CVCRD01Y.cpy | `app/cbl/COCRDSLC.cbl:194` |
| [CVCRD01Y](../08-data/layouts/CVCRD01Y.md) | COCRDUPC | cobol-program | COPY | inventory | app/cpy/CVCRD01Y.cpy | `app/cbl/COCRDUPC.cbl:268` |
| [CVCRD01Y](../08-data/layouts/CVCRD01Y.md) | COTRTLIC | cobol-program | COPY | inventory | app/cpy/CVCRD01Y.cpy | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:327` |
| [CVCRD01Y](../08-data/layouts/CVCRD01Y.md) | COTRTUPC | cobol-program | COPY | inventory | app/cpy/CVCRD01Y.cpy | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:241` |
| [CVCUS01Y](../08-data/layouts/CVCUS01Y.md) | CBCUS01C | cobol-program | COPY | inventory | app/cpy/CVCUS01Y.cpy | `app/cbl/CBCUS01C.cbl:45` |
| [CVCUS01Y](../08-data/layouts/CVCUS01Y.md) | CBEXPORT | cobol-program | COPY | inventory | app/cpy/CVCUS01Y.cpy | `app/cbl/CBEXPORT.cbl:75` |
| [CVCUS01Y](../08-data/layouts/CVCUS01Y.md) | CBIMPORT | cobol-program | COPY | inventory | app/cpy/CVCUS01Y.cpy | `app/cbl/CBIMPORT.cbl:84` |
| [CVCUS01Y](../08-data/layouts/CVCUS01Y.md) | CBTRN01C | cobol-program | COPY | inventory | app/cpy/CVCUS01Y.cpy | `app/cbl/CBTRN01C.cbl:104` |
| [CVCUS01Y](../08-data/layouts/CVCUS01Y.md) | COACTUPC | cobol-program | COPY | inventory | app/cpy/CVCUS01Y.cpy | `app/cbl/COACTUPC.cbl:646` |
| [CVCUS01Y](../08-data/layouts/CVCUS01Y.md) | COACTVWC | cobol-program | COPY | inventory | app/cpy/CVCUS01Y.cpy | `app/cbl/COACTVWC.cbl:254` |
| [CVCUS01Y](../08-data/layouts/CVCUS01Y.md) | COCRDSLC | cobol-program | COPY | inventory | app/cpy/CVCUS01Y.cpy | `app/cbl/COCRDSLC.cbl:240` |
| [CVCUS01Y](../08-data/layouts/CVCUS01Y.md) | COCRDUPC | cobol-program | COPY | inventory | app/cpy/CVCUS01Y.cpy | `app/cbl/COCRDUPC.cbl:359` |
| [CVCUS01Y](../08-data/layouts/CVCUS01Y.md) | COPAUA0C | cobol-program | COPY | inventory | app/cpy/CVCUS01Y.cpy | `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:209` |
| [CVCUS01Y](../08-data/layouts/CVCUS01Y.md) | COPAUS0C | cobol-program | COPY | inventory | app/cpy/CVCUS01Y.cpy | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:153` |
| [CVEXPORT](../08-data/layouts/CVEXPORT.md) | CBEXPORT | cobol-program | COPY | inventory | app/cpy/CVEXPORT.cpy | `app/cbl/CBEXPORT.cbl:96` |
| [CVEXPORT](../08-data/layouts/CVEXPORT.md) | CBIMPORT | cobol-program | COPY | inventory | app/cpy/CVEXPORT.cpy | `app/cbl/CBIMPORT.cbl:113` |
| [CVTRA01Y](../08-data/layouts/CVTRA01Y.md) | CBACT04C | cobol-program | COPY | inventory | app/cpy/CVTRA01Y.cpy | `app/cbl/CBACT04C.cbl:97` |
| [CVTRA01Y](../08-data/layouts/CVTRA01Y.md) | CBTRN02C | cobol-program | COPY | inventory | app/cpy/CVTRA01Y.cpy | `app/cbl/CBTRN02C.cbl:126` |
| [CVTRA02Y](../08-data/layouts/CVTRA02Y.md) | CBACT04C | cobol-program | COPY | inventory | app/cpy/CVTRA02Y.cpy | `app/cbl/CBACT04C.cbl:107` |
| [CVTRA03Y](../08-data/layouts/CVTRA03Y.md) | CBTRN03C | cobol-program | COPY | inventory | app/cpy/CVTRA03Y.cpy | `app/cbl/CBTRN03C.cbl:103` |
| [CVTRA04Y](../08-data/layouts/CVTRA04Y.md) | CBTRN03C | cobol-program | COPY | inventory | app/cpy/CVTRA04Y.cpy | `app/cbl/CBTRN03C.cbl:108` |
| [CVTRA05Y](../08-data/layouts/CVTRA05Y.md) | CBACT04C | cobol-program | COPY | inventory | app/cpy/CVTRA05Y.cpy | `app/cbl/CBACT04C.cbl:117` |
| [CVTRA05Y](../08-data/layouts/CVTRA05Y.md) | CBEXPORT | cobol-program | COPY | inventory | app/cpy/CVTRA05Y.cpy | `app/cbl/CBEXPORT.cbl:84` |
| [CVTRA05Y](../08-data/layouts/CVTRA05Y.md) | CBIMPORT | cobol-program | COPY | inventory | app/cpy/CVTRA05Y.cpy | `app/cbl/CBIMPORT.cbl:99` |
| [CVTRA05Y](../08-data/layouts/CVTRA05Y.md) | CBTRN01C | cobol-program | COPY | inventory | app/cpy/CVTRA05Y.cpy | `app/cbl/CBTRN01C.cbl:124` |
| [CVTRA05Y](../08-data/layouts/CVTRA05Y.md) | CBTRN02C | cobol-program | COPY | inventory | app/cpy/CVTRA05Y.cpy | `app/cbl/CBTRN02C.cbl:107` |
| [CVTRA05Y](../08-data/layouts/CVTRA05Y.md) | CBTRN03C | cobol-program | COPY | inventory | app/cpy/CVTRA05Y.cpy | `app/cbl/CBTRN03C.cbl:93` |
| [CVTRA05Y](../08-data/layouts/CVTRA05Y.md) | COBIL00C | cobol-program | COPY | inventory | app/cpy/CVTRA05Y.cpy | `app/cbl/COBIL00C.cbl:82` |
| [CVTRA05Y](../08-data/layouts/CVTRA05Y.md) | CORPT00C | cobol-program | COPY | inventory | app/cpy/CVTRA05Y.cpy | `app/cbl/CORPT00C.cbl:146` |
| [CVTRA05Y](../08-data/layouts/CVTRA05Y.md) | COTRN00C | cobol-program | COPY | inventory | app/cpy/CVTRA05Y.cpy | `app/cbl/COTRN00C.cbl:78` |
| [CVTRA05Y](../08-data/layouts/CVTRA05Y.md) | COTRN01C | cobol-program | COPY | inventory | app/cpy/CVTRA05Y.cpy | `app/cbl/COTRN01C.cbl:69` |
| [CVTRA05Y](../08-data/layouts/CVTRA05Y.md) | COTRN02C | cobol-program | COPY | inventory | app/cpy/CVTRA05Y.cpy | `app/cbl/COTRN02C.cbl:88` |
| [CVTRA06Y](../08-data/layouts/CVTRA06Y.md) | CBTRN01C | cobol-program | COPY | inventory | app/cpy/CVTRA06Y.cpy | `app/cbl/CBTRN01C.cbl:99` |
| [CVTRA06Y](../08-data/layouts/CVTRA06Y.md) | CBTRN02C | cobol-program | COPY | inventory | app/cpy/CVTRA06Y.cpy | `app/cbl/CBTRN02C.cbl:102` |
| [CVTRA07Y](../08-data/layouts/CVTRA07Y.md) | CBTRN03C | cobol-program | COPY | inventory | app/cpy/CVTRA07Y.cpy | `app/cbl/CBTRN03C.cbl:113` |
| [DCLTRCAT](../08-data/layouts/DCLTRCAT.md) | COTRTUPC | cobol-program | EXEC SQL INCLUDE | inventory | app/app-transaction-type-db2/dcl/DCLTRCAT.dcl | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:288` |
| [DCLTRTYP](../08-data/layouts/DCLTRTYP.md) | COBTUPDT | cobol-program | EXEC SQL INCLUDE | inventory | app/app-transaction-type-db2/dcl/DCLTRTYP.dcl | `app/app-transaction-type-db2/cbl/COBTUPDT.cbl:54` |
| [DCLTRTYP](../08-data/layouts/DCLTRTYP.md) | COTRTLIC | cobol-program | EXEC SQL INCLUDE | inventory | app/app-transaction-type-db2/dcl/DCLTRTYP.dcl | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:333` |
| [DCLTRTYP](../08-data/layouts/DCLTRTYP.md) | COTRTUPC | cobol-program | EXEC SQL INCLUDE | inventory | app/app-transaction-type-db2/dcl/DCLTRTYP.dcl | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:286` |
| DFHAID | COACTUPC | cobol-program | COPY | system |  | `app/cbl/COACTUPC.cbl:616` |
| DFHAID | COACTVWC | cobol-program | COPY | system |  | `app/cbl/COACTVWC.cbl:222` |
| DFHAID | COADM01C | cobol-program | COPY | system |  | `app/cbl/COADM01C.cbl:60` |
| DFHAID | COBIL00C | cobol-program | COPY | system |  | `app/cbl/COBIL00C.cbl:84` |
| DFHAID | COCRDLIC | cobol-program | COPY | system |  | `app/cbl/COCRDLIC.cbl:268` |
| DFHAID | COCRDSLC | cobol-program | COPY | system |  | `app/cbl/COCRDSLC.cbl:209` |
| DFHAID | COCRDUPC | cobol-program | COPY | system |  | `app/cbl/COCRDUPC.cbl:328` |
| DFHAID | COMEN01C | cobol-program | COPY | system |  | `app/cbl/COMEN01C.cbl:60` |
| DFHAID | COPAUS0C | cobol-program | COPY | system |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:168` |
| DFHAID | COPAUS1C | cobol-program | COPY | system |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:148` |
| DFHAID | CORPT00C | cobol-program | COPY | system |  | `app/cbl/CORPT00C.cbl:148` |
| DFHAID | COSGN00C | cobol-program | COPY | system |  | `app/cbl/COSGN00C.cbl:57` |
| DFHAID | COTRN00C | cobol-program | COPY | system |  | `app/cbl/COTRN00C.cbl:80` |
| DFHAID | COTRN01C | cobol-program | COPY | system |  | `app/cbl/COTRN01C.cbl:71` |
| DFHAID | COTRN02C | cobol-program | COPY | system |  | `app/cbl/COTRN02C.cbl:92` |
| DFHAID | COTRTLIC | cobol-program | COPY | system |  | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:426` |
| DFHAID | COTRTUPC | cobol-program | COPY | system |  | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:258` |
| DFHAID | COUSR00C | cobol-program | COPY | system |  | `app/cbl/COUSR00C.cbl:83` |
| DFHAID | COUSR01C | cobol-program | COPY | system |  | `app/cbl/COUSR01C.cbl:55` |
| DFHAID | COUSR02C | cobol-program | COPY | system |  | `app/cbl/COUSR02C.cbl:67` |
| DFHAID | COUSR03C | cobol-program | COPY | system |  | `app/cbl/COUSR03C.cbl:67` |
| DFHATTR | COSGN00C | cobol-program | COPY | system (commented out) |  | `app/cbl/COSGN00C.cbl:59` |
| DFHATTR | COUSR01C | cobol-program | COPY | system (commented out) |  | `app/cbl/COUSR01C.cbl:57` |
| DFHBMSCA | COACTUPC | cobol-program | COPY | system |  | `app/cbl/COACTUPC.cbl:615` |
| DFHBMSCA | COACTVWC | cobol-program | COPY | system |  | `app/cbl/COACTVWC.cbl:221` |
| DFHBMSCA | COADM01C | cobol-program | COPY | system |  | `app/cbl/COADM01C.cbl:61` |
| DFHBMSCA | COBIL00C | cobol-program | COPY | system |  | `app/cbl/COBIL00C.cbl:85` |
| DFHBMSCA | COCRDLIC | cobol-program | COPY | system |  | `app/cbl/COCRDLIC.cbl:267` |
| DFHBMSCA | COCRDSLC | cobol-program | COPY | system |  | `app/cbl/COCRDSLC.cbl:208` |
| DFHBMSCA | COCRDUPC | cobol-program | COPY | system |  | `app/cbl/COCRDUPC.cbl:327` |
| DFHBMSCA | COMEN01C | cobol-program | COPY | system |  | `app/cbl/COMEN01C.cbl:61` |
| DFHBMSCA | COPAUS0C | cobol-program | COPY | system |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:169` |
| DFHBMSCA | COPAUS1C | cobol-program | COPY | system |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:149` |
| DFHBMSCA | COPAUS2C | cobol-program | COPY | system (commented out) |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:61` |
| DFHBMSCA | CORPT00C | cobol-program | COPY | system |  | `app/cbl/CORPT00C.cbl:149` |
| DFHBMSCA | COSGN00C | cobol-program | COPY | system |  | `app/cbl/COSGN00C.cbl:58` |
| DFHBMSCA | COTRN00C | cobol-program | COPY | system |  | `app/cbl/COTRN00C.cbl:81` |
| DFHBMSCA | COTRN01C | cobol-program | COPY | system |  | `app/cbl/COTRN01C.cbl:72` |
| DFHBMSCA | COTRN02C | cobol-program | COPY | system |  | `app/cbl/COTRN02C.cbl:93` |
| DFHBMSCA | COTRTLIC | cobol-program | COPY | system |  | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:425` |
| DFHBMSCA | COTRTUPC | cobol-program | COPY | system |  | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:257` |
| DFHBMSCA | COUSR00C | cobol-program | COPY | system |  | `app/cbl/COUSR00C.cbl:84` |
| DFHBMSCA | COUSR01C | cobol-program | COPY | system |  | `app/cbl/COUSR01C.cbl:56` |
| DFHBMSCA | COUSR02C | cobol-program | COPY | system |  | `app/cbl/COUSR02C.cbl:68` |
| DFHBMSCA | COUSR03C | cobol-program | COPY | system |  | `app/cbl/COUSR03C.cbl:68` |
| [IMSFUNCS](../08-data/layouts/IMSFUNCS.md) | DBUNLDGS | cobol-program | COPY | inventory | app/app-authorization-ims-db2-mq/cpy/IMSFUNCS.cpy | `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:136` |
| [IMSFUNCS](../08-data/layouts/IMSFUNCS.md) | PAUDBLOD | cobol-program | COPY | inventory | app/app-authorization-ims-db2-mq/cpy/IMSFUNCS.cpy | `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:142` |
| [IMSFUNCS](../08-data/layouts/IMSFUNCS.md) | PAUDBUNL | cobol-program | COPY | inventory | app/app-authorization-ims-db2-mq/cpy/IMSFUNCS.cpy | `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:132` |
| [PADFLPCB](../08-data/layouts/PADFLPCB.md) | DBUNLDGS | cobol-program | COPY | inventory | app/app-authorization-ims-db2-mq/cpy/PADFLPCB.CPY | `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:156` |
| [PASFLPCB](../08-data/layouts/PASFLPCB.md) | DBUNLDGS | cobol-program | COPY | inventory | app/app-authorization-ims-db2-mq/cpy/PASFLPCB.CPY | `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:155` |
| [PAUTBPCB](../08-data/layouts/PAUTBPCB.md) | DBUNLDGS | cobol-program | COPY | inventory | app/app-authorization-ims-db2-mq/cpy/PAUTBPCB.CPY | `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:154` |
| [PAUTBPCB](../08-data/layouts/PAUTBPCB.md) | PAUDBLOD | cobol-program | COPY | inventory | app/app-authorization-ims-db2-mq/cpy/PAUTBPCB.CPY | `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:161` |
| [PAUTBPCB](../08-data/layouts/PAUTBPCB.md) | PAUDBUNL | cobol-program | COPY | inventory | app/app-authorization-ims-db2-mq/cpy/PAUTBPCB.CPY | `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:150` |
| SQLCA | COBTUPDT | cobol-program | EXEC SQL INCLUDE | system |  | `app/app-transaction-type-db2/cbl/COBTUPDT.cbl:50-52` |
| SQLCA | COPAUS2C | cobol-program | EXEC SQL INCLUDE | system |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:65-67` |
| SQLCA | COTRTLIC | cobol-program | EXEC SQL INCLUDE | system |  | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:331` |
| SQLCA | COTRTUPC | cobol-program | EXEC SQL INCLUDE | system |  | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:282-284` |

## Sources

- `docs/_work/structure/copybook-usage.json`

## Confidence

Confirmed: parsed from source.
