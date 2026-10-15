Add-Block 'Heading 1' '4. Repository Structure and Code Organization'
Add-Block 'Heading 2' '4.1 Top-level layout'
Add-Block 'Normal' 'The repository root holds the application, diagrams, a documentation toolkit, sample compile jobs, and shell scripts. The docs folder is analysis output produced from that source. It is not loaded by CICS or by a batch job. Editor rules under .cursor guide how this documentation was read. They are not part of the running application.'
Add-Block 'TreeText' 'repository root'
Add-Block 'TreeText' '|-- README.md, LICENSE, NOTICE, CONTRIBUTING.md, CODE_OF_CONDUCT.md'
Add-Block 'TreeText' '|-- app/'
Add-Block 'TreeText' '|   |-- asm/  bms/  cbl/  cpy/  cpy-bms/  csd/  ctl/  data/  jcl/  maclib/  proc/  scheduler/  catlg/'
Add-Block 'TreeText' '|   |-- app-authorization-ims-db2-mq/   (bms, cbl, cpy, csd, ddl, dcl, ims, jcl, data)'
Add-Block 'TreeText' '|   |-- app-transaction-type-db2/       (bms, cbl, cpy, csd, ddl, dcl, ctl, jcl)'
Add-Block 'TreeText' '|   |-- app-vsam-mq/                    (cbl, csd)'
Add-Block 'TreeText' '|-- diagrams/          screen images and data-model drawings'
Add-Block 'TreeText' '|-- docs/              analysis work files and the generated documentation package'
Add-Block 'TreeText' '|-- docs-toolkit/      project profile used by the documentation analysis'
Add-Block 'TreeText' '|-- samples/           compile JCL, compile procedures, and excluded runtime archives'
Add-Block 'TreeText' '|   |-- jcl/  proc/  m2/'
Add-Block 'TreeText' '`-- scripts/           upload, submit, and compile shell scripts, plus empty marker files'
Add-Block 'Evidence' 'Folder list confirmed by directory listing of the repository on 13 October 2026. Module assignment: docs-toolkit/project-profile.yaml:25-61.'

Add-Block 'Heading 2' '4.2 What each folder is for'
Add-Table @('Folder','Responsibility','Evidence') @(
    @('app/cbl','Base COBOL programs, online and batch.','31 COBOL programs in this folder. Two Assembler programs in app/asm bring the base module to 33.'),
    @('app/bms','BMS mapset source for the base screens.','17 base mapsets in the component inventory'),
    @('app/cpy-bms','Symbolic maps generated for those screens. COBOL programs reference these names.','Inventory type bms-symbolic-map'),
    @('app/cpy','Shared record layouts, the menu tables, the commarea, and edit routines.','Copybook members under app/cpy'),
    @('app/csd','CICS resource definitions for the base group CARDDEMO.','app/csd/CARDDEMO.CSD'),
    @('app/jcl','Batch jobs that load files, post, calculate interest, and open or close CICS files.','Job catalog'),
    @('app/proc','Procedures REPROC and TRANREPT. TRANREPT is the report procedure. Its first label in the member says REPROC.','app/proc/TRANREPT.prc:1 and :21'),
    @('app/asm and app/maclib','Date conversion routine COBDATFT and wait routine MVSWAIT, plus macros.','app/asm/COBDATFT.asm, app/asm/MVSWAIT.asm'),
    @('app/data','Sample data in ASCII and EBCDIC. The README names these as the files to load.','README.md:126-143, Unverified as a required load; files are present'),
    @('app/scheduler','CA7 export CardDemo.ca7 and Control-M export CardDemo.controlm.','Two scheduler files in the inventory'),
    @('app/catlg','A point-in-time LISTCAT report dated in the file, not a live catalog.','app/catlg/LISTCAT.txt'),
    @('app/ctl','IDCAMS REPRO control card used by procedure REPROC.','app/ctl/REPROCT.ctl'),
    @('samples/proc','Compile procedures for batch COBOL, CICS COBOL, CICS DB2 COBOL, and BMS.','samples/proc/BUILDBAT.prc and the siblings'),
    @('samples/jcl','Sample jobs that execute those procedures, plus RACF, sort, and repro samples.','samples/jcl'),
    @('samples/m2','Binary runtime archives. They are excluded from analysis and were not unpacked.','docs-toolkit/project-profile.yaml:76-78'),
    @('scripts','Shell scripts that pad members to 80 columns, upload them, and submit JCL to a listener.','scripts/upld_module.sh, scripts/remote_submit.sh')
)
Add-Block 'Evidence' 'Types and paths: docs/application-documentation/04-component-inventory.md, which lists every file in docs/_work/inventory.json.'

