# Screen COBIL00

| Item | Value |
|---|---|
| Mapset | COBIL00 |
| Maps | COBIL0A |
| Source | app/bms/COBIL00.bms:19 |
| Module | base |
| Programs | COBIL00C |
| Transactions | CB00 |

## Purpose

Mapset COBIL00 is defined in the BMS source cited below. Field text in the mockup comes from BMS INITIAL and POS values already extracted.

## Map COBIL0A

## Layout mockup

```text
Tran: XXXX          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Date: mm/dd/yy
Prog: XXXXXXXX      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Time: hh:mm:ss

                                  Bill Payment

     Enter Acct ID: ___________

     ------------------------------------------------ ---------------------


     Your current balance is:  XXXXXXXXXXXXXX



     Do you want to pay your balance now. Please con- firm _  (Y/N)







XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
ENTER=Continue  F3=Back  F4=Clear
```

## Fields

| Field | Row | Col | Len | Attributes | Color | Initial | Evidence |
|---|---|---|---|---|---|---|---|
|  | 1 | 1 | 5 | (ASKIP,NORM) | BLUE | Tran: | app/bms/COBIL00.bms:29 |
| TRNNAME | 1 | 7 | 4 | (ASKIP,FSET,NORM) | BLUE |  | app/bms/COBIL00.bms:34 |
| TITLE01 | 1 | 21 | 40 | (ASKIP,FSET,NORM) | YELLOW |  | app/bms/COBIL00.bms:38 |
|  | 1 | 65 | 5 | (ASKIP,NORM) | BLUE | Date: | app/bms/COBIL00.bms:42 |
| CURDATE | 1 | 71 | 8 | (ASKIP,FSET,NORM) | BLUE | mm/dd/yy | app/bms/COBIL00.bms:47 |
|  | 2 | 1 | 5 | (ASKIP,NORM) | BLUE | Prog: | app/bms/COBIL00.bms:52 |
| PGMNAME | 2 | 7 | 8 | (ASKIP,FSET,NORM) | BLUE |  | app/bms/COBIL00.bms:57 |
| TITLE02 | 2 | 21 | 40 | (ASKIP,FSET,NORM) | YELLOW |  | app/bms/COBIL00.bms:61 |
|  | 2 | 65 | 5 | (ASKIP,NORM) | BLUE | Time: | app/bms/COBIL00.bms:65 |
| CURTIME | 2 | 71 | 8 | (ASKIP,FSET,NORM) | BLUE | hh:mm:ss | app/bms/COBIL00.bms:70 |
|  | 4 | 35 | 12 | (ASKIP,BRT) | NEUTRAL | Bill Payment | app/bms/COBIL00.bms:75 |
|  | 6 | 6 | 14 | (ASKIP,NORM) | GREEN | Enter Acct ID: | app/bms/COBIL00.bms:80 |
| ACTIDIN | 6 | 21 | 11 | (FSET,IC,NORM,UNPROT) | GREEN |  | app/bms/COBIL00.bms:85 |
|  | 6 | 33 | 0 | (ASKIP,NORM) |  |  | app/bms/COBIL00.bms:90 |
|  | 8 | 6 | 70 |  | YELLOW | ------------------------------------------------ ----------------------- | app/bms/COBIL00.bms:93 |
|  | 11 | 6 | 25 | (ASKIP,NORM) | TURQUOISE | Your current balance is:  | app/bms/COBIL00.bms:98 |
| CURBAL | 11 | 32 | 14 | (ASKIP,FSET,NORM) | BLUE |  | app/bms/COBIL00.bms:103 |
|  | 11 | 47 | 0 |  |  |  | app/bms/COBIL00.bms:107 |
|  | 15 | 6 | 53 | (ASKIP,NORM) | TURQUOISE | Do you want to pay your balance now. Please con- firm:  | app/bms/COBIL00.bms:109 |
| CONFIRM | 15 | 60 | 1 | (FSET,NORM,UNPROT) | GREEN |  | app/bms/COBIL00.bms:115 |
|  | 15 | 62 | 0 |  |  |  | app/bms/COBIL00.bms:120 |
|  | 15 | 63 | 5 | (ASKIP,NORM) | NEUTRAL | (Y/N) | app/bms/COBIL00.bms:122 |
| ERRMSG | 23 | 1 | 78 | (ASKIP,BRT,FSET) | RED |  | app/bms/COBIL00.bms:127 |
|  | 24 | 1 | 33 | (ASKIP,NORM) | YELLOW | ENTER=Continue  F3=Back  F4=Clear | app/bms/COBIL00.bms:131 |

## Function keys

| Key | Action | Target | Evidence |
|---|---|---|---|
| DFHENTER | WHEN DFHENTER |  | app/cbl/COBIL00C.cbl:126 |
| DFHPF3 | WHEN DFHPF3 |  | app/cbl/COBIL00C.cbl:128 |
| DFHPF4 | WHEN DFHPF4 |  | app/cbl/COBIL00C.cbl:136 |

## Validation and messages

Message literals for these programs are indexed in [Error handling](../../12-error-handling-messages.md).

## Behaviour

See the program specifications linked from the transaction catalog for first-time display and AID handling.

## Sources

- `app/bms/COBIL00.bms:19`
- `docs/_work/online/screens/COBIL00.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
