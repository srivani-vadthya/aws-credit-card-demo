# Screen COTRN00

| Item | Value |
|---|---|
| Mapset | COTRN00 |
| Maps | COTRN0A |
| Source | app/bms/COTRN00.bms:19 |
| Module | base |
| Programs | COTRN00C |
| Transactions | CT00 |

## Purpose

Mapset COTRN00 is defined in the BMS source cited below. Field text in the mockup comes from BMS INITIAL and POS values already extracted.

## Map COTRN0A

## Layout mockup

```text
Tran: XXXX          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Date: mm/dd/yy
Prog: XXXXXXXX      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Time: hh:mm:ss

                             List Transactions                  Page:

    Search Tran ID: ________________

 Sel    Transaction ID      Date          Description                Amount
 ---   ----------------   --------   --------------------------   ------------











           Type

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
ENTER=Continue  F3=Back  F7=Backward  F8=Forwar-
```

## Fields

| Field | Row | Col | Len | Attributes | Color | Initial | Evidence |
|---|---|---|---|---|---|---|---|
|  | 1 | 1 | 5 | (ASKIP,NORM) | BLUE | Tran: | app/bms/COTRN00.bms:29 |
| TRNNAME | 1 | 7 | 4 | (ASKIP,FSET,NORM) | BLUE |  | app/bms/COTRN00.bms:34 |
| TITLE01 | 1 | 21 | 40 | (ASKIP,FSET,NORM) | YELLOW |  | app/bms/COTRN00.bms:38 |
|  | 1 | 65 | 5 | (ASKIP,NORM) | BLUE | Date: | app/bms/COTRN00.bms:42 |
| CURDATE | 1 | 71 | 8 | (ASKIP,FSET,NORM) | BLUE | mm/dd/yy | app/bms/COTRN00.bms:47 |
|  | 2 | 1 | 5 | (ASKIP,NORM) | BLUE | Prog: | app/bms/COTRN00.bms:52 |
| PGMNAME | 2 | 7 | 8 | (ASKIP,FSET,NORM) | BLUE |  | app/bms/COTRN00.bms:57 |
| TITLE02 | 2 | 21 | 40 | (ASKIP,FSET,NORM) | YELLOW |  | app/bms/COTRN00.bms:61 |
|  | 2 | 65 | 5 | (ASKIP,NORM) | BLUE | Time: | app/bms/COTRN00.bms:65 |
| CURTIME | 2 | 71 | 8 | (ASKIP,FSET,NORM) | BLUE | hh:mm:ss | app/bms/COTRN00.bms:70 |
|  | 4 | 30 | 17 | (ASKIP,BRT) | NEUTRAL | List Transactions | app/bms/COTRN00.bms:75 |
|  | 4 | 65 | 5 | (ASKIP,BRT) | TURQUOISE | Page: | app/bms/COTRN00.bms:80 |
| PAGENUM | 4 | 71 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:85 |
|  | 6 | 5 | 15 | (ASKIP,NORM) | TURQUOISE | Search Tran ID: | app/bms/COTRN00.bms:90 |
| TRNIDIN | 6 | 21 | 16 | (FSET,NORM,UNPROT) | GREEN |  | app/bms/COTRN00.bms:95 |
|  | 6 | 38 | 0 | (ASKIP,NORM) |  |  | app/bms/COTRN00.bms:100 |
|  | 8 | 2 | 3 | (ASKIP,NORM) | NEUTRAL | Sel | app/bms/COTRN00.bms:103 |
|  | 8 | 8 | 16 | (ASKIP,NORM) | NEUTRAL |  Transaction ID  | app/bms/COTRN00.bms:108 |
|  | 8 | 27 | 8 | (ASKIP,NORM) | NEUTRAL |   Date   | app/bms/COTRN00.bms:113 |
|  | 8 | 38 | 26 | (ASKIP,NORM) | NEUTRAL |      Description           | app/bms/COTRN00.bms:118 |
|  | 8 | 67 | 12 | (ASKIP,NORM) | NEUTRAL |    Amount    | app/bms/COTRN00.bms:123 |
|  | 9 | 2 | 3 | (ASKIP,NORM) | NEUTRAL | --- | app/bms/COTRN00.bms:128 |
|  | 9 | 8 | 16 | (ASKIP,NORM) | NEUTRAL | ---------------- | app/bms/COTRN00.bms:133 |
|  | 9 | 27 | 8 | (ASKIP,NORM) | NEUTRAL | -------- | app/bms/COTRN00.bms:138 |
|  | 9 | 38 | 26 | (ASKIP,NORM) | NEUTRAL | -------------------------- | app/bms/COTRN00.bms:143 |
|  | 9 | 67 | 12 | (ASKIP,NORM) | NEUTRAL | ------------ | app/bms/COTRN00.bms:148 |
| SEL0001 | 10 | 3 | 1 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COTRN00.bms:153 |
|  | 10 | 5 | 0 | (ASKIP,NORM) |  |  | app/bms/COTRN00.bms:159 |
| TRNID01 | 10 | 8 | 16 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:162 |
| TDATE01 | 10 | 27 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:167 |
| TDESC01 | 10 | 38 | 26 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:172 |
| TAMT001 | 10 | 67 | 12 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:177 |
| SEL0002 | 11 | 3 | 1 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COTRN00.bms:182 |
|  | 11 | 5 | 0 | (ASKIP,NORM) |  |  | app/bms/COTRN00.bms:188 |
| TRNID02 | 11 | 8 | 16 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:191 |
| TDATE02 | 11 | 27 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:196 |
| TDESC02 | 11 | 38 | 26 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:201 |
| TAMT002 | 11 | 67 | 12 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:206 |
| SEL0003 | 12 | 3 | 1 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COTRN00.bms:211 |
|  | 12 | 5 | 0 | (ASKIP,NORM) |  |  | app/bms/COTRN00.bms:217 |
| TRNID03 | 12 | 8 | 16 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:220 |
| TDATE03 | 12 | 27 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:225 |
| TDESC03 | 12 | 38 | 26 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:230 |
| TAMT003 | 12 | 67 | 12 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:235 |
| SEL0004 | 13 | 3 | 1 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COTRN00.bms:240 |
|  | 13 | 5 | 0 | (ASKIP,NORM) |  |  | app/bms/COTRN00.bms:246 |
| TRNID04 | 13 | 8 | 16 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:249 |
| TDATE04 | 13 | 27 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:254 |
| TDESC04 | 13 | 38 | 26 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:259 |
| TAMT004 | 13 | 67 | 12 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:264 |
| SEL0005 | 14 | 3 | 1 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COTRN00.bms:269 |
|  | 14 | 5 | 0 | (ASKIP,NORM) |  |  | app/bms/COTRN00.bms:275 |
| TRNID05 | 14 | 8 | 16 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:278 |
| TDATE05 | 14 | 27 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:283 |
| TDESC05 | 14 | 38 | 26 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:288 |
| TAMT005 | 14 | 67 | 12 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:293 |
| SEL0006 | 15 | 3 | 1 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COTRN00.bms:298 |
|  | 15 | 5 | 0 | (ASKIP,NORM) |  |  | app/bms/COTRN00.bms:304 |
| TRNID06 | 15 | 8 | 16 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:307 |
| TDATE06 | 15 | 27 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:312 |
| TDESC06 | 15 | 38 | 26 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:317 |
| TAMT006 | 15 | 67 | 12 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:322 |
| SEL0007 | 16 | 3 | 1 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COTRN00.bms:327 |
|  | 16 | 5 | 0 | (ASKIP,NORM) |  |  | app/bms/COTRN00.bms:333 |
| TRNID07 | 16 | 8 | 16 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:336 |
| TDATE07 | 16 | 27 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:341 |
| TDESC07 | 16 | 38 | 26 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:346 |
| TAMT007 | 16 | 67 | 12 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:351 |
| SEL0008 | 17 | 3 | 1 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COTRN00.bms:356 |
|  | 17 | 5 | 0 | (ASKIP,NORM) |  |  | app/bms/COTRN00.bms:362 |
| TRNID08 | 17 | 8 | 16 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:365 |
| TDATE08 | 17 | 27 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:370 |
| TDESC08 | 17 | 38 | 26 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:375 |
| TAMT008 | 17 | 67 | 12 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:380 |
| SEL0009 | 18 | 3 | 1 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COTRN00.bms:385 |
|  | 18 | 5 | 0 | (ASKIP,NORM) |  |  | app/bms/COTRN00.bms:391 |
| TRNID09 | 18 | 8 | 16 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:394 |
| TDATE09 | 18 | 27 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:399 |
| TDESC09 | 18 | 38 | 26 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:404 |
| TAMT009 | 18 | 67 | 12 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:409 |
| SEL0010 | 19 | 3 | 1 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COTRN00.bms:414 |
|  | 19 | 5 | 0 | (ASKIP,NORM) |  |  | app/bms/COTRN00.bms:420 |
| TRNID10 | 19 | 8 | 16 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:423 |
| TDATE10 | 19 | 27 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:428 |
| TDESC10 | 19 | 38 | 26 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:433 |
| TAMT010 | 19 | 67 | 12 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COTRN00.bms:438 |
|  | 21 | 12 | 50 | (ASKIP,BRT) | NEUTRAL | Type  | app/bms/COTRN00.bms:444 |
| ERRMSG | 23 | 1 | 78 | (ASKIP,BRT,FSET) | RED |  | app/bms/COTRN00.bms:450 |
|  | 24 | 1 | 48 | (ASKIP,NORM) | YELLOW | ENTER=Continue  F3=Back  F7=Backward  F8=Forwar- d | app/bms/COTRN00.bms:454 |

## Function keys

| Key | Action | Target | Evidence |
|---|---|---|---|
| DFHENTER | WHEN DFHENTER |  | app/cbl/COTRN00C.cbl:120 |
| DFHPF3 | WHEN DFHPF3 |  | app/cbl/COTRN00C.cbl:122 |
| DFHPF7 | WHEN DFHPF7 |  | app/cbl/COTRN00C.cbl:125 |
| DFHPF8 | WHEN DFHPF8 |  | app/cbl/COTRN00C.cbl:127 |

## Validation and messages

Message literals for these programs are indexed in [Error handling](../../12-error-handling-messages.md).

## Behaviour

See the program specifications linked from the transaction catalog for first-time display and AID handling.

## Sources

- `app/bms/COTRN00.bms:19`
- `docs/_work/online/screens/COTRN00.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