Add-Block 'Heading 2' '4.3 Online programs and what they own'
Add-Block 'Normal' 'An online program owns one screen conversation. It receives the commarea, sends a map, reads CICS files, and either returns to its own transaction or transfers to another program. The table names the program, the transaction that starts it, and the module. A one-line business label is taken from the menu literal or the CSD description where one exists. Program-header comments are not used as the label, because those comments are Unverified.'
Add-Table @('Program','Transaction','Module','Responsibility grounded in source') @(
    @('COSGN00C','CC00','base','Sign-on. Reads USRSEC and routes by user type.'),
    @('COMEN01C','CM00','base','User menu. Transfers to the eleven option programs.'),
    @('COACTVWC','CAVW','base','Account view. Reads the account file for a keyed account.'),
    @('COACTUPC','CAUP','base','Account update. Edits account and customer fields, then rewrites them.'),
    @('COCRDLIC','CCLI','base','Card list. Transfers to card view or card update.'),
    @('COCRDSLC','CCDL','base','Card view. Filters on account, card, or both.'),
    @('COCRDUPC','CCUP','base','Card update. Edits name, status, and expiry, then rewrites the card.'),
    @('COTRN00C','CT00','base','Transaction list. Can transfer to transaction view.'),
    @('COTRN01C','CT01','base','Transaction view. Can return to the list.'),
    @('COTRN02C','CT02','base','Creates rows on the transaction file. Detailed edits not fully catalogued.'),
    @('CORPT00C','CR00','base','Writes report JCL to queue JOBS.'),
    @('COBIL00C','CB00','base','Bill payment. Updates the account and creates a transaction.'),
    @('COADM01C','CA00','base','Admin menu. Transfers to user maintenance and transaction-type programs.'),
    @('COUSR00C','CU00','base','Lists user-security rows and can open update or delete.'),
    @('COUSR01C','CU01','base','Adds a user-security row.'),
    @('COUSR02C','CU02','base','Updates a user-security row.'),
    @('COUSR03C','CU03','base','Deletes a user-security row.'),
    @('COPAUS0C','CPVS','auth','Pending-authorization summary. Uses IMS.'),
    @('COPAUS1C','CPVD','auth','Pending-authorization detail. Links to COPAUS2C.'),
    @('COPAUS2C','(linked)','auth','DB2 table CARDDEMO.AUTHFRDS.'),
    @('COPAUA0C','CP00','auth','MQ-triggered authorization request.'),
    @('COTRTLIC','CTLI','trantype','Lists and deletes DB2 transaction types.'),
    @('COTRTUPC','CTTU','trantype','Adds or changes one DB2 transaction type.'),
    @('COACCT01','CDRA','vsammq','MQ account inquiry against VSAM.'),
    @('CODATE01','CDRD','vsammq','MQ date inquiry.')
)
Add-Block 'Normal' 'CICS also defines transaction CDV1 with program COCRDSEC. The program source is not in this repository. The definition is recorded as external-or-missing.'
Add-Block 'Evidence' 'Transactions: docs/application-documentation/05-online/transaction-catalog.md, citing the four CSD members. Missing program: app/csd/CARDDEMO.CSD:211 and :390, and docs/_work/gaps.md.'

Add-Block 'Heading 2' '4.4 Batch programs and what they own'
Add-Table @('Program','Started by','Module','Responsibility grounded in source') @(
    @('CBTRN02C','POSTTRAN step STEP15','base','Reads the daily file, posts valid records, writes rejects.'),
    @('CBACT04C','INTCALC step STEP15','base','Computes monthly interest and writes a transaction.'),
    @('CBTRN03C','TRANREPT procedure','base','Report program after the report procedure sorts transactions.'),
    @('CBTRN01C','No job, call, or transaction','base','Present in app/cbl. A comment calls it a batch post program. The comment is Unverified. The program is unreferenced.'),
    @('CBSTM03A','CREASTMT','base','Statement program named by the README and the job. Header text is Unverified.'),
    @('CBSTM03B','Called from the statement flow','base','Subprogram. See the program page for the call.'),
    @('CBACT01C, CBACT02C, CBACT03C, CBCUS01C','Batch jobs that read accounts, cards, customers','base','Read programs used by the READ* jobs. See each program page for the file.'),
    @('CBEXPORT, CBIMPORT','CBEXPORT and CBIMPORT jobs','base','Export and import programs for application files.'),
    @('COBSWAIT','WAITSTEP','base','Wait step used between a batch update and OPENFIL.'),
    @('CSUTLDTC','Called from date edits','base','Date validation subprogram used by account update.'),
    @('COBDATFT','Assembler, called for date conversion','base','Converts between two date presentations. Rules BR-BASE-COBDATFT-001 through 003.'),
    @('MVSWAIT','Assembler wait','base','Used with the ASMWAIT macro. Invoked from app/asm/MVSWAIT.asm.'),
    @('CBPAUP0C','CBPAUP0J','auth','Deletes expired IMS pending authorizations and adjusts counts.'),
    @('PAUDBLOD, PAUDBUNL, DBUNLDGS','LOADPADB, UNLDPADB, UNLDGSAM','auth','Load and unload programs for the IMS authorization data.'),
    @('COBTUPDT','MNTTRDB2','trantype','Applies insert, update, and delete actions to DB2 transaction types.')
)
Add-Block 'Evidence' 'Invocation column: docs/application-documentation/07-programs/index.md and the job facts. CBTRN01C orphan: docs/_work/gaps.md. COBDATFT rules: app/asm/COBDATFT.asm:30-56.'

Add-Block 'Heading 2' '4.5 Screens, copybooks, and the session block'
Add-Block 'Normal' 'Each BMS mapset is the picture of a screen: where fields sit, which ones the person can type, and which ones are protected. The symbolic map in cpy-bms is the COBOL view of those fields. Programs refer to field names such as the user id on the sign-on map. Twenty-one mapsets are in the inventory, seventeen in the base folder and the rest in the optional modules.'
Add-Block 'Normal' 'Copybooks hold the record layouts the programs share. CVACT01Y, CVACT02Y, CVACT03Y, and CVCUS01Y are the layouts the README associates with account, card, cross-reference, and customer data. CVTRA05Y and CVTRA06Y are associated with transactions. Several of those files share a record length with other copybooks, so a matching length alone does not prove which layout belongs to which dataset. The analysis leaves those layouts unbound and lists the candidates in the gaps register.'
Add-Block 'Normal' 'The session block CARDDEMO-COMMAREA carries the transaction and program the user came from, the user id, the user type, a small context flag, and customer and account fields. Programs pass that block on every transfer. That is how account update knows which menu to return to, and how sign-on tells the menu whether the person is an administrator.'
Add-Block 'Evidence' 'Mapset count: inventory type bms-mapset, 21. Commaarea: app/cpy/COCOM01Y.cpy:20-38. Unbound layouts: docs/_work/gaps.md, record layouts not tied to one store. README copybook column: README.md:131-143, Unverified where it conflicts with the unbound-length finding; the copybook text itself is Confirmed.'

