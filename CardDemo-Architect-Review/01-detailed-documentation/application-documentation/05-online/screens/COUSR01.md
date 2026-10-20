# Screen COUSR01

| Item | Value |
|---|---|
| Mapset | COUSR01 |
| Maps | COUSR1A |
| Source | app/bms/COUSR01.bms:19 |
| Module | base |
| Programs | COUSR01C |
| Transactions | CU01 |

## Purpose

Mapset COUSR01 is defined in the BMS source cited below. Field text in the mockup comes from BMS INITIAL and POS values already extracted.

## Map COUSR1A

## Layout mockup

```text
Tran: XXXX          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Date: mm/dd/yy
Prog: XXXXXXXX      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Time: hh:mm:ss

                                  Add User



     First Name: ____________________       Last Name: ____________________


     User ID: ________ (8 Char)             Password: ******** (8 Char)


     User Type: _ (A=Admin, U=User)








XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
ENTER=Add User  F3=Back  F4=Clear  F12=Exit
```

## Fields

| Field | Row | Col | Len | Attributes | Color | Initial | Evidence |
|---|---|---|---|---|---|---|---|
|  | 1 | 1 | 5 | (ASKIP,NORM) | BLUE | Tran: | app/bms/COUSR01.bms:29 |
| TRNNAME | 1 | 7 | 4 | (ASKIP,FSET,NORM) | BLUE |  | app/bms/COUSR01.bms:34 |
| TITLE01 | 1 | 21 | 40 | (ASKIP,FSET,NORM) | YELLOW |  | app/bms/COUSR01.bms:38 |
|  | 1 | 65 | 5 | (ASKIP,NORM) | BLUE | Date: | app/bms/COUSR01.bms:42 |
| CURDATE | 1 | 71 | 8 | (ASKIP,FSET,NORM) | BLUE | mm/dd/yy | app/bms/COUSR01.bms:47 |
|  | 2 | 1 | 5 | (ASKIP,NORM) | BLUE | Prog: | app/bms/COUSR01.bms:52 |
| PGMNAME | 2 | 7 | 8 | (ASKIP,FSET,NORM) | BLUE |  | app/bms/COUSR01.bms:57 |
| TITLE02 | 2 | 21 | 40 | (ASKIP,FSET,NORM) | YELLOW |  | app/bms/COUSR01.bms:61 |
|  | 2 | 65 | 5 | (ASKIP,NORM) | BLUE | Time: | app/bms/COUSR01.bms:65 |
| CURTIME | 2 | 71 | 8 | (ASKIP,FSET,NORM) | BLUE | hh:mm:ss | app/bms/COUSR01.bms:70 |
|  | 4 | 35 | 9 | (ASKIP,BRT) | NEUTRAL | Add User | app/bms/COUSR01.bms:75 |
|  | 8 | 6 | 11 |  | TURQUOISE | First Name: | app/bms/COUSR01.bms:80 |
| FNAME | 8 | 18 | 20 | (FSET,IC,NORM,UNPROT) | GREEN |  | app/bms/COUSR01.bms:84 |
|  | 8 | 39 | 0 | (ASKIP,NORM) |  |  | app/bms/COUSR01.bms:89 |
|  | 8 | 45 | 10 | (ASKIP,NORM) | TURQUOISE | Last Name: | app/bms/COUSR01.bms:92 |
| LNAME | 8 | 56 | 20 | (FSET,NORM,UNPROT) | GREEN |  | app/bms/COUSR01.bms:97 |
|  | 8 | 77 | 0 | (ASKIP,NORM) | GREEN |  | app/bms/COUSR01.bms:102 |
|  | 11 | 6 | 8 | (ASKIP,NORM) | TURQUOISE | User ID: | app/bms/COUSR01.bms:106 |
| USERID | 11 | 15 | 8 | (FSET,NORM,UNPROT) | GREEN |  | app/bms/COUSR01.bms:111 |
|  | 11 | 24 | 8 | (ASKIP,NORM) | BLUE | (8 Char) | app/bms/COUSR01.bms:116 |
|  | 11 | 45 | 9 | (ASKIP,NORM) | TURQUOISE | Password: | app/bms/COUSR01.bms:121 |
| PASSWD | 11 | 55 | 8 | (DRK,FSET,UNPROT) | GREEN |  | app/bms/COUSR01.bms:126 |
|  | 11 | 64 | 8 | (ASKIP,NORM) | BLUE | (8 Char) | app/bms/COUSR01.bms:131 |
|  | 14 | 6 | 11 | (ASKIP,NORM) | TURQUOISE | User Type:  | app/bms/COUSR01.bms:136 |
| USRTYPE | 14 | 17 | 1 | (FSET,NORM,UNPROT) | GREEN |  | app/bms/COUSR01.bms:141 |
|  | 14 | 19 | 17 | (ASKIP,NORM) | BLUE | (A=Admin, U=User) | app/bms/COUSR01.bms:146 |
| ERRMSG | 23 | 1 | 78 | (ASKIP,BRT,FSET) | RED |  | app/bms/COUSR01.bms:151 |
|  | 24 | 1 | 43 | (ASKIP,NORM) | YELLOW | ENTER=Add User  F3=Back  F4=Clear  F12=Exit | app/bms/COUSR01.bms:155 |

## Function keys

| Key | Action | Target | Evidence |
|---|---|---|---|
| DFHENTER | WHEN DFHENTER |  | app/cbl/COUSR01C.cbl:91 |
| DFHPF3 | WHEN DFHPF3 |  | app/cbl/COUSR01C.cbl:93 |
| DFHPF4 | WHEN DFHPF4 |  | app/cbl/COUSR01C.cbl:96 |

## Validation and messages

Message literals for these programs are indexed in [Error handling](../../12-error-handling-messages.md).

## Behaviour

See the program specifications linked from the transaction catalog for first-time display and AID handling.

## Sources

- `app/bms/COUSR01.bms:19`
- `docs/_work/online/screens/COUSR01.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
