Add-Block 'Heading 1' '3. Business Workflow and Use Cases'
Add-Block 'Heading 2' '3.1 A session in plain language'
Add-Block 'Normal' 'Online work is a conversation of screens. The person types a four-character transaction code, CC00, to begin. CICS starts the sign-on program. That program sends a screen, receives the user id and password, and either transfers to a menu or redisplays sign-on with a message. From a menu, the person types an option number. The menu program transfers to the program named for that option and passes the shared session block, so the next program knows who signed on and which program sent them.'
Add-Block 'Normal' 'Leaving a screen is the reverse transfer. Many programs return to the menu that called them. PF3 on either menu returns to sign-on. Each program also has its own sign-off path back to COSGN00C. While a person is on a screen, CICS keeps the task alive with a return to the same transaction, which is why the transaction catalog shows both a starting program and a return-to-transaction.'
Add-Block 'Evidence' 'Sign-on return transaction CC00: app/cbl/COSGN00C.cbl:98. Menu PF3: app/cbl/COMEN01C.cbl:96-98 and app/cbl/COADM01C.cbl:100-102. Empty return target becomes COSGN00C: app/cbl/COMEN01C.cbl:198-200 and app/cbl/COADM01C.cbl:165-167. Rule ids BR-BASE-001 and BR-BASE-002.'

Add-Block 'Heading 2' '3.2 Sign-on'
Add-Block 'Normal' 'The sign-on screen asks for an 8-character user id and an 8-character password, then tells the person to press Enter. The password field is dark. Function key F3 exits. The decorative lines on the screen include the words Credit Card Demo Application for Mainframe Modernization.'
Add-Figure $script:Figures.Signon 'Figure 3. Sign-on decisions implemented in COSGN00C. Successful routes are green. Failures redisplays the same screen.'
Add-Block 'Heading 3' 'Successful sign-on'
Add-Block 'Normal' 'The program converts the entered user id and password to upper case, then reads the user-security file by user id. When the read succeeds and the stored password equals the upper-cased password, the program copies the stored user type into the session block. If that type is A, control transfers to COADM01C. For every other type, control transfers to COMEN01C. Type U is the named regular-user value. The branch itself tests only for A.'
Add-Block 'Heading 3' 'Unsuccessful sign-on'
Add-Block 'Bullet' 'A blank user id stops the flow before the password is checked. The screen returns with Please enter User ID.'
Add-Block 'Bullet' 'A user id with a blank password stops the flow. The screen returns with Please enter Password.'
Add-Block 'Bullet' 'A read response of 13 means the user id is not on the file. The screen returns with User not found. Try again.'
Add-Block 'Bullet' 'A stored password that does not match returns Wrong Password. Try again. The cursor is placed on the password field.'
Add-Block 'Bullet' 'Any other non-zero read response returns Unable to verify the User.'
Add-Block 'Normal' 'The sign-on program does not count failed attempts, and it does not lock the user id. The README lists sample sign-on values for an administrator and a regular user. Those values are not repeated here. They are Unverified as application rules, because the program accepts whatever password is stored on the file after upper case.'
Add-Block 'Evidence' 'Rules BR-BASE-COSGN00C-001 through BR-BASE-COSGN00C-006. Source app/cbl/COSGN00C.cbl:118-136 and :211-256. Screen: app/bms/COSGN00.bms:98-99, :149, :155-189, and :205. Password field length: app/cpy/CSUSR01Y.cpy:21 as cited by the security page. README sample ids: README.md:203-204, Unverified, values not copied.'

