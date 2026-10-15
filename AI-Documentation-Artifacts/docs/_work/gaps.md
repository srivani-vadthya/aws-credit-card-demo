# Gaps register

Facts below are limited to what the source and the A1 scan show. `Confirmed` is stated by a file. `Inferred` is a conclusion from several of those facts. `Unverified` is a comment or README only.

## MQ queue names

- Reply queues are literals: `CARD.DEMO.REPLY.ACCT` at `app/app-vsam-mq/cbl/COACCT01.cbl:198` and `CARD.DEMO.REPLY.DATE` at `app/app-vsam-mq/cbl/CODATE01.cbl:147`. Confirmed.
- `COACCT01` also uses `CARD.DEMO.ERROR` at `app/app-vsam-mq/cbl/COACCT01.cbl:294`. Confirmed.
- The request queue name is copied from the MQ trigger message (`MQTM-QNAME`) after `EXEC CICS RETRIEVE` (`app/app-vsam-mq/cbl/COACCT01.cbl:191-197`). It is not a literal in the source. What would resolve it: the MQ process definition that starts the CICS transaction. Not in this repository.

## External or missing

| Target | Where referenced | What would resolve it |
|---|---|---|
| `COCRDSEC` | `app/csd/CARDDEMO.CSD:211` (`DEFINE PROGRAM`), `app/csd/CARDDEMO.CSD:390` (`PROGRAM(COCRDSEC)`) | Program source is not in this repository. Confirmed missing. |
| `DSNTIAD` | `app/app-transaction-type-db2/ctl/DB2TIAD1.ctl:16` (`RUN PROGRAM(DSNTIAD)`) | Not an inventory member and not in the discovery skill's vendor-member list. Confirm from IBM DB2 documentation whether this is a supplied program. |

`BLDBAT` is not missing. The procedure name is defined at `samples/proc/BUILDBAT.prc:24` (member name `BUILDBAT`) and again in-stream at `scripts/compile_batch.jcl.template:7`. The `EXEC` at `scripts/compile_batch.jcl.template:64` resolves to the in-stream definition. Confirmed.

## Dynamic program names

Resolved in the base-module program pass:

- `CDEMO-MENU-OPT-PGMNAME` is the program-name column of `app/cpy/COMEN02Y.cpy:19-98`. `COMEN01C` transfers to those literals (`app/cbl/COMEN01C.cbl:177-187`). `COPAUS0C` is transferred only when `INQUIRE PROGRAM` returns NORMAL (`app/cbl/COMEN01C.cbl:147-159`). Confirmed.
- `CDEMO-ADMIN-OPT-PGMNAME` is the program-name column of `app/cpy/COADM02Y.cpy:29-59`. `COADM01C` transfers to a name that does not start with `DUMMY` (`app/cbl/COADM01C.cbl:141-148`). Confirmed.
- When `CDEMO-TO-PROGRAM` is spaces or low-values, `COMEN01C` and `COADM01C` set it to `COSGN00C` (`app/cbl/COMEN01C.cbl:198-199`, `app/cbl/COADM01C.cbl:165-166`). Confirmed. Any other value still comes from the caller. Not fully resolved.

Resolved in the 2026-10-12 pass. Every program-name constant below is set only by its `VALUE` clause; no `MOVE` targets it.