Add-Block 'Heading 2' '4.6 Jobs, procedures, and schedulers'
Add-Block 'Normal' 'There are 55 JCL members. They fall into four groups. Load jobs define VSAM clusters and copy sample sequential files into them: ACCTFILE, CARDFILE, CUSTFILE, XREFFILE, TRANFILE, DISCGRP, TCATBALF, TRANCATG, TRANTYPE, and DUSRSECJ. Business jobs update data: POSTTRAN, INTCALC, COMBTRAN, CREASTMT, TRANBKP, and TRANIDX. Operations jobs close and open CICS files, wait, submit another job through the internal reader, or define CICS resources: CLOSEFIL, OPENFIL, WAITSTEP, INTRDRJ1, INTRDRJ2, and CBADMCDJ. Sample and optional jobs compile programs, run DB2 and IMS utilities, or exercise FTP, sort, and repro.'
Add-Block 'Normal' 'Procedure REPROC runs IDCAMS with control member REPROCT, whose statement copies INFILE to OUTFILE. TRANBKP, the report job, PRTCATBL, and REPRTEST use that procedure. Two copies of REPROCT exist and are byte-identical. Which copy is uploaded into the control library is not stated. The report procedure member is named TRANREPT, while its first JCL label says REPROC, and it then executes procedure REPROC. How the runtime treats that label is not stated.'
Add-Block 'Evidence' 'Job count: docs/application-documentation/06-batch/job-catalog.md. REPRO statement: app/ctl/REPROCT.ctl:15. Procedure label: app/proc/TRANREPT.prc:1. Upload uncertainty: docs/_work/gaps.md.'

Add-Block 'Heading 2' '4.7 How a request moves through the code'
Add-Block 'Normal' 'A screen request does not call a service layer. CICS starts the program named on the transaction. That program uses EXEC CICS to read or update a file, and EXEC CICS XCTL to give control to the next program. The commarea is the only application session. There is no separate API module, no REST resource, and no web service definition in the inventory.'
Add-Block 'Normal' 'A batch request is a job submitted by a person, by a shell script, by a scheduler export, or by the report program writing to queue JOBS. The job step names a program and the data sets that program opens. COBOL SELECT names are connected to those data sets by the DD names in the job.'
Add-Block 'Normal' 'An MQ request is different again. CICS starts COACCT01, CODATE01, or COPAUA0C because an MQ process triggered the transaction. The program reads the queue name from the trigger message, gets the request, and puts a reply. The programs that send the original request are not in this repository.'
Add-Block 'Evidence' 'CICS file and transfer style: navigation file docs/_work/online/navigation.json. MQ trigger: app/app-vsam-mq/cbl/COACCT01.cbl:191-197. No web-service resource type was required to explain the CSD members that were catalogued; URIMAP and WEBSERVICE were not part of the transaction catalog. Unavailable external callers of MQ.'

Add-Block 'Heading 2' '4.8 Files a new team member should open first'
Add-Block 'Bullet' 'README.md for the publisher description. Treat it as Unverified wherever it disagrees with code.'
Add-Block 'Bullet' 'app/csd/CARDDEMO.CSD for transactions, files, and the report queue.'
Add-Block 'Bullet' 'app/cbl/COSGN00C.cbl and app/cpy/COCOM01Y.cpy for sign-on and the session block.'
Add-Block 'Bullet' 'app/cpy/COMEN02Y.cpy and app/cpy/COADM02Y.cpy for the menus.'
Add-Block 'Bullet' 'app/cbl/CBTRN02C.cbl and app/jcl/POSTTRAN.jcl for daily posting.'
Add-Block 'Bullet' 'app/cbl/CBACT04C.cbl and app/jcl/INTCALC.jcl for interest.'
Add-Block 'Bullet' 'app/scheduler/CardDemo.ca7 and app/scheduler/CardDemo.controlm for the two schedules, read as separate lists.'
Add-Block 'Bullet' 'docs/application-documentation/00-index.md for the detailed package behind this narrative.'
Add-Block 'Evidence' 'Each path above is cited in Chapters 1 to 3.'

Add-Block 'Heading 1' '5. Technology Stack and Technology Usage Analysis'
Add-Block 'Heading 2' '5.1 Technology inventory'
Add-Block 'Normal' 'Technologies are listed because the source contains them. A technology with no artifact is omitted rather than assumed. Product versions are not taken from comments. A sample compile procedure names a CICS library OEM.CICSTS.V05R06M0. That is a data set name in the sample, not a statement that this repository was certified on that release.'
Add-Table @('Technology','Present','Where it shows up') @(
    @('COBOL','Yes','44 programs. Online, batch, DB2, and IMS.'),
    @('Assembler','Yes','COBDATFT and MVSWAIT, plus one macro and one copybook.'),
    @('CICS','Yes','Four CSD members, transactions, files, and one transient-data queue.'),
    @('BMS','Yes','21 mapsets and 21 symbolic maps.'),
    @('VSAM','Yes','KSDS, AIX, path, ESDS, and RRDS definitions.'),
    @('JCL and procedures','Yes','55 jobs and 6 procedures, plus one JCL template.'),
    @('CA7','Yes','app/scheduler/CardDemo.ca7.'),
    @('Control-M','Yes','app/scheduler/CardDemo.controlm.'),
    @('DB2','Yes','DDL, DCLGEN, and SQL in the optional modules.'),
    @('IMS DB','Yes','DBD and PSB members, and DLI calls in the authorization module.'),
    @('IBM MQ','Yes','Literal reply queues and trigger-message request queues.'),
    @('GDG','Yes','Generation data groups defined by DEFGDGB and used by rejects, backups, and reports.'),
    @('FTP','Yes','Job FTPJCL and the shell scripts that put JCL to a listener.'),
    @('DFSORT, IDCAMS, SDSF','Yes','Sort, cluster definition, and the CEMT commands issued through SDSF.'),
    @('RACF samples','Yes','samples/jcl/RACFCMDS.jcl. It is a sample command job, not a complete security design.'),
    @('HTTP, REST, or web services','No artifact','No WEBSERVICE or URIMAP implementation was catalogued as application behavior. The README lists web services as roadmap work.')
)
Add-Block 'Evidence' 'Inventory type counts from docs/_work/inventory.json. CICS library name: samples/proc/BUILDONL.prc:28. Roadmap: README.md:367-369, Unverified.'