Add-Block 'Heading 2' '3.3 The regular-user menu'
Add-Block 'Normal' 'Transaction CM00 starts COMEN01C. The menu offers eleven options. Every option in the current table is marked for user type U, including Transaction Add. A commented line once labeled Transaction Add as admin only. The active code marks it U, so a regular user is allowed to start it. The program still contains a check that refuses an option marked A when the session type is U, with the message No access - Admin Only option. With the current table that check does not fire, because no option is marked A.'
Add-Table @('Option','Screen label','Program','Transaction') @(
    @('1','Account View','COACTVWC','CAVW'),
    @('2','Account Update','COACTUPC','CAUP'),
    @('3','Credit Card List','COCRDLIC','CCLI'),
    @('4','Credit Card View','COCRDSLC','CCDL'),
    @('5','Credit Card Update','COCRDUPC','CCUP'),
    @('6','Transaction List','COTRN00C','CT00'),
    @('7','Transaction View','COTRN01C','CT01'),
    @('8','Transaction Add','COTRN02C','CT02'),
    @('9','Transaction Reports','CORPT00C','CR00'),
    @('10','Bill Payment','COBIL00C','CB00'),
    @('11','Pending Authorization View','COPAUS0C','CPVS')
)
Add-Block 'Heading 3' 'What can go wrong on the menu'
Add-Block 'Bullet' 'An option that is not numeric, is zero, or is greater than 11 returns Please enter a valid option number.'
Add-Block 'Bullet' 'Option 11, pending authorizations, is started only when CICS reports that program COPAUS0C is available. Otherwise the menu says the option is not installed. This is how the base menu tolerates a system that does not have the optional module.'
Add-Block 'Bullet' 'A program name that begins with DUMMY is not started. The menu says the option is coming soon. No current option uses that prefix.'
Add-Block 'Evidence' 'Option table: app/cpy/COMEN02Y.cpy:21-90. Commented admin-only label: app/cpy/COMEN02Y.cpy:69-72. Validation: app/cbl/COMEN01C.cbl:127-142 and :147-176. Rules BR-BASE-COMEN01C-001 and BR-BASE-COMEN01C-002. Transactions: app/csd/CARDDEMO.CSD:306-439.'

Add-Block 'Heading 2' '3.4 Accounts'
Add-Block 'Normal' 'Account View, program COACTVWC, asks for an account number and reads the account file. A blank account number is reported as not provided, and the message becomes No input received. A supplied account number that is not numeric, or that is zeros, is rejected. An asterisk or spaces in the screen field is treated as not supplied.'
Add-Block 'Normal' 'Account Update, program COACTUPC, is the largest program in the repository, with 3,744 code lines. It reads the account and the related customer, lets the person change them, and writes the changes back only after field edits pass. The first failing edit is the message the person sees. When every field still matches the fetched values, the program reports that nothing changed and skips the field edits. When the edits pass, the changes are marked validated and not yet confirmed. The message on that path is Changes validated.Press F5 to save. F5 is one of the keys the program accepts in that state.'
Add-Block 'Heading 3' 'Edits a person will meet on account update'
Add-Block 'Bullet' 'Account status and primary card holder are required and must be Y or N.'
Add-Block 'Bullet' 'Credit limit, cash credit limit, current balance, and the current-cycle credit and debit amounts are required and must pass the numeric test used by the program.'
Add-Block 'Bullet' 'Dates need a century of 19 or 20, a month from 1 to 12, and a real day, including a leap-year test for 29 February. A further date routine is called. A date of birth must be earlier than the current date. A date of birth equal to today is rejected.'
Add-Block 'Bullet' 'The social security number is three parts. Each part is required, numeric, and non-zero. The first part must not be 000, 666, or 900 through 999.'
Add-Block 'Bullet' 'The FICO score is required, three digits, and from 300 through 850.'
Add-Block 'Bullet' 'Names may contain letters and spaces. Address line 1, city, country, state, and zip are required. State must be one of 56 codes. Zip must be five digits and, together with the state, one of 240 listed combinations. Address line 2 is not edited.'
Add-Block 'Bullet' 'Phone numbers are optional. When one is entered, the area code must be in a list of 410 codes, and the prefix and line number must be non-zero.'
Add-Block 'Bullet' 'The electronic-funds account id is required and must be a 10-digit non-zero number.'
Add-Block 'Normal' 'Two behaviors are worth knowing because the code does not do what a reader might assume. If the date routine reports a failure, control still falls through a path that marks the date flags valid. The error flag and the message remain set, so the update is still blocked, but the date field itself is not marked in error, and the future-date check for date of birth still runs. The phone not-entered test compares the area code where the line number is expected, so a phone with a blank area code and prefix can be treated as not entered even when a line number is keyed. Both observations are recorded as rules and left in the source unchanged.'
Add-Block 'Evidence' 'View rule BR-BASE-COACTVWC-001, app/cbl/COACTVWC.cbl:622-680. Update rules BR-BASE-COACTUPC-001 through BR-BASE-COACTUPC-015, app/cbl/COACTUPC.cbl:1429-2558, app/cpy/CSUTLDPY.cpy, and app/cpy/CSLKPCDY.cpy. Confirm message and F5: app/cbl/COACTUPC.cbl:472-473, :906-908, and :1674. Date-flag path: app/cpy/CSUTLDPY.cpy:315-327. Phone test: app/cbl/COACTUPC.cbl:2238-2239. Code lines: program fact COACTUPC loc.code 3744.'

