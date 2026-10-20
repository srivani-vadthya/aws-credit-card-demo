# Screen COPAU00

| Item | Value |
|---|---|
| Mapset | COPAU00 |
| Maps | COPAU0A |
| Source | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:19 |
| Module | auth |
| Programs | COPAUS0C |
| Transactions | CPVS |

## Purpose

Mapset COPAU00 is defined in the BMS source cited below. Field text in the mockup comes from BMS INITIAL and POS values already extracted.

## Map COPAU0A

## Layout mockup

```text
Tran: XXXX          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Date: mm/dd/yy
Prog: XXXXXXXX      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Time: hh:mm:ss
                             View Authorizations

  Search Acct Id: ___________
  Name:  XXXXXXXXXXXXXXXXXXXXXXXXX         Customer Id:  XXXXXXXXX
         XXXXXXXXXXXXXXXXXXXXXXXXX         Acct Status:  X
         XXXXXXXXXXXXXXXXXXXXXXXXX
         PH:  XXXXXXXXXXXXX                Approval # :  XXX   Decline #:  XXX

     Credit Lim:                  Cash Lim:              Appr Amt:
     Credit Bal:                  Cash Bal:              Decl Amt:

 Sel    Transaction ID      Date       Time     Type   A/D  STS      Amount
 ---   ----------------   --------  --------    ----   ---  ---   ------------






           Type
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
ENTER=Continue  F3=Back  F7=Backward  F8=Forwar-
```

## Fields

