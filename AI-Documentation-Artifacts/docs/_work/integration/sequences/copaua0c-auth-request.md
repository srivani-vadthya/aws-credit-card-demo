# COPAUA0C authorization request

Evidence: `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:238`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:293`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:354-374`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:413-414`, `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:620`.

```mermaid
sequenceDiagram
    participant Trigger as MQ trigger
    participant Task as COPAUA0C
    participant InQ as Request queue
    participant IMS as DBPAUTP0
    participant Reply as ReplyToQ
    Trigger->>Task: Start CP00
    Task->>Task: RETRIEVE MQTM-QNAME
    Task->>IMS: EXEC DLI SCHD PSBPAUTB
    Task->>InQ: MQGET
    InQ-->>Task: comma-separated authorization fields
    Task->>Task: UNSTRING DELIMITED BY comma
    Task->>IMS: GU, REPL, or ISRT
    Task->>Reply: MQPUT to MQMD-REPLYTOQ
```
