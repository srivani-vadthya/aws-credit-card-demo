# Screen COCRDSL

| Item | Value |
|---|---|
| Mapset | COCRDSL |
| Maps | CCRDSLA |
| Source | app/bms/COCRDSL.bms:20 |
| Module | base |
| Programs |  |
| Transactions |  |

## Purpose

Mapset COCRDSL is defined in the BMS source cited below. Field text in the mockup comes from BMS INITIAL and POS values already extracted.

## Map CCRDSLA

## Layout mockup

```text
Tran: XXXX          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Date: mm/dd/yy
Prog: XXXXXXXX      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Time: hh:mm:ss

                             View Credit Card Detail


                      Account Number    :   ___________
                      Card Number       :   ________________


   Name on card      :  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

   Card Active Y/N   :  X

   Expiry Date       :  XX / XXXX




                        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
ENTER=Search Cards  F3=Exit
```

## Fields

| Field | Row | Col | Len | Attributes | Color | Initial | Evidence |
|---|---|---|---|---|---|---|---|
|  | 1 | 1 | 5 | (ASKIP,NORM) | BLUE | Tran: | app/bms/COCRDSL.bms:29 |
| TRNNAME | 1 | 7 | 4 | (ASKIP,FSET,NORM) | BLUE |  | app/bms/COCRDSL.bms:34 |
| TITLE01 | 1 | 21 | 40 | (ASKIP,NORM) | YELLOW |  | app/bms/COCRDSL.bms:38 |
|  | 1 | 65 | 5 | (ASKIP,NORM) | BLUE | Date: | app/bms/COCRDSL.bms:42 |
| CURDATE | 1 | 71 | 8 | (ASKIP,NORM) | BLUE | mm/dd/yy | app/bms/COCRDSL.bms:47 |
|  | 2 | 1 | 5 | (ASKIP,NORM) | BLUE | Prog: | app/bms/COCRDSL.bms:52 |
| PGMNAME | 2 | 7 | 8 | (ASKIP,NORM) | BLUE |  | app/bms/COCRDSL.bms:57 |
| TITLE02 | 2 | 21 | 40 | (ASKIP,NORM) | YELLOW |  | app/bms/COCRDSL.bms:61 |
|  | 2 | 65 | 5 | (ASKIP,NORM) | BLUE | Time: | app/bms/COCRDSL.bms:65 |
| CURTIME | 2 | 71 | 8 | (ASKIP,NORM) | BLUE | hh:mm:ss | app/bms/COCRDSL.bms:70 |
|  | 4 | 30 | 23 |  | NEUTRAL | View Credit Card Detail | app/bms/COCRDSL.bms:75 |
|  | 7 | 23 | 19 | (ASKIP,NORM) | TURQUOISE | Account Number    : | app/bms/COCRDSL.bms:79 |
| ACCTSID | 7 | 45 | 11 | (FSET,IC,NORM,UNPROT) | DEFAULT |  | app/bms/COCRDSL.bms:84 |
|  | 7 | 57 | 0 |  |  |  | app/bms/COCRDSL.bms:89 |
|  | 8 | 23 | 19 | (ASKIP,NORM) | TURQUOISE | Card Number       : | app/bms/COCRDSL.bms:91 |
| CARDSID | 8 | 45 | 16 | (FSET,NORM,UNPROT) | DEFAULT |  | app/bms/COCRDSL.bms:96 |
|  | 8 | 62 | 0 |  |  |  | app/bms/COCRDSL.bms:101 |
|  | 11 | 4 | 20 |  | TURQUOISE | Name on card      : | app/bms/COCRDSL.bms:103 |
| CRDNAME | 11 | 25 | 50 |  |  |  | app/bms/COCRDSL.bms:107 |
|  | 11 | 76 | 0 |  |  |  | app/bms/COCRDSL.bms:110 |
|  | 13 | 4 | 20 |  | TURQUOISE | Card Active Y/N   :  | app/bms/COCRDSL.bms:112 |
| CRDSTCD | 13 | 25 | 1 | (ASKIP) |  |  | app/bms/COCRDSL.bms:116 |
|  | 13 | 27 | 0 |  |  |  | app/bms/COCRDSL.bms:120 |
|  | 15 | 4 | 20 |  | TURQUOISE | Expiry Date       :  | app/bms/COCRDSL.bms:122 |
| EXPMON | 15 | 25 | 2 | (ASKIP) |  |  | app/bms/COCRDSL.bms:126 |
|  | 15 | 28 | 1 |  |  | / | app/bms/COCRDSL.bms:130 |
| EXPYEAR | 15 | 30 | 4 | (ASKIP) |  |  | app/bms/COCRDSL.bms:133 |
|  | 15 | 35 | 0 |  |  |  | app/bms/COCRDSL.bms:137 |
| INFOMSG | 20 | 25 | 40 | (PROT) | NEUTRAL |  | app/bms/COCRDSL.bms:139 |
| ERRMSG | 23 | 1 | 80 | (ASKIP,BRT,FSET) | RED |  | app/bms/COCRDSL.bms:144 |
| FKEYS | 24 | 1 | 75 | (ASKIP,NORM) | YELLOW | ENTER=Search Cards  F3=Exit | app/bms/COCRDSL.bms:148 |

## Function keys

| Key | Action | Target | Evidence |
|---|---|---|---|
|   |   |   |   |

## Validation and messages

Message literals for these programs are indexed in [Error handling](../../12-error-handling-messages.md).

## Behaviour

See the program specifications linked from the transaction catalog for first-time display and AID handling.

## Sources

- `app/bms/COCRDSL.bms:20`
- `docs/_work/online/screens/COCRDSL.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
