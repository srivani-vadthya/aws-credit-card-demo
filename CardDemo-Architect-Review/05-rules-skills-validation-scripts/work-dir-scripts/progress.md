# Documentation progress

Application: CardDemo. Profile: `docs-toolkit/project-profile.yaml`.

```
Phase 0  Setup
- [x] 0.1 Profile exists and validated (bootstrap.md)
- [x] 0.2 Rules installed in .cursor/rules
Phase A  Extraction (write to work_dir)
- [x] A1 Inventory + classification       -> mainframe-inventory-discovery
- [x] A2 Program facts (COBOL/ASM/PLI)    -> cobol-program-analysis
- [x] A3 Online facts (CSD/BMS/flows)     -> cics-online-analysis
- [x] A4 Batch facts (JCL/PROC/sched)     -> batch-jcl-analysis
- [x] A5 Data facts (layouts/VSAM/DB2/IMS/MQ) -> mainframe-data-model-analysis
- [x] A6 Integration facts (MQ/DLI/SQL/FTP)   -> mainframe-integration-analysis
- [x] A7 Business rules                   -> business-rules-extraction
- [x] A8 Build/deploy/security/ops        -> build-deploy-security-analysis
- [x] A9 Cross-reference + CRUD matrix consolidation
Phase S  Structure and batched semantics (write to work_dir)
- [x] S1 extract_structure.py             -> structure/
- [x] S2 batch_manager.py init + worksheets -> batches/ (B01-B10), semantic/ skeletons
- [x] S3 Semantic files for 44 programs and 44 copybooks
- [x] S4 batch_manager.py check all       -> 10 of 10 batches validated
Phase B  Assembly (write to output_dir)
- [x] B1 Render templates                 -> mainframe-doc-assembly-qa
- [x] B1b render_detail.py                -> detailed pages
- [x] B2 coverage_validate.py 26/26 pass + check_package.py 0 issues
- [x] B3 gap_report.py + QA checklist + gaps register published
```

## A1 result (2026-10-09)

- `inventory.json`: 331 files, unclassified 0. Module counts: base 169, auth 40, trantype 27, vsammq 4, build 71, no module 20.
- `references.json`: 2748 raw references from the scanner.
- `resolved_refs` added on each file. Counts: inventory 466, system 253, dynamic-unresolved 33, external-or-missing 2.
- 17 files have a numeric columns 73-80 sequence area (`inventory.json` `summary.files_with_sequence_area`). Confirmed.
- Output package is `docs/application-documentation/` (403 Markdown files). Coverage check issues: 0.

## A2 base module (2026-10-11)

- 31 COBOL programs and 2 Assembler routines under `docs/_work/programs/`. Inventory `analysis_status` is `done` for those members.
- Cross-references for this module: `docs/_work/xref/call-graph.json`, `copybook-usage.json`, `crud-matrix.json`.
- Paragraph purposes are Inferred from the statements in each paragraph. Header comments stay Unverified.
- Candidate business rules were written for `COSGN00C`, `COBDATFT`, and `MVSWAIT`, where the procedure was read in full. Other programs carry messages, CRUD, and control flow for the business-rules pass.
- Menu and admin transfer targets are the literals in `app/cpy/COMEN02Y.cpy` and `app/cpy/COADM02Y.cpy`. See `gaps.md`.

## A2 optional modules (2026-10-11)

Program facts now exist for every COBOL program in `auth` (8), `trantype` (3), and `vsammq` (2), plus the base programs. `docs/_work/xref/` was rebuilt from all of those files.

Confirmed in this pass:

- `COACCT01` reads CICS file `ACCTDAT` and replies on the literal queue `CARD.DEMO.REPLY.ACCT` (`app/app-vsam-mq/cbl/COACCT01.cbl:116`, `app/app-vsam-mq/cbl/COACCT01.cbl:198`).
- `CODATE01` replies on `CARD.DEMO.REPLY.DATE` (`app/app-vsam-mq/cbl/CODATE01.cbl:147`).
- Both take the request queue name from `EXEC CICS RETRIEVE` of the MQ trigger message. That name is not a literal.
- `COPAUS2C` inserts and updates `CARDDEMO.AUTHFRDS`.
- `COBTUPDT` is the batch DB2 program run by `app/app-transaction-type-db2/jcl/MNTTRDB2.jcl:30`.

## A3 online (2026-10-11)

Written under `docs/_work/online/`:

- `transactions.json`: 89 CSD resources, 25 transactions, 21 mapsets. `CC00` starts `COSGN00C` (`app/csd/CARDDEMO.CSD:378`). `CDV1` starts `COCRDSEC`, which still has no source.
- `screens/<MAPSET>.json`: field tables and a 24x80 mockup built from `POS`, `LENGTH`, and `INITIAL`. Signon map `COSGN0A` is `app/bms/COSGN00.bms:19`. The password field is `PASSWD`, dark and unprotected, at `app/bms/COSGN00.bms:175`.
- `navigation.json`: 73 XCTL, LINK, START, and RETURN TRANSID edges, plus 48 AID-key `WHEN` lines.
- `commarea.json`: fields of `CARDDEMO-COMMAREA` from `app/cpy/COCOM01Y.cpy:19`.
- `queues.json`: TD queue `JOBS` (`app/csd/CARDDEMO.CSD:499`). `CORPT00C` writes that queue (`app/cbl/CORPT00C.cbl:517`).

