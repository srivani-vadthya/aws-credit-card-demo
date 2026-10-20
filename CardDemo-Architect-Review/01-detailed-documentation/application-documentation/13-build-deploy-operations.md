# Build, deploy and operations

## Build chains

| Source type | PROC member | Steps | Evidence |
|---|---|---|---|
| batch-cobol | BUILDBAT | COMPILE IGYCRCTL, CBLPRINT IEBGENER, LKED HEWL | samples/proc/BUILDBAT.prc:24 |
| cics-cobol | BUILDONL | COB IGYCRCTL, DISPLIST IEBGENER, COPYLINK IEBGENER, LKED HEWL | samples/proc/BUILDONL.prc:25 |
| cics-db2-cobol | BLDCIDB2 | PRECMP DSNHPC, TRN DFHECP1$, COBOL IGYCRCTL, LKED HEWL, BINDPK IKJEFT01, BINDPL IKJEFT01 | samples/proc/BLDCIDB2.prc:25 |
| bms-mapset | BUILDBMS | PRINT IEBGENER, MAP ASMA90, LKED HEWL, DSECT ASMA90, DISPLIST IEBGENER, DELTEMP IEFBR14 | samples/proc/BUILDBMS.prc:23 |
| cics-dli-sample |  | TRN DFHECP1$, COBOL IGYCRCTL, LKED IEWL | samples/jcl/IMSMQCMP.jcl:28 |

No DBDGEN, PSBGEN, or ACBGEN job is in the repository.

## Setup sequence

The README install order is Unverified. The named JCL members exist. See `docs/_work/ops/deploy.json`.

## Automation scripts

| Script | Order or actions | Evidence |
|---|---|---|
| scripts/remote_refresh.sh | CLOSEFIL, ACCTFILE, CARDFILE, XREFFILE, CUSTFILE, TRANFILE, DISCGRP, TCATBALF, TRANCATG, TRANTYPE, DUSRSECJ, OPENFIL | scripts/remote_refresh.sh:9-50 |
| scripts/run_full_batch.sh | CLOSEFIL, ACCTFILE, CARDFILE, XREFFILE, CUSTFILE, TRANBKP, DISCGRP, TCATBALF, TRANTYPE, DUSRSECJ, POSTTRAN, INTCALC, TRANBKP, COMBTRAN, TRANIDX, OPENFIL | scripts/run_full_batch.sh:9-66 |
| scripts/run_posting.sh | CLOSEFIL, ACCTFILE, TCATBALF, TRANBKP, POSTTRAN, TRANIDX, OPENFIL | scripts/run_posting.sh:9-34 |
| scripts/run_interest_calc.sh | CLOSEFIL, INTCALC, TRANBKP, COMBTRAN, TRANIDX, OPENFIL | scripts/run_interest_calc.sh:11-34 |
| scripts/remote_compile.sh | accepts a .cbl path, substitutes ZZZZZZZZ in scripts/compile_batch.jcl.template, puts the temp JCL to JES on localhost 2121 | scripts/remote_compile.sh:20-38 |
| scripts/remote_submit.sh | accepts a .jcl path and puts it to JES on localhost 2121 | scripts/remote_submit.sh:14-24 |
| scripts/upld_module.sh | pads the file to 80 columns with scripts/pad.awk, puts the member to 'AWS.M2.CARDDEMO.<module_type>(<module_name>)' | scripts/upld_module.sh:29-38 |
| scripts/local_compile.sh | runs cobc on sample/cobol/SIZING.cbl | scripts/local_compile.sh:2 |
| scripts/git-addSrcVersionInfo.sh | takes one source path; deletes every local git tag except `app_version` and tags `app_version`; writes a `Ver: CardDemo_<git describe>-<commit count> Date: <now>` banner using the comment syntax for cbl/cob/cpy, jcl/prc/proc, bms, or py; replaces an existing banner or appends one, overwriting the file | scripts/git-addSrcVersionInfo.sh:11-12, scripts/git-addSrcVersionInfo.sh:30-43, scripts/git-addSrcVersionInfo.sh:50-98 |

The version script sets `app_version=v2.0` (`scripts/git-addSrcVersionInfo.sh:12`). Banners in the source read `CardDemo_v1.0-15-g27d6c6f-68` (example `app/proc/REPROC.prc:31`). No other script or job in the repository calls the version script. Confirmed.

## Run book

