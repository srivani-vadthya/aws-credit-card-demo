# Screen COPAU01

| Item | Value |
|---|---|
| Mapset | COPAU01 |
| Maps | COPAU1A |
| Source | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:19 |
| Module | auth |
| Programs | COPAUS1C |
| Transactions | CPVD |

## Purpose

Mapset COPAU01 is defined in the BMS source cited below. Field text in the mockup comes from BMS INITIAL and POS values already extracted.

## Map COPAU1A

## Layout mockup

```text
Tran: XXXX          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Date: mm/dd/yy
Prog: XXXXXXXX      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Time: hh:mm:ss

                          View Authorization Details


 Card #:  XXXXXXXXXXXXXXXX    Auth Date:               Auth Time:

 Auth Resp:      Resp Reason:                          Auth Code:

 Amount:                    POS Entry Mode:            Source   :

 MCC Code:              Card Exp. Date:            Auth Type:

 Tran Id:                     Match Status:        Fraud Status:

 Merchant Details ------------------------------- ---------------------------

 Name:                                  Merchant ID:

 City:                                  State:        Zip:

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
 F3=Back  F5=Mark/Remove Fraud  F8=Next Auth
```

## Fields

| Field | Row | Col | Len | Attributes | Color | Initial | Evidence |
|---|---|---|---|---|---|---|---|
|  | 1 | 1 | 5 | (ASKIP,NORM) | BLUE | Tran: | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:29 |
| TRNNAME | 1 | 7 | 4 | (ASKIP,NORM) | BLUE |  | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:34 |
| TITLE01 | 1 | 21 | 40 | (ASKIP,NORM) | YELLOW |  | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:38 |
|  | 1 | 65 | 5 | (ASKIP,NORM) | BLUE | Date: | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:42 |
| CURDATE | 1 | 71 | 8 | (ASKIP,NORM) | BLUE | mm/dd/yy | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:47 |
|  | 2 | 1 | 5 | (ASKIP,NORM) | BLUE | Prog: | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:52 |
| PGMNAME | 2 | 7 | 8 | (ASKIP,NORM) | BLUE |  | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:57 |
| TITLE02 | 2 | 21 | 40 | (ASKIP,NORM) | YELLOW |  | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:61 |
|  | 2 | 65 | 5 | (ASKIP,NORM) | BLUE | Time: | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:65 |
| CURTIME | 2 | 71 | 8 | (ASKIP,NORM) | BLUE | hh:mm:ss | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:70 |
|  | 4 | 27 | 26 | (ASKIP,BRT) | NEUTRAL | View Authorization Details | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:75 |
|  | 7 | 2 | 7 | (ASKIP,NORM) | TURQUOISE | Card #: | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:80 |
| CARDNUM | 7 | 11 | 16 | (ASKIP,NORM) | PINK |  | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:85 |
|  | 7 | 31 | 10 | (ASKIP,NORM) | TURQUOISE | Auth Date: | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:89 |
| AUTHDT | 7 | 43 | 10 | (ASKIP,NORM) | PINK |   | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:94 |
|  | 7 | 56 | 10 | (ASKIP,NORM) | TURQUOISE | Auth Time: | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:99 |
| AUTHTM | 7 | 68 | 10 | (ASKIP,NORM) | PINK |   | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:104 |
|  | 9 | 2 | 10 | (ASKIP,NORM) | TURQUOISE | Auth Resp: | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:109 |
| AUTHRSP | 9 | 14 | 1 | (ASKIP,NORM) | PINK |   | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:114 |
|  | 9 | 18 | 12 | (ASKIP,NORM) | TURQUOISE | Resp Reason: | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:119 |
| AUTHRSN | 9 | 32 | 20 | (ASKIP,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:124 |
|  | 9 | 56 | 10 | (ASKIP,NORM) | TURQUOISE | Auth Code: | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:129 |
| AUTHCD | 9 | 68 | 6 | (ASKIP,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:134 |
|  | 11 | 2 | 7 | (ASKIP,NORM) | TURQUOISE | Amount: | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:139 |
| AUTHAMT | 11 | 11 | 12 | (ASKIP,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:144 |
|  | 11 | 29 | 15 | (ASKIP,NORM) | TURQUOISE | POS Entry Mode: | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:149 |
| POSEMD | 11 | 46 | 4 | (ASKIP,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:154 |
|  | 11 | 56 | 10 | (ASKIP,NORM) | TURQUOISE | Source   : | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:159 |
| AUTHSRC | 11 | 68 | 10 | (ASKIP,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:164 |
|  | 13 | 2 | 9 | (ASKIP,NORM) | TURQUOISE | MCC Code: | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:169 |
| MCCCD | 13 | 13 | 4 | (ASKIP,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:174 |
|  | 13 | 25 | 15 | (ASKIP,NORM) | TURQUOISE | Card Exp. Date: | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:179 |
| CRDEXP | 13 | 42 | 5 | (ASKIP,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:184 |
|  | 13 | 52 | 10 | (ASKIP,NORM) | TURQUOISE | Auth Type: | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:189 |
| AUTHTYP | 13 | 64 | 14 | (ASKIP,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:194 |
|  | 15 | 2 | 18 | (ASKIP,NORM) | TURQUOISE | Tran Id: | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:199 |
| TRNID | 15 | 12 | 15 | (ASKIP,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:204 |
|  | 15 | 31 | 13 | (ASKIP,NORM) | TURQUOISE | Match Status: | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:209 |
| AUTHMTC | 15 | 46 | 1 | (ASKIP,NORM) | RED |   | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:214 |
|  | 15 | 52 | 13 | (ASKIP,NORM) | TURQUOISE | Fraud Status: | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:219 |
| AUTHFRD | 15 | 67 | 10 | (ASKIP,NORM) | RED |   | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:224 |
|  | 17 | 2 | 76 |  | NEUTRAL | Merchant Details ------------------------------- ----------------------------- | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:229 |
|  | 19 | 2 | 5 | (ASKIP,NORM) | TURQUOISE | Name: | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:234 |
| MERNAME | 19 | 9 | 25 | (ASKIP,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:239 |
|  | 19 | 41 | 12 | (ASKIP,NORM) | TURQUOISE | Merchant ID: | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:244 |
| MERID | 19 | 55 | 15 | (ASKIP,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:249 |
|  | 21 | 2 | 5 | (ASKIP,NORM) | TURQUOISE | City: | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:254 |
| MERCITY | 21 | 9 | 25 | (ASKIP,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:259 |
|  | 21 | 41 | 6 | (ASKIP,NORM) | TURQUOISE | State: | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:264 |
| MERST | 21 | 49 | 2 | (ASKIP,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:269 |
|  | 21 | 55 | 4 | (ASKIP,NORM) | TURQUOISE | Zip: | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:274 |
| MERZIP | 21 | 61 | 10 | (ASKIP,NORM) | BLUE |   | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:279 |
| ERRMSG | 23 | 1 | 78 | (ASKIP,BRT,FSET) | RED |  | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:284 |
|  | 24 | 1 | 45 | (ASKIP,NORM) | YELLOW |  F3=Back  F5=Mark/Remove Fraud  F8=Next Auth | app/app-authorization-ims-db2-mq/bms/COPAU01.bms:288 |

## Function keys

| Key | Action | Target | Evidence |
|---|---|---|---|
| DFHENTER | WHEN DFHENTER |  | app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:181 |
| DFHPF3 | WHEN DFHPF3 |  | app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:184 |
| DFHPF5 | WHEN DFHPF5 |  | app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:187 |
| DFHPF8 | WHEN DFHPF8 |  | app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:190 |

## Validation and messages

Message literals for these programs are indexed in [Error handling](../../12-error-handling-messages.md).

## Behaviour

See the program specifications linked from the transaction catalog for first-time display and AID handling.

## Sources

- `app/app-authorization-ims-db2-mq/bms/COPAU01.bms:19`
- `docs/_work/online/screens/COPAU01.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
