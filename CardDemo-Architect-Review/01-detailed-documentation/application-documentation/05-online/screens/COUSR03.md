# Screen COUSR03

| Item | Value |
|---|---|
| Mapset | COUSR03 |
| Maps | COUSR3A |
| Source | app/bms/COUSR03.bms:19 |
| Module | base |
| Programs | COUSR03C |
| Transactions | CU03 |

## Purpose

Mapset COUSR03 is defined in the BMS source cited below. Field text in the mockup comes from BMS INITIAL and POS values already extracted.

## Map COUSR3A

## Layout mockup

```text
Tran: XXXX          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Date: mm/dd/yy
Prog: XXXXXXXX      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Time: hh:mm:ss

                                  Delete User

     Enter User ID: ________

     ***********************************************- DFHMDF ATTRB=(ASKIP,N


                 XXXXXXXXXXXXXXXXXXXX

     Last Name:  XXXXXXXXXXXXXXXXXXXX

     User Type: X (A=Admin, U=User)







XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
ENTER=Fetch  F3=Back  F4=Clear  F5=Delete
```

## Fields

| Field | Row | Col | Len | Attributes | Color | Initial | Evidence |
|---|---|---|---|---|---|---|---|
|  | 1 | 1 | 5 | (ASKIP,NORM) | BLUE | Tran: | app/bms/COUSR03.bms:29 |
| TRNNAME | 1 | 7 | 4 | (ASKIP,FSET,NORM) | BLUE |  | app/bms/COUSR03.bms:34 |
| TITLE01 | 1 | 21 | 40 | (ASKIP,FSET,NORM) | YELLOW |  | app/bms/COUSR03.bms:38 |
|  | 1 | 65 | 5 | (ASKIP,NORM) | BLUE | Date: | app/bms/COUSR03.bms:42 |
| CURDATE | 1 | 71 | 8 | (ASKIP,FSET,NORM) | BLUE | mm/dd/yy | app/bms/COUSR03.bms:47 |
|  | 2 | 1 | 5 | (ASKIP,NORM) | BLUE | Prog: | app/bms/COUSR03.bms:52 |
| PGMNAME | 2 | 7 | 8 | (ASKIP,FSET,NORM) | BLUE |  | app/bms/COUSR03.bms:57 |
| TITLE02 | 2 | 21 | 40 | (ASKIP,FSET,NORM) | YELLOW |  | app/bms/COUSR03.bms:61 |
|  | 2 | 65 | 5 | (ASKIP,NORM) | BLUE | Time: | app/bms/COUSR03.bms:65 |
| CURTIME | 2 | 71 | 8 | (ASKIP,FSET,NORM) | BLUE | hh:mm:ss | app/bms/COUSR03.bms:70 |
|  | 4 | 35 | 11 | (ASKIP,BRT) | NEUTRAL | Delete User | app/bms/COUSR03.bms:75 |
|  | 6 | 6 | 14 | (ASKIP,NORM) | GREEN | Enter User ID: | app/bms/COUSR03.bms:80 |
| USRIDIN | 6 | 21 | 8 | (FSET,IC,NORM,UNPROT) | GREEN |  | app/bms/COUSR03.bms:85 |
|  | 6 | 30 | 0 | (ASKIP,NORM) |  |  | app/bms/COUSR03.bms:90 |
|  | 8 | 6 | 70 | (ASKIP,NORM) | YELLOW | ***********************************************- DFHMDF ATTRB=(ASKIP,NORM),                                     - COLOR=TURQUOISE,                                        - LENGTH=11,                                              - POS=(11,6),                                             - INITIAL= | app/bms/COUSR03.bms:93 |
| FNAME | 11 | 18 | 20 | (ASKIP,FSET,NORM) | BLUE |  | app/bms/COUSR03.bms:103 |
|  | 11 | 39 | 0 | (ASKIP,NORM) |  |  | app/bms/COUSR03.bms:108 |
|  | 13 | 6 | 10 | (ASKIP,NORM) | TURQUOISE | Last Name: | app/bms/COUSR03.bms:111 |
| LNAME | 13 | 18 | 20 | (ASKIP,FSET,NORM) | BLUE |  | app/bms/COUSR03.bms:116 |
|  | 13 | 39 | 0 | (ASKIP,NORM) | GREEN |  | app/bms/COUSR03.bms:121 |
|  | 15 | 6 | 11 | (ASKIP,NORM) | TURQUOISE | User Type:  | app/bms/COUSR03.bms:125 |
| USRTYPE | 15 | 17 | 1 | (ASKIP,FSET,NORM) | BLUE |  | app/bms/COUSR03.bms:130 |
|  | 15 | 19 | 17 | (ASKIP,NORM) | BLUE | (A=Admin, U=User) | app/bms/COUSR03.bms:135 |
| ERRMSG | 23 | 1 | 78 | (ASKIP,BRT,FSET) | RED |  | app/bms/COUSR03.bms:140 |
|  | 24 | 1 | 58 | (ASKIP,NORM) | YELLOW | ENTER=Fetch  F3=Back  F4=Clear  F5=Delete | app/bms/COUSR03.bms:144 |

## Function keys

| Key | Action | Target | Evidence |
|---|---|---|---|
| DFHENTER | WHEN DFHENTER |  | app/cbl/COUSR03C.cbl:109 |
| DFHPF3 | WHEN DFHPF3 |  | app/cbl/COUSR03C.cbl:111 |
| DFHPF4 | WHEN DFHPF4 |  | app/cbl/COUSR03C.cbl:119 |
| DFHPF5 | WHEN DFHPF5 |  | app/cbl/COUSR03C.cbl:121 |
| DFHPF12 | WHEN DFHPF12 |  | app/cbl/COUSR03C.cbl:123 |

## Validation and messages

Message literals for these programs are indexed in [Error handling](../../12-error-handling-messages.md).

## Behaviour

See the program specifications linked from the transaction catalog for first-time display and AID handling.

## Sources

- `app/bms/COUSR03.bms:19`
- `docs/_work/online/screens/COUSR03.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