Add-Block 'Heading 2' '3.5 Cards'
Add-Block 'Normal' 'Credit Card List, COCRDLIC, shows cards and can transfer onward. Choosing view sets the next program to COCRDSLC. Choosing update sets it to COCRDUPC. The list can also return to the user menu.'
Add-Block 'Normal' 'Credit Card View filters on account number, card number, or both. A blank, zero, or non-numeric value is rejected. When both filters are blank, the screen reports that no input was received.'
Add-Block 'Normal' 'Credit Card Update fetches a card by account and card number, then edits the new values. Before the fetch, a missing or non-numeric account or card is rejected. A zero account number is treated as not provided on this screen. Account update treats a zero account number differently: it rejects it as not an 11-digit non-zero number. When the new card data equals the fetched data after upper case, the program reports no change. Otherwise the embossed name must be letters and spaces, the active status must be Y or N, the expiry month must be 1 through 12, and the expiry year must be 1950 through 2099. Comments in the program say the expiry year must be numeric and 1 through 12. The code tests the year through 1950 to 2099. The code is the rule. Those comments also say the month and year must be numeric, and no IS NUMERIC test is coded for them. How a non-numeric value behaves in the coded tests depends on compiler options that are not in the repository.'
Add-Block 'Evidence' 'Navigation: app/cbl/COCRDLIC.cbl:187-204, :526, and :554. View rules BR-BASE-COCRDSLC-001 through 003. Update rules BR-BASE-COCRDUPC-001 through 008, app/cbl/COCRDUPC.cbl:641-945. Zero-account difference: app/cbl/COCRDUPC.cbl:725-731 and app/cbl/COACTUPC.cbl:1802-1808. Comment conflict: app/cbl/COCRDUPC.cbl:894-895 and :928-929 versus the 88-level at app/cbl/COCRDUPC.cbl:99.'

Add-Block 'Heading 2' '3.6 Transactions on the screen'
Add-Block 'Normal' 'Transaction List, COTRN00C, can transfer to Transaction View, COTRN01C, and both can return to the user menu or to sign-on. Transaction View can return to the list.'
Add-Block 'Normal' 'Transaction Add, COTRN02C, writes new rows to the online transaction file. It also reads the card cross-reference and its alternate index. The program comment calls this function an add. The comment is Unverified. The create access on the transaction file is Confirmed. The field-by-field checks inside COTRN02C were not extracted one by one. An example of those checks is at app/cbl/COTRN02C.cbl:199. Until that extraction is done, this document does not describe which add-screen fields are required.'
Add-Block 'Evidence' 'Navigation edges: docs/application-documentation/05-online/navigation-flow.md, citing app/cbl/COTRN00C.cbl:192 and :518 and app/cbl/COTRN01C.cbl:205. File access: app/cbl/COTRN02C.cbl:578, :611, and :644-713. Gap: docs/_work/gaps.md, business rules not yet written one by one.'

Add-Block 'Heading 2' '3.7 Transaction reports'
Add-Block 'Normal' 'From menu option 9 the person enters a date range on the report screen. Program CORPT00C does not format the report in the online task. It writes the job control for a job named TRNRPT00, which executes procedure TRANREPT, onto CICS transient-data queue JOBS, one 80-byte line at a time. The dates from the screen are placed on the sort and report steps. The procedure copies transactions, sorts them, and runs program CBTRN03C.'
Add-Block 'Normal' 'Queue JOBS is defined as an extrapartition queue with DD name INREADER. The CICS region startup job that would connect INREADER to an internal reader is not in this repository. The write to the queue is Confirmed. Whether that write becomes a submitted job is Unverified until the region job is known.'
Add-Figure $script:Figures.Report 'Figure 4. Report submission from the online screen into batch. The final hand-off is unverified.'
Add-Block 'Evidence' 'app/cbl/CORPT00C.cbl:83-121 and :497-520. Queue: app/csd/CARDDEMO.CSD:499-501. Procedure steps: app/proc/TRANREPT.prc:21, :35, and :57. Gap: docs/_work/gaps.md, resume pass, CORPT00C.'

