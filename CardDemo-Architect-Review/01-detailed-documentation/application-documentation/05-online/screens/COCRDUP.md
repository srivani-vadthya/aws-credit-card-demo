# Screen COCRDUP

| Item | Value |
|---|---|
| Mapset | COCRDUP |
| Maps | CCRDUPA |
| Source | app/bms/COCRDUP.bms:20 |
| Module | base |
| Programs |  |
| Transactions |  |

## Purpose

Mapset COCRDUP is defined in the BMS source cited below. Field text in the mockup comes from BMS INITIAL and POS values already extracted.

## Map CCRDUPA

## Layout mockup

```text
Tran: XXXX          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Date: mm/dd/yy
Prog: XXXXXXXX      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Time: hh:mm:ss

                             Update Credit Card Details


                      Account Number    :   XXXXXXXXXXX
                      Card Number       :   ________________


   Name on card      :  __________________________________________________

   Card Active Y/N   :  _

   Expiry Date       :  __ / ____  XX




                        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
ENTER=Process F3=Exit F5=Save F12=Cancel
```

## Fields

| Field | Row | Col | Len | Attributes | Color | Initial | Evidence |
|---|---|---|---|---|---|---|---|
|  | 1 | 1 | 5 | (ASKIP,NORM) | BLUE | Tran: | app/bms/COCRDUP.bms:29 |
| TRNNAME | 1 | 7 | 4 | (ASKIP,FSET,NORM) | BLUE |  | app/bms/COCRDUP.bms:34 |
| TITLE01 | 1 | 21 | 40 | (ASKIP,NORM) | YELLOW |  | app/bms/COCRDUP.bms:38 |
|  | 1 | 65 | 5 | (ASKIP,NORM) | BLUE | Date: | app/bms/COCRDUP.bms:42 |
| CURDATE | 1 | 71 | 8 | (ASKIP,NORM) | BLUE | mm/dd/yy | app/bms/COCRDUP.bms:47 |
|  | 2 | 1 | 5 | (ASKIP,NORM) | BLUE | Prog: | app/bms/COCRDUP.bms:52 |
| PGMNAME | 2 | 7 | 8 | (ASKIP,NORM) | BLUE |  | app/bms/COCRDUP.bms:57 |
| TITLE02 | 2 | 21 | 40 | (ASKIP,NORM) | YELLOW |  | app/bms/COCRDUP.bms:61 |
|  | 2 | 65 | 5 | (ASKIP,NORM) | BLUE | Time: | app/bms/COCRDUP.bms:65 |
| CURTIME | 2 | 71 | 8 | (ASKIP,NORM) | BLUE | hh:mm:ss | app/bms/COCRDUP.bms:70 |
|  | 4 | 30 | 26 |  | NEUTRAL | Update Credit Card Details | app/bms/COCRDUP.bms:75 |
|  | 7 | 23 | 19 | (ASKIP,NORM) | TURQUOISE | Account Number    : | app/bms/COCRDUP.bms:79 |
| ACCTSID | 7 | 45 | 11 | (FSET,IC,NORM,PROT) | DEFAULT |  | app/bms/COCRDUP.bms:84 |
|  | 7 | 57 | 0 |  |  |  | app/bms/COCRDUP.bms:89 |
|  | 8 | 23 | 19 | (ASKIP,NORM) | TURQUOISE | Card Number       : | app/bms/COCRDUP.bms:91 |
| CARDSID | 8 | 45 | 16 | (FSET,NORM,UNPROT) | DEFAULT |  | app/bms/COCRDUP.bms:96 |
|  | 8 | 62 | 0 |  |  |  | app/bms/COCRDUP.bms:101 |
|  | 11 | 4 | 20 |  | TURQUOISE | Name on card      : | app/bms/COCRDUP.bms:103 |
| CRDNAME | 11 | 25 | 50 | (UNPROT) |  |  | app/bms/COCRDUP.bms:107 |
|  | 11 | 76 | 0 |  |  |  | app/bms/COCRDUP.bms:111 |
|  | 13 | 4 | 20 |  | TURQUOISE | Card Active Y/N   :  | app/bms/COCRDUP.bms:113 |
| CRDSTCD | 13 | 25 | 1 | (UNPROT) |  |  | app/bms/COCRDUP.bms:117 |
|  | 13 | 27 | 0 |  |  |  | app/bms/COCRDUP.bms:121 |
|  | 15 | 4 | 20 |  | TURQUOISE | Expiry Date       :  | app/bms/COCRDUP.bms:123 |
| EXPMON | 15 | 25 | 2 | (UNPROT) |  |  | app/bms/COCRDUP.bms:127 |
|  | 15 | 28 | 1 |  |  | / | app/bms/COCRDUP.bms:132 |
| EXPYEAR | 15 | 30 | 4 | (UNPROT) |  |  | app/bms/COCRDUP.bms:135 |
|  | 15 | 35 | 0 |  |  |  | app/bms/COCRDUP.bms:140 |
| EXPDAY | 15 | 36 | 2 | (DRK,FSET,PROT) |  |  | app/bms/COCRDUP.bms:142 |
|  | 15 | 39 | 0 |  |  |  | app/bms/COCRDUP.bms:147 |
| INFOMSG | 20 | 25 | 40 | (PROT) | NEUTRAL |  | app/bms/COCRDUP.bms:149 |
| ERRMSG | 23 | 1 | 80 | (ASKIP,BRT,FSET) | RED |  | app/bms/COCRDUP.bms:154 |
| FKEYS | 24 | 1 | 21 | (ASKIP,NORM) | YELLOW | ENTER=Process F3=Exit | app/bms/COCRDUP.bms:158 |
| FKEYSC | 24 | 23 | 18 | (ASKIP,DRK) | YELLOW | F5=Save F12=Cancel | app/bms/COCRDUP.bms:163 |

## Function keys

| Key | Action | Target | Evidence |
|---|---|---|---|
|   |   |   |   |

## Validation and messages

Message literals for these programs are indexed in [Error handling](../../12-error-handling-messages.md).

## Behaviour

See the program specifications linked from the transaction catalog for first-time display and AID handling.

## Sources

- `app/bms/COCRDUP.bms:20`
- `docs/_work/online/screens/COCRDUP.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