| Field | Row | Col | Len | Attributes | Color | Initial | Evidence |
|---|---|---|---|---|---|---|---|
|  | 1 | 1 | 5 | (ASKIP,NORM) | BLUE | Tran: | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:29 |
| TRNNAME | 1 | 7 | 4 | (ASKIP,FSET,NORM) | BLUE |  | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:34 |
| TITLE01 | 1 | 21 | 40 | (ASKIP,FSET,NORM) | YELLOW |  | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:38 |
|  | 1 | 65 | 5 | (ASKIP,NORM) | BLUE | Date: | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:42 |
| CURDATE | 1 | 71 | 8 | (ASKIP,FSET,NORM) | BLUE | mm/dd/yy | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:47 |
|  | 2 | 1 | 5 | (ASKIP,NORM) | BLUE | Prog: | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:52 |
| PGMNAME | 2 | 7 | 8 | (ASKIP,FSET,NORM) | BLUE |  | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:57 |
| TITLE02 | 2 | 21 | 40 | (ASKIP,FSET,NORM) | YELLOW |  | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:61 |
|  | 2 | 65 | 5 | (ASKIP,NORM) | BLUE | Time: | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:65 |
| CURTIME | 2 | 71 | 8 | (ASKIP,FSET,NORM) | BLUE | hh:mm:ss | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:70 |
|  | 3 | 30 | 19 |  | NEUTRAL | View Authorizations | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:75 |
|  | 5 | 3 | 15 | (ASKIP,NORM) | TURQUOISE | Search Acct Id: | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:79 |
| ACCTID | 5 | 19 | 11 | (FSET,NORM,UNPROT) | GREEN |  | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:84 |
|  | 5 | 31 | 0 | (ASKIP,NORM) |  |  | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:89 |
|  | 6 | 3 | 6 |  | DEFAULT | Name:  | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:92 |
| CNAME | 6 | 10 | 25 | (ASKIP,NORM) | BLUE |  | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:96 |
|  | 6 | 44 | 13 |  |  | Customer Id:  | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:100 |
| CUSTID | 6 | 58 | 9 | (ASKIP,NORM) | BLUE |  | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:103 |
| ADDR001 | 7 | 10 | 25 | (ASKIP,NORM) | BLUE |  | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:107 |
|  | 7 | 44 | 13 |  |  | Acct Status:  | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:111 |
| ACCSTAT | 7 | 58 | 1 | (ASKIP,NORM) | BLUE |  | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:114 |
| ADDR002 | 8 | 10 | 25 | (ASKIP,NORM) | BLUE |  | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:118 |
|  | 9 | 10 | 3 |  |  | PH: | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:122 |
| PHONE1 | 9 | 15 | 13 | (ASKIP,NORM) | BLUE |  | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:125 |
|  | 9 | 44 | 13 |  |  | Approval # :  | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:129 |
| APPRCNT | 9 | 58 | 3 | (ASKIP,NORM) | BLUE |  | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:132 |
|  | 9 | 64 | 10 |  |  | Decline #: | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:136 |
| DECLCNT | 9 | 76 | 3 | (ASKIP,NORM) | BLUE |  | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:139 |
|  | 11 | 6 | 11 |  | DEFAULT | Credit Lim: | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:143 |
| CREDLIM | 11 | 19 | 12 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:147 |
|  | 11 | 35 | 9 |  | DEFAULT | Cash Lim: | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:152 |
| CASHLIM | 11 | 46 | 9 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:156 |
|  | 11 | 58 | 9 |  | DEFAULT | Appr Amt: | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:161 |
| APPRAMT | 11 | 69 | 10 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:165 |
|  | 12 | 6 | 11 |  | DEFAULT | Credit Bal: | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:170 |
| CREDBAL | 12 | 19 | 12 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:174 |
|  | 12 | 35 | 9 |  | DEFAULT | Cash Bal: | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:179 |
| CASHBAL | 12 | 46 | 9 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:183 |
|  | 12 | 58 | 9 |  | DEFAULT | Decl Amt: | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:188 |
| DECLAMT | 12 | 69 | 10 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:192 |
|  | 14 | 2 | 3 | (ASKIP,NORM) | NEUTRAL | Sel | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:197 |
|  | 14 | 8 | 16 | (ASKIP,NORM) | NEUTRAL |  Transaction ID  | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:202 |
|  | 14 | 27 | 8 | (ASKIP,NORM) | NEUTRAL |   Date   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:207 |
|  | 14 | 38 | 8 | (ASKIP,NORM) | NEUTRAL |   Time   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:212 |
|  | 14 | 49 | 5 | (ASKIP,NORM) | NEUTRAL | Type  | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:217 |
|  | 14 | 56 | 3 | (ASKIP,NORM) | NEUTRAL | A/D | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:222 |
|  | 14 | 61 | 3 | (ASKIP,NORM) | NEUTRAL | STS | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:227 |
|  | 14 | 67 | 12 | (ASKIP,NORM) | NEUTRAL |    Amount    | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:232 |
|  | 15 | 2 | 3 | (ASKIP,NORM) | NEUTRAL | --- | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:237 |
|  | 15 | 8 | 16 | (ASKIP,NORM) | NEUTRAL | ---------------- | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:242 |
|  | 15 | 27 | 8 | (ASKIP,NORM) | NEUTRAL | -------- | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:247 |
|  | 15 | 37 | 8 | (ASKIP,NORM) | NEUTRAL | -------- | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:252 |
|  | 15 | 49 | 4 | (ASKIP,NORM) | NEUTRAL | ---- | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:257 |
|  | 15 | 56 | 3 | (ASKIP,NORM) | NEUTRAL | --- | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:262 |
|  | 15 | 61 | 3 | (ASKIP,NORM) | NEUTRAL | --- | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:267 |
|  | 15 | 67 | 12 | (ASKIP,NORM) | NEUTRAL | ------------ | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:272 |
| SEL0001 | 16 | 3 | 1 | (FSET,NORM,UNPROT) | GREEN |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:277 |
|  | 16 | 5 | 0 | (ASKIP,NORM) |  |  | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:283 |
| TRNID01 | 16 | 8 | 16 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:286 |
| PDATE01 | 16 | 27 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:291 |
| PTIME01 | 16 | 38 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:296 |
| PTYPE01 | 16 | 49 | 4 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:301 |
| PAPRV01 | 16 | 58 | 1 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:306 |
| PSTAT01 | 16 | 63 | 1 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:311 |
| PAMT001 | 16 | 67 | 12 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:316 |
| SEL0002 | 17 | 3 | 1 | (FSET,NORM,UNPROT) | GREEN |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:321 |
|  | 17 | 5 | 0 | (ASKIP,NORM) |  |  | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:327 |
| TRNID02 | 17 | 8 | 16 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:330 |
| PDATE02 | 17 | 27 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:335 |
| PTIME02 | 17 | 38 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:340 |
| PTYPE02 | 17 | 49 | 4 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:345 |
| PAPRV02 | 17 | 58 | 1 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:350 |
| PSTAT02 | 17 | 63 | 1 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:355 |
| PAMT002 | 17 | 67 | 12 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:360 |
| SEL0003 | 18 | 3 | 1 | (FSET,NORM,UNPROT) | GREEN |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:365 |
|  | 18 | 5 | 0 | (ASKIP,NORM) |  |  | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:371 |
| TRNID03 | 18 | 8 | 16 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:374 |
| PDATE03 | 18 | 27 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:379 |
| PTIME03 | 18 | 38 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:384 |
| PTYPE03 | 18 | 49 | 4 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:389 |
| PAPRV03 | 18 | 58 | 1 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:394 |
| PSTAT03 | 18 | 63 | 1 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:399 |
| PAMT003 | 18 | 67 | 12 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:404 |
| SEL0004 | 19 | 3 | 1 | (FSET,NORM,UNPROT) | GREEN |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:409 |
|  | 19 | 5 | 0 | (ASKIP,NORM) |  |  | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:415 |
| TRNID04 | 19 | 8 | 16 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:418 |
| PDATE04 | 19 | 27 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:423 |
| PTIME04 | 19 | 38 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:428 |
| PTYPE04 | 19 | 49 | 4 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:433 |
| PAPRV04 | 19 | 58 | 1 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:438 |
| PSTAT04 | 19 | 63 | 1 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:443 |
| PAMT004 | 19 | 67 | 12 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:448 |
| TRNID05 | 20 | 8 | 16 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:453 |
| PDATE05 | 20 | 27 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:458 |
| PTIME05 | 20 | 38 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:463 |
| PTYPE05 | 20 | 49 | 4 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:468 |
| PAPRV05 | 20 | 58 | 1 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:473 |
| PSTAT05 | 20 | 63 | 1 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:478 |
| PAMT005 | 20 | 67 | 12 | (ASKIP,FSET,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:483 |
| SEL0005 | 20 | 3 | 1 | (FSET,NORM,UNPROT) | GREEN |   | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:488 |
|  | 20 | 5 | 0 | (ASKIP,NORM) |  |  | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:494 |
|  | 22 | 12 | 52 | (ASKIP,BRT) | NEUTRAL | Type  | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:497 |
| ERRMSG | 23 | 1 | 78 | (ASKIP,BRT,FSET) | RED |  | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:503 |
|  | 24 | 1 | 48 | (ASKIP,NORM) | YELLOW | ENTER=Continue  F3=Back  F7=Backward  F8=Forwar- d | app/app-authorization-ims-db2-mq/bms/COPAU00.bms:507 |

## Function keys

| Key | Action | Target | Evidence |
|---|---|---|---|
| DFHENTER | WHEN DFHENTER |  | app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:225 |
| DFHPF3 | WHEN DFHPF3 |  | app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:235 |
| DFHPF7 | WHEN DFHPF7 |  | app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:239 |
| DFHPF8 | WHEN DFHPF8 |  | app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:242 |

## Validation and messages

Message literals for these programs are indexed in [Error handling](../../12-error-handling-messages.md).

## Behaviour

See the program specifications linked from the transaction catalog for first-time display and AID handling.

## Sources

- `app/app-authorization-ims-db2-mq/bms/COPAU00.bms:19`
- `docs/_work/online/screens/COPAU00.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