Add-Block 'Heading 2' '3.8 Bill payment'
Add-Block 'Normal' 'Menu option 10 starts COBIL00C under transaction CB00. The program reads and updates the account file, reads the cross-reference alternate index, and browses and creates transaction records. It can return to the user menu or to sign-on. The program comment says the screen pays an account balance in full and writes a transaction for the online bill payment. That comment is Unverified, including a spelling error in the comment itself. Field edits for the screen were not extracted, so this document does not state the payment amount rule, the success message, or the failure messages.'
Add-Block 'Evidence' 'Transaction: app/csd/CARDDEMO.CSD:337. File access: app/cbl/COBIL00C.cbl:345-512. Return: app/cbl/COBIL00C.cbl:281. Header: program page COBIL00C, Unverified.'

Add-Block 'Heading 2' '3.9 Administrator work and user security'
Add-Block 'Normal' 'Transaction CA00 starts COADM01C. The admin menu has six options. Options 1 through 4 maintain users. Options 5 and 6 maintain DB2 transaction types. An option is started when its program name does not begin with DUMMY. Unlike the user menu, the admin menu does not ask CICS whether the target program is installed, and it does not re-check that the session type is A. The protection is the sign-on transfer that sends only type A here.'
Add-Table @('Option','Screen label','Program','Transaction') @(
    @('1','User List (Security)','COUSR00C','CU00'),
    @('2','User Add (Security)','COUSR01C','CU01'),
    @('3','User Update (Security)','COUSR02C','CU02'),
    @('4','User Delete (Security)','COUSR03C','CU03'),
    @('5','Transaction Type List/Update (Db2)','COTRTLIC','CTLI'),
    @('6','Transaction Type Maintenance (Db2)','COTRTUPC','CTTU')
)
Add-Block 'Normal' 'The user list can transfer to update or delete. Add, update, and delete can return to the admin menu or to sign-on. A new-user password is stored from the screen field without the upper-case conversion that sign-on applies on the way in. The inline field checks in the four user programs were not extracted one by one.'
Add-Block 'Evidence' 'Menu: app/cpy/COADM02Y.cpy:22-53. Start rule BR-BASE-COADM01C-001, app/cbl/COADM01C.cbl:141-148. Password stored as entered: app/cbl/COUSR01C.cbl:157. Navigation: docs/application-documentation/05-online/navigation-flow.md.'

Add-Block 'Heading 2' '3.10 Optional pending authorizations'
Add-Block 'Normal' 'When the authorization module is installed, menu option 11 opens a summary screen, transaction CPVS, program COPAUS0C. From the summary the person can open details, transaction CPVD, program COPAUS1C. The detail program links to COPAUS2C, which reads and writes the DB2 table CARDDEMO.AUTHFRDS. The summary and detail programs also use IMS program specification block PSBPAUTB and database DBPAUTP0. A third transaction, CP00, starts COPAUA0C when an MQ trigger arrives. That program reads the request queue name from the trigger message and sends the reply to the reply-to queue on the message. The request queue name is not a literal in the source.'
Add-Block 'Normal' 'Batch job CBPAUP0J runs CBPAUP0C as an IMS batch message program. A pending authorization is deleted when the computed day difference is greater than or equal to the expiry days. Expiry days are the numeric parameter, or 5 when that parameter is not numeric. If the response code is 00, the approved count and amount are reduced. Any other response code reduces the declined count and amount. The expression 99999 minus the authorization date is recorded as written. The program does not state what 99999 means.'
Add-Block 'Evidence' 'Transactions: app/app-authorization-ims-db2-mq/csd/CRDDEMO2.csd:39, :49, and :59. Link: app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:35 and :248-249. IMS: app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:75. MQ: app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:238 and :354-414. Expiry rules BR-AUTH-CBPAUP0C-001 and 002, app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:196-199 and :280-293. Install check: app/cbl/COMEN01C.cbl:147-159.'