## A4 batch (2026-10-11)

Written under `docs/_work/jobs/` (55 jobs, one file per JCL job card) and `docs/_work/batch/`:

- `schedule.json`: 28 CA7 trigger edges and 12 Control-M condition edges, kept as separate lists. Shell `put` order is `script_submits`. TD queue `JOBS` is recorded as a submit path with no literal job name.
- `dataflow.json`: 243 dataset edges from DD statements that have both a data set name and a DISP usage.
- `catalog.json`: job and PROC index.

Confirmed in this pass:

- `CBPAUP0J` step `STEP01` is `PGM=DFSRRC00` with `PARM='BMP,CBPAUP0C,PSBPAUTB'` (`app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:24`). CA7 successor is `POSTTRAN` (`app/scheduler/CardDemo.ca7:70`).
- `POSTTRAN` step `STEP15` executes `CBTRN02C` (`app/jcl/POSTTRAN.jcl:23`).
- `DEFGDGB` step `STEP05` runs `IDCAMS` `DEFINE GENERATIONDATAGROUP` (`app/jcl/DEFGDGB.jcl:24`).
- Control-M daily folder `DAILY-TransactionBackup`: `CLOSEFIL` adds condition `DAILY-TransactionBackup-CLOSEFIL`, and `TRANBKP` waits on it (`app/scheduler/CardDemo.controlm:4-8`). `DAYS="ALL"`, `TIMETO="23:00"`.
- `MNTTRDB2` SYSIN is `RUN PROGRAM(COBTUPDT) PLAN(CARDDEMO)` (`app/app-transaction-type-db2/jcl/MNTTRDB2.jcl:30`).
- `INTRDRJ1` step `STEP01` copies `AWS.M2.CARDDEMO.JCL(INTRDRJ2)` to `SYSOUT=(A,INTRDR)` (`app/jcl/INTRDRJ1.JCL:17-18`).
- CA7 jobs `CLOSEFIL1` and `CLOSEFIL2` name JCL member `CLOSEFIL` (`app/scheduler/CardDemo.ca7:225`, `app/scheduler/CardDemo.ca7:252`). There is no job card with those names.

Comment text stored as a job description is Unverified. `SCHID` is recorded and not given a business meaning. Jobs that are absent from both schedulers and the shell `jcl/` puts have that absence as a finding on the job file. Sample members under `samples/jcl/` are in that set.

Inventory `analysis_status` is `done` for the 55 `jcl-job` files.

## A5 data (2026-10-11)

Written under `docs/_work/layouts/` (44 COBOL copybooks and DCLGEN members, JSON and Markdown), `docs/_work/datasets/` (204 stores), and `docs/_work/data/`:

- `entities.json`: account, card, customer, card-cross-reference, and authorization-fraud, with the relationships that have a field, AIX, or DB2 column behind them.
- `length-checks.json`: copybook length against `RECORDSIZE` or LISTCAT `MAXLRECL`. A check is unbound when more than one copybook has that length.
- `samples.json`: text files by record count and line length. Binary files by size. No sample values were copied.

Confirmed in this pass:

- `ACCOUNT-RECORD` in `app/cpy/CVACT01Y.cpy` is 300 bytes. `ACCT-ID` is `PIC 9(11)` at byte 1 (`app/cpy/CVACT01Y.cpy:5`). `ACCTFILE` defines that cluster at `app/jcl/ACCTFILE.jcl:36`, with `KEYS(11 0)` at line 40 and `RECORDSIZE(300 300)` at line 41. LISTCAT `MAXLRECL` is 300 and `KEYLEN` is 11 (`app/catlg/LISTCAT.txt:59-60`). `app/data/ASCII/acctdata.txt` has 50 lines of 300 characters. LISTCAT `REC-TOTAL` for that cluster is 50 (`app/catlg/LISTCAT.txt:64`). The catalog date on the listing is 09/01/22.
- `CARD-RECORD` in `app/cpy/CVACT02Y.cpy` is 150 bytes. `CARD-NUM` is 16 bytes at byte 1. That agrees with `CARDFILE` `RECORDSIZE` and `KEYS(16 0)`.
- `CARD-XREF-RECORD` in `app/cpy/CVACT03Y.cpy` is 50 bytes. `XREF-CARD-NUM` is bytes 1-16 (`app/cpy/CVACT03Y.cpy:5`). `XREF-ACCT-ID` is `PIC 9(11)` at byte 26 (`app/cpy/CVACT03Y.cpy:7`), which is `KEYS(11,25)` on the alternate index (`app/jcl/XREFFILE.jcl:72-74`). Other copybooks are also 50 bytes, so this layout was not stored as the only layout for that cluster.
- `DBPAUTP0` is `ACCESS=(HIDAM,VSAM)` (`app/app-authorization-ims-db2-mq/ims/DBPAUTP0.dbd:18`). Root `PAUTSUM0` is 100 bytes, sequence field `ACCNTID` (`app/app-authorization-ims-db2-mq/ims/DBPAUTP0.dbd:28-30`). Child `PAUTDTL1` is 200 bytes (`app/app-authorization-ims-db2-mq/ims/DBPAUTP0.dbd:36`). `CIPAUSMY` lays out to 100 bytes and `CIPAUDTY` to 200. Both are copied by `CBPAUP0C` (`app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:117` and `:121`).
- `CARDDEMO.TRANSACTION_TYPE` has `TR_TYPE CHAR(2) NOT NULL` and primary key `TR_TYPE` (`app/app-transaction-type-db2/ddl/TRNTYPE.ddl:1-3`). The tablespace in the control cards is `CARDDEMO.CARDSPC1` (`app/app-transaction-type-db2/ctl/DB2CREAT.ctl:35-39`).
- `CARDDEMO.AUTHFRDS` primary key is `CARD_NUM, AUTH_TS` (`app/app-authorization-ims-db2-mq/ddl/AUTHFRDS.ddl:28`).
- Reply queues `CARD.DEMO.REPLY.ACCT` and `CARD.DEMO.REPLY.DATE` are literals. The request queue name is still the trigger message.

