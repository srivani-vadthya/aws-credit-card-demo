# COBTUPDT transaction-type maintenance

Evidence: `app/app-transaction-type-db2/jcl/MNTTRDB2.jcl:30`, `app/app-transaction-type-db2/cbl/COBTUPDT.cbl:111-119`, `app/app-transaction-type-db2/cbl/COBTUPDT.cbl:137`, `app/app-transaction-type-db2/cbl/COBTUPDT.cbl:171`, `app/app-transaction-type-db2/cbl/COBTUPDT.cbl:201`.

```mermaid
sequenceDiagram
    participant JCL as MNTTRDB2
    participant Pgm as COBTUPDT
    participant DB2 as CARDDEMO.TRANSACTION_TYPE
    JCL->>Pgm: RUN PROGRAM PLAN CARDDEMO
    Pgm->>Pgm: Read input row action
    alt action A
        Pgm->>DB2: INSERT
    else action U
        Pgm->>DB2: UPDATE
    else action D
        Pgm->>DB2: DELETE
    end
    Pgm->>Pgm: SQLCODE zero, +100, or less than zero
```
