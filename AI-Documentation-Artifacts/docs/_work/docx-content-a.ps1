Add-Block 'Title' 'AWS Mainframe Credit Card Demo'
Add-Block 'Subtitle' 'CardDemo project documentation'
Add-Block 'Normal' 'A guide for executives, business analysts, developers, testers, architects, and new team members.'
Add-Block 'Normal' 'Document date: 13 October 2026. The facts come from the source in this repository and from the completed analysis under docs/_work. This file does not describe a live CICS region, because the repository does not record one.'
Add-Block 'Evidence' 'Inventory snapshot: docs/_work/inventory.json, 331 files. License text: LICENSE:1-3, Apache License, Version 2.0. README version badge: README.md:3, Unverified as a running version.'

Add-Callout 'How confidence is marked' @'
Confirmed means the code, a definition, or a counted file states the fact. The citation is a repository path and line, or a count taken from the analysis files.

Inferred means the conclusion follows from several confirmed facts. The chain is stated.

Unverified means the statement comes from README.md, a comment, or a diagram, and the code does not state it.

Illustrative means an example invented so a reader can follow a workflow. Illustrative names and amounts are not rows from app/data.

Unavailable means the repository does not contain the information. Unavailable items are listed again in the gaps section. They are not filled in with guesses.
'@

Add-SectionBreak

Add-Block 'Heading 1' 'How to read this document'
Add-Block 'Normal' 'Start with the executive summary if you need the shape of the project in a few pages. Read the workflow chapter if you need to follow what a person does on a screen, and what the nightly and monthly jobs do with the same files. Read the repository and technology chapters if you are about to change, test, or move the code. Use the glossary when a mainframe term appears for the first time.'
Add-Block 'Normal' 'Each factual passage is followed by a short evidence line in smaller italic type. That line is the trace back to the repository. A longer per-program and per-job package already exists under docs/application-documentation. This document is the single narrative. It does not replace the line-level program pages.'
Add-Block 'Heading 2' 'Contents'
$tocRange = $script:Doc.Range()
$tocRange.Collapse(0)
$null = $script:Doc.TablesOfContents.Add($tocRange, $true, 1, 3)
$afterToc = $script:Doc.Range()
$afterToc.Collapse(0)
$afterToc.InsertParagraphAfter() | Out-Null
Add-Block 'Evidence' 'The contents list is a Word field. It lists Heading 1, Heading 2, and Heading 3. Open the document in Microsoft Word if the page numbers need a refresh.'

Add-SectionBreak

Add-Block 'Heading 1' '1. Executive Summary'
Add-Block 'Heading 2' '1.1 What this project is'
Add-Block 'Normal' 'CardDemo is a sample credit-card servicing application written for a mainframe. A person signs on at a screen. The application then shows either an administrator menu or a regular-user menu. From those menus the person can look at and change accounts, cards, customers, transactions, and, for an administrator, user-security records. Separate batch jobs post a daily transaction file and calculate interest. The sign-on screen itself calls the application a credit card demo for mainframe modernization.'
Add-Block 'Normal' 'The repository holds the source for that sample, three optional add-on modules, sample compile jobs, and shell scripts that upload and submit work. It is application source plus the jobs that prepare it. It is not a running system, a cloud service, or a web application.'
Add-Block 'Evidence' 'Confirmed screen text: app/bms/COSGN00.bms:98-99. Confirmed source layout: docs-toolkit/project-profile.yaml:16-61 and the folders under app/. Unverified product description: README.md:1 and README.md:5-7.'

Add-Block 'Heading 2' '1.2 Why it exists'
Add-Block 'Normal' 'The programs implement day-to-day card servicing: identify the person, show the matching menu, maintain account and card data, record transactions, and run batch updates against the same files. That is the behavior the code carries out.'
Add-Block 'Normal' 'The README gives a different reason for the repository itself. It says the sample exists so that teams can practice discovery, migration assessment, performance testing, and service enablement against a realistic mainframe codebase, including mixed coding styles. That purpose is the stated reason the sample was published. It is not a requirement encoded in COBOL, and the repository contains no project charter, sponsor statement, or success metric.'
Add-Block 'Evidence' 'Unverified purpose: README.md:28-38. Confirmed absence of a charter: no requirements file is in the inventory (docs/_work/inventory.json).'