| Name | Resolves to | Evidence | Confidence |
|---|---|---|---|
| `CDEMO-TO-PROGRAM` | Literal or constant moved before each `XCTL`; per-edge sets are in `docs/_work/online/navigation.json` (`resolved_to`) | example `app/cbl/COUSR00C.cbl:192` then `app/cbl/COUSR00C.cbl:196-197` | Confirmed, except the return-to-caller rows below |
| `CDEMO-TO-PROGRAM` from `CDEMO-FROM-PROGRAM` | The caller: `COMEN01C` for `COACTVWC` and `COACTUPC`; `COMEN01C` or `COCRDLIC` for `COCRDSLC` and `COCRDUPC`; `COADM01C` or `COTRTLIC` for `COTRTUPC`; `COADM01C` for `COTRTLIC` | example `app/cbl/COACTVWC.cbl:333-339`; callers set `CDEMO-FROM-PROGRAM` to their own name (`app/cbl/COMEN01C.cbl:36`, `app/cbl/COMEN01C.cbl:179-185`, `app/cbl/COCRDLIC.cbl:521`) | Inferred: limited to callers found in this repository |
| `CCARD-NEXT-PROG` | `COCRDSLC` (view), `COCRDUPC` (update) | `app/cbl/COCRDLIC.cbl:526`, `app/cbl/COCRDLIC.cbl:554`; values `app/cbl/COCRDLIC.cbl:195-204` | Confirmed |
| `LIT-MENUPGM` | `COMEN01C` | `app/cbl/COCRDLIC.cbl:187-188` (same value in `COACTVWC`, `COACTUPC`, `COCRDSLC`, `COCRDUPC`) | Confirmed |
| `LIT-ADDTPGM` | `COTRTUPC` | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:50`, used at `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:648-649` | Confirmed |
| `WS-PGM-AUTH-FRAUD` | `COPAUS2C` (LINK) | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:35`, `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:248-249` | Confirmed |
| `LIT-DSNTIAC` | `DSNTIAC` (CALL; no source in repository, external-or-missing) | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:54`; call in `app/app-transaction-type-db2/cpy/CSDB2RPY.cpy:57`, included at `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:2055` | Confirmed name; target external |

Two moves were not counted as transfer targets. `COPAUS0C` sets `CDEMO-TO-PROGRAM` to its own name on first entry and then sends its screen without a transfer (`app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:190-198`). The move at `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:638` feeds the separate transfer at line 648.

## Orphans (findings, not errors)

- Copybook `app/cpy/UNUSED1Y.cpy` has no `COPY` in any program scanned. Confirmed unreferenced. The member name is not used as evidence of purpose.
- Program `app/cbl/CBTRN01C.cbl` (`PROGRAM-ID` at line 23) is not the target of a CSD `DEFINE PROGRAM`, JCL `EXEC PGM`, JCL `PARM` program token, `RUN PROGRAM`, `CALL`, or CICS `LINK`/`XCTL`. Confirmed unreferenced by those mechanisms. The comment at `app/cbl/CBTRN01C.cbl:3-5` calls it a batch post program. Unverified until a job or caller is found. Sibling programs are invoked: `CBTRN02C` at `app/jcl/POSTTRAN.jcl:23`, `CBTRN03C` at `app/jcl/TRANREPT.jcl:59`.

These are invoked, so they are not orphans:

- `CBPAUP0C` via `PARM` at `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:25`
- `PAUDBLOD` via `PARM` at `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL:27`
- `PAUDBUNL` via `PARM` at `app/app-authorization-ims-db2-mq/jcl/UNLDPADB.JCL:39`
- `DBUNLDGS` via `PARM` at `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL:27`
- `COBTUPDT` via `RUN PROGRAM` at `app/app-transaction-type-db2/jcl/MNTTRDB2.jcl:30`
- `CSSTRPFY` via quoted `COPY` (example `app/cbl/COCRDLIC.cbl:1416`)
- `CSUTLDWY` via quoted `COPY` (example `app/cbl/COACTUPC.cbl:166`)
- `COCDATFT` via Assembler `COPY` at `app/asm/COBDATFT.asm:66`
- `ASMWAIT` is a macro invoked at `app/asm/MVSWAIT.asm:23`, not a copybook

## Jobs not named in the scheduler exports or shell scripts

Search was a case-insensitive substring of the JCL member name in `app/scheduler/CardDemo.ca7`, `app/scheduler/CardDemo.controlm`, and `script-shell` files. Confirmed absent as that substring. Inferred: absence does not by itself prove the job never runs; a schedule could use a different name, or the job can be submitted by hand.

Application and optional-module jobs:

- `app/app-authorization-ims-db2-mq/jcl/DBPAUTP0.jcl`
- `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL`
- `app/app-authorization-ims-db2-mq/jcl/UNLDGSAM.JCL`
- `app/app-authorization-ims-db2-mq/jcl/UNLDPADB.JCL`
- `app/app-transaction-type-db2/jcl/CREADB21.jcl`
- `app/jcl/CBADMCDJ.jcl`
- `app/jcl/CBEXPORT.jcl`
- `app/jcl/CBIMPORT.jcl`
- `app/jcl/DALYREJS.jcl`
- `app/jcl/DEFCUST.jcl`
- `app/jcl/DEFGDGB.jcl`
- `app/jcl/DEFGDGD.jcl`
- `app/jcl/ESDSRRDS.jcl`
- `app/jcl/FTPJCL.JCL`
- `app/jcl/INTRDRJ1.JCL`
- `app/jcl/INTRDRJ2.JCL`
- `app/jcl/REPTFILE.jcl`
- `app/jcl/TRANREPT.jcl`

Sample compile and utility jobs under `samples/jcl/`: `BATCMP.jcl`, `BMSCMP.jcl`, `CICCMP.jcl`, `CICDBCMP.jcl`, `IMSMQCMP.jcl`, `LISTCAT.jcl`, `RACFCMDS.jcl`, `REPRTEST.jcl`, `SORTTEST.jcl`.

Named in shell scripts and not in the scheduler exports: `app/jcl/ACCTFILE.jcl`, `CARDFILE.jcl`, `CUSTFILE.jcl`, `DUSRSECJ.jcl`, `TRANFILE.jcl`, `TRANIDX.jcl`, `XREFFILE.jcl`. Their FTP `put` order is in `docs/_work/batch/schedule.json` `script_submits`.

## Scheduler names and calendars

- CA7 jobs `CLOSEFIL1` and `CLOSEFIL2` list JCL member `CLOSEFIL` (`app/scheduler/CardDemo.ca7:225`, `app/scheduler/CardDemo.ca7:252`). Confirmed. No job card in this repository is named `CLOSEFIL1` or `CLOSEFIL2`.
- CA7 `JCLLIB=&CARDDEMOPRODJCL` (`app/scheduler/CardDemo.ca7:35`). The symbol is a parameter. Its data set name is not in this repository.
- `SCHID` values on CA7 trigger lines (example `SCHID=030` at `app/scheduler/CardDemo.ca7:43`) are recorded on the edges. No schedule-id definition in this repository says what `030`, `031`, or `032` mean.
- Control-M job `TRANEXTR` has `PARENT_FOLDER="WEEKLY-DisclosureGroupsRefresh"` (`app/scheduler/CardDemo.controlm:58`) and is nested in `SMART_FOLDER` `FOLDER_NAME="WEEKLY-TransactionTypesDBRefresh"` (`app/scheduler/CardDemo.controlm:57`). Confirmed. Its `INCOND` is `WEEKLY-TransactionTypesDBRefresh-MNTTRDB2` (`app/scheduler/CardDemo.controlm:59`). The dependency used in `schedule.json` is that condition, not the `PARENT_FOLDER` attribute.
- `MNTTRDB2` has `TIMETO="23:00"` and no `DAYS` attribute (`app/scheduler/CardDemo.controlm:27`). The enclosing `FOLDER` `WEEKLY-TransactionTypesDBRefresh` also has no `DAYS` (`app/scheduler/CardDemo.controlm:26`). The word WEEKLY in `DESCRIPTION` is Unverified and is not a calendar.

## Record layouts not tied to one store

These clusters have a `RECORDSIZE` or LISTCAT `MAXLRECL` that matches more than one copybook, so `docs/_work/data/length-checks.json` leaves the layout unbound:

- `AWS.M2.CARDDEMO.CARDXREF.VSAM.KSDS`, `DISCGRP.VSAM.KSDS`, and `TCATBALF.VSAM.KSDS` are 50 bytes. Candidates include `CVACT03Y`, `CVTRA01Y`, `CVTRA02Y`, and `CSMSG01Y`.
- `AWS.M2.CARDDEMO.CUSTDATA.VSAM.KSDS` is 500 bytes. `CVCUS01Y` and `CUSTREC` both define `CUSTOMER-RECORD`. The date-of-birth field is `CUST-DOB-YYYY-MM-DD` at `app/cpy/CVCUS01Y.cpy:19` and `CUST-DOB-YYYYMMDD` at `app/cpy/CUSTREC.cpy:19`.
- `AWS.M2.CARDDEMO.TRANSACT.VSAM.KSDS` and `TRXFL.VSAM.KSDS` are 350 bytes. Candidates are `CVTRA05Y`, `CVTRA06Y`, and `COSTM01`.
- `TRANTYPE` and `TRANCATG` are 60 bytes (`CVTRA03Y` and `CVTRA04Y`).
- CICS file `USRSEC` names `AWS.M2.CARDDEMO.USRSEC.VSAM.KSDS` (`app/csd/CARDDEMO.CSD:88-89`). `ESDSRRDS` defines `AWS.M2.CARDDEMO.USRSEC.VSAM.ESDS` (`app/jcl/ESDSRRDS.jcl:65`) and `AWS.M2.CARDDEMO.USRSEC.VSAM.RRDS` (`app/jcl/ESDSRRDS.jcl:99`). All three are 80-byte candidates with `CSUSR01Y`, `CODATECN`, and `UNUSED1Y`.

`CIPAUSMY` is 100 bytes and `CIPAUDTY` is 200. Those totals agree with `PAUTSUM0` and `PAUTDTL1`. The copybooks have no `01` level, so the offsets are relative to the `COPY`.

The Assembler member `app/maclib/COCDATFT.mac` was not laid out by the COBOL layout tool.

## Integration leftovers

- No COBOL `EXEC SQL` references `CARDDEMO.TRANSACTION_TYPE_CATEGORY`. The rows are inserted by `app/app-transaction-type-db2/ctl/DB2LTCAT.ctl:15`, run from `app/app-transaction-type-db2/jcl/CREADB21.jcl:84`. Confirmed.
- `COBTUPDT` has no `EXEC SQL COMMIT`. The batch plan is `CARDDEMO` at `app/app-transaction-type-db2/jcl/MNTTRDB2.jcl:30`. Where that plan commits is not stated in the program.
- `FTPJCLS` SYSIN contains a user id and a password (`app/jcl/FTPJCL.JCL:33-40`). Those values are not repeated in the integration catalog. The comment at `app/jcl/FTPJCL.JCL:22` says the job receives a file. The command at line 40 is `PUT`. The comment is Unverified.

## Business rules not yet written one by one

`docs/_work/rules/rules.json` holds the decisions that were read in this pass. The remaining programs still contain validations.

- `docs/_work/rules/messages.json` lists 34 inline quoted strings on lines that mention a message field. Messages stored in copybooks, such as `CCDA-MSG-INVALID-KEY` at `app/cbl/COADM01C.cbl:105`, are not in that index.
- `docs/_work/rules/computes.json` lists 88 `COMPUTE` lines. Only the interest formula in `CBACT04C` and the expiry day difference in `CBPAUP0C` were promoted to rules.
- Field edits now written as rules: `COACTUPC` (`app/cbl/COACTUPC.cbl:1429-2558`), `COCRDUPC` (`app/cbl/COCRDUPC.cbl:641-945`), `COCRDSLC` (`app/cbl/COCRDSLC.cbl:608-719`), `COACTVWC` (`app/cbl/COACTVWC.cbl:622-680`), and `COTRTUPC` (`app/app-transaction-type-db2/cbl/COTRTUPC.cbl:689-974`). Still not written one by one: the inline checks in `COUSR01C`, `COUSR02C`, `COUSR03C`, and `COTRN02C` (example `app/cbl/COTRN02C.cbl:199`).
- The meaning of `99999 - PA-AUTH-DATE-9C` (`app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:280`) is not stated in the paragraph. The formula is recorded as written.

## Operations leftovers

- `samples/proc/BUILDONL.prc:25` and `samples/proc/BLDCIDB2.prc:25` both use the procedure label `BLDONL`. The sample jobs execute `BUILDONL` (`samples/jcl/CICCMP.jcl:41`) and `BLDCIDB2` (`samples/jcl/CICDBCMP.jcl:54`).
- `scripts/local_compile.sh:2` compiles `sample/cobol/SIZING.cbl`. That source file is not in this repository.
- The README install order at `README.md:147-166` is Unverified. The named JCL members exist. The README does not prove that order is required.
- No MQ authority commands, and no DBDGEN, PSBGEN, or ACBGEN jobs, were found.

## Cross-reference leftovers

COBOL `SELECT` names stay in `docs/_work/xref/crud-matrix.json`. They were not copied onto dataset rows. A shared record length does not identify which dataset a copybook belongs to.

`CBTRN01C` remains unreferenced by a call target, a job step, an invoked program name, or a CICS transaction (`docs/_work/xref/catalog.json`).

## Scanner limits corrected in this pass

`references.json` is the raw scan. These patterns were confirmed in source and recorded on `resolved_refs` when the raw scan missed them:

- Quoted COBOL `COPY 'name'` (example `app/cbl/COCRDLIC.cbl:1416`).
- Assembler `COPY` (`app/asm/COBDATFT.asm:66`).
- Program name in a `DFSRRC00` `PARM` (example `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:25`).
- `RUN PROGRAM(name)` in SYSIN (example `app/app-transaction-type-db2/jcl/MNTTRDB2.jcl:30`).
- Procedure name different from the member name (`BLDBAT` vs `BUILDBAT`, above).

`docs-toolkit/project-profile.yaml:103` contains the word `DFHMSD` in a sentence. The BMS signature matched it. Corrected in `inventory.json` to `documentation`. The signature now requires a mapset label in column 1 followed by `DFHMSD`. Confirmed the 21 `.bms` files still match and this yaml file does not.

## Duplicate member names

`scripts/markers/` holds empty files whose names match application members (example `scripts/markers/CBTRN02C` and `app/cbl/CBTRN02C.cbl`). Member resolution prefers the typed source (program, copybook, proc, map) over `placeholder`. Confirmed by file size 0 on the marker entries in `inventory.json`.

## Resume pass findings (2026-10-12)

No application source changed since the previous run. Every non-excluded file has the same `sha256` as in `inventory.json`; only `docs-toolkit/README.md` and `docs-toolkit/project-profile.yaml` differ. Confirmed.

Open items found in this pass:

- `REPROC` reads its IDCAMS control card from `&CNTLLIB(REPROCT)` (`app/proc/REPROC.prc:27-28`), and every caller sets `CNTLLIB=AWS.M2.CARDDEMO.CNTL` (for example `app/jcl/TRANBKP.jcl:24`). The repository has two copies, `app/ctl/REPROCT.ctl` and `app/app-transaction-type-db2/ctl/REPROCT.ctl`. They are byte-identical, so the statement `REPRO INFILE(FILEIN) OUTFILE(FILEOUT)` (line 15 of both) is Confirmed. Which file is uploaded into `AWS.M2.CARDDEMO.CNTL` is not stated. `scripts/upld_module.sh:37` takes the target library as an argument. What would resolve it: the upload procedure used for the control library.
- `CORPT00C` writes the JCL of job `TRNRPT00` (`EXEC PROC=TRANREPT`) to TD queue `JOBS` (`app/cbl/CORPT00C.cbl:83-94`, `app/cbl/CORPT00C.cbl:497-520`). Confirmed. `JOBS` is `TYPE(EXTRA) DDNAME(INREADER)` (`app/csd/CARDDEMO.CSD:499-501`). The CICS region JCL that defines DD `INREADER` is not in the repository, so the queue's destination is Unverified. What would resolve it: the CICS region startup JCL.
- `app/proc/TRANREPT.prc:1` is labelled `//REPROC PROC` while the member name is `TRANREPT`. Its step `STEP01R` executes `PROC=REPROC` (`app/proc/TRANREPT.prc:21`), which names member `app/proc/REPROC.prc`. Confirmed observation. How the label mismatch is treated at run time is not stated in the repository.
- Two jobs reuse a step name: `STEP05R` at `app/jcl/TRANREPT.jcl:23` and `app/jcl/TRANREPT.jcl:37`, and `STEP05` at `app/jcl/DEFCUST.jcl:22` and `app/jcl/DEFCUST.jcl:32`. Confirmed. A step-qualified override or referback to those names is ambiguous.
- `scripts/git-addSrcVersionInfo.sh:12` sets `app_version=v2.0`. The banners in the source read `CardDemo_v1.0-15-g27d6c6f-68` (example `app/proc/REPROC.prc:31`). Confirmed. Nothing in the repository runs that script.