LISTCAT contributes 160 `NONVSAM` names. Those entries are the catalog as of 09/01/22, including data sets that are not defined by the JCL in this repository.

## A6 integration (2026-10-11)

Written under `docs/_work/integration/`:

- `interfaces.json`: 14 interfaces. CICS `XCTL` and `LINK` stay in `docs/_work/online/navigation.json`.
- `sequences/`: four Mermaid sequence drafts for the account MQ reply, the authorization MQ request, the DB2 type maintenance job, and the IMS checkpoint loop.

Confirmed in this pass:

- `CDRA` starts `COACCT01` and `CDRD` starts `CODATE01` (`app/app-vsam-mq/csd/CRDDEMOM.csd:17-18`, `app/app-vsam-mq/csd/CRDDEMOM.csd:27-28`). Both retrieve `MQTM-QNAME`, get with a 5000 millisecond wait under `MQGMO-SYNCPOINT`, and put the reply on a literal queue. The reply descriptor receives the saved request `MsgId` and `CorrelId` (`app/app-vsam-mq/cbl/COACCT01.cbl:469-470`).
- `CP00` starts `COPAUA0C` (`app/app-authorization-ims-db2-mq/csd/CRDDEMO2.csd:59-60`). The request buffer is `UNSTRING` delimited by comma (`app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:354-374`). The reply queue is `MQMD-REPLYTOQ` (`app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:413-414`).
- `PSBPAUTB` is the literal PSB name in the CICS programs and in `CBPAUP0J` (`app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:80`, `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:25`). `CBPAUP0C` checkpoints with `EXEC DLI CHKP` (`app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:355`).
- `CARDDEMO.TRANSACTION_TYPE` is maintained by `COTRTLIC`, `COTRTUPC`, and `COBTUPDT`. Input actions in the batch program are `A`, `U`, `D`, and `*` (`app/app-transaction-type-db2/cbl/COBTUPDT.cbl:111-120`). `COBTUPDT` contains no `EXEC SQL COMMIT`.
- `CARDDEMO.TRANSACTION_TYPE_CATEGORY` is created in DDL and loaded by `CREADB21` step `LDTCCAT` through `DSNTEP4` (`app/app-transaction-type-db2/jcl/CREADB21.jcl:77-84`). No COBOL `EXEC SQL` against that table was found.
- `FTPJCLS` step `STEP1` runs `PGM=FTP`. The SYSIN command is `PUT`. User id and password in that SYSIN were not copied.

## A7 business rules (2026-10-11)

Written under `docs/_work/rules/`:

- `rules.json`: 18 rules, schema `rules/1`. Drafts in `by-program/` for `COSGN00C`, `COMEN01C`, `COADM01C`, `CBACT04C`, `COBTUPDT`, `CBPAUP0C`, and `COBDATFT`.
- `messages.json`: 34 inline message literals. `computes.json`: 88 `COMPUTE` lines. These indexes are not rules.

Confirmed in this pass:

- Blank user id and blank password stop sign-on before the security file is read (`app/cbl/COSGN00C.cbl:118-127`). Both values are upper-cased (`app/cbl/COSGN00C.cbl:132-136`). A password mismatch redisplays `Wrong Password. Try again ...` (`app/cbl/COSGN00C.cbl:241-246`). Admin type `A` (`app/cpy/COCOM01Y.cpy:27`) transfers to `COADM01C`; any other type transfers to `COMEN01C` (`app/cbl/COSGN00C.cbl:230-239`).
- PF3 on both menus sets the return target to `COSGN00C` (`app/cbl/COMEN01C.cbl:96-98`, `app/cbl/COADM01C.cbl:100-102`). An empty return target is also set to `COSGN00C` (`app/cbl/COMEN01C.cbl:198-200`, `app/cbl/COADM01C.cbl:165-167`).
- Monthly interest is `(TRAN-CAT-BAL * DIS-INT-RATE) / 1200` into `WS-MONTHLY-INT PIC S9(09)V99` with no `ROUNDED` (`app/cbl/CBACT04C.cbl:168`, `app/cbl/CBACT04C.cbl:464-465`).
- `INPUT-REC-TYPE` `A`/`U`/`D`/`*` and other (`app/app-transaction-type-db2/cbl/COBTUPDT.cbl:111-128`).
- Pending authorization delete uses `WS-DAY-DIFF >= WS-EXPIRY-DAYS`. The default expiry is 5 when the parm is not numeric (`app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:196-199`, `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:284-286`). Response `00` adjusts the approved totals (`app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:287-293`).

