# Screen COTRTUP

| Item | Value |
|---|---|
| Mapset | COTRTUP |
| Maps | CTRTUPA |
| Source | app/app-transaction-type-db2/bms/COTRTUP.bms:20 |
| Module | trantype |
| Programs |  |
| Transactions |  |

## Purpose

Mapset COTRTUP is defined in the BMS source cited below. Field text in the mockup comes from BMS INITIAL and POS values already extracted.

## Map CTRTUPA

## Layout mockup

```text
Tran: XXXX          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Date: mm/dd/yy
Prog: XXXXXXXX      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Time: hh:mm:ss




                           Maintain Transaction Type




   Transaction Type  :   __

   Description       :   __________________________________________________







                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
ENTER=Process F3=Exit F4=Delete F5=Save   F6=Add                    F12=Cancel
```

## Fields

| Field | Row | Col | Len | Attributes | Color | Initial | Evidence |
|---|---|---|---|---|---|---|---|
|  | 1 | 1 | 5 | (ASKIP,NORM) | BLUE | Tran: | app/app-transaction-type-db2/bms/COTRTUP.bms:29 |
| TRNNAME | 1 | 7 | 4 | (ASKIP,FSET,NORM) | BLUE |  | app/app-transaction-type-db2/bms/COTRTUP.bms:34 |
| TITLE01 | 1 | 21 | 40 | (ASKIP,NORM) | YELLOW |  | app/app-transaction-type-db2/bms/COTRTUP.bms:38 |
|  | 1 | 65 | 5 | (ASKIP,NORM) | BLUE | Date: | app/app-transaction-type-db2/bms/COTRTUP.bms:42 |
| CURDATE | 1 | 71 | 8 | (ASKIP,NORM) | BLUE | mm/dd/yy | app/app-transaction-type-db2/bms/COTRTUP.bms:47 |
|  | 2 | 1 | 5 | (ASKIP,NORM) | BLUE | Prog: | app/app-transaction-type-db2/bms/COTRTUP.bms:52 |
| PGMNAME | 2 | 7 | 8 | (ASKIP,NORM) | BLUE |  | app/app-transaction-type-db2/bms/COTRTUP.bms:57 |
| TITLE02 | 2 | 21 | 40 | (ASKIP,NORM) | YELLOW |  | app/app-transaction-type-db2/bms/COTRTUP.bms:61 |
|  | 2 | 65 | 5 | (ASKIP,NORM) | BLUE | Time: | app/app-transaction-type-db2/bms/COTRTUP.bms:65 |
| CURTIME | 2 | 71 | 8 | (ASKIP,NORM) | BLUE | hh:mm:ss | app/app-transaction-type-db2/bms/COTRTUP.bms:70 |
|  | 7 | 28 | 25 |  | NEUTRAL | Maintain Transaction Type | app/app-transaction-type-db2/bms/COTRTUP.bms:75 |
|  | 12 | 4 | 19 | (ASKIP,NORM) | TURQUOISE | Transaction Type  : | app/app-transaction-type-db2/bms/COTRTUP.bms:79 |
| TRTYPCD | 12 | 26 | 2 | (IC,UNPROT) |  |  | app/app-transaction-type-db2/bms/COTRTUP.bms:84 |
|  | 12 | 29 | 0 |  |  |  | app/app-transaction-type-db2/bms/COTRTUP.bms:88 |
|  | 14 | 4 | 19 |  | TURQUOISE | Description       : | app/app-transaction-type-db2/bms/COTRTUP.bms:90 |
| TRTYDSC | 14 | 26 | 50 | (UNPROT) |  |  | app/app-transaction-type-db2/bms/COTRTUP.bms:94 |
|  | 14 | 77 | 0 |  |  |  | app/app-transaction-type-db2/bms/COTRTUP.bms:98 |
| INFOMSG | 22 | 23 | 45 | (ASKIP) | NEUTRAL |  | app/app-transaction-type-db2/bms/COTRTUP.bms:100 |
|  | 22 | 69 | 0 |  |  |  | app/app-transaction-type-db2/bms/COTRTUP.bms:105 |
| ERRMSG | 23 | 1 | 78 | (ASKIP,BRT,FSET) | RED |  | app/app-transaction-type-db2/bms/COTRTUP.bms:107 |
| FKEYS | 24 | 1 | 21 | (ASKIP,NORM) | YELLOW | ENTER=Process F3=Exit | app/app-transaction-type-db2/bms/COTRTUP.bms:111 |
| FKEY04 | 24 | 23 | 9 | (ASKIP,DRK) | YELLOW | F4=Delete | app/app-transaction-type-db2/bms/COTRTUP.bms:116 |
| FKEY05 | 24 | 33 | 8 | (ASKIP,DRK) | YELLOW | F5=Save | app/app-transaction-type-db2/bms/COTRTUP.bms:121 |
| FKEY06 | 24 | 43 | 6 | (ASKIP,DRK) | YELLOW | F6=Add | app/app-transaction-type-db2/bms/COTRTUP.bms:126 |
| FKEY12 | 24 | 69 | 10 | (ASKIP,DRK) | YELLOW | F12=Cancel | app/app-transaction-type-db2/bms/COTRTUP.bms:131 |

## Function keys

| Key | Action | Target | Evidence |
|---|---|---|---|
|   |   |   |   |

## Validation and messages

Message literals for these programs are indexed in [Error handling](../../12-error-handling-messages.md).

## Behaviour

See the program specifications linked from the transaction catalog for first-time display and AID handling.

## Sources

- `app/app-transaction-type-db2/bms/COTRTUP.bms:20`
- `docs/_work/online/screens/COTRTUP.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