Code findings from the update-screen field edits (recorded as observations; the source is not changed):

- Phone not-entered test. `app/cbl/COACTUPC.cbl:2238-2239` reads `(WS-EDIT-US-PHONE-NUMA EQUAL SPACES OR WS-EDIT-US-PHONE-NUMC EQUAL LOW-VALUES)`. The two lines before it test NUMA and NUMB, so NUMC is expected in both halves of this pair. Confirmed as written. Inferred effect: a phone number with a blank area code and prefix is accepted as not entered even when a line number is keyed. Rule `BR-BASE-COACTUPC-014`.
- Date flags after a CSUTLDTC failure. `GO TO EDIT-DATE-LE-EXIT` (`app/cpy/CSUTLDPY.cpy:315`) lands inside the `PERFORM EDIT-DATE-CCYYMMDD THRU EDIT-DATE-CCYYMMDD-EXIT` range (`app/cbl/COACTUPC.cbl:1480-1481`), so control falls through to `SET WS-EDIT-DATE-IS-VALID TO TRUE` (`app/cpy/CSUTLDPY.cpy:327`). Confirmed. `INPUT-ERROR` and the message stay set, so the update is still blocked (`app/cbl/COACTUPC.cbl:1671-1675`). Inferred effect: the date's own flags read valid, so the field is not marked in error, and for Date of Birth the future-date check still runs (`app/cbl/COACTUPC.cbl:1538-1540`). Rule `BR-BASE-COACTUPC-007`.
- Zero account number. `COCRDUPC` treats a zero account number as not provided (`app/cbl/COCRDUPC.cbl:725-731`). `COACTUPC` rejects it with 'Account Number if supplied must be a 11 digit Non-Zero Number' (`app/cbl/COACTUPC.cbl:1802-1808`). Confirmed difference.
- Comments that disagree with code in `COCRDUPC`. The comment at `app/cbl/COCRDUPC.cbl:928-929` says the expiry year must be numeric and 1 to 12. The code tests `VALID-YEAR` 1950 thru 2099 (`app/cbl/COCRDUPC.cbl:99`). The comments at `app/cbl/COCRDUPC.cbl:894-895` and `928` say "must be numeric", but no `IS NUMERIC` test is coded. The month and year are tested through 88-levels on `PIC 9` redefinitions of `PIC X` input (`app/cbl/COCRDUPC.cbl:92-99`). Code wins. How a non-numeric value behaves in those 88-level tests depends on compiler options that are not in the repository. Unverified.
- Date of birth equal to today. `EDIT-DATE-OF-BIRTH` accepts the date only when the current date is greater (`app/cpy/CSUTLDPY.cpy:350`), so today's date is rejected with ':cannot be in the future'. Confirmed.