Add-Block 'Heading 2' '1.3 The problem the code addresses'
Add-Block 'Normal' 'No separate problem statement is stored in the repository. The problem that can be read from the implementation is operational. Cardholder data is split across account, customer, card, and cross-reference records. A person must be identified before data is shown. Online updates and batch updates share files, so the batch chains close those files, update them, and open them again.'
Add-Block 'Evidence' 'Confirmed cross-reference fields: app/cpy/CVACT03Y.cpy:5-6 and app/jcl/XREFFILE.jcl:74. Confirmed sign-on rejection: app/cbl/COSGN00C.cbl:211-256. Confirmed close and open: app/jcl/CLOSEFIL.jcl:26-30 and app/jcl/OPENFIL.jcl:26-30.'

Add-Block 'Heading 2' '1.4 Who uses it'
Add-Block 'Normal' 'Two roles are defined in the shared session block that programs pass to one another. User type A is an administrator. User type U is a regular user. After a matching password, type A is transferred to the admin menu program COADM01C. Any other type is transferred to the user menu program COMEN01C.'
Add-Block 'Normal' 'No call-center role, auditor, cardholder self-service role, or bank customer is named in the code. The person at the screen is an internal user of the servicing application. Someone installing the sample on a mainframe is described in the README. That installer is Unverified as an application role.'
Add-Block 'Evidence' 'Confirmed roles: app/cpy/COCOM01Y.cpy:26-28. Confirmed routing: app/cbl/COSGN00C.cbl:230-239. Unverified installer: README.md:96-99.'

Add-Block 'Heading 2' '1.5 How it works'
Add-Block 'Normal' 'A person starts transaction CC00. Program COSGN00C checks the user-security file and opens one of the two menus. Each menu option starts another COBOL program. The programs talk to each other by transferring control and passing a shared block named CARDDEMO-COMMAREA. Screens are BMS maps. The business files are VSAM.'
Add-Block 'Normal' 'Separately, scheduler exports and shell scripts run batch jobs. Those jobs close selected online files, post transactions or calculate interest, wait, and open the files again. From the reports screen, program CORPT00C writes a batch job into a CICS queue instead of printing the report itself.'
Add-Figure $script:Figures.Context 'Figure 1. Base online work, batch work, and the three optional modules. Boundaries are taken from the source folders and the scheduler exports.'
Add-Block 'Evidence' 'Confirmed transaction CC00: app/csd/CARDDEMO.CSD:378. Confirmed commarea: app/cpy/COCOM01Y.cpy:20-31. Confirmed report queue: app/cbl/CORPT00C.cbl:497-520 and app/csd/CARDDEMO.CSD:499-501.'

Add-Block 'Heading 2' '1.6 What is implemented today'
Add-Block 'Normal' 'The source for the base application and the three optional modules is in this repository. The optional modules cover pending authorizations (IMS, DB2, and MQ), DB2 transaction types, and account and date replies over MQ. Compile procedures and upload scripts are present. A documentation package generated from this source is under docs/application-documentation. That package describes the application. It is not the application.'
Add-Block 'Normal' 'Nothing in the repository records that a CICS region is running this code. The README says the optional features have been added and was last updated in April 2025. That status sentence is Unverified. The README roadmap lists DB2 rewards, IMS DC, SFTP, and web services as future work. Those items are not implemented in the programs inventoried for this document.'
Add-Block 'Evidence' 'Confirmed folders: app/, app/app-authorization-ims-db2-mq/, app/app-transaction-type-db2/, app/app-vsam-mq/. Unverified status and roadmap: README.md:359-369 and README.md:386-397.'

