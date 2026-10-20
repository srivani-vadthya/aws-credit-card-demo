# Security and access

## Authentication

Transaction CC00 starts COSGN00C. The password field SEC-USR-PWD is PIC X(08). Sign-on upper-cases the entered user id and password, then compares the password for equality. The BMS password field is dark. No lockout counter is present in the sign-on EVALUATE.

| Role | Identified by | Enforcement | Evidence |
|---|---|---|---|
| admin | CDEMO-USRTYP-ADMIN VALUE 'A' | After a matching password, COSGN00C transfers to COADM01C. | app/cpy/COCOM01Y.cpy:27 |
| user | CDEMO-USRTYP-USER VALUE 'U' | A non-admin match transfers to COMEN01C. On that menu, a user-type U session is refused an option whose table user type is A. | app/cpy/COCOM01Y.cpy:28 |

## Platform security

| Mechanism | Definition | Evidence |
|---|---|---|
| CICS transaction security attributes | RESSEC(NO) CMDSEC(NO) | app/csd/CARDDEMO.CSD:314, app/app-vsam-mq/csd/CRDDEMOM.csd:24, app/app-transaction-type-db2/csd/CRDDEMOD.csd:32, app/app-authorization-ims-db2-mq/csd/CRDDEMO2.csd:46 |
| DB2 GRANT | GRANT DBADM ON DATABASE CARDDEMO TO PUBLIC; GRANT USE OF TABLESPACE CARDDEMO.CARDSPC1 TO PUBLIC; GRANT DELETE, INSERT, SELECT, UPDATE on CARDDEMO.TRANSACTION_TYPE and CARDDEMO.TRANSACTION_TYPE_CATEGORY TO PUBLIC. | app/app-transaction-type-db2/ctl/DB2CREAT.ctl:52-59, app/app-transaction-type-db2/ctl/DB2CREAT.ctl:103-105 |
| RACF sample commands | RACFCMDS runs IKJEFT01. SYSIN contains RALT GCICSTRN CARD ADDMEM(CT02) and CONNECT of one user to GROUP(M2APPDEV). No ADDUSER, PERMIT, or RDEFINE of a data-set profile is in that job. | samples/jcl/RACFCMDS.jcl:19, samples/jcl/RACFCMDS.jcl:24, samples/jcl/RACFCMDS.jcl:29 |
| Catalog RACF flag | The point-in-time LISTCAT shows RACF----------------(NO) on listed clusters. Example line 43. This is the catalog as of 09/01/22, not a RACF rule. | app/catlg/LISTCAT.txt:43 |
| MQ authority | No MQ set-authority command was found. |  |

## Observations

- Sign-on stores the user type from SEC-USR-TYPE into CDEMO-USER-TYPE and branches only on the value A.
- The user menu refuses an option marked A when the commarea user type is U, with message 'No access - Admin Only option... '.
- DB2 privileges in DB2CREAT.ctl are granted to PUBLIC.
- CICS resource and command security are set to NO on the transaction definitions that were read.

COADM01C does not test the admin user type. The admin menu is reached by the sign-on transfer.

A new-user password is stored from the screen field without UPPER-CASE (`app/cbl/COUSR01C.cbl:157`).

## Sources

- `docs/_work/ops/security.json`
- `app/cbl/COSGN00C.cbl:132-136`
- `app/cbl/COSGN00C.cbl:223`
- `app/cpy/CSUSR01Y.cpy:21`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