Add-Block 'Heading 2' '3.11 Optional transaction types in DB2'
Add-Block 'Normal' 'Admin options 5 and 6 maintain reference data in DB2. COTRTLIC lists types and can delete through a cursor. COTRTUPC adds or changes one type. The type code is required, numeric, non-zero, and two characters, and a valid code is rewritten with leading zeros. The description is required and may contain letters, digits, and spaces, up to 50 characters. When the code and description already match the stored row, the program reports no change.'
Add-Block 'Normal' 'The tables are CARDDEMO.TRANSACTION_TYPE, with a two-character code and a description, and CARDDEMO.TRANSACTION_TYPE_CATEGORY, which references the type code and is not removed when a type is deleted because the foreign key is ON DELETE RESTRICT. Category rows are loaded by a control script from job CREADB21. No COBOL program in the inventory issues SQL against the category table.'
Add-Block 'Normal' 'Batch program COBTUPDT, run by job MNTTRDB2 under plan CARDDEMO, applies a maintenance file. Action A inserts, U updates, D deletes, and an asterisk is ignored. Any other action abends with ERROR: TYPE NOT VALID. The program has no SQL COMMIT. Where the plan commits is not stated.'
Add-Block 'Evidence' 'Rules BR-BASE-COTRTUPC-001 through 003 and BR-TRANTYPE-COBTUPDT-001. DDL: app/app-transaction-type-db2/ddl/TRNTYPE.ddl:1-4 and app/app-transaction-type-db2/ddl/TRNTYCAT.ddl:1-7. Category load: app/app-transaction-type-db2/ctl/DB2LTCAT.ctl:15 and app/app-transaction-type-db2/jcl/CREADB21.jcl:84. Plan: app/app-transaction-type-db2/jcl/MNTTRDB2.jcl:30.'

Add-Block 'Heading 2' '3.12 Optional account and date replies'
Add-Block 'Normal' 'Two programs answer MQ requests. Transaction CDRA starts COACCT01, which reads an account from VSAM and puts a reply on the literal queue CARD.DEMO.REPLY.ACCT. Transaction CDRD starts CODATE01, which puts a reply on CARD.DEMO.REPLY.DATE. Both take the request queue name from the MQ trigger message, so the request queue is supplied at runtime. Failures can be written to CARD.DEMO.ERROR. There is no BMS map for these two transactions. They are message programs, not screens.'
Add-Block 'Evidence' 'app/app-vsam-mq/csd/CRDDEMOM.csd:17 and :27. Queues: app/app-vsam-mq/cbl/COACCT01.cbl:191-198 and :294, app/app-vsam-mq/cbl/CODATE01.cbl:147. Account read: app/app-vsam-mq/cbl/COACCT01.cbl:396.'

Add-Block 'Heading 2' '3.13 Daily posting'
Add-Block 'Normal' 'Job POSTTRAN runs program CBTRN02C. The program reads the sequential daily transaction file AWS.M2.CARDDEMO.DALYTRAN.PS. For each record it looks up the card number on the cross-reference file. If the card is found, it reads the account. A record is posted only when that validation records no failure. Posting copies the daily fields onto a transaction-master record, updates the category balance, updates the account, and writes the transaction master.'
Add-Block 'Heading 3' 'Successful posting'
Add-Block 'Normal' 'A daily record is posted when the card number exists on the cross-reference, the account exists, the computed balance is within the credit limit, and the transaction timestamp is not after the account expiration field. The balance used for the limit test is current-cycle credit, minus current-cycle debit, plus the daily amount. The account field is spelled ACCT-EXPIRAION-DATE in the source.'
Add-Block 'Heading 3' 'Unsuccessful posting'
Add-Block 'Bullet' 'Card number not on the cross-reference: reason 100, INVALID CARD NUMBER FOUND. The record is written to the reject file.'
Add-Block 'Bullet' 'Account not found: reason 101, ACCOUNT RECORD NOT FOUND.'
Add-Block 'Bullet' 'Computed balance above the credit limit: reason 102, OVERLIMIT TRANSACTION.'
Add-Block 'Bullet' 'Transaction after account expiration: reason 103, TRANSACTION RECEIVED AFTER ACCT EXPIRATION.'
Add-Block 'Normal' 'The limit test and the expiration test both run when the account is found. If both fail, reason 103 replaces reason 102. Rejected records are written to a new generation of AWS.M2.CARDDEMO.DALYREJS. The program displays the processed count and the rejected count. If any record was rejected, it sets return code 4. An error opening or reading the daily file abends the program. A comment in the validation paragraph says more validations could be added. That comment is not a rule.'
Add-Block 'Evidence' 'Job step: app/jcl/POSTTRAN.jcl:23-38. Loop and return code: app/cbl/CBTRN02C.cbl:202-231. Validation: app/cbl/CBTRN02C.cbl:370-442. Reject write: app/cbl/CBTRN02C.cbl:446-448.'