Add-Block 'Heading 3' 'Size at a glance'
Add-Table @('Measure','Value','What it counts') @(
    @('Inventory files','331','Every classified file in docs/_work/inventory.json'),
    @('Program facts','46','COBOL and Assembler members with a program page'),
    @('Code lines in those programs','26,341','loc.code summed across the 46 program facts'),
    @('Total lines in those programs','30,289','loc.total summed across the same facts'),
    @('CICS transactions','25','Definitions across the four CSD members'),
    @('BMS mapsets','21','Screen layouts'),
    @('JCL jobs','55','Job members in app, the optional modules, and samples'),
    @('Dataset fact pages','204','Named data stores in the analysis, including generations'),
    @('Confirmed business rules','50','Decisions extracted into docs/_work/rules/rules.json'),
    @('Integration interfaces','14','MQ, IMS, DB2, the report queue, and file transfer')
)
Add-Block 'Evidence' 'Counts taken from docs/_work/inventory.json, docs/_work/programs/, docs/_work/rules/rules.json, docs/_work/datasets/, and the catalogs in docs/application-documentation. Confirmed as analysis counts on 13 October 2026.'

Add-Block 'Heading 1' '2. Introduction and Project Background'
Add-Block 'Heading 2' '2.1 Purpose and objectives'
Add-Block 'Normal' 'The implemented purpose is credit-card account servicing. A signed-on session can view and update cardholder data. Batch jobs can post a daily transaction file and calculate interest while selected online files are closed. That purpose is read from the programs and jobs, not from a charter.'
Add-Block 'Normal' 'The published objective in the README is to give migration and modernization tools a realistic mainframe application to work against. No objective list, benefit target, or acceptance criterion is stored beside that README text.'
Add-Block 'Evidence' 'Confirmed servicing behavior is detailed in Chapter 3. Unverified modernization objective: README.md:28-38.'

Add-Block 'Heading 2' '2.2 Business context'
Add-Block 'Normal' 'The card portfolio in the base application is stored in VSAM. An account, a customer, and a card are tied together by a cross-reference record. Transactions are stored in their own keyed file. A disclosure group and a transaction-category balance support interest calculation. User ids and passwords live in a separate user-security file.'
Add-Block 'Normal' 'Optional modules add other stores. Pending authorizations use an IMS database. Fraud-related authorization rows use a DB2 table. Transaction-type reference data uses two DB2 tables. Account and date inquiries answer through MQ.'
Add-Figure $script:Figures.Data 'Figure 2. Relationships that the source cites. The arrows are fields, not an assumed banking data model.'
Add-Block 'Evidence' 'Confirmed relationships: docs/application-documentation/08-data/data-model.md, citing app/cpy/CVACT03Y.cpy:5-6, app/jcl/XREFFILE.jcl:74, and app/app-authorization-ims-db2-mq/ddl/AUTHFRDS.ddl:2 and :26-27.'

Add-Block 'Heading 2' '2.3 Scope'
Add-Block 'Heading 3' 'In scope'
Add-Block 'Bullet' 'Base online and batch source under app/cbl, app/bms, app/jcl, app/cpy, app/csd, app/proc, app/asm, and app/scheduler.'
Add-Block 'Bullet' 'The authorization module, the transaction-type module, and the VSAM-MQ module, each in its own folder.'
Add-Block 'Bullet' 'Compile and upload samples under samples/ and scripts/.'
Add-Block 'Bullet' 'Sample data files under app/data, in ASCII and EBCDIC copies, as data rather than as programs.'
Add-Block 'Heading 3' 'Outside what this repository can confirm'
Add-Block 'Bullet' 'A running CICS region, a DB2 subsystem, an IMS control region, or an MQ queue manager.'
Add-Block 'Bullet' 'The roadmap items named in the README: DB2 rewards, IMS DC, SFTP, and web services.'
Add-Block 'Bullet' 'A production operations manual. Job comments and the README install order are not a confirmed run book.'
Add-Block 'Bullet' 'Performance targets, recovery-time objectives, and service levels. None are stated.'
Add-Block 'Evidence' 'Scope of source: docs-toolkit/project-profile.yaml:16-61. Roadmap: README.md:359-369, Unverified, and absent from the program inventory.'

