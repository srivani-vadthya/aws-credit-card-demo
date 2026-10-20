# Screen COTRN02

| Item | Value |
|---|---|
| Mapset | COTRN02 |
| Maps | COTRN2A |
| Source | app/bms/COTRN02.bms:19 |
| Module | base |
| Programs | COTRN02C |
| Transactions | CT02 |

## Purpose

Mapset COTRN02 is defined in the BMS source cited below. Field text in the mockup comes from BMS INITIAL and POS values already extracted.

## Map COTRN2A

## Layout mockup

```text
Tran: XXXX          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Date: mm/dd/yy
Prog: XXXXXXXX      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Time: hh:mm:ss

                             Add Transaction

     Enter Acct #:                  (or)     Card #:  ________________

     ------------------------------------------------ ---------------------

     Type CD:         Category CD:           Source:

     Description:

     Amount:                  Orig Date:                Proc Date:
            (-99999999.99)              (YYYY-MM-DD)              (YYYY-MM-DD)
     Merchant ID:               Merchant Name:

     Merchant City:                                 Merchant Zip:


     You are about to add this transaction. Please c- onfirm  _  (Y/N)

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
ENTER=Continue  F3=Back  F4=Clear  F5=Copy Last- Tran
```

## Fields

| Field | Row | Col | Len | Attributes | Color | Initial | Evidence |
|---|---|---|---|---|---|---|---|
|  | 1 | 1 | 5 | (ASKIP,NORM) | BLUE | Tran: | app/bms/COTRN02.bms:29 |
| TRNNAME | 1 | 7 | 4 | (ASKIP,FSET,NORM) | BLUE |  | app/bms/COTRN02.bms:34 |
| TITLE01 | 1 | 21 | 40 | (ASKIP,FSET,NORM) | YELLOW |  | app/bms/COTRN02.bms:38 |
|  | 1 | 65 | 5 | (ASKIP,NORM) | BLUE | Date: | app/bms/COTRN02.bms:42 |
| CURDATE | 1 | 71 | 8 | (ASKIP,FSET,NORM) | BLUE | mm/dd/yy | app/bms/COTRN02.bms:47 |
|  | 2 | 1 | 5 | (ASKIP,NORM) | BLUE | Prog: | app/bms/COTRN02.bms:52 |
| PGMNAME | 2 | 7 | 8 | (ASKIP,FSET,NORM) | BLUE |  | app/bms/COTRN02.bms:57 |
| TITLE02 | 2 | 21 | 40 | (ASKIP,FSET,NORM) | YELLOW |  | app/bms/COTRN02.bms:61 |
|  | 2 | 65 | 5 | (ASKIP,NORM) | BLUE | Time: | app/bms/COTRN02.bms:65 |
| CURTIME | 2 | 71 | 8 | (ASKIP,FSET,NORM) | BLUE | hh:mm:ss | app/bms/COTRN02.bms:70 |
|  | 4 | 30 | 15 | (ASKIP,BRT) | NEUTRAL | Add Transaction | app/bms/COTRN02.bms:75 |
|  | 6 | 6 | 13 | (ASKIP,NORM) | TURQUOISE | Enter Acct #: | app/bms/COTRN02.bms:80 |
| ACTIDIN | 6 | 21 | 11 | (FSET,IC,NORM,UNPROT) | GREEN |   | app/bms/COTRN02.bms:85 |
|  | 6 | 33 | 0 | (ASKIP,NORM) |  |  | app/bms/COTRN02.bms:91 |
|  | 6 | 37 | 4 | (ASKIP,NORM) | NEUTRAL | (or) | app/bms/COTRN02.bms:94 |
|  | 6 | 46 | 7 | (ASKIP,NORM) | TURQUOISE | Card #: | app/bms/COTRN02.bms:99 |
| CARDNIN | 6 | 55 | 16 | (FSET,NORM,UNPROT) | GREEN |  | app/bms/COTRN02.bms:104 |
|  | 6 | 72 | 0 |  |  |  | app/bms/COTRN02.bms:109 |
|  | 8 | 6 | 70 | (ASKIP,NORM) | NEUTRAL | ------------------------------------------------ ----------------------- | app/bms/COTRN02.bms:111 |
|  | 10 | 6 | 8 | (ASKIP,NORM) | TURQUOISE | Type CD: | app/bms/COTRN02.bms:117 |
| TTYPCD | 10 | 15 | 2 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COTRN02.bms:122 |
|  | 10 | 18 | 0 |  |  |  | app/bms/COTRN02.bms:128 |
|  | 10 | 23 | 12 | (ASKIP,NORM) | TURQUOISE | Category CD: | app/bms/COTRN02.bms:130 |
| TCATCD | 10 | 36 | 4 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COTRN02.bms:135 |
|  | 10 | 41 | 0 |  |  |  | app/bms/COTRN02.bms:141 |
|  | 10 | 46 | 7 | (ASKIP,NORM) | TURQUOISE | Source: | app/bms/COTRN02.bms:143 |
| TRNSRC | 10 | 54 | 10 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COTRN02.bms:148 |
|  | 10 | 65 | 0 |  |  |  | app/bms/COTRN02.bms:154 |
|  | 12 | 6 | 12 | (ASKIP,NORM) | TURQUOISE | Description: | app/bms/COTRN02.bms:156 |
| TDESC | 12 | 19 | 60 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COTRN02.bms:161 |
|  | 12 | 80 | 0 |  |  |  | app/bms/COTRN02.bms:167 |
|  | 14 | 6 | 7 | (ASKIP,NORM) | TURQUOISE | Amount: | app/bms/COTRN02.bms:169 |
| TRNAMT | 14 | 14 | 12 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COTRN02.bms:174 |
|  | 14 | 27 | 0 |  |  |  | app/bms/COTRN02.bms:180 |
|  | 14 | 31 | 10 | (ASKIP,NORM) | TURQUOISE | Orig Date: | app/bms/COTRN02.bms:182 |
| TORIGDT | 14 | 42 | 10 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COTRN02.bms:187 |
|  | 14 | 53 | 0 |  |  |  | app/bms/COTRN02.bms:193 |
|  | 14 | 57 | 10 | (ASKIP,NORM) | TURQUOISE | Proc Date: | app/bms/COTRN02.bms:195 |
| TPROCDT | 14 | 68 | 10 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COTRN02.bms:200 |
|  | 14 | 79 | 0 |  |  |  | app/bms/COTRN02.bms:206 |
|  | 15 | 13 | 14 | (ASKIP,NORM) | BLUE | (-99999999.99) | app/bms/COTRN02.bms:208 |
|  | 15 | 41 | 12 | (ASKIP,NORM) | BLUE | (YYYY-MM-DD) | app/bms/COTRN02.bms:213 |
|  | 15 | 67 | 12 | (ASKIP,NORM) | BLUE | (YYYY-MM-DD) | app/bms/COTRN02.bms:218 |
|  | 16 | 6 | 12 | (ASKIP,NORM) | TURQUOISE | Merchant ID: | app/bms/COTRN02.bms:223 |
| MID | 16 | 19 | 9 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COTRN02.bms:228 |
|  | 16 | 29 | 0 |  |  |  | app/bms/COTRN02.bms:234 |
|  | 16 | 33 | 14 | (ASKIP,NORM) | TURQUOISE | Merchant Name: | app/bms/COTRN02.bms:236 |
| MNAME | 16 | 48 | 30 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COTRN02.bms:241 |
|  | 16 | 79 | 0 |  |  |  | app/bms/COTRN02.bms:247 |
|  | 18 | 6 | 14 | (ASKIP,NORM) | TURQUOISE | Merchant City: | app/bms/COTRN02.bms:249 |
| MCITY | 18 | 21 | 25 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COTRN02.bms:254 |
|  | 18 | 47 | 0 |  |  |  | app/bms/COTRN02.bms:260 |
|  | 18 | 53 | 13 | (ASKIP,NORM) | TURQUOISE | Merchant Zip: | app/bms/COTRN02.bms:262 |
| MZIP | 18 | 67 | 10 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COTRN02.bms:267 |
|  | 18 | 78 | 0 |  |  |  | app/bms/COTRN02.bms:273 |
|  | 21 | 6 | 55 | (ASKIP,NORM) | TURQUOISE | You are about to add this transaction. Please c- onfirm : | app/bms/COTRN02.bms:275 |
| CONFIRM | 21 | 63 | 1 | (FSET,NORM,UNPROT) | GREEN |  | app/bms/COTRN02.bms:281 |
|  | 21 | 65 | 0 |  |  |  | app/bms/COTRN02.bms:286 |
|  | 21 | 66 | 5 | (ASKIP,NORM) | NEUTRAL | (Y/N) | app/bms/COTRN02.bms:288 |
| ERRMSG | 23 | 1 | 78 | (ASKIP,BRT,FSET) | RED |  | app/bms/COTRN02.bms:293 |
|  | 24 | 1 | 53 | (ASKIP,NORM) | YELLOW | ENTER=Continue  F3=Back  F4=Clear  F5=Copy Last- Tran. | app/bms/COTRN02.bms:297 |

## Function keys

| Key | Action | Target | Evidence |
|---|---|---|---|
| DFHENTER | WHEN DFHENTER |  | app/cbl/COTRN02C.cbl:134 |
| DFHPF3 | WHEN DFHPF3 |  | app/cbl/COTRN02C.cbl:136 |
| DFHPF4 | WHEN DFHPF4 |  | app/cbl/COTRN02C.cbl:144 |
| DFHPF5 | WHEN DFHPF5 |  | app/cbl/COTRN02C.cbl:146 |

## Validation and messages

Message literals for these programs are indexed in [Error handling](../../12-error-handling-messages.md).

## Behaviour

See the program specifications linked from the transaction catalog for first-time display and AID handling.

## Sources

- `app/bms/COTRN02.bms:19`
- `docs/_work/online/screens/COTRN02.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
