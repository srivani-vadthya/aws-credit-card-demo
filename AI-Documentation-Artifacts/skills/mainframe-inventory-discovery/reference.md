# Discovery Reference

## Artifact taxonomy (`type` values)

| type | Meaning |
|---|---|
| cobol-program | Compilable COBOL (has PROCEDURE DIVISION / PROGRAM-ID) |
| cobol-copybook | COBOL data/procedure fragment for COPY |
| bms-symbolic-map | Copybook generated from a BMS mapset (fields with L/F/A/I/O suffixes) |
| db2-dclgen | DCLGEN: EXEC SQL DECLARE TABLE + host structure |
| pli-program / pli-include | PL/I source (extend signatures when found) |
| asm-program | Assembler source (CSECT, START, AMODE/RMODE) |
| asm-macro | Assembler macro definition (MACRO ... MEND) |
| asm-copybook | Assembler COPY member with DSECTs/EQUs only (no CSECT) |
| bms-mapset | BMS macro source (DFHMSD/DFHMDI/DFHMDF) |
| cics-csd | CSD / RDO definitions (DEFINE ... GROUP) |
| jcl-job | JCL with a JOB card |
| jcl-proc | Cataloged procedure (PROC without JOB) |
| jcl-template | JCL with template placeholders meant for generation |
| control-cards | Utility input (IDCAMS, SORT, SQL, DSN commands) without JCL |
| ims-dbd / ims-psb | IMS database / program specification definitions |
| db2-ddl | SQL DDL |
| mq-definition | MQSC definitions (DEFINE QLOCAL/QREMOTE/PROCESS) |
| scheduler-ca7 / scheduler-controlm / scheduler-other | Scheduler exports |
| script-shell / script-rexx / script-awk | Automation scripts |
| catalog-listing | IDCAMS LISTCAT or similar catalog report |
| data-text / data-binary | Sample/test data (ASCII text / EBCDIC or binary) |
| documentation / diagram / archive / repo-meta / placeholder | Non-source |
| unclassified | No signature matched - must be resolved |

## Signature principles

- Signatures are regexes over the upper-cased first 64 KB of the file, with
  `MULTILINE`. Content signatures run before extension hints.
- Order specific before generic: `bms-symbolic-map` and `db2-dclgen` before
  `cobol-copybook`; `jcl-job` before `jcl-proc`; `cics-csd` before
  `control-cards`.
- Binary detection: NUL bytes, or more than 30% of bytes outside printable
  ASCII. EBCDIC hint: high share of bytes 0x40 (space) and 0xC1-0xE9
  (letters) with few ASCII letters.

## System / vendor members (not application code)

- CICS: DFHAID, DFHBMSCA, DFHATTR, DFHEIBLK, DFHCOMMAREA, DFHRESP, DFHVALUE
- DB2: SQLCA, SQLDA, DSNTEP2/4, DSNTIAUL, DSNTIAR, DSNHPC, DSNUTILB
- IMS: CBLTDLI, AIBTDLI, DFSRRC00, DFSURGU0/DFSURGL0, DFSUDMP0, DLITCBL
- MQ: CMQV, CMQODV, CMQMDV, CMQGMOV, CMQPMOV, CMQTML, MQCONN/MQOPEN/MQGET/
  MQPUT/MQPUT1/MQCLOSE/MQDISC/MQINQ
- LE / runtime: CEE3ABD, CEEDAYS, CEELOCT, CEEDATM, CEEGMT, IGZEBST,
  ILBOABN0
- z/OS utilities: IDCAMS, IEBGENER, IEBCOPY, IEFBR14, IEBPTPCH, IKJEFT01,
  IKJEFT1B, SORT/DFSORT/SYNCSORT/ICETOOL/ICEMAN, IGYCRCTL, ASMA90, HEWL,
  IEWL, IEWBLINK, DFHECP1$/DFHECP1, DFHCSDUP, SDSF, FTP, IRXJCL, TXT2PDF

Unknown names are never assumed to be system members; add them here only
with evidence (vendor documentation or JCL STEPLIB pointing outside the
application).

## Technology evidence signals

| Technology | Signals |
|---|---|
| CICS | `EXEC CICS`, CSD file, DFHCOMMAREA, DFHECP1 translator step |
| BMS | DFHMSD, symbolic map copybooks |
| VSAM | IDCAMS DEFINE CLUSTER/AIX/PATH, `ORGANIZATION IS INDEXED/RELATIVE`, CSD FILE |
| GDG | IDCAMS DEFINE GDG, `DSN=...(+1)` |
| DB2 | `EXEC SQL`, DDL, DCLGEN, DSN commands, DB2ENTRY |
| IMS DB | DBD/PSB, `EXEC DLI`, `CALL 'CBLTDLI'`, DFSRRC00 |
| IMS DC | `CALL 'CBLTDLI'` with IO-PCB GU/ISRT, MFS sources |
| MQ | MQOPEN/MQGET/MQPUT calls, CMQ* copybooks, MQSC |
| Batch sort | SORT/ICETOOL steps, `SORT` verb in COBOL |
| Internal reader / FTP | `SYSOUT=(A,INTRDR)`, TDQ to INTRDR, FTP steps |