Add-Block 'Heading 2' '2.4 Functional scope'
Add-Block 'Normal' 'The application does the following. Each item is Confirmed unless the sentence says otherwise.'
Add-Block 'Bullet' 'Authenticate a user id and password and choose a menu.'
Add-Block 'Bullet' 'View and update an account and the related customer.'
Add-Block 'Bullet' 'List, view, and update cards.'
Add-Block 'Bullet' 'List, view, and add transactions.'
Add-Block 'Bullet' 'Submit a transaction report job for a date range entered on the screen.'
Add-Block 'Bullet' 'Open a bill-payment screen, read and update the account file, and write a transaction. Field-by-field rules for that screen were not extracted.'
Add-Block 'Bullet' 'Maintain user ids from the admin menu: list, add, update, and delete.'
Add-Block 'Bullet' 'When the add-on programs are installed, list pending authorizations and maintain DB2 transaction types.'
Add-Block 'Bullet' 'Post a daily transaction file and calculate interest in batch.'
Add-Block 'Evidence' 'Menu literals: app/cpy/COMEN02Y.cpy:21-90 and app/cpy/COADM02Y.cpy:22-53. Bill-payment file access: app/cbl/COBIL00C.cbl:345-512. Report submit: app/cbl/CORPT00C.cbl:83-121.'

Add-Block 'Heading 2' '2.5 Qualities the source shows'
Add-Block 'Normal' 'These are observed properties of the source. They are not written requirements.'
Add-Table @('Quality','What the repository shows','Tag') @(
    @('Identification','Sign-on upper-cases the user id and password, then compares the password with the user-security file.','Confirmed'),
    @('Menu separation','Type A reaches the admin menu. Every other type reaches the user menu.','Confirmed'),
    @('Platform security switches','CICS transaction definitions set resource security and command security off.','Confirmed'),
    @('DB2 privileges','The transaction-type create script grants database administration and table changes to PUBLIC.','Confirmed'),
    @('Shared-file discipline','Scheduler chains close files, update, wait, and reopen them.','Confirmed pattern'),
    @('Response time','No response-time or throughput figure is in the source.','Unavailable'),
    @('Recovery objective','File definitions in the base CSD set RECOVERY(NONE). No recovery-time objective is stated.','Confirmed setting; numeric target unavailable'),
    @('Maintainability','Optional features are separate folders. The README says coding styles were mixed on purpose.','Folder split Confirmed; motive Unverified')
)
Add-Block 'Evidence' 'Sign-on: app/cbl/COSGN00C.cbl:132-136 and :223. Security switches: app/csd/CARDDEMO.CSD:314. DB2 grants: app/app-transaction-type-db2/ctl/DB2CREAT.ctl:52-59 and :103-105. Recovery attribute example: app/csd/CARDDEMO.CSD:9. Motive: README.md:38, Unverified.'

Add-Block 'Heading 2' '2.6 People and roles'
Add-Table @('Party','What the repository says','Tag') @(
    @('Regular user, type U','Defined on the commarea. Receives the user menu.','Confirmed'),
    @('Administrator, type A','Defined on the commarea. Receives the admin menu after a matching password.','Confirmed'),
    @('Installer of the sample','Described in the README installation section.','Unverified'),
    @('Cardholder, auditor, or bank customer','Not named in the programs or menus.','Unavailable')
)
Add-Block 'Evidence' 'app/cpy/COCOM01Y.cpy:27-28. README.md:96-99 and README.md:239-243.'