`MVSWAIT` passes a fullword delay to `ASMWAIT` (`app/asm/MVSWAIT.asm:20-23`). That is technical plumbing and is not a business rule.

## A8 build, deploy, security, and operations (2026-10-11)

Written under `docs/_work/ops/`:

- `build.json`: batch COBOL, CICS COBOL, CICS-DB2 COBOL, BMS, and the IMSMQCMP sample job.
- `deploy.json`: README install list marked Unverified, shell submit orders, CSD job, and environment tokens.
- `security.json`: sign-on, user types, CICS `RESSEC`/`CMDSEC`, DB2 `GRANT`, and the RACF sample job.
- `runbook.json`: close/open files, NEWCOPY, data refresh, posting, and interest.

Confirmed in this pass:

- Batch compile is `IGYCRCTL` then `HEWL` (`samples/proc/BUILDBAT.prc:35-36`, `samples/proc/BUILDBAT.prc:74`). CICS COBOL compile uses `IGYCRCTL` with `PARM` `CICS` and has no separate translator step (`samples/proc/BUILDONL.prc:39-40`). CICS-DB2 compile is `DSNHPC`, `DFHECP1$`, `IGYCRCTL`, `HEWL`, then `BIND PACKAGE` and `BIND PLAN` (`samples/proc/BLDCIDB2.prc:46-47`, `samples/proc/BLDCIDB2.prc:68`, `samples/proc/BLDCIDB2.prc:144-169`).
- BMS assembly uses `ASMA90` with `SYSPARM(MAP)` and a second `ASMA90` with `SYSPARM(DSECT)` (`samples/proc/BUILDBMS.prc:49`, `samples/proc/BUILDBMS.prc:78`).
- `CLOSEFIL` and `OPENFIL` run `SDSF` and issue `/F CICSAWSA` `CEMT SET FIL` close and open commands (`app/jcl/CLOSEFIL.jcl:26-30`, `app/jcl/OPENFIL.jcl:26-30`).
- `CBADMCDJ` runs `DFHCSDUP`. `INSTALL GROUP(CARDDEMO)` is a comment (`app/jcl/CBADMCDJ.jcl:27-28`, `app/jcl/CBADMCDJ.jcl:37`).
- Transaction definitions set `RESSEC(NO) CMDSEC(NO)` (`app/csd/CARDDEMO.CSD:314`). DB2 grants on `CARDDEMO` are `TO PUBLIC` (`app/app-transaction-type-db2/ctl/DB2CREAT.ctl:52-59`).
- Sign-on compares the upper-cased password with `SEC-USR-PWD` (`app/cbl/COSGN00C.cbl:132-136`, `app/cbl/COSGN00C.cbl:223`). The password picture is `PIC X(08)` (`app/cpy/CSUSR01Y.cpy:21`). A user-type `U` session is refused a menu option marked `A` (`app/cbl/COMEN01C.cbl:136-142`).

No DBDGEN, PSBGEN, or ACBGEN job is in the repository. No runtime archive is in the repository. The FTP user id and password in `FTPJCLS` were not copied.

## A9 cross-reference (2026-10-11)

The program call graph, copybook usage, and CRUD matrix were left in place: 134 call edges, 70 copybooks, 92 CRUD rows.

Added under `docs/_work/xref/`:

- `online-trace.json`: 25 transactions, each with its program, mapset, stores, and rules. `CC00` is `COSGN00C` on mapset `COSGN00`.
- `batch-trace.json`: 55 jobs. A step whose `PGM` is `DFSRRC00` or `IKJEFT01` also records the application program from the `PARM` or from `RUN PROGRAM`. `CBPAUP0J` invokes `CBPAUP0C`. `MNTTRDB2` invokes `COBTUPDT`.
- `dataset-names.json`: 204 dataset names, with CICS file aliases and JCL DD names. `AWS.M2.CARDDEMO.ACCTDATA.VSAM.KSDS` is CICS file `ACCTDAT` (`app/csd/CARDDEMO.CSD:1`) and appears on 6 DD statements.
- `rule-trace.json`: 18 rules joined to the programs, transactions, and jobs that implement them.
- `interface-trace.json`: the 14 interfaces already listed in `docs/_work/integration/interfaces.json`.
- `catalog.json`: counts for this pass.

`CBTRN01C` is still not referenced by a call, a job, or a transaction.

## Phase B assembly (2026-10-11)

