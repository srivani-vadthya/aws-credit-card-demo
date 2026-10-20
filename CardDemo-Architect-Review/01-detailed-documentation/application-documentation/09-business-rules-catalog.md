# Business rules catalog

All business rules: 50 legacy rules from the first pass (each re-reviewed in the batch analysis) and 342 rules from the batch analysis. Every rule cites a line range; batch rules also carry a verbatim code anchor that `batch_manager.py check` verified inside that range.

| Category | Rules |
|---|---|
| authorization | 1 |
| calculation | 23 |
| data-integrity | 13 |
| decision | 107 |
| error-policy | 69 |
| routing | 49 |
| security | 1 |
| temporal | 1 |
| transformation | 36 |
| validation | 92 |

## Programs without business rules

| Program | Reason |
|---|---|
| [CBACT02C](07-programs/CBACT02C.md) | CBACT02C is a pure file-print utility: it opens the card KSDS (CARDFILE) for sequential input, DISPLAYs every CARD-RECORD to SYSOUT, and closes the file. It makes no data-driven decisions; its only conditional logic is file-status handling (end of file, abend code 999 on any I/O error). |
| [CBACT03C](07-programs/CBACT03C.md) | CBACT03C is a pure file-print utility: it opens the card cross-reference KSDS (XREFFILE) for sequential input, DISPLAYs every CARD-XREF-RECORD to SYSOUT, and closes the file. Its only conditional logic is file-status handling (end of file, abend code 999 on any I/O error). |
| [CBCUS01C](07-programs/CBCUS01C.md) | CBCUS01C is a pure file-print utility: it opens the customer KSDS (CUSTFILE) for sequential input, DISPLAYs every CUSTOMER-RECORD to SYSOUT, and closes the file. Its only conditional logic is file-status handling (end of file, abend code 999 on any I/O error). |
| [CBSTM03B](07-programs/CBSTM03B.md) | CBSTM03B is a file-access subroutine for CBSTM03A. Based on the DD name and operation code passed in LK-M03B-AREA it opens, reads (sequentially or by key) or closes one of four indexed files and returns the file status in LK-M03B-RC. It makes no business decisions; its conditional logic is only the dispatch on file name and operation code. |
| [COBSWAIT](07-programs/COBSWAIT.md) | COBSWAIT is a technical batch utility: it reads a wait duration from SYSIN and calls the external routine MVSWAIT to suspend the step. It contains no decisions, validations, calculations or data processing with business meaning. |

## CBACT01C

Program page: [CBACT01C](07-programs/CBACT01C.md).

### BR-CBACT01C-001

When the account's current-cycle debit (ACCT-CURR-CYC-DEBIT) is zero, the extract record carries a fixed cycle debit of 2525.00 in OUT-ACCT-CURR-CYC-DEBIT instead of zero.

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | ACCT-CURR-CYC-DEBIT = 0 |
| Outcome | OUT-ACCT-CURR-CYC-DEBIT = 2525.00 in the OUTFILE record; non-zero debits are not moved at all (see observation). |
| Implemented at | CBACT01C 1300-POPUL-ACCT-RECORD `app/cbl/CBACT01C.cbl:236-238` |
| Anchor (verified) | `IF ACCT-CURR-CYC-DEBIT EQUAL TO ZERO MOVE 2525.00 TO OUT-ACCT-CURR-CYC-DEBIT` |

### BR-CBACT01C-002

The account reissue date is reformatted for the extract by calling COBDATFT with input type '2' (YYYY-MM-DD-IN) and output type '2' (YYYYMMDD-OP); the converted CODATECN-0UT-DATE becomes OUT-ACCT-REISSUE-DATE.

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Inferred |
| Conditions | Every successfully read account record. |
| Outcome | OUT-ACCT-REISSUE-DATE holds the reformatted date (expected YYYYMMDD per the 88-level meanings). |
| Implemented at | CBACT01C 1300-POPUL-ACCT-RECORD `app/cbl/CBACT01C.cbl:223-233` |
| Implemented at | CBACT01C  `app/cpy/CODATECN.cpy:19-21` |
| Implemented at | CBACT01C  `app/cpy/CODATECN.cpy:36-38` |
| Anchor (verified) | `CALL 'COBDATFT' USING CODATECN-REC.` |

### BR-CBACT01C-003

Any account-file read status other than '00' (record) or '10' (end of file) stops the job: the program displays 'ERROR READING ACCOUNT FILE', the file status, and abends with code 999 via CEE3ABD.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | ACCTFILE-STATUS not '00' and not '10' |
| Outcome | Abend code 999; no further records processed. |
| Messages | ERROR READING ACCOUNT FILE; ABENDING PROGRAM |
| Implemented at | CBACT01C 1000-ACCTFILE-GET-NEXT `app/cbl/CBACT01C.cbl:180-197` |
| Implemented at | CBACT01C  `app/cbl/CBACT01C.cbl:406-410` |
| Anchor (verified) | `DISPLAY 'ERROR READING ACCOUNT FILE'` |


## CBACT04C

Program page: [CBACT04C](07-programs/CBACT04C.md).

### BR-BASE-CBACT04C-001

Monthly interest for a category balance is the category balance times the disclosure interest rate, divided by 1200.

| Item | Value |
|---|---|
| Category | calculation |
| Confidence | Confirmed |
| Implemented at | CBACT04C 1300-COMPUTE-INTEREST `app/cbl/CBACT04C.cbl:464-465` |
| Batch review | confirmed: Confirmed: WS-MONTHLY-INT = (TRAN-CAT-BAL * DIS-INT-RATE) / 1200, i.e. the annual percentage rate divided by 12 months and by 100. No ROUNDED clause, so the result is truncated to 2 decimals (WS-MONTHLY-INT PIC S9(09)V99). It is only executed when DIS-INT-RATE is not zero (see BR-CBACT04C-002). (`app/cbl/CBACT04C.cbl:464-465`, anchor `COMPUTE WS-MONTHLY-INT = ( TRAN-CAT-BAL * DIS-INT-RATE) / 1200`) |

### BR-CBACT04C-001

Transaction-category balances are processed as a control break on account id: when TRANCAT-ACCT-ID changes, the previously accumulated interest is posted to the previous account (not on the first record), the interest total is reset to zero, and the new account record and its card cross-reference are read.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | TRANCAT-ACCT-ID differs from WS-LAST-ACCT-NUM |
| Outcome | 1050-UPDATE-ACCOUNT for the previous account (if WS-FIRST-TIME is not 'Y'); WS-TOTAL-INT = 0; 1100-GET-ACCT-DATA and 1110-GET-XREF-DATA for the new account. |
| Implemented at | CBACT04C (PROCEDURE DIVISION entry) `app/cbl/CBACT04C.cbl:194-206` |
| Anchor (verified) | `IF TRANCAT-ACCT-ID NOT= WS-LAST-ACCT-NUM` |

### BR-CBACT04C-002

Interest (and the future fee calculation) is generated for a transaction category only when the disclosure-group interest rate DIS-INT-RATE for the account group, transaction type and category is non-zero; zero-rate categories produce no interest transaction.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | DIS-INT-RATE <> 0 |
| Outcome | 1300-COMPUTE-INTEREST and 1400-COMPUTE-FEES are performed. |
| Implemented at | CBACT04C (PROCEDURE DIVISION entry) `app/cbl/CBACT04C.cbl:210-217` |
| Anchor (verified) | `IF DIS-INT-RATE NOT = 0` |

### BR-CBACT04C-003

When no disclosure group record exists for the account's group id, type and category (status '23'), the interest rate is taken from the disclosure group with group id 'DEFAULT' for the same type and category; if that default record is also missing the job abends.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | DISCGRP-STATUS = '23' (record not found) |
| Outcome | Re-read DISCGRP with FD-DIS-ACCT-GROUP-ID = 'DEFAULT'; abend 999 with 'ERROR READING DEFAULT DISCLOSURE GROUP' if not found. |
| Messages | DISCLOSURE GROUP RECORD MISSING; TRY WITH DEFAULT GROUP CODE; ERROR READING DEFAULT DISCLOSURE GROUP |
| Implemented at | CBACT04C 1200-GET-INTEREST-RATE `app/cbl/CBACT04C.cbl:436-439` |
| Implemented at | CBACT04C  `app/cbl/CBACT04C.cbl:416-426` |
| Implemented at | CBACT04C  `app/cbl/CBACT04C.cbl:444-459` |
| Anchor (verified) | `MOVE 'DEFAULT' TO FD-DIS-ACCT-GROUP-ID` |

### BR-CBACT04C-004

Monthly interest of all categories of an account is summed in WS-TOTAL-INT; at the account break the total is added to the account's current balance and the current-cycle credit and debit totals are reset to zero before the account is rewritten.

| Item | Value |
|---|---|
| Category | calculation |
| Confidence | Confirmed |
| Conditions | Account control break (BR-CBACT04C-001). |
| Outcome | ACCT-CURR-BAL += WS-TOTAL-INT; ACCT-CURR-CYC-CREDIT = 0; ACCT-CURR-CYC-DEBIT = 0; REWRITE of the account record. |
| Implemented at | CBACT04C 1050-UPDATE-ACCOUNT `app/cbl/CBACT04C.cbl:352-356` |
| Implemented at | CBACT04C  `app/cbl/CBACT04C.cbl:467` |
| Anchor (verified) | `ADD WS-TOTAL-INT TO ACCT-CURR-BAL` |

### BR-CBACT04C-005

Each computed monthly interest amount is posted as a system transaction: id = run date parameter (PARM-DATE) + 6-digit running sequence, type '01', category 5, source 'System', description 'Int. for a/c ' followed by the account id, amount = monthly interest, card number from the account's cross-reference, and the current timestamp as both origin and processing timestamp.

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | DIS-INT-RATE <> 0 for the category. |
| Outcome | One TRAN-RECORD written to TRANSACT per interest-bearing category. |
| Implemented at | CBACT04C 1300-B-WRITE-TX `app/cbl/CBACT04C.cbl:474-498` |
| Anchor (verified) | `STRING 'Int. for a/c ' , ACCT-ID` |

### BR-CBACT04C-006

A transaction-category balance whose account is missing from the account master (or has no card cross-reference) is not skipped: the program displays 'ACCOUNT NOT FOUND: ' with the id and abends the run with code 999.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | ACCTFILE-STATUS or XREFFILE-STATUS not '00' after the keyed read. |
| Outcome | 'ERROR READING ACCOUNT FILE' / 'ERROR READING XREF FILE', file status display, abend 999. |
| Messages | ACCOUNT NOT FOUND: ; ERROR READING ACCOUNT FILE; ERROR READING XREF FILE |
| Implemented at | CBACT04C 1100-GET-ACCT-DATA `app/cbl/CBACT04C.cbl:373-390` |
| Implemented at | CBACT04C  `app/cbl/CBACT04C.cbl:394-412` |
| Anchor (verified) | `DISPLAY 'ACCOUNT NOT FOUND: ' FD-ACCT-ID` |


## CBEXPORT

Program page: [CBEXPORT](07-programs/CBEXPORT.md).

### BR-CBEXPORT-001

The branch-migration export is a full, unfiltered extract: every customer, account, card cross-reference, transaction and card record is exported, in that fixed order (one entity type after another), with no selection criteria.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | Always. |
| Outcome | EXPFILE contains all records of the five source files. |
| Implemented at | CBEXPORT 0000-MAIN-PROCESSING `app/cbl/CBEXPORT.cbl:151-157` |
| Implemented at | CBEXPORT  `app/cbl/CBEXPORT.cbl:249-252` |
| Anchor (verified) | `PERFORM 2000-EXPORT-CUSTOMERS` |

### BR-CBEXPORT-002

Each export record carries a type code identifying the entity ('C' customer, 'A' account, 'X' card cross-reference, 'T' transaction, 'D' card), the run timestamp, a sequence number incremented across all record types, branch id '0001' and region code 'NORTH'.

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | Every exported record. |
| Outcome | EXPORT-REC-TYPE, EXPORT-TIMESTAMP, EXPORT-SEQUENCE-NUM, EXPORT-BRANCH-ID, EXPORT-REGION-CODE populated. |
| Implemented at | CBEXPORT 2200-CREATE-CUSTOMER-EXP-REC `app/cbl/CBEXPORT.cbl:273-279` |
| Implemented at | CBEXPORT  `app/cbl/CBEXPORT.cbl:343-348` |
| Implemented at | CBEXPORT  `app/cbl/CBEXPORT.cbl:407-412` |
| Implemented at | CBEXPORT  `app/cbl/CBEXPORT.cbl:462-467` |
| Implemented at | CBEXPORT  `app/cbl/CBEXPORT.cbl:527-532` |
| Anchor (verified) | `MOVE 'C' TO EXPORT-REC-TYPE` |

### BR-CBEXPORT-003

Any failure to open a source or export file, or any read status other than success/end-of-file, stops the export with an error message naming the file and its status and an abend via CEE3ABD.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | Open status not '00'; read status not '00' and not '10'. |
| Outcome | Abend; partial export file may remain. |
| Messages | ERROR: Cannot open CUSTOMER-INPUT, Status: ; ERROR: Reading CUSTOMER-INPUT, Status: ; CBEXPORT: ABENDING PROGRAM |
| Implemented at | CBEXPORT 1100-OPEN-FILES `app/cbl/CBEXPORT.cbl:200-240` |
| Implemented at | CBEXPORT  `app/cbl/CBEXPORT.cbl:262-266` |
| Implemented at | CBEXPORT  `app/cbl/CBEXPORT.cbl:331-335` |
| Implemented at | CBEXPORT  `app/cbl/CBEXPORT.cbl:395-399` |
| Implemented at | CBEXPORT  `app/cbl/CBEXPORT.cbl:450-454` |
| Implemented at | CBEXPORT  `app/cbl/CBEXPORT.cbl:515-519` |
| Anchor (verified) | `DISPLAY 'ERROR: Cannot open CUSTOMER-INPUT, Status: '` |

### BR-CBEXPORT-004

A failed write of any export record (status not '00') aborts the whole export run; no record is skipped silently.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | WS-EXPORT-STATUS not '00' after WRITE. |
| Outcome | Abend via 9999-ABEND-PROGRAM. |
| Messages | ERROR: Writing export record, Status: |
| Implemented at | CBEXPORT 2200-CREATE-CUSTOMER-EXP-REC `app/cbl/CBEXPORT.cbl:301-307` |
| Implemented at | CBEXPORT  `app/cbl/CBEXPORT.cbl:364-370` |
| Implemented at | CBEXPORT  `app/cbl/CBEXPORT.cbl:419-425` |
| Implemented at | CBEXPORT  `app/cbl/CBEXPORT.cbl:484-490` |
| Implemented at | CBEXPORT  `app/cbl/CBEXPORT.cbl:542-548` |
| Anchor (verified) | `DISPLAY 'ERROR: Writing export record, Status: '` |


## CBIMPORT

Program page: [CBIMPORT](07-programs/CBIMPORT.md).

### BR-CBIMPORT-001

Each export record is routed to its normalized target file by EXPORT-REC-TYPE: 'C' to the customer file, 'A' to the account file, 'X' to the card cross-reference file, 'T' to the transaction file, 'D' to the card file; any other type is treated as an unknown record.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | Value of EXPORT-REC-TYPE. |
| Outcome | Record written to CUSTOUT, ACCTOUT, XREFOUT, TRNXOUT or CARDOUT, or handled by 2700-PROCESS-UNKNOWN-RECORD. |
| Implemented at | CBIMPORT 2200-PROCESS-RECORD-BY-TYPE `app/cbl/CBIMPORT.cbl:272-284` |
| Anchor (verified) | `EVALUATE EXPORT-REC-TYPE` |

### BR-CBIMPORT-002

A record with an unknown type is not imported and does not stop the run: it is counted, logged to the error file with timestamp, type, sequence number and 'Unknown record type encountered', and processing continues.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | EXPORT-REC-TYPE not in ('C','A','X','T','D'). |
| Outcome | Error record written to ERROUT; WS-UNKNOWN-RECORD-TYPE-COUNT and WS-ERROR-RECORDS-WRITTEN incremented. |
| Messages | Unknown record type encountered |
| Implemented at | CBIMPORT 2700-PROCESS-UNKNOWN-RECORD `app/cbl/CBIMPORT.cbl:427-433` |
| Implemented at | CBIMPORT  `app/cbl/CBIMPORT.cbl:439-446` |
| Anchor (verified) | `MOVE 'Unknown record type encountered' TO ERR-MESSAGE` |

### BR-CBIMPORT-003

Failure to open any file, a read error on the export file (status not '00'/'10'), or a failed write to any target master file aborts the import via CEE3ABD.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | Open status not '00'; read status not '00'/'10'; write status not '00'. |
| Outcome | Abend; target files may be partially written. |
| Messages | ERROR: Cannot open EXPORT-INPUT, Status: ; ERROR: Writing customer record, Status: ; CBIMPORT: ABENDING PROGRAM |
| Implemented at | CBIMPORT 1100-OPEN-FILES `app/cbl/CBIMPORT.cbl:198-245` |
| Implemented at | CBIMPORT  `app/cbl/CBIMPORT.cbl:263-267` |
| Implemented at | CBIMPORT  `app/cbl/CBIMPORT.cbl:314-318` |
| Implemented at | CBIMPORT  `app/cbl/CBIMPORT.cbl:343-347` |
| Implemented at | CBIMPORT  `app/cbl/CBIMPORT.cbl:363-367` |
| Implemented at | CBIMPORT  `app/cbl/CBIMPORT.cbl:393-397` |
| Implemented at | CBIMPORT  `app/cbl/CBIMPORT.cbl:416-420` |
| Anchor (verified) | `DISPLAY 'ERROR: Cannot open EXPORT-INPUT, Status: '` |

### BR-CBIMPORT-004

Imported records are rebuilt field by field into the standard CardDemo master layouts (customer 500, account 300, cross-reference 50, transaction 350, card 150 bytes), converting the export's packed (COMP/COMP-3) numeric fields back to the display formats of CVCUS01Y, CVACT01Y, CVACT03Y, CVTRA05Y and CVACT02Y. No field is validated or altered.

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | Record of a known type. |
| Outcome | One record written to the matching target file. |
| Implemented at | CBIMPORT 2400-PROCESS-ACCOUNT-RECORD `app/cbl/CBIMPORT.cbl:325-341` |
| Implemented at | CBIMPORT  `app/cbl/CBIMPORT.cbl:290-312` |
| Implemented at | CBIMPORT  `app/cbl/CBIMPORT.cbl:354-361` |
| Implemented at | CBIMPORT  `app/cbl/CBIMPORT.cbl:374-391` |
| Implemented at | CBIMPORT  `app/cbl/CBIMPORT.cbl:404-414` |
| Anchor (verified) | `MOVE EXP-ACCT-CURR-BAL TO ACCT-CURR-BAL` |


## CBPAUP0C

Program page: [CBPAUP0C](07-programs/CBPAUP0C.md).

### BR-AUTH-CBPAUP0C-001

A pending authorization qualifies for delete when the computed day difference is greater than or equal to the expiry days. Expiry days are the numeric parm value, or 5 when that parm is not numeric.

| Item | Value |
|---|---|
| Category | temporal |
| Confidence | Confirmed |
| Conditions | WS-DAY-DIFF >= |
| Outcome | SET QUALIFIED-FOR-DELETE TO TRUE |
| Implemented at | CBPAUP0C 4000-CHECK-IF-EXPIRED `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:280-286` |
| Implemented at | CBPAUP0C  `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:196-199` |
| Batch review | confirmed: Matches code; default of 5 at 196-199. Same as BR-CBPAUP0C-001/004. Note the YYDDD subtraction does not handle year boundaries. (`app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:280-286`, anchor `IF WS-DAY-DIFF >= WS-EXPIRY-DAYS`) |

### BR-AUTH-CBPAUP0C-002

When a pending authorization qualifies for delete and its response code is 00, the approved count and approved amount are reduced. Any other response code reduces the declined count and the declined amount.

| Item | Value |
|---|---|
| Category | calculation |
| Confidence | Confirmed |
| Conditions | PA-AUTH-RESP-CODE = 00 |
| Outcome | subtract 1 from PA-APPROVED-AUTH-CNT and PA-APPROVED-AMT from PA-APPROVED-AUTH-AMT; subtract 1 from PA-DECLINED-AUTH-CNT and PA-TRANSACTION-AMT from PA-DECLINED-AUTH-AMT |
| Implemented at | CBPAUP0C 4000-CHECK-IF-EXPIRED `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:287-293` |
| Batch review | confirmed: Matches code. The reductions are in working storage only; the summary segment is never replaced (no REPL), so they only influence the summary-delete decision. Same as BR-CBPAUP0C-002. (`app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:287-293`, anchor `SUBTRACT PA-APPROVED-AMT    FROM PA-APPROVED-AUTH-AMT`) |

### BR-CBPAUP0C-001

A pending authorization detail is selected for purge when the number of days between today (YYDDD) and its authorization date (99999 minus the stored complemented PA-AUTH-DATE-9C) is greater than or equal to the expiry-days threshold.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | CURRENT-YYDDD - (99999 - PA-AUTH-DATE-9C) >= WS-EXPIRY-DAYS |
| Outcome | QUALIFIED-FOR-DELETE set; MAIN-PARA then deletes the PAUTDTL1 segment (5000-DELETE-AUTH-DTL). Otherwise NOT-QUALIFIED-FOR-DELETE and the detail is kept. |
| Implemented at | CBPAUP0C 4000-CHECK-IF-EXPIRED `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:280-284` |
| Implemented at | CBPAUP0C  `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:293-295` |
| Anchor (verified) | `IF WS-DAY-DIFF >= WS-EXPIRY-DAYS` |

### BR-CBPAUP0C-002

When an expired detail is purged, its effect is backed out of the summary totals: an approved detail (PA-AUTH-RESP-CODE '00') decrements PA-APPROVED-AUTH-CNT and reduces PA-APPROVED-AUTH-AMT by PA-APPROVED-AMT; any other response code decrements PA-DECLINED-AUTH-CNT and reduces PA-DECLINED-AUTH-AMT by PA-TRANSACTION-AMT.

| Item | Value |
|---|---|
| Category | calculation |
| Confidence | Confirmed |
| Conditions | Detail qualified for delete; split on PA-AUTH-RESP-CODE = '00' |
| Outcome | Summary counters in PENDING-AUTH-SUMMARY are reduced in working storage (no REPL of the summary segment is issued in this program). |
| Implemented at | CBPAUP0C 4000-CHECK-IF-EXPIRED `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:286-292` |
| Anchor (verified) | `IF PA-AUTH-RESP-CODE = '00'` |

### BR-CBPAUP0C-003

After all details of an account summary have been processed, the pending authorization summary root is deleted when its approved authorization count is zero or negative. The condition tests PA-APPROVED-AUTH-CNT twice; the declined count is not tested.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | PA-APPROVED-AUTH-CNT <= 0 (after expiry back-outs) |
| Outcome | 6000-DELETE-AUTH-SUMMARY performs DLET of the PAUTSUM0 segment (IMS deletes any remaining child details with it). |
| Implemented at | CBPAUP0C MAIN-PARA `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:156-158` |
| Anchor (verified) | `IF PA-APPROVED-AUTH-CNT <= 0 AND PA-APPROVED-AUTH-CNT <= 0` |

### BR-CBPAUP0C-004

Run parameters default when missing: expiry days default to 5 when the SYSIN value is not numeric; checkpoint frequency defaults to 5 and checkpoint display frequency to 10 when blank, zero or low-values; the debug flag is forced to 'N' unless it is 'Y'.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | SYSIN PRM-INFO fields absent or invalid |
| Outcome | WS-EXPIRY-DAYS = 5, P-CHKP-FREQ = 5, P-CHKP-DIS-FREQ = 10, P-DEBUG-FLAG = 'N' as applicable. |
| Implemented at | CBPAUP0C 1000-INITIALIZE `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:196-209` |
| Anchor (verified) | `IF P-EXPIRY-DAYS IS NUMERIC` |

### BR-CBPAUP0C-005

An IMS checkpoint is taken after more than P-CHKP-FREQ summaries have been processed since the last checkpoint, and again at the end of the run, so the purge is committed in units of work.

| Item | Value |
|---|---|
| Category | data-integrity |
| Confidence | Confirmed |
| Conditions | WS-AUTH-SMRY-PROC-CNT > P-CHKP-FREQ |
| Outcome | 9000-TAKE-CHECKPOINT issues DLI CHKP and WS-AUTH-SMRY-PROC-CNT is reset to 0. |
| Implemented at | CBPAUP0C MAIN-PARA `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:160-164` |
| Implemented at | CBPAUP0C  `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:169-169` |
| Anchor (verified) | `IF WS-AUTH-SMRY-PROC-CNT > P-CHKP-FREQ` |

### BR-CBPAUP0C-006

Any DL/I status other than the expected ones (spaces; 'GB' end of database on summary read; 'GE'/'GB' on detail read) on read, delete or checkpoint stops the purge with return code 16 after displaying the status and counters.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | Unexpected DIBSTAT after GN, GNP, DLET or CHKP |
| Outcome | Display 'CBPAUP0C ABENDING ...', RETURN-CODE 16, GOBACK. |
| Messages | AUTH SUMMARY READ FAILED  :; AUTH DETAIL READ FAILED  :; AUTH DETAIL DELETE FAILED :; AUTH SUMMARY DELETE FAILED :; CHKP FAILED: DIBSTAT - ; CBPAUP0C ABENDING ... |
| Implemented at | CBPAUP0C 9999-ABEND `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:380-382` |
| Implemented at | CBPAUP0C  `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:228-241` |
| Implemented at | CBPAUP0C  `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:259-271` |
| Implemented at | CBPAUP0C  `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:315-321` |
| Implemented at | CBPAUP0C  `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:340-346` |
| Implemented at | CBPAUP0C  `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:358-370` |
| Anchor (verified) | `MOVE 16 TO RETURN-CODE` |


## CBSTM03A

Program page: [CBSTM03A](07-programs/CBSTM03A.md).

### BR-CBSTM03A-001

Before any statement is produced, all transactions are loaded into a two-dimensional in-memory table grouped by card number: consecutive transactions with the same TRNX-CARD-NUM are stored under one card entry, and a change of card number starts a new card entry. The table holds up to 51 cards with up to 10 transactions each.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | TRNX-CARD-NUM equal to / different from WS-SAVE-CARD. |
| Outcome | WS-CARD-NUM, WS-TRAN-NUM, WS-TRAN-REST and WS-TRCT populated; CR-CNT = number of cards. |
| Implemented at | CBSTM03A 8500-READTRNX-READ `app/cbl/CBSTM03A.CBL:819-830` |
| Implemented at | CBSTM03A  `app/cbl/CBSTM03A.CBL:225-233` |
| Implemented at | CBSTM03A  `app/cbl/CBSTM03A.CBL:849-850` |
| Anchor (verified) | `IF WS-SAVE-CARD = TRNX-CARD-NUM` |

### BR-CBSTM03A-002

A statement lists only the transactions whose card number equals the cross-reference card number being processed. The table search stops at the first table card number greater than the cross-reference card, which assumes both files are in ascending card-number order (TRNXFILE is keyed by card number + transaction id in CBSTM03B).

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | WS-CARD-NUM(CR-JMP) = XREF-CARD-NUM; search ends when CR-JMP > CR-CNT or WS-CARD-NUM(CR-JMP) > XREF-CARD-NUM. |
| Outcome | Each matching transaction written as a detail line (text and HTML). |
| Implemented at | CBSTM03A 4000-TRNXFILE-GET `app/cbl/CBSTM03A.CBL:417-431` |
| Implemented at | CBSTM03A  `app/cbl/CBSTM03B.CBL:31-35` |
| Anchor (verified) | `IF XREF-CARD-NUM = WS-CARD-NUM (CR-JMP)` |

### BR-CBSTM03A-003

The statement total ('Total EXP:') is the sum of TRNX-AMT of all transactions listed for the card; it is reset to zero for each cross-reference record.

| Item | Value |
|---|---|
| Category | calculation |
| Confidence | Confirmed |
| Conditions | Each listed transaction. |
| Outcome | ST-TOTAL-TRAMT printed on ST-LINE14A. |
| Messages | Total EXP: |
| Implemented at | CBSTM03A 4000-TRNXFILE-GET `app/cbl/CBSTM03A.CBL:429-436` |
| Implemented at | CBSTM03A  `app/cbl/CBSTM03A.CBL:325` |
| Anchor (verified) | `ADD TRNX-AMT TO WS-TOTAL-AMT` |

### BR-CBSTM03A-004

Every card cross-reference must resolve to an existing customer (XREF-CUST-ID) and account (XREF-ACCT-ID); if either keyed read fails, or the cross-reference read fails other than end of file, the statement run abends instead of skipping the card.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | WS-M03B-RC not '00' after customer or account keyed read; not '00'/'10' after cross-reference read. |
| Outcome | 'ERROR READING CUSTFILE' / 'ERROR READING ACCTFILE' / 'ERROR READING XREFFILE', return code display, abend via CEE3ABD. |
| Messages | ERROR READING CUSTFILE; ERROR READING ACCTFILE; ERROR READING XREFFILE; RETURN CODE: |
| Implemented at | CBSTM03A 2000-CUSTFILE-GET `app/cbl/CBSTM03A.CBL:379-385` |
| Implemented at | CBSTM03A  `app/cbl/CBSTM03A.CBL:403-410` |
| Implemented at | CBSTM03A  `app/cbl/CBSTM03A.CBL:353-362` |
| Anchor (verified) | `DISPLAY 'ERROR READING CUSTFILE'` |

### BR-CBSTM03A-005

The statement header shows the customer name as first, middle and last name each truncated at the first space and separated by single spaces, address lines 1 and 2, a third address line combining address line 3, state, country and ZIP, plus account id, current balance and FICO score.

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | Every statement. |
| Outcome | ST-NAME, ST-ADD1..3, ST-ACCT-ID, ST-CURR-BAL, ST-FICO-SCORE in text and HTML output. |
| Implemented at | CBSTM03A 5000-CREATE-STATEMENT `app/cbl/CBSTM03A.CBL:462-484` |
| Anchor (verified) | `STRING CUST-FIRST-NAME DELIMITED BY ' '` |

### BR-CBSTM03A-006

One statement (text and HTML) is produced for every record in the card cross-reference file, in cross-reference order, until end of file.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | Each XREFFILE record read with RC '00'. |
| Outcome | Statement header, transaction lines and total written to STMTFILE and HTMLFILE. |
| Implemented at | CBSTM03A 1000-MAINLINE `app/cbl/CBSTM03A.CBL:317-329` |
| Anchor (verified) | `PERFORM 5000-CREATE-STATEMENT` |


## CBTRN01C

Program page: [CBTRN01C](07-programs/CBTRN01C.md).

### BR-CBTRN01C-001

A daily transaction is accepted for further checking only if its card number exists in the card cross-reference file; otherwise the transaction is reported as unverifiable and skipped.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | DALYTRAN-CARD-NUM not found in XREFFILE (INVALID KEY, WS-XREF-READ-STATUS = 4). |
| Outcome | DISPLAY 'CARD NUMBER <n> COULD NOT BE VERIFIED. SKIPPING TRANSACTION ID-<id>'; no account lookup. |
| Messages | INVALID CARD NUMBER FOR XREF; CARD NUMBER ;  COULD NOT BE VERIFIED. SKIPPING TRANSACTION ID- |
| Implemented at | CBTRN01C MAIN-PARA `app/cbl/CBTRN01C.cbl:170-183` |
| Implemented at | CBTRN01C  `app/cbl/CBTRN01C.cbl:228-239` |
| Anchor (verified) | `' COULD NOT BE VERIFIED. SKIPPING TRANSACTION ID-'` |

### BR-CBTRN01C-002

For a transaction whose card is in the cross-reference, the linked account (XREF-ACCT-ID) must exist in the account master; if not, the program reports 'ACCOUNT <id> NOT FOUND'. No further action (posting or rejection file) follows either way.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | WS-XREF-READ-STATUS = 0 and account read INVALID KEY (WS-ACCT-READ-STATUS = 4). |
| Outcome | DISPLAY 'INVALID ACCOUNT NUMBER FOUND' and 'ACCOUNT <id> NOT FOUND'. |
| Messages | INVALID ACCOUNT NUMBER FOUND; ACCOUNT ;  NOT FOUND |
| Implemented at | CBTRN01C MAIN-PARA `app/cbl/CBTRN01C.cbl:173-179` |
| Implemented at | CBTRN01C  `app/cbl/CBTRN01C.cbl:242-250` |
| Anchor (verified) | `DISPLAY 'ACCOUNT ' ACCT-ID ' NOT FOUND'` |

### BR-CBTRN01C-003

A read error on the daily transaction file (status other than '00' or '10') aborts the run with abend code 999, while card or account lookup failures only skip/report the transaction.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | DALYTRAN-STATUS not '00' and not '10'. |
| Outcome | File status displayed; CEE3ABD abend code 999. |
| Messages | ERROR READING DAILY TRANSACTION FILE; ABENDING PROGRAM |
| Implemented at | CBTRN01C 1000-DALYTRAN-GET-NEXT `app/cbl/CBTRN01C.cbl:213-224` |
| Anchor (verified) | `DISPLAY 'ERROR READING DAILY TRANSACTION FILE'` |


## CBTRN02C

Program page: [CBTRN02C](07-programs/CBTRN02C.md).

### BR-CBTRN02C-001

Each daily transaction's card number (DALYTRAN-CARD-NUM) must exist in the card cross-reference file; otherwise the transaction is rejected with reason 100 'INVALID CARD NUMBER FOUND'.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | No XREF-FILE record keyed by DALYTRAN-CARD-NUM (INVALID KEY). |
| Outcome | WS-VALIDATION-FAIL-REASON = 100, description 'INVALID CARD NUMBER FOUND'; the transaction is later written to DALYREJS. |
| Messages | INVALID CARD NUMBER FOUND |
| Implemented at | CBTRN02C 1500-A-LOOKUP-XREF `app/cbl/CBTRN02C.cbl:382-391` |
| Anchor (verified) | `MOVE 100 TO WS-VALIDATION-FAIL-REASON` |

### BR-CBTRN02C-002

Account-level validation (account existence, credit limit, expiration) is only performed when the card cross-reference lookup succeeded.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | WS-VALIDATION-FAIL-REASON = 0 after the xref lookup. |
| Outcome | 1500-B-LOOKUP-ACCT is performed; otherwise the reason 100 stands. |
| Implemented at | CBTRN02C 1500-VALIDATE-TRAN `app/cbl/CBTRN02C.cbl:372-376` |
| Anchor (verified) | `IF WS-VALIDATION-FAIL-REASON = 0 PERFORM 1500-B-LOOKUP-ACCT` |

### BR-CBTRN02C-003

The account referenced by the card cross-reference (XREF-ACCT-ID) must exist in the account master; otherwise the transaction is rejected with reason 101 'ACCOUNT RECORD NOT FOUND'.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | No ACCOUNT-FILE record keyed by XREF-ACCT-ID (INVALID KEY). |
| Outcome | WS-VALIDATION-FAIL-REASON = 101, description 'ACCOUNT RECORD NOT FOUND'. |
| Messages | ACCOUNT RECORD NOT FOUND |
| Implemented at | CBTRN02C 1500-B-LOOKUP-ACCT `app/cbl/CBTRN02C.cbl:394-399` |
| Anchor (verified) | `MOVE 101 TO WS-VALIDATION-FAIL-REASON` |

### BR-CBTRN02C-004

The projected cycle balance used for the credit-limit check is WS-TEMP-BAL = ACCT-CURR-CYC-CREDIT - ACCT-CURR-CYC-DEBIT + DALYTRAN-AMT (the account's current balance ACCT-CURR-BAL is not used).

| Item | Value |
|---|---|
| Category | calculation |
| Confidence | Confirmed |
| Conditions | Account record found. |
| Outcome | WS-TEMP-BAL holds the projected balance compared against the credit limit. |
| Implemented at | CBTRN02C 1500-B-LOOKUP-ACCT `app/cbl/CBTRN02C.cbl:403-405` |
| Anchor (verified) | `COMPUTE WS-TEMP-BAL = ACCT-CURR-CYC-CREDIT - ACCT-CURR-CYC-DEBIT + DALYTRAN-AMT` |

### BR-CBTRN02C-005

A transaction is rejected as over-limit (reason 102 'OVERLIMIT TRANSACTION') when the account credit limit is less than the projected cycle balance WS-TEMP-BAL; a projected balance equal to the limit is allowed.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | ACCT-CREDIT-LIMIT < WS-TEMP-BAL. |
| Outcome | WS-VALIDATION-FAIL-REASON = 102, description 'OVERLIMIT TRANSACTION' (may be overwritten by reason 103). |
| Messages | OVERLIMIT TRANSACTION |
| Implemented at | CBTRN02C 1500-B-LOOKUP-ACCT `app/cbl/CBTRN02C.cbl:407-413` |
| Anchor (verified) | `IF ACCT-CREDIT-LIMIT >= WS-TEMP-BAL` |

### BR-CBTRN02C-006

A transaction whose origination date (first 10 characters of DALYTRAN-ORIG-TS) is later than the account expiration date ACCT-EXPIRAION-DATE is rejected with reason 103 'TRANSACTION RECEIVED AFTER ACCT EXPIRATION'; a transaction on the expiration date itself is accepted. This check runs even if the over-limit check already failed and then overrides reason 102.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | ACCT-EXPIRAION-DATE < DALYTRAN-ORIG-TS(1:10), compared as character strings. |
| Outcome | WS-VALIDATION-FAIL-REASON = 103, description 'TRANSACTION RECEIVED AFTER ACCT EXPIRATION'. |
| Messages | TRANSACTION RECEIVED AFTER ACCT EXPIRATION |
| Implemented at | CBTRN02C 1500-B-LOOKUP-ACCT `app/cbl/CBTRN02C.cbl:414-420` |
| Anchor (verified) | `IF ACCT-EXPIRAION-DATE >= DALYTRAN-ORIG-TS (1:10)` |

### BR-CBTRN02C-007

A daily transaction that passes all validations (reason code 0) is posted; any non-zero reason code causes the transaction to be counted as rejected and written to the daily rejects file instead of being posted.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | WS-VALIDATION-FAIL-REASON = 0 after 1500-VALIDATE-TRAN. |
| Outcome | Posted via 2000-POST-TRANSACTION; otherwise WS-REJECT-COUNT + 1 and 2500-WRITE-REJECT-REC. |
| Implemented at | CBTRN02C (PROCEDURE DIVISION entry) `app/cbl/CBTRN02C.cbl:211-216` |
| Anchor (verified) | `IF WS-VALIDATION-FAIL-REASON = 0 PERFORM 2000-POST-TRANSACTION` |

### BR-CBTRN02C-008

A rejected transaction is written to DALYREJS as the full 350-byte input record followed by an 80-byte validation trailer containing the 4-digit reason code and its 76-character description.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | Transaction failed validation. |
| Outcome | One REJECT-RECORD written to DALYREJS (LRECL 430). |
| Implemented at | CBTRN02C 2500-WRITE-REJECT-REC `app/cbl/CBTRN02C.cbl:447-451` |
| Implemented at | CBTRN02C  `app/cbl/CBTRN02C.cbl:176-182` |
| Anchor (verified) | `MOVE WS-VALIDATION-TRAILER TO VALIDATION-TRAILER` |

### BR-CBTRN02C-009

When at least one transaction was rejected, the job step ends with return code 4 (warning) instead of 0.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | WS-REJECT-COUNT > 0 at end of run. |
| Outcome | RETURN-CODE = 4. |
| Implemented at | CBTRN02C (PROCEDURE DIVISION entry) `app/cbl/CBTRN02C.cbl:229-231` |
| Anchor (verified) | `IF WS-REJECT-COUNT > 0 MOVE 4 TO RETURN-CODE` |

### BR-CBTRN02C-010

A posted transaction record copies all business fields from the daily transaction record and stamps TRAN-PROC-TS with the current system timestamp in DB2 format (the input DALYTRAN-PROC-TS is not used).

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | Transaction passed validation. |
| Outcome | TRAN-RECORD populated and later written to TRANSACT-FILE. |
| Implemented at | CBTRN02C 2000-POST-TRANSACTION `app/cbl/CBTRN02C.cbl:425-438` |
| Implemented at | CBTRN02C  `app/cbl/CBTRN02C.cbl:692-703` |
| Anchor (verified) | `MOVE DB2-FORMAT-TS TO TRAN-PROC-TS` |

### BR-CBTRN02C-011

Category balances are kept per account + transaction type + transaction category. If no balance record exists for that key, a new one is created; otherwise the existing record is updated.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | TCATBAL READ by key (XREF-ACCT-ID, DALYTRAN-TYPE-CD, DALYTRAN-CAT-CD) returned INVALID KEY. |
| Outcome | 2700-A-CREATE-TCATBAL-REC when not found, else 2700-B-UPDATE-TCATBAL-REC. |
| Messages | TCATBAL record not found for key : |
| Implemented at | CBTRN02C 2700-UPDATE-TCATBAL `app/cbl/CBTRN02C.cbl:495-499` |
| Implemented at | CBTRN02C  `app/cbl/CBTRN02C.cbl:469-478` |
| Anchor (verified) | `IF WS-CREATE-TRANCAT-REC = 'Y'` |

### BR-CBTRN02C-012

A newly created category balance record starts at zero and is set to the transaction amount.

| Item | Value |
|---|---|
| Category | calculation |
| Confidence | Confirmed |
| Conditions | No existing balance record for the key. |
| Outcome | New TCATBAL record written with TRAN-CAT-BAL = DALYTRAN-AMT. |
| Implemented at | CBTRN02C 2700-A-CREATE-TCATBAL-REC `app/cbl/CBTRN02C.cbl:504-510` |
| Anchor (verified) | `ADD DALYTRAN-AMT TO TRAN-CAT-BAL` |

### BR-CBTRN02C-013

For an existing category balance record, the transaction amount (signed) is added to TRAN-CAT-BAL and the record is rewritten.

| Item | Value |
|---|---|
| Category | calculation |
| Confidence | Confirmed |
| Conditions | Balance record exists for the key. |
| Outcome | TRAN-CAT-BAL = TRAN-CAT-BAL + DALYTRAN-AMT; REWRITE. |
| Implemented at | CBTRN02C 2700-B-UPDATE-TCATBAL-REC `app/cbl/CBTRN02C.cbl:527-528` |
| Anchor (verified) | `ADD DALYTRAN-AMT TO TRAN-CAT-BAL` |

### BR-CBTRN02C-014

Posting adds the signed transaction amount to the account current balance ACCT-CURR-BAL; non-negative amounts are also accumulated in ACCT-CURR-CYC-CREDIT and negative amounts in ACCT-CURR-CYC-DEBIT (as negative values).

| Item | Value |
|---|---|
| Category | calculation |
| Confidence | Confirmed |
| Conditions | Transaction is being posted; split on DALYTRAN-AMT >= 0. |
| Outcome | ACCT-CURR-BAL and either ACCT-CURR-CYC-CREDIT or ACCT-CURR-CYC-DEBIT updated; account record rewritten. |
| Implemented at | CBTRN02C 2800-UPDATE-ACCOUNT-REC `app/cbl/CBTRN02C.cbl:547-552` |
| Anchor (verified) | `IF DALYTRAN-AMT >= 0 ADD DALYTRAN-AMT TO ACCT-CURR-CYC-CREDIT` |

### BR-CBTRN02C-015

If the account rewrite fails with INVALID KEY, reason 109 'ACCOUNT RECORD NOT FOUND' is set but has no effect: the transaction is still written to the transaction master and is not rejected.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | REWRITE FD-ACCTFILE-REC raises INVALID KEY. |
| Outcome | WS-VALIDATION-FAIL-REASON = 109 set; processing continues with 2900-WRITE-TRANSACTION-FILE. |
| Messages | ACCOUNT RECORD NOT FOUND |
| Implemented at | CBTRN02C 2800-UPDATE-ACCOUNT-REC `app/cbl/CBTRN02C.cbl:554-559` |
| Implemented at | CBTRN02C  `app/cbl/CBTRN02C.cbl:440-442` |
| Anchor (verified) | `MOVE 109 TO WS-VALIDATION-FAIL-REASON` |

### BR-CBTRN02C-016

When reading the category balance file, status '00' (found) and '23' (not found) are both normal; any other status stops the run with 'ERROR READING TRANSACTION BALANCE FILE' and an abend.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | TCATBALF-STATUS not '00' and not '23'. |
| Outcome | Abend via 9999-ABEND-PROGRAM. |
| Messages | ERROR READING TRANSACTION BALANCE FILE |
| Implemented at | CBTRN02C 2700-UPDATE-TCATBAL `app/cbl/CBTRN02C.cbl:481-493` |
| Anchor (verified) | `IF TCATBALF-STATUS = '00' OR '23'` |

### BR-CBTRN02C-017

Any fatal file error (open, read, write, rewrite or close failure that the program tests) terminates the job step with user abend code 999 through the Language Environment service CEE3ABD.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | A paragraph detects a non-'00' file status (or non-'00'/'10' on read). |
| Outcome | Abend U999 after displaying 'ABENDING PROGRAM'. |
| Messages | ABENDING PROGRAM |
| Implemented at | CBTRN02C 9999-ABEND-PROGRAM `app/cbl/CBTRN02C.cbl:707-711` |
| Anchor (verified) | `CALL 'CEE3ABD' USING ABCODE, TIMING` |


## CBTRN03C

Program page: [CBTRN03C](07-programs/CBTRN03C.md).

### BR-CBTRN03C-001

Only transactions whose processing date (first 10 characters of TRAN-PROC-TS) is between the DATEPARM start date and end date, both inclusive, are reported. The comparison is a character comparison. An out-of-range record executes NEXT SENTENCE, which (Inferred) leaves the read loop rather than skipping just that record.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | WS-START-DATE <= TRAN-PROC-TS(1:10) <= WS-END-DATE. |
| Outcome | In range: record is processed. Out of range: NEXT SENTENCE. |
| Implemented at | CBTRN03C (PROCEDURE DIVISION entry) `app/cbl/CBTRN03C.cbl:173-178` |
| Implemented at | CBTRN03C  `app/cbl/CBTRN03C.cbl:122-125` |
| Anchor (verified) | `IF TRAN-PROC-TS (1:10) >= WS-START-DATE AND TRAN-PROC-TS (1:10) <= WS-END-DATE` |

### BR-CBTRN03C-002

When the card number changes from the previous transaction, the accumulated 'Account Total' of the previous card is printed (not before the first detail line) and the card cross-reference is read to obtain the account id for the new card. Correct grouping relies on the input being sorted by card number (done by the SORT step in TRANREPT.jcl).

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | WS-CURR-CARD-NUM differs from TRAN-CARD-NUM; account totals only when WS-FIRST-TIME = 'N'. |
| Outcome | 1120-WRITE-ACCOUNT-TOTALS, WS-CURR-CARD-NUM updated, 1500-A-LOOKUP-XREF performed. |
| Implemented at | CBTRN03C (PROCEDURE DIVISION entry) `app/cbl/CBTRN03C.cbl:181-187` |
| Implemented at | CBTRN03C  `app/jcl/TRANREPT.jcl:46` |
| Anchor (verified) | `IF WS-CURR-CARD-NUM NOT= TRAN-CARD-NUM` |

### BR-CBTRN03C-003

A reported transaction whose card number is not in the card cross-reference file stops the report run with an abend.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | XREF-FILE READ returns INVALID KEY. |
| Outcome | Display 'INVALID CARD NUMBER : ', file status 0023, abend 999. |
| Messages | INVALID CARD NUMBER : |
| Implemented at | CBTRN03C 1500-A-LOOKUP-XREF `app/cbl/CBTRN03C.cbl:485-491` |
| Anchor (verified) | `DISPLAY 'INVALID CARD NUMBER : ' FD-XREF-CARD-NUM` |

### BR-CBTRN03C-004

A reported transaction whose type code is not in the transaction type file stops the report run with an abend.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | TRANTYPE-FILE READ returns INVALID KEY. |
| Outcome | Display 'INVALID TRANSACTION TYPE : ', file status 0023, abend 999. |
| Messages | INVALID TRANSACTION TYPE : |
| Implemented at | CBTRN03C 1500-B-LOOKUP-TRANTYPE `app/cbl/CBTRN03C.cbl:495-501` |
| Anchor (verified) | `DISPLAY 'INVALID TRANSACTION TYPE : ' FD-TRAN-TYPE` |

### BR-CBTRN03C-005

A reported transaction whose type + category combination is not in the transaction category file stops the report run with an abend.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | TRANCATG-FILE READ returns INVALID KEY. |
| Outcome | Display 'INVALID TRAN CATG KEY : ', file status 0023, abend 999. |
| Messages | INVALID TRAN CATG KEY : |
| Implemented at | CBTRN03C 1500-C-LOOKUP-TRANCATG `app/cbl/CBTRN03C.cbl:505-511` |
| Anchor (verified) | `DISPLAY 'INVALID TRAN CATG KEY : ' FD-TRAN-CAT-KEY` |

### BR-CBTRN03C-006

Before the first detail line the report header is written once with the DATEPARM start and end dates as the report date range.

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | WS-FIRST-TIME = 'Y'. |
| Outcome | WS-FIRST-TIME set to 'N'; headers written. |
| Implemented at | CBTRN03C 1100-WRITE-TRANSACTION-REPORT `app/cbl/CBTRN03C.cbl:275-280` |
| Anchor (verified) | `MOVE WS-START-DATE TO REPT-START-DATE` |

### BR-CBTRN03C-007

A page break (page total line followed by new headers) occurs before a detail line whenever the running line count is an exact multiple of the page size of 20 lines.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | MOD(WS-LINE-COUNTER, 20) = 0. |
| Outcome | 1110-WRITE-PAGE-TOTALS and 1120-WRITE-HEADERS. |
| Implemented at | CBTRN03C 1100-WRITE-TRANSACTION-REPORT `app/cbl/CBTRN03C.cbl:282-284` |
| Implemented at | CBTRN03C  `app/cbl/CBTRN03C.cbl:129-132` |
| Anchor (verified) | `IF FUNCTION MOD(WS-LINE-COUNTER, WS-PAGE-SIZE) = 0` |

### BR-CBTRN03C-008

Each reported transaction amount is added to both the current page total and the current account (card) total.

| Item | Value |
|---|---|
| Category | calculation |
| Confidence | Confirmed |
| Conditions | Transaction is reported. |
| Outcome | WS-PAGE-TOTAL and WS-ACCOUNT-TOTAL increased by TRAN-AMT. |
| Implemented at | CBTRN03C 1100-WRITE-TRANSACTION-REPORT `app/cbl/CBTRN03C.cbl:286-288` |
| Anchor (verified) | `ADD TRAN-AMT TO WS-PAGE-TOTAL WS-ACCOUNT-TOTAL` |

### BR-CBTRN03C-009

The grand total is the sum of the page totals: when a page total is printed it is added to WS-GRAND-TOTAL and the page total is reset to zero.

| Item | Value |
|---|---|
| Category | calculation |
| Confidence | Confirmed |
| Conditions | Page total line written. |
| Outcome | WS-GRAND-TOTAL += WS-PAGE-TOTAL; WS-PAGE-TOTAL = 0. |
| Messages | Page Total |
| Implemented at | CBTRN03C 1110-WRITE-PAGE-TOTALS `app/cbl/CBTRN03C.cbl:294-298` |
| Anchor (verified) | `ADD WS-PAGE-TOTAL TO WS-GRAND-TOTAL` |

### BR-CBTRN03C-010

When an account (card) total is printed, WS-ACCOUNT-TOTAL is reset to zero for the next card.

| Item | Value |
|---|---|
| Category | calculation |
| Confidence | Confirmed |
| Conditions | Card number change. |
| Outcome | 'Account Total' line written; WS-ACCOUNT-TOTAL = 0. |
| Messages | Account Total |
| Implemented at | CBTRN03C 1120-WRITE-ACCOUNT-TOTALS `app/cbl/CBTRN03C.cbl:307-310` |
| Anchor (verified) | `MOVE 0 TO WS-ACCOUNT-TOTAL` |

### BR-CBTRN03C-011

At end of the transaction file the program adds TRAN-AMT (still holding the last record read) to the page and account totals, then prints the final page total and the grand total; no final account total is printed.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | END-OF-FILE = 'Y' after the read. |
| Outcome | 1110-WRITE-PAGE-TOTALS and 1110-WRITE-GRAND-TOTALS. |
| Messages | Grand Total |
| Implemented at | CBTRN03C (PROCEDURE DIVISION entry) `app/cbl/CBTRN03C.cbl:197-203` |
| Anchor (verified) | `PERFORM 1110-WRITE-GRAND-TOTALS` |

### BR-CBTRN03C-012

The report date range comes from the first DATEPARM record; if DATEPARM is empty the run ends without reading transactions or writing a report line, and any other read error abends.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | DATEPARM-STATUS '00' / '10' / other. |
| Outcome | '00': display range; '10': END-OF-FILE = 'Y'; other: 'ERROR READING DATEPARM FILE' and abend. |
| Messages | Reporting from ; ERROR READING DATEPARM FILE |
| Implemented at | CBTRN03C 0550-DATEPARM-READ `app/cbl/CBTRN03C.cbl:231-242` |
| Anchor (verified) | `DISPLAY 'Reporting from ' WS-START-DATE` |

### BR-CBTRN03C-013

Each detail line shows transaction id, account id (from the card xref), type code and description, category code and description, source and amount; descriptions are truncated to the report column widths (15 and 29 characters).

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | Transaction is reported. |
| Outcome | TRANSACTION-DETAIL-REPORT written to TRANREPT. |
| Implemented at | CBTRN03C 1120-WRITE-DETAIL `app/cbl/CBTRN03C.cbl:362-371` |
| Implemented at | CBTRN03C  `app/cpy/CVTRA07Y.cpy:15-31` |
| Anchor (verified) | `MOVE XREF-ACCT-ID TO TRAN-REPORT-ACCOUNT-ID` |

### BR-CBTRN03C-014

Any fatal file error tested by the program terminates the step with user abend code 999 via CEE3ABD.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | Open/read/write/close status not as expected, or a lookup INVALID KEY. |
| Outcome | Abend U999 after 'ABENDING PROGRAM'. |
| Messages | ABENDING PROGRAM |
| Implemented at | CBTRN03C 9999-ABEND-PROGRAM `app/cbl/CBTRN03C.cbl:626-630` |
| Anchor (verified) | `CALL 'CEE3ABD' USING ABCODE, TIMING` |


## COACCT01

Program page: [COACCT01](07-programs/COACCT01.md).

### BR-COACCT01-001

An account inquiry request is accepted only when the 4-character function code WS-FUNC equals 'INQA' and the 11-digit account number WS-KEY is greater than zero. Otherwise no file read happens and the reply is 'INVALID REQUEST PARAMETERS ACCT ID : ' followed by WS-KEY and 'FUNCTION : ' followed by WS-FUNC.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | WS-FUNC not 'INQA' or WS-KEY = 0 |
| Outcome | Rejection text reply put on the reply queue; request is consumed. |
| Messages | INVALID REQUEST PARAMETERS ; ACCT ID : ; FUNCTION : |
| Implemented at | COACCT01 4000-PROCESS-REQUEST-REPLY `app/app-vsam-mq/cbl/COACCT01.cbl:393-394` |
| Implemented at | COACCT01  `app/app-vsam-mq/cbl/COACCT01.cbl:447-455` |
| Anchor (verified) | `IF WS-FUNC = 'INQA' AND WS-KEY > ZEROES` |

### BR-COACCT01-002

When the account is found in ACCTDAT, the reply is the fixed-layout text record WS-ACCT-RESPONSE: labels 'ACCOUNT ID : ', 'ACCOUNT STATUS : ', 'BALANCE : ', 'CREDIT LIMIT : ', 'CASH LIMIT : ', 'OPEN DATE : ', 'EXPR DATE : ', 'REIS DATE : ', 'CREDIT BAL : ', 'DEBIT BAL : ', 'GROUP ID : ' each followed by the matching ACCOUNT-RECORD field. ACCT-ADDR-ZIP is not returned.

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | CICS READ of ACCTDAT by WS-KEY returns NORMAL |
| Outcome | Formatted account reply put on CARD.DEMO.REPLY.ACCT |
| Messages | ACCOUNT ID : ; ACCOUNT STATUS : ; BALANCE : ; CREDIT LIMIT : |
| Implemented at | COACCT01 4000-PROCESS-REQUEST-REPLY `app/app-vsam-mq/cbl/COACCT01.cbl:406-427` |
| Implemented at | COACCT01  `app/app-vsam-mq/cbl/COACCT01.cbl:130-169` |
| Implemented at | COACCT01  `app/cpy/CVACT01Y.cpy:4-17` |
| Anchor (verified) | `MOVE WS-ACCT-RESPONSE TO REPLY-MESSAGE` |

### BR-COACCT01-003

If the requested account number is not on ACCTDAT (NOTFND), the requester receives the reply 'INVALID REQUEST PARAMETERS ACCT ID : ' followed by WS-KEY; processing continues with the next message.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | CICS READ response NOTFND |
| Outcome | Not-found text reply put on the reply queue |
| Messages | INVALID REQUEST PARAMETERS ; ACCT ID : |
| Implemented at | COACCT01 4000-PROCESS-REQUEST-REPLY `app/app-vsam-mq/cbl/COACCT01.cbl:428-434` |
| Anchor (verified) | `WHEN DFHRESP(NOTFND)` |

### BR-COACCT01-004

Any other ACCTDAT READ response (not NORMAL or NOTFND) sends an error record 'ERROR WHILE READING ACCTFILE' with the RESP/RESP2 values to the error queue and ends the transaction; no reply is sent to the requester and remaining messages are left for a later trigger.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | WS-RESP-CD other than NORMAL or NOTFND |
| Outcome | Error message on CARD.DEMO.ERROR, 8000-TERMINATION (CICS RETURN) |
| Messages | ERROR WHILE READING ACCTFILE |
| Implemented at | COACCT01 4000-PROCESS-REQUEST-REPLY `app/app-vsam-mq/cbl/COACCT01.cbl:437-445` |
| Anchor (verified) | `MOVE 'ERROR WHILE READING ACCTFILE'` |

### BR-COACCT01-005

Replies are always put on the fixed queue CARD.DEMO.REPLY.ACCT (not the request's ReplyToQ) with the reply MsgId and CorrelId copied from the request message, as an MQFMT-STRING message in the queue manager CCSID.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | Every reply (success, not-found, invalid request) |
| Outcome | MQPUT to OUTPUT-QUEUE-HANDLE |
| Messages | CARD.DEMO.REPLY.ACCT |
| Implemented at | COACCT01 4100-PUT-REPLY `app/app-vsam-mq/cbl/COACCT01.cbl:466-477` |
| Implemented at | COACCT01  `app/app-vsam-mq/cbl/COACCT01.cbl:196-198` |
| Anchor (verified) | `MOVE SAVE-CORELID                 TO MQMD-CORRELID` |

### BR-COACCT01-006

The transaction drains the triggered input queue: it keeps getting messages (waiting up to 5 seconds each time) and commits with CICS SYNCPOINT after each one, stopping normally when MQGET returns MQRC-NO-MSG-AVAILABLE. Any other MQGET failure is reported as 'INP MQGET ERR:' on the error queue and ends the transaction.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | MQ-CONDITION-CODE not MQCC-OK |
| Outcome | NO-MORE-MSGS set (normal end) or error report and termination |
| Messages | INP MQGET ERR: |
| Implemented at | COACCT01 3000-GET-REQUEST `app/app-vsam-mq/cbl/COACCT01.cbl:363-387` |
| Implemented at | COACCT01  `app/app-vsam-mq/cbl/COACCT01.cbl:337-338` |
| Implemented at | COACCT01  `app/app-vsam-mq/cbl/COACCT01.cbl:325-331` |
| Implemented at | COACCT01  `app/app-vsam-mq/cbl/COACCT01.cbl:214-216` |
| Anchor (verified) | `IF MQ-REASON-CODE  =  MQRC-NO-MSG-AVAILABLE` |

### BR-COACCT01-007

If the input queue or reply queue cannot be opened, or a reply cannot be put, the program writes an error record (paragraph text, condition code, reason code, queue name and 'INP MQOPEN ERR' / 'OUT MQOPEN ERR' / 'MQPUT ERR') to CARD.DEMO.ERROR and ends the transaction.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | MQOPEN or MQPUT completion code other than MQCC-OK |
| Outcome | 9000-ERROR then 8000-TERMINATION |
| Messages | INP MQOPEN ERR; OUT MQOPEN ERR; MQPUT ERR |
| Implemented at | COACCT01 2300-OPEN-INPUT-QUEUE `app/app-vsam-mq/cbl/COACCT01.cbl:240-252` |
| Implemented at | COACCT01  `app/app-vsam-mq/cbl/COACCT01.cbl:274-286` |
| Implemented at | COACCT01  `app/app-vsam-mq/cbl/COACCT01.cbl:488-498` |
| Anchor (verified) | `MOVE 'INP MQOPEN ERR'  TO MQ-APPL-RETURN-MESSAGE` |

### BR-COACCT01-008

If the CICS trigger data cannot be retrieved (RETRIEVE response not NORMAL), the program reports 'CICS RETREIVE' with the RESP code to the error queue and ends without processing any request.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | EXEC CICS RETRIEVE INTO(MQTM) response not NORMAL |
| Outcome | 9000-ERROR then 8000-TERMINATION |
| Messages | CICS RETREIVE; RESP: |
| Implemented at | COACCT01 1000-CONTROL `app/app-vsam-mq/cbl/COACCT01.cbl:195-210` |
| Anchor (verified) | `IF WS-CICS-RESP1-CD =  DFHRESP(NORMAL)` |


## COACTUPC

Program page: [COACTUPC](07-programs/COACTUPC.md).

### BR-BASE-003

Each field edit writes its message only when no message is set yet, so the screen shows the first failing edit.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | WS-RETURN-MSG = spaces (WS-RETURN-MSG-OFF) |
| Outcome | write the edit message into WS-RETURN-MSG |
| Implemented at | COCRDUPC  `app/cbl/COCRDUPC.cbl:173-174` |
| Implemented at | COCRDUPC 1210-EDIT-ACCOUNT `app/cbl/COCRDUPC.cbl:730-732` |
| Implemented at | COACTUPC  `app/cbl/COACTUPC.cbl:480` |
| Implemented at | COACTUPC 1210-EDIT-ACCOUNT `app/cbl/COACTUPC.cbl:1805-1812` |
| Implemented at | COCRDSLC  `app/cbl/COCRDSLC.cbl:135` |
| Implemented at | COACTVWC  `app/cbl/COACTVWC.cbl:118` |
| Implemented at | COTRTUPC 1230-EDIT-ALPHANUM-REQD `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:863-868` |
| Batch review | corrected: Cited line 118 is only the 88-level WS-RETURN-MSG-OFF definition. In COACTVWC the 'first message wins' guard is applied in 2210-EDIT-ACCOUNT (657, 670) and the NOTFND branches of the reads (743, 792, 845), but NOT universally: the cross-field edit at 640-642 sets 'No input received' unconditionally, overwriting 'Account number not provided', and the WHEN OTHER read-error branches (762-766, 812-816, 861-865) overwrite any prior message with the file-error text. (`app/cbl/COACTVWC.cbl:653-680`, anchor `IF WS-RETURN-MSG-OFF`) |

### BR-BASE-004

When no field edit sets INPUT-ERROR, the card update, account update and transaction-type update programs mark the changes as validated but not yet confirmed.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | INPUT-ERROR not set |
| Outcome | set CCUP-CHANGES-OK-NOT-CONFIRMED or ACUP-CHANGES-OK-NOT-CONFIRMED |
| Implemented at | COCRDUPC 1200-EDIT-MAP-INPUTS `app/cbl/COCRDUPC.cbl:710-714` |
| Implemented at | COACTUPC 1200-EDIT-MAP-INPUTS `app/cbl/COACTUPC.cbl:1671-1675` |
| Implemented at | COTRTUPC 1200-EDIT-MAP-INPUTS `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:772-775` |
| Batch review | confirmed: Confirmed: after all edits, no INPUT-ERROR sets ACUP-CHANGES-OK-NOT-CONFIRMED ('N'). ACUP-CHANGES-NOT-OK ('E') was set before the edits (app/cbl/COACTUPC.cbl:1470), so any error leaves the state at 'E'. 2000-DECIDE-ACTION repeats the same transition for ACUP-SHOW-DETAILS (2585-2591). (`app/cbl/COACTUPC.cbl:1670-1675`, anchor `SET ACUP-CHANGES-OK-NOT-CONFIRMED TO TRUE`) |

### BR-BASE-COACTUPC-001

Before account details are fetched, a blank account number is reported as not provided, and the message becomes No input received. A supplied account number that is not numeric or is zero is rejected.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | CC-ACCT-ID = low-values or spaces ; CC-ACCT-ID is not numeric, or CC-ACCT-ID-N = zeros |
| Outcome | set INPUT-ERROR and redisplay the screen - No input received; set INPUT-ERROR and redisplay the screen - Account Number if supplied must be a 11 digit Non-Zero Number |
| Messages | Account number not provided; No input received; Account Number if supplied must be a 11 digit Non-Zero Number |
| Implemented at | COACTUPC 1200-EDIT-MAP-INPUTS `app/cbl/COACTUPC.cbl:1433-1446` |
| Implemented at | COACTUPC 1210-EDIT-ACCOUNT `app/cbl/COACTUPC.cbl:1783-1818` |
| Implemented at | COACTUPC  `app/cbl/COACTUPC.cbl:483-490` |
| Batch review | confirmed: Confirmed. Blank id: INPUT-ERROR, FLG-ACCTFILTER-BLANK, 'Account number not provided' (1787-1797), then replaced by 'No input received' in 1200-EDIT-MAP-INPUTS (1441-1443). Non-numeric or zero id: 'Account Number if supplied must be a 11 digit Non-Zero Number' (1802-1813). The 88-level texts at 492-495 (SEARCHED-ACCT-*) are not used by this check. (`app/cbl/COACTUPC.cbl:1783-1818`, anchor `IF CC-ACCT-ID IS NOT NUMERIC`) |

### BR-BASE-COACTUPC-002

No change is reported when every account and customer field equals the fetched value. Text fields are compared after trim and upper case. Amounts, dates, phone parts, SSN, EFT account and FICO score are compared exactly. Field edits are then skipped.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | all ACUP-NEW-* fields = matching ACUP-OLD-* fields |
| Outcome | skip the field edits - No change detected with respect to values fetched. |
| Messages | No change detected with respect to values fetched. |
| Implemented at | COACTUPC 1205-COMPARE-OLD-NEW `app/cbl/COACTUPC.cbl:1681-1775` |
| Implemented at | COACTUPC 1200-EDIT-MAP-INPUTS `app/cbl/COACTUPC.cbl:1460-1467` |
| Implemented at | COACTUPC  `app/cbl/COACTUPC.cbl:491-492` |
| Batch review | confirmed: Confirmed. Detail: account status is compared upper-cased without trim, account group id and customer id trimmed and upper-cased, the primary-holder flag and government id trimmed and upper-cased. A change only in letter case is therefore reported as 'No change detected'. Field edits are skipped at 1463-1468. (`app/cbl/COACTUPC.cbl:1681-1775`, anchor `SET NO-CHANGES-DETECTED TO TRUE`) |

### BR-BASE-COACTUPC-003

Account Status and Primary Card Holder are required and must be Y or N. Low-values, spaces or zeros count as not supplied.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | field = low-values, spaces or zeros ; field not Y or N |
| Outcome | set INPUT-ERROR and redisplay the screen - <field> must be supplied.; set INPUT-ERROR and redisplay the screen - <field> must be Y or N. |
| Messages | <field> must be supplied.; <field> must be Y or N. |
| Implemented at | COACTUPC 1200-EDIT-MAP-INPUTS `app/cbl/COACTUPC.cbl:1472-1476` |
| Implemented at | COACTUPC 1200-EDIT-MAP-INPUTS `app/cbl/COACTUPC.cbl:1657-1662` |
| Implemented at | COACTUPC 1220-EDIT-YESNO `app/cbl/COACTUPC.cbl:1856-1892` |
| Batch review | confirmed: Confirmed: low-values, spaces or zeros give '<field> must be supplied.'; anything other than 'Y'/'N' (88 at 78) gives '<field> must be Y or N.'. Only upper-case Y/N are accepted. Applied to Account Status (1472-1476) and Primary Card Holder (1657-1662). (`app/cbl/COACTUPC.cbl:1856-1893`, anchor `IF FLG-YES-NO-ISVALID`) |

### BR-BASE-COACTUPC-004

Credit Limit, Cash Credit Limit, Current Balance, Current Cycle Credit and Current Cycle Debit are required and must pass the TEST-NUMVAL-C numeric test.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | WS-EDIT-SIGNED-NUMBER-9V2-X = low-values or spaces ; TEST-NUMVAL-C(field) not 0 |
| Outcome | set INPUT-ERROR and redisplay the screen - <field> must be supplied.; set INPUT-ERROR and redisplay the screen - <field> is not valid |
| Messages | <field> must be supplied.; <field> is not valid |
| Implemented at | COACTUPC 1200-EDIT-MAP-INPUTS `app/cbl/COACTUPC.cbl:1484-1527` |
| Implemented at | COACTUPC 1250-EDIT-SIGNED-9V2 `app/cbl/COACTUPC.cbl:2180-2219` |
| Batch review | confirmed: Confirmed for credit limit, cash credit limit, current balance, cycle credit and cycle debit (calls at 1483-1527). No sign, range or cross-field check (for example cash limit not above credit limit) is coded. (`app/cbl/COACTUPC.cbl:2180-2219`, anchor `IF FUNCTION TEST-NUMVAL-C(WS-EDIT-SIGNED-NUMBER-9V2-X) = 0`) |

### BR-BASE-COACTUPC-005

A date year is required, must be numeric, and its century must be 19 or 20. The month is required and must be 1 through 12. The day is required and must be 1 through 31.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | WS-EDIT-DATE-CCYY blank, not numeric, or century not 19 or 20 ; WS-EDIT-DATE-MM blank or not 1 thru 12 ; WS-EDIT-DATE-DD blank or not 1 thru 31 |
| Outcome | set INPUT-ERROR and redisplay the screen - <field> : Year must be supplied.; set INPUT-ERROR and redisplay the screen - <field> must be 4 digit number.; set INPUT-ERROR and redisplay the screen - <field> : Century is not valid.; set INPUT-ERROR and redisplay the screen - <field> : Month must be supplied.; set INPUT-ERROR and redisplay the screen - <field>: Month must be a number between 1 and 12.; set INPUT-ERROR and redisplay the screen - <field> : Day must be supplied.; set INPUT-ERROR and redisplay the screen - <field>:day must be a number between 1 and 31. |
| Messages | Year must be supplied.; must be 4 digit number.; Century is not valid.; Month must be supplied.; Month must be a number between 1 and 12.; Day must be supplied.; day must be a number between 1 and 31. |
| Implemented at | COACTUPC 1200-EDIT-MAP-INPUTS `app/cbl/COACTUPC.cbl:1478-1507` |
| Implemented at | COACTUPC 1200-EDIT-MAP-INPUTS `app/cbl/COACTUPC.cbl:1533-1538` |
| Implemented at | COACTUPC EDIT-YEAR-CCYY, EDIT-MONTH, EDIT-DAY `app/cpy/CSUTLDPY.cpy:25-205` |
| Implemented at | COACTUPC  `app/cpy/CSUTLDWY.cpy:9-32` |
| Batch review | confirmed: Confirmed in EDIT-YEAR-CCYY, EDIT-MONTH and EDIT-DAY; applied to open, expiry, reissue dates and date of birth (app/cbl/COACTUPC.cbl:1478-1538). A failing year does not stop the month and day edits because each GO TO targets that paragraph's own exit and control falls through to the next paragraph. (`app/cpy/CSUTLDPY.cpy:25-205`, anchor `IF THIS-CENTURY OR LAST-CENTURY`) |

### BR-BASE-COACTUPC-006

Day 31 is rejected outside months 1, 3, 5, 7, 8, 10 and 12. Day 30 is rejected in February. Day 29 in February is accepted only in a leap year: a year ending in 00 must divide by 400, any other year by 4.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | WS-EDIT-DATE-DD = 31 and month not a 31-day month ; WS-EDIT-DATE-DD = 30 and month = 2 ; WS-EDIT-DATE-DD = 29 and month = 2 and CCYY not divisible by 400 (YY = 00) or by 4 |
| Outcome | set INPUT-ERROR and redisplay the screen - <field>:Cannot have 31 days in this month.; set INPUT-ERROR and redisplay the screen - <field>:Cannot have 30 days in this month.; set INPUT-ERROR and redisplay the screen - <field>:Not a leap year.Cannot have 29 days in this month. |
| Messages | Cannot have 31 days in this month.; Cannot have 30 days in this month.; Not a leap year.Cannot have 29 days in this month. |
| Implemented at | COACTUPC EDIT-DAY-MONTH-YEAR `app/cpy/CSUTLDPY.cpy:209-272` |
| Implemented at | COACTUPC  `app/cpy/CSUTLDWY.cpy:21-32` |
| Batch review | confirmed: Confirmed in EDIT-DAY-MONTH-YEAR: day 31 outside WS-31-DAY-MONTH, day 30 in February, and day 29 in February unless the year divides by 400 (YY = 00) or by 4 are rejected. Range tightened from 209-272 to the IF blocks. (`app/cpy/CSUTLDPY.cpy:213-272`, anchor `IF WS-FEBRUARY AND WS-DAY-29`) |

### BR-BASE-COACTUPC-007

A date that passes the year, month and day edits is checked again by CALL CSUTLDTC with format YYYYMMDD. A non-zero severity rejects the date.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | WS-SEVERITY-N not 0 |
| Outcome | set INPUT-ERROR and redisplay the screen - <field> validation error Sev code: <sev> Message code: <msg> |
| Messages | validation error Sev code: ... Message code: ... |
| Implemented at | COACTUPC EDIT-DATE-LE `app/cpy/CSUTLDPY.cpy:273-321` |
| Batch review | confirmed: Confirmed: CALL 'CSUTLDTC' with format 'YYYYMMDD'; WS-SEVERITY-N not 0 sets INPUT-ERROR and '<field> validation error Sev code: ...'. Range corrected from 273-321 to the EDIT-DATE-LE paragraph. Caveat: the failure GO TO EDIT-DATE-LE-EXIT falls into SET WS-EDIT-DATE-IS-VALID (CSUTLDPY.cpy:327), so the field flags end up valid although INPUT-ERROR stays set (see observations). (`app/cpy/CSUTLDPY.cpy:283-321`, anchor `CALL 'CSUTLDTC'`) |

### BR-BASE-COACTUPC-008

A date of birth that passes the date edits must be earlier than the current date. A date equal to today is rejected.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | INTEGER-OF-DATE(current date) not > INTEGER-OF-DATE(date of birth) |
| Outcome | set INPUT-ERROR and redisplay the screen - <field>:cannot be in the future |
| Messages | cannot be in the future |
| Implemented at | COACTUPC 1200-EDIT-MAP-INPUTS `app/cbl/COACTUPC.cbl:1533-1543` |
| Implemented at | COACTUPC EDIT-DATE-OF-BIRTH `app/cpy/CSUTLDPY.cpy:341-368` |
| Batch review | confirmed: Confirmed: only when the current date is strictly greater than the date of birth is it accepted; equal or later gives '<field>:cannot be in the future '. Invoked only when the date flags are valid (app/cbl/COACTUPC.cbl:1539-1543). (`app/cpy/CSUTLDPY.cpy:341-368`, anchor `IF WS-CURRENT-DATE-BINARY > WS-EDIT-DATE-BINARY`) |

### BR-BASE-COACTUPC-009

The SSN is entered in three parts of 3, 2 and 4 digits. Each part is required, must be numeric and must not be zero. The first part must also not be 000, 666 or 900 through 999.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | ACUP-NEW-CUST-SSN-1/2/3 blank, not numeric, or zero ; ACUP-NEW-CUST-SSN-1 in 0, 666, 900 thru 999 |
| Outcome | set INPUT-ERROR and redisplay the screen - SSN: First 3 chars: should not be 000, 666, or between 900 and 999 |
| Messages | must be supplied.; must be all numeric.; must not be zero.; : should not be 000, 666, or between 900 and 999 |
| Implemented at | COACTUPC 1265-EDIT-US-SSN `app/cbl/COACTUPC.cbl:2431-2487` |
| Implemented at | COACTUPC  `app/cbl/COACTUPC.cbl:121-123` |
| Implemented at | COACTUPC 1245-EDIT-NUM-REQD `app/cbl/COACTUPC.cbl:2109-2174` |
| Batch review | confirmed: Confirmed: parts of 3, 2 and 4 digits each go through 1245-EDIT-NUM-REQD (required, numeric, non-zero); part 1 is also rejected for 0, 666 or 900-999 (88 at 121-123). Part 2 and part 3 have no further check beyond non-zero. (`app/cbl/COACTUPC.cbl:2431-2488`, anchor `IF INVALID-SSN-PART1`) |

### BR-BASE-COACTUPC-010

The FICO score is required, must be a 3-digit non-zero number, and must be 300 through 850.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | FICO score blank, not numeric, or zero ; FICO score not 300 thru 850 |
| Outcome | set INPUT-ERROR and redisplay the screen - FICO Score: should be between 300 and 850 |
| Messages | : should be between 300 and 850 |
| Implemented at | COACTUPC 1200-EDIT-MAP-INPUTS `app/cbl/COACTUPC.cbl:1545-1557` |
| Implemented at | COACTUPC 1275-EDIT-FICO-SCORE `app/cbl/COACTUPC.cbl:2514-2529` |
| Implemented at | COACTUPC  `app/cbl/COACTUPC.cbl:848-849` |
| Batch review | confirmed: Confirmed: FICO is first edited as a required 3-character non-zero number (1545-1552); only then (guard at 1553) the 300-850 range of the 88 at 848-849 is applied with ': should be between 300 and 850'. (`app/cbl/COACTUPC.cbl:2514-2530`, anchor `IF FICO-RANGE-IS-VALID`) |

### BR-BASE-COACTUPC-011

First Name and Last Name are required and may contain only letters and spaces, within 25 characters. Middle Name is optional, but when supplied it may contain only letters and spaces.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | first or last name blank ; name contains a character other than a letter or space |
| Outcome | set INPUT-ERROR and redisplay the screen - <field> must be supplied.; set INPUT-ERROR and redisplay the screen - <field> can have alphabets only. |
| Messages | <field> must be supplied.; <field> can have alphabets only. |
| Implemented at | COACTUPC 1200-EDIT-MAP-INPUTS `app/cbl/COACTUPC.cbl:1560-1582` |
| Implemented at | COACTUPC 1225-EDIT-ALPHA-REQD `app/cbl/COACTUPC.cbl:1898-1949` |
| Implemented at | COACTUPC 1235-EDIT-ALPHA-OPT `app/cbl/COACTUPC.cbl:2012-2055` |
| Batch review | confirmed: Confirmed: first and last names use 1225-EDIT-ALPHA-REQD with length 25 (1560-1582); the INSPECT converts A-Z and a-z to spaces, so letters and embedded spaces are allowed. Middle name uses the optional variant 1235-EDIT-ALPHA-OPT (2012-2056). (`app/cbl/COACTUPC.cbl:1898-1950`, anchor `' can have alphabets only.'`) |

### BR-BASE-COACTUPC-012

Address Line 1 is required. City (address line 3) and Country are required and letters-and-spaces only. State is required, letters only, and must be one of 56 US state and territory codes. Address Line 2 is not edited.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | Address Line 1, City, Country, State blank ; City, Country, State not letters and spaces ; State not VALID-US-STATE-CODE |
| Outcome | set INPUT-ERROR and redisplay the screen - <field> must be supplied.; set INPUT-ERROR and redisplay the screen - <field> can have alphabets only.; set INPUT-ERROR and redisplay the screen - State: is not a valid state code |
| Messages | <field> must be supplied.; <field> can have alphabets only.; : is not a valid state code |
| Implemented at | COACTUPC 1200-EDIT-MAP-INPUTS `app/cbl/COACTUPC.cbl:1584-1602` |
| Implemented at | COACTUPC 1200-EDIT-MAP-INPUTS `app/cbl/COACTUPC.cbl:1613-1630` |
| Implemented at | COACTUPC 1215-EDIT-MANDATORY `app/cbl/COACTUPC.cbl:1824-1850` |
| Implemented at | COACTUPC 1270-EDIT-US-STATE-CD `app/cbl/COACTUPC.cbl:2493-2509` |
| Implemented at | COACTUPC  `app/cpy/CSLKPCDY.cpy:1013-1069` |
| Batch review | confirmed: Confirmed: Address Line 1 required (1583-1590), state alpha-only then one of 56 codes (CSLKPCDY.cpy:1013-1069; the list is upper case, so lower-case input is rejected), city and country required alpha-only (1614-1630), Address Line 2 unedited (comment at 1613). The country field is protected on screen (3546-3547), so the user cannot normally change it. (`app/cbl/COACTUPC.cbl:2493-2510`, anchor `IF VALID-US-STATE-CODE`) |

### BR-BASE-COACTUPC-013

Zip is required, must be a 5-digit number and must not be zero. When State and Zip each pass, the state code plus the first two zip digits must be one of 240 listed combinations.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | Zip blank, not numeric, or zero ; state code + zip(1:2) not VALID-US-STATE-ZIP-CD2-COMBO |
| Outcome | set INPUT-ERROR and redisplay the screen - Invalid zip code for state |
| Messages | must be supplied.; must be all numeric.; must not be zero.; Invalid zip code for state |
| Implemented at | COACTUPC 1200-EDIT-MAP-INPUTS `app/cbl/COACTUPC.cbl:1605-1611` |
| Implemented at | COACTUPC 1200-EDIT-MAP-INPUTS `app/cbl/COACTUPC.cbl:1665-1669` |
| Implemented at | COACTUPC 1280-EDIT-US-STATE-ZIP-CD `app/cbl/COACTUPC.cbl:2536-2556` |
| Implemented at | COACTUPC  `app/cpy/CSLKPCDY.cpy:1073-1313` |
| Batch review | confirmed: Confirmed: zip is a required 5-character non-zero number (1604-1611); the cross edit runs only when both state and zip flags are valid (1665-1669) and checks state + first two zip digits against the 240 values at CSLKPCDY.cpy:1074-1313. Failure marks both state and zip in error with 'Invalid zip code for state'. (`app/cbl/COACTUPC.cbl:2536-2557`, anchor `IF VALID-US-STATE-ZIP-CD2-COMBO`) |

### BR-BASE-COACTUPC-014

Phone Number 1 and 2 are optional. When a number is entered, the area code must be a 3-digit non-zero number in the list of 410 North American general purpose area codes, the prefix must be a 3-digit non-zero number, and the line number must be a 4-digit non-zero number.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | area code blank, not numeric, zero, or not VALID-GENERAL-PURP-CODE ; prefix blank, not numeric, or zero ; line number blank, not numeric, or zero |
| Outcome | set INPUT-ERROR and redisplay the screen - : Area code must be supplied.; set INPUT-ERROR and redisplay the screen - : Not valid North America general purpose area code; set INPUT-ERROR and redisplay the screen - : Prefix code must be A 3 digit number.; set INPUT-ERROR and redisplay the screen - : Line number code cannot be zero |
| Messages | : Area code must be supplied.; : Area code must be A 3 digit number.; : Area code cannot be zero; : Not valid North America general purpose area code; : Prefix code must be supplied.; : Prefix code must be A 3 digit number.; : Prefix code cannot be zero; : Line number code must be supplied.; : Line number code must be A 4 digit number.; : Line number code cannot be zero |
| Implemented at | COACTUPC 1200-EDIT-MAP-INPUTS `app/cbl/COACTUPC.cbl:1632-1646` |
| Implemented at | COACTUPC 1260-EDIT-US-PHONE-NUM `app/cbl/COACTUPC.cbl:2225-2423` |
| Implemented at | COACTUPC  `app/cpy/CSLKPCDY.cpy:521-930` |
| Batch review | corrected: Corrected: the area code, prefix and line-number checks are as stated (410 codes at CSLKPCDY.cpy:521-930), but the 'phone not entered' test at app/cbl/COACTUPC.cbl:2234-2239 checks WS-EDIT-US-PHONE-NUMA EQUAL SPACES where NUMC is expected. As coded, a number whose area code and prefix are blank (spaces) is accepted as not entered even when a line number is keyed, so 'when a number is entered' is not fully enforced. (`app/cbl/COACTUPC.cbl:2225-2423`, anchor `IF VALID-GENERAL-PURP-CODE`) |

### BR-BASE-COACTUPC-015

EFT Account Id is required, must be a 10-digit number and must not be zero.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | EFT Account Id blank, not numeric, or zero |
| Outcome | set INPUT-ERROR and redisplay the screen - <field> must be supplied.; set INPUT-ERROR and redisplay the screen - <field> must be all numeric.; set INPUT-ERROR and redisplay the screen - <field> must not be zero. |
| Messages | <field> must be supplied.; <field> must be all numeric.; <field> must not be zero. |
| Implemented at | COACTUPC 1200-EDIT-MAP-INPUTS `app/cbl/COACTUPC.cbl:1648-1655` |
| Implemented at | COACTUPC 1245-EDIT-NUM-REQD `app/cbl/COACTUPC.cbl:2109-2174` |
| Batch review | confirmed: Confirmed: EFT Account Id is edited by 1245-EDIT-NUM-REQD with length 10 (1648-1655): required, all numeric, not zero. (`app/cbl/COACTUPC.cbl:2109-2175`, anchor `' must not be zero.'`) |

### BR-COACTUPC-001

Only Enter, PF3, PF5 (only while validated changes await confirmation) and PF12 (only after account details have been fetched) are accepted; any other key, or PF5/PF12 outside those states, is processed as Enter.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | CCARD-AID mapped from EIBAID; ACUP-CHANGE-ACTION state |
| Outcome | PFK-INVALID forces CCARD-AID-ENTER |
| Implemented at | COACTUPC 0000-MAIN `app/cbl/COACTUPC.cbl:905-916` |
| Implemented at | COACTUPC  `app/cpy/CSSTRPFY.cpy:21-78` |
| Anchor (verified) | `(CCARD-AID-PFK05 AND ACUP-CHANGES-OK-NOT-CONFIRMED)` |

### BR-COACTUPC-002

PF3 ends the update dialog: the program takes a SYNCPOINT and transfers control (XCTL) to CDEMO-FROM-PROGRAM with CDEMO-FROM-TRANID, or to COMEN01C / CM00 when the caller fields are blank, recording CAUP/COACTUPC as the new caller.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | CCARD-AID-PFK03 |
| Outcome | SYNCPOINT, XCTL PROGRAM(CDEMO-TO-PROGRAM) COMMAREA(CARDDEMO-COMMAREA); CDEMO-USRTYP-USER and CDEMO-PGM-ENTER set |
| Implemented at | COACTUPC 0000-MAIN `app/cbl/COACTUPC.cbl:921-959` |
| Anchor (verified) | `WHEN CCARD-AID-PFK03` |

### BR-COACTUPC-003

On the interaction after an update finished (state 'C') or failed (state 'L' lock error or 'F' update failed), the program clears its program area, working storage and CDEMO-ACCT-ID and shows the empty search screen again, so a new account must be entered.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | ACUP-CHANGES-OKAYED-AND-DONE or ACUP-CHANGES-FAILED at task start |
| Outcome | INITIALIZE WS-THIS-PROGCOMMAREA WS-MISC-STORAGE CDEMO-ACCT-ID; 3000-SEND-MAP; ACUP-DETAILS-NOT-FETCHED |
| Implemented at | COACTUPC 0000-MAIN `app/cbl/COACTUPC.cbl:979-989` |
| Anchor (verified) | `WHEN ACUP-CHANGES-FAILED` |

### BR-COACTUPC-004

An input field keyed as '*' or left as spaces is treated as not supplied and stored as LOW-VALUES; until an account has been fetched, only the account number is taken from the screen.

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | <field>I OF CACTUPAI = '*' OR SPACES |
| Outcome | LOW-VALUES moved to the ACUP-NEW-* field (and CC-ACCT-ID for the account id); required-field edits later report it as not supplied |
| Implemented at | COACTUPC 1100-RECEIVE-MAP `app/cbl/COACTUPC.cbl:1051-1062` |
| Implemented at | COACTUPC  `app/cbl/COACTUPC.cbl:1064-1423` |
| Anchor (verified) | `IF ACUP-DETAILS-NOT-FETCHED GO TO 1100-RECEIVE-MAP-EXIT` |

### BR-COACTUPC-005

Credit limit, cash credit limit, current balance, current cycle credit and current cycle debit may be keyed in currency format; when FUNCTION TEST-NUMVAL-C accepts the text, FUNCTION NUMVAL-C converts it into the signed 10.2 numeric field used for display and for the rewrite.

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | TEST-NUMVAL-C(<amount text>) = 0 |
| Outcome | COMPUTE ACUP-NEW-<amount>-N = FUNCTION NUMVAL-C(<input>) |
| Implemented at | COACTUPC 1100-RECEIVE-MAP `app/cbl/COACTUPC.cbl:1072-1084` |
| Implemented at | COACTUPC  `app/cbl/COACTUPC.cbl:1086-1140` |
| Anchor (verified) | `IF FUNCTION TEST-NUMVAL-C(ACUP-NEW-CREDIT-LIMIT-X) = 0` |

### BR-COACTUPC-006

Until an account has been fetched, only the account number is edited and no other field edit runs; a blank account number ends with the message 'No input received'.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | ACUP-DETAILS-NOT-FETCHED |
| Outcome | 1210-EDIT-ACCOUNT then GO TO 1200-EDIT-MAP-INPUTS-EXIT |
| Messages | No input received |
| Implemented at | COACTUPC 1200-EDIT-MAP-INPUTS `app/cbl/COACTUPC.cbl:1433-1448` |
| Anchor (verified) | `SET NO-SEARCH-CRITERIA-RECEIVED TO TRUE` |

### BR-COACTUPC-007

Field edits are skipped and all edit flags cleared when nothing changed, when the changes were already validated and await PF5 confirmation, or when they were already committed; values validated once are not edited again on the confirming key press.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | NO-CHANGES-FOUND OR ACUP-CHANGES-OK-NOT-CONFIRMED OR ACUP-CHANGES-OKAYED-AND-DONE |
| Outcome | WS-NON-KEY-FLAGS = LOW-VALUES; exit without editing |
| Implemented at | COACTUPC 1200-EDIT-MAP-INPUTS `app/cbl/COACTUPC.cbl:1463-1468` |
| Anchor (verified) | `MOVE LOW-VALUES TO WS-NON-KEY-FLAGS` |

### BR-COACTUPC-008

When no account is shown yet, or the user presses PF12, the program re-reads the account (cross-reference, account and customer) for a valid account number and shows the stored values; PF12 therefore discards any unsaved changes.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | (ACUP-DETAILS-NOT-FETCHED or CCARD-AID-PFK12) and FLG-ACCTFILTER-ISVALID |
| Outcome | 9000-READ-ACCT; ACUP-SHOW-DETAILS when FOUND-CUST-IN-MASTER |
| Implemented at | COACTUPC 2000-DECIDE-ACTION `app/cbl/COACTUPC.cbl:2563-2580` |
| Anchor (verified) | `WHEN CCARD-AID-PFK12` |

### BR-COACTUPC-009

While details are shown, input with edit errors or with no change stays on the change screen without any update; only error-free changed input moves to the 'awaiting confirmation' state.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | ACUP-SHOW-DETAILS or ACUP-CHANGES-NOT-OK |
| Outcome | ACUP-CHANGES-OK-NOT-CONFIRMED only when no INPUT-ERROR and a change exists |
| Implemented at | COACTUPC 2000-DECIDE-ACTION `app/cbl/COACTUPC.cbl:2585-2597` |
| Anchor (verified) | `IF INPUT-ERROR OR NO-CHANGES-DETECTED` |

### BR-COACTUPC-010

The account and customer are written only when the user presses PF5 while validated changes await confirmation. The outcome sets the next state: account lock failure gives 'L', a failed rewrite gives 'F', a concurrent change returns to showing details, and any other outcome is treated as success 'C'. Without PF5 the confirmation screen is shown again.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | ACUP-CHANGES-OK-NOT-CONFIRMED AND CCARD-AID-PFK05 |
| Outcome | 9600-WRITE-PROCESSING; ACUP-CHANGES-OKAYED-LOCK-ERROR / ACUP-CHANGES-OKAYED-BUT-FAILED / ACUP-SHOW-DETAILS / ACUP-CHANGES-OKAYED-AND-DONE |
| Messages | Changes committed to database; Changes unsuccessful. Please try again |
| Implemented at | COACTUPC 2000-DECIDE-ACTION `app/cbl/COACTUPC.cbl:2602-2621` |
| Anchor (verified) | `WHEN COULD-NOT-LOCK-ACCT-FOR-UPDATE` |

### BR-COACTUPC-011

A change-action state not handled by 2000-DECIDE-ACTION abends the task: ABEND-CODE '0001', message 'UNEXPECTED DATA SCENARIO', the abend data is sent to the terminal and the task abends with code 9999. Any other CICS abend is routed to the same routine with 'UNEXPECTED ABEND OCCURRED.'.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | WHEN OTHER in the action EVALUATE, or any abend after HANDLE ABEND |
| Outcome | EXEC CICS SEND FROM(ABEND-DATA); EXEC CICS ABEND ABCODE('9999') |
| Messages | UNEXPECTED DATA SCENARIO; UNEXPECTED ABEND OCCURRED. |
| Implemented at | COACTUPC 2000-DECIDE-ACTION `app/cbl/COACTUPC.cbl:2633-2640` |
| Implemented at | COACTUPC  `app/cbl/COACTUPC.cbl:4203-4224` |
| Implemented at | COACTUPC  `app/cbl/COACTUPC.cbl:861-863` |
| Anchor (verified) | `MOVE 'UNEXPECTED DATA SCENARIO'` |

### BR-COACTUPC-012

Fields are editable only while details are shown or after edit errors; before fetch only the account number is editable, and during confirmation and after commit everything is protected. The customer id and the country code are always protected, so they cannot be changed from this screen.

| Item | Value |
|---|---|
| Category | data-integrity |
| Confidence | Confirmed |
| Conditions | ACUP-CHANGE-ACTION state |
| Outcome | DFHBMFSE on editable fields; DFHBMPRF on ACSTNUMA and ACSCTRYA |
| Implemented at | COACTUPC 3300-SETUP-SCREEN-ATTRS `app/cbl/COACTUPC.cbl:2993-3005` |
| Implemented at | COACTUPC  `app/cbl/COACTUPC.cbl:3530-3547` |
| Anchor (verified) | `PERFORM 3320-UNPROTECT-FEW-ATTRS` |

### BR-COACTUPC-013

Account details are fetched in sequence: card cross-reference by account id, then the account master, then the customer master using the customer id from the cross-reference; a missing cross-reference stops the fetch before the account is read.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | FLG-ACCTFILTER-NOT-OK after 9200; DID-NOT-FIND-* message conditions after 9300 and 9400 |
| Outcome | GO TO 9000-READ-ACCT-EXIT on failure; otherwise 9500-STORE-FETCHED-DATA |
| Implemented at | COACTUPC 9000-READ-ACCT `app/cbl/COACTUPC.cbl:3620-3638` |
| Implemented at | COACTUPC  `app/cbl/COACTUPC.cbl:3664-3667` |
| Anchor (verified) | `IF FLG-ACCTFILTER-NOT-OK` |

### BR-COACTUPC-014

A NOTFND on the cross-reference, account or customer read is an input error: the account (or customer) filter is flagged and a message naming the key, file, RESP and RESP2 is shown; any other response shows 'File Error: READ on <file> returned RESP ..,RESP2 ..'.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | WS-RESP-CD NOTFND or OTHER after EXEC CICS READ |
| Outcome | INPUT-ERROR, FLG-ACCTFILTER-NOT-OK or FLG-CUSTFILTER-NOT-OK, WS-RETURN-MSG |
| Messages | not found in Cross ref file.  Resp:;  not found in Acct Master file.Resp:;  in customer master.Resp: |
| Implemented at | COACTUPC 9200-GETCARDXREF-BYACCT `app/cbl/COACTUPC.cbl:3664-3695` |
| Implemented at | COACTUPC  `app/cbl/COACTUPC.cbl:3713-3746` |
| Implemented at | COACTUPC  `app/cbl/COACTUPC.cbl:3762-3794` |
| Anchor (verified) | `WHEN DFHRESP(NOTFND)` |

### BR-COACTUPC-015

Optimistic concurrency check: after reading both records for update, every stored account and customer value is compared with the value captured when the screen was filled; any difference cancels the save with 'Record changed by some one else. Please review'. Group id is compared case-insensitively (lower case), customer text fields upper-cased.

| Item | Value |
|---|---|
| Category | data-integrity |
| Confidence | Confirmed |
| Conditions | Any field of ACCOUNT-RECORD/CUSTOMER-RECORD differs from ACUP-OLD-DETAILS |
| Outcome | DATA-WAS-CHANGED-BEFORE-UPDATE; no REWRITE; 2000-DECIDE-ACTION returns to ACUP-SHOW-DETAILS |
| Messages | Record changed by some one else. Please review |
| Implemented at | COACTUPC 9700-CHECK-CHANGE-IN-REC `app/cbl/COACTUPC.cbl:4114-4145` |
| Implemented at | COACTUPC  `app/cbl/COACTUPC.cbl:4152-4191` |
| Implemented at | COACTUPC  `app/cbl/COACTUPC.cbl:3946-3952` |
| Anchor (verified) | `SET DATA-WAS-CHANGED-BEFORE-UPDATE TO TRUE` |

### BR-COACTUPC-016

Before updating, the account record and then the customer record are read with UPDATE (locked); if either read fails the save is abandoned with 'Could not lock account record for update' or 'Could not lock customer record for update'.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | WS-RESP-CD not NORMAL on READ ... UPDATE |
| Outcome | INPUT-ERROR; message (when none set yet); GO TO 9600-WRITE-PROCESSING-EXIT |
| Messages | Could not lock account record for update; Could not lock customer record for update |
| Implemented at | COACTUPC 9600-WRITE-PROCESSING `app/cbl/COACTUPC.cbl:3894-3915` |
| Implemented at | COACTUPC  `app/cbl/COACTUPC.cbl:3921-3942` |
| Anchor (verified) | `SET COULD-NOT-LOCK-ACCT-FOR-UPDATE TO TRUE` |

### BR-COACTUPC-017

The account record is rewritten first and then the customer record; a failed account rewrite stops with 'Update of record failed', and a failed customer rewrite sets the same message and issues SYNCPOINT ROLLBACK so the account rewrite is backed out.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | WS-RESP-CD not NORMAL after REWRITE ACCTDAT / CUSTDAT |
| Outcome | LOCKED-BUT-UPDATE-FAILED; ROLLBACK on customer failure |
| Messages | Update of record failed |
| Implemented at | COACTUPC 9600-WRITE-PROCESSING `app/cbl/COACTUPC.cbl:4064-4103` |
| Anchor (verified) | `SYNCPOINT ROLLBACK` |

### BR-COACTUPC-018

On save, open, expiry, reissue and birth dates are stored as YYYY-MM-DD built from the keyed parts, and each phone number is stored as (AAA)BBB-CCCC from its three parts; amounts are taken from the NUMVAL-C converted fields and the SSN from the 9-digit concatenation of its parts.

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | Save after confirmation |
| Outcome | ACCT-UPDATE-*-DATE, CUST-UPDATE-PHONE-NUM-1/2, CUST-UPDATE-DOB-YYYY-MM-DD, CUST-UPDATE-SSN populated |
| Implemented at | COACTUPC 9600-WRITE-PROCESSING `app/cbl/COACTUPC.cbl:3976-4000` |
| Implemented at | COACTUPC  `app/cbl/COACTUPC.cbl:4027-4041` |
| Implemented at | COACTUPC  `app/cbl/COACTUPC.cbl:4043-4052` |
| Implemented at | COACTUPC  `app/cbl/COACTUPC.cbl:3963-3974` |
| Anchor (verified) | `STRING ACUP-NEW-OPEN-YEAR` |

### BR-COACTUPC-019

PF13 through PF24 are treated as PF1 through PF12 (for example PF15 acts as PF3 and PF17 as PF5); Enter, Clear, PA1 and PA2 are recorded as such.

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | EIBAID = DFHPF13 .. DFHPF24 |
| Outcome | CCARD-AID-PFK01 .. CCARD-AID-PFK12 set |
| Implemented at | COACTUPC YYYY-STORE-PFKEY `app/cpy/CSSTRPFY.cpy:54-77` |
| Anchor (verified) | `WHEN EIBAID IS EQUAL TO DFHPF13 SET CCARD-AID-PFK01 TO TRUE` |

### BR-COACTUPC-020

A first entry (no commarea, or arrival from the main menu COMEN01C that is not a re-entry) starts a fresh dialog: commarea and program state are initialized and the empty search screen prompting for the account id is sent.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | EIBCALEN = 0, or CDEMO-FROM-PROGRAM = 'COMEN01C' and not CDEMO-PGM-REENTER, or ACUP-DETAILS-NOT-FETCHED with CDEMO-PGM-ENTER |
| Outcome | INITIALIZE; 3000-SEND-MAP; CDEMO-PGM-REENTER; ACUP-DETAILS-NOT-FETCHED |
| Messages | Enter or update id of account to update |
| Implemented at | COACTUPC 0000-MAIN `app/cbl/COACTUPC.cbl:964-973` |
| Implemented at | COACTUPC  `app/cbl/COACTUPC.cbl:880-892` |
| Anchor (verified) | `WHEN CDEMO-FROM-PROGRAM EQUAL LIT-MENUPGM AND NOT CDEMO-PGM-REENTER` |


## COACTVWC

Program page: [COACTVWC](07-programs/COACTVWC.md).

### BR-BASE-COACTVWC-001

An account-view filter of low-values or spaces is reported as not provided, and the message becomes No input received. A supplied account number that is not numeric or is zeros is rejected. An asterisk or spaces on the screen field is treated as not supplied.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | CC-ACCT-ID = low-values or spaces ; CC-ACCT-ID is not numeric, or = zeros |
| Outcome | set INPUT-ERROR and redisplay the screen - No input received; set INPUT-ERROR and redisplay the screen - Account Filter must  be a non-zero 11 digit number |
| Messages | Account number not provided; No input received; Account Filter must  be a non-zero 11 digit number |
| Implemented at | COACTVWC 2200-EDIT-MAP-INPUTS `app/cbl/COACTVWC.cbl:627-642` |
| Implemented at | COACTVWC 2210-EDIT-ACCOUNT `app/cbl/COACTVWC.cbl:649-680` |
| Implemented at | COACTVWC  `app/cbl/COACTVWC.cbl:121-124` |
| Batch review | confirmed: Confirmed: '*' or spaces -> low-values (628-633); blank -> FLG-ACCTFILTER-BLANK with 'Account number not provided' (653-661) then overwritten by 'No input received' (640-642); non-numeric or zero -> 'Account Filter must  be a non-zero 11 digit number' (666-676). Because CC-ACCT-ID is PIC X(11), an id with fewer than 11 digits (trailing spaces) fails the NUMERIC test. The 88-levels at 121-128 (SEARCHED-ACCT-ZEROES etc.) are not the literal actually used. (`app/cbl/COACTVWC.cbl:627-680`, anchor `IF ACCTSIDI OF CACTVWAI = '*'`) |

### BR-COACTVWC-001

PF3 on the account view returns to the program and transaction that invoked it (CDEMO-FROM-PROGRAM / CDEMO-FROM-TRANID); when these are blank or low-values the main menu COMEN01C / CM00 is used. Before the XCTL the commarea is stamped with from-transaction CAVW and from-program COACTVWC, user type is forced to 'U' (CDEMO-USRTYP-USER), program context to first-entry and last map/mapset to CACTVWA/COACTVW.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | CCARD-AID-PFK03 (PF3 or PF15) |
| Outcome | XCTL to CDEMO-TO-PROGRAM with CARDDEMO-COMMAREA |
| Implemented at | COACTVWC 0000-MAIN `app/cbl/COACTVWC.cbl:324-352` |
| Anchor (verified) | `MOVE LIT-MENUPGM TO CDEMO-TO-PROGRAM` |

### BR-COACTVWC-002

Only ENTER and PF3 are meaningful on the account view; any other attention key (including PF keys, CLEAR, PA1/PA2) is silently treated as ENTER. PF13-PF24 are folded onto PF1-PF12, so PF15 also exits.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | AID not ENTER and not PF3 |
| Outcome | Processed as ENTER |
| Implemented at | COACTVWC 0000-MAIN `app/cbl/COACTVWC.cbl:306-314` |
| Implemented at | COACTVWC  `app/cpy/CSSTRPFY.cpy:58-59` |
| Anchor (verified) | `SET CCARD-AID-ENTER TO TRUE` |

### BR-COACTVWC-003

On first entry (CDEMO-PGM-ENTER) the account view only displays the empty search screen; on re-entry it edits the input and, only when the input is valid, reads the account data before redisplaying. When the program is entered from COMEN01C without the re-enter flag (or with no commarea) the shared commarea is re-initialised.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | CDEMO-PGM-ENTER / CDEMO-PGM-REENTER and INPUT-ERROR |
| Outcome | Screen sent; account lookup only after successful edit |
| Implemented at | COACTVWC 0000-MAIN `app/cbl/COACTVWC.cbl:353-374` |
| Implemented at | COACTVWC  `app/cbl/COACTVWC.cbl:282-292` |
| Anchor (verified) | `PERFORM 9000-READ-ACCT` |

### BR-COACTVWC-004

If the program context is neither first-entry nor re-entry (and PF3 not pressed), the account view ends the conversation by sending the plain-text message 'UNEXPECTED DATA SCENARIO' and returning to CICS without a next transaction (abend code '0001' is prepared but no abend is issued).

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | EVALUATE TRUE reaches WHEN OTHER |
| Outcome | SEND TEXT + RETURN (session ends) |
| Messages | UNEXPECTED DATA SCENARIO |
| Implemented at | COACTVWC 0000-MAIN `app/cbl/COACTVWC.cbl:375-382` |
| Anchor (verified) | `MOVE 'UNEXPECTED DATA SCENARIO'` |

### BR-COACTVWC-005

An account is looked up in three steps: the card cross-reference via the account alternate index CXACAIX gives the customer id and a card number; then the account master ACCTDAT is read by account id; then the customer master CUSTDAT is read by the customer id obtained from the cross-reference. If the account is not in the cross-reference, the account and customer masters are not read.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | Valid account id entered |
| Outcome | ACCOUNT-RECORD and CUSTOMER-RECORD loaded; CDEMO-CUST-ID / CDEMO-CARD-NUM set from xref |
| Implemented at | COACTVWC 9000-READ-ACCT `app/cbl/COACTVWC.cbl:691-715` |
| Implemented at | COACTVWC  `app/cbl/COACTVWC.cbl:737-740` |
| Anchor (verified) | `MOVE CDEMO-CUST-ID TO WS-CARD-RID-CUST-ID` |

### BR-COACTVWC-006

An account id not present in the card cross-reference file is rejected with 'Account:<id> not found in Cross ref file.  Resp:<resp> Reas:<resp2>'; any other xref read failure is reported as 'File Error: READ on CXACAIX returned RESP ...'. Both set INPUT-ERROR and mark the account filter invalid (red).

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | CXACAIX READ RESP NOTFND or other non-NORMAL |
| Outcome | Error message displayed, no account data |
| Messages | Account:;  not found in;  Cross ref file.  Resp:; File Error: |
| Implemented at | COACTVWC 9200-GETCARDXREF-BYACCT `app/cbl/COACTVWC.cbl:741-768` |
| Anchor (verified) | `' Cross ref file.  Resp:'` |

### BR-COACTVWC-007

When the account master has no record for the account the screen shows 'Account:<id> not found in Acct Master file.Resp:...'; when the customer master has no record for the cross-referenced customer it shows 'CustId:<id> not found in customer master.Resp: ...'. Other read failures show the generic 'File Error: READ on <file> returned RESP ...' text. All set INPUT-ERROR.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | ACCTDAT or CUSTDAT READ RESP NOTFND / other |
| Outcome | Error message displayed |
| Messages | Acct Master file.Resp:;  in customer master.Resp: |
| Implemented at | COACTVWC 9300-GETACCTDATA-BYACCT `app/cbl/COACTVWC.cbl:785-819` |
| Implemented at | COACTVWC  `app/cbl/COACTVWC.cbl:836-868` |
| Anchor (verified) | `' Acct Master file.Resp:'` |

### BR-COACTVWC-008

Account financial and date fields are displayed when the account or customer record was found; customer fields are displayed only when the customer record was found, with the 9-digit SSN reformatted as NNN-NN-NNNN (full SSN, not masked).

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | FOUND-ACCT-IN-MASTER or FOUND-CUST-IN-MASTER; FOUND-CUST-IN-MASTER |
| Outcome | Screen fields ACSTTUSO..AADDGRPO, ACSTNUMO, ACSTSSNO etc. populated |
| Implemented at | COACTVWC 1200-SETUP-SCREEN-VARS `app/cbl/COACTVWC.cbl:471-504` |
| Anchor (verified) | `CUST-SSN(1:3)` |


## COADM01C

Program page: [COADM01C](07-programs/COADM01C.md).

### BR-BASE-001

When the return target is spaces or low-values, the user menu and the admin menu both set it to COSGN00C before the transfer.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | CDEMO-TO-PROGRAM = spaces or low-values |
| Outcome | XCTL |
| Implemented at | COMEN01C RETURN-TO-SIGNON-SCREEN `app/cbl/COMEN01C.cbl:198-200` |
| Implemented at | COADM01C RETURN-TO-SIGNON-SCREEN `app/cbl/COADM01C.cbl:165-167` |
| Batch review | confirmed: Confirmed for COMEN01C; the XCTL at 201-203 passes no commarea. The COADM01C half is reviewed in COADM01C.json. (`app/cbl/COMEN01C.cbl:198-200`, anchor `IF CDEMO-TO-PROGRAM = LOW-VALUES OR SPACES`) |

### BR-BASE-002

PF3 on the user menu and on the admin menu sets the return target to COSGN00C and returns to sign-on.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | EIBAID = DFHPF3 |
| Outcome | XCTL |
| Implemented at | COMEN01C  `app/cbl/COMEN01C.cbl:96-98` |
| Implemented at | COADM01C  `app/cbl/COADM01C.cbl:100-102` |
| Batch review | confirmed: PF3 sets CDEMO-TO-PROGRAM to 'COSGN00C' and performs RETURN-TO-SIGNON-SCREEN (XCTL without commarea). (`app/cbl/COMEN01C.cbl:96-98`, anchor `MOVE 'COSGN00C' TO CDEMO-TO-PROGRAM`) |

### BR-BASE-COADM01C-001

An admin-menu option is started when its program name does not begin with DUMMY.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | CDEMO-ADMIN-OPT-PGMNAME(WS-OPTION) does not start with DUMMY |
| Outcome | XCTL |
| Implemented at | COADM01C  `app/cbl/COADM01C.cbl:141-146` |
| Batch review | confirmed: Confirmed; range extended to END-IF at 149. Before XCTL it sets CDEMO-FROM-TRANID/PROGRAM and context 0. A DUMMY program falls through to the green 'This option is not installed ...' message (150-157), not a 'coming soon' message as in COMEN01C. No COADM02Y entry currently starts with DUMMY. (`app/cbl/COADM01C.cbl:141-149`, anchor `IF CDEMO-ADMIN-OPT-PGMNAME(WS-OPTION)(1:5) NOT = 'DUMMY'`) |

### BR-COADM01C-001

The admin menu option must be numeric, non-zero and not greater than CDEMO-ADMIN-OPT-COUNT (6 in COADM02Y); otherwise the menu is redisplayed with 'Please enter a valid option number...'. Trailing blanks are trimmed and remaining blanks replaced by zeros before the check.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | WS-OPTION NOT NUMERIC or > CDEMO-ADMIN-OPT-COUNT or = 0 |
| Outcome | Error flag set, menu redisplayed with message |
| Messages | Please enter a valid option number... |
| Implemented at | COADM01C PROCESS-ENTER-KEY `app/cbl/COADM01C.cbl:131-138` |
| Implemented at | COADM01C  `app/cbl/COADM01C.cbl:121-129` |
| Implemented at | COADM01C  `app/cpy/COADM02Y.cpy:22` |
| Anchor (verified) | `WS-OPTION > CDEMO-ADMIN-OPT-COUNT OR` |

### BR-COADM01C-002

When the program of a selected admin option is not defined to CICS (PGMIDERR on XCTL), the admin menu does not abend: it shows 'This option is not installed ...' in green, redisplays the menu and continues the conversation with transaction CA00.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | XCTL raises PGMIDERR |
| Outcome | Message displayed, RETURN TRANSID(CA00) |
| Messages | This option is not installed ... |
| Implemented at | COADM01C PGMIDERR-ERR-PARA `app/cbl/COADM01C.cbl:270-283` |
| Implemented at | COADM01C  `app/cbl/COADM01C.cbl:77-79` |
| Anchor (verified) | `'is not installed ...' DELIMITED BY SIZE` |

### BR-COADM01C-003

The admin menu distinguishes first entry from re-entry with CDEMO-PGM-CONTEXT: entered from another program it sets CDEMO-PGM-REENTER and only displays the menu; input is processed only on re-entry. A start without commarea is sent to sign-on COSGN00C. Any key other than ENTER or PF3 redisplays the menu with 'Invalid key pressed. Please see below...'.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | EIBCALEN = 0; CDEMO-PGM-REENTER; EIBAID |
| Outcome | Sign-on transfer, menu display, option processing or invalid-key message |
| Messages | Invalid key pressed. Please see below... |
| Implemented at | COADM01C MAIN-PARA `app/cbl/COADM01C.cbl:85-107` |
| Implemented at | COADM01C  `app/cpy/CSMSG01Y.cpy:20-21` |
| Anchor (verified) | `IF NOT CDEMO-PGM-REENTER` |


## COBDATFT

### BR-BASE-COBDATFT-001

Date input type 1 is rejected when character 5 of the input is a hyphen or the requested output type is 2. Otherwise hyphens are inserted after the year and after the month.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | COINTYPE = 1; COINPDT+4 = -; COOUTYPE = 2 |
| Outcome | move INVALID INPUT to COERMSG; insert hyphens into the output date |
| Messages | INVALID INPUT |
| Implemented at | COBDATFT  `app/asm/COBDATFT.asm:30-45` |
| Batch review | confirmed: VALIDIN1 rejects when COINPDT+4 (the fifth input character) equals '-' or COOUTYPE is '2' (lines 36-39), otherwise copies the year and inserts hyphens at COOUTDT+4 and COOUTDT+7 (lines 40-44). The rejection branches to GOTOERR (line 55), which leaves COOUTDT unchanged. (`app/asm/COBDATFT.asm:35-45`, anchor `VALIDIN1`) |

### BR-BASE-COBDATFT-002

Date input type 2 is rejected when the requested output type is 1. Otherwise characters are copied while skipping the hyphen positions. The hyphen-position check for type 2 is present only as a comment.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | COINTYPE = 2; COOUTYPE = 1 |
| Outcome | copy date characters skipping hyphen positions |
| Implemented at | COBDATFT  `app/asm/COBDATFT.asm:46-54` |
| Batch review | confirmed: VALIDIN2 rejects only when COOUTYPE is '1' (lines 49-50); the hyphen check is commented out (lines 47-48). Otherwise it copies input positions 0-3, 5-6 and 8-9 to the output (lines 51-53). The only caller, CBACT01C, passes type '2' with output type '2' (app/cbl/CBACT01C.cbl:225-231), which takes this path. (`app/asm/COBDATFT.asm:46-54`, anchor `VALIDIN2`) |

### BR-BASE-COBDATFT-003

A date input type other than 1 or 2 moves INVALID INPUT into the error message field.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | COINTYPE not 1 and not 2 |
| Outcome | move INVALID INPUT to COERMSG - INVALID INPUT |
| Messages | INVALID INPUT |
| Implemented at | COBDATFT  `app/asm/COBDATFT.asm:34-56` |
| Batch review | confirmed: A COINTYPE other than '1' or '2' falls through the CLI tests at lines 30-33 to B GOTOERR (line 34); GOTOERR moves 'INVALID INPUT' to COERMSG (lines 55-56). The cited range 34-56 in the legacy rule omits the type tests at lines 30-33; the review cites 30-56. (`app/asm/COBDATFT.asm:30-56`, anchor `GOTOERR`) |


## COBIL00C

Program page: [COBIL00C](07-programs/COBIL00C.md).

### BR-COBIL00C-001

On first entry, if the commarea carries a pre-selected value in CDEMO-CB00-TRN-SELECTED (not spaces and not low-values), it is used as the account id and processed immediately as if ENTER had been pressed (account read and balance shown with confirmation prompt).

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | First entry (not CDEMO-PGM-REENTER) and CDEMO-CB00-TRN-SELECTED not blank |
| Outcome | ACTIDINI pre-filled and PROCESS-ENTER-KEY performed |
| Implemented at | COBIL00C MAIN-PARA `app/cbl/COBIL00C.cbl:116-121` |
| Anchor (verified) | `MOVE CDEMO-CB00-TRN-SELECTED TO` |

### BR-COBIL00C-002

On the bill-payment screen PF3 returns to the program recorded in CDEMO-FROM-PROGRAM, or to the main menu COMEN01C when it is blank; PF4 clears the account, balance and confirmation fields; any other key except ENTER redisplays the screen with 'Invalid key pressed. Please see below...'.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | Re-entry with EIBAID = DFHPF3 / DFHPF4 / other |
| Outcome | XCTL to previous program / screen cleared / invalid-key message |
| Messages | Invalid key pressed. Please see below... |
| Implemented at | COBIL00C MAIN-PARA `app/cbl/COBIL00C.cbl:128-141` |
| Implemented at | COBIL00C  `app/cpy/CSMSG01Y.cpy:20-21` |
| Anchor (verified) | `MOVE 'COMEN01C' TO CDEMO-TO-PROGRAM` |

### BR-COBIL00C-003

The account id is mandatory for a bill payment: when ACTIDINI is spaces or low-values the screen is redisplayed with 'Acct ID can NOT be empty...' and nothing is read. No numeric or length check is made on the account id before it is moved to the numeric key ACCT-ID.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | ACTIDINI = SPACES or LOW-VALUES |
| Outcome | Error flag set, message displayed |
| Messages | Acct ID can NOT be empty... |
| Implemented at | COBIL00C PROCESS-ENTER-KEY `app/cbl/COBIL00C.cbl:158-167` |
| Anchor (verified) | `MOVE 'Acct ID can NOT be empty...' TO` |

### BR-COBIL00C-004

The confirmation field drives the payment: 'Y' or 'y' authorises the payment (account read for update and payment processed); 'N' or 'n' cancels and clears the screen; blank or low-values only looks up the account and shows its balance with the prompt 'Confirm to make a bill payment...'; any other value is rejected with 'Invalid value. Valid values are (Y/N)...'.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | CONFIRMI value |
| Outcome | Pay / cancel / show balance and prompt / reject |
| Messages | Invalid value. Valid values are (Y/N)...; Confirm to make a bill payment... |
| Implemented at | COBIL00C PROCESS-ENTER-KEY `app/cbl/COBIL00C.cbl:173-191` |
| Implemented at | COBIL00C  `app/cbl/COBIL00C.cbl:236-239` |
| Anchor (verified) | `MOVE 'Invalid value. Valid values are (Y/N)...'` |

### BR-COBIL00C-005

A bill payment is refused when the account's current balance is zero or negative: the screen shows 'You have nothing to pay...' and no transaction is written.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | ACCT-CURR-BAL <= 0 and account id present and no earlier error |
| Outcome | Error flag set, message displayed |
| Messages | You have nothing to pay... |
| Implemented at | COBIL00C PROCESS-ENTER-KEY `app/cbl/COBIL00C.cbl:197-205` |
| Anchor (verified) | `IF ACCT-CURR-BAL <= ZEROS AND` |

### BR-COBIL00C-006

The payment is executed only when the user confirmed with Y (CONF-PAY-YES) and no earlier error occurred; otherwise the balance is displayed with the prompt 'Confirm to make a bill payment...'.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | NOT ERR-FLG-ON and CONF-PAY-YES |
| Outcome | Payment transaction written and account updated, or confirmation prompt |
| Messages | Confirm to make a bill payment... |
| Implemented at | COBIL00C PROCESS-ENTER-KEY `app/cbl/COBIL00C.cbl:208-243` |
| Anchor (verified) | `IF CONF-PAY-YES` |

### BR-COBIL00C-007

The new transaction id is the highest existing TRAN-ID in TRANSACT plus 1: the program starts a browse at HIGH-VALUES, reads the previous (last) record, ends the browse and adds 1 to its id as a 16-digit number. If the file is empty (ENDFILE) the id starts from 0, giving 1.

| Item | Value |
|---|---|
| Category | calculation |
| Confidence | Confirmed |
| Conditions | Payment confirmed |
| Outcome | TRAN-ID = last TRAN-ID + 1 |
| Implemented at | COBIL00C PROCESS-ENTER-KEY `app/cbl/COBIL00C.cbl:212-219` |
| Implemented at | COBIL00C  `app/cbl/COBIL00C.cbl:483-488` |
| Anchor (verified) | `ADD 1 TO WS-TRAN-ID-NUM` |

### BR-COBIL00C-008

The bill-payment transaction record is built with type code '02', category code 2, source 'POS TERM', description 'BILL PAYMENT - ONLINE', amount equal to the full current account balance, the card number from the account's cross-reference record, merchant id 999999999, merchant name 'BILL PAYMENT', merchant city and zip 'N/A', and origination and processing timestamps both set to the current CICS time (YYYY-MM-DD HH:MM:SS.000000).

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | Payment confirmed |
| Outcome | TRAN-RECORD written to TRANSACT |
| Implemented at | COBIL00C PROCESS-ENTER-KEY `app/cbl/COBIL00C.cbl:218-233` |
| Implemented at | COBIL00C  `app/cbl/COBIL00C.cbl:249-267` |
| Anchor (verified) | `MOVE 'BILL PAYMENT - ONLINE' TO TRAN-DESC` |

### BR-COBIL00C-009

A bill payment always pays the entire outstanding balance: TRAN-AMT is set to ACCT-CURR-BAL and the new balance is ACCT-CURR-BAL - TRAN-AMT (i.e. zero), which is rewritten to the account master. Partial payments are not supported.

| Item | Value |
|---|---|
| Category | calculation |
| Confidence | Confirmed |
| Conditions | Payment confirmed |
| Outcome | ACCT-CURR-BAL becomes 0 and ACCTDAT is rewritten |
| Implemented at | COBIL00C PROCESS-ENTER-KEY `app/cbl/COBIL00C.cbl:224-235` |
| Anchor (verified) | `COMPUTE ACCT-CURR-BAL = ACCT-CURR-BAL - TRAN-AMT` |

### BR-COBIL00C-010

After writing the payment transaction the user sees 'Payment successful.  Your Transaction ID is <id>.' in green and the input fields are cleared; a duplicate transaction key gives 'Tran ID already exist...' and any other write failure 'Unable to Add Bill pay Transaction...'.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | TRANSACT WRITE RESP NORMAL / DUPKEY / DUPREC / other |
| Outcome | Success or error message |
| Messages | Payment successful. ;  Your Transaction ID is ; Tran ID already exist...; Unable to Add Bill pay Transaction... |
| Implemented at | COBIL00C WRITE-TRANSACT-FILE `app/cbl/COBIL00C.cbl:522-547` |
| Anchor (verified) | `MOVE 'Tran ID already exist...' TO` |

### BR-COBIL00C-011

An account id not found in the account master is rejected with 'Account ID NOT found...'; any other read failure shows 'Unable to lookup Account...'. Both stop the payment.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | ACCTDAT READ UPDATE RESP NOTFND / other |
| Outcome | Error flag set, message displayed |
| Messages | Account ID NOT found...; Unable to lookup Account... |
| Implemented at | COBIL00C READ-ACCTDAT-FILE `app/cbl/COBIL00C.cbl:356-372` |
| Anchor (verified) | `MOVE 'Unable to lookup Account...' TO` |

### BR-COBIL00C-012

A missing card cross-reference for the account shows 'Account ID NOT found...' and other xref read errors 'Unable to lookup XREF AIX file...'; an account rewrite failure shows 'Account ID NOT found...' (NOTFND) or 'Unable to Update Account...'. These set the error flag but do not stop or undo the remaining payment steps (see observations).

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | CXACAIX READ or ACCTDAT REWRITE not NORMAL |
| Outcome | Error message displayed |
| Messages | Unable to lookup XREF AIX file...; Unable to Update Account... |
| Implemented at | COBIL00C READ-CXACAIX-FILE `app/cbl/COBIL00C.cbl:420-436` |
| Implemented at | COBIL00C  `app/cbl/COBIL00C.cbl:386-403` |
| Anchor (verified) | `MOVE 'Unable to lookup XREF AIX file...' TO` |

### BR-COBIL00C-013

When returning to a previous screen and no target program is set, the bill-payment program goes to the sign-on program COSGN00C; the commarea is stamped with from-transaction CB00, from-program COBIL00C and context 0. A start without commarea (EIBCALEN = 0) is sent to COSGN00C.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | CDEMO-TO-PROGRAM blank |
| Outcome | XCTL to COSGN00C with commarea |
| Implemented at | COBIL00C RETURN-TO-PREV-SCREEN `app/cbl/COBIL00C.cbl:275-283` |
| Implemented at | COBIL00C  `app/cbl/COBIL00C.cbl:106-109` |
| Anchor (verified) | `IF CDEMO-TO-PROGRAM = LOW-VALUES OR SPACES` |


## COBTUPDT

Program page: [COBTUPDT](07-programs/COBTUPDT.md).

### BR-TRANTYPE-COBTUPDT-001

A transaction-type maintenance record inserts when the type is A, updates when the type is U, deletes when the type is D, and is ignored when the type is asterisk. Any other type abends with message ERROR: TYPE NOT VALID.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | INPUT-REC-TYPE EVALUATE |
| Outcome | INSERT; UPDATE; DELETE; ignore; abend - ERROR: TYPE NOT VALID |
| Messages | ERROR: TYPE NOT VALID |
| Implemented at | COBTUPDT 1003-TREAT-RECORD `app/app-transaction-type-db2/cbl/COBTUPDT.cbl:111-128` |
| Batch review | corrected: Dispatch on INPUT-REC-TYPE is correct (A=INSERT via 10031-INSERT-DB, U=UPDATE via 10032-UPDATE-DB, D=DELETE via 10033-DELETE-DB, '*'=display 'IGNORING COMMENTED LINE' only). Corrected: the OTHER branch builds 'ERROR: TYPE NOT VALID' and PERFORMs 9999-ABEND, but 9999-ABEND (COBTUPDT.cbl:230-233) only DISPLAYs WS-RETURN-MSG and moves 4 to RETURN-CODE; it does not stop the run or issue an abend, so the loop in 1001-READ-NEXT-RECORDS continues with the next record. Range widened to include the EVALUATE header (line 110) and END-EVALUATE (129). (`app/app-transaction-type-db2/cbl/COBTUPDT.cbl:110-129`, anchor `WHEN OTHER`) |

### BR-COBTUPDT-001

Any record-level failure (invalid record type, SQL error, or row not found) is reported by displaying the message and setting the job return code to 4, but processing continues with the next input record; successful records before and after are still applied.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | 9999-ABEND is performed from 1003-TREAT-RECORD, 10031-INSERT-DB, 10032-UPDATE-DB or 10033-DELETE-DB. |
| Outcome | WS-RETURN-MSG displayed; RETURN-CODE = 4; loop continues until end of file. |
| Implemented at | COBTUPDT 9999-ABEND `app/app-transaction-type-db2/cbl/COBTUPDT.cbl:230-233` |
| Implemented at | COBTUPDT  `app/app-transaction-type-db2/cbl/COBTUPDT.cbl:93-96` |
| Anchor (verified) | `MOVE 4 TO RETURN-CODE` |

### BR-COBTUPDT-002

Adding a transaction type succeeds only when the INSERT returns SQLCODE 0; any negative SQLCODE (for example a duplicate TR_TYPE) is reported as a TRANSACTION_TYPE table access error with the SQLCODE and sets RC 4.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | INPUT-REC-TYPE = 'A'; INSERT of TR_TYPE = INPUT-REC-NUMBER, TR_DESCRIPTION = INPUT-REC-DESC. |
| Outcome | SQLCODE 0: 'RECORD INSERTED SUCCESSFULLY'. SQLCODE < 0: message 'Error accessing: TRANSACTION_TYPE table. SQLCODE:' + code, 9999-ABEND. |
| Messages | RECORD INSERTED SUCCESSFULLY; Error accessing:;  TRANSACTION_TYPE table. SQLCODE: |
| Implemented at | COBTUPDT 10031-INSERT-DB `app/app-transaction-type-db2/cbl/COBTUPDT.cbl:151-163` |
| Implemented at | COBTUPDT  `app/app-transaction-type-db2/cbl/COBTUPDT.cbl:136-148` |
| Anchor (verified) | `WHEN SQLCODE < 0` |

### BR-COBTUPDT-003

An update record for a transaction type code that does not exist in TRANSACTION_TYPE (SQLCODE +100) is rejected with 'No records found.' and RC 4; negative SQLCODEs are reported as table access errors. Only TR_DESCRIPTION is changed; TR_TYPE is the key.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | INPUT-REC-TYPE = 'U'; UPDATE ... SET TR_DESCRIPTION = :INPUT-REC-DESC WHERE TR_TYPE = :INPUT-REC-NUMBER. |
| Outcome | 0: 'RECORD UPDATED SUCCESSFULLY'; +100: 'No records found.' + 9999-ABEND; <0: table error + 9999-ABEND. |
| Messages | RECORD UPDATED SUCCESSFULLY; No records found. |
| Implemented at | COBTUPDT 10032-UPDATE-DB `app/app-transaction-type-db2/cbl/COBTUPDT.cbl:177-193` |
| Implemented at | COBTUPDT  `app/app-transaction-type-db2/cbl/COBTUPDT.cbl:171-175` |
| Anchor (verified) | `WHEN SQLCODE = +100` |

### BR-COBTUPDT-004

A delete record for a transaction type code that does not exist (SQLCODE +100) is rejected with 'No records found.' and RC 4; negative SQLCODEs (for example a referential constraint from TRANSACTION_TYPE_CATEGORY) are reported as table access errors with RC 4.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | INPUT-REC-TYPE = 'D'; DELETE WHERE TR_TYPE = :INPUT-REC-NUMBER. |
| Outcome | 0: 'RECORD DELETED SUCCESSFULLY'; +100: 'No records found.' + 9999-ABEND; <0: table error + 9999-ABEND. |
| Messages | RECORD DELETED SUCCESSFULLY; No records found. |
| Implemented at | COBTUPDT 10033-DELETE-DB `app/app-transaction-type-db2/cbl/COBTUPDT.cbl:207-225` |
| Implemented at | COBTUPDT  `app/app-transaction-type-db2/cbl/COBTUPDT.cbl:201-204` |
| Anchor (verified) | `DISPLAY 'RECORD DELETED SUCCESSFULLY'` |


## COCRDLIC

Program page: [COCRDLIC](07-programs/COCRDLIC.md).

### BR-COCRDLIC-001

The card list starts afresh (first page, paging keys cleared, last page not shown) whenever it is entered in first-entry mode from a different program, e.g. from the main menu; with no commarea at all it also creates a new commarea with from-transaction CCLI, from-program COCRDLIC and user type 'U'.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | EIBCALEN = 0, or CDEMO-PGM-ENTER and CDEMO-FROM-PROGRAM not COCRDLIC |
| Outcome | WS-THIS-PROGCOMMAREA initialised; CA-FIRST-PAGE, CA-LAST-PAGE-NOT-SHOWN |
| Implemented at | COCRDLIC 0000-MAIN `app/cbl/COCRDLIC.cbl:315-343` |
| Anchor (verified) | `AND CDEMO-FROM-PROGRAM NOT EQUAL LIT-THISPGM)` |

### BR-COCRDLIC-002

On the card list only ENTER, PF3, PF7 and PF8 are recognised; any other attention key is processed as ENTER. Screen input is received and edited only when the list re-enters itself (commarea present and CDEMO-FROM-PROGRAM = COCRDLIC).

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | AID not ENTER/PF3/PF7/PF8 |
| Outcome | Treated as ENTER |
| Implemented at | COCRDLIC 0000-MAIN `app/cbl/COCRDLIC.cbl:357-380` |
| Anchor (verified) | `CCARD-AID-PFK08` |

### BR-COCRDLIC-003

PF3 pressed on the card list always returns to the main menu COMEN01C (not to the caller): the commarea is stamped with from CCLI/COCRDLIC, user type 'U', first-entry context and last map, then XCTL to COMEN01C.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | CCARD-AID-PFK03 and CDEMO-FROM-PROGRAM = COCRDLIC |
| Outcome | XCTL COMEN01C with CARDDEMO-COMMAREA |
| Implemented at | COCRDLIC 0000-MAIN `app/cbl/COCRDLIC.cbl:383-406` |
| Anchor (verified) | `PROGRAM (LIT-MENUPGM)` |

### BR-COCRDLIC-004

When the input has errors the list is redisplayed with the error; the card file is re-read only when both filters are valid (i.e. the error is in the row selections). With an invalid account or card filter no records are read and the selection column is protected.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | INPUT-ERROR |
| Outcome | Screen redisplayed with error message; list re-read only for selection errors |
| Implemented at | COCRDLIC 0000-MAIN `app/cbl/COCRDLIC.cbl:418-438` |
| Anchor (verified) | `AND NOT FLG-CARDFILTER-NOT-OK` |

### BR-COCRDLIC-005

PF7 on the first page does not page: the current page is re-read from its first card and the message 'NO PREVIOUS PAGES TO DISPLAY' is shown.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | CCARD-AID-PFK07 and CA-FIRST-PAGE |
| Outcome | Same page redisplayed with message |
| Messages | NO PREVIOUS PAGES TO DISPLAY |
| Implemented at | COCRDLIC 0000-MAIN `app/cbl/COCRDLIC.cbl:439-454` |
| Implemented at | COCRDLIC  `app/cbl/COCRDLIC.cbl:901-904` |
| Anchor (verified) | `AND CA-FIRST-PAGE` |

### BR-COCRDLIC-006

When control comes back to the card list from another program (re-entry flag set but from-program not COCRDLIC, or PF3 still set as AID), the commarea is re-initialised and the list restarts at page 1, discarding filters and the previously selected account/card.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | CCARD-AID-PFK03 (from other program) or CDEMO-PGM-REENTER and CDEMO-FROM-PROGRAM not COCRDLIC |
| Outcome | CARDDEMO-COMMAREA and paging context initialised; first page listed |
| Implemented at | COCRDLIC 0000-MAIN `app/cbl/COCRDLIC.cbl:458-482` |
| Anchor (verified) | `WHEN CDEMO-PGM-REENTER AND` |

### BR-COCRDLIC-007

PF8 pages forward only when a next page exists: the page number is increased by 1 and the browse restarts at the saved last-card key (the first record after the current page). Without a next page, PF8 falls to the default branch and redisplays the current page.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | CCARD-AID-PFK08 and CA-NEXT-PAGE-EXISTS |
| Outcome | Next 7 matching cards listed |
| Implemented at | COCRDLIC 0000-MAIN `app/cbl/COCRDLIC.cbl:485-497` |
| Implemented at | COCRDLIC  `app/cbl/COCRDLIC.cbl:410-414` |
| Anchor (verified) | `ADD +1 TO WS-CA-SCREEN-NUM` |

### BR-COCRDLIC-008

PF7 when not on the first page pages backward: the page number is decreased by 1 and the 7 matching cards preceding the current page's first card are read backwards.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | CCARD-AID-PFK07 and NOT CA-FIRST-PAGE |
| Outcome | Previous page listed |
| Implemented at | COCRDLIC 0000-MAIN `app/cbl/COCRDLIC.cbl:501-513` |
| Anchor (verified) | `SUBTRACT 1 FROM WS-CA-SCREEN-NUM` |

### BR-COCRDLIC-009

ENTER with 'S' against one listed card transfers to the card detail program COCRDSLC, passing that row's account number in CDEMO-ACCT-ID and card number in CDEMO-CARD-NUM, with from CCLI/COCRDLIC, user type 'U' and first-entry context.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | CCARD-AID-ENTER, VIEW-REQUESTED-ON(I-SELECTED), no input error, re-entry from itself |
| Outcome | XCTL COCRDSLC with CARDDEMO-COMMAREA |
| Implemented at | COCRDLIC 0000-MAIN `app/cbl/COCRDLIC.cbl:517-541` |
| Anchor (verified) | `AND VIEW-REQUESTED-ON(I-SELECTED)` |

### BR-COCRDLIC-010

ENTER with 'U' against one listed card transfers to the card update program COCRDUPC, passing that row's account number and card number in the commarea, with from CCLI/COCRDLIC, user type 'U' and first-entry context.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | CCARD-AID-ENTER, UPDATE-REQUESTED-ON(I-SELECTED), re-entry from itself |
| Outcome | XCTL COCRDUPC with CARDDEMO-COMMAREA |
| Implemented at | COCRDLIC 0000-MAIN `app/cbl/COCRDLIC.cbl:545-569` |
| Anchor (verified) | `AND UPDATE-REQUESTED-ON(I-SELECTED)` |

### BR-COCRDLIC-011

In all other cases (ENTER without a selection, first display, PF8 with no next page) the list is (re)displayed starting from the first card key of the current page; on a fresh start this key is empty, so the list starts at the beginning of the card file.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | No earlier WHEN matched |
| Outcome | Page listed from WS-CA-FIRST-CARD-NUM |
| Implemented at | COCRDLIC 0000-MAIN `app/cbl/COCRDLIC.cbl:572-582` |
| Anchor (verified) | `WHEN OTHER` |

### BR-COCRDLIC-012

Paging messages: PF8 when no next page exists first shows the action hint 'TYPE S FOR DETAIL, U TO UPDATE ANY RECORD' and marks the last page as shown; a further PF8 shows 'NO MORE PAGES TO DISPLAY'. The hint is also shown whenever a next page exists or no other info is set. Filter errors suppress these messages.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | CCARD-AID-PFK08, CA-NEXT-PAGE-NOT-EXISTS, CA-LAST-PAGE-SHOWN / NOT-SHOWN |
| Outcome | Error or info message on the list screen |
| Messages | NO PREVIOUS PAGES TO DISPLAY; NO MORE PAGES TO DISPLAY; TYPE S FOR DETAIL, U TO UPDATE ANY RECORD |
| Implemented at | COCRDLIC 1400-SETUP-MESSAGE `app/cbl/COCRDLIC.cbl:897-930` |
| Implemented at | COCRDLIC  `app/cbl/COCRDLIC.cbl:113-116` |
| Anchor (verified) | `MOVE 'NO MORE PAGES TO DISPLAY'` |

### BR-COCRDLIC-013

The account filter is optional: spaces, low-values or all zeros mean no account filter. If supplied it must be numeric over all 11 positions; otherwise the input is rejected with 'ACCOUNT FILTER,IF SUPPLIED MUST BE A 11 DIGIT NUMBER', the account filter is shown in red and row selection is protected.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | CC-ACCT-ID blank/zero -> no filter; NOT NUMERIC -> error |
| Outcome | FLG-ACCTFILTER-BLANK / NOT-OK / ISVALID; CDEMO-ACCT-ID set or zeroed |
| Messages | ACCOUNT FILTER,IF SUPPLIED MUST BE A 11 DIGIT NUMBER |
| Implemented at | COCRDLIC 2210-EDIT-ACCOUNT `app/cbl/COCRDLIC.cbl:1007-1029` |
| Anchor (verified) | `'ACCOUNT FILTER,IF SUPPLIED MUST BE A 11 DIGIT NUMBER'` |

### BR-COCRDLIC-014

The card number filter is optional: spaces, low-values or all zeros mean no card filter. If supplied it must be numeric over all 16 positions; otherwise the input is rejected with 'CARD ID FILTER,IF SUPPLIED MUST BE A 16 DIGIT NUMBER' (only if no account-filter message is already set) and row selection is protected.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | CC-CARD-NUM blank/zero -> no filter; NOT NUMERIC -> error |
| Outcome | FLG-CARDFILTER-BLANK / NOT-OK / ISVALID; CDEMO-CARD-NUM set or zeroed |
| Messages | CARD ID FILTER,IF SUPPLIED MUST BE A 16 DIGIT NUMBER |
| Implemented at | COCRDLIC 2220-EDIT-CARD `app/cbl/COCRDLIC.cbl:1042-1066` |
| Anchor (verified) | `'CARD ID FILTER,IF SUPPLIED MUST BE A 16 DIGIT NUMBER'` |

### BR-COCRDLIC-015

Only one card may be selected per request: if more than one row carries 'S' or 'U', the input is rejected with 'PLEASE SELECT ONLY ONE RECORD TO VIEW OR UPDATE' and every selected row is highlighted as an error. Selection editing is skipped when a filter is invalid.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | Count of 'S' + 'U' in WS-EDIT-SELECT-FLAGS > 1 |
| Outcome | INPUT-ERROR; message; row error flags set |
| Messages | PLEASE SELECT ONLY ONE RECORD TO VIEW OR UPDATE |
| Implemented at | COCRDLIC 2250-EDIT-ARRAY `app/cbl/COCRDLIC.cbl:1075-1094` |
| Implemented at | COCRDLIC  `app/cbl/COCRDLIC.cbl:123-124` |
| Anchor (verified) | `SET WS-MORE-THAN-1-ACTION TO TRUE` |

### BR-COCRDLIC-016

Valid row action codes are 'S' (view detail), 'U' (update) or blank. Any other code marks the row in error and rejects the input with 'INVALID ACTION CODE' (unless another message is already set). The row with S/U becomes the selected row (I-SELECTED).

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | WS-EDIT-SELECT(I) not in ('S','U',' ',LOW-VALUES) |
| Outcome | INPUT-ERROR; row flagged; message |
| Messages | INVALID ACTION CODE |
| Implemented at | COCRDLIC 2250-EDIT-ARRAY `app/cbl/COCRDLIC.cbl:1099-1115` |
| Implemented at | COCRDLIC  `app/cbl/COCRDLIC.cbl:74-82` |
| Implemented at | COCRDLIC  `app/cbl/COCRDLIC.cbl:125-126` |
| Anchor (verified) | `SET WS-INVALID-ACTION-CODE TO TRUE` |

### BR-COCRDLIC-017

A page holds at most 7 cards (WS-MAX-SCREEN-LINES). Reading forward from the start key in card-number order, only records passing the filters are placed on the page; the first placed card's key becomes the page's first-card key, and the page number is set to 1 if it was 0.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | READNEXT NORMAL/DUPREC and WS-DONOT-EXCLUDE-THIS-RECORD |
| Outcome | WS-SCREEN-ROWS filled; WS-CA-FIRST-CARDKEY and WS-CA-LAST-CARDKEY saved |
| Implemented at | COCRDLIC 9000-READ-FORWARD `app/cbl/COCRDLIC.cbl:1144-1194` |
| Implemented at | COCRDLIC  `app/cbl/COCRDLIC.cbl:177-178` |
| Anchor (verified) | `IF WS-SCRN-COUNTER = WS-MAX-SCREEN-LINES` |

### BR-COCRDLIC-018

After the 7th card is placed, one more record is read (without filtering) to decide whether a next page exists; its key becomes the start key for PF8. Reaching end of file sets 'no next page' and the message 'NO MORE RECORDS TO SHOW'; if page 1 has no matching card at all, the message is 'NO RECORDS FOUND FOR THIS SEARCH CONDITION.'.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | Lookahead READNEXT result; ENDFILE; WS-CA-SCREEN-NUM = 1 and WS-SCRN-COUNTER = 0 |
| Outcome | CA-NEXT-PAGE-EXISTS / NOT-EXISTS; message |
| Messages | NO MORE RECORDS TO SHOW; NO RECORDS FOUND FOR THIS SEARCH CONDITION. |
| Implemented at | COCRDLIC 9000-READ-FORWARD `app/cbl/COCRDLIC.cbl:1196-1246` |
| Implemented at | COCRDLIC  `app/cbl/COCRDLIC.cbl:121-122` |
| Anchor (verified) | `SET WS-NO-RECORDS-FOUND TO TRUE` |

### BR-COCRDLIC-019

Any card-file read failure other than end of file stops the list fill and shows 'File Error: READ on CARDDAT returned RESP <resp>,RESP2 <resp2>' on the screen; the rows read so far are still displayed.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | READNEXT RESP not NORMAL/DUPREC/ENDFILE |
| Outcome | Loop ends; file-error message |
| Messages | File Error:;  returned RESP |
| Implemented at | COCRDLIC 9000-READ-FORWARD `app/cbl/COCRDLIC.cbl:1247-1254` |
| Implemented at | COCRDLIC  `app/cbl/COCRDLIC.cbl:153-171` |
| Anchor (verified) | `MOVE WS-FILE-ERROR-MESSAGE TO WS-ERROR-MSG` |

### BR-COCRDLIC-020

Paging backward reads the card file in descending card-number order from the current page's first card, skips that card itself, and fills rows 7 down to 1 with the preceding cards that pass the filters; the card placed in row 1 becomes the new first-card key. A read error (including reaching the start of the file) ends the fill with the file-error message.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | PF7 and not first page |
| Outcome | WS-SCREEN-ROWS filled bottom-up; WS-CA-FIRST-CARDKEY updated |
| Implemented at | COCRDLIC 9100-READ-BACKWARDS `app/cbl/COCRDLIC.cbl:1283-1371` |
| Anchor (verified) | `WS-MAX-SCREEN-LINES + 1` |

### BR-COCRDLIC-021

Record selection filter: a card is listed only if it matches every supplied filter - its CARD-ACCT-ID equals the account filter when a valid account filter was entered, and its CARD-NUM equals the card filter when a valid card filter was entered. With no filters all cards are listed.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | FLG-ACCTFILTER-ISVALID / FLG-CARDFILTER-ISVALID |
| Outcome | WS-EXCLUDE-THIS-RECORD or WS-DONOT-EXCLUDE-THIS-RECORD |
| Implemented at | COCRDLIC 9500-FILTER-RECORDS `app/cbl/COCRDLIC.cbl:1382-1407` |
| Anchor (verified) | `IF CARD-ACCT-ID = CC-ACCT-ID` |


## COCRDSLC

Program page: [COCRDSLC](07-programs/COCRDSLC.md).

### BR-BASE-COCRDSLC-001

A card-list account filter of low-values, spaces or zero is reported as not provided. A supplied account number that is not numeric is rejected. An asterisk or spaces on the screen field is treated as not supplied.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | CC-ACCT-ID = low-values or spaces, or CC-ACCT-ID-N = zeros ; CC-ACCT-ID is not numeric |
| Outcome | set INPUT-ERROR and redisplay the screen - Account number not provided; set INPUT-ERROR and redisplay the screen - ACCOUNT FILTER,IF SUPPLIED MUST BE A 11 DIGIT NUMBER |
| Messages | Account number not provided; ACCOUNT FILTER,IF SUPPLIED MUST BE A 11 DIGIT NUMBER |
| Implemented at | COCRDSLC 2200-EDIT-MAP-INPUTS `app/cbl/COCRDSLC.cbl:608-620` |
| Implemented at | COCRDSLC 2210-EDIT-ACCOUNT `app/cbl/COCRDSLC.cbl:647-679` |
| Implemented at | COCRDSLC  `app/cbl/COCRDSLC.cbl:138-139` |
| Batch review | corrected: COCRDSLC is the card detail (single card) screen, not the card list. A blank/zero account is not merely 'reported': it sets INPUT-ERROR, so the account number is mandatory and the card is not read. The non-numeric message is the hardcoded literal 'ACCOUNT FILTER,IF SUPPLIED MUST BE A 11 DIGIT NUMBER' (669-671); the 88-level SEARCHED-ACCT-NOT-NUMERIC text at 145-146 is never used. '*'/SPACES normalisation at 615-620 confirmed. (`app/cbl/COCRDSLC.cbl:647-679`, anchor `IF CC-ACCT-ID IS NOT NUMERIC`) |

### BR-BASE-COCRDSLC-002

A card-list card filter of low-values, spaces or zero is reported as not provided. A supplied card number that is not numeric is rejected. An asterisk or spaces on the screen field is treated as not supplied.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | CC-CARD-NUM = low-values or spaces, or CC-CARD-NUM-N = zeros ; CC-CARD-NUM is not numeric |
| Outcome | set INPUT-ERROR and redisplay the screen - Card number not provided; set INPUT-ERROR and redisplay the screen - CARD ID FILTER,IF SUPPLIED MUST BE A 16 DIGIT NUMBER |
| Messages | Card number not provided; CARD ID FILTER,IF SUPPLIED MUST BE A 16 DIGIT NUMBER |
| Implemented at | COCRDSLC 2200-EDIT-MAP-INPUTS `app/cbl/COCRDSLC.cbl:622-634` |
| Implemented at | COCRDSLC 2220-EDIT-CARD `app/cbl/COCRDSLC.cbl:685-719` |
| Implemented at | COCRDSLC  `app/cbl/COCRDSLC.cbl:140-141` |
| Batch review | corrected: Same correction as for the account: this is the card detail screen, and a blank/zero card number sets INPUT-ERROR (mandatory). Non-numeric message is the literal 'CARD ID FILTER,IF SUPPLIED MUST BE A 16 DIGIT NUMBER' (710-712); the 88 SEARCHED-CARD-NOT-NUMERIC at 147-148 is unused. '*'/SPACES normalisation at 622-627 confirmed. (`app/cbl/COCRDSLC.cbl:685-720`, anchor `IF CC-CARD-NUM IS NOT NUMERIC`) |

### BR-BASE-COCRDSLC-003

When both the account filter and the card filter are blank, the card list screen reports that no input was received.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | FLG-ACCTFILTER-BLANK and FLG-CARDFILTER-BLANK true |
| Outcome | set INPUT-ERROR and redisplay the screen - No input received |
| Messages | No input received |
| Implemented at | COCRDSLC 2200-EDIT-MAP-INPUTS `app/cbl/COCRDSLC.cbl:636-640` |
| Implemented at | COCRDSLC  `app/cbl/COCRDSLC.cbl:142-143` |
| Batch review | confirmed: Confirmed. The SET is unconditional, so 'No input received' replaces the 'Account number not provided' message already set by 2210-EDIT-ACCOUNT. (`app/cbl/COCRDSLC.cbl:637-640`, anchor `IF FLG-ACCTFILTER-BLANK AND FLG-CARDFILTER-BLANK SET NO-SEARCH-CRITERIA-RECEIVED TO TRUE`) |

### BR-COCRDSLC-001

When PF3 is pressed the program transfers control (XCTL) back to the program and transaction recorded in CDEMO-FROM-PROGRAM / CDEMO-FROM-TRANID; when either is LOW-VALUES or SPACES the main menu COMEN01C / transaction CM00 is used instead. Before leaving it records itself as the from-program, sets the user type to regular user and the context to first entry.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | AID key is PF3 (or PF15, folded to PF3) |
| Outcome | XCTL to caller or COMEN01C with CARDDEMO-COMMAREA; CDEMO-USRTYP-USER and CDEMO-PGM-ENTER set |
| Implemented at | COCRDSLC 0000-MAIN `app/cbl/COCRDSLC.cbl:304-334` |
| Implemented at | COCRDSLC  `app/cbl/COCRDSLC.cbl:179-182` |
| Anchor (verified) | `IF CDEMO-FROM-TRANID EQUAL LOW-VALUES OR CDEMO-FROM-TRANID EQUAL SPACES MOVE LIT-MENUTRANID TO CDEMO-TO-TRANID` |

### BR-COCRDSLC-002

Only ENTER and PF3 are accepted on the card detail screen; any other attention key is silently treated as ENTER.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | CCARD-AID is neither ENTER nor PFK03 |
| Outcome | CCARD-AID-ENTER is set and processing continues as for ENTER; no error message |
| Implemented at | COCRDSLC 0000-MAIN `app/cbl/COCRDSLC.cbl:291-299` |
| Anchor (verified) | `IF PFK-INVALID SET CCARD-AID-ENTER TO TRUE` |

### BR-COCRDSLC-003

When the program is first entered from the card list program COCRDLIC, the account and card number passed in the commarea are treated as already validated: the card is read and its details displayed without editing the inputs.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | CDEMO-PGM-ENTER and CDEMO-FROM-PROGRAM = 'COCRDLIC' |
| Outcome | INPUT-OK; CDEMO-ACCT-ID/CDEMO-CARD-NUM moved to CC-ACCT-ID-N/CC-CARD-NUM-N; 9000-READ-DATA then screen sent |
| Implemented at | COCRDSLC 0000-MAIN `app/cbl/COCRDSLC.cbl:339-348` |
| Anchor (verified) | `WHEN CDEMO-PGM-ENTER AND CDEMO-FROM-PROGRAM EQUAL LIT-CCLISTPGM` |

### BR-COCRDSLC-004

On first entry from any program other than COCRDLIC the search screen is shown without reading data; on re-entry the typed criteria are edited and, if any edit fails, the screen is redisplayed with the error, otherwise the card is read and displayed.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | CDEMO-PGM-ENTER (not from COCRDLIC) or CDEMO-PGM-REENTER with INPUT-ERROR / no error |
| Outcome | Screen sent; card read only when all input edits passed |
| Implemented at | COCRDSLC 0000-MAIN `app/cbl/COCRDSLC.cbl:349-371` |
| Anchor (verified) | `WHEN CDEMO-PGM-REENTER PERFORM 2000-PROCESS-INPUTS` |

### BR-COCRDSLC-005

If the program context matches none of the expected scenarios, the program sends the plain-text message 'UNEXPECTED DATA SCENARIO' and ends the conversation (no abend is issued even though ABEND-CODE '0001' is prepared).

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | WHEN OTHER of the main EVALUATE |
| Outcome | SEND TEXT then CICS RETURN without TRANSID |
| Messages | UNEXPECTED DATA SCENARIO |
| Implemented at | COCRDSLC 0000-MAIN `app/cbl/COCRDSLC.cbl:373-380` |
| Anchor (verified) | `MOVE 'UNEXPECTED DATA SCENARIO' TO WS-RETURN-MSG` |

### BR-COCRDSLC-006

The card is looked up in CARDDAT by card number only; the entered account number is not part of the key and is not compared with CARD-ACCT-ID. Not found produces 'Did not find cards for this search condition' and marks both filters in error; any other response produces a 'File Error: READ on CARDDAT returned RESP ... ,RESP2 ...' message.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | CICS READ response NORMAL / NOTFND / other |
| Outcome | FOUND-CARDS-FOR-ACCOUNT on success; INPUT-ERROR with message otherwise |
| Messages | Did not find cards for this search condition; File Error: |
| Implemented at | COCRDSLC 9100-GETCARD-BYACCTCARD `app/cbl/COCRDSLC.cbl:740-772` |
| Implemented at | COCRDSLC  `app/cbl/COCRDSLC.cbl:153-154` |
| Anchor (verified) | `RIDFLD (WS-CARD-RID-CARDNUM)` |

### BR-COCRDSLC-007

When the card detail screen was reached from the card list (last mapset COCRDLI and caller COCRDLIC), the account and card number fields are protected so the user cannot change the selection; otherwise they are enterable.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | CDEMO-LAST-MAPSET = 'COCRDLI' and CDEMO-FROM-PROGRAM = 'COCRDLIC' |
| Outcome | ACCTSIDA/CARDSIDA = DFHBMPRF, else DFHBMFSE |
| Implemented at | COCRDSLC 1300-SETUP-SCREEN-ATTRS `app/cbl/COCRDSLC.cbl:505-512` |
| Anchor (verified) | `MOVE DFHBMPRF TO ACCTSIDA OF CCRDSLAI` |


## COCRDUPC

Program page: [COCRDUPC](07-programs/COCRDUPC.md).

### BR-BASE-COCRDUPC-001

Before card details are fetched, an account number that is low-values, spaces or zero is reported as not provided. A supplied account number that is not numeric is rejected.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | CC-ACCT-ID = low-values or spaces, or CC-ACCT-ID-N = zeros ; CC-ACCT-ID is not numeric |
| Outcome | set INPUT-ERROR and redisplay the screen - Account number not provided; set INPUT-ERROR and redisplay the screen - ACCOUNT FILTER,IF SUPPLIED MUST BE A 11 DIGIT NUMBER |
| Messages | Account number not provided; ACCOUNT FILTER,IF SUPPLIED MUST BE A 11 DIGIT NUMBER |
| Implemented at | COCRDUPC 1210-EDIT-ACCOUNT `app/cbl/COCRDUPC.cbl:721-756` |
| Implemented at | COCRDUPC  `app/cbl/COCRDUPC.cbl:176-177` |
| Batch review | confirmed: Confirmed; only performed when CCUP-DETAILS-NOT-FETCHED (645-647). A blank account sets INPUT-ERROR (mandatory). The non-numeric message is the literal 'ACCOUNT FILTER,IF SUPPLIED MUST BE A 11 DIGIT NUMBER' (744-746), not an 88-level value. (`app/cbl/COCRDUPC.cbl:721-756`, anchor `IF CC-ACCT-ID IS NOT NUMERIC`) |

### BR-BASE-COCRDUPC-002

Before card details are fetched, a card number that is low-values, spaces or zero is reported as not provided. A supplied card number that is not numeric is rejected.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | CC-CARD-NUM = low-values or spaces, or CC-CARD-NUM-N = zeros ; CC-CARD-NUM is not numeric |
| Outcome | set INPUT-ERROR and redisplay the screen - Card number not provided; set INPUT-ERROR and redisplay the screen - CARD ID FILTER,IF SUPPLIED MUST BE A 16 DIGIT NUMBER |
| Messages | Card number not provided; CARD ID FILTER,IF SUPPLIED MUST BE A 16 DIGIT NUMBER |
| Implemented at | COCRDUPC 1220-EDIT-CARD `app/cbl/COCRDUPC.cbl:762-800` |
| Implemented at | COCRDUPC  `app/cbl/COCRDUPC.cbl:178-180` |
| Batch review | confirmed: Confirmed; blank card sets INPUT-ERROR and 'Card number not provided'; non-numeric uses the literal 'CARD ID FILTER,IF SUPPLIED MUST BE A 16 DIGIT NUMBER' (787-790). (`app/cbl/COCRDUPC.cbl:762-800`, anchor `IF CC-CARD-NUM IS NOT NUMERIC`) |

### BR-BASE-COCRDUPC-003

Before card details are fetched, only the account and card search keys are edited. When both are blank the message is No input received.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | CCUP-DETAILS-NOT-FETCHED true ; FLG-ACCTFILTER-BLANK and FLG-CARDFILTER-BLANK true |
| Outcome | skip the card detail edits - No input received |
| Messages | No input received |
| Implemented at | COCRDUPC 1200-EDIT-MAP-INPUTS `app/cbl/COCRDUPC.cbl:644-662` |
| Implemented at | COCRDUPC  `app/cbl/COCRDUPC.cbl:184-185` |
| Batch review | confirmed: Confirmed; the 'No input received' SET is unconditional and replaces 'Account number not provided'. CCUP-NEW-CARDDATA is cleared to LOW-VALUES on this path (653). (`app/cbl/COCRDUPC.cbl:644-662`, anchor `IF FLG-ACCTFILTER-BLANK AND FLG-CARDFILTER-BLANK SET NO-SEARCH-CRITERIA-RECEIVED TO TRUE`) |

### BR-BASE-COCRDUPC-004

When the new card data equals the fetched card data after both are converted to upper case, no change is reported and the card detail edits are skipped.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | UPPER-CASE(CCUP-NEW-CARDDATA) = UPPER-CASE(CCUP-OLD-CARDDATA) |
| Outcome | skip the card detail edits - No change detected with respect to values fetched. |
| Messages | No change detected with respect to values fetched. |
| Implemented at | COCRDUPC 1200-EDIT-MAP-INPUTS `app/cbl/COCRDUPC.cbl:680-693` |
| Implemented at | COCRDUPC  `app/cbl/COCRDUPC.cbl:186-187` |
| Batch review | confirmed: Confirmed. The detail edits are also skipped when the state is already 'N' (validated) or 'C' (done) (685-686). The compared group includes name, expiry year/month/day and status; CVV is not part of CCUP-*-CARDDATA. (`app/cbl/COCRDUPC.cbl:680-693`, anchor `IF (FUNCTION UPPER-CASE(CCUP-NEW-CARDDATA) EQUAL FUNCTION UPPER-CASE(CCUP-OLD-CARDDATA))`) |

### BR-BASE-COCRDUPC-005

The embossed card name is required and may contain only letters A-Z, a-z and spaces. A name of low-values, spaces or zeros counts as not provided.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | CCUP-NEW-CRDNAME = low-values, spaces or zeros ; CCUP-NEW-CRDNAME contains a character other than a letter or space |
| Outcome | set INPUT-ERROR and redisplay the screen - Card name not provided; set INPUT-ERROR and redisplay the screen - Card name can only contain alphabets and spaces |
| Messages | Card name not provided; Card name can only contain alphabets and spaces |
| Implemented at | COCRDUPC 1230-EDIT-NAME `app/cbl/COCRDUPC.cbl:806-840` |
| Implemented at | COCRDUPC  `app/cbl/COCRDUPC.cbl:255-260` |
| Implemented at | COCRDUPC  `app/cbl/COCRDUPC.cbl:181-184` |
| Batch review | confirmed: Confirmed; messages 'Card name not provided' and 'Card name can only contain alphabets and spaces' (181-184). (`app/cbl/COCRDUPC.cbl:806-840`, anchor `INSPECT CARD-NAME-CHECK CONVERTING LIT-ALL-ALPHA-FROM TO LIT-ALL-SPACES-TO`) |

### BR-BASE-COCRDUPC-006

The card active status must be Y or N. A blank status gets the same message.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | CCUP-NEW-CRDSTCD not in 'Y','N' |
| Outcome | set INPUT-ERROR and redisplay the screen - Card Active Status must be Y or N |
| Messages | Card Active Status must be Y or N |
| Implemented at | COCRDUPC 1240-EDIT-CARDSTATUS `app/cbl/COCRDUPC.cbl:845-873` |
| Implemented at | COCRDUPC  `app/cbl/COCRDUPC.cbl:89-91` |
| Implemented at | COCRDUPC  `app/cbl/COCRDUPC.cbl:194-195` |
| Batch review | confirmed: Confirmed; FLG-YES-NO-VALID accepts only upper-case 'Y' and 'N' (91), so lower-case input is rejected. Message 'Card Active Status must be Y or N'. (`app/cbl/COCRDUPC.cbl:845-873`, anchor `IF FLG-YES-NO-VALID`) |

### BR-BASE-COCRDUPC-007

The card expiry month is required and must be 1 through 12.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | CARD-MONTH-CHECK-N not 1 thru 12 |
| Outcome | set INPUT-ERROR and redisplay the screen - Card expiry month must be between 1 and 12 |
| Messages | Card expiry month must be between 1 and 12 |
| Implemented at | COCRDUPC 1250-EDIT-EXPIRY-MON `app/cbl/COCRDUPC.cbl:877-908` |
| Implemented at | COCRDUPC  `app/cbl/COCRDUPC.cbl:92-95` |
| Implemented at | COCRDUPC  `app/cbl/COCRDUPC.cbl:196-197` |
| Batch review | confirmed: Confirmed; VALID-MONTH VALUES 1 THRU 12 on the PIC 9(2) redefinition (93-95); message 'Card expiry month must be between 1 and 12'. (`app/cbl/COCRDUPC.cbl:877-908`, anchor `IF VALID-MONTH`) |

### BR-BASE-COCRDUPC-008

The card expiry year is required and must be 1950 through 2099.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | CARD-YEAR-CHECK-N not 1950 thru 2099 |
| Outcome | set INPUT-ERROR and redisplay the screen - Invalid card expiry year |
| Messages | Invalid card expiry year |
| Implemented at | COCRDUPC 1260-EDIT-EXPIRY-YEAR `app/cbl/COCRDUPC.cbl:913-944` |
| Implemented at | COCRDUPC  `app/cbl/COCRDUPC.cbl:96-99` |
| Implemented at | COCRDUPC  `app/cbl/COCRDUPC.cbl:198-200` |
| Batch review | confirmed: Confirmed; VALID-YEAR VALUES 1950 THRU 2099 (96-99); message 'Invalid card expiry year'. No check that the expiry date is in the future and the expiry day is not validated. (`app/cbl/COCRDUPC.cbl:913-944`, anchor `IF VALID-YEAR`) |

### BR-COCRDUPC-001

The program exits when PF3 is pressed, or automatically when an update has completed or failed and the user originally came from the card list (last mapset COCRDLI). It commits (SYNCPOINT) and XCTLs to CDEMO-FROM-PROGRAM/TRANID, or to COMEN01C/CM00 when those are blank; when returning to the card list the account and card numbers in the commarea are zeroed.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | PF3, or (state C/L/F and CDEMO-LAST-MAPSET = 'COCRDLI') |
| Outcome | SYNCPOINT; XCTL with CARDDEMO-COMMAREA; CDEMO-USRTYP-USER and CDEMO-PGM-ENTER set |
| Implemented at | COCRDUPC 0000-MAIN `app/cbl/COCRDUPC.cbl:429-476` |
| Anchor (verified) | `IF CDEMO-LAST-MAPSET EQUAL LIT-CCLISTMAPSET MOVE ZEROS TO CDEMO-ACCT-ID` |

### BR-COCRDUPC-002

Accepted keys are ENTER, PF3, PF5 only when changes have been validated but not yet confirmed, and PF12 only after card details have been fetched; any other key is treated as ENTER.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | CCARD-AID and CCUP-CHANGE-ACTION |
| Outcome | Invalid keys silently mapped to CCARD-AID-ENTER |
| Implemented at | COCRDUPC 0000-MAIN `app/cbl/COCRDUPC.cbl:413-424` |
| Anchor (verified) | `(CCARD-AID-PFK05 AND CCUP-CHANGES-OK-NOT-CONFIRMED)` |

### BR-COCRDUPC-003

On first entry from the card list COCRDLIC (or PF12 when the caller is COCRDLIC), the account and card from the commarea are trusted as valid keys: the card is read and its details shown for editing without key edits.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | (CDEMO-PGM-ENTER or PF12) and CDEMO-FROM-PROGRAM = 'COCRDLIC' |
| Outcome | 9000-READ-DATA; CCUP-SHOW-DETAILS; screen sent |
| Implemented at | COCRDUPC 0000-MAIN `app/cbl/COCRDUPC.cbl:482-496` |
| Anchor (verified) | `WHEN CCARD-AID-PFK12 AND CDEMO-FROM-PROGRAM EQUAL LIT-CCLISTPGM` |

### BR-COCRDUPC-004

On a fresh entry (details not fetched and first entry, or first entry from the main menu) the program shows an empty search screen asking for account and card number.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | CCUP-DETAILS-NOT-FETCHED and CDEMO-PGM-ENTER, or CDEMO-FROM-PROGRAM = 'COMEN01C' and not re-enter |
| Outcome | WS-THIS-PROGCOMMAREA initialized; search screen sent; state not fetched / re-enter |
| Messages | Please enter Account and Card Number |
| Implemented at | COCRDUPC 0000-MAIN `app/cbl/COCRDUPC.cbl:502-511` |
| Anchor (verified) | `WHEN CCUP-DETAILS-NOT-FETCHED AND CDEMO-PGM-ENTER` |

### BR-COCRDUPC-005

After an update has completed or failed (and the user did not come from the card list), the next interaction resets the update state, working storage and the commarea account/card numbers and prompts for new search keys.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | CCUP-CHANGE-ACTION = 'C', 'L' or 'F' |
| Outcome | State reset to not fetched; search screen sent |
| Implemented at | COCRDUPC 0000-MAIN `app/cbl/COCRDUPC.cbl:517-528` |
| Anchor (verified) | `WHEN CCUP-CHANGES-OKAYED-AND-DONE WHEN CCUP-CHANGES-FAILED INITIALIZE WS-THIS-PROGCOMMAREA` |

### BR-COCRDUPC-006

In every other situation the screen input is received and edited, the next action is decided from the update state, and the screen is redisplayed.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | WHEN OTHER of the main EVALUATE |
| Outcome | 1000-PROCESS-INPUTS, 2000-DECIDE-ACTION, 3000-SEND-MAP |
| Implemented at | COCRDUPC 0000-MAIN `app/cbl/COCRDUPC.cbl:535-542` |
| Anchor (verified) | `PERFORM 2000-DECIDE-ACTION` |

### BR-COCRDUPC-007

An input of '*' or spaces in the account, card, name, status, expiry month or expiry year field is treated as not supplied (LOW-VALUES); the expiry day is taken from the screen as is.

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | field value '*' or SPACES |
| Outcome | LOW-VALUES moved to CC-ACCT-ID/CC-CARD-NUM/CCUP-NEW-* fields |
| Implemented at | COCRDUPC 1100-RECEIVE-MAP `app/cbl/COCRDUPC.cbl:588-635` |
| Anchor (verified) | `IF CRDNAMEI OF CCRDUPAI = '*' OR CRDNAMEI OF CCRDUPAI = SPACES` |

### BR-COCRDUPC-008

When details are not yet fetched, or the user presses PF12 to cancel changes, the card is (re)read only if both the account and card keys are valid; if found, the state becomes show details, discarding any edits.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | CCUP-DETAILS-NOT-FETCHED or PF12; both key flags valid; card found |
| Outcome | CCUP-SHOW-DETAILS set |
| Implemented at | COCRDUPC 2000-DECIDE-ACTION `app/cbl/COCRDUPC.cbl:949-966` |
| Anchor (verified) | `IF FLG-ACCTFILTER-ISVALID AND FLG-CARDFILTER-ISVALID PERFORM 9000-READ-DATA` |

### BR-COCRDUPC-009

While details are shown, changes become 'validated, awaiting confirmation' only when there is no input error and a change was detected; when edits failed the state stays 'changes not OK' and the user must correct the fields.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | CCUP-SHOW-DETAILS / CCUP-CHANGES-NOT-OK |
| Outcome | State N or unchanged |
| Implemented at | COCRDUPC 2000-DECIDE-ACTION `app/cbl/COCRDUPC.cbl:971-983` |
| Anchor (verified) | `IF INPUT-ERROR OR NO-CHANGES-DETECTED CONTINUE ELSE SET CCUP-CHANGES-OK-NOT-CONFIRMED TO TRUE` |

### BR-COCRDUPC-010

Validated changes are saved only when the user confirms with PF5. The outcome sets the state: lock failure -> 'L' (Changes unsuccessful), rewrite failure -> 'F' (Changes unsuccessful), record changed by another user -> back to show details with the refreshed values, otherwise 'C' (Changes committed to database).

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | CCUP-CHANGES-OK-NOT-CONFIRMED and PF5 |
| Outcome | 9200-WRITE-PROCESSING; CCUP-CHANGE-ACTION set to L, F, S or C |
| Messages | Changes validated.Press F5 to save; Changes committed to database; Changes unsuccessful. Please try again |
| Implemented at | COCRDUPC 2000-DECIDE-ACTION `app/cbl/COCRDUPC.cbl:988-1001` |
| Implemented at | COCRDUPC  `app/cbl/COCRDUPC.cbl:1149-1156` |
| Anchor (verified) | `WHEN DATA-WAS-CHANGED-BEFORE-UPDATE SET CCUP-SHOW-DETAILS TO TRUE` |

### BR-COCRDUPC-011

Without PF5 a validated change is simply redisplayed awaiting confirmation. After a successful save the details are shown again; when there is no calling transaction the commarea account, card and account status are cleared.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | State N without PF5; state C |
| Outcome | No action, or CCUP-SHOW-DETAILS with commarea keys zeroed |
| Implemented at | COCRDUPC 2000-DECIDE-ACTION `app/cbl/COCRDUPC.cbl:1006-1018` |
| Anchor (verified) | `WHEN CCUP-CHANGES-OKAYED-AND-DONE SET CCUP-SHOW-DETAILS TO TRUE` |

### BR-COCRDUPC-012

An update state not handled by the decision logic is treated as a program error: ABEND-ROUTINE sends 'UNEXPECTED DATA SCENARIO' and the task abends with code 9999.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | WHEN OTHER in 2000-DECIDE-ACTION |
| Outcome | CICS ABEND ABCODE('9999') |
| Messages | UNEXPECTED DATA SCENARIO |
| Implemented at | COCRDUPC 2000-DECIDE-ACTION `app/cbl/COCRDUPC.cbl:1019-1026` |
| Implemented at | COCRDUPC  `app/cbl/COCRDUPC.cbl:1531-1553` |
| Anchor (verified) | `MOVE 'UNEXPECTED DATA SCENARIO' TO ABEND-MSG` |

### BR-COCRDUPC-013

When the card is found, the values fetched for later comparison are saved with the embossed name converted to upper case and the expiry date split into year (1-4), month (6-7) and day (9-10).

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | FOUND-CARDS-FOR-ACCOUNT |
| Outcome | CCUP-OLD-CVV-CD, CCUP-OLD-CRDNAME, CCUP-OLD-EXPYEAR/MON/DAY, CCUP-OLD-CRDSTCD populated |
| Implemented at | COCRDUPC 9000-READ-DATA `app/cbl/COCRDUPC.cbl:1352-1369` |
| Anchor (verified) | `INSPECT CARD-EMBOSSED-NAME CONVERTING LIT-LOWER TO LIT-UPPER` |

### BR-COCRDUPC-014

The card to update is located in CARDDAT by card number only; the account number is not part of the key and is not compared with CARD-ACCT-ID. Not found gives 'Did not find cards for this search condition'; other responses give a 'File Error: READ on CARDDAT' message.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | CICS READ response |
| Outcome | FOUND-CARDS-FOR-ACCOUNT or INPUT-ERROR with message |
| Messages | Did not find cards for this search condition; File Error: |
| Implemented at | COCRDUPC 9100-GETCARD-BYACCTCARD `app/cbl/COCRDUPC.cbl:1380-1412` |
| Anchor (verified) | `RIDFLD (WS-CARD-RID-CARDNUM)` |

### BR-COCRDUPC-015

If the card record cannot be read for update (lock), the update is abandoned with 'Could not lock record for update'.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | READ UPDATE response not NORMAL |
| Outcome | INPUT-ERROR; message set; no rewrite |
| Messages | Could not lock record for update |
| Implemented at | COCRDUPC 9200-WRITE-PROCESSING `app/cbl/COCRDUPC.cbl:1427-1449` |
| Anchor (verified) | `SET COULD-NOT-LOCK-FOR-UPDATE TO TRUE` |

### BR-COCRDUPC-016

Optimistic concurrency: before rewriting, the locked record's CVV, upper-cased embossed name, expiry year/month/day and active status must equal the values fetched when the details were shown; otherwise the update is not applied, the message 'Record changed by some one else. Please review' is set and the stored old values are refreshed from the current record.

| Item | Value |
|---|---|
| Category | data-integrity |
| Confidence | Confirmed |
| Conditions | Any compared field differs |
| Outcome | No REWRITE; CCUP-OLD-* refreshed; state returns to show details |
| Messages | Record changed by some one else. Please review |
| Implemented at | COCRDUPC 9300-CHECK-CHANGE-IN-REC `app/cbl/COCRDUPC.cbl:1499-1519` |
| Implemented at | COCRDUPC  `app/cbl/COCRDUPC.cbl:1453-1457` |
| Anchor (verified) | `SET DATA-WAS-CHANGED-BEFORE-UPDATE TO TRUE` |

### BR-COCRDUPC-017

The rewritten card record is built from the screen values: card number, account number from the (protected) account field, CVV from CCUP-NEW-CVV-CD, embossed name as typed, expiry date formatted 'YYYY-MM-DD' from new year, month and day, and the new active status. A REWRITE failure sets 'Update of record failed'.

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | Lock obtained and record unchanged |
| Outcome | EXEC CICS REWRITE FILE(CARDDAT); LOCKED-BUT-UPDATE-FAILED on error |
| Messages | Update of record failed |
| Implemented at | COCRDUPC 9200-WRITE-PROCESSING `app/cbl/COCRDUPC.cbl:1461-1491` |
| Anchor (verified) | `STRING CCUP-NEW-EXPYEAR '-' CCUP-NEW-EXPMON '-' CCUP-NEW-EXPDAY` |

### BR-COCRDUPC-018

Which fields may be edited depends on the update state: before fetch only the account and card keys are enterable; while showing details or correcting errors only name, status, expiry month and year are enterable; once validated or saved all fields are protected. The expiry day is never enterable.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | CCUP-CHANGE-ACTION |
| Outcome | DFHBMFSE / DFHBMPRF attributes on input fields |
| Implemented at | COCRDUPC 3300-SETUP-SCREEN-ATTRS `app/cbl/COCRDUPC.cbl:1172-1208` |
| Anchor (verified) | `WHEN CCUP-CHANGES-OK-NOT-CONFIRMED WHEN CCUP-CHANGES-OKAYED-AND-DONE MOVE DFHBMPRF TO ACCTSIDA OF CCRDUPAI` |


## CODATE01

Program page: [CODATE01](07-programs/CODATE01.md).

### BR-CODATE01-001

Every request message, whatever its content, is answered with the current CICS system date and time as text: 'SYSTEM DATE : ' followed by the date in MM-DD-YYYY form and 'SYSTEM TIME : ' followed by the time formatted by FORMATTIME with a time separator.

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | A request message was received successfully |
| Outcome | Date/time text reply put on CARD.DEMO.REPLY.DATE |
| Messages | SYSTEM DATE : ; SYSTEM TIME : |
| Implemented at | CODATE01 4000-PROCESS-REQUEST-REPLY `app/app-vsam-mq/cbl/CODATE01.cbl:343-361` |
| Anchor (verified) | `STRING  'SYSTEM DATE : ' WS-MMDDYYYY` |

### BR-CODATE01-002

Replies are always put on the fixed queue CARD.DEMO.REPLY.DATE (not the request's ReplyToQ) with MsgId and CorrelId copied from the request, as an MQFMT-STRING message in the queue manager CCSID.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | Every reply |
| Outcome | MQPUT to OUTPUT-QUEUE-HANDLE |
| Messages | CARD.DEMO.REPLY.DATE |
| Implemented at | CODATE01 4100-PUT-REPLY `app/app-vsam-mq/cbl/CODATE01.cbl:370-381` |
| Implemented at | CODATE01  `app/app-vsam-mq/cbl/CODATE01.cbl:145-147` |
| Anchor (verified) | `MOVE SAVE-CORELID                 TO MQMD-CORRELID` |

### BR-CODATE01-003

The transaction drains the triggered input queue: it keeps getting messages (waiting up to 5 seconds each) and commits with CICS SYNCPOINT after each one, stopping normally when MQGET returns MQRC-NO-MSG-AVAILABLE. Any other MQGET failure is reported as 'INP MQGET ERR:' on the error queue and ends the transaction.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | MQ-CONDITION-CODE not MQCC-OK |
| Outcome | NO-MORE-MSGS set (normal end) or error report and termination |
| Messages | INP MQGET ERR: |
| Implemented at | CODATE01 3000-GET-REQUEST `app/app-vsam-mq/cbl/CODATE01.cbl:312-336` |
| Implemented at | CODATE01  `app/app-vsam-mq/cbl/CODATE01.cbl:286-287` |
| Implemented at | CODATE01  `app/app-vsam-mq/cbl/CODATE01.cbl:274-280` |
| Implemented at | CODATE01  `app/app-vsam-mq/cbl/CODATE01.cbl:163-165` |
| Anchor (verified) | `IF MQ-REASON-CODE  =  MQRC-NO-MSG-AVAILABLE` |

### BR-CODATE01-004

If the input queue or reply queue cannot be opened, or a reply cannot be put, the program writes an error record (condition code, reason code, queue name and 'INP MQOPEN ERR' / 'OUT MQOPEN ERR' / 'MQPUT ERR') to CARD.DEMO.ERROR and ends the transaction.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | MQOPEN or MQPUT completion code other than MQCC-OK |
| Outcome | 9000-ERROR then 8000-TERMINATION |
| Messages | INP MQOPEN ERR; OUT MQOPEN ERR; MQPUT ERR |
| Implemented at | CODATE01 2300-OPEN-INPUT-QUEUE `app/app-vsam-mq/cbl/CODATE01.cbl:189-201` |
| Implemented at | CODATE01  `app/app-vsam-mq/cbl/CODATE01.cbl:223-235` |
| Implemented at | CODATE01  `app/app-vsam-mq/cbl/CODATE01.cbl:392-402` |
| Anchor (verified) | `MOVE 'INP MQOPEN ERR'  TO MQ-APPL-RETURN-MESSAGE` |

### BR-CODATE01-005

If the CICS trigger data cannot be retrieved (RETRIEVE response not NORMAL), the program reports 'CICS RETRIEVE' with the RESP code to the error queue and ends without processing any request.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | EXEC CICS RETRIEVE INTO(MQTM) response not NORMAL |
| Outcome | 9000-ERROR then 8000-TERMINATION |
| Messages | CICS RETRIEVE; RESP: |
| Implemented at | CODATE01 1000-CONTROL `app/app-vsam-mq/cbl/CODATE01.cbl:145-159` |
| Anchor (verified) | `IF WS-CICS-RESP1-CD =  DFHRESP(NORMAL)` |


## COMEN01C

Program page: [COMEN01C](07-programs/COMEN01C.md).

### BR-BASE-COMEN01C-001

Menu option COPAUS0C is started only when INQUIRE PROGRAM returns a normal response. Otherwise the menu shows that the option is not installed.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | EIBRESP = DFHRESP(NORMAL) |
| Outcome | XCTL; redisplay menu - This option ... is not installed... |
| Messages | is not installed... |
| Implemented at | COMEN01C  `app/cbl/COMEN01C.cbl:147-168` |
| Batch review | confirmed: INQUIRE PROGRAM ... NOHANDLE; when not NORMAL the message 'This option <name> is not installed...' is shown in red (DFHRED). On success CDEMO-FROM-TRANID/PROGRAM and context 0 are set before XCTL. (`app/cbl/COMEN01C.cbl:147-168`, anchor `IF EIBRESP = DFHRESP(NORMAL)`) |

### BR-BASE-COMEN01C-002

A user-menu option whose program name begins with DUMMY is not started. The menu shows that the option is coming soon.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | CDEMO-MENU-OPT-PGMNAME(WS-OPTION) starts with DUMMY |
| Outcome | redisplay menu - This option ... is coming soon ... |
| Messages | is coming soon ... |
| Implemented at | COMEN01C  `app/cbl/COMEN01C.cbl:169-176` |
| Batch review | confirmed: Message built as 'This option ' + option name up to the first space + 'is coming soon ...' in green. No COMEN02Y entry currently starts with DUMMY, so this branch is dormant. (`app/cbl/COMEN01C.cbl:169-176`, anchor `WHEN CDEMO-MENU-OPT-PGMNAME(WS-OPTION)(1:5) = 'DUMMY'`) |

### BR-COMEN01C-001

The menu option entered must be numeric, not zero and not greater than the number of configured options (CDEMO-MENU-OPT-COUNT, 11 in COMEN02Y); otherwise the menu is redisplayed with 'Please enter a valid option number...'. Before the test, trailing blanks are dropped and embedded/leading blanks are replaced by zeros, so ' 5' and '5 ' both mean option 5.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | WS-OPTION IS NOT NUMERIC or WS-OPTION > CDEMO-MENU-OPT-COUNT or WS-OPTION = 0 |
| Outcome | Error flag set; menu redisplayed with message; no transfer |
| Messages | Please enter a valid option number... |
| Implemented at | COMEN01C PROCESS-ENTER-KEY `app/cbl/COMEN01C.cbl:127-134` |
| Implemented at | COMEN01C  `app/cbl/COMEN01C.cbl:117-125` |
| Implemented at | COMEN01C  `app/cpy/COMEN02Y.cpy:21` |
| Anchor (verified) | `WS-OPTION > CDEMO-MENU-OPT-COUNT OR` |

### BR-COMEN01C-002

A regular user (CDEMO-USER-TYPE 'U') may not select a menu option flagged admin-only (CDEMO-MENU-OPT-USRTYPE = 'A'); the menu is redisplayed with 'No access - Admin Only option... ' and no transfer happens. In the current COMEN02Y table every option is flagged 'U', so the check never fires with the shipped configuration.

| Item | Value |
|---|---|
| Category | security |
| Confidence | Confirmed |
| Conditions | CDEMO-USRTYP-USER and CDEMO-MENU-OPT-USRTYPE(WS-OPTION) = 'A' |
| Outcome | Error flag set; menu redisplayed with message |
| Messages | No access - Admin Only option... |
| Implemented at | COMEN01C PROCESS-ENTER-KEY `app/cbl/COMEN01C.cbl:136-143` |
| Implemented at | COMEN01C  `app/cpy/COMEN02Y.cpy:25-90` |
| Anchor (verified) | `CDEMO-MENU-OPT-USRTYPE(WS-OPTION) = 'A'` |

### BR-COMEN01C-003

A valid, permitted option whose program is neither COPAUS0C nor a DUMMY placeholder transfers control (XCTL) to the program named in CDEMO-MENU-OPT-PGMNAME for that option, passing the commarea with from-transaction CM00, from-program COMEN01C and program context 0 (first entry). Options 1-10 map to COACTVWC, COACTUPC, COCRDLIC, COCRDSLC, COCRDUPC, COTRN00C, COTRN01C, COTRN02C, CORPT00C, COBIL00C.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | Error flag off and option program not COPAUS0C and not starting 'DUMMY' |
| Outcome | XCTL to option program with CARDDEMO-COMMAREA |
| Implemented at | COMEN01C PROCESS-ENTER-KEY `app/cbl/COMEN01C.cbl:177-187` |
| Implemented at | COMEN01C  `app/cbl/COMEN01C.cbl:144-146` |
| Implemented at | COMEN01C  `app/cpy/COMEN02Y.cpy:25-84` |
| Anchor (verified) | `XCTL PROGRAM(CDEMO-MENU-OPT-PGMNAME(WS-OPTION))` |

### BR-COMEN01C-004

The menu distinguishes first entry from re-entry with CDEMO-PGM-CONTEXT: when entered from another program (context not 1) it sets CDEMO-PGM-REENTER and only displays the menu; screen input is received and acted on only on re-entry. A call without any commarea is sent back to sign-on (COSGN00C).

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | EIBCALEN = 0; or CDEMO-PGM-REENTER false/true |
| Outcome | No commarea: XCTL to COSGN00C. First entry: menu sent. Re-entry: map received and key processed. |
| Implemented at | COMEN01C MAIN-PARA `app/cbl/COMEN01C.cbl:82-92` |
| Anchor (verified) | `IF NOT CDEMO-PGM-REENTER` |

### BR-COMEN01C-005

On the main menu any key other than ENTER or PF3 is rejected: the menu is redisplayed with 'Invalid key pressed. Please see below...' and no option is processed.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | Re-entry and EIBAID not DFHENTER/DFHPF3 |
| Outcome | Menu redisplayed with invalid-key message |
| Messages | Invalid key pressed. Please see below... |
| Implemented at | COMEN01C MAIN-PARA `app/cbl/COMEN01C.cbl:99-102` |
| Implemented at | COMEN01C  `app/cpy/CSMSG01Y.cpy:20-21` |
| Anchor (verified) | `MOVE CCDA-MSG-INVALID-KEY TO WS-MESSAGE` |


## COPAUA0C

Program page: [COPAUA0C](07-programs/COPAUA0C.md).

### BR-COPAUA0C-001

A triggered COPAUA0C task processes request messages until the queue is empty (5-second MQGET wait) or until more than 500 requests (WS-REQSTS-PROCESS-LIMIT) have been processed, committing with CICS SYNCPOINT after each request.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | NO-MORE-MSG-AVAILABLE (MQRC-NO-MSG-AVAILABLE) or WS-MSG-PROCESSED > 500 |
| Outcome | Loop ends; task terminates (DLI TERM, MQCLOSE, CICS RETURN). Remaining messages wait for a new trigger. |
| Implemented at | COPAUA0C 2000-MAIN-PROCESS `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:326-344` |
| Implemented at | COPAUA0C  `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:40-40` |
| Implemented at | COPAUA0C  `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:242-242` |
| Implemented at | COPAUA0C  `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:416-417` |
| Anchor (verified) | `IF WS-MSG-PROCESSED > WS-REQSTS-PROCESS-LIMIT` |

### BR-COPAUA0C-002

Account, customer and IMS summary data are looked up only when the card number is found in the card cross-reference file; the authorization is written to the IMS database (summary update and detail insert) only for cards found in the cross-reference. A response is always returned.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | CARD-FOUND-XREF after CCXREF read by PA-RQ-CARD-NUM |
| Outcome | Card not found: decision runs (declined) and response sent, but no IMS write. |
| Messages | CARD NOT FOUND IN XREF |
| Implemented at | COPAUA0C 5000-PROCESS-AUTH `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:450-465` |
| Anchor (verified) | `IF CARD-FOUND-XREF` |

### BR-COPAUA0C-003

Available credit is the IMS summary credit limit minus the summary credit balance when a pending-authorization summary exists for the account; otherwise it is the account master credit limit minus current balance. The request is declined for insufficient funds when the transaction amount is greater than the available credit, and declined (no reason flag) when neither summary nor account record exists.

| Item | Value |
|---|---|
| Category | calculation |
| Confidence | Confirmed |
| Conditions | FOUND-PAUT-SMRY-SEG -> PA-CREDIT-LIMIT - PA-CREDIT-BALANCE; else FOUND-ACCT-IN-MSTR -> ACCT-CREDIT-LIMIT - ACCT-CURR-BAL; else decline |
| Outcome | DECLINE-AUTH and INSUFFICIENT-FUND set when amount exceeds available; DECLINE-AUTH alone when no account data. |
| Implemented at | COPAUA0C 6000-MAKE-DECISION `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:665-683` |
| Implemented at | COPAUA0C  `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:627-640` |
| Anchor (verified) | `IF WS-TRANSACTION-AMT > WS-AVAILABLE-AMT` |

### BR-COPAUA0C-004

A declined authorization returns response code '05' with approved amount 0; an approved authorization returns response code '00' with the approved amount equal to the full requested transaction amount (no partial approvals).

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | DECLINE-AUTH vs APPROVE-AUTH (default set in 5000-PROCESS-AUTH) |
| Outcome | PA-RL-AUTH-RESP-CODE '05'/'00'; PA-RL-APPROVED-AMT and WS-APPROVED-AMT 0 or PA-RQ-TRANSACTION-AMT. |
| Implemented at | COPAUA0C 6000-MAKE-DECISION `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:685-696` |
| Anchor (verified) | `MOVE '05'                   TO PA-RL-AUTH-RESP-CODE` |

### BR-COPAUA0C-005

Decline reason codes: card, account or customer not found = '3100'; insufficient funds = '4100'; card not active = '4200'; account closed = '4300'; card fraud = '5100'; merchant fraud = '5200'; any other decline = '9000'. Approved responses carry reason '0000'.

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | AUTH-RESP-DECLINED, first true of the decline flags in EVALUATE order |
| Outcome | PA-RL-AUTH-RESP-REASON set; also stored as PA-AUTH-RESP-REASON in the detail segment. |
| Implemented at | COPAUA0C 6000-MAKE-DECISION `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:698-718` |
| Anchor (verified) | `MOVE '4100'         TO PA-RL-AUTH-RESP-REASON` |

### BR-COPAUA0C-006

When writing an authorization, the account's pending summary is created if absent (zeros, account and customer id from xref), its credit and cash limits are refreshed from the account master, and its totals are updated: approved -> approved count +1, approved amount and credit balance + approved amount, cash balance set to 0; declined -> declined count +1 and declined amount + PA-TRANSACTION-AMT. The summary is then replaced or inserted.

| Item | Value |
|---|---|
| Category | calculation |
| Confidence | Confirmed |
| Conditions | Card found in xref; NFOUND/FOUND-PAUT-SMRY-SEG; AUTH-RESP-APPROVED |
| Outcome | DLI REPL or ISRT of PAUTSUM0. |
| Implemented at | COPAUA0C 8400-UPDATE-SUMMARY `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:801-834` |
| Anchor (verified) | `ADD WS-APPROVED-AMT           TO PA-CREDIT-BALANCE` |

### BR-COPAUA0C-007

Each authorization detail is keyed by complemented date and time (PA-AUTH-DATE-9C = 99999 - current YYDDD, PA-AUTH-TIME-9C = 999999999 - HHMMSSmmm) so that the newest authorization sorts first, and its match status starts as 'P' (pending) when approved or 'D' (declined) when declined, with fraud fields blank.

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Inferred |
| Conditions | Card found in xref (detail insert path) |
| Outcome | PAUTDTL1 inserted under PAUTSUM0 for XREF-ACCT-ID. |
| Implemented at | COPAUA0C 8500-INSERT-AUTH `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:871-909` |
| Anchor (verified) | `COMPUTE PA-AUTH-DATE-9C = 99999 - WS-YYDDD` |

### BR-COPAUA0C-008

Every error is logged to TD queue CSSL; errors classified critical (MQ open/get/put failures, unexpected VSAM responses, IMS schedule/read/update/insert failures) terminate the task immediately (DLI TERM, MQCLOSE, CICS RETURN), while not-found conditions and MQ close failures are warnings that let processing continue.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | ERR-LEVEL = 'C' |
| Outcome | 9990-END-ROUTINE: terminate and CICS RETURN; no explicit rollback is issued. |
| Messages | REQ MQ OPEN ERROR; IMS SCHD FAILED; FAILED TO READ REQUEST MQ; FAILED TO READ XREF FILE; IMS GET SUMMARY FAILED; FAILED TO PUT ON REPLY MQ; IMS UPDATE SUMRY FAILED; IMS INSERT DETL FAILED |
| Implemented at | COPAUA0C 9500-LOG-ERROR `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:1001-1010` |
| Implemented at | COPAUA0C  `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl:1016-1022` |
| Anchor (verified) | `IF ERR-CRITICAL` |


## COPAUS0C

Program page: [COPAUS0C](07-programs/COPAUS0C.md).

### BR-COPAUS0C-001

The account id entered on the authorization summary screen is mandatory and must be numeric; otherwise the account is cleared, the error flag is set and a message is shown.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | ACCTIDI blank/low-values, or not numeric |
| Outcome | WS-ACCT-ID = LOW-VALUES, WS-ERR-FLG = 'Y', message shown, no list loaded. |
| Messages | Please enter Acct Id...; Acct Id must be Numeric ... |
| Implemented at | COPAUS0C PROCESS-ENTER-KEY `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:264-284` |
| Anchor (verified) | `IF ACCTIDI OF COPAU0AI IS NOT NUMERIC` |

### BR-COPAUS0C-002

Selecting a listed authorization with 'S' or 's' transfers control to the authorization detail program COPAUS1C, passing the selected authorization key in CDEMO-CPVS-PAU-SELECTED; only the first non-blank selection field of the five rows is honoured and any other selection value is rejected.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | Valid account id and a selection code with a saved authorization key |
| Outcome | XCTL PROGRAM(COPAUS1C) with CARDDEMO-COMMAREA; otherwise message. |
| Messages | Invalid selection. Valid value is S |
| Implemented at | COPAUS0C PROCESS-ENTER-KEY `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:285-332` |
| Anchor (verified) | `MOVE WS-PGM-AUTH-DTL  TO CDEMO-TO-PROGRAM` |

### BR-COPAUS0C-003

Pending authorizations are listed five per page in IMS key order under the account's summary; a page number and the first key of each page are kept in the commarea, and one look-ahead read decides whether a next page exists.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | No error; summary found |
| Outcome | Up to 5 rows populated; CDEMO-CPVS-PAUKEY-LAST, CDEMO-CPVS-PAUKEY-PREV-PG(page), NEXT-PAGE-YES/NO set. |
| Implemented at | COPAUS0C PROCESS-PAGE-FORWARD `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:418-452` |
| Anchor (verified) | `PERFORM UNTIL WS-IDX > 5 OR AUTHS-EOF OR ERR-FLG-ON` |

### BR-COPAUS0C-004

PF7 pages backward only when the current page number is greater than 1, otherwise shows a top-of-list message; PF8 pages forward only when a next page was detected, otherwise shows a bottom-of-list message.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | PF7: CDEMO-CPVS-PAGE-NUM > 1; PF8: NEXT-PAGE-YES |
| Outcome | Page reloaded or message shown. |
| Messages | You are already at the top of the page...; You are already at the bottom of the page... |
| Implemented at | COPAUS0C PROCESS-PF7-KEY `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:365-384` |
| Implemented at | COPAUS0C  `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:391-411` |
| Anchor (verified) | `IF CDEMO-CPVS-PAGE-NUM > 1` |

### BR-COPAUS0C-005

In the authorization list an authorization is shown as approved ('A') when its response code is '00' and as declined ('D') for any other response code.

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | PA-AUTH-RESP-CODE |
| Outcome | WS-AUTH-APRV-STAT shown in PAPRVnnI. |
| Implemented at | COPAUS0C POPULATE-AUTH-LIST `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:536-540` |
| Anchor (verified) | `IF PA-AUTH-RESP-CODE = '00'` |

### BR-COPAUS0C-006

Account-level authorization totals (approved/declined counts and amounts, credit and cash balances) are shown from the IMS pending authorization summary when one exists for the account; otherwise they are shown as zero and no authorization list is loaded.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | FOUND-PAUT-SMRY-SEG |
| Outcome | Summary fields displayed or zero; list loaded only when summary exists. |
| Implemented at | COPAUS0C GATHER-ACCOUNT-DETAILS `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:787-807` |
| Implemented at | COPAUS0C  `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:349-356` |
| Anchor (verified) | `MOVE PA-APPROVED-AUTH-CNT   TO WS-DISPLAY-COUNT` |

### BR-COPAUS0C-007

PF3 returns to the main menu program COMEN01C; any key other than ENTER, PF3, PF7 or PF8 is rejected with the common invalid-key message. When no target program is set, return defaults to the sign-on program COSGN00C.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | EIBAID |
| Outcome | XCTL to COMEN01C (or COSGN00C) or message CCDA-MSG-INVALID-KEY. |
| Implemented at | COPAUS0C MAIN-PARA `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:224-250` |
| Implemented at | COPAUS0C  `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:668-670` |
| Anchor (verified) | `MOVE WS-PGM-MENU        TO CDEMO-TO-PROGRAM` |

### BR-COPAUS0C-008

When entered from another CardDemo program, the account id passed in the commarea is used to load the screen immediately if it is numeric; otherwise the account field is left blank and nothing is loaded.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | NOT CDEMO-PGM-REENTER and CDEMO-ACCT-ID numeric |
| Outcome | WS-ACCT-ID/ACCTIDO set and details gathered. |
| Implemented at | COPAUS0C MAIN-PARA `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:207-213` |
| Anchor (verified) | `IF CDEMO-ACCT-ID IS NUMERIC` |

### BR-COPAUS0C-009

Unexpected IMS statuses while reading the summary or detail segments set the error flag, stop further list loading and display a system-error message with the IMS status code.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | DIBSTAT not OK, 'GE' or 'GB' |
| Outcome | WS-ERR-FLG = 'Y', message, screen sent. |
| Messages | System error while reading AUTH Details: Code:;  System error while repos. AUTH Details: Code:;  System error while reading AUTH Summary: Code: |
| Implemented at | COPAUS0C GET-AUTHORIZATIONS `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:467-483` |
| Implemented at | COPAUS0C  `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:500-517` |
| Implemented at | COPAUS0C  `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:980-995` |
| Anchor (verified) | `' System error while reading AUTH Details: Code:'` |


## COPAUS1C

Program page: [COPAUS1C](07-programs/COPAUS1C.md).

### BR-COPAUS1C-001

An authorization detail is displayed only when the commarea carries a numeric account id and a non-blank selected authorization key; otherwise the error flag is set and the detail fields are left empty.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | CDEMO-ACCT-ID numeric and CDEMO-CPVD-PAU-SELECTED not spaces/low-values |
| Outcome | Read and display, or ERR-FLG-ON (no display). |
| Implemented at | COPAUS1C PROCESS-ENTER-KEY `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:211-224` |
| Anchor (verified) | `IF CDEMO-ACCT-ID IS NUMERIC AND` |

### BR-COPAUS1C-002

PF5 toggles the fraud status of the displayed authorization: if it is currently confirmed fraud ('F') it becomes fraud removed ('R') and the action sent to COPAUS2C is remove; otherwise it becomes confirmed fraud ('F') and the action is report.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | PA-FRAUD-CONFIRMED |
| Outcome | PA-AUTH-FRAUD and WS-FRD-ACTION set before LINK to COPAUS2C. |
| Implemented at | COPAUS1C MARK-AUTH-FRAUD `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:236-242` |
| Anchor (verified) | `SET PA-FRAUD-REMOVED          TO TRUE` |

### BR-COPAUS1C-003

The IMS detail is updated with the new fraud status only when COPAUS2C has recorded the fraud action in DB2 successfully; if the LINK fails or COPAUS2C reports failure, the unit of work is rolled back and COPAUS2C's message is shown. A failed IMS replace also rolls back both updates.

| Item | Value |
|---|---|
| Category | data-integrity |
| Confidence | Confirmed |
| Conditions | EIBRESP NORMAL and WS-FRD-UPDATE-STATUS = 'S'; then DLI REPL status OK |
| Outcome | SYNCPOINT with 'AUTH FRAUD REMOVED...' / 'AUTH MARKED FRAUD...', or SYNCPOINT ROLLBACK with error message. |
| Messages | AUTH FRAUD REMOVED...; AUTH MARKED FRAUD...;  System error while FRAUD Tagging, ROLLBACK\|\| |
| Implemented at | COPAUS1C MARK-AUTH-FRAUD `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:253-262` |
| Implemented at | COPAUS1C  `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:531-551` |
| Anchor (verified) | `IF WS-FRD-UPDT-SUCCESS` |

### BR-COPAUS1C-004

The response is displayed as 'A' in green when the response code is '00' and 'D' in red otherwise; the reason code is decoded through a sorted table (0000 APPROVED, 3100 INVALID CARD, 4100 INSUFFICNT FUND, 4200 CARD NOT ACTIVE, 4300 ACCOUNT CLOSED, 4400 EXCED DAILY LMT, 5100 CARD FRAUD, 5200 MERCHANT FRAUD, 5300 LOST CARD, 9000 UNKNOWN) and shown as '9999-ERROR' when not in the table.

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | PA-AUTH-RESP-CODE, PA-AUTH-RESP-REASON |
| Outcome | AUTHRSPO/AUTHRSPC and AUTHRSNO populated. |
| Implemented at | COPAUS1C POPULATE-AUTH-DETAILS `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:311-328` |
| Implemented at | COPAUS1C  `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:56-73` |
| Anchor (verified) | `SEARCH ALL WS-DECLINE-REASON-TAB` |

### BR-COPAUS1C-005

The fraud field shows the fraud flag and the fraud report date only when the authorization is confirmed fraud or fraud removed; otherwise it shows '-'.

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | PA-AUTH-FRAUD in ('F','R') |
| Outcome | AUTHFRDO = flag '-' report date, or '-'. |
| Implemented at | COPAUS1C POPULATE-AUTH-DETAILS `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:344-350` |
| Anchor (verified) | `IF PA-FRAUD-CONFIRMED OR PA-FRAUD-REMOVED` |

### BR-COPAUS1C-006

PF8 shows the next pending authorization of the same account in IMS key order; when there is none the current one stays and the message 'Already at the last Authorization...' is shown.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | AUTHS-EOF after GNP |
| Outcome | Next detail displayed and CDEMO-CPVD-PAU-SELECTED updated, or message. |
| Messages | Already at the last Authorization... |
| Implemented at | COPAUS1C PROCESS-PF8-KEY `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:281-287` |
| Implemented at | COPAUS1C  `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:501-517` |
| Anchor (verified) | `'Already at the last Authorization...'` |

### BR-COPAUS1C-007

Unexpected IMS statuses on reading the summary or the selected detail set the error flag and display a system-error message with the IMS code; a missing summary or detail ('GE'/'GB') is treated as end of data.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | DIBSTAT not OK/'GE'/'GB' |
| Outcome | WS-ERR-FLG = 'Y', message, screen sent. |
| Messages | System error while reading Auth Summary: Code:;  System error while reading Auth Details: Code: |
| Implemented at | COPAUS1C READ-AUTH-RECORD `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:446-488` |
| Anchor (verified) | `' System error while reading Auth Summary: Code:'` |

### BR-COPAUS1C-008

PF3, or entry without a commarea, returns to the authorization summary program COPAUS0C.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | EIBCALEN = 0 or EIBAID = DFHPF3 |
| Outcome | XCTL to COPAUS0C with CDEMO-PGM-ENTER. |
| Implemented at | COPAUS1C MAIN-PARA `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:164-185` |
| Anchor (verified) | `MOVE WS-PGM-AUTH-SMRY     TO CDEMO-TO-PROGRAM` |


## COPAUS2C

Program page: [COPAUS2C](07-programs/COPAUS2C.md).

### BR-COPAUS2C-001

A fraud report/removal is recorded in DB2 table AUTHFRDS as an insert of the full authorization; if a row already exists for the same card number and authorization timestamp (SQLCODE -803), only its fraud flag and fraud report date are updated.

| Item | Value |
|---|---|
| Category | data-integrity |
| Confidence | Confirmed |
| Conditions | INSERT SQLCODE 0 / -803 / other |
| Outcome | Row inserted or AUTH_FRAUD/FRAUD_RPT_DATE updated; WS-FRD-UPDATE-STATUS 'S' or 'F'. |
| Messages | ADD SUCCESS; UPDT SUCCESS |
| Implemented at | COPAUS2C MAIN-PARA `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:199-216` |
| Implemented at | COPAUS2C  `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:141-198` |
| Implemented at | COPAUS2C  `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:222-229` |
| Anchor (verified) | `IF SQLCODE = -803` |

### BR-COPAUS2C-002

The DB2 authorization timestamp is built from the original authorization date (YYMMDD from the request) and the time recovered from the complemented key (999999999 - PA-AUTH-TIME-9C = HHMMSSmmm), formatted 'YY-MM-DD HH.MI.SSmmm000' and converted with TIMESTAMP_FORMAT.

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | Always |
| Outcome | AUTH-TS host variable set; part of the AUTHFRDS primary key with CARD_NUM. |
| Implemented at | COPAUS2C MAIN-PARA `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:103-114` |
| Implemented at | COPAUS2C  `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:171-172` |
| Anchor (verified) | `COMPUTE WS-AUTH-TIME = 999999999 - PA-AUTH-TIME-9C` |

### BR-COPAUS2C-003

Any DB2 error other than duplicate key on insert, or any error on the update, is returned to the caller as failure ('F') with the SQLCODE and SQLSTATE in the message; the caller decides to roll back.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | SQLCODE not 0 (and not -803 on insert) |
| Outcome | WS-FRD-UPDT-FAILED, WS-FRD-ACT-MSG set. |
| Messages | SYSTEM ERROR DB2: CODE:;  UPDT ERROR DB2: CODE: |
| Implemented at | COPAUS2C FRAUD-UPDATE `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:230-243` |
| Implemented at | COPAUS2C  `app/app-authorization-ims-db2-mq/cbl/COPAUS2C.cbl:205-214` |
| Anchor (verified) | `' UPDT ERROR DB2: CODE:'` |


## CORPT00C

Program page: [CORPT00C](07-programs/CORPT00C.md).

### BR-CORPT00C-001

Without a commarea the program returns to the sign-on program COSGN00C. On first entry it shows the report selection screen; afterwards ENTER processes the request, PF3 returns to the main menu COMEN01C and any other key shows 'Invalid key pressed. Please see below...'.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | EIBCALEN, CDEMO-PGM-REENTER, EIBAID |
| Outcome | XCTL to COSGN00C/COMEN01C, screen sent, or invalid-key message |
| Messages | Invalid key pressed. Please see below... |
| Implemented at | CORPT00C MAIN-PARA `app/cbl/CORPT00C.cbl:172-196` |
| Implemented at | CORPT00C  `app/cpy/CSMSG01Y.cpy:20-21` |
| Anchor (verified) | `MOVE 'COMEN01C' TO CDEMO-TO-PROGRAM` |

### BR-CORPT00C-002

Monthly report: the reporting period runs from the first day of the current month (YYYY-MM-01) to the last day of the current month, computed as the day before the first day of the next month (with year roll-over after December).

| Item | Value |
|---|---|
| Category | calculation |
| Confidence | Confirmed |
| Conditions | Monthly selection field not spaces/low-values (checked first) |
| Outcome | PARM-START-DATE-1/2 and PARM-END-DATE-1/2 set; SUBMIT-JOB-TO-INTRDR |
| Implemented at | CORPT00C PROCESS-ENTER-KEY `app/cbl/CORPT00C.cbl:212-237` |
| Anchor (verified) | `COMPUTE WS-CURDATE-N = FUNCTION DATE-OF-INTEGER( FUNCTION INTEGER-OF-DATE(WS-CURDATE-N) - 1)` |

### BR-CORPT00C-003

Yearly report: the reporting period is January 1 to December 31 of the current year. It applies only when Monthly is not selected.

| Item | Value |
|---|---|
| Category | calculation |
| Confidence | Confirmed |
| Conditions | Yearly selection field not spaces/low-values and Monthly blank |
| Outcome | Dates YYYY-01-01 / YYYY-12-31 set; SUBMIT-JOB-TO-INTRDR |
| Implemented at | CORPT00C PROCESS-ENTER-KEY `app/cbl/CORPT00C.cbl:239-254` |
| Anchor (verified) | `MOVE '12' TO WS-END-DATE-MM` |

### BR-CORPT00C-004

Custom report: start month, start day, start year, end month, end day and end year are all required, checked in that order; the first empty one is reported ('Start Date - Month can NOT be empty...' etc.) and processing stops.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | Custom selected (Monthly and Yearly blank) and a date part is spaces/low-values |
| Outcome | Error message, cursor on field, screen sent, task ends |
| Messages | Start Date - Month can NOT be empty...; Start Date - Day can NOT be empty...; Start Date - Year can NOT be empty...; End Date - Month can NOT be empty...; End Date - Day can NOT be empty...; End Date - Year can NOT be empty... |
| Implemented at | CORPT00C PROCESS-ENTER-KEY `app/cbl/CORPT00C.cbl:256-303` |
| Anchor (verified) | `MOVE 'Start Date - Month can NOT be empty...'` |

### BR-CORPT00C-005

Custom report dates: each part is converted with NUMVAL-C; month must be numeric and not greater than 12, day numeric and not greater than 31, and year numeric, for both start and end date; the first failure is reported ('Start Date - Not a valid Month...' etc.).

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | Converted date part not numeric or out of range |
| Outcome | Error message, screen sent, task ends |
| Messages | Start Date - Not a valid Month...; Start Date - Not a valid Day...; Start Date - Not a valid Year...; End Date - Not a valid Month...; End Date - Not a valid Day...; End Date - Not a valid Year... |
| Implemented at | CORPT00C PROCESS-ENTER-KEY `app/cbl/CORPT00C.cbl:304-378` |
| Anchor (verified) | `IF SDTMMI OF CORPT0AI IS NOT NUMERIC OR SDTMMI OF CORPT0AI > '12'` |

### BR-CORPT00C-006

Custom start and end dates (YYYY-MM-DD) must be valid calendar dates according to CSUTLDTC/CEEDAYS. A non-zero severity is rejected ('Start Date - Not a valid date...' / 'End Date - Not a valid date...') except when the CEEDAYS message number is 2513, which is accepted.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | CSUTLDTC-RESULT-SEV-CD not '0000' and CSUTLDTC-RESULT-MSG-NUM not '2513' |
| Outcome | Error message, screen sent, task ends |
| Messages | Start Date - Not a valid date...; End Date - Not a valid date... |
| Implemented at | CORPT00C PROCESS-ENTER-KEY `app/cbl/CORPT00C.cbl:386-426` |
| Implemented at | CORPT00C  `app/cbl/CSUTLDTC.cbl:62-70` |
| Anchor (verified) | `IF CSUTLDTC-RESULT-MSG-NUM NOT = '2513'` |

### BR-CORPT00C-007

A custom report is submitted only when no validation error was raised; on success of any report the selection fields are cleared and '<Monthly|Yearly|Custom> report submitted for printing ...' is shown in green.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | ERR-FLG-OFF |
| Outcome | SUBMIT-JOB-TO-INTRDR; success message with DFHGREEN |
| Messages | report submitted for printing ... |
| Implemented at | CORPT00C PROCESS-ENTER-KEY `app/cbl/CORPT00C.cbl:429-455` |
| Anchor (verified) | `' report submitted for printing ...'` |

### BR-CORPT00C-008

If none of Monthly, Yearly or Custom is selected, the request is rejected with 'Select a report type to print report...'. The selection fields are evaluated in priority order Monthly, Yearly, Custom.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | All three selection fields blank |
| Outcome | Error message, cursor on Monthly, screen sent |
| Messages | Select a report type to print report... |
| Implemented at | CORPT00C PROCESS-ENTER-KEY `app/cbl/CORPT00C.cbl:437-442` |
| Anchor (verified) | `MOVE 'Select a report type to print report...' TO WS-MESSAGE` |

### BR-CORPT00C-009

The report job is submitted only after explicit confirmation: a blank CONFIRM field asks 'Please confirm to print the <name> report...'; 'N' or 'n' cancels and clears the screen; any value other than 'Y'/'y'/'N'/'n' is rejected with '"<value>" is not a valid value to confirm...'.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | CONFIRMI value |
| Outcome | Prompt, cancel, error, or continue to job submission |
| Messages | Please confirm to print the ; " is not a valid value to confirm... |
| Implemented at | CORPT00C SUBMIT-JOB-TO-INTRDR `app/cbl/CORPT00C.cbl:464-493` |
| Anchor (verified) | `WHEN CONFIRMI OF CORPT0AI = 'Y' OR 'y'` |

### BR-CORPT00C-010

Job submission: the in-storage JCL deck (job TRNRPT00, JCLLIB AWS.M2.CARDDEMO.PROC, EXEC PROC=TRANREPT, SYMNAMES TRAN-CARD-NUM,263,16,ZD and TRAN-PROC-DT,305,10,CH, PARM-START-DATE/PARM-END-DATE symbols and a DATEPARM card with start and end date) is written one 80-byte line at a time to TDQ 'JOBS', up to and including the first line that is '/*EOF', spaces or low-values (maximum 1000 lines) or until an error occurs.

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | Confirmed with Y/y and no error |
| Outcome | EXEC CICS WRITEQ TD QUEUE('JOBS') for each JCL line |
| Implemented at | CORPT00C SUBMIT-JOB-TO-INTRDR `app/cbl/CORPT00C.cbl:496-508` |
| Implemented at | CORPT00C  `app/cbl/CORPT00C.cbl:81-127` |
| Implemented at | CORPT00C  `app/cbl/CORPT00C.cbl:515-523` |
| Anchor (verified) | `IF JCL-RECORD = '/*EOF' OR JCL-RECORD = SPACES OR LOW-VALUES` |

### BR-CORPT00C-011

If any write to TDQ 'JOBS' fails, the RESP/RESP2 codes are DISPLAYed, the error flag is set and 'Unable to Write TDQ (JOBS)...' is shown; lines already written are not removed.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | WRITEQ TD response not NORMAL |
| Outcome | Error message; task ends via SEND-TRNRPT-SCREEN |
| Messages | Unable to Write TDQ (JOBS)... |
| Implemented at | CORPT00C WIRTE-JOBSUB-TDQ `app/cbl/CORPT00C.cbl:524-535` |
| Anchor (verified) | `MOVE 'Unable to Write TDQ (JOBS)...' TO WS-MESSAGE` |

### BR-CORPT00C-012

When returning to a previous screen and no target program is set, the sign-on program COSGN00C is used.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | CDEMO-TO-PROGRAM blank |
| Outcome | XCTL to COSGN00C |
| Implemented at | CORPT00C RETURN-TO-PREV-SCREEN `app/cbl/CORPT00C.cbl:542-551` |
| Anchor (verified) | `IF CDEMO-TO-PROGRAM = LOW-VALUES OR SPACES` |


## COSGN00C

Program page: [COSGN00C](07-programs/COSGN00C.md).

### BR-BASE-COSGN00C-001

Sign-on stops before the password is checked when the entered user id is spaces or low-values, and the screen is redisplayed with 'Please enter User ID ...'.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | USERIDI OF COSGN0AI = spaces or low-values |
| Outcome | redisplay sign-on screen - Please enter User ID ... |
| Messages | Please enter User ID ... |
| Implemented at | COSGN00C PROCESS-ENTER-KEY `app/cbl/COSGN00C.cbl:118-122` |
| Batch review | confirmed: Blank user id sets WS-ERR-FLG='Y' and redisplays with 'Please enter User ID ...'; READ-USER-SEC-FILE is then skipped by IF NOT ERR-FLG-ON at 138-140. (`app/cbl/COSGN00C.cbl:118-122`, anchor `WHEN USERIDI OF COSGN0AI = SPACES OR LOW-VALUES`) |

### BR-BASE-COSGN00C-002

Sign-on stops when a user id is present and the password is spaces or low-values, and the screen is redisplayed with 'Please enter Password ...'.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | PASSWDI OF COSGN0AI = spaces or low-values |
| Outcome | redisplay sign-on screen - Please enter Password ... |
| Messages | Please enter Password ... |
| Implemented at | COSGN00C PROCESS-ENTER-KEY `app/cbl/COSGN00C.cbl:123-127` |
| Batch review | confirmed: Second WHEN of EVALUATE TRUE, so only evaluated when user id is present; message 'Please enter Password ...'. (`app/cbl/COSGN00C.cbl:123-127`, anchor `WHEN PASSWDI OF COSGN0AI = SPACES OR LOW-VALUES`) |

### BR-BASE-COSGN00C-003

The entered user id and password are converted to upper case before the user-security file is read and the password is compared.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Outcome | upper-case USERIDI into WS-USER-ID and PASSWDI into WS-USER-PWD |
| Implemented at | COSGN00C PROCESS-ENTER-KEY `app/cbl/COSGN00C.cbl:132-136` |
| Batch review | confirmed: User id is upper-cased into WS-USER-ID and CDEMO-USER-ID, password into WS-USER-PWD; the conversion happens even when the error flag is on, but the read is skipped then. (`app/cbl/COSGN00C.cbl:132-136`, anchor `MOVE FUNCTION UPPER-CASE(PASSWDI OF COSGN0AI) TO`) |

### BR-BASE-COSGN00C-004

Sign-on is refused when the stored password does not equal the upper-cased entered password, and the screen is redisplayed with 'Wrong Password. Try again ...'.

| Item | Value |
|---|---|
| Category | authorization |
| Confidence | Confirmed |
| Conditions | SEC-USR-PWD != |
| Outcome | redisplay sign-on screen - Wrong Password. Try again ... |
| Messages | Wrong Password. Try again ... |
| Implemented at | COSGN00C READ-USER-SEC-FILE `app/cbl/COSGN00C.cbl:241-246` |
| Batch review | confirmed: ELSE branch of IF SEC-USR-PWD = WS-USER-PWD (line 223). Note WS-ERR-FLG is not set in this branch (no functional effect, screen already sent). (`app/cbl/COSGN00C.cbl:241-246`, anchor `MOVE 'Wrong Password. Try again ...' TO`) |

### BR-BASE-COSGN00C-005

A matching password transfers an admin user to COADM01C and any other user to COMEN01C. Admin means CDEMO-USER-TYPE equals 'A'.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | CDEMO-USRTYP-ADMIN 88-level A |
| Outcome | XCTL; XCTL |
| Implemented at | COSGN00C READ-USER-SEC-FILE `app/cbl/COSGN00C.cbl:223-239` |
| Batch review | confirmed: CDEMO-USRTYP-ADMIN is the 88-level VALUE 'A' on CDEMO-USER-TYPE (app/cpy/COCOM01Y.cpy:26-27); any other value, including values other than 'U', goes to COMEN01C. (`app/cbl/COSGN00C.cbl:223-239`, anchor `IF CDEMO-USRTYP-ADMIN`) |

### BR-BASE-COSGN00C-006

A user-security read response of 13 redisplays sign-on with 'User not found. Try again ...'. Any other non-zero response redisplays sign-on with 'Unable to verify the User ...'.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | WS-RESP-CD = 13 |
| Outcome | redisplay sign-on screen - User not found. Try again ...; redisplay sign-on screen - Unable to verify the User ... |
| Messages | User not found. Try again ...; Unable to verify the User ... |
| Implemented at | COSGN00C READ-USER-SEC-FILE `app/cbl/COSGN00C.cbl:221-256` |
| Batch review | confirmed: WHEN 13 (NOTFND) at 247-251 gives 'User not found. Try again ...'; WHEN OTHER at 252-256 gives 'Unable to verify the User ...'. Both set the error flag and put the cursor on USERID. (`app/cbl/COSGN00C.cbl:221-256`, anchor `WHEN 13`) |

### BR-COSGN00C-001

On the sign-on screen PF3 ends the CardDemo session: the program sends the plain-text message 'Thank you for using CardDemo application...' and returns to CICS without a next transaction; any key other than ENTER or PF3 is rejected and the sign-on screen is redisplayed with 'Invalid key pressed. Please see below...'.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | EIBCALEN not zero and EIBAID = DFHPF3, or EIBAID is neither DFHENTER nor DFHPF3 |
| Outcome | PF3: SEND TEXT + RETURN (session ends). Other key: error flag set, screen redisplayed with invalid-key message. |
| Messages | Thank you for using CardDemo application...; Invalid key pressed. Please see below... |
| Implemented at | COSGN00C MAIN-PARA `app/cbl/COSGN00C.cbl:85-95` |
| Implemented at | COSGN00C  `app/cbl/COSGN00C.cbl:162-172` |
| Implemented at | COSGN00C  `app/cpy/CSMSG01Y.cpy:18-21` |
| Anchor (verified) | `MOVE CCDA-MSG-THANK-YOU TO WS-MESSAGE` |

### BR-COSGN00C-002

On successful sign-on the commarea passed to the menu carries the signed-on user id, the user type copied from SEC-USR-TYPE of the security record, from-transaction CC00, from-program COSGN00C and program context 0 (first entry), so the target menu starts in first-entry mode with the role from the security file.

| Item | Value |
|---|---|
| Category | data-integrity |
| Confidence | Confirmed |
| Conditions | USRSEC read RESP 0 and SEC-USR-PWD = WS-USER-PWD |
| Outcome | CDEMO-FROM-TRANID, CDEMO-FROM-PROGRAM, CDEMO-USER-ID, CDEMO-USER-TYPE set; CDEMO-PGM-CONTEXT = 0 |
| Implemented at | COSGN00C READ-USER-SEC-FILE `app/cbl/COSGN00C.cbl:224-228` |
| Anchor (verified) | `MOVE SEC-USR-TYPE TO CDEMO-USER-TYPE` |


## COTRN00C

Program page: [COTRN00C](07-programs/COTRN00C.md).

### BR-COTRN00C-001

When the program is started without a COMMAREA (EIBCALEN = 0) the user is sent to the sign-on program COSGN00C instead of the transaction list.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | EIBCALEN = 0 |
| Outcome | CDEMO-TO-PROGRAM = 'COSGN00C'; XCTL to COSGN00C. |
| Implemented at | COTRN00C MAIN-PARA `app/cbl/COTRN00C.cbl:107-109` |
| Implemented at | COTRN00C  `app/cbl/COTRN00C.cbl:512-520` |
| Anchor (verified) | `IF EIBCALEN = 0` |

### BR-COTRN00C-002

On re-entry the attention key decides the action: Enter processes selection/filter, PF3 returns to the main menu COMEN01C, PF7 pages backward, PF8 pages forward; any other key is rejected with the invalid-key message and the list is redisplayed.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | CDEMO-PGM-REENTER and EIBAID value |
| Outcome | DFHENTER -> PROCESS-ENTER-KEY; DFHPF3 -> XCTL COMEN01C; DFHPF7 -> PROCESS-PF7-KEY; DFHPF8 -> PROCESS-PF8-KEY; other -> WS-ERR-FLG 'Y', CCDA-MSG-INVALID-KEY shown. |
| Messages | Invalid key pressed. Please see below... |
| Implemented at | COTRN00C MAIN-PARA `app/cbl/COTRN00C.cbl:119-134` |
| Anchor (verified) | `MOVE 'COMEN01C' TO CDEMO-TO-PROGRAM` |

### BR-COTRN00C-003

Only one row selection is honoured per Enter: the selection fields are tested in screen order SEL0001I to SEL0010I and the first non-blank one is taken together with the Tran ID of the same row; if none is filled the stored selection is cleared.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | SELnnnnI not SPACES/LOW-VALUES, evaluated from row 1 to row 10 |
| Outcome | CDEMO-CT00-TRN-SEL-FLG = selection value, CDEMO-CT00-TRN-SELECTED = TRNIDnnI of that row; otherwise both set to SPACES. |
| Implemented at | COTRN00C PROCESS-ENTER-KEY `app/cbl/COTRN00C.cbl:148-181` |
| Anchor (verified) | `WHEN SEL0001I OF COTRN0AI NOT = SPACES AND LOW-VALUES` |

### BR-COTRN00C-004

The only valid row selection code is 'S' (upper or lower case). A valid selection on a row with a Tran ID transfers control to the transaction view program COTRN01C with the selected Tran ID in the COMMAREA; any other code is rejected with a message and the list is refreshed.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | CDEMO-CT00-TRN-SEL-FLG and CDEMO-CT00-TRN-SELECTED both not blank; flag = 'S' or 's' |
| Outcome | 'S'/'s': CDEMO-FROM-TRANID = CT00, CDEMO-FROM-PROGRAM = COTRN00C, CDEMO-PGM-CONTEXT = 0, XCTL COTRN01C. Other: WS-MESSAGE 'Invalid selection. Valid value is S' (error flag not set; list processing continues). |
| Messages | Invalid selection. Valid value is S |
| Implemented at | COTRN00C PROCESS-ENTER-KEY `app/cbl/COTRN00C.cbl:183-203` |
| Anchor (verified) | `MOVE 'COTRN01C'   TO CDEMO-TO-PROGRAM` |

### BR-COTRN00C-005

The optional start Tran ID entered on the screen must be numeric. Blank means list from the start of the file; a numeric value positions the list at that Tran ID; a non-numeric value is rejected.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | TRNIDINI blank / numeric / not numeric |
| Outcome | Blank: TRAN-ID = LOW-VALUES. Numeric: TRAN-ID = TRNIDINI. Not numeric: WS-ERR-FLG 'Y', message 'Tran ID must be Numeric ...', screen sent. |
| Messages | Tran ID must be Numeric ... |
| Implemented at | COTRN00C PROCESS-ENTER-KEY `app/cbl/COTRN00C.cbl:206-219` |
| Anchor (verified) | `IF TRNIDINI  OF COTRN0AI IS NUMERIC` |

### BR-COTRN00C-006

Every Enter (and the first display) restarts paging: the page number is reset to 0 before the forward page read, so the first page shown is page 1.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | Enter key or first entry |
| Outcome | CDEMO-CT00-PAGE-NUM = 0, then PROCESS-PAGE-FORWARD increments it. |
| Implemented at | COTRN00C PROCESS-ENTER-KEY `app/cbl/COTRN00C.cbl:224-225` |
| Anchor (verified) | `MOVE 0       TO CDEMO-CT00-PAGE-NUM` |

### BR-COTRN00C-007

PF7 (previous page) is allowed only when the current page number is greater than 1; the backward browse starts at the first Tran ID of the current page (or LOW-VALUES if none is stored). On page 1 the user is told they are already at the top.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | CDEMO-CT00-PAGE-NUM > 1 |
| Outcome | TRAN-ID = CDEMO-CT00-TRNID-FIRST, NEXT-PAGE-YES, PROCESS-PAGE-BACKWARD; else message 'You are already at the top of the page...' sent without erase. |
| Messages | You are already at the top of the page... |
| Implemented at | COTRN00C PROCESS-PF7-KEY `app/cbl/COTRN00C.cbl:236-252` |
| Anchor (verified) | `IF CDEMO-CT00-PAGE-NUM > 1` |

### BR-COTRN00C-008

PF8 (next page) is allowed only when the previous forward read found a record beyond the 10 shown (next-page flag 'Y'); the browse starts at the last Tran ID of the current page (HIGH-VALUES if none is stored). Otherwise the user is told they are already at the bottom.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | NEXT-PAGE-YES (CDEMO-CT00-NEXT-PAGE-FLG = 'Y') |
| Outcome | TRAN-ID = CDEMO-CT00-TRNID-LAST, PROCESS-PAGE-FORWARD; else message 'You are already at the bottom of the page...' sent without erase. |
| Messages | You are already at the bottom of the page... |
| Implemented at | COTRN00C PROCESS-PF8-KEY `app/cbl/COTRN00C.cbl:259-274` |
| Anchor (verified) | `IF NEXT-PAGE-YES` |

### BR-COTRN00C-009

When paging forward with PF8 the record at the start key (the last Tran ID of the previous page) is skipped so it is not repeated; for Enter (filter or first display) the list starts with the record at the start key itself.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | EIBAID not Enter, PF7 or PF3 |
| Outcome | One READNEXT is issued and discarded before filling rows. |
| Implemented at | COTRN00C PROCESS-PAGE-FORWARD `app/cbl/COTRN00C.cbl:284-286` |
| Anchor (verified) | `IF EIBAID NOT = DFHENTER AND DFHPF7 AND DFHPF3` |

### BR-COTRN00C-010

A page holds at most 10 transactions: the 10 rows are cleared and then filled with up to 10 consecutive TRANSACT records in ascending Tran ID order, stopping early at end of file or on error.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | WS-IDX < 11 and not end of file and no error |
| Outcome | Rows 1..n populated via POPULATE-TRAN-DATA; remaining rows blank. |
| Implemented at | COTRN00C PROCESS-PAGE-FORWARD `app/cbl/COTRN00C.cbl:289-303` |
| Anchor (verified) | `PERFORM UNTIL WS-IDX >= 11 OR TRANSACT-EOF OR ERR-FLG-ON` |

### BR-COTRN00C-011

After a forward page fill, the page number is increased by 1 when the page is full and records remain, and a look-ahead read decides whether a next page exists; when end of file was reached during the fill, there is no next page and the page number is increased only if at least one row was shown.

| Item | Value |
|---|---|
| Category | calculation |
| Confidence | Confirmed |
| Conditions | TRANSACT-NOT-EOF and no error after 10 rows; else WS-IDX > 1 |
| Outcome | CDEMO-CT00-PAGE-NUM + 1; NEXT-PAGE-YES if the 11th record exists, otherwise NEXT-PAGE-NO. |
| Implemented at | COTRN00C PROCESS-PAGE-FORWARD `app/cbl/COTRN00C.cbl:305-320` |
| Anchor (verified) | `COMPUTE CDEMO-CT00-PAGE-NUM =` |

### BR-COTRN00C-012

When paging backward with PF7 the record at the start key (the first Tran ID of the current page) is skipped, then up to 10 previous records are read in descending Tran ID order and placed from row 10 up to row 1 so the screen remains in ascending order.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | EIBAID not Enter or PF8 for the skip; WS-IDX > 0 and not end of file and no error for the fill |
| Outcome | Rows filled from WS-IDX 10 down to 1. |
| Implemented at | COTRN00C PROCESS-PAGE-BACKWARD `app/cbl/COTRN00C.cbl:339-357` |
| Anchor (verified) | `IF EIBAID NOT = DFHENTER AND DFHPF8` |

### BR-COTRN00C-013

After a full backward page, a further previous record is read: if it exists and the page number is above 1, the page number is decreased by 1; otherwise the page number is forced to 1. If the backward fill hit the start of the file, the page number is left unchanged.

| Item | Value |
|---|---|
| Category | calculation |
| Confidence | Confirmed |
| Conditions | TRANSACT-NOT-EOF and no error after the fill, NEXT-PAGE-YES, look-ahead READPREV result, CDEMO-CT00-PAGE-NUM > 1 |
| Outcome | CDEMO-CT00-PAGE-NUM - 1 or = 1. |
| Implemented at | COTRN00C PROCESS-PAGE-BACKWARD `app/cbl/COTRN00C.cbl:359-369` |
| Anchor (verified) | `SUBTRACT 1 FROM CDEMO-CT00-PAGE-NUM` |

### BR-COTRN00C-014

Each listed transaction shows its original timestamp date reformatted from YYYY-MM-DD to MM/DD/YY and its amount edited with sign and two decimals (+99999999.99).

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | Every row populated |
| Outcome | WS-TRAN-DATE and WS-TRAN-AMT moved to TDATEnnI / TAMTnnnI. |
| Implemented at | COTRN00C POPULATE-TRAN-DATA `app/cbl/COTRN00C.cbl:383-388` |
| Anchor (verified) | `MOVE WS-TIMESTAMP-DT-YYYY(3:2) TO WS-CURDATE-YY` |

### BR-COTRN00C-015

The Tran ID shown on row 1 is remembered as the page's first key and the Tran ID on row 10 as the page's last key; these keys are the start positions for PF7 and PF8 paging.

| Item | Value |
|---|---|
| Category | data-integrity |
| Confidence | Confirmed |
| Conditions | WS-IDX = 1 or WS-IDX = 10 |
| Outcome | CDEMO-CT00-TRNID-FIRST / CDEMO-CT00-TRNID-LAST updated in the COMMAREA. |
| Implemented at | COTRN00C POPULATE-TRAN-DATA `app/cbl/COTRN00C.cbl:391-393` |
| Implemented at | COTRN00C  `app/cbl/COTRN00C.cbl:437-439` |
| Anchor (verified) | `CDEMO-CT00-TRNID-FIRST` |

### BR-COTRN00C-016

Starting the browse: if no record exists at or after the start key the list is treated as at end and the user sees a top-of-page message; any other failure sets the error flag and shows a lookup-failure message, which stops the page fill.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | WS-RESP-CD after STARTBR |
| Outcome | NOTFND: TRANSACT-EOF, 'You are at the top of the page...'. Other: DISPLAY RESP/REAS, WS-ERR-FLG 'Y', 'Unable to lookup transaction...'. |
| Messages | You are at the top of the page...; Unable to lookup transaction... |
| Implemented at | COTRN00C STARTBR-TRANSACT-FILE `app/cbl/COTRN00C.cbl:602-619` |
| Anchor (verified) | `WHEN DFHRESP(NOTFND)` |

### BR-COTRN00C-017

Reading forward: end of file stops the list with a bottom-of-page message; any other failure sets the error flag and shows a lookup-failure message.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | WS-RESP-CD after READNEXT |
| Outcome | ENDFILE: TRANSACT-EOF and message. Other: WS-ERR-FLG 'Y' and 'Unable to lookup transaction...'. |
| Messages | You have reached the bottom of the page...; Unable to lookup transaction... |
| Implemented at | COTRN00C READNEXT-TRANSACT-FILE `app/cbl/COTRN00C.cbl:636-653` |
| Anchor (verified) | `'You have reached the bottom of the page...'` |

### BR-COTRN00C-018

Reading backward: start of file stops the list with a top-of-page message; any other failure sets the error flag and shows a lookup-failure message.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | WS-RESP-CD after READPREV |
| Outcome | ENDFILE: TRANSACT-EOF and message. Other: WS-ERR-FLG 'Y' and 'Unable to lookup transaction...'. |
| Messages | You have reached the top of the page...; Unable to lookup transaction... |
| Implemented at | COTRN00C READPREV-TRANSACT-FILE `app/cbl/COTRN00C.cbl:670-687` |
| Anchor (verified) | `'You have reached the top of the page...'` |


## COTRN01C

Program page: [COTRN01C](07-programs/COTRN01C.md).

### BR-COTRN01C-001

When started without a COMMAREA (EIBCALEN = 0) the user is sent to the sign-on program COSGN00C.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | EIBCALEN = 0 |
| Outcome | XCTL COSGN00C. |
| Implemented at | COTRN01C MAIN-PARA `app/cbl/COTRN01C.cbl:94-96` |
| Implemented at | COTRN01C  `app/cbl/COTRN01C.cbl:199-207` |
| Anchor (verified) | `IF EIBCALEN = 0` |

### BR-COTRN01C-002

On first entry, when a Tran ID was selected on the transaction list (CDEMO-CT01-TRN-SELECTED not blank), that transaction is looked up and displayed immediately without the user typing it; otherwise an empty view screen is shown.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | NOT CDEMO-PGM-REENTER and CDEMO-CT01-TRN-SELECTED not SPACES/LOW-VALUES |
| Outcome | TRNIDINI = CDEMO-CT01-TRN-SELECTED; PROCESS-ENTER-KEY; screen sent. |
| Implemented at | COTRN01C MAIN-PARA `app/cbl/COTRN01C.cbl:99-109` |
| Anchor (verified) | `IF CDEMO-CT01-TRN-SELECTED NOT =` |

### BR-COTRN01C-003

On re-entry the attention key decides the action: Enter looks up the typed Tran ID; PF3 returns to the program that called this one (CDEMO-FROM-PROGRAM) or to the main menu COMEN01C when unknown; PF4 clears the screen; PF5 goes to the transaction list COTRN00C; any other key shows the invalid-key message.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | EIBAID value; for PF3 whether CDEMO-FROM-PROGRAM is blank |
| Outcome | DFHENTER -> PROCESS-ENTER-KEY; DFHPF3 -> XCTL CDEMO-FROM-PROGRAM or COMEN01C; DFHPF4 -> CLEAR-CURRENT-SCREEN; DFHPF5 -> XCTL COTRN00C; other -> WS-ERR-FLG 'Y', CCDA-MSG-INVALID-KEY. |
| Messages | Invalid key pressed. Please see below... |
| Implemented at | COTRN01C MAIN-PARA `app/cbl/COTRN01C.cbl:112-132` |
| Anchor (verified) | `IF CDEMO-FROM-PROGRAM = SPACES OR LOW-VALUES` |

### BR-COTRN01C-004

A Tran ID is mandatory to view a transaction; no format (numeric) check is applied.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | TRNIDINI = SPACES or LOW-VALUES |
| Outcome | WS-ERR-FLG 'Y', message shown, no file read. |
| Messages | Tran ID can NOT be empty... |
| Implemented at | COTRN01C PROCESS-ENTER-KEY `app/cbl/COTRN01C.cbl:146-156` |
| Anchor (verified) | `'Tran ID can NOT be empty...'` |

### BR-COTRN01C-005

The transaction is read by exact Tran ID; if it does not exist the user is told it was not found, and any other read failure shows a lookup-failure message; in both cases the details are not displayed.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | WS-RESP-CD after READ TRANSACT |
| Outcome | NOTFND: WS-ERR-FLG 'Y', 'Transaction ID NOT found...'. Other: DISPLAY RESP/REAS, WS-ERR-FLG 'Y', 'Unable to lookup Transaction...'. |
| Messages | Transaction ID NOT found...; Unable to lookup Transaction... |
| Implemented at | COTRN01C READ-TRANSACT-FILE `app/cbl/COTRN01C.cbl:280-295` |
| Anchor (verified) | `'Transaction ID NOT found...'` |

### BR-COTRN01C-006

A found transaction is displayed with its amount edited with sign and two decimals (+99999999.99); timestamps and other fields are shown as stored.

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | No error after the read |
| Outcome | TRAN-RECORD fields moved to the COTRN1A detail fields and the screen sent. |
| Implemented at | COTRN01C PROCESS-ENTER-KEY `app/cbl/COTRN01C.cbl:176-191` |
| Anchor (verified) | `MOVE WS-TRAN-AMT      TO TRNAMTI    OF COTRN1AI` |


## COTRN02C

Program page: [COTRN02C](07-programs/COTRN02C.md).

### BR-COTRN02C-001

Without a commarea the program returns to sign-on COSGN00C. On re-entry ENTER processes the add request, PF3 returns to the calling program (or COMEN01C when none is recorded), PF4 clears the screen, PF5 copies the last transaction's data, and any other key shows 'Invalid key pressed. Please see below...'.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | EIBCALEN, CDEMO-PGM-REENTER, EIBAID |
| Outcome | XCTL, clear, copy, process or invalid-key message |
| Messages | Invalid key pressed. Please see below... |
| Implemented at | COTRN02C MAIN-PARA `app/cbl/COTRN02C.cbl:115-152` |
| Implemented at | COTRN02C  `app/cpy/CSMSG01Y.cpy:20-21` |
| Anchor (verified) | `WHEN DFHPF5 PERFORM COPY-LAST-TRAN-DATA` |

### BR-COTRN02C-002

On first entry, if a selected value is present in CDEMO-CT02-TRN-SELECTED of the commarea, it is placed in the card number field and the add request is processed immediately (key lookup and validation).

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | First entry and CDEMO-CT02-TRN-SELECTED not spaces/low-values |
| Outcome | PROCESS-ENTER-KEY performed with the pre-filled card number |
| Implemented at | COTRN02C MAIN-PARA `app/cbl/COTRN02C.cbl:124-129` |
| Anchor (verified) | `MOVE CDEMO-CT02-TRN-SELECTED TO CARDNINI OF COTRN2AI` |

### BR-COTRN02C-003

A transaction is added only after explicit confirmation 'Y' or 'y'. 'N', 'n' or blank does not cancel but asks 'Confirm to add this transaction...'; any other value gives 'Invalid value. Valid values are (Y/N)...'. Confirmation is evaluated only after all key and data validations passed.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | CONFIRMI value |
| Outcome | ADD-TRANSACTION or message with cursor on CONFIRM |
| Messages | Confirm to add this transaction...; Invalid value. Valid values are (Y/N)... |
| Implemented at | COTRN02C PROCESS-ENTER-KEY `app/cbl/COTRN02C.cbl:169-187` |
| Anchor (verified) | `MOVE 'Confirm to add this transaction...'` |

### BR-COTRN02C-004

The transaction must be tied to a card in the card cross-reference: if an account id is entered it must be numeric and exist in CXACAIX, and the cross-reference card number replaces the card field; otherwise a numeric card number must be entered and exist in CCXREF, and its account id is filled in. Account id takes precedence when both are entered; if neither is entered the request is rejected.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | ACTIDINI / CARDNINI entered, numeric, found |
| Outcome | Account and card fields populated from CARD-XREF-RECORD, or error message |
| Messages | Account ID must be Numeric...; Card Number must be Numeric...; Account or Card Number must be entered...; Account ID NOT found...; Card Number NOT found...; Unable to lookup Acct in XREF AIX file...; Unable to lookup Card # in XREF file... |
| Implemented at | COTRN02C VALIDATE-INPUT-KEY-FIELDS `app/cbl/COTRN02C.cbl:195-230` |
| Implemented at | COTRN02C  `app/cbl/COTRN02C.cbl:587-603` |
| Implemented at | COTRN02C  `app/cbl/COTRN02C.cbl:621-637` |
| Anchor (verified) | `MOVE 'Account or Card Number must be entered...' TO WS-MESSAGE` |

### BR-COTRN02C-005

All transaction data fields are mandatory and are checked in this order: type code, category code, source, description, amount, orig date, proc date, merchant id, merchant name, merchant city, merchant zip; the first empty field is reported ('<Field> can NOT be empty...').

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | Field = SPACES or LOW-VALUES |
| Outcome | Error message, cursor on field, task ends |
| Messages | Type CD can NOT be empty...; Category CD can NOT be empty...; Source can NOT be empty...; Description can NOT be empty...; Amount can NOT be empty...; Orig Date can NOT be empty...; Proc Date can NOT be empty...; Merchant ID can NOT be empty...; Merchant Name can NOT be empty...; Merchant City can NOT be empty...; Merchant Zip can NOT be empty... |
| Implemented at | COTRN02C VALIDATE-INPUT-DATA-FIELDS `app/cbl/COTRN02C.cbl:251-320` |
| Anchor (verified) | `MOVE 'Type CD can NOT be empty...' TO WS-MESSAGE` |

### BR-COTRN02C-006

Transaction type code and category code must be numeric.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | TTYPCDI or TCATCDI not numeric |
| Outcome | 'Type CD must be Numeric...' / 'Category CD must be Numeric...' |
| Messages | Type CD must be Numeric...; Category CD must be Numeric... |
| Implemented at | COTRN02C VALIDATE-INPUT-DATA-FIELDS `app/cbl/COTRN02C.cbl:322-337` |
| Anchor (verified) | `WHEN TTYPCDI OF COTRN2AI NOT NUMERIC` |

### BR-COTRN02C-007

The amount must be entered exactly as a sign ('+' or '-'), 8 digits, a decimal point and 2 digits (format -99999999.99); it is then converted with NUMVAL-C and redisplayed as +99999999.99.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | Position 1 not sign, 2-9 not numeric, 10 not '.', 11-12 not numeric |
| Outcome | 'Amount should be in format -99999999.99' |
| Messages | Amount should be in format -99999999.99 |
| Implemented at | COTRN02C VALIDATE-INPUT-DATA-FIELDS `app/cbl/COTRN02C.cbl:339-385` |
| Anchor (verified) | `WHEN TRNAMTI OF COTRN2AI(1:1) NOT EQUAL '-' AND '+'` |

### BR-COTRN02C-008

Origination and processing dates must have the layout YYYY-MM-DD (4 digits, '-', 2 digits, '-', 2 digits).

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | Any position of TORIGDTI/TPROCDTI violates the layout |
| Outcome | 'Orig Date should be in format YYYY-MM-DD' / 'Proc Date should be in format YYYY-MM-DD' |
| Messages | Orig Date should be in format YYYY-MM-DD; Proc Date should be in format YYYY-MM-DD |
| Implemented at | COTRN02C VALIDATE-INPUT-DATA-FIELDS `app/cbl/COTRN02C.cbl:353-381` |
| Anchor (verified) | `MOVE 'Orig Date should be in format YYYY-MM-DD' TO WS-MESSAGE` |

### BR-COTRN02C-009

Origination and processing dates must be valid calendar dates according to CSUTLDTC/CEEDAYS; a non-zero severity is rejected unless the CEEDAYS message number is 2513 (unsupported range), which is accepted.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | CSUTLDTC-RESULT-SEV-CD not '0000' and CSUTLDTC-RESULT-MSG-NUM not '2513' |
| Outcome | 'Orig Date - Not a valid date...' / 'Proc Date - Not a valid date...' |
| Messages | Orig Date - Not a valid date...; Proc Date - Not a valid date... |
| Implemented at | COTRN02C VALIDATE-INPUT-DATA-FIELDS `app/cbl/COTRN02C.cbl:389-427` |
| Implemented at | COTRN02C  `app/cbl/CSUTLDTC.cbl:62-70` |
| Anchor (verified) | `MOVE 'Proc Date - Not a valid date...'` |

### BR-COTRN02C-010

Merchant id must be numeric.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | MIDI not numeric |
| Outcome | 'Merchant ID must be Numeric...' |
| Messages | Merchant ID must be Numeric... |
| Implemented at | COTRN02C VALIDATE-INPUT-DATA-FIELDS `app/cbl/COTRN02C.cbl:430-436` |
| Anchor (verified) | `IF MIDI OF COTRN2AI IS NOT NUMERIC` |

### BR-COTRN02C-011

The new transaction id is the highest TRAN-ID currently in TRANSACT plus 1 (TRAN-ID treated as a 16-digit number); when the file is empty the first id is 1.

| Item | Value |
|---|---|
| Category | calculation |
| Confidence | Confirmed |
| Conditions | Confirmed add |
| Outcome | TRAN-ID = MAX(TRAN-ID) + 1 |
| Implemented at | COTRN02C ADD-TRANSACTION `app/cbl/COTRN02C.cbl:444-451` |
| Implemented at | COTRN02C  `app/cbl/COTRN02C.cbl:684-689` |
| Anchor (verified) | `ADD 1 TO WS-TRAN-ID-N` |

### BR-COTRN02C-012

The new transaction record is built from the screen: type, category, source, description, amount (NUMVAL-C of the entered amount), card number (from the cross-reference lookup), merchant id/name/city/zip, and the 10-character orig/proc dates stored in the 26-character TRAN-ORIG-TS/TRAN-PROC-TS fields.

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | Confirmed add |
| Outcome | TRAN-RECORD populated; WRITE-TRANSACT-FILE |
| Implemented at | COTRN02C ADD-TRANSACTION `app/cbl/COTRN02C.cbl:450-466` |
| Anchor (verified) | `MOVE TPROCDTI OF COTRN2AI TO TRAN-PROC-TS` |

### BR-COTRN02C-013

Writing the transaction: success clears the screen and shows 'Transaction added successfully.  Your Tran ID is <id>.' in green; a duplicate key gives 'Tran ID already exist...'; any other error gives 'Unable to Add Transaction...'.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | CICS WRITE response |
| Outcome | Success or error message |
| Messages | Transaction added successfully. ;  Your Tran ID is ; Tran ID already exist...; Unable to Add Transaction... |
| Implemented at | COTRN02C WRITE-TRANSACT-FILE `app/cbl/COTRN02C.cbl:723-749` |
| Anchor (verified) | `MOVE 'Tran ID already exist...' TO WS-MESSAGE` |

### BR-COTRN02C-014

PF5 pre-fills the data fields with those of the last transaction in TRANSACT (highest TRAN-ID, regardless of account or card) after validating the key fields, and then runs the normal add processing, which still requires confirmation.

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | PF5 and no key-field error |
| Outcome | Screen data fields copied from last TRAN-RECORD; PROCESS-ENTER-KEY |
| Implemented at | COTRN02C COPY-LAST-TRAN-DATA `app/cbl/COTRN02C.cbl:473-494` |
| Anchor (verified) | `MOVE TRAN-MERCHANT-ID TO MIDI OF COTRN2AI` |

### BR-COTRN02C-015

When returning to a previous screen with no target program set, the sign-on program COSGN00C is used.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | CDEMO-TO-PROGRAM blank |
| Outcome | XCTL to COSGN00C |
| Implemented at | COTRN02C RETURN-TO-PREV-SCREEN `app/cbl/COTRN02C.cbl:502-511` |
| Anchor (verified) | `IF CDEMO-TO-PROGRAM = LOW-VALUES OR SPACES` |


## COTRTLIC

Program page: [COTRTLIC](07-programs/COTRTLIC.md).

### BR-COTRTLIC-001

PF3 returns to the calling transaction/program recorded in the commarea; if none is recorded (low-values, spaces or this program itself) it returns to the admin menu CA00 / COADM01C. A CICS SYNCPOINT is taken before the XCTL.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | CCARD-AID-PFK03 |
| Outcome | EXEC CICS XCTL PROGRAM(CDEMO-TO-PROGRAM) with CARDDEMO-COMMAREA. |
| Implemented at | COTRTLIC 0000-MAIN `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:591-625` |
| Implemented at | COTRTLIC  `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:47-49` |
| Anchor (verified) | `MOVE LIT-ADMINTRANID   TO CDEMO-TO-TRANID` |

### BR-COTRTLIC-002

PF10 (confirm) is honoured only when a delete or update confirmation is pending and neither filter nor the selected row number has changed since the confirmation prompt; otherwise PF10 is processed as ENTER (re-validate and re-prompt). PF10 without a pending request is an invalid key and is also treated as ENTER.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | CCARD-AID-PFK10 AND (CA-DELETE-REQUESTED OR CA-UPDATE-REQUESTED) AND FLG-TYPEFILTER-CHANGED-NO AND FLG-DESCFILTER-CHANGED-NO AND FLG-ROW-SELECTION-CHANGED-NO |
| Outcome | Otherwise SET CCARD-AID-ENTER TO TRUE. |
| Implemented at | COTRTLIC 0000-MAIN `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:666-678` |
| Implemented at | COTRTLIC  `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:574-587` |
| Implemented at | COTRTLIC  `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1042-1047` |
| Anchor (verified) | `AND FLG-ROW-SELECTION-CHANGED-NO` |

### BR-COTRTLIC-003

Before any list processing the program verifies DB2 connectivity with a priming query; if it fails, the formatted DB2 error is sent as plain text and the conversation ends.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | WS-DB2-ERROR after 9998-PRIMING-QUERY |
| Outcome | SEND TEXT WS-LONG-MSG and EXEC CICS RETURN (no TRANSID). |
| Messages | Db2 access failure. |
| Implemented at | COTRTLIC 0000-MAIN `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:684-691` |
| Implemented at | COTRTLIC  `app/app-transaction-type-db2/cpy/CSDB2RPY.cpy:21-46` |
| Anchor (verified) | `PERFORM SEND-LONG-TEXT` |

### BR-COTRTLIC-004

When any input edit fails, the screen is redisplayed with the error message; the current page is re-read from its first key only if neither filter is in error, so rows are not shown for an invalid or non-matching filter.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | INPUT-ERROR |
| Outcome | WS-RETURN-MSG to CCARD-ERROR-MSG; optional 8000-READ-FORWARD; 2000-SEND-MAP; COMMON-RETURN. |
| Implemented at | COTRTLIC 0000-MAIN `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:698-720` |
| Anchor (verified) | `WHEN INPUT-ERROR` |

### BR-COTRTLIC-005

Paging: PF8 moves to the next page only when CA-NEXT-PAGE-EXISTS, starting at WS-CA-LAST-TR-CODE (the first row of the next page) and incrementing the page number; PF7 on page 1 re-reads the first page ('No previous pages to display'); PF7 on later pages decrements the page number and reads backwards from WS-CA-FIRST-TR-CODE. Row selections are cleared when paging.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | CCARD-AID-PFK07 / CCARD-AID-PFK08 with CA-FIRST-PAGE / CA-NEXT-PAGE-EXISTS |
| Outcome | 8000-READ-FORWARD or 8100-READ-BACKWARDS, INITIALIZE WS-EDIT-SELECT-FLAGS, 2000-SEND-MAP. |
| Implemented at | COTRTLIC 0000-MAIN `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:721-790` |
| Implemented at | COTRTLIC  `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:657-661` |
| Anchor (verified) | `AND CA-NEXT-PAGE-EXISTS` |

### BR-COTRTLIC-006

Deleting a transaction type is a two-step action: ENTER with a 'D' selection redisplays the page and asks for confirmation; PF10 with the 'D' selection performs the DELETE. After a successful delete the screen shows the result and the list state is reset so the next interaction starts from the first page.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | CCARD-AID-ENTER or CCARD-AID-PFK10, WS-DELETES-REQUESTED > 0, CDEMO-FROM-PROGRAM = 'COTRTLIC' |
| Outcome | ENTER: prompt 'Delete HIGHLIGHTED row ? Press F10 to confirm'. PF10: 9300-DELETE-RECORD; on success FLG-DELETED-YES, send map, then INITIALIZE commarea and set first page. |
| Messages | Delete HIGHLIGHTED row ? Press F10 to confirm |
| Implemented at | COTRTLIC 0000-MAIN `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:794-834` |
| Implemented at | COTRTLIC  `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1514-1522` |
| Anchor (verified) | `PERFORM 9300-DELETE-RECORD` |

### BR-COTRTLIC-007

Updating a transaction type description is a two-step action: ENTER with a 'U' selection validates the new description and asks for confirmation; PF10 performs the UPDATE and then re-reads and redisplays the current page.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | CCARD-AID-ENTER or CCARD-AID-PFK10, WS-UPDATES-REQUESTED > 0, CDEMO-FROM-PROGRAM = 'COTRTLIC' |
| Outcome | ENTER: prompt 'Update HIGHLIGHTED row. Press F10 to save'. PF10: 9200-UPDATE-RECORD; on success FLG-UPDATE-COMPLETED; 8000-READ-FORWARD; 2000-SEND-MAP. |
| Messages | Update HIGHLIGHTED row. Press F10 to save |
| Implemented at | COTRTLIC 0000-MAIN `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:838-868` |
| Implemented at | COTRTLIC  `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1523-1531` |
| Anchor (verified) | `PERFORM 9200-UPDATE-RECORD` |

### BR-COTRTLIC-008

A row description entered as '*' or all spaces is treated as not supplied (LOW-VALUES); any other entry is trimmed of leading and trailing spaces before validation and update.

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | TRTYPDI(I) = '*' or SPACES |
| Outcome | WS-ROW-TR-DESC-IN(I) = LOW-VALUES, else FUNCTION TRIM(TRTYPDI(I)). |
| Implemented at | COTRTLIC 1100-RECEIVE-SCREEN `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:944-951` |
| Anchor (verified) | `IF   TRTYPDI(I) = LIT-ASTERISK` |

### BR-COTRTLIC-009

The only valid row action codes are 'D' (delete) and 'U' (update); blank means no action. Any other code marks the row in error and rejects the input with 'Action code selected is invalid'. A 'U' row triggers the description edit.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | WS-EDIT-SELECT(I) not in ('D','U',' ',LOW-VALUES) |
| Outcome | INPUT-ERROR, WS-ROW-TRTSELECT-ERROR(I) = '1', FLG-BAD-ACTIONS-SELECTED-YES. |
| Messages | Action code selected is invalid |
| Implemented at | COTRTLIC 1210-EDIT-ARRAY `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1021-1039` |
| Implemented at | COTRTLIC  `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:180-188` |
| Anchor (verified) | `SET WS-MESG-INVALID-ACTION-CODE      TO TRUE` |

### BR-COTRTLIC-010

Only one row action may be requested per screen: if more than one select field is non-blank, the input is rejected with 'Please select only 1 action' and the selected rows are flagged in error.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | WS-ACTIONS-REQUESTED = 7 - count(blank selects) in 2 THRU 7 (WS-MORETHAN1ACTION) |
| Outcome | INPUT-ERROR with message 'Please select only 1 action'. |
| Messages | Please select only 1 action |
| Implemented at | COTRTLIC 1210-EDIT-ARRAY `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1049-1052` |
| Implemented at | COTRTLIC  `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:997-1012` |
| Implemented at | COTRTLIC  `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1022-1027` |
| Anchor (verified) | `SET WS-MESG-MORE-THAN-1-ACTION           TO TRUE` |

### BR-COTRTLIC-011

Intended rule: if either filter was changed, all row selections are discarded and no row action is processed. As coded the change flags are evaluated before the filter edits set them, so this reset does not take effect (see observation).

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Inferred |
| Conditions | FLG-TYPEFILTER-CHANGED-YES OR FLG-DESCFILTER-CHANGED-YES |
| Outcome | WS-EDIT-SELECT-FLAGS initialised; exit 1210-EDIT-ARRAY. |
| Implemented at | COTRTLIC 1210-EDIT-ARRAY `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:991-994` |
| Implemented at | COTRTLIC  `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:965-972` |
| Anchor (verified) | `INITIALIZE                 WS-EDIT-SELECT-FLAGS` |

### BR-COTRTLIC-012

An update whose new description equals the current database description, ignoring case and leading/trailing spaces, is reported as 'No change detected with respect to database values.' and the description is not re-validated.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | UPPER(TRIM(WS-ROW-TR-DESC-IN(I))) = UPPER(TRIM(WS-CA-ROW-TR-DESC-OUT(I))) and equal trimmed lengths |
| Outcome | WS-RETURN-MSG = 'No change detected with respect to database values.'; INPUT-ERROR is not set. |
| Messages | No change detected with respect to database values. |
| Implemented at | COTRTLIC 1211-EDIT-ARRAY-DESC `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1064-1076` |
| Anchor (verified) | `SET WS-MESG-NO-CHANGES-DETECTED   TO TRUE` |

### BR-COTRTLIC-013

A changed transaction type description is mandatory and may contain only letters (A-Z, a-z), digits and spaces; otherwise the input is rejected with 'Transaction Desc must be supplied.' or 'Transaction Desc can have numbers or alphabets only.' and the description is highlighted.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | Description empty, or contains a character outside LIT-UPPER, LIT-LOWER, LIT-NUMBERS and space |
| Outcome | INPUT-ERROR; FLG-ALPHNANUM-BLANK or FLG-ALPHNANUM-NOT-OK; message only if no earlier message. |
| Messages | must be supplied.;  can have numbers or alphabets only. |
| Implemented at | COTRTLIC 1240-EDIT-ALPHANUM-REQD `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1186-1231` |
| Implemented at | COTRTLIC  `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1083-1089` |
| Implemented at | COTRTLIC  `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:65-72` |
| Anchor (verified) | `' can have numbers or alphabets only.'` |

### BR-COTRTLIC-014

The transaction type code filter is optional (blank, spaces or '00' mean no filter); if supplied it must be numeric (2 digits), otherwise the input is rejected with 'TYPE CODE FILTER,IF SUPPLIED MUST BE A 2 DIGIT NUMBER' and row selection is disabled.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | WS-IN-TYPE-CD not LOW-VALUES/SPACES/ZEROS and NOT NUMERIC |
| Outcome | INPUT-ERROR, FLG-TYPEFILTER-NOT-OK, FLG-PROTECT-SELECT-ROWS-YES; else WS-TYPE-CD-FILTER = WS-IN-TYPE-CD with FLG-TYPEFILTER-ISVALID. |
| Messages | TYPE CODE FILTER,IF SUPPLIED MUST BE A 2 DIGIT NUMBER |
| Implemented at | COTRTLIC 1220-EDIT-TYPECD `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1101-1122` |
| Anchor (verified) | `IF WS-IN-TYPE-CD  IS NOT NUMERIC` |

### BR-COTRTLIC-015

Changing either search filter (type code or description) restarts paging: the saved paging state (first/last keys, page number, next-page indicator) is cleared and the new filter value is remembered in the commarea.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | WS-IN-TYPE-CD <> WS-CA-TYPE-CD (unless both empty); WS-IN-TYPE-DESC <> WS-CA-TYPE-DESC (unless both empty) |
| Outcome | INITIALIZE WS-CA-PAGING-VARIABLES; FLG-TYPEFILTER-CHANGED-YES / FLG-DESCFILTER-CHANGED-YES. |
| Implemented at | COTRTLIC 1220-EDIT-TYPECD-EXIT `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1127-1137` |
| Implemented at | COTRTLIC  `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1166-1175` |
| Anchor (verified) | `INITIALIZE WS-CA-PAGING-VARIABLES` |

### BR-COTRTLIC-016

A non-blank description filter is applied as a 'contains' search: TR_DESCRIPTION LIKE '%<trimmed filter>%'. Inferred: the match is case-sensitive because the column is compared as stored without case folding.

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | WS-IN-TYPE-DESC not LOW-VALUES/SPACES |
| Outcome | FLG-DESCFILTER-ISVALID; WS-TYPE-DESC-FILTER = '%' \|\| TRIM(input) \|\| '%'. |
| Implemented at | COTRTLIC 1230-EDIT-DESC `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1147-1163` |
| Implemented at | COTRTLIC  `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:338-352` |
| Anchor (verified) | `STRING '%'` |

### BR-COTRTLIC-017

When a type or description filter is supplied, the program counts matching TRANSACTION_TYPE rows first; if none match, the input is rejected with 'No Records found for these filter conditions', the supplied filters are flagged in error and row selection is disabled. A SQL error on the count is also treated as an input error with a formatted DB2 message.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | FLG-TYPEFILTER-ISVALID OR FLG-DESCFILTER-ISVALID; WS-RECORDS-COUNT = 0 |
| Outcome | INPUT-ERROR, filter flags NOT-OK, FLG-PROTECT-SELECT-ROWS-YES. |
| Messages | No Records found for these filter conditions; Error reading TRANSACTION_TYPE table |
| Implemented at | COTRTLIC 1290-CROSS-EDITS `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1241-1267` |
| Implemented at | COTRTLIC  `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1803-1833` |
| Anchor (verified) | `'No Records found for these filter conditions'` |

### BR-COTRTLIC-018

The list shows at most 7 transaction types per page in ascending TR_TYPE order starting at the page start key and honouring the active filters. An eighth row is fetched only to decide whether a next page exists and to set the next page's start key. If page 1 has no rows the message 'No records found for this search condition.' is shown; pressing PF8 at the end shows 'No more pages for these search conditions'. Other SQL errors stop the read with a formatted DB2 message.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | C-TR-TYPE-FORWARD: TR_TYPE >= WS-START-KEY, optional TR_TYPE = filter, optional TR_DESCRIPTION LIKE filter, ORDER BY TR_TYPE |
| Outcome | WS-CA-ROW-*-OUT(1..7), WS-CA-FIRST-TR-CODE, WS-CA-LAST-TR-CODE, CA-NEXT-PAGE-EXISTS/NOT-EXISTS. |
| Messages | No records found for this search condition.; No more pages for these search conditions |
| Implemented at | COTRTLIC 8000-READ-FORWARD `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1609-1719` |
| Implemented at | COTRTLIC  `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:338-352` |
| Implemented at | COTRTLIC  `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:60` |
| Anchor (verified) | `IF WS-ROW-NUMBER = WS-MAX-SCREEN-LINES` |

### BR-COTRTLIC-019

Page back reads the 7 transaction types immediately before the current page's first code (TR_TYPE < start key, descending) and places them in rows 7 down to 1, so the page is shown in ascending order; the new first code becomes the start key. Any fetch that does not return a row is treated as a DB2 error.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | C-TR-TYPE-BACKWARD: TR_TYPE < WS-START-KEY with the same filters, ORDER BY TR_TYPE DESC |
| Outcome | Rows filled from 7 to 1; WS-CA-FIRST-TR-CODE updated; on error WS-DB2-ERROR with 'Error on fetch Cursor C-TR-TYPE-BACKWARD'. |
| Messages | Error on fetch Cursor C-TR-TYPE-BACKWARD |
| Implemented at | COTRTLIC 8100-READ-BACKWARDS `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1735-1791` |
| Implemented at | COTRTLIC  `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:354-368` |
| Anchor (verified) | `FETCH C-TR-TYPE-BACKWARD` |

### BR-COTRTLIC-020

A confirmation is armed (CA-DELETE-REQUESTED or CA-UPDATE-REQUESTED stored in the commarea) only when exactly one valid action is selected and no row has an invalid action; after a completed delete or update the row's select code is cleared.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | DELETE-REQUESTED-ON(I) / UPDATE-REQUESTED-ON(I) AND WS-ONLY-1-VALID-ACTION AND FLG-BAD-ACTIONS-SELECTED-NO |
| Outcome | CA-DELETE-REQUESTED / CA-UPDATE-REQUESTED set, or SELECT-BLANK(I) when FLG-DELETED-YES / FLG-UPDATE-COMPLETED. |
| Implemented at | COTRTLIC 2300-SCREEN-ARRAY-INIT `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1391-1411` |
| Anchor (verified) | `SET CA-DELETE-REQUESTED      TO TRUE` |

### BR-COTRTLIC-021

Screen messages follow a fixed priority: delete success, update success, filter errors (no info message), confirmation prompts for a single delete/update on ENTER (only if filters unchanged), 'No previous pages to display' on PF7 at page 1, 'No more pages to display' on PF8 once the last page has already been shown, otherwise the hint 'Type U to update, D to delete any record'.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | FLG-DELETED-YES, FLG-UPDATE-COMPLETED, filter flags, AID key, CA-FIRST-PAGE, CA-NEXT-PAGE-NOT-EXISTS, CA-LAST-PAGE-SHOWN |
| Outcome | WS-INFO-MSG / WS-RETURN-MSG set; CA-LAST-PAGE-SHOWN set on first PF8 at the end. |
| Messages | HIGHLIGHTED row deleted.Hit Enter to continue; HIGHLIGHTED row was updated; No previous pages to display; No more pages to display; Type U to update, D to delete any record |
| Implemented at | COTRTLIC 2500-SETUP-MESSAGE `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1506-1555` |
| Implemented at | COTRTLIC  `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:237-248` |
| Anchor (verified) | `MOVE 'No previous pages to display'` |

### BR-COTRTLIC-022

A confirmed description update is committed (CICS SYNCPOINT) only on SQLCODE 0. Row not found (+100, 'Record not found. Deleted by others ? '), deadlock/timeout (-911, 'Deadlock. Someone else updating ?', also an input error) and other negative SQLCODEs ('Update failed with') keep the update request pending so the user can retry.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | UPDATE CARDDEMO.TRANSACTION_TYPE SET TR_DESCRIPTION = :DCL-TR-DESCRIPTION WHERE TR_TYPE = :DCL-TR-TYPE |
| Outcome | 0: SYNCPOINT, CA-UPDATE-SUCCEEDED, 'HIGHLIGHTED row was updated'; else CA-UPDATE-REQUESTED and formatted DB2 message. |
| Messages | Record not found. Deleted by others ? ; Deadlock. Someone else updating ?; Update failed with |
| Implemented at | COTRTLIC 9200-UPDATE-RECORD `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1841-1889` |
| Anchor (verified) | `WHEN SQLCODE = -911` |

### BR-COTRTLIC-023

A transaction type that still has category rows cannot be deleted: SQLCODE -532 (delete restricted by the TRANSACTION_TYPE_CATEGORY foreign key ON DELETE RESTRICT) produces 'Please delete associated child records first:' and keeps the delete pending. A successful delete is committed with CICS SYNCPOINT; any other SQLCODE produces 'Delete failed with message:'.

| Item | Value |
|---|---|
| Category | data-integrity |
| Confidence | Confirmed |
| Conditions | DELETE FROM CARDDEMO.TRANSACTION_TYPE WHERE TR_TYPE = :DCL-TR-TYPE |
| Outcome | 0: SYNCPOINT, CA-DELETE-SUCCEEDED, 'HIGHLIGHTED row deleted.Hit Enter to continue'; -532: CA-DELETE-REQUESTED + message; other: message. |
| Messages | Please delete associated child records first:; Delete failed with message: |
| Implemented at | COTRTLIC 9300-DELETE-RECORD `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:1902-1936` |
| Implemented at | COTRTLIC  `app/app-transaction-type-db2/ddl/TRNTYCAT.ddl:1-7` |
| Anchor (verified) | `WHEN SQLCODE = -532` |


## COTRTUPC

Program page: [COTRTUPC](07-programs/COTRTUPC.md).

### BR-BASE-COTRTUPC-001

The transaction type code is required, must be numeric, and must not be zero, within 2 characters. A code that passes is rewritten with leading zeros.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | TTUP-NEW-TTYP-TYPE blank, not numeric, or zero |
| Outcome | set INPUT-ERROR and redisplay the screen - Tran Type code must be supplied.; set INPUT-ERROR and redisplay the screen - Tran Type code must be numeric.; set INPUT-ERROR and redisplay the screen - Tran Type code must not be zero.; zero-pad the type code to 2 characters |
| Messages | must be supplied.; must be numeric.; must not be zero. |
| Implemented at | COTRTUPC 1210-EDIT-TRANTYPE `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:820-842` |
| Implemented at | COTRTUPC 1245-EDIT-NUM-REQD `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:907-974` |
| Batch review | corrected: Range spans 1210-EDIT-TRANTYPE (820-842) and 1245-EDIT-NUM-REQD (907-973); the 1230-EDIT-ALPHANUM-REQD lines in between belong to BR-BASE-COTRTUPC-002. Required and non-zero are correct ('Tran Type code must be supplied.', 'Tran Type code must not be zero.'). Corrected on 'numeric': the test is FUNCTION TEST-NUMVAL on the 2-character value (934-935), which also accepts a sign, a decimal point or trailing spaces (message 'Tran Type code must be numeric.'). A passing value is converted with NUMVAL into unsigned PIC 9(02) WS-EDIT-NUMERIC-2, so a sign or fraction is dropped (Inferred: '-5' becomes '05', '.5' becomes '00' after passing the non-zero test). The code is then rewritten with leading zeros (spaces replaced by zeros). The edit only runs when not in create-new or confirm state (712-717). (`app/app-transaction-type-db2/cbl/COTRTUPC.cbl:820-973`, anchor `COMPUTE WS-EDIT-NUMERIC-2`) |

### BR-BASE-COTRTUPC-002

The transaction description is required and may contain only letters, digits and spaces, within 50 characters.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | TTUP-NEW-TTYP-TYPE-DESC blank ; description contains a character other than a letter, digit or space |
| Outcome | set INPUT-ERROR and redisplay the screen - Transaction Desc must be supplied.; set INPUT-ERROR and redisplay the screen - Transaction Desc can have numbers or alphabets only. |
| Messages | must be supplied.; can have numbers or alphabets only. |
| Implemented at | COTRTUPC 1200-EDIT-MAP-INPUTS `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:755-764` |
| Implemented at | COTRTUPC 1230-EDIT-ALPHANUM-REQD `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:849-903` |
| Batch review | confirmed: Invoked from 1200-EDIT-MAP-INPUTS at 755-764. Description (TTUP-NEW-TTYP-TYPE-DESC, length 50) must be non-blank ('Transaction Desc must be supplied.') and contain only A-Z, a-z, 0-9 and spaces ('Transaction Desc can have numbers or alphabets only.'). The edit runs only when a change has been detected (746-751). (`app/app-transaction-type-db2/cbl/COTRTUPC.cbl:849-902`, anchor `' can have numbers or alphabets only.'`) |

### BR-BASE-COTRTUPC-003

No change is reported when the type code matches after upper case, and the description matches after trim and upper case and has the same trimmed length. Field edits are then skipped.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | UPPER-CASE(new type) = UPPER-CASE(old type); trimmed upper-case description and its length = old description |
| Outcome | skip the field edits - No change detected with respect to values fetched. |
| Messages | No change detected with respect to values fetched. |
| Implemented at | COTRTUPC 1205-COMPARE-OLD-NEW `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:783-811` |
| Implemented at | COTRTUPC 1200-EDIT-MAP-INPUTS `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:743-750` |
| Implemented at | COTRTUPC  `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:179-180` |
| Batch review | confirmed: Range spans the skip decision in 1200-EDIT-MAP-INPUTS (743-751) through 1205-COMPARE-OLD-NEW (783-811). Confirmed: type code compared upper-cased, description compared trimmed and upper-cased with equal trimmed length; if equal 'No change detected with respect to values fetched.' (only when no prior message) and the non-key edits are skipped (WS-NON-KEY-FLAGS cleared). Edits are also skipped when the state is already 'N' (validated) or 'C' (done). A case-only description change is therefore treated as no change. (`app/app-transaction-type-db2/cbl/COTRTUPC.cbl:743-811`, anchor `SET NO-CHANGES-DETECTED   TO TRUE`) |

### BR-COTRTUPC-001

After a completed or failed save, a completed or failed delete, a cancelled new-record entry (backed out with no fetched record), or PF12 while viewing details, creating a record or on a not-found key, the screen restarts as a fresh search (enter transaction type).

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | PF12 with TTUP-SHOW-DETAILS/CREATE-NEW-RECORD/DETAILS-NOT-FOUND, or state C, L, F, 7, 6, or B with empty old details |
| Outcome | CDEMO-PGM-ENTER and TTUP-DETAILS-NOT-FETCHED; empty search screen sent. |
| Messages | Enter transaction type to be maintained |
| Implemented at | COTRTUPC 0000-MAIN `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:405-419` |
| Implemented at | COTRTUPC  `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:465-478` |
| Anchor (verified) | `WHEN TTUP-CHANGES-OKAYED-AND-DONE` |

### BR-COTRTUPC-002

PF3 returns to the calling transaction/program from the commarea, or to the admin menu CA00 / COADM01C when none is recorded, after a CICS SYNCPOINT.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | CCARD-AID-PFK03 |
| Outcome | EXEC CICS XCTL PROGRAM(CDEMO-TO-PROGRAM) COMMAREA(CARDDEMO-COMMAREA). |
| Implemented at | COTRTUPC 0000-MAIN `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:423-460` |
| Anchor (verified) | `MOVE LIT-ADMINTRANID   TO CDEMO-TO-TRANID` |

### BR-COTRTUPC-003

Function keys are only accepted in the screen states where they make sense: PF3 always; ENTER except while a delete confirmation is pending; PF4 when a record is shown or delete confirmation is pending; PF5 when changes are validated, the key was not found, or a delete is in progress; PF12 when validated, showing details, not found, confirming delete or creating new. Any other key redisplays the screen with 'Invalid key pressed'.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | AID key versus TTUP-CHANGE-ACTION |
| Outcome | PFK-VALID, or PFK-INVALID with 'Invalid key pressed' and screen resent. |
| Messages | Invalid key pressed |
| Implemented at | COTRTUPC 0001-CHECK-PFKEYS `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:582-608` |
| Implemented at | COTRTUPC  `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:539-542` |
| Anchor (verified) | `SET WS-INVALID-KEY-PRESSED  TO TRUE` |

### BR-COTRTUPC-004

Deleting a transaction type is two-step: PF4 on a displayed record asks 'Delete this record ? Press F4 to confirm'; a second PF4 in that state performs the DELETE.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | CCARD-AID-PFK04 AND TTUP-SHOW-DETAILS, then CCARD-AID-PFK04 AND TTUP-CONFIRM-DELETE |
| Outcome | TTUP-CONFIRM-DELETE; then TTUP-START-DELETE and 9800-DELETE-PROCESSING. |
| Messages | Delete this record ? Press F4 to confirm |
| Implemented at | COTRTUPC 0000-MAIN `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:482-498` |
| Anchor (verified) | `SET TTUP-START-DELETE                TO TRUE` |

### BR-COTRTUPC-005

When the entered transaction type code does not exist, the user may press PF5 to create it: the screen switches to new-record entry ('Enter new transaction type details.'); after the description passes validation, PF5 saves it.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | CCARD-AID-PFK05 AND TTUP-DETAILS-NOT-FOUND; later CCARD-AID-PFK05 AND TTUP-CHANGES-OK-NOT-CONFIRMED |
| Outcome | TTUP-CREATE-NEW-RECORD; then 9600-WRITE-PROCESSING. |
| Messages | Press F05 to add. F12 to cancel; Enter new transaction type details. |
| Implemented at | COTRTUPC 0000-MAIN `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:503-520` |
| Implemented at | COTRTUPC  `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1053-1055` |
| Anchor (verified) | `SET TTUP-CREATE-NEW-RECORD TO TRUE` |

### BR-COTRTUPC-006

PF12 cancels a pending action: cancelling a delete confirmation gives 'Delete was cancelled' and returns to the search prompt; cancelling validated changes gives 'Update was cancelled', restores the fetched values (backed out) and the next interaction returns to edit mode.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | CCARD-AID-PFK12 AND (TTUP-CONFIRM-DELETE OR TTUP-CHANGES-OK-NOT-CONFIRMED) |
| Outcome | TTUP-DETAILS-NOT-FETCHED or TTUP-CHANGES-BACKED-OUT (then TTUP-CHANGES-NOT-OK). |
| Messages | Delete was cancelled; Update was cancelled |
| Implemented at | COTRTUPC 2000-DECIDE-ACTION `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:999-1008` |
| Implemented at | COTRTUPC  `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:524-533` |
| Implemented at | COTRTUPC  `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1041-1042` |
| Anchor (verified) | `SET WS-UPDATE-WAS-CANCELLED     TO TRUE` |

### BR-COTRTUPC-007

Screen input of '*' or all spaces in the type code or description is treated as not supplied (LOW-VALUES); other input is trimmed. When a not-found key is resent unchanged without PF5, the previously entered values are kept.

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | TRTYPCDI / TRTYDSCI = '*' or SPACES |
| Outcome | TTUP-NEW-TTYP-TYPE / TTUP-NEW-TTYP-TYPE-DESC = LOW-VALUES, else FUNCTION TRIM(input). |
| Implemented at | COTRTUPC 1150-STORE-MAP-IN-NEW `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:654-684` |
| Anchor (verified) | `IF  TRTYPCDI OF CTRTUPAI = '*'` |

### BR-COTRTUPC-008

If the key was not found and the user resends the same key: with PF5 the key is accepted for creation; otherwise the record is looked up again. Edits are skipped in both cases.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | TTUP-DETAILS-NOT-FOUND AND TRIM(TRTYPCDI) = TTUP-NEW-TTYP-TYPE |
| Outcome | FLG-TRANFILTER-ISVALID; TTUP-DETAILS-NOT-FETCHED unless PF5. |
| Implemented at | COTRTUPC 1200-EDIT-MAP-INPUTS `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:698-710` |
| Anchor (verified) | `SET TTUP-DETAILS-NOT-FETCHED    TO TRUE` |

### BR-COTRTUPC-009

A transaction type code must be entered to search: blank input gives 'No input received' and stays on the search prompt; a code failing the numeric edit marks the search key invalid. The key edit is skipped in create-new and validated states.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | FLG-TRANFILTER-BLANK or FLG-TRANFILTER-NOT-OK after 1210-EDIT-TRANTYPE |
| Outcome | TTUP-DETAILS-NOT-FETCHED (and TTUP-INVALID-SEARCH-KEYS when invalid). |
| Messages | No input received |
| Implemented at | COTRTUPC 1200-EDIT-MAP-INPUTS `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:712-737` |
| Anchor (verified) | `SET NO-SEARCH-CRITERIA-RECEIVED TO TRUE` |

### BR-COTRTUPC-010

A valid search key is looked up in TRANSACTION_TYPE: if found the record is displayed for change or delete, otherwise the user is offered to add it.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | TTUP-DETAILS-NOT-FETCHED (or PF12) AND FLG-TRANFILTER-ISVALID |
| Outcome | 9000-READ-TRANTYPE; TTUP-SHOW-DETAILS or TTUP-DETAILS-NOT-FOUND. |
| Implemented at | COTRTUPC 2000-DECIDE-ACTION `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:979-997` |
| Implemented at | COTRTUPC  `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1456-1458` |
| Anchor (verified) | `SET TTUP-DETAILS-NOT-FOUND       TO TRUE` |

### BR-COTRTUPC-011

When a displayed record has been changed and passes all edits, the program asks for confirmation ('Changes validated.Press F5 to save') instead of saving immediately; edit errors or no detected change keep the record in edit mode.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | TTUP-SHOW-DETAILS AND NOT (INPUT-ERROR OR NO-CHANGES-DETECTED OR WS-INVALID-KEY) |
| Outcome | TTUP-CHANGES-OK-NOT-CONFIRMED. |
| Messages | Changes validated.Press F5 to save |
| Implemented at | COTRTUPC 2000-DECIDE-ACTION `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1023-1030` |
| Anchor (verified) | `OR NO-CHANGES-DETECTED` |

### BR-COTRTUPC-012

After a successful save the record is shown again; if the program was not entered from another transaction, the account context in the commarea (account id, card number, account status) is cleared.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | TTUP-CHANGES-OKAYED-AND-DONE; CDEMO-FROM-TRANID LOW-VALUES or SPACES |
| Outcome | TTUP-SHOW-DETAILS; CDEMO-ACCT-ID, CDEMO-CARD-NUM = 0; CDEMO-ACCT-STATUS = LOW-VALUES. |
| Implemented at | COTRTUPC 2000-DECIDE-ACTION `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1065-1072` |
| Anchor (verified) | `MOVE ZEROES       TO CDEMO-ACCT-ID` |

### BR-COTRTUPC-013

Any screen state not handled by the decision logic is treated as a program error: the task sends the abend data ('UNEXPECTED DATA SCENARIO') to the terminal and abends with code 9999.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | WHEN OTHER in 2000-DECIDE-ACTION (or any CICS abend via HANDLE ABEND) |
| Outcome | ABEND-ROUTINE: EXEC CICS SEND ABEND-DATA, HANDLE ABEND CANCEL, EXEC CICS ABEND ABCODE('9999'). |
| Messages | UNEXPECTED DATA SCENARIO; UNEXPECTED ABEND OCCURRED. |
| Implemented at | COTRTUPC 2000-DECIDE-ACTION `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1073-1080` |
| Implemented at | COTRTUPC  `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1677-1697` |
| Anchor (verified) | `'UNEXPECTED DATA SCENARIO'` |

### BR-COTRTUPC-014

A transaction type code that does not exist in TRANSACTION_TYPE is reported as 'No record found for this key in database'; a SQL error on the lookup is reported with the SQLCODE and SQLERRM. Both mark the key as not OK.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | SELECT ... WHERE TR_TYPE = :DCL-TR-TYPE returns +100 or < 0 |
| Outcome | INPUT-ERROR, FLG-TRANFILTER-NOT-OK, message. |
| Messages | No record found for this key in database; Error accessing:;  TRANSACTION_TYPE table. SQLCODE: |
| Implemented at | COTRTUPC 9100-GET-TRANSACTION-TYPE `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1486-1509` |
| Anchor (verified) | `SET WS-RECORD-NOT-FOUND       TO TRUE` |

### BR-COTRTUPC-015

Saving is an upsert: the description is UPDATEd by TR_TYPE; if no row exists (+100) the row is INSERTed. A successful update or insert is committed with CICS SYNCPOINT. Deadlock/timeout (-911) gives 'Could not lock record for update'; other negative SQLCODEs give 'Error updating: TRANSACTION_TYPE Table. SQLCODE:...' and insert failures 'Error inserting record into: TRANSACTION_TYPE Table. SQLCODE:...'.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | PF5 with TTUP-CHANGES-OK-NOT-CONFIRMED |
| Outcome | SYNCPOINT on success; INPUT-ERROR on -911; error message otherwise. |
| Messages | Could not lock record for update; Error updating:; Error inserting record into: |
| Implemented at | COTRTUPC 9600-WRITE-PROCESSING `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1555-1578` |
| Implemented at | COTRTUPC  `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1538-1548` |
| Implemented at | COTRTUPC  `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1604-1619` |
| Anchor (verified) | `PERFORM 9700-INSERT-RECORD` |

### BR-COTRTUPC-016

The outcome of a save sets the next screen state: lock failure shows 'Changes unsuccessful' (lock error), a flagged update failure shows 'Changes unsuccessful' (failed), a concurrent-change condition returns to show details, and anything else is treated as committed ('Changes committed to database'). Inferred: because the failure flag is overwritten by the SQL error text, SQL failures also reach the committed state (see observation).

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Inferred |
| Conditions | COULD-NOT-LOCK-REC-FOR-UPDATE / TABLE-UPDATE-FAILED / DATA-WAS-CHANGED-BEFORE-UPDATE / OTHER |
| Outcome | TTUP-CHANGES-OKAYED-LOCK-ERROR, -BUT-FAILED, TTUP-SHOW-DETAILS or TTUP-CHANGES-OKAYED-AND-DONE. |
| Messages | Changes unsuccessful; Changes committed to database |
| Implemented at | COTRTUPC 9600-WRITE-PROCESSING `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1580-1589` |
| Anchor (verified) | `SET TTUP-CHANGES-OKAYED-AND-DONE     TO TRUE` |

### BR-COTRTUPC-017

A confirmed delete removes the transaction type by its fetched code and commits (CICS SYNCPOINT, 'Delete successful.'). If category rows still reference it (SQLCODE -532, foreign key ON DELETE RESTRICT) the message 'Please delete associated child records first:' with SQLCODE and SQLERRM is shown; any other failure sets delete-failed with 'Delete failed with message:'.

| Item | Value |
|---|---|
| Category | data-integrity |
| Confidence | Confirmed |
| Conditions | DELETE FROM CARDDEMO.TRANSACTION_TYPE WHERE TR_TYPE = TTUP-OLD-TTYP-TYPE |
| Outcome | 0: TTUP-DELETE-DONE + SYNCPOINT; -532: RECORD-DELETE-FAILED + message; other: TTUP-DELETE-FAILED + message. |
| Messages | Please delete associated child records first:; Delete failed with message:; Delete successful. |
| Implemented at | COTRTUPC 9800-DELETE-PROCESSING `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1634-1662` |
| Implemented at | COTRTUPC  `app/app-transaction-type-db2/ddl/TRNTYCAT.ddl:1-7` |
| Anchor (verified) | `WHEN SQLCODE = -532` |


## COUSR00C

Program page: [COUSR00C](07-programs/COUSR00C.md).

### BR-COUSR00C-001

When started without a COMMAREA (EIBCALEN = 0) the user is sent to the sign-on program COSGN00C.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | EIBCALEN = 0 |
| Outcome | XCTL COSGN00C. |
| Implemented at | COUSR00C MAIN-PARA `app/cbl/COUSR00C.cbl:110-112` |
| Implemented at | COUSR00C  `app/cbl/COUSR00C.cbl:508-516` |
| Anchor (verified) | `IF EIBCALEN = 0` |

### BR-COUSR00C-002

On re-entry the attention key decides the action: Enter processes selection/filter, PF3 returns to the admin menu COADM01C, PF7 pages backward, PF8 pages forward; other keys are rejected with the invalid-key message.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | CDEMO-PGM-REENTER and EIBAID |
| Outcome | DFHENTER -> PROCESS-ENTER-KEY; DFHPF3 -> XCTL COADM01C; DFHPF7/DFHPF8 -> paging; other -> WS-ERR-FLG 'Y', CCDA-MSG-INVALID-KEY. |
| Messages | Invalid key pressed. Please see below... |
| Implemented at | COUSR00C MAIN-PARA `app/cbl/COUSR00C.cbl:122-137` |
| Anchor (verified) | `MOVE 'COADM01C' TO CDEMO-TO-PROGRAM` |

### BR-COUSR00C-003

Only one row selection is honoured per Enter: selection fields are tested from row 1 to row 10 and the first non-blank one is taken with the user ID of the same row; if none is filled the stored selection is cleared.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | SELnnnnI not SPACES/LOW-VALUES, first match in row order |
| Outcome | CDEMO-CU00-USR-SEL-FLG / CDEMO-CU00-USR-SELECTED set, otherwise SPACES. |
| Implemented at | COUSR00C PROCESS-ENTER-KEY `app/cbl/COUSR00C.cbl:151-184` |
| Anchor (verified) | `WHEN SEL0001I OF COUSR0AI NOT = SPACES AND LOW-VALUES` |

### BR-COUSR00C-004

Valid row actions are 'U' (update) and 'D' (delete), upper or lower case. 'U' transfers to COUSR02C and 'D' to COUSR03C with the selected user ID in the COMMAREA; any other code is rejected with a message and the list is refreshed.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | CDEMO-CU00-USR-SEL-FLG and CDEMO-CU00-USR-SELECTED both not blank |
| Outcome | 'U'/'u': XCTL COUSR02C; 'D'/'d': XCTL COUSR03C (FROM tranid CU00, FROM program COUSR00C, context 0). Other: message shown, error flag not set. |
| Messages | Invalid selection. Valid values are U and D |
| Implemented at | COUSR00C PROCESS-ENTER-KEY `app/cbl/COUSR00C.cbl:186-216` |
| Anchor (verified) | `'Invalid selection. Valid values are U and D'` |

### BR-COUSR00C-005

The optional start user ID positions the list: blank lists from the beginning of USRSEC, otherwise the browse starts at the entered user ID (no format validation). Each Enter resets the page number to 0 before reading the first page.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | USRIDINI blank or not |
| Outcome | SEC-USR-ID = LOW-VALUES or USRIDINI; CDEMO-CU00-PAGE-NUM = 0; PROCESS-PAGE-FORWARD. |
| Implemented at | COUSR00C PROCESS-ENTER-KEY `app/cbl/COUSR00C.cbl:218-228` |
| Anchor (verified) | `IF USRIDINI OF COUSR0AI = SPACES OR LOW-VALUES` |

### BR-COUSR00C-006

PF7 (previous page) is allowed only when the page number is greater than 1; the backward browse starts at the first user ID of the current page (LOW-VALUES if none). On page 1 the user is told they are already at the top.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | CDEMO-CU00-PAGE-NUM > 1 |
| Outcome | PROCESS-PAGE-BACKWARD, else 'You are already at the top of the page...'. |
| Messages | You are already at the top of the page... |
| Implemented at | COUSR00C PROCESS-PF7-KEY `app/cbl/COUSR00C.cbl:239-255` |
| Anchor (verified) | `IF CDEMO-CU00-PAGE-NUM > 1` |

### BR-COUSR00C-007

PF8 (next page) is allowed only when the last forward read found an 11th user (next-page flag 'Y'); the browse starts at the last user ID of the current page (HIGH-VALUES if none). Otherwise the user is told they are already at the bottom.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | NEXT-PAGE-YES |
| Outcome | PROCESS-PAGE-FORWARD, else 'You are already at the bottom of the page...'. |
| Messages | You are already at the bottom of the page... |
| Implemented at | COUSR00C PROCESS-PF8-KEY `app/cbl/COUSR00C.cbl:262-277` |
| Anchor (verified) | `IF NEXT-PAGE-YES` |

### BR-COUSR00C-008

A page holds at most 10 users. On PF8 the record at the start key (last user of the previous page) is skipped; the rows are cleared and up to 10 users are read in ascending user ID order.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | EIBAID not Enter/PF7/PF3 for the skip; WS-IDX < 11, not EOF, no error for the fill |
| Outcome | Rows 1..n populated, remaining rows blank. |
| Implemented at | COUSR00C PROCESS-PAGE-FORWARD `app/cbl/COUSR00C.cbl:288-306` |
| Anchor (verified) | `PERFORM UNTIL WS-IDX >= 11 OR USER-SEC-EOF OR ERR-FLG-ON` |

### BR-COUSR00C-009

After a forward fill, the page number is increased by 1 when the page is full and a look-ahead read decides whether a next page exists; when end of file was hit during the fill there is no next page and the page number is increased only if at least one row was shown.

| Item | Value |
|---|---|
| Category | calculation |
| Confidence | Confirmed |
| Conditions | USER-SEC-NOT-EOF and no error; else WS-IDX > 1 |
| Outcome | CDEMO-CU00-PAGE-NUM + 1; NEXT-PAGE-YES/NO. |
| Implemented at | COUSR00C PROCESS-PAGE-FORWARD `app/cbl/COUSR00C.cbl:308-323` |
| Anchor (verified) | `COMPUTE CDEMO-CU00-PAGE-NUM =` |

### BR-COUSR00C-010

On PF7 the record at the start key (first user of the current page) is skipped and up to 10 previous users are read in descending order into rows 10 down to 1, so the screen stays in ascending order.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | EIBAID not Enter/PF8 for the skip; WS-IDX > 0, not EOF, no error for the fill |
| Outcome | Rows filled from 10 down to 1. |
| Implemented at | COUSR00C PROCESS-PAGE-BACKWARD `app/cbl/COUSR00C.cbl:342-360` |
| Anchor (verified) | `IF EIBAID NOT = DFHENTER  AND DFHPF8` |

### BR-COUSR00C-011

After a full backward page, one more previous record is read: if it exists and the page number is above 1 the page number is decreased by 1, otherwise it is set to 1. If the fill hit the start of the file, the page number is left unchanged.

| Item | Value |
|---|---|
| Category | calculation |
| Confidence | Confirmed |
| Conditions | USER-SEC-NOT-EOF and no error after the fill, NEXT-PAGE-YES, look-ahead result, CDEMO-CU00-PAGE-NUM > 1 |
| Outcome | CDEMO-CU00-PAGE-NUM - 1 or = 1. |
| Implemented at | COUSR00C PROCESS-PAGE-BACKWARD `app/cbl/COUSR00C.cbl:362-372` |
| Anchor (verified) | `SUBTRACT 1 FROM CDEMO-CU00-PAGE-NUM` |

### BR-COUSR00C-012

The user ID on row 1 is remembered as the page's first key and the user ID on row 10 as its last key; these are the start positions for PF7 and PF8.

| Item | Value |
|---|---|
| Category | data-integrity |
| Confidence | Confirmed |
| Conditions | WS-IDX = 1 or 10 |
| Outcome | CDEMO-CU00-USRID-FIRST / CDEMO-CU00-USRID-LAST updated. |
| Implemented at | COUSR00C POPULATE-USER-DATA `app/cbl/COUSR00C.cbl:387-389` |
| Implemented at | COUSR00C  `app/cbl/COUSR00C.cbl:433-435` |
| Anchor (verified) | `CDEMO-CU00-USRID-FIRST` |

### BR-COUSR00C-013

Starting the browse: no user at or after the start key is treated as end of list with a top-of-page message; any other failure sets the error flag with a lookup-failure message, stopping the page fill.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | WS-RESP-CD after STARTBR |
| Outcome | NOTFND: USER-SEC-EOF, 'You are at the top of the page...'. Other: DISPLAY RESP/REAS, WS-ERR-FLG 'Y'. |
| Messages | You are at the top of the page...; Unable to lookup User... |
| Implemented at | COUSR00C STARTBR-USER-SEC-FILE `app/cbl/COUSR00C.cbl:596-614` |
| Anchor (verified) | `'Unable to lookup User...'` |

### BR-COUSR00C-014

Reading forward: end of file stops the list with a bottom-of-page message; other failures set the error flag with a lookup-failure message.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | WS-RESP-CD after READNEXT |
| Outcome | ENDFILE: USER-SEC-EOF and message. Other: WS-ERR-FLG 'Y', 'Unable to lookup User...'. |
| Messages | You have reached the bottom of the page...; Unable to lookup User... |
| Implemented at | COUSR00C READNEXT-USER-SEC-FILE `app/cbl/COUSR00C.cbl:631-648` |
| Anchor (verified) | `'You have reached the bottom of the page...'` |

### BR-COUSR00C-015

Reading backward: start of file stops the list with a top-of-page message; other failures set the error flag with a lookup-failure message.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | WS-RESP-CD after READPREV |
| Outcome | ENDFILE: USER-SEC-EOF and message. Other: WS-ERR-FLG 'Y', 'Unable to lookup User...'. |
| Messages | You have reached the top of the page...; Unable to lookup User... |
| Implemented at | COUSR00C READPREV-USER-SEC-FILE `app/cbl/COUSR00C.cbl:665-682` |
| Anchor (verified) | `'You have reached the top of the page...'` |


## COUSR01C

Program page: [COUSR01C](07-programs/COUSR01C.md).

### BR-COUSR01C-001

When started without a COMMAREA (EIBCALEN = 0) the user is sent to the sign-on program COSGN00C.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | EIBCALEN = 0 |
| Outcome | XCTL COSGN00C. |
| Implemented at | COUSR01C MAIN-PARA `app/cbl/COUSR01C.cbl:78-80` |
| Implemented at | COUSR01C  `app/cbl/COUSR01C.cbl:167-177` |
| Anchor (verified) | `IF EIBCALEN = 0` |

### BR-COUSR01C-002

On re-entry the attention key decides the action: Enter validates and adds the user, PF3 returns to the admin menu COADM01C, PF4 clears the screen, any other key shows the invalid-key message.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | CDEMO-PGM-REENTER and EIBAID |
| Outcome | DFHENTER -> PROCESS-ENTER-KEY; DFHPF3 -> XCTL COADM01C; DFHPF4 -> CLEAR-CURRENT-SCREEN; other -> WS-ERR-FLG 'Y', CCDA-MSG-INVALID-KEY. |
| Messages | Invalid key pressed. Please see below... |
| Implemented at | COUSR01C MAIN-PARA `app/cbl/COUSR01C.cbl:90-103` |
| Anchor (verified) | `MOVE 'COADM01C' TO CDEMO-TO-PROGRAM` |

### BR-COUSR01C-003

To add a user, first name, last name, user ID, password and user type are all mandatory. They are checked in that order and only the first missing field is reported; no format or value checks are applied (e.g. user type is not restricted to 'A' or 'U').

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | FNAMEI, LNAMEI, USERIDI, PASSWDI, USRTYPEI = SPACES or LOW-VALUES |
| Outcome | WS-ERR-FLG 'Y', message for the first blank field, cursor on that field, screen sent; no write. |
| Messages | First Name can NOT be empty...; Last Name can NOT be empty...; User ID can NOT be empty...; Password can NOT be empty...; User Type can NOT be empty... |
| Implemented at | COUSR01C PROCESS-ENTER-KEY `app/cbl/COUSR01C.cbl:117-151` |
| Anchor (verified) | `WHEN FNAMEI OF COUSR1AI = SPACES OR LOW-VALUES` |

### BR-COUSR01C-004

A new user security record is built directly from the screen: user ID, first name, last name, password (stored as entered, in clear text) and user type.

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | All mandatory fields present |
| Outcome | SEC-USER-DATA populated and WRITE-USER-SEC-FILE performed. |
| Implemented at | COUSR01C PROCESS-ENTER-KEY `app/cbl/COUSR01C.cbl:153-160` |
| Anchor (verified) | `MOVE PASSWDI  OF COUSR1AI TO SEC-USR-PWD` |

### BR-COUSR01C-005

User IDs must be unique: the add is rejected when a record with the same user ID already exists in USRSEC. On success the screen is cleared and a confirmation naming the user is shown; any other write failure is reported as unable to add.

| Item | Value |
|---|---|
| Category | data-integrity |
| Confidence | Confirmed |
| Conditions | WS-RESP-CD after WRITE USRSEC |
| Outcome | NORMAL: fields cleared, green 'User <id> has been added ...'. DUPKEY/DUPREC: WS-ERR-FLG 'Y', 'User ID already exist...'. Other: WS-ERR-FLG 'Y', 'Unable to Add User...'. |
| Messages | User ID already exist...; Unable to Add User...;  has been added ... |
| Implemented at | COUSR01C WRITE-USER-SEC-FILE `app/cbl/COUSR01C.cbl:250-274` |
| Anchor (verified) | `'User ID already exist...'` |


## COUSR02C

Program page: [COUSR02C](07-programs/COUSR02C.md).

### BR-COUSR02C-001

When started without a COMMAREA (EIBCALEN = 0) the user is sent to the sign-on program COSGN00C.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | EIBCALEN = 0 |
| Outcome | XCTL COSGN00C. |
| Implemented at | COUSR02C MAIN-PARA `app/cbl/COUSR02C.cbl:90-92` |
| Implemented at | COUSR02C  `app/cbl/COUSR02C.cbl:252-260` |
| Anchor (verified) | `IF EIBCALEN = 0` |

### BR-COUSR02C-002

On first entry, when a user was selected on the user list (CDEMO-CU02-USR-SELECTED not blank), that user is fetched and displayed for editing immediately.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | NOT CDEMO-PGM-REENTER and CDEMO-CU02-USR-SELECTED not SPACES/LOW-VALUES |
| Outcome | USRIDINI = CDEMO-CU02-USR-SELECTED; PROCESS-ENTER-KEY; screen sent. |
| Implemented at | COUSR02C MAIN-PARA `app/cbl/COUSR02C.cbl:95-105` |
| Anchor (verified) | `IF CDEMO-CU02-USR-SELECTED NOT =` |

### BR-COUSR02C-003

Key actions on re-entry: Enter fetches the user; PF5 saves changes; PF3 also attempts to save changes and then returns to the calling program (CDEMO-FROM-PROGRAM, or COADM01C when unknown) regardless of the save outcome; PF4 clears the screen; PF12 returns to the admin menu COADM01C without saving; other keys show the invalid-key message.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | EIBAID value; for PF3 whether CDEMO-FROM-PROGRAM is blank |
| Outcome | DFHENTER -> PROCESS-ENTER-KEY; DFHPF3 -> UPDATE-USER-INFO then XCTL; DFHPF4 -> CLEAR-CURRENT-SCREEN; DFHPF5 -> UPDATE-USER-INFO; DFHPF12 -> XCTL COADM01C; other -> WS-ERR-FLG 'Y', CCDA-MSG-INVALID-KEY. |
| Messages | Invalid key pressed. Please see below... |
| Implemented at | COUSR02C MAIN-PARA `app/cbl/COUSR02C.cbl:108-131` |
| Anchor (verified) | `WHEN DFHPF12` |

### BR-COUSR02C-004

A user ID is required to fetch a user for update.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | USRIDINI = SPACES or LOW-VALUES |
| Outcome | WS-ERR-FLG 'Y', 'User ID can NOT be empty...', no read. |
| Messages | User ID can NOT be empty... |
| Implemented at | COUSR02C PROCESS-ENTER-KEY `app/cbl/COUSR02C.cbl:145-155` |
| Anchor (verified) | `WHEN USRIDINI OF COUSR2AI = SPACES OR LOW-VALUES` |

### BR-COUSR02C-005

To save an update, user ID, first name, last name, password and user type must all be non-blank; they are checked in that order and only the first missing field is reported. No value or format checks are applied (user type is not restricted to 'A'/'U').

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | USRIDINI, FNAMEI, LNAMEI, PASSWDI, USRTYPEI blank |
| Outcome | WS-ERR-FLG 'Y', message for the first blank field, screen sent; no update. |
| Messages | User ID can NOT be empty...; First Name can NOT be empty...; Last Name can NOT be empty...; Password can NOT be empty...; User Type can NOT be empty... |
| Implemented at | COUSR02C UPDATE-USER-INFO `app/cbl/COUSR02C.cbl:179-213` |
| Anchor (verified) | `WHEN PASSWDI OF COUSR2AI = SPACES OR LOW-VALUES` |

### BR-COUSR02C-006

Only fields that differ from the stored record are changed: first name, last name, password and user type on the screen are each compared with the record just read, the new value is copied when different, and the record is marked as modified. The user ID itself is the key and cannot be changed.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | No validation error; screen value NOT = stored value per field |
| Outcome | SEC-USR-FNAME / SEC-USR-LNAME / SEC-USR-PWD / SEC-USR-TYPE updated, USR-MODIFIED-YES. |
| Implemented at | COUSR02C UPDATE-USER-INFO `app/cbl/COUSR02C.cbl:215-234` |
| Anchor (verified) | `IF FNAMEI  OF COUSR2AI NOT = SEC-USR-FNAME` |

### BR-COUSR02C-007

The user record is rewritten only when at least one field was changed; otherwise the user is asked to modify something and nothing is written.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | USR-MODIFIED-YES |
| Outcome | UPDATE-USER-SEC-FILE; else message 'Please modify to update ...' in red (DFHRED). |
| Messages | Please modify to update ... |
| Implemented at | COUSR02C UPDATE-USER-INFO `app/cbl/COUSR02C.cbl:236-243` |
| Anchor (verified) | `'Please modify to update ...'` |

### BR-COUSR02C-008

Fetching the user by exact user ID: if found the user is prompted to press PF5 to save; if not found the user is told so; other failures report a lookup error. Not-found and lookup errors set the error flag.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | WS-RESP-CD after READ UPDATE USRSEC |
| Outcome | NORMAL: 'Press PF5 key to save your updates ...' (DFHNEUTR) and screen sent. NOTFND: WS-ERR-FLG 'Y', 'User ID NOT found...'. Other: DISPLAY RESP/REAS, WS-ERR-FLG 'Y', 'Unable to lookup User...'. |
| Messages | Press PF5 key to save your updates ...; User ID NOT found...; Unable to lookup User... |
| Implemented at | COUSR02C READ-USER-SEC-FILE `app/cbl/COUSR02C.cbl:333-353` |
| Anchor (verified) | `'User ID NOT found...'` |

### BR-COUSR02C-009

Saving the user: a successful rewrite shows a green confirmation naming the user; not-found and other failures set the error flag with their messages.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | WS-RESP-CD after REWRITE USRSEC |
| Outcome | NORMAL: green 'User <id> has been updated ...'. NOTFND: 'User ID NOT found...'. Other: 'Unable to Update User...'. |
| Messages | has been updated ...; User ID NOT found...; Unable to Update User... |
| Implemented at | COUSR02C UPDATE-USER-SEC-FILE `app/cbl/COUSR02C.cbl:368-390` |
| Anchor (verified) | `' has been updated ...' DELIMITED BY SIZE` |


## COUSR03C

Program page: [COUSR03C](07-programs/COUSR03C.md).

### BR-COUSR03C-001

When started without a COMMAREA (EIBCALEN = 0) the user is sent to the sign-on program COSGN00C.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | EIBCALEN = 0 |
| Outcome | XCTL COSGN00C. |
| Implemented at | COUSR03C MAIN-PARA `app/cbl/COUSR03C.cbl:90-92` |
| Implemented at | COUSR03C  `app/cbl/COUSR03C.cbl:199-207` |
| Anchor (verified) | `IF EIBCALEN = 0` |

### BR-COUSR03C-002

On first entry, when a user was selected for deletion on the user list (CDEMO-CU03-USR-SELECTED not blank), that user is fetched and displayed immediately with the delete prompt.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | NOT CDEMO-PGM-REENTER and CDEMO-CU03-USR-SELECTED not SPACES/LOW-VALUES |
| Outcome | USRIDINI = CDEMO-CU03-USR-SELECTED; PROCESS-ENTER-KEY; screen sent. |
| Implemented at | COUSR03C MAIN-PARA `app/cbl/COUSR03C.cbl:95-105` |
| Anchor (verified) | `IF CDEMO-CU03-USR-SELECTED NOT =` |

### BR-COUSR03C-003

Key actions on re-entry: Enter fetches the user; PF5 deletes the user whose ID is on the screen; PF3 returns to the calling program (CDEMO-FROM-PROGRAM, or COADM01C when unknown); PF4 clears the screen; PF12 returns to the admin menu COADM01C; other keys show the invalid-key message.

| Item | Value |
|---|---|
| Category | routing |
| Confidence | Confirmed |
| Conditions | EIBAID value; for PF3 whether CDEMO-FROM-PROGRAM is blank |
| Outcome | DFHENTER -> PROCESS-ENTER-KEY; DFHPF3 -> XCTL CDEMO-FROM-PROGRAM or COADM01C; DFHPF4 -> clear; DFHPF5 -> DELETE-USER-INFO; DFHPF12 -> XCTL COADM01C; other -> WS-ERR-FLG 'Y', CCDA-MSG-INVALID-KEY. |
| Messages | Invalid key pressed. Please see below... |
| Implemented at | COUSR03C MAIN-PARA `app/cbl/COUSR03C.cbl:108-130` |
| Anchor (verified) | `PERFORM DELETE-USER-INFO` |

### BR-COUSR03C-004

A user ID is required to look up a user for deletion.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | USRIDINI = SPACES or LOW-VALUES |
| Outcome | WS-ERR-FLG 'Y', 'User ID can NOT be empty...', no read. |
| Messages | User ID can NOT be empty... |
| Implemented at | COUSR03C PROCESS-ENTER-KEY `app/cbl/COUSR03C.cbl:144-154` |
| Anchor (verified) | `WHEN USRIDINI OF COUSR3AI = SPACES OR LOW-VALUES` |

### BR-COUSR03C-005

PF5 deletes the user whose ID is currently in the input field; the only condition is that the ID is not blank. The user does not have to have been displayed first (no confirmation state is kept).

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | USRIDINI not blank |
| Outcome | READ UPDATE then DELETE of SEC-USR-ID; blank ID gives 'User ID can NOT be empty...'. |
| Messages | User ID can NOT be empty... |
| Implemented at | COUSR03C DELETE-USER-INFO `app/cbl/COUSR03C.cbl:176-192` |
| Anchor (verified) | `PERFORM DELETE-USER-SEC-FILE` |

### BR-COUSR03C-006

Fetching the user by exact user ID: if found the user is prompted to press PF5 to delete; if not found the user is told so; other failures report a lookup error. Not-found and lookup errors set the error flag.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | WS-RESP-CD after READ UPDATE USRSEC |
| Outcome | NORMAL: prompt (DFHNEUTR) and screen sent. NOTFND: WS-ERR-FLG 'Y', 'User ID NOT found...'. Other: DISPLAY RESP/REAS, WS-ERR-FLG 'Y', 'Unable to lookup User...'. |
| Messages | Press PF5 key to delete this user ...; User ID NOT found...; Unable to lookup User... |
| Implemented at | COUSR03C READ-USER-SEC-FILE `app/cbl/COUSR03C.cbl:280-300` |
| Anchor (verified) | `'Press PF5 key to delete this user ...'` |

### BR-COUSR03C-007

Deleting the user: success clears the screen and shows a green confirmation naming the user; not-found and other failures set the error flag with their messages (the generic failure text says 'Update').

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | WS-RESP-CD after DELETE USRSEC |
| Outcome | NORMAL: fields cleared, green 'User <id> has been deleted ...'. NOTFND: 'User ID NOT found...'. Other: DISPLAY RESP/REAS, 'Unable to Update User...'. |
| Messages | has been deleted ...; User ID NOT found...; Unable to Update User... |
| Implemented at | COUSR03C DELETE-USER-SEC-FILE `app/cbl/COUSR03C.cbl:313-336` |
| Anchor (verified) | `' has been deleted ...' DELIMITED BY SIZE` |


## CSUTLDTC

Program page: [CSUTLDTC](07-programs/CSUTLDTC.md).

### BR-CSUTLDTC-001

A date is valid when the Language Environment service CEEDAYS can convert the supplied date string using the supplied format mask into a Lilian day number; the validity is expressed by the CEEDAYS feedback severity and message number.

| Item | Value |
|---|---|
| Category | validation |
| Confidence | Confirmed |
| Conditions | Any call |
| Outcome | WS-SEVERITY-N and WS-MSG-NO-N set from FEEDBACK-CODE |
| Implemented at | CSUTLDTC A000-MAIN `app/cbl/CSUTLDTC.cbl:105-124` |
| Anchor (verified) | `CALL "CEEDAYS" USING WS-DATE-TO-TEST, WS-DATE-FORMAT, OUTPUT-LILLIAN, FEEDBACK-CODE` |

### BR-CSUTLDTC-002

The CEEDAYS feedback token is translated into a short result text: all-zero token -> 'Date is valid'; message 2507 -> 'Insufficient'; 2508 -> 'Datevalue error'; 2509 -> 'Invalid Era'; 2513 -> 'Unsupp. Range'; 2517 -> 'Invalid month'; 2518 -> 'Bad Pic String'; 2520 -> 'Nonnumeric data'; 2521 -> 'YearInEra is 0'; any other token -> 'Date is invalid'.

| Item | Value |
|---|---|
| Category | transformation |
| Confidence | Confirmed |
| Conditions | FEEDBACK-TOKEN-VALUE matches an 88-level |
| Outcome | WS-RESULT text |
| Messages | Date is valid; Insufficient; Datevalue error; Invalid Era; Unsupp. Range; Invalid month; Bad Pic String; Nonnumeric data; YearInEra is 0; Date is invalid |
| Implemented at | CSUTLDTC A000-MAIN `app/cbl/CSUTLDTC.cbl:128-149` |
| Implemented at | CSUTLDTC  `app/cbl/CSUTLDTC.cbl:61-70` |
| Anchor (verified) | `WHEN FC-UNSUPP-RANGE MOVE 'Unsupp. Range ' TO WS-RESULT` |

### BR-CSUTLDTC-003

The validation outcome is returned to the caller as an 80-byte result (severity in bytes 1-4, 'Mesg Code:', message number in bytes 16-19, result text, tested date and mask) and the CEEDAYS severity is also placed in RETURN-CODE; the subprogram never abends on an invalid date, leaving the decision to the caller.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | Every call |
| Outcome | LS-RESULT filled; RETURN-CODE = severity |
| Implemented at | CSUTLDTC (PROCEDURE DIVISION entry) `app/cbl/CSUTLDTC.cbl:90-100` |
| Implemented at | CSUTLDTC  `app/cbl/CSUTLDTC.cbl:42-57` |
| Anchor (verified) | `MOVE WS-SEVERITY-N TO RETURN-CODE` |


## DBUNLDGS

Program page: [DBUNLDGS](07-programs/DBUNLDGS.md).

### BR-DBUNLDGS-001

Only pending authorization summaries whose account id (PA-ACCT-ID) is numeric are unloaded; for those, the summary and all its child details are written to the GSAM datasets. Summaries with a non-numeric account id and their details are skipped silently.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | PA-ACCT-ID IS NUMERIC (packed decimal validity) |
| Outcome | ISRT to PASFLPCB, then details ISRT to PADFLPCB. |
| Implemented at | DBUNLDGS 2000-FIND-NEXT-AUTH-SUMMARY `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:241-247` |
| Anchor (verified) | `IF PA-ACCT-ID IS NUMERIC` |

### BR-DBUNLDGS-002

The unload stops with return code 16 on any IMS status other than blank or 'GB' on the summary read, other than blank or 'GE' on the detail read, or any non-blank status on a GSAM insert.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | Unexpected PCB status |
| Outcome | DISPLAY diagnostics, RETURN-CODE 16, GOBACK. |
| Messages | AUTH SUM  GN FAILED  :; GNP CALL FAILED  :; GSAM PARENT FAIL :; DBUNLDGS ABENDING ... |
| Implemented at | DBUNLDGS 2000-FIND-NEXT-AUTH-SUMMARY `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:253-256` |
| Implemented at | DBUNLDGS  `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:290-294` |
| Implemented at | DBUNLDGS  `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:311-315` |
| Implemented at | DBUNLDGS  `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:330-334` |
| Implemented at | DBUNLDGS  `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:360-363` |
| Anchor (verified) | `IF PAUT-PCB-STATUS NOT EQUAL TO  SPACES AND 'GB'` |


## PAUDBLOD

Program page: [PAUDBLOD](07-programs/PAUDBLOD.md).

### BR-PAUDBLOD-001

A detail record from the child file is loaded only when its packed account key (ROOT-SEG-KEY) is numeric; it is inserted as a PAUTDTL1 child under the PAUTSUM0 root whose ACCNTID equals that key. Records with a non-numeric key are skipped silently.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | ROOT-SEG-KEY IS NUMERIC and GU on PAUTSUM0 (ACCNTID EQ key) returns blank status |
| Outcome | ISRT PAUTDTL1 under that root. |
| Implemented at | PAUDBLOD 3000-READ-CHILD-SEG-FILE `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:274-282` |
| Implemented at | PAUDBLOD  `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:296-309` |
| Anchor (verified) | `IF ROOT-SEG-KEY IS NUMERIC` |

### BR-PAUDBLOD-002

Reloading is re-runnable: a root or child segment that already exists (IMS status 'II') is reported and skipped rather than treated as an error; any other insert failure ends the run with return code 16.

| Item | Value |
|---|---|
| Category | data-integrity |
| Confidence | Confirmed |
| Conditions | PAUT-PCB-STATUS after ISRT |
| Outcome | 'II' -> message only; other non-blank -> RETURN-CODE 16. |
| Messages | ROOT SEGMENT ALREADY IN DB; CHILD SEGMENT ALREADY IN DB; ROOT INSERT FAILED  :; INSERT CALL FAIL FOR CHILD:; IMS LOAD ABENDING ... |
| Implemented at | PAUDBLOD 2100-INSERT-ROOT-SEG `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:253-262` |
| Implemented at | PAUDBLOD  `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:326-336` |
| Implemented at | PAUDBLOD  `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:363-366` |
| Anchor (verified) | `IF PAUT-PCB-STATUS NOT EQUAL TO  SPACES AND 'II'` |

### BR-PAUDBLOD-003

An input file that cannot be opened ends the run with return code 16; read errors other than end of file are only displayed and processing continues.

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | Open status not spaces/'00' |
| Outcome | 9999-ABEND (RETURN-CODE 16). |
| Messages | ERROR IN OPENING INFILE1:; ERROR IN OPENING INFILE2: |
| Implemented at | PAUDBLOD 1000-INITIALIZE `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:201-215` |
| Anchor (verified) | `DISPLAY 'ERROR IN OPENING INFILE1:' WS-INFIL1-STATUS` |


## PAUDBUNL

Program page: [PAUDBUNL](07-programs/PAUDBUNL.md).

### BR-PAUDBUNL-001

Only pending authorization summaries with a numeric account id are unloaded; for each such summary the summary record is written to OUTFIL1 and each child detail is written to OUTFIL2 prefixed with the packed account id so it can be re-parented on reload.

| Item | Value |
|---|---|
| Category | decision |
| Confidence | Confirmed |
| Conditions | PA-ACCT-ID IS NUMERIC |
| Outcome | WRITE OPFIL1-REC; WRITE OPFIL2-REC per detail with ROOT-SEG-KEY = PA-ACCT-ID. |
| Implemented at | PAUDBUNL 2000-FIND-NEXT-AUTH-SUMMARY `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:227-237` |
| Implemented at | PAUDBUNL  `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:266-272` |
| Anchor (verified) | `IF PA-ACCT-ID IS NUMERIC` |

### BR-PAUDBUNL-002

The unload stops with return code 16 when an output file cannot be opened or when IMS returns an unexpected status (not blank/'GB' on summary, not blank/'GE' on detail).

| Item | Value |
|---|---|
| Category | error-policy |
| Confidence | Confirmed |
| Conditions | Open status not spaces/'00'; unexpected PCB status |
| Outcome | DISPLAY, RETURN-CODE 16, GOBACK. |
| Messages | AUTH SUM  GN FAILED  :; GNP CALL FAILED  :; IMSUNLOD ABENDING ... |
| Implemented at | PAUDBUNL 2000-FIND-NEXT-AUTH-SUMMARY `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:243-246` |
| Implemented at | PAUDBUNL  `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:186-200` |
| Implemented at | PAUDBUNL  `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:279-283` |
| Implemented at | PAUDBUNL  `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:311-314` |
| Anchor (verified) | `IF PAUT-PCB-STATUS NOT EQUAL TO  SPACES AND 'GB'` |

## Sources

- `docs/_work/rules/rules.json`
- `docs/_work/rules/rules-legacy.json`
- `docs/_work/semantic/programs/`

## Confidence

Each rule carries its own Confirmed/Inferred tag. Legacy rules without a batch review are listed as not reviewed.
