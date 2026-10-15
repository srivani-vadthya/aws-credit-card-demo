# CBPAUP0C checkpoint

Evidence: `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:25`, `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:201-205`, `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:223`, `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:310`, `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:355`.

```mermaid
sequenceDiagram
    participant Job as CBPAUP0J
    participant Pgm as CBPAUP0C
    participant IMS as DBPAUTP0
    Job->>Pgm: BMP PSBPAUTB
    loop summaries
        Pgm->>IMS: GN / GNP
        Pgm->>IMS: DLET expired authorization
        alt count above checkpoint frequency
            Pgm->>IMS: CHKP
        end
    end
```