Add-Block 'Heading 2' '2.7 The four source modules'
Add-Block 'Normal' 'The analysis assigns each file to a module by the longest matching path. The base module is the card-servicing application. Three modules are optional add-ons. A build module holds compile samples and scripts. Twenty files sit outside those modules: the repository license and community files, the README, diagrams, and the documentation toolkit profile.'
Add-Table @('Module','Files','What it contains') @(
    @('base','169','COBOL, BMS, JCL, copybooks, CSD, Assembler, schedulers, and sample data'),
    @('build','71','Sample compile JCL and procedures, shell scripts, and empty marker files'),
    @('auth','40','Pending authorizations with IMS, DB2, and MQ'),
    @('trantype','27','Transaction-type maintenance on DB2'),
    @('vsammq','4','Two MQ programs and their CICS definitions'),
    @('No module','20','License, README, diagrams, and toolkit files')
)
Add-Block 'Evidence' 'Module globs: docs-toolkit/project-profile.yaml:63-69. Counts from docs/_work/inventory.json on 13 October 2026.'

Add-Block 'Heading 2' '2.8 Parameters an environment must supply'
Add-Block 'Normal' 'Several names in JCL and in the READMEs are parameters. This document does not invent values for them. Where a job also contains a literal, both are recorded.'
Add-Table @('Token','How to read it','Evidence') @(
    @('&HLQ','High-level qualifier for datasets. The README describes it. Job CBADMCDJ sets HLQ=AWS.M2.CARDDEMO. BUILDONL defaults HLQ to empty.','README.md:108; app/jcl/CBADMCDJ.jcl:25; samples/proc/BUILDONL.prc:26'),
    @('&SYSUID','User id notified when a job ends.','app/jcl/CBADMCDJ.jcl:2'),
    @('&SSID and &PLAN','DB2 subsystem and plan name passed into the DB2 compile procedure. Job MNTTRDB2 uses the literal plan CARDDEMO.','samples/proc/BLDCIDB2.prc:143 and :168; app/app-transaction-type-db2/jcl/MNTTRDB2.jcl:30'),
    @('&CARDDEMOPRODJCL','CA7 library symbol. The data set name is not in this repository.','app/scheduler/CardDemo.ca7:35'),
    @('CICSAWSA','Literal CICS region name in the operator commands that close and open files.','app/jcl/CLOSEFIL.jcl:26'),
    @('<<db2-schema>>','Named in the authorization README. The transaction-type DDL uses the literal schema CARDDEMO.','app/app-authorization-ims-db2-mq/README.md:113; app/app-transaction-type-db2/ddl/TRNTYPE.ddl:1'),
    @('&&SYSPARM','BMS assembly switch. The sample BMS procedure sets MAP and, in a later step, DSECT.','samples/proc/BUILDBMS.prc:49 and :78')
)
Add-Block 'Evidence' 'Parameter list aligned with docs/application-documentation/13-build-deploy-operations.md and docs-toolkit/project-profile.yaml:103-114.'

Add-Block 'Heading 2' '2.9 What a reader should expect from the code'
Add-Block 'Normal' 'Most dataset names in the JCL and in the CICS file definitions are written out in full as AWS.M2.CARDDEMO followed by a further qualifier. That pattern is an observation about this repository. It is not a rule for naming new files. Version banners inside source members are not uniform. Many read CardDemo_v1.0-15-g27d6c6f-68. The admin menu copybook and the posting program carry later banners, including a v2.0 form. A script in the repository sets a variable app_version to v2.0 and can rewrite banners, and nothing in the repository shows that script being run. The README badge says 1.0.0. Treat the badge and the banners as labels in files, not as proof of a single deployed release.'
Add-Block 'Evidence' 'Example banner: app/cbl/COSGN00C.cbl:259 and app/proc/REPROC.prc:31. Later banners: app/cpy/COADM02Y.cpy:61 and app/cbl/CBTRN02C.cbl version banner recorded on the program page. Script: scripts/git-addSrcVersionInfo.sh:12. Badge: README.md:3, Unverified as a runtime version.'