Add-Block 'Heading 2' '3.14 Monthly interest'
Add-Block 'Normal' 'Job INTCALC runs program CBACT04C with the ten-character parameter 2022071800. The program reads category balances and the disclosure group. Monthly interest for a category balance is the balance times the disclosure interest rate, divided by 1200. The result is a signed amount with two decimal places, and the COMPUTE has no ROUNDED phrase. The interest amount is added into a total and written as a transaction whose identifier begins with that ten-character parameter. The job reads the account file, the cross-reference, and the disclosure file, and it creates a new transaction generation.'
Add-Block 'Evidence' 'Formula BR-BASE-CBACT04C-001: app/cbl/CBACT04C.cbl:464-467. Parameter: app/jcl/INTCALC.jcl:22 and app/cbl/CBACT04C.cbl:176-180 and :476. Files: app/jcl/INTCALC.jcl:27-40.'

Add-Block 'Heading 2' '3.15 How batch and online share files'
Add-Block 'Normal' 'CLOSEFIL and OPENFIL issue operator commands to a CICS region named CICSAWSA. CLOSEFIL closes the files TRANSACT, CCXREF, ACCTDAT, CXACAIX, and USRSEC. OPENFIL opens the same five. Some load jobs close and reopen a single file around the load, using the same style of command. Control-M and CA7 are separate scheduler exports. A job name that appears in both is not one chain.'
Add-Figure $script:Figures.Batch 'Figure 5. The close, update, wait, and open pattern. The posting box and the interest box are different jobs.'
Add-Block 'Heading 3' 'Chains the exports actually name'
Add-Block 'Bullet' 'Control-M daily folder: CLOSEFIL, then TRANBKP, then WAITSTEP, then OPENFIL.'
Add-Block 'Bullet' 'Control-M monthly folder: CLOSEFIL, then INTCALC, then COMBTRAN, then WAITSTEP, then OPENFIL.'
Add-Block 'Bullet' 'Control-M weekly folder: MNTTRDB2, then TRANEXTR, and a nested disclosure path CLOSEFIL, DISCGRP, WAITSTEP, OPENFIL. The word WEEKLY is in a description and a folder name. The folder has no DAYS attribute, so the calendar is not confirmed by the export.'
Add-Block 'Bullet' 'CA7 schedule id 030 includes CLOSEFIL, then CBPAUP0J, then POSTTRAN, then WAITSTEP, then OPENFIL. The same export also chains file reads, statement creation, and a category print. What schedule ids 030, 031, and 032 mean is not defined in the repository.'
Add-Block 'Bullet' 'Shell script run_posting.sh submits CLOSEFIL, ACCTFILE, TCATBALF, TRANBKP, POSTTRAN, TRANIDX, and OPENFIL, in that order, by file transfer to a listener on localhost port 2121.'
Add-Block 'Bullet' 'Shell script run_interest_calc.sh submits CLOSEFIL, INTCALC, TRANBKP, COMBTRAN, TRANIDX, and OPENFIL.'
Add-Block 'Normal' 'The README lists a longer batch sequence, including a statement job. That README order is Unverified. The shell scripts are Confirmed as the order of their put commands. Several application jobs, including the report job TRANREPT, are not named in either scheduler export. They can still be submitted by hand or, for the report, by the online program.'
Add-Block 'Evidence' 'Operator commands: app/jcl/CLOSEFIL.jcl:22-30 and app/jcl/OPENFIL.jcl:22-30. Schedules: app/scheduler/CardDemo.controlm and app/scheduler/CardDemo.ca7:43-124. Scripts: scripts/run_posting.sh:9-34 and scripts/run_interest_calc.sh:11-34. README order: README.md:209-233, Unverified. Jobs absent from schedulers: docs/_work/gaps.md.'

