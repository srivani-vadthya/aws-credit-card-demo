# Screen COTRN01

| Item | Value |
|---|---|
| Mapset | COTRN01 |
| Maps | COTRN1A |
| Source | app/bms/COTRN01.bms:19 |
| Module | base |
| Programs | COTRN01C |
| Transactions | CT01 |

## Purpose

Mapset COTRN01 is defined in the BMS source cited below. Field text in the mockup comes from BMS INITIAL and POS values already extracted.

## Map COTRN1A

## Layout mockup

```text
Tran: XXXX          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Date: mm/dd/yy
Prog: XXXXXXXX      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Time: hh:mm:ss

                             View Transaction

     Enter Tran ID:

     ------------------------------------------------ ---------------------

     Transaction ID:                        Card Number:

     Type CD:         Category CD:           Source:

     Description:

     Amount:                  Orig Date:                Proc Date:

     Merchant ID:               Merchant Name:

     Merchant City:                                 Merchant Zip:


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
ENTER=Fetch  F3=Back  F4=Clear  F5=Browse Tran.
```

## Fields

| Field | Row | Col | Len | Attributes | Color | Initial | Evidence |
|---|---|---|---|---|---|---|---|
|  | 1 | 1 | 5 | (ASKIP,NORM) | BLUE | Tran: | app/bms/COTRN01.bms:29 |
| TRNNAME | 1 | 7 | 4 | (ASKIP,FSET,NORM) | BLUE |  | app/bms/COTRN01.bms:34 |
| TITLE01 | 1 | 21 | 40 | (ASKIP,FSET,NORM) | YELLOW |  | app/bms/COTRN01.bms:38 |
|  | 1 | 65 | 5 | (ASKIP,NORM) | BLUE | Date: | app/bms/COTRN01.bms:42 |
| CURDATE | 1 | 71 | 8 | (ASKIP,FSET,NORM) | BLUE | mm/dd/yy | app/bms/COTRN01.bms:47 |
|  | 2 | 1 | 5 | (ASKIP,NORM) | BLUE | Prog: | app/bms/COTRN01.bms:52 |
| PGMNAME | 2 | 7 | 8 | (ASKIP,FSET,NORM) | BLUE |  | app/bms/COTRN01.bms:57 |
| TITLE02 | 2 | 21 | 40 | (ASKIP,FSET,NORM) | YELLOW |  | app/bms/COTRN01.bms:61 |
|  | 2 | 65 | 5 | (ASKIP,NORM) | BLUE | Time: | app/bms/COTRN01.bms:65 |
| CURTIME | 2 | 71 | 8 | (ASKIP,FSET,NORM) | BLUE | hh:mm:ss | app/bms/COTRN01.bms:70 |
|  | 4 | 30 | 16 | (ASKIP,BRT) | NEUTRAL | View Transaction | app/bms/COTRN01.bms:75 |
|  | 6 | 6 | 14 | (ASKIP,NORM) | TURQUOISE | Enter Tran ID: | app/bms/COTRN01.bms:80 |
| TRNIDIN | 6 | 21 | 16 | (FSET,IC,NORM,UNPROT) | GREEN |   | app/bms/COTRN01.bms:85 |
|  | 6 | 38 | 0 | (ASKIP,NORM) |  |  | app/bms/COTRN01.bms:91 |
|  | 8 | 6 | 70 | (ASKIP,NORM) | NEUTRAL | ------------------------------------------------ ----------------------- | app/bms/COTRN01.bms:94 |
|  | 10 | 6 | 15 | (ASKIP,NORM) | TURQUOISE | Transaction ID: | app/bms/COTRN01.bms:100 |
| TRNID | 10 | 22 | 16 | (ASKIP,NORM) | BLUE |   | app/bms/COTRN01.bms:105 |
|  | 10 | 39 | 0 | (ASKIP,NORM) |  |  | app/bms/COTRN01.bms:110 |
|  | 10 | 45 | 12 | (ASKIP,NORM) | TURQUOISE | Card Number: | app/bms/COTRN01.bms:113 |
| CARDNUM | 10 | 58 | 16 | (ASKIP,NORM) | BLUE |   | app/bms/COTRN01.bms:118 |
|  | 10 | 75 | 0 | (ASKIP,NORM) | GREEN |  | app/bms/COTRN01.bms:123 |
|  | 12 | 6 | 8 | (ASKIP,NORM) | TURQUOISE | Type CD: | app/bms/COTRN01.bms:127 |
| TTYPCD | 12 | 15 | 2 | (ASKIP,NORM) | BLUE |   | app/bms/COTRN01.bms:132 |
|  | 12 | 18 | 0 |  |  |  | app/bms/COTRN01.bms:137 |
|  | 12 | 23 | 12 | (ASKIP,NORM) | TURQUOISE | Category CD: | app/bms/COTRN01.bms:139 |
| TCATCD | 12 | 36 | 4 | (ASKIP,NORM) | BLUE |   | app/bms/COTRN01.bms:144 |
|  | 12 | 41 | 0 |  |  |  | app/bms/COTRN01.bms:149 |
|  | 12 | 46 | 7 | (ASKIP,NORM) | TURQUOISE | Source: | app/bms/COTRN01.bms:151 |
| TRNSRC | 12 | 54 | 10 | (ASKIP,NORM) | BLUE |   | app/bms/COTRN01.bms:156 |
|  | 12 | 65 | 0 |  |  |  | app/bms/COTRN01.bms:161 |
|  | 14 | 6 | 12 | (ASKIP,NORM) | TURQUOISE | Description: | app/bms/COTRN01.bms:163 |
| TDESC | 14 | 19 | 60 | (ASKIP,NORM) | BLUE |   | app/bms/COTRN01.bms:168 |
|  | 14 | 80 | 0 |  |  |  | app/bms/COTRN01.bms:173 |
|  | 16 | 6 | 7 | (ASKIP,NORM) | TURQUOISE | Amount: | app/bms/COTRN01.bms:175 |
| TRNAMT | 16 | 14 | 12 | (ASKIP,NORM) | BLUE |   | app/bms/COTRN01.bms:180 |
|  | 16 | 27 | 0 |  |  |  | app/bms/COTRN01.bms:185 |
|  | 16 | 31 | 10 | (ASKIP,NORM) | TURQUOISE | Orig Date: | app/bms/COTRN01.bms:187 |
| TORIGDT | 16 | 42 | 10 | (ASKIP,NORM) | BLUE |   | app/bms/COTRN01.bms:192 |
|  | 16 | 53 | 0 |  |  |  | app/bms/COTRN01.bms:197 |
|  | 16 | 57 | 10 | (ASKIP,NORM) | TURQUOISE | Proc Date: | app/bms/COTRN01.bms:199 |
| TPROCDT | 16 | 68 | 10 | (ASKIP,NORM) | BLUE |   | app/bms/COTRN01.bms:204 |
|  | 16 | 79 | 0 |  |  |  | app/bms/COTRN01.bms:209 |
|  | 18 | 6 | 12 | (ASKIP,NORM) | TURQUOISE | Merchant ID: | app/bms/COTRN01.bms:211 |
| MID | 18 | 19 | 9 | (ASKIP,NORM) | BLUE |   | app/bms/COTRN01.bms:216 |
|  | 18 | 29 | 0 |  |  |  | app/bms/COTRN01.bms:221 |
|  | 18 | 33 | 14 | (ASKIP,NORM) | TURQUOISE | Merchant Name: | app/bms/COTRN01.bms:223 |
| MNAME | 18 | 48 | 30 | (ASKIP,NORM) | BLUE |   | app/bms/COTRN01.bms:228 |
|  | 18 | 79 | 0 |  |  |  | app/bms/COTRN01.bms:233 |
|  | 20 | 6 | 14 | (ASKIP,NORM) | TURQUOISE | Merchant City: | app/bms/COTRN01.bms:235 |
| MCITY | 20 | 21 | 25 | (ASKIP,NORM) | BLUE |   | app/bms/COTRN01.bms:240 |
|  | 20 | 47 | 0 |  |  |  | app/bms/COTRN01.bms:245 |
|  | 20 | 53 | 13 | (ASKIP,NORM) | TURQUOISE | Merchant Zip: | app/bms/COTRN01.bms:247 |
| MZIP | 20 | 67 | 10 | (ASKIP,NORM) | BLUE |   | app/bms/COTRN01.bms:252 |
|  | 20 | 78 | 0 |  |  |  | app/bms/COTRN01.bms:257 |
| ERRMSG | 23 | 1 | 78 | (ASKIP,BRT,FSET) | RED |  | app/bms/COTRN01.bms:259 |
|  | 24 | 1 | 47 | (ASKIP,NORM) | YELLOW | ENTER=Fetch  F3=Back  F4=Clear  F5=Browse Tran.-  | app/bms/COTRN01.bms:263 |

## Function keys

| Key | Action | Target | Evidence |
|---|---|---|---|
| DFHENTER | WHEN DFHENTER |  | app/cbl/COTRN01C.cbl:113 |
| DFHPF3 | WHEN DFHPF3 |  | app/cbl/COTRN01C.cbl:115 |
| DFHPF4 | WHEN DFHPF4 |  | app/cbl/COTRN01C.cbl:123 |
| DFHPF5 | WHEN DFHPF5 |  | app/cbl/COTRN01C.cbl:125 |

## Validation and messages

Message literals for these programs are indexed in [Error handling](../../12-error-handling-messages.md).

## Behaviour

See the program specifications linked from the transaction catalog for first-time display and AID handling.

## Sources

- `app/bms/COTRN01.bms:19`
- `docs/_work/online/screens/COTRN01.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
