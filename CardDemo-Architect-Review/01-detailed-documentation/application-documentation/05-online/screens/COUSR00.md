# Screen COUSR00

| Item | Value |
|---|---|
| Mapset | COUSR00 |
| Maps | COUSR0A |
| Source | app/bms/COUSR00.bms:19 |
| Module | base |
| Programs | COUSR00C |
| Transactions | CU00 |

## Purpose

Mapset COUSR00 is defined in the BMS source cited below. Field text in the mockup comes from BMS INITIAL and POS values already extracted.

## Map COUSR0A

## Layout mockup

```text
Tran: XXXX          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Date: mm/dd/yy
Prog: XXXXXXXX      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Time: hh:mm:ss

                                  List Users                    Page:

    Search User ID: ________

    Sel    User ID          First Name              Last Name          Type
    ---    --------    --------------------    --------------------    ----











           Type

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
ENTER=Continue  F3=Back  F7=Backward  F8=Forwar-
```

## Fields

| Field | Row | Col | Len | Attributes | Color | Initial | Evidence |
|---|---|---|---|---|---|---|---|
|  | 1 | 1 | 5 | (ASKIP,NORM) | BLUE | Tran: | app/bms/COUSR00.bms:29 |
| TRNNAME | 1 | 7 | 4 | (ASKIP,FSET,NORM) | BLUE |  | app/bms/COUSR00.bms:34 |
| TITLE01 | 1 | 21 | 40 | (ASKIP,FSET,NORM) | YELLOW |  | app/bms/COUSR00.bms:38 |
|  | 1 | 65 | 5 | (ASKIP,NORM) | BLUE | Date: | app/bms/COUSR00.bms:42 |
| CURDATE | 1 | 71 | 8 | (ASKIP,FSET,NORM) | BLUE | mm/dd/yy | app/bms/COUSR00.bms:47 |
|  | 2 | 1 | 5 | (ASKIP,NORM) | BLUE | Prog: | app/bms/COUSR00.bms:52 |
| PGMNAME | 2 | 7 | 8 | (ASKIP,FSET,NORM) | BLUE |  | app/bms/COUSR00.bms:57 |
| TITLE02 | 2 | 21 | 40 | (ASKIP,FSET,NORM) | YELLOW |  | app/bms/COUSR00.bms:61 |
|  | 2 | 65 | 5 | (ASKIP,NORM) | BLUE | Time: | app/bms/COUSR00.bms:65 |
| CURTIME | 2 | 71 | 8 | (ASKIP,FSET,NORM) | BLUE | hh:mm:ss | app/bms/COUSR00.bms:70 |
|  | 4 | 35 | 10 | (ASKIP,BRT) | NEUTRAL | List Users | app/bms/COUSR00.bms:75 |
|  | 4 | 65 | 5 | (ASKIP,BRT) | TURQUOISE | Page: | app/bms/COUSR00.bms:80 |
| PAGENUM | 4 | 71 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:85 |
|  | 6 | 5 | 15 | (ASKIP,NORM) | TURQUOISE | Search User ID: | app/bms/COUSR00.bms:90 |
| USRIDIN | 6 | 21 | 8 | (FSET,NORM,UNPROT) | GREEN |  | app/bms/COUSR00.bms:95 |
|  | 6 | 30 | 0 | (ASKIP,NORM) |  |  | app/bms/COUSR00.bms:100 |
|  | 8 | 5 | 3 | (ASKIP,NORM) | NEUTRAL | Sel | app/bms/COUSR00.bms:103 |
|  | 8 | 12 | 8 | (ASKIP,NORM) | NEUTRAL | User ID  | app/bms/COUSR00.bms:108 |
|  | 8 | 24 | 20 | (ASKIP,NORM) | NEUTRAL |      First Name      | app/bms/COUSR00.bms:113 |
|  | 8 | 48 | 20 | (ASKIP,NORM) | NEUTRAL |      Last Name       | app/bms/COUSR00.bms:118 |
|  | 8 | 72 | 4 | (ASKIP,NORM) | NEUTRAL | Type | app/bms/COUSR00.bms:123 |
|  | 9 | 5 | 3 | (ASKIP,NORM) | NEUTRAL | --- | app/bms/COUSR00.bms:128 |
|  | 9 | 12 | 8 | (ASKIP,NORM) | NEUTRAL | -------- | app/bms/COUSR00.bms:133 |
|  | 9 | 24 | 20 | (ASKIP,NORM) | NEUTRAL | -------------------- | app/bms/COUSR00.bms:138 |
|  | 9 | 48 | 20 | (ASKIP,NORM) | NEUTRAL | -------------------- | app/bms/COUSR00.bms:143 |
|  | 9 | 72 | 4 | (ASKIP,NORM) | NEUTRAL | ---- | app/bms/COUSR00.bms:148 |
| SEL0001 | 10 | 6 | 1 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COUSR00.bms:153 |
|  | 10 | 8 | 0 | (ASKIP,NORM) |  |  | app/bms/COUSR00.bms:159 |
| USRID01 | 10 | 12 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:162 |
| FNAME01 | 10 | 24 | 20 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:167 |
| LNAME01 | 10 | 48 | 20 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:172 |
| UTYPE01 | 10 | 73 | 1 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:177 |
| SEL0002 | 11 | 6 | 1 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COUSR00.bms:182 |
|  | 11 | 8 | 0 | (ASKIP,NORM) |  |  | app/bms/COUSR00.bms:188 |
| USRID02 | 11 | 12 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:191 |
| FNAME02 | 11 | 24 | 20 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:196 |
| LNAME02 | 11 | 48 | 20 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:201 |
| UTYPE02 | 11 | 73 | 1 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:206 |
| SEL0003 | 12 | 6 | 1 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COUSR00.bms:211 |
|  | 12 | 8 | 0 | (ASKIP,NORM) |  |  | app/bms/COUSR00.bms:217 |
| USRID03 | 12 | 12 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:220 |
| FNAME03 | 12 | 24 | 20 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:225 |
| LNAME03 | 12 | 48 | 20 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:230 |
| UTYPE03 | 12 | 73 | 1 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:235 |
| SEL0004 | 13 | 6 | 1 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COUSR00.bms:240 |
|  | 13 | 8 | 0 | (ASKIP,NORM) |  |  | app/bms/COUSR00.bms:246 |
| USRID04 | 13 | 12 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:249 |
| FNAME04 | 13 | 24 | 20 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:254 |
| LNAME04 | 13 | 48 | 20 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:259 |
| UTYPE04 | 13 | 73 | 1 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:264 |
| SEL0005 | 14 | 6 | 1 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COUSR00.bms:269 |
|  | 14 | 8 | 0 | (ASKIP,NORM) |  |  | app/bms/COUSR00.bms:275 |
| USRID05 | 14 | 12 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:278 |
| FNAME05 | 14 | 24 | 20 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:283 |
| LNAME05 | 14 | 48 | 20 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:288 |
| UTYPE05 | 14 | 73 | 1 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:293 |
| SEL0006 | 15 | 6 | 1 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COUSR00.bms:298 |
|  | 15 | 8 | 0 | (ASKIP,NORM) |  |  | app/bms/COUSR00.bms:304 |
| USRID06 | 15 | 12 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:307 |
| FNAME06 | 15 | 24 | 20 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:312 |
| LNAME06 | 15 | 48 | 20 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:317 |
| UTYPE06 | 15 | 73 | 1 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:322 |
| SEL0007 | 16 | 6 | 1 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COUSR00.bms:327 |
|  | 16 | 8 | 0 | (ASKIP,NORM) |  |  | app/bms/COUSR00.bms:333 |
| USRID07 | 16 | 12 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:336 |
| FNAME07 | 16 | 24 | 20 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:341 |
| LNAME07 | 16 | 48 | 20 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:346 |
| UTYPE07 | 16 | 73 | 1 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:351 |
| SEL0008 | 17 | 6 | 1 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COUSR00.bms:356 |
|  | 17 | 8 | 0 | (ASKIP,NORM) |  |  | app/bms/COUSR00.bms:362 |
| USRID08 | 17 | 12 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:365 |
| FNAME08 | 17 | 24 | 20 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:370 |
| LNAME08 | 17 | 48 | 20 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:375 |
| UTYPE08 | 17 | 73 | 1 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:380 |
| SEL0009 | 18 | 6 | 1 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COUSR00.bms:385 |
|  | 18 | 8 | 0 | (ASKIP,NORM) |  |  | app/bms/COUSR00.bms:391 |
| USRID09 | 18 | 12 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:394 |
| FNAME09 | 18 | 24 | 20 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:399 |
| LNAME09 | 18 | 48 | 20 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:404 |
| UTYPE09 | 18 | 73 | 1 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:409 |
| SEL0010 | 19 | 6 | 1 | (FSET,NORM,UNPROT) | GREEN |   | app/bms/COUSR00.bms:414 |
|  | 19 | 8 | 0 | (ASKIP,NORM) |  |  | app/bms/COUSR00.bms:420 |
| USRID10 | 19 | 12 | 8 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:423 |
| FNAME10 | 19 | 24 | 20 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:428 |
| LNAME10 | 19 | 48 | 20 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:433 |
| UTYPE10 | 19 | 73 | 1 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COUSR00.bms:438 |
|  | 21 | 12 | 56 | (ASKIP,BRT) | NEUTRAL | Type  | app/bms/COUSR00.bms:443 |
| ERRMSG | 23 | 1 | 78 | (ASKIP,BRT,FSET) | RED |  | app/bms/COUSR00.bms:449 |
|  | 24 | 1 | 48 | (ASKIP,NORM) | YELLOW | ENTER=Continue  F3=Back  F7=Backward  F8=Forwar- d | app/bms/COUSR00.bms:453 |

## Function keys

| Key | Action | Target | Evidence |
|---|---|---|---|
| DFHENTER | WHEN DFHENTER |  | app/cbl/COUSR00C.cbl:123 |
| DFHPF3 | WHEN DFHPF3 |  | app/cbl/COUSR00C.cbl:125 |
| DFHPF7 | WHEN DFHPF7 |  | app/cbl/COUSR00C.cbl:128 |
| DFHPF8 | WHEN DFHPF8 |  | app/cbl/COUSR00C.cbl:130 |

## Validation and messages

Message literals for these programs are indexed in [Error handling](../../12-error-handling-messages.md).

## Behaviour

See the program specifications linked from the transaction catalog for first-time display and AID handling.

## Sources

- `app/bms/COUSR00.bms:19`
- `docs/_work/online/screens/COUSR00.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