Add-Block 'Heading 2' '5.2 Quantitative picture'
Add-Block 'Normal' 'The figures below are counts of source, not measures of production volume. No transaction-per-second figure, file record count from a live system, or batch elapsed time is in the repository. Sample data files exist. Their business meaning as a test population is Unverified beyond the README descriptions.'
Add-Table @('Item','Count','Notes') @(
    @('Inventory files','331','247 analysis status done, 80 not-analyzable, 2 pending README files, 2 excluded archives'),
    @('Sum of inventoried line counts','59,336','format.line_count across inventory files, including JCL and copybooks'),
    @('COBOL programs','44','Includes optional modules'),
    @('Assembler programs','2','COBDATFT, MVSWAIT'),
    @('Online CICS programs','19','runtime type cics-online'),
    @('Online programs that also use DB2','3','COTRTLIC, COTRTUPC, COPAUS2C'),
    @('MQ-triggered programs','3','COACCT01, CODATE01, COPAUA0C'),
    @('Batch main programs','11','Plus CBACT04C, which is both a batch main and a subprogram'),
    @('IMS batch programs','2 BMP and 2 DLI','CBPAUP0C, PAUDBLOD, PAUDBUNL, DBUNLDGS'),
    @('COBOL copybooks','41','Plus 21 BMS symbolic maps'),
    @('DB2 DDL members','7','Includes create scripts classified as DDL'),
    @('DB2 DCLGEN members','3','Host structures for the tables'),
    @('IMS DBD members','4','Including the authorization database and index'),
    @('IMS PSB members','4','Program specification blocks'),
    @('Shell scripts','9','Plus one awk script, scripts/pad.awk'),
    @('Empty marker files','48','scripts/markers, type placeholder, size 0. Names match application members and are not source.'),
    @('Dataset fact pages','204','160 sequential names, 13 KSDS, 10 GDG bases, 5 MQ queues, 3 DB2 tables, and smaller counts of AIX, path, ESDS, RRDS, GSAM, IMS, and the TD queue'),
    @('Largest program','COACTUPC, 3,744 code lines','Account update'),
    @('Smallest analyzed programs','MVSWAIT 12 code lines, COBSWAIT 19','Wait routines')
)
Add-Block 'Evidence' 'Computed from docs/_work/inventory.json and docs/_work/programs/*.json loc fields, and from store_kind on docs/_work/datasets/*.json, on 13 October 2026.'

Add-Block 'Heading 2' '5.3 COBOL and Assembler'
Add-Block 'Normal' 'COBOL is the language of the screens and of the batch updates. Programs are fixed-format. Some members also carry sequence numbers in columns 73 through 80. The analysis records that mixture rather than treating every file the same. Online programs use EXEC CICS. Batch programs use ordinary COBOL file READ and WRITE. DB2 programs add EXEC SQL. IMS programs add DLI calls.'
Add-Block 'Normal' 'Assembler is used for two small routines. COBDATFT converts a date between a form with hyphens and a form without them, and it rejects a type other than 1 or 2. MVSWAIT is the wait routine used by the batch pause. The README names both routines. The code confirms they exist. Their role is taken from the instructions, not from the README alone.'
Add-Block 'Evidence' 'Program fact languages: 44 COBOL, 2 Assembler. Fixed format is the profile setting docs-toolkit/project-profile.yaml:120-122, confirmed by the program facts source_format. Date rules: app/asm/COBDATFT.asm:30-56. README mention: README.md:48-50, consistent with the code.'

Add-Block 'Heading 2' '5.4 CICS, screens, and the shared session'
Add-Block 'Normal' 'CICS is the online container. A transaction code of four characters names a program. The base definitions live in group CARDDEMO. The optional modules have their own CSD members and groups. File definitions point at VSAM data sets and allow read, update, add, delete, and browse, with recovery set to none on the base account file and the same pattern on the other base files that were read.'
Add-Block 'Normal' 'The eight base files a screen program can open are listed below. Alternate indexes let a program reach a card from an account, or a cross-reference from an account, without using the primary key alone.'
Add-Table @('CICS file','Data set','What it holds, from the definition or description') @(
    @('ACCTDAT','AWS.M2.CARDDEMO.ACCTDATA.VSAM.KSDS','Account master'),
    @('CARDDAT','AWS.M2.CARDDEMO.CARDDATA.VSAM.KSDS','Card master'),
    @('CARDAIX','AWS.M2.CARDDEMO.CARDDATA.VSAM.AIX.PATH','Alternate index path for cards'),
    @('CUSTDAT','AWS.M2.CARDDEMO.CUSTDATA.VSAM.KSDS','Customer master. The CSD description says CARDDEMO CUSTOMER DATA.'),
    @('CCXREF','AWS.M2.CARDDEMO.CARDXREF.VSAM.KSDS','Card cross-reference. The CSD description says CARD TO ACCOUNT XREF.'),
    @('CXACAIX','AWS.M2.CARDDEMO.CARDXREF.VSAM.AIX.PATH','Alternate index by account. The CSD description says so.'),
    @('TRANSACT','AWS.M2.CARDDEMO.TRANSACT.VSAM.KSDS','Online transactions'),
    @('USRSEC','AWS.M2.CARDDEMO.USRSEC.VSAM.KSDS','User security')
)
Add-Block 'Evidence' 'app/csd/CARDDEMO.CSD:1-99. Descriptions: lines 38, 51, and 64.'