Add-Block 'Heading 2' '3.16 An illustrative walkthrough'
Add-Callout 'Illustrative example, not sample data' @'
The names and amounts in this box are invented so the workflow is easy to follow. They are not rows from app/data, and they are not the sample sign-on values in the README.

A person starts CC00 and enters a user id whose stored type is U, with a password that matches after upper case. COSGN00C transfers to the user menu. The person chooses option 1 and enters an account number. COACTVWC reads the account file and shows the account. The person returns to the menu and chooses option 8 to add a transaction. COTRN02C creates a transaction row if its own checks pass. Those checks are not fully catalogued.

Later, a batch window runs CLOSEFIL, then POSTTRAN. A daily record whose card number is on the cross-reference, whose account is under the credit limit, and whose timestamp is within the account expiration is posted. A daily record with an unknown card number is written to the reject generation and counted. If any record was rejected, CBTRN02C ends with return code 4. OPENFIL makes the five online files available again.

A second person with stored type A signs on and reaches the admin menu. Choosing option 2 starts the add-user program. The password they type is stored without upper case. The next time that new user signs on, sign-on will upper-case the typed password before comparing it.
'@
Add-Block 'Evidence' 'The routes in the example are the confirmed routes in sections 3.2, 3.3, 3.6, 3.9, and 3.13. The invented ids and amounts are illustrative only.'

Add-Block 'Heading 2' '3.17 Use-case summary'
Add-Table @('Use case','Actor','Starts','Successful outcome','Unsuccessful outcome') @(
    @('Sign on','Any stored user','CC00','Menu for type A, or the user menu otherwise','Screen message, no menu'),
    @('View or update an account','User menu','CAVW or CAUP','Account and customer shown or updated','Input message, no write'),
    @('List, view, or update a card','User menu','CCLI, CCDL, or CCUP','Card shown or updated','Input message, no write'),
    @('List, view, or add a transaction','User menu','CT00, CT01, or CT02','Transaction shown or created','Add-screen rules not fully catalogued'),
    @('Request a report','User menu','CR00','Job text written to queue JOBS','Delivery to JES unverified'),
    @('Bill payment','User menu','CB00','Account updated and a transaction created','Field rules unavailable'),
    @('Maintain users','Administrator','CU00 to CU03','User row listed, added, updated, or deleted','Field rules not fully catalogued'),
    @('Pending authorization','User, if installed','CPVS then CPVD','IMS summary and detail, DB2 fraud row','Menu says option is not installed'),
    @('Transaction types','Administrator','CTLI or CTTU','DB2 type listed, added, changed, or deleted','Validation message, or batch abend for a bad action'),
    @('Post the daily file','Batch','POSTTRAN','Master, account, and category balance updated','Reject file and return code 4, or an abend on I/O'),
    @('Calculate interest','Batch','INTCALC','Interest transaction written from balance times rate / 1200','Abend path when the disclosure group cannot be read')
)
Add-Block 'Evidence' 'Each row restates a section above. Disclosure read failure: app/cbl/CBACT04C.cbl:452-458.'

Add-Block 'Heading 2' '3.18 Confirmed business rules'
Add-Block 'Normal' 'Fifty decisions were read from the code and given identifiers. The table is the catalog. Programs that still contain validations not listed here are named in the gaps chapter: the user-maintenance programs and the transaction-add program. Eighty-eight COMPUTE lines were indexed, and only the interest formula and the authorization expiry test were promoted to rules.'

$rules = Get-FirstMarkdownTable (Join-Path $script:RepoRoot 'docs\application-documentation\09-business-rules-catalog.md')
$ruleRows = New-Object System.Collections.Generic.List[object]
foreach ($row in $rules.Rows) {
    $ruleRows.Add(@($row[0], $row[3], $row[4]))
}
Add-Table @('Rule','Statement','Source') $ruleRows
Add-Block 'Evidence' 'docs/_work/rules/rules.json and docs/application-documentation/09-business-rules-catalog.md. COMPUTE index note: docs/_work/gaps.md.'
