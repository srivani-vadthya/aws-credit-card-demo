# Screen COUSR02

| Item | Value |
|---|---|
| Mapset | COUSR02 |
| Maps | COUSR2A |
| Source | app/bms/COUSR02.bms:19 |
| Module | base |
| Programs | COUSR02C |
| Transactions | CU02 |

## Purpose

Mapset COUSR02 is defined in the BMS source cited below. Field text in the mockup comes from BMS INITIAL and POS values already extracted.

## Map COUSR2A

## Layout mockup

```text
Tran: XXXX          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Date: mm/dd/yy
Prog: XXXXXXXX      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Time: hh:mm:ss

                                  Update User

     Enter User ID: ________

     ***********************************************- DFHMDF ATTRB=(ASKIP,N


                 ____________________       Last Name: ____________________

     Password: ******** (8 Char)

     User Type: _ (A=Admin, U=User)







XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
ENTER=Fetch  F3=Save&&Exit  F4=Clear  F5=Save  - F12=Cance
```

## Fields

| Field | Row | Col | Len | Attributes | Color | Initial | Evidence |
|---|---|---|---|---|---|---|---|
|  | 1 | 1 | 5 | (ASKIP,NORM) | BLUE | Tran: | app/bms/COUSR02.bms:29 |
| TRNNAME | 1 | 7 | 4 | (ASKIP,FSET,NORM) | BLUE |  | app/bms/COUSR02.bms:34 |
| TITLE01 | 1 | 21 | 40 | (ASKIP,FSET,NORM) | YELLOW |  | app/bms/COUSR02.bms:38 |
|  | 1 | 65 | 5 | (ASKIP,NORM) | BLUE | Date: | app/bms/COUSR02.bms:42 |
| CURDATE | 1 | 71 | 8 | (ASKIP,FSET,NORM) | BLUE | mm/dd/yy | app/bms/COUSR02.bms:47 |
|  | 2 | 1 | 5 | (ASKIP,NORM) | BLUE | Prog: | app/bms/COUSR02.bms:52 |
| PGMNAME | 2 | 7 | 8 | (ASKIP,FSET,NORM) | BLUE |  | app/bms/COUSR02.bms:57 |
| TITLE02 | 2 | 21 | 40 | (ASKIP,FSET,NORM) | YELLOW |  | app/bms/COUSR02.bms:61 |
|  | 2 | 65 | 5 | (ASKIP,NORM) | BLUE | Time: | app/bms/COUSR02.bms:65 |
| CURTIME | 2 | 71 | 8 | (ASKIP,FSET,NORM) | BLUE | hh:mm:ss | app/bms/COUSR02.bms:70 |
|  | 4 | 35 | 11 | (ASKIP,BRT) | NEUTRAL | Update User | app/bms/COUSR02.bms:75 |
|  | 6 | 6 | 14 | (ASKIP,NORM) | GREEN | Enter User ID: | app/bms/COUSR02.bms:80 |
| USRIDIN | 6 | 21 | 8 | (FSET,IC,NORM,UNPROT) | GREEN |  | app/bms/COUSR02.bms:85 |
|  | 6 | 30 | 0 | (ASKIP,NORM) |  |  | app/bms/COUSR02.bms:90 |
|  | 8 | 6 | 70 | (ASKIP,NORM) | YELLOW | ***********************************************- DFHMDF ATTRB=(ASKIP,NORM),                                     - COLOR=TURQUOISE,                                        - LENGTH=11,                                              - POS=(11,6),                                             - INITIAL= | app/bms/COUSR02.bms:93 |
| FNAME | 11 | 18 | 20 | (FSET,NORM,UNPROT) | GREEN |  | app/bms/COUSR02.bms:103 |
|  | 11 | 39 | 0 | (ASKIP,NORM) |  |  | app/bms/COUSR02.bms:108 |
|  | 11 | 45 | 10 | (ASKIP,NORM) | TURQUOISE | Last Name: | app/bms/COUSR02.bms:111 |
| LNAME | 11 | 56 | 20 | (FSET,NORM,UNPROT) | GREEN |  | app/bms/COUSR02.bms:116 |
|  | 11 | 77 | 0 | (ASKIP,NORM) | GREEN |  | app/bms/COUSR02.bms:121 |
|  | 13 | 6 | 9 | (ASKIP,NORM) | TURQUOISE | Password: | app/bms/COUSR02.bms:125 |
| PASSWD | 13 | 16 | 8 | (DRK,FSET,UNPROT) | GREEN |  | app/bms/COUSR02.bms:130 |
|  | 13 | 25 | 8 | (ASKIP,NORM) | BLUE | (8 Char) | app/bms/COUSR02.bms:135 |
|  | 15 | 6 | 11 | (ASKIP,NORM) | TURQUOISE | User Type:  | app/bms/COUSR02.bms:140 |
| USRTYPE | 15 | 17 | 1 | (FSET,NORM,UNPROT) | GREEN |  | app/bms/COUSR02.bms:145 |
|  | 15 | 19 | 17 | (ASKIP,NORM) | BLUE | (A=Admin, U=User) | app/bms/COUSR02.bms:150 |
| ERRMSG | 23 | 1 | 78 | (ASKIP,BRT,FSET) | RED |  | app/bms/COUSR02.bms:155 |
|  | 24 | 1 | 58 | (ASKIP,NORM) | YELLOW | ENTER=Fetch  F3=Save&&Exit  F4=Clear  F5=Save  - F12=Cancel | app/bms/COUSR02.bms:159 |

## Function keys

| Key | Action | Target | Evidence |
|---|---|---|---|
| DFHENTER | WHEN DFHENTER |  | app/cbl/COUSR02C.cbl:109 |
| DFHPF3 | WHEN DFHPF3 |  | app/cbl/COUSR02C.cbl:111 |
| DFHPF4 | WHEN DFHPF4 |  | app/cbl/COUSR02C.cbl:120 |
| DFHPF5 | WHEN DFHPF5 |  | app/cbl/COUSR02C.cbl:122 |
| DFHPF12 | WHEN DFHPF12 |  | app/cbl/COUSR02C.cbl:124 |

## Validation and messages

Message literals for these programs are indexed in [Error handling](../../12-error-handling-messages.md).

## Behaviour

See the program specifications linked from the transaction catalog for first-time display and AID handling.

## Sources

- `app/bms/COUSR02.bms:19`
- `docs/_work/online/screens/COUSR02.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