Add-Block 'Heading 2' '5.5 VSAM and the other stores'
Add-Block 'Normal' 'Keyed VSAM (KSDS) holds the masters the screens update. Alternate indexes (AIX) and paths provide a second key. Job ESDSRRDS defines an entry-sequenced and a relative-record version of a user-security name. Those clusters are additional definitions. The CICS file USRSEC points at the KSDS, not at the ESDS or the RRDS. Generation data groups hold successive backups, reject files, combined transactions, and reports. A new generation is requested with a relative name such as (+1) on the DD statement.'
Add-Block 'Normal' 'Sequential files are the inputs to the load jobs and the daily transaction file. Many dataset pages in the analysis are individual generations that appeared in a catalog listing or a JCL reference, which is why the dataset count is 204 while the number of business masters is much smaller.'
Add-Block 'Evidence' 'CICS USRSEC data set: app/csd/CARDDEMO.CSD:88-89. ESDS and RRDS: app/jcl/ESDSRRDS.jcl:65 and :99. GDG example: app/jcl/POSTTRAN.jcl:34-38. Store-kind counts: section 5.2.'

Add-Block 'Heading 2' '5.6 Batch, JCL, and the two schedulers'
Add-Block 'Normal' 'JCL is the batch language. A job names a program, a library AWS.M2.CARDDEMO.LOADLIB, and the data sets for that step. Symbolics such as &SYSUID stay unresolved unless the same job sets them. The two scheduler files are exports, not a single calendar. CA7 uses schedule ids whose meaning is not defined here. Control-M uses conditions inside folders. Shell scripts are a third submission path: they put JCL to a listener on localhost port 2121.'
Add-Block 'Evidence' 'Load library example: app/jcl/POSTTRAN.jcl:24-25. Listener: scripts/remote_submit.sh:14-24. Scheduler separation: docs/application-documentation/06-batch/batch-schedule-flow.md.'

Add-Block 'Heading 2' '5.7 DB2'
Add-Block 'Normal' 'DB2 appears only in the optional modules. Transaction types use schema CARDDEMO as a literal, database CARDDEMO, and plan CARDDEMO. The authorization module uses table CARDDEMO.AUTHFRDS, whose key begins with card number and authorization timestamp, and which also carries account id and customer id. Grants in the transaction-type create script give PUBLIC the ability to administer the database and to delete, insert, select, and update both type tables. Compile procedure BLDCIDB2 precompiles SQL, translates CICS, compiles, link-edits, and binds a package and a plan. The subsystem and plan name on that procedure are parameters, except where a job hard-codes plan CARDDEMO.'
Add-Block 'Evidence' 'DDL: app/app-transaction-type-db2/ddl/TRNTYPE.ddl:1-4, app/app-transaction-type-db2/ddl/TRNTYCAT.ddl:1-7, app/app-authorization-ims-db2-mq/ddl/AUTHFRDS.ddl:1-2. Grants: app/app-transaction-type-db2/ctl/DB2CREAT.ctl:52-59 and :103-105. Build: samples/proc/BLDCIDB2.prc:25.'

Add-Block 'Heading 2' '5.8 IMS'
Add-Block 'Normal' 'IMS is confined to the authorization module. Programs schedule PSB PSBPAUTB against DBD DBPAUTP0 for pending authorizations. Unload programs use other PSBs, PAUTBUNL and DLIGSAMP. Jobs run the IMS region controller and pass the application program name in the parameter string. No DBDGEN, PSBGEN, or ACBGEN job is in the repository, so the database can be described here and cannot be shown being generated.'
Add-Block 'Evidence' 'PSB and DBD: app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:75 and app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl:25. Missing gen jobs: docs/_work/gaps.md, operations leftovers.'

Add-Block 'Heading 2' '5.9 Message queues'
Add-Block 'Normal' 'MQ is used as a request and reply channel, not as a screen. The interfaces are the ones below. No MQ authority command was found, so who may put and get is unavailable.'
Add-Table @('Interface','Direction','Queue','Programs') @(
    @('IF-vsammq-001','Inbound','Name taken from the trigger message','COACCT01, CODATE01'),
    @('IF-vsammq-002','Outbound','CARD.DEMO.REPLY.ACCT','COACCT01'),
    @('IF-vsammq-003','Outbound','CARD.DEMO.REPLY.DATE','CODATE01'),
    @('IF-vsammq-004','Outbound','CARD.DEMO.ERROR','COACCT01, CODATE01'),
    @('IF-auth-001','Request and reply','Request from the trigger; reply from the message reply-to queue','COPAUA0C')
)
Add-Block 'Evidence' 'docs/application-documentation/10-integration-interfaces.md, citing app/app-vsam-mq/cbl/COACCT01.cbl:191-198 and :294, app/app-vsam-mq/cbl/CODATE01.cbl:147, and app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:238.'