The published package is `docs/application-documentation/`. It has 403 Markdown files: one page per program, job, mapset, dataset, and layout, plus the overview and cross-reference pages.

`check_package.py` reported 0 uncovered artifacts, 0 broken links, 0 placeholders, 0 Mermaid warnings, and 0 documents missing a Sources section.

## Resume pass (2026-10-12)

- Discovery was re-run into a scratch file and compared with `inventory.json`. No application source changed. Only `docs-toolkit/README.md` and `docs-toolkit/project-profile.yaml` changed; their `sha256` values were updated. The scratch file was deleted.
- 101 artifacts were still `pending` after the earlier phases. 99 are now `done` because the work facts cite them by path or member name. The other two, `app/app-transaction-type-db2/README.md` and `app/app-vsam-mq/README.md`, stay `pending`: the package lists them, but no fact uses them as evidence.
- Extraction fixes: the `REPROC` expansion and the `REPROCT` control card were added to `TRANBKP`, `TRANREPT`, `PRTCATBL`, and `REPRTEST`. DDs in `TRANREPT` and `DEFCUST` were reassigned by step line range because each job reuses a step name. The online-submitted job `TRNRPT00` from `CORPT00C` is now recorded in `programs/CORPT00C.json` and `batch/schedule.json`. `scripts/git-addSrcVersionInfo.sh` is recorded in `ops/build.json` under `tools`.
- Rendering fixes: 105 control-statement citations in 32 job pages got their line numbers back. Pages updated: 5 job pages, `CORPT00C`, `CBTRN03C`, datasets `AWS.M2.CARDDEMO.CNTL` and `JOBS`, `06-batch/batch-schedule-flow.md`, `13-build-deploy-operations.md`, and `16-gaps-assumptions-open-questions.md`.
- `check_package.py`: 403 documents, 0 issues. Manual checks: 0 citations without a line number, and exactly one H1 on every page.
- New open items are under "Resume pass findings (2026-10-12)" in `gaps.md`.
- Dynamic program names: 32 variable XCTL edges in `online/navigation.json` and `xref/call-graph.json` now carry `resolved_to` and `resolution_confidence`. Targets set from literals are Confirmed. Return-to-caller targets are Inferred from the caller lists. Two moves that are not transfers are kept under `excluded_moves`. `05-online/navigation-flow.md` gained user-menu and admin-menu flow diagrams, and the program pages show the resolved names.
- Business rules: 25 rules were added to `rules/rules.json` (43 in total) for the field edits of `COCRDUPC` (`app/cbl/COCRDUPC.cbl:641-945`) and `COACTUPC` (`app/cbl/COACTUPC.cbl:1429-2558`, with copybooks `CSUTLDPY`, `CSUTLDWY`, `CSLKPCDY`). `xref/rule-trace.json`, `rules/by-program/COCRDUPC.md`, `rules/by-program/COACTUPC.md`, `09-business-rules-catalog.md`, and the two program pages were updated. Five code findings went to `gaps.md`, including the phone not-entered test at `app/cbl/COACTUPC.cbl:2238-2239` and the date flag fall-through at `app/cpy/CSUTLDPY.cpy:315-327`.
- `check_package.py` after the rules work: 403 documents, 0 issues. Manual checks passed, and all 90 rule citations resolve to a line range inside an existing file.
- Seven more rules were added for the card-list search (`COCRDSLC`), the account-view search (`COACTVWC`), and the transaction-type update screen (`COTRTUPC`). `rules.json` now holds 50 rules. `BR-BASE-003` and `BR-BASE-004` now include those programs.
- One shareable walkthrough was written at `docs/application-documentation/CardDemo-end-to-end.md` and linked from `00-index.md`. `check_package.py`: 404 documents, 0 issues.
- The same walkthrough was written as `docs/application-documentation/CardDemo-end-to-end.docx` so it opens in Word. Flow diagrams are step lines. Source citations stay in the text.

## Resume pass (2026-10-13)

Discovery was re-run into `.mfdoc-tmp/inventory-resume.json` and compared with `docs/_work/inventory.json`. No application source `sha256` changed. Two new root files appeared: `COMBINED_DOCUMENTATION.md` and `PROJECT_DOCUMENTATION.docx`. Both are generated reading copies, so they were added to `exclude` in `docs-toolkit/project-profile.yaml`. The profile entry in `inventory.json` was updated (`sha256`, size, line count, and the `DFHMSD` prose line, now 111).

`docs/application-documentation/CardDemo-end-to-end.md` was missing, and `00-index.md` linked to it twice. The page was restored from `CardDemo-end-to-end.docx`. Diagrams are Mermaid again. Sign-on citations were re-checked against `app/cbl/COSGN00C.cbl:118-136` and `app/csd/CARDDEMO.CSD:378`.

`check_package.py`: 404 documents, 0 issues.

## Detailed coverage pass (2026-10-15)

Goal: paragraph-level documentation of every program, copybook and JCL member, rules for all 44 programs, measured coverage, and a classified gap report.

