# Executive summary

## Purpose of the application

CardDemo is a sample credit-card servicing application. A person signs on with a user id and a password. An administrator receives a different menu from other users. Online screens maintain accounts, cards, customers, users, and transactions. Batch jobs post transactions, calculate interest, and refresh files.

The sign-on screen text calls it a credit card demo application (`app/bms/COSGN00.bms`, mockup in [COSGN00](05-online/screens/COSGN00.md)).

## Users and roles

| Role | How identified | Main capabilities | Evidence |
|---|---|---|---|
| Administrator | User type A | Admin menu COADM01C | app/cpy/COCOM01Y.cpy:27 |
| User | User type U | User menu. Options marked admin-only are refused. | app/cpy/COCOM01Y.cpy:28 |

## Business capabilities

| Capability | Channel | Key components | Details |
|---|---|---|---|
| Sign on | Online | CC00 COSGN00C | [Transactions](05-online/transaction-catalog.md) |
| Account, card, and customer maintenance | Online | Menu programs | [Programs](07-programs/index.md) |
| Post transactions and calculate interest | Batch | POSTTRAN INTCALC | [Jobs](06-batch/job-catalog.md) |
| Transaction types in DB2 | Online and batch | COTRTUPC COBTUPDT | [Rules](09-business-rules-catalog.md) |
| Pending authorization expiry | Batch IMS | CBPAUP0C | [Rules](09-business-rules-catalog.md) |
| Account and date replies | Message | COACCT01 CODATE01 | [Interfaces](10-integration-interfaces.md) |

## Key business objects

Account, card, customer, card cross-reference, and authorization-fraud rows are the entities with a cited field or key. See [data model](08-data/data-model.md).

## Size and composition

| Measure | Value |
|---|---|
| Inventory files | 331 |
| Program facts | 46 |
| Non-comment lines on program facts | 26341 |
| Transactions | 25 |
| Mapsets | 21 |
| JCL jobs | 55 |
| Dataset pages | 204 |
| Business rules | 50 |
| Interfaces | 14 |

## Optional modules

Authorization (IMS, DB2, MQ), transaction-type DB2, and VSAM-MQ are separate source trees. File counts are in the architecture page.

## Notable findings

- CBTRN01C has no caller, job, or transaction. See [gaps](16-gaps-assumptions-open-questions.md).
- CICS transaction definitions set resource and command security off. DB2 grants in the create script are to PUBLIC. See [security](11-security-access.md).
- Several record layouts share a length, so they are not tied to one dataset.
- No database description gen job is in the repository.

## Sources

- `docs/_work/inventory.json`
- `docs/_work/programs/`
- `app/bms/COSGN00.bms`
- `app/cpy/COCOM01Y.cpy:27`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