Add-Block 'Heading 2' '5.10 File transfer and other utilities'
Add-Block 'Normal' 'Job FTPJCL contains an FTP script. A comment says the job receives a file. The command in the script is PUT. The comment is Unverified, and the command is Confirmed. The script also contains a user id and a password. Those values are not copied into this document. Shell scripts use a similar put, aimed at a job listener rather than at an application file.'
Add-Block 'Normal' 'Other utilities present as jobs, and not described further because they are samples or one-step tools, include text-to-PDF (TXT2PDF1), internal reader submission (INTRDRJ1 and INTRDRJ2), IDCAMS repro, and DFSORT. Job TXT2PDF1 is chained after CREASTMT in the CA7 export.'
Add-Block 'Evidence' 'app/jcl/FTPJCL.JCL:22, :30, :33, :36, and :40. CA7 chain: app/scheduler/CardDemo.ca7:468-527.'

Add-Block 'Heading 2' '5.11 Build and deployment'
Add-Block 'Normal' 'Building a program is a mainframe compile, not a local application build, except for one script that invokes the GnuCOBOL compiler on a file sample/cobol/SIZING.cbl. That source file is not in the repository. The sample procedures call the IBM compiler IGYCRCTL, the CICS translator DFHECP1$, the DB2 precompiler DSNHPC, the assembler ASMA90, and the binders HEWL and IEWL.'
Add-Table @('Kind of source','Procedure','Steps') @(
    @('Batch COBOL','BUILDBAT','Compile, listing, link-edit'),
    @('CICS COBOL','BUILDONL','Compile, listing, link-edit'),
    @('CICS and DB2 COBOL','BLDCIDB2','DB2 precompile, CICS translate, compile, link-edit, bind package, bind plan'),
    @('BMS map','BUILDBMS','Assemble the map, link-edit, assemble the symbolic map'),
    @('CICS and IMS sample','IMSMQCMP job, no shared procedure name','Translate, compile, link-edit with IEWL')
)
Add-Block 'Normal' 'Deployment, as far as the scripts show it, is upload then submit. upld_module.sh pads a member to 80 columns and puts it to a data set AWS.M2.CARDDEMO followed by a library type and a member name. remote_refresh.sh submits the close, the file loads, the user-security load, and the open. remote_compile.sh fills a JCL template and submits it. The README install sequence names many of the same jobs and adds DB2 and GDG setup. That README sequence is Unverified as a required order. The named members exist.'
Add-Block 'Normal' 'After a CICS compile, sample job CICCMP issues a NEWCOPY for a placeholder program name CICSPGMN. The BMS sample does the same for CICSMAP. Those names are samples in the job, not the application program names. Job CBADMCDJ runs DFHCSDUP to define group CARDDEMO. The install command in that job is a comment. The job comment says to install the group with CEDA.'
Add-Block 'Evidence' 'Procedures: samples/proc/BUILDBAT.prc:24, samples/proc/BUILDONL.prc:25, samples/proc/BLDCIDB2.prc:25, samples/proc/BUILDBMS.prc:23, samples/jcl/IMSMQCMP.jcl:28. Local compile: scripts/local_compile.sh:2. Upload: scripts/upld_module.sh:29-38. Refresh: scripts/remote_refresh.sh:9-50. NEWCOPY: samples/jcl/CICCMP.jcl:45-49. CSD job: app/jcl/CBADMCDJ.jcl:27-45.'

Add-Block 'Heading 2' '5.12 Interfaces in place of a web API'
Add-Block 'Normal' 'Readers looking for an application programming interface will find mainframe interfaces rather than HTTP endpoints. The stable online interface is the set of CICS transaction codes in the transaction catalog. The message interface is the set of MQ queues in section 5.9. The database interface is embedded SQL and DLI calls inside the optional programs, not a published query library. The batch interface is the job names and their DD names. The only internal hand-off from online to batch is queue JOBS.'
Add-Block 'Normal' 'There is no OpenAPI document, no URI map, and no client SDK in the inventory. The README lists exposure of transactions to distributed applications as future work. That item is Unverified and is not implemented in the programs reviewed here.'
Add-Block 'Evidence' 'Interface catalog: docs/application-documentation/10-integration-interfaces.md. Roadmap: README.md:366-369.'

Add-Block 'Heading 2' '5.13 Security observations'
Add-Block 'Normal' 'Application security is the user-security file plus the menu split. Platform security switches on the CICS transactions are set to no. DB2 grants in the sample create script are to PUBLIC. A point-in-time catalog listing shows RACF not indicated on the clusters it prints. That listing is dated in the file and is not a RACF rule. The RACF sample job alters a transaction group and connects one user to a group. It does not define a data-set profile. No MQ set-authority command was found. Passwords in the FTP script are not reproduced. A new user password is stored without the upper-case step that sign-on uses on input.'
Add-Block 'Evidence' 'docs/application-documentation/11-security-access.md. Catalog line: app/catlg/LISTCAT.txt:43. RACF sample: samples/jcl/RACFCMDS.jcl:19-29. Password store: app/cbl/COUSR01C.cbl:157.'

Add-Block 'Heading 2' '5.14 Testing and verification status'
Add-Block 'Normal' 'The repository does not contain a unit-test framework, a test script that asserts screen results, or a recorded test run. Two sample jobs, REPRTEST and SORTTEST, exercise the repro procedure and a sort. Their comments do not describe an application acceptance test. The README lists test creation as one reason a team might use the sample. That sentence is Unverified. Verification available from the source is static: the programs, the definitions, and the rules extracted from them. Runtime behavior of a particular CICS region is unavailable.'
Add-Block 'Evidence' 'Job pages docs/application-documentation/06-batch/jobs/REPRTEST.md and SORTTEST.md. README testing bullet: README.md:36, Unverified. No test directory in the repository listing.'

