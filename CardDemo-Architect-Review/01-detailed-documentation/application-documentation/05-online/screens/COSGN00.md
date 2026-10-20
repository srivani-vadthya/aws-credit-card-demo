# Screen COSGN00

| Item | Value |
|---|---|
| Mapset | COSGN00 |
| Maps | COSGN0A |
| Source | app/bms/COSGN00.bms:19 |
| Module | base |
| Programs | COSGN00C |
| Transactions | CC00 |

## Purpose

Mapset COSGN00 is defined in the BMS source cited below. Field text in the mockup comes from BMS INITIAL and POS values already extracted.

## Map COSGN0A

## Layout mockup

```text
Tran : XXXX         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   Date : mm/dd/yy
Prog : XXXXXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   Time : Ahh:mm:ss
AppID: XXXXXXXX                                                SysID:

     This is a Credit Card Demo Application for Main- frame Modernizati

                    +========================================+
                    |%%%%%%%  NATIONAL RESERVE NOTE  %%%%%%%%|
                    |%(1)  THE UNITED STATES OF KICSLAND (1)%|
                    |%$$              ___       ********  $$%|
                    |%$    {x}       (o o)                 $%|
                    |%$     ******  (  V  )      O N E     $%|
                    |%(1)          ---m-m---             (1)%|
                    |%%~~~~~~~~~~~ ONE DOLLAR ~~~~~~~~~~~~~%%|
                    +========================================+

               Type your User ID and Password, then press ENTE-

                            User ID     : ________ (8 Char)
                            Password    : ________ (8 Char)


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
ENTER=Sign-on  F3=Exit
```

## Fields

