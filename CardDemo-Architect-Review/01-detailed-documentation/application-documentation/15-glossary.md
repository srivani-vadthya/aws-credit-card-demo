# Glossary

| Term | Meaning in this package |
|---|---|
| CICS | Online transaction monitor. Transactions and files are defined in CSD members. |
| BMS | Basic Mapping Support. Screen layouts in mapset source. |
| VSAM KSDS | Keyed VSAM cluster. Account, card, customer, and user-security files use this organisation. |
| AIX | Alternate index over a VSAM cluster. |
| GDG | Generation data group. Relative names such as (+1) appear on some DD statements. |
| DB2 | Relational database. Transaction-type tables use schema CARDDEMO as a literal. |
| IMS | Hierarchical database. Pending authorizations use DBD DBPAUTP0. |
| MQ | Message queues. Some queue names are literals and the trigger queue name is supplied at runtime. |
| COMMAREA | CICS communication area. Layout name CARDDEMO-COMMAREA. |
| JCL | Job control language for batch jobs. |
| CA7 | Scheduler export CardDemo.ca7. Kept separate from Control-M. |
| Control-M | Scheduler export CardDemo.controlm. Kept separate from CA7. |
| Confirmed | The statement is in the code or definition cited. |
| Inferred | The statement is reasoned from several cited facts. |
| Unverified | The statement comes from a comment, README, or diagram. |

## Sources

- `docs/_work/inventory.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