Add-Block 'Heading 2' '5.15 Data flow across a business day'
Add-Block 'Normal' 'During the day, signed-on programs read and update the VSAM masters. Account update changes the account and the customer. Card update changes the card. Transaction add and bill payment create transaction rows and, for bill payment, update the account. None of those online programs post the daily sequential file. That file is a batch input.'
Add-Block 'Normal' 'When a batch window runs, CLOSEFIL makes five of the online files unavailable to CICS. POSTTRAN reads the daily file, updates the account, the category balance, and the transaction master, and writes rejects. INTCALC, on its own chain, reads the category balance and the disclosure group and writes interest transactions. TRANBKP copies the transaction master. COMBTRAN combines transaction files. TRANIDX rebuilds the alternate index. OPENFIL returns the five files to CICS. The report path is independent: a person submits it from a screen, and the report procedure reads transactions for the dates entered.'
Add-Block 'Normal' 'Weekly, in the Control-M export, transaction-type maintenance runs against DB2 and an extract reloads the VSAM transaction-type files. Pending-authorization expiry runs on the CA7 chain before posting. These cadences are the names and conditions in the exports. They are not a confirmed operations calendar.'
Add-Block 'Evidence' 'Online file access is in the program pages cited in Chapter 3. Batch order is in section 3.15. Extract job: app/app-transaction-type-db2/jcl/TRANEXTR.jcl as catalogued, and Control-M condition WEEKLY-TransactionTypesDBRefresh-MNTTRDB2 in app/scheduler/CardDemo.controlm.'

Add-Block 'Heading 1' '6. Glossary and Technical References'
Add-Block 'Heading 2' '6.1 Glossary'
Add-Table @('Term','Meaning in this project') @(
    @('AIX','An alternate index on a VSAM cluster. Card data and the cross-reference both have one.'),
    @('BMS','Basic Mapping Support. The screen layouts in the bms folders.'),
    @('CA7','A scheduler. This repository contains an export, CardDemo.ca7, kept separate from Control-M.'),
    @('CICS','The online transaction monitor. Transaction codes such as CC00 start COBOL programs.'),
    @('COMMAREA','The block programs pass on a transfer. The layout name is CARDDEMO-COMMAREA.'),
    @('Control-M','A scheduler. This repository contains an export, CardDemo.controlm.'),
    @('Copybook','A shared COBOL layout included by COPY. Menus, records, and edit routines use them.'),
    @('CSD','The CICS resource definition file. CARDDEMO.CSD defines files, programs, transactions, and maps.'),
    @('DB2','The relational database used by the optional transaction-type and authorization modules.'),
    @('DFHMSD','The BMS macro that starts a mapset. Assembly chooses map or symbolic output through &&SYSPARM.'),
    @('DLI','The IMS data language used by the authorization programs.'),
    @('ESDS','Entry-sequenced VSAM. Defined by ESDSRRDS for a user-security name. CICS USRSEC uses the KSDS.'),
    @('GDG','Generation data group. A relative generation such as (+1) creates the next copy of a file.'),
    @('HLQ','High-level qualifier. A parameter in the README. Many jobs write the literal AWS.M2.CARDDEMO.'),
    @('IMS','The hierarchical database used for pending authorizations. Database description DBPAUTP0.'),
    @('JCL','Job control language. The batch jobs under app/jcl, the optional modules, and samples.'),
    @('KSDS','Key-sequenced VSAM. The account, card, customer, transaction, and user-security masters.'),
    @('MQ','IBM message queues. Reply queue names are literals. The request queue name comes from the trigger.'),
    @('PSB','IMS program specification block. Pending-authorization programs use PSBPAUTB.'),
    @('RACF','The security manager named by the README and by a sample command job. Not a complete rule set in this repository.'),
    @('RRDS','Relative-record VSAM. Also defined by ESDSRRDS, and not the file CICS opens as USRSEC.'),
    @('TD queue','Transient-data queue. JOBS is the queue that receives report JCL.'),
    @('VSAM','Virtual Storage Access Method. The file technology for the base masters.'),
    @('XCTL','The CICS command that transfers to another program and passes the commarea.'),
    @('Confirmed','The statement is in the code or definition cited.'),
    @('Inferred','The statement is reasoned from several cited facts, and the chain is given.'),
    @('Unverified','The statement comes from a comment, a README, or a diagram.'),
    @('Illustrative','An example invented for reading. Not a row from the sample data.'),
    @('Unavailable','The repository does not contain the fact. It is listed in the gaps section.')
)
Add-Block 'Evidence' 'Terms follow the artifacts in docs/_work/inventory.json and the glossary page docs/application-documentation/15-glossary.md, expanded for this narrative.'

Add-Block 'Heading 2' '6.2 Where the evidence lives'
Add-Table @('Need','Open this') @(
    @('Every file and its type','docs/_work/inventory.json and docs/application-documentation/04-component-inventory.md'),
    @('One program','docs/application-documentation/07-programs/ and docs/_work/programs/'),
    @('One job','docs/application-documentation/06-batch/jobs/ and docs/_work/jobs/'),
    @('Screens and navigation','docs/application-documentation/05-online/'),
    @('Data sets and layouts','docs/application-documentation/08-data/'),
    @('Business rules','docs/_work/rules/rules.json and Chapter 3 of this document'),
    @('MQ, IMS, and DB2 interfaces','docs/application-documentation/10-integration-interfaces.md'),
    @('Security','docs/application-documentation/11-security-access.md'),
    @('Compile and run','docs/application-documentation/13-build-deploy-operations.md'),
    @('Unknowns','docs/_work/gaps.md and section 6.4 of this document'),
    @('Publisher overview','README.md, tagged Unverified when the code does not repeat it')
)
Add-Block 'Evidence' 'Package index: docs/application-documentation/00-index.md.'