| Field | Row | Col | Len | Attributes | Color | Initial | Evidence |
|---|---|---|---|---|---|---|---|
|  | 1 | 1 | 6 | (ASKIP,NORM) | BLUE | Tran : | app/bms/COSGN00.bms:29 |
| TRNNAME | 1 | 8 | 4 | (ASKIP,FSET,NORM) | BLUE |  | app/bms/COSGN00.bms:34 |
| TITLE01 | 1 | 21 | 40 | (ASKIP,FSET,NORM) | YELLOW |  | app/bms/COSGN00.bms:38 |
|  | 1 | 64 | 6 | (ASKIP,NORM) | BLUE | Date : | app/bms/COSGN00.bms:42 |
| CURDATE | 1 | 71 | 8 | (ASKIP,FSET,NORM) | BLUE | mm/dd/yy | app/bms/COSGN00.bms:47 |
|  | 2 | 1 | 6 | (ASKIP,NORM) | BLUE | Prog : | app/bms/COSGN00.bms:52 |
| PGMNAME | 2 | 8 | 8 | (FSET,NORM,PROT) | BLUE |  | app/bms/COSGN00.bms:57 |
| TITLE02 | 2 | 21 | 40 | (ASKIP,FSET,NORM) | YELLOW |  | app/bms/COSGN00.bms:61 |
|  | 2 | 64 | 6 | (ASKIP,NORM) | BLUE | Time : | app/bms/COSGN00.bms:65 |
| CURTIME | 2 | 71 | 9 | (FSET,NORM,PROT) | BLUE | Ahh:mm:ss | app/bms/COSGN00.bms:70 |
|  | 3 | 1 | 6 | (FSET,NORM,PROT) | BLUE | AppID: | app/bms/COSGN00.bms:75 |
| APPLID | 3 | 8 | 8 | (FSET,NORM,PROT) | BLUE |  | app/bms/COSGN00.bms:80 |
|  | 3 | 64 | 6 | (ASKIP,NORM) | BLUE | SysID: | app/bms/COSGN00.bms:84 |
| SYSID | 3 | 71 | 8 | (FSET,NORM,PROT) | BLUE |          | app/bms/COSGN00.bms:89 |
|  | 5 | 6 | 66 | (ASKIP,NORM) | NEUTRAL | This is a Credit Card Demo Application for Main- frame Modernization | app/bms/COSGN00.bms:94 |
|  | 7 | 21 | 42 | (ASKIP,NORM) | BLUE | +========================================+ | app/bms/COSGN00.bms:100 |
|  | 8 | 21 | 42 | (ASKIP,NORM) | BLUE | /%%%%%%%  NATIONAL RESERVE NOTE  %%%%%%%%/ | app/bms/COSGN00.bms:105 |
|  | 9 | 21 | 42 | (ASKIP,NORM) | BLUE | /%(1)  THE UNITED STATES OF KICSLAND (1)%/ | app/bms/COSGN00.bms:110 |
|  | 10 | 21 | 42 | (ASKIP,NORM) | BLUE | /%$$              ___       ********  $$%/ | app/bms/COSGN00.bms:115 |
|  | 11 | 21 | 42 | (ASKIP,NORM) | BLUE | /%$    {x}       (o o)                 $%/ | app/bms/COSGN00.bms:120 |
|  | 12 | 21 | 42 | (ASKIP,NORM) | BLUE | /%$     ******  (  V  )      O N E     $%/ | app/bms/COSGN00.bms:125 |
|  | 13 | 21 | 42 | (ASKIP,NORM) | BLUE | /%(1)          ---m-m---             (1)%/ | app/bms/COSGN00.bms:130 |
|  | 14 | 21 | 42 | (ASKIP,NORM) | BLUE | /%%~~~~~~~~~~~ ONE DOLLAR ~~~~~~~~~~~~~%%/ | app/bms/COSGN00.bms:135 |
|  | 15 | 21 | 42 | (ASKIP,NORM) | BLUE | +========================================+ | app/bms/COSGN00.bms:140 |
|  | 17 | 16 | 49 | (ASKIP,NORM) | TURQUOISE | Type your User ID and Password, then press ENTE- R: | app/bms/COSGN00.bms:145 |
|  | 19 | 29 | 13 | (ASKIP,NORM) | TURQUOISE | User ID     : | app/bms/COSGN00.bms:151 |
| USERID | 19 | 43 | 8 | (FSET,IC,NORM,UNPROT) | GREEN |  | app/bms/COSGN00.bms:156 |
|  | 19 | 52 | 0 | (ASKIP,NORM) | GREEN |  | app/bms/COSGN00.bms:161 |
|  | 19 | 52 | 8 | (ASKIP,NORM) | BLUE | (8 Char) | app/bms/COSGN00.bms:165 |
|  | 20 | 29 | 13 | (ASKIP,NORM) | TURQUOISE | Password    : | app/bms/COSGN00.bms:170 |
| PASSWD | 20 | 43 | 8 | (DRK,FSET,UNPROT) | GREEN | ________ | app/bms/COSGN00.bms:175 |
|  | 20 | 52 | 0 | (ASKIP,NORM) | GREEN |  | app/bms/COSGN00.bms:181 |
|  | 20 | 52 | 8 | (ASKIP,NORM) | BLUE | (8 Char) | app/bms/COSGN00.bms:185 |
|  | 20 | 61 | 1 | (DRK,UNPROT) |  |   | app/bms/COSGN00.bms:190 |
|  | 20 | 63 | 0 | (ASKIP,NORM) |  |  | app/bms/COSGN00.bms:194 |
| ERRMSG | 23 | 1 | 78 | (ASKIP,BRT,FSET) | RED |  | app/bms/COSGN00.bms:197 |
|  | 24 | 1 | 22 | (ASKIP,NORM) | YELLOW | ENTER=Sign-on  F3=Exit | app/bms/COSGN00.bms:201 |

## Function keys

| Key | Action | Target | Evidence |
|---|---|---|---|
| DFHENTER | WHEN DFHENTER |  | app/cbl/COSGN00C.cbl:86 |
| DFHPF3 | WHEN DFHPF3 |  | app/cbl/COSGN00C.cbl:88 |

## Validation and messages

Message literals for these programs are indexed in [Error handling](../../12-error-handling-messages.md).

## Behaviour

See the program specifications linked from the transaction catalog for first-time display and AID handling.

## Sources

- `app/bms/COSGN00.bms:19`
- `docs/_work/online/screens/COSGN00.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