| Task | Job | How | Evidence |
|---|---|---|---|
| Close CICS files before batch | CLOSEFIL | PGM=SDSF. ISFIN issues /F CICSAWSA,'CEMT SET FIL(...) CLO' for TRANSACT, CCXREF, ACCTDAT, CXACAIX, and USRSEC. | app/jcl/CLOSEFIL.jcl:22-30 |
| Open CICS files after batch | OPENFIL | PGM=SDSF. ISFIN issues /F CICSAWSA,'CEMT SET FIL(...) OPE' for the same five files. | app/jcl/OPENFIL.jcl:22-30 |
| Close and reopen one file around a load | CARDFILE, CUSTFILE, TRANFILE | Each job issues CEMT SET FIL CLO before the load and OPE after it, through the same /F CICSAWSA form. | app/jcl/CARDFILE.jcl:26-27, app/jcl/CARDFILE.jcl:122-123, app/jcl/CUSTFILE.jcl:26, app/jcl/CUSTFILE.jcl:80, app/jcl/TRANFILE.jcl:26-27, app/jcl/TRANFILE.jcl:120-121 |
| NEWCOPY a compiled CICS program | CICCMP | After the compile PROC, step NEWCOPY runs PGM=SDSF with /MODIFY CICSAWSA,'CEMT SET PROG(CICSPGMN) NEWCOPY'. CICSPGMN is the sample placeholder named in the job comment. | samples/jcl/CICCMP.jcl:45-49 |
| NEWCOPY a compiled BMS map | BMSCMP | Step SDSF1 runs PGM=SDSF with /MODIFY CICSAWSA,'CEMT SET PROG(CICSMAP) NEWCOPY'. | samples/jcl/BMSCMP.jcl:42-46 |
| Define CICS resources | CBADMCDJ | DFHCSDUP reads SYSIN DEFINE commands for GROUP(CARDDEMO). INSTALL GROUP is a comment. The job comment says to use CEDA INSTALL GROUP(CARDDEMO). | app/jcl/CBADMCDJ.jcl:27-45 |
| Load the user-security file | DUSRSECJ | IEFBR14, IEBGENER, then IDCAMS, then IDCAMS REPRO. | app/jcl/DUSRSECJ.jcl:23, app/jcl/DUSRSECJ.jcl:32, app/jcl/DUSRSECJ.jcl:58, app/jcl/DUSRSECJ.jcl:80-87 |
| Refresh application files from the shell |  | scripts/remote_refresh.sh puts CLOSEFIL, the file-load jobs, DUSRSECJ, and OPENFIL to JES in that order. | scripts/remote_refresh.sh:12-50 |
| Post transactions |  | scripts/run_posting.sh puts CLOSEFIL, ACCTFILE, TCATBALF, TRANBKP, POSTTRAN, TRANIDX, and OPENFIL. | scripts/run_posting.sh:12-34 |
| Calculate interest |  | scripts/run_interest_calc.sh puts CLOSEFIL, INTCALC, TRANBKP, COMBTRAN, TRANIDX, and OPENFIL. | scripts/run_interest_calc.sh:14-34 |
| Submit one job |  | scripts/remote_submit.sh puts a path whose extension is .jcl to JES on localhost port 2121. | scripts/remote_submit.sh:14-24 |

## Parameters

| Token | Value | Where defined |
|---|---|---|
| &HLQ | deployment-provided | README.md:108 describes it. CBADMCDJ sets HLQ=AWS.M2.CARDDEMO at app/jcl/CBADMCDJ.jcl:25. BUILDONL defaults HLQ to empty at samples/proc/BUILDONL.prc:26. |
| &SYSUID | deployment-provided | NOTIFY=&SYSUID on the CBADMCDJ job card at app/jcl/CBADMCDJ.jcl:2. |
| &SSID | deployment-provided | Passed by CICDBCMP and used as DSN SYSTEM (&SSID) at samples/proc/BLDCIDB2.prc:143. |
| &PLAN | deployment-provided | BIND PLAN (&PLAN) at samples/proc/BLDCIDB2.prc:168. MNTTRDB2 uses the literal PLAN(CARDDEMO) at app/app-transaction-type-db2/jcl/MNTTRDB2.jcl:30. |
| &DBRMLIB | deployment-provided | samples/proc/BLDCIDB2.prc:138 |
| &LOADLIB | default &HLQ..CARDDEMO.LOADLIB | samples/proc/BUILDONL.prc:33 |
| &CARDDEMOPRODJCL | deployment-provided | CA7 JCLLIB symbol. See docs/_work/gaps.md. |
| CICSAWSA | CICSAWSA | Literal CICS region name in operator commands, app/jcl/CLOSEFIL.jcl:26. |
| CARDDEMO | CARDDEMO | Literal DB2 qualifier and package collection in samples/proc/BLDCIDB2.prc:144-146 and in the DDL. This is not the <<db2-schema>> placeholder. |
| <<db2-schema>> | deployment-provided | Named in app/app-authorization-ims-db2-mq/README.md. The transaction-type DDL uses the literal CARDDEMO. |
| &&SYSPARM | MAP or DSECT at assembly | BUILDBMS sets SYSPARM(MAP) at samples/proc/BUILDBMS.prc:49 and SYSPARM(DSECT) at samples/proc/BUILDBMS.prc:78. |

## Alternative runtime packages

Not applicable - no runtime archive is in the repository.

## Sources

- `scripts/git-addSrcVersionInfo.sh:11-98`
- `app/proc/REPROC.prc:31`
- `docs/_work/ops/build.json`
- `docs/_work/ops/deploy.json`
- `docs/_work/ops/runbook.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