Add-Block 'Heading 2' '6.3 Document control'
Add-Table @('Item','Value') @(
    @('Document','PROJECT_DOCUMENTATION.docx'),
    @('Application','CardDemo'),
    @('Repository','aws-mainframe-modernization-carddemo'),
    @('Document date','13 October 2026'),
    @('Evidence snapshot','docs/_work analysis of the source in this working copy'),
    @('License file','Apache License, Version 2.0 (LICENSE:1-3)'),
    @('Application source','Not modified by this document')
)
Add-Block 'Normal' 'Source file banners name Amazon.com, Inc. or its affiliates and point at the Apache License, Version 2.0. That notice is what the files contain. This document does not add a legal interpretation beyond the presence of LICENSE.'
Add-Block 'Evidence' 'Example notice: app/bms/COSGN00.bms:3-17. LICENSE:1-3.'

Add-Block 'Heading 2' '6.4 Unresolved documentation gaps'
Add-Block 'Normal' 'These items are unavailable or only partly resolved. They are stated here so a reader can see the boundary of the document. None of them was filled with an assumed value.'
Add-Block 'Heading 3' 'Behavior the source does not decide'
Add-Block 'Bullet' 'The MQ request queue name is copied from the trigger message. The MQ process definition that would name it is not in the repository.'
Add-Block 'Bullet' 'Program COCRDSEC is defined in the CSD and has no source member here.'
Add-Block 'Bullet' 'DSNTIAD is named in a DB2 control script and is not an application member. Whether it is an IBM-supplied program is not decided by this repository.'
Add-Block 'Bullet' 'Queue JOBS uses DD name INREADER. The CICS region JCL that defines that DD is absent, so submission of the report job is unverified.'
Add-Block 'Bullet' 'CA7 schedule ids 030, 031, and 032 have no definition that says what they mean. CA7 jobs CLOSEFIL1 and CLOSEFIL2 point at member CLOSEFIL. No job card is named CLOSEFIL1 or CLOSEFIL2.'
Add-Block 'Bullet' 'The symbol &CARDDEMOPRODJCL has no data set name in the repository.'
Add-Block 'Bullet' 'Control-M folder names include WEEKLY, and the folder has no DAYS attribute.'
Add-Block 'Bullet' 'No running CICS region, response-time target, or test-run log is stored here.'
Add-Block 'Heading 3' 'Layouts and references that stay ambiguous'
Add-Block 'Bullet' 'Several VSAM record lengths match more than one copybook, including the cross-reference, customer, transaction, and user-security lengths. The analysis does not force a single layout onto those files.'
Add-Block 'Bullet' 'Copybook UNUSED1Y is not copied by any scanned program.'
Add-Block 'Bullet' 'Program CBTRN01C is not the target of a CSD definition, a job step, a call, or a CICS link.'
Add-Block 'Bullet' 'Two copies of control card REPROCT are byte-identical. The repository does not say which copy is uploaded.'
Add-Block 'Bullet' 'Procedure member TRANREPT begins with the label REPROC. Runtime treatment of that mismatch is not stated.'
Add-Block 'Bullet' 'Jobs TRANREPT and DEFCUST each reuse a step name. A step-qualified override of those names is ambiguous.'
Add-Block 'Heading 3' 'Rules and operations not fully written'
Add-Block 'Bullet' 'Field edits in COUSR01C, COUSR02C, COUSR03C, and COTRN02C are still in the source and are not one-by-one rules in the catalog.'
Add-Block 'Bullet' 'Bill-payment field rules were not extracted. File access and navigation were.'
Add-Block 'Bullet' 'COBTUPDT has no SQL COMMIT. The place the plan commits is not stated.'
Add-Block 'Bullet' 'No DBDGEN, PSBGEN, ACBGEN, or MQ authority job was found.'
Add-Block 'Bullet' 'scripts/local_compile.sh names sample/cobol/SIZING.cbl, which is not in the repository.'
Add-Block 'Bullet' 'The README install order is Unverified. The shell-script order is the confirmed submission order for those scripts.'
Add-Block 'Heading 3' 'Code observations left as written'
Add-Block 'Bullet' 'Account-update phone test checks the area-code field where the line number is expected (app/cbl/COACTUPC.cbl:2238-2239).'
Add-Block 'Bullet' 'A failed date-routine call still marks the date flags valid, while the update remains blocked (app/cpy/CSUTLDPY.cpy:315-327).'
Add-Block 'Bullet' 'Card update and account update disagree on a zero account number.'
Add-Block 'Bullet' 'Card-update comments disagree with the expiry-year test. The code accepts 1950 through 2099.'
Add-Block 'Bullet' 'Daily posting overwrites reason 102 with reason 103 when both the limit and the expiration fail.'
Add-Block 'Bullet' 'Version banners and the README badge do not name one release. The version script sets v2.0 and is not shown running.'
Add-Block 'Evidence' 'Full register: docs/_work/gaps.md. This section is a reading of that register, not a new discovery pass. Each bullet cites a location already recorded there or in Chapter 3.'

Add-Block 'Heading 2' '6.5 Transaction reference'
Add-Block 'Normal' 'The full online transaction list is repeated here so a tester or a new developer can find a code without returning to Chapter 3. Mapset and rule columns come from the transaction catalog. An empty rule cell means no rule identifier was attached to that transaction in the catalog, not that the program has no validation.'

$tx = Get-FirstMarkdownTable (Join-Path $script:RepoRoot 'docs\application-documentation\05-online\transaction-catalog.md')
Add-Table $tx.Headers $tx.Rows
Add-Block 'Evidence' 'docs/_work/online/transactions.json and docs/application-documentation/05-online/transaction-catalog.md.'