Corrections to earlier work files in this pass:

- `docs/_work/batch/schedule.json` said the JCL written to `JOBS` had no literal job name. It has one: `TRNRPT00` (`app/cbl/CORPT00C.cbl:84`). The submit entry now records the job, the PROC, and the queue attributes.
- The job facts for `TRANREPT` and `DEFCUST` gave both same-named steps every DD in the job. DDs are now assigned by line range. Four duplicate dataflow edges for `TRANREPT` were removed from `docs/_work/batch/dataflow.json`.
- The four jobs that run `REPROC` (`TRANBKP`, `TRANREPT`, `PRTCATBL`, `REPRTEST`) now record the PROC expansion, the `PRC001.SYSIN` DD, and the `REPROCT` control statement. `docs/_work/datasets/AWS.M2.CARDDEMO.CNTL.json` lists those readers.
- The job pages had dropped the line number from 105 control-statement citations (the path was followed by a colon and no line). The numbers were restored from the job facts. `check_package.py` does not test for a citation that has no line number.

## Resume pass findings (2026-10-13)

No application source changed. Discovery compared with `docs/_work/inventory.json` found two new root files, `COMBINED_DOCUMENTATION.md` and `PROJECT_DOCUMENTATION.docx`. Both are generated reading copies. They are excluded in `docs-toolkit/project-profile.yaml`. Confirmed from `COMBINED_DOCUMENTATION.md:1-9` and from the opening of `PROJECT_DOCUMENTATION.docx`.

`docs/application-documentation/CardDemo-end-to-end.md` was absent while `00-index.md` still linked to it. The page was restored from `CardDemo-end-to-end.docx`. The `DFHMSD` prose token in the profile is now `docs-toolkit/project-profile.yaml:111`.