Review of the earlier state. The 404 documents reported by `check_package.py` were real files, but `check_package.py` only checks that each artifact name appears somewhere. Program pages listed paragraphs without their logic, 32 of 44 programs had no rule in `rules.json`, and no script compared parsed source elements with the pages. Defects found in earlier facts: spurious `MAINLINE` paragraphs in `CBPAUP0C`, `DBUNLDGS` and `PAUDBLOD`; the `XREF-FILE` DSN for `CBTRN02C` was taken from `CBEXPORT.jcl`; DD usage was derived from DISP (for example `TRANFILE` shown as read although the program opens it OUTPUT). The new pages derive DD usage from the program's OPEN mode and DSNs from the steps that run the program.

New scripts (orchestrator skill `scripts/`): `extract_structure.py`, `batch_manager.py`, `render_detail.py`, `coverage_validate.py`, `gap_report.py`. New contract `batch-analysis.md`. New rule `.cursor/rules/mainframe-doc-batching.mdc` (copy in the skill's `assets/rules/`).

Structure extracted: 44 programs, 881 paragraphs, 286 EXEC blocks, 62 CALLs, 54 SELECT/FD files, 2,327 program data items, 1,242 business-candidate decision points; 44 copybooks (41 COBOL + 3 DCLGEN), 559 fields, 70 88-levels, 366 COPY edges (0 missing members); 55 jobs, 7 PROC/template members, 163 steps, 792 DDs, 30 conditions; 89 CSD resources; 22 data definitions.

Batches: 10 (B01 auth, B02-B07 base, B08 trantype, B09 vsammq, B10 unused copybook). B01-B09 were analysed by one agent each; B10 by the orchestrator. All 10 validated by `batch_manager.py check docs/_work all`. Two validator defects were fixed during the pass: a trailing-newline off-by-one in line counting (it let `CSDB2RPY.cpy:88-90` pass on an 89-line file; corrected to 87-89) and copybook `source` fields under other keys not being range-checked.

Rules: `rules/rules.json` (schema `rules/2`) holds 392 rules: 342 from batch analysis and 50 earlier rules (`rules/rules-legacy.json`). Earlier-rule reviews: 41 confirmed, 6 corrected, 3 not reviewed because they cite Assembler `COBDATFT`, which is outside the COBOL batches. Five programs have no business rules, each with a recorded reason: `CBACT02C`, `CBACT03C`, `CBCUS01C`, `CBSTM03B`, `COBSWAIT`.

Validation: `coverage_validate.py` 26 of 26 criteria pass; 12,256 distinct source references resolve. `gap_report.py`: 361 components, 298 documented, 48 requires SME clarification, 15 unresolved, 0 missing, 0 unanalyzed, 0 partially documented; 55 inventory entries excluded with a reason. `check_package.py`: 419 documents, 0 issues. Page count: 404 earlier + 15 new pages (`06-batch/procs/` 7, `05-online/cics-resources.md`, `08-data/data-definitions.md`, `17-dependencies/` 4, `18-coverage/` 2) = 419.

## Statement-level validation pass (2026-10-16)

Goal: close gaps that the 26 criteria of 2026-10-15 could not see, and publish the complete package as one DOCX.

Gaps found in the 2026-10-15 state:
- `extract_structure.py` recorded literal MOVEs but silently dropped field-to-field MOVEs (2,908 statements). It also put procedure-division `COPY ... REPLACING` (48), `ENTRY 'DLITCBL'` (3) and `NEXT SENTENCE` (5) nowhere.
- Copybook pages had no field-level where-used list.
- No check tied a paragraph description to its code. 31 descriptions named nothing from their paragraph, for example generic text for `POPULATE-HEADER-INFO`.
- The three `COBDATFT` legacy rules had no review path.
- Copybook "requires SME clarification" entries in the gap report had empty reasons.
- Job pages for steps that run PROC `REPROC` did not show the dataset the PROC supplies (`app/proc/REPROC.prc:27-28`).
- `PROJECT_DOCUMENTATION.docx` (2026-10-13) is a summary and does not hold the detailed pages.

Changes:
- **Scripts (orchestrator skill `scripts/`).**
  - `extract_structure.py` records `data_moves`, classifies COPY, ENTRY, NEXT SENTENCE and ALTER as other statements, and records anything else as `unclassified` (currently 0). Structure summary counts are unchanged.
  - `render_detail.py` adds a statement inventory and lists every statement in source order per paragraph, adds "Field references by program" to copybook pages, lists PROC-supplied datasets on job steps, and shows reviews of non-COBOL legacy rules.
  - `batch_manager.py` adds the paragraph-logic grounding warning (`ungrounded_paragraphs`) and the `check-reviews` command for `semantic/reviews/<MEMBER>.json`.
  - `coverage_validate.py` adds 7 criteria: procedure statements, all decision points, dataflow edges, logic grounding, unclassified statements, rule traceability (anchor in cited lines, paragraph exists, legacy rules re-verified, rule in catalog), and scheduler edges. Data items are now matched by name and line.
  - `gap_report.py` feeds the new categories into component status, gives copybook SME flags a reason, includes copybook SME questions, and counts validated reviews as re-verification.
- **New QA script.** `mainframe-doc-assembly-qa/scripts/build_docx.py` writes every Markdown page into one DOCX.
- **Semantics.** 31 paragraph descriptions in 18 programs were rewritten from the source. `semantic/reviews/COBDATFT.json` confirms `BR-BASE-COBDATFT-001`, `-002` and `-003`, and widens the citation of `-003` to `app/asm/COBDATFT.asm:30-56`. It also records that R15 is always zero (`app/asm/COBDATFT.asm:61`).
- **Validator fixes made during the pass.** These are recorded here because they changed results, not pages.
  - Rule paragraphs that live in procedure copybooks (`CSUTLDPY`, `CSSTRPFY`) are looked up in the copybook structure.
  - A comma-separated paragraph list in `BR-BASE-COACTUPC-005` is split.
  - Dataflow edges citing the first line of a DD match the DD's line range on the page.

Validation (2026-10-16):
- `batch_manager.py check docs/_work all`: 44 programs and 44 copybooks validated, 0 ungrounded paragraphs. `check-reviews`: COBDATFT validated, 3 reviews.
- `coverage_validate.py`: 33 of 33 criteria pass. Coverage: 10,152 procedure statements, 2,230 decision points, 881 paragraphs grounded, 392 of 392 rules traceable, 81 scheduler edges, 243 dataflow edges, and 15,775 distinct source references resolve.
- `gap_report.py`: 361 components, 298 documented, 48 requires SME clarification, 15 unresolved, 0 missing, 0 unanalyzed and 0 partially documented. Registers: 120 SME questions, 74 conflicts, 10 ambiguous dependencies, 14 unresolved items. The unresolved items are 13 JCL symbolic-parameter sets plus `COCRDSEC`; the `COBDATFT` legacy rules have left this list.
- `check_package.py`: 419 documents, 0 issues.
- `CardDemo-complete-documentation.docx`: 419 pages and 15,782 distinct source references, with word count within 1% of the Markdown. Word opened it with 165,286 paragraphs and 2,240 tables.

## Resume pass (2026-10-19)

- `batch_manager.py status`: 10 batches and the COBDATFT review `validated`. `batch_manager.py check docs/_work all` recomputed source sha256 values: 44 programs and 44 copybooks validated with 0 issues, COBDATFT 3 reviews validated.
- Discovery was re-run into `.mfdoc-tmp/inventory-resume.json` (deleted afterwards). No application source was added, removed or changed. `docs-toolkit/README.md` had changed; its `sha256` and size were updated in `inventory.json`.
- New folder `AI-Documentation-Artifacts/` (541 files, commit `4226c2a`, 2026-10-15) is a snapshot copy of the skills, rules, `docs-toolkit` and `docs/_work` output. It was added to `exclude` in `docs-toolkit/project-profile.yaml` and is not inventoried. The profile entry in `inventory.json` was updated (`sha256`, size, `DFHMSD` prose line now 113).
- The `--exclude` flags passed to `classify_inventory.py` on the command line did not remove `docs/_work/**` or `docs/application-documentation/**` from the scratch output; the comparison filtered those paths afterwards. Check how the script applies `--exclude` on Windows before relying on it for a real inventory rebuild.
- Regenerated: `render_detail.py` (44 programs, 44 copybooks, 55 jobs, 392 rules), `coverage_validate.py` 33 of 33 pass (10,152 procedure statements, 2,230 decision points, 15,775 distinct references valid), `gap_report.py` (361 components: 298 documented, 48 requires SME clarification, 15 unresolved, 0 missing, 0 unanalyzed, 0 partially documented), `check_package.py` 419 documents 0 issues, `build_docx.py` 419 pages, `build_combined_markdown.ps1` 563 files.

## Requirements review pass (2026-10-19 to 2026-10-20)

Goal: confirm `COMBINED_DOCUMENTATION.md` answers the 10 review requirements (code, rules, copybooks, JCL and dependencies, outputs, traceability, automated validation, incremental execution, gap report, acceptance) and fix what does not.

Findings:
- All 12 Control-M edges and 15 Control-M job records in `batch/schedule.json` cited `app/scheduler/CardDemo.controlm` with no line number, and `coverage_validate.py` accepted that. Traceability gap.
- The gaps register still described the 2026-10-12 rules state ("Business rules not yet written one by one"), under a "Superseded" note.
- The combined file had a fixed date (16 October 2026), named `CardDemo-end-to-end.docx`, which is no longer in the output folder, and had no map from requirements to sections.

Changes:
- New `mainframe-doc-orchestrator/scripts/schedule_lines.py`: locates each Control-M edge by folder, job name and condition, and records the OUTCOND (+) line as `source` and the INCOND line as `incond_source`; JOB tag line on each job record. Run: 27 facts updated, 0 unresolved. Checked by hand against the XML: CLOSEFIL to TRANBKP is `app/scheduler/CardDemo.controlm:5` and `:9`; MNTTRDB2 to TRANEXTR is `:28` and `:59`.
- `render_detail.py`: job pages and `17-dependencies/job-dependencies.md` show both OUTCOND and INCOND lines.
- `coverage_validate.py`: a scheduler edge or script submit whose citation has no line number, or a Control-M edge without its INCOND line on a page, is no longer counted as documented. Negative test before re-rendering: 12 Control-M edges failed; after re-rendering 81 of 81 pass.
- `SKILL.md` (tool table and resume order) and `docs-toolkit/README.md` list `schedule_lines.py`. Inventory `sha256` of `docs-toolkit/README.md` updated.
- `gaps.md` and `16-gaps-assumptions-open-questions.md`: the stale section is replaced by "Business rules coverage status" with the current counts; the open `CBPAUP0C` formula question is kept.
- `build_combined_markdown.ps1`: adds "Requirements coverage summary" at the top of the combined file. Every figure is read from `coverage/coverage.json`, `coverage/gaps.json`, `rules/rules.json` and the program semantic files; the build fails if a link in that section has no target anchor. The document date is the date of the last validation run; the Word files are listed from the output folder.

## Architect review bundle pass (2026-10-20)

Goal: five separate review deliverables (detailed documentation, coverage validation report, business rules and traceability report, gap report, repeatable rules/skills/scripts).

Findings:
- `14-cross-reference-traceability.md` dated from A9: its rules table had 18 rows and no generator, so it no longer matched the 392 validated rules.
- Statements tagged Unverified in the work folder JSON were not listed in the gap report.
- `docs-toolkit/project-profile.yaml`: the `AI-Documentation-Artifacts/**` exclude entry was indented under the previous entry (invalid list item).

Changes:
- `render_detail.py`: new `traceability_page` writes `14-cross-reference-traceability.md`. It maps every rule to its program, paragraph, source lines, the CICS transactions that start or reach the program (through XCTL/LINK/CALL edges; Inferred when a hop uses a resolved dynamic name) and the JCL steps that run it, and adds online flows (transaction, program, CSD lines, mapsets, transfers) and batch flows (job, step, program, step lines). Result: 392 rule rows; 311 rules in programs reached from a transaction, 75 in programs run by a JCL step. Repeated resolved targets on one edge are listed once.
- `gap_report.py`: section "Unverified statements" and `unverified` in `gaps.json`: 72 items, each with its source line.
- `build_combined_markdown.ps1`: requirement 9 reports the Unverified count.
- New `docs/_work/check_instream_secrets.py`: fails when an FTP in-stream line of `app/jcl/FTPJCL.JCL` other than an FTP command appears in an output file; prints line numbers and counts only.
- New `docs/_work/build_review_bundle.ps1`: copies the validated package into `CardDemo-Architect-Review/` (five folders plus a README whose metrics are read from the JSON reports), runs the secrets check and writes `CardDemo-Architect-Review.zip`. Both paths are excluded in the profile.
- Profile exclude entry indentation fixed; `DFHMSD` prose line is now `project-profile.yaml:117` (inventory `evidence_line` and the gaps register updated). Inventory `sha256` of `docs-toolkit/README.md` and `project-profile.yaml` updated.
- `SKILL.md` and `docs-toolkit/README.md` describe the traceability page, the Unverified section and the bundle step.

Validation: see the final run at the end of this pass (`coverage_validate.py` all_pass, `check_package.py` issues, secrets check findings) recorded in `CardDemo-Architect-Review/README.md`.

## Final architect review pass (2026-10-20)

Audit of the first `CardDemo-Architect-Review.zip` and fixes; full list in `docs/_work/review-changelog.md` (copied to the bundle as `CHANGELOG.md`).
- Counts recounted from source: 44 `.cbl`; 41 `.cpy` + 3 `.dcl` = 44 layout pages (the DCLGEN members are `EXEC SQL INCLUDE`d, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:286`, `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:69`); 21 BMS symbolic maps; 46 `.jcl` in `app/` + 9 in `samples/jcl/` = 55 job pages; 6 `.prc` + 1 template = 7 PROC pages.
- `gap_report.py`: gap register (290 rows, all with line-level sources), conflict kinds, count reconciliation section. `render_detail.py`: derived paragraph/division on the traceability page.
- New `prepare_review_bundle.py`, `verify_review_bundle.py`, `write_review_readme.py`; `build_review_bundle.ps1` rebuilt (snapshot with redaction, link repair, independent verification, README, secrets check, ZIP re-verification).
- `00-index.md` links the gap register.

## Resume here

Run `batch_manager.py status docs/_work` first. If every batch is `validated` and no source changed, regenerate with `render_detail.py`, `coverage_validate.py`, `gap_report.py --claimed-pages 404`, `check_package.py`, `build_docx.py`, `build_combined_markdown.ps1` and `build_review_bundle.ps1` (commands in `docs-toolkit/README.md`). If a source changed: re-run discovery, then `extract_structure.py`, then `batch_manager.py check docs/_work all`; stale programs show `failed` with a sha256 issue and must be re-analysed per `batch-analysis.md` before re-rendering. Do not run `batch_manager.py init` on this work folder unless a new batch plan is intended. Python 3.1 is the interpreter; set `PYTHONIOENCODING=utf-8`.
