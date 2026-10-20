# Screen CORPT00

| Item | Value |
|---|---|
| Mapset | CORPT00 |
| Maps | CORPT0A |
| Source | app/bms/CORPT00.bms:19 |
| Module | base |
| Programs | CORPT00C |
| Transactions | CR00 |

## Purpose

Mapset CORPT00 is defined in the BMS source cited below. Field text in the mockup comes from BMS INITIAL and POS values already extracted.

## Map CORPT0A

## Layout mockup

```text
Tran: XXXX          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Date: mm/dd/yy
Prog: XXXXXXXX      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Time: hh:mm:ss

                             Transaction Reports


              Monthly (Current Month)

              Yearly (Current Year)

              Custom (Date Range)

              Start Date :     /    /        (MM/DD/YYYY)
                End Date :     /    /        (MM/DD/YYYY)




     The Report will be submitted for printing. Plea- se confirm _  (Y/N)



XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
ENTER=Continue  F3=Back
```

## Fields

| Field | Row | Col | Len | Attributes | Color | Initial | Evidence |
|---|---|---|---|---|---|---|---|
|  | 1 | 1 | 5 | (ASKIP,NORM) | BLUE | Tran: | app/bms/CORPT00.bms:29 |
| TRNNAME | 1 | 7 | 4 | (ASKIP,FSET,NORM) | BLUE |  | app/bms/CORPT00.bms:34 |
| TITLE01 | 1 | 21 | 40 | (ASKIP,FSET,NORM) | YELLOW |  | app/bms/CORPT00.bms:38 |
|  | 1 | 65 | 5 | (ASKIP,NORM) | BLUE | Date: | app/bms/CORPT00.bms:42 |
| CURDATE | 1 | 71 | 8 | (ASKIP,FSET,NORM) | BLUE | mm/dd/yy | app/bms/CORPT00.bms:47 |
|  | 2 | 1 | 5 | (ASKIP,NORM) | BLUE | Prog: | app/bms/CORPT00.bms:52 |
| PGMNAME | 2 | 7 | 8 | (ASKIP,FSET,NORM) | BLUE |  | app/bms/CORPT00.bms:57 |
| TITLE02 | 2 | 21 | 40 | (ASKIP,FSET,NORM) | YELLOW |  | app/bms/CORPT00.bms:61 |
|  | 2 | 65 | 5 | (ASKIP,NORM) | BLUE | Time: | app/bms/CORPT00.bms:65 |
| CURTIME | 2 | 71 | 8 | (ASKIP,FSET,NORM) | BLUE | hh:mm:ss | app/bms/CORPT00.bms:70 |
|  | 4 | 30 | 19 | (ASKIP,BRT) | NEUTRAL | Transaction Reports | app/bms/CORPT00.bms:75 |
| MONTHLY | 7 | 10 | 1 | (FSET,IC,NORM,UNPROT) | GREEN |   | app/bms/CORPT00.bms:80 |
|  | 7 | 12 | 0 | (ASKIP,NORM) |  |  | app/bms/CORPT00.bms:86 |
|  | 7 | 15 | 23 | (ASKIP,BRT) | TURQUOISE | Monthly (Current Month) | app/bms/CORPT00.bms:89 |
| YEARLY | 9 | 10 | 1 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/CORPT00.bms:94 |
|  | 9 | 12 | 0 | (ASKIP,NORM) |  |  | app/bms/CORPT00.bms:100 |
|  | 9 | 15 | 23 | (ASKIP,BRT) | TURQUOISE | Yearly (Current Year) | app/bms/CORPT00.bms:103 |
| CUSTOM | 11 | 10 | 1 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/CORPT00.bms:108 |
|  | 11 | 12 | 0 | (ASKIP,NORM) |  |  | app/bms/CORPT00.bms:114 |
|  | 11 | 15 | 23 | (ASKIP,BRT) | TURQUOISE | Custom (Date Range) | app/bms/CORPT00.bms:117 |
|  | 13 | 15 | 12 | (ASKIP,NORM) | TURQUOISE | Start Date : | app/bms/CORPT00.bms:122 |
| SDTMM | 13 | 29 | 2 | (FSET,NORM,NUM,UNPROT) | GREEN |    | app/bms/CORPT00.bms:127 |
|  | 13 | 32 | 1 | (ASKIP,NORM) | BLUE | / | app/bms/CORPT00.bms:133 |
| SDTDD | 13 | 34 | 2 | (FSET,NORM,NUM,UNPROT) | GREEN |    | app/bms/CORPT00.bms:138 |
|  | 13 | 37 | 1 | (ASKIP,NORM) | BLUE | / | app/bms/CORPT00.bms:144 |
| SDTYYYY | 13 | 39 | 4 | (FSET,NORM,NUM,UNPROT) | GREEN |      | app/bms/CORPT00.bms:149 |
|  | 13 | 44 | 0 |  |  |  | app/bms/CORPT00.bms:155 |
|  | 13 | 46 | 12 |  | BLUE | (MM/DD/YYYY) | app/bms/CORPT00.bms:157 |
|  | 14 | 15 | 12 | (ASKIP,NORM) | TURQUOISE |   End Date : | app/bms/CORPT00.bms:161 |
| EDTMM | 14 | 29 | 2 | (FSET,NORM,NUM,UNPROT) | GREEN |    | app/bms/CORPT00.bms:166 |
|  | 14 | 32 | 1 | (ASKIP,NORM) | BLUE | / | app/bms/CORPT00.bms:172 |
| EDTDD | 14 | 34 | 2 | (FSET,NORM,NUM,UNPROT) | GREEN |    | app/bms/CORPT00.bms:177 |
|  | 14 | 37 | 1 | (ASKIP,NORM) | BLUE | / | app/bms/CORPT00.bms:183 |
| EDTYYYY | 14 | 39 | 4 | (FSET,NORM,NUM,UNPROT) | GREEN |      | app/bms/CORPT00.bms:188 |
|  | 14 | 44 | 0 |  |  |  | app/bms/CORPT00.bms:194 |
|  | 14 | 46 | 12 |  | BLUE | (MM/DD/YYYY) | app/bms/CORPT00.bms:196 |
|  | 19 | 6 | 59 | (ASKIP,NORM) | TURQUOISE | The Report will be submitted for printing. Plea- se confirm:  | app/bms/CORPT00.bms:200 |
| CONFIRM | 19 | 66 | 1 | (FSET,NORM,UNPROT) | GREEN |  | app/bms/CORPT00.bms:206 |
|  | 19 | 68 | 0 |  |  |  | app/bms/CORPT00.bms:211 |
|  | 19 | 69 | 5 | (ASKIP,NORM) | NEUTRAL | (Y/N) | app/bms/CORPT00.bms:213 |
| ERRMSG | 23 | 1 | 78 | (ASKIP,BRT,FSET) | RED |  | app/bms/CORPT00.bms:218 |
|  | 24 | 1 | 23 | (ASKIP,NORM) | YELLOW | ENTER=Continue  F3=Back | app/bms/CORPT00.bms:222 |

## Function keys

| Key | Action | Target | Evidence |
|---|---|---|---|
| DFHENTER | WHEN DFHENTER |  | app/cbl/CORPT00C.cbl:185 |
| DFHPF3 | WHEN DFHPF3 |  | app/cbl/CORPT00C.cbl:187 |

## Validation and messages

Message literals for these programs are indexed in [Error handling](../../12-error-handling-messages.md).

## Behaviour

See the program specifications linked from the transaction catalog for first-time display and AID handling.

## Sources

- `app/bms/CORPT00.bms:19`
- `docs/_work/online/screens/CORPT00.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
