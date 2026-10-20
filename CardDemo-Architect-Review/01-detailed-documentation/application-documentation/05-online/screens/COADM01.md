# Screen COADM01

| Item | Value |
|---|---|
| Mapset | COADM01 |
| Maps | COADM1A |
| Source | app/bms/COADM01.bms:19 |
| Module | base |
| Programs | COADM01C |
| Transactions | CA00 |

## Purpose

Mapset COADM01 is defined in the BMS source cited below. Field text in the mockup comes from BMS INITIAL and POS values already extracted.

## Map COADM1A

## Layout mockup

```text
Tran: XXXX          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Date: mm/dd/yy
Prog: XXXXXXXX      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Time: hh:mm:ss

                                  Admin Menu















              Please select an option : 99


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
ENTER=Continue  F3=Exit
```

## Fields

| Field | Row | Col | Len | Attributes | Color | Initial | Evidence |
|---|---|---|---|---|---|---|---|
|  | 1 | 1 | 5 | (ASKIP,NORM) | BLUE | Tran: | app/bms/COADM01.bms:29 |
| TRNNAME | 1 | 7 | 4 | (ASKIP,FSET,NORM) | BLUE |  | app/bms/COADM01.bms:34 |
| TITLE01 | 1 | 21 | 40 | (ASKIP,FSET,NORM) | YELLOW |  | app/bms/COADM01.bms:38 |
|  | 1 | 65 | 5 | (ASKIP,NORM) | BLUE | Date: | app/bms/COADM01.bms:42 |
| CURDATE | 1 | 71 | 8 | (ASKIP,FSET,NORM) | BLUE | mm/dd/yy | app/bms/COADM01.bms:47 |
|  | 2 | 1 | 5 | (ASKIP,NORM) | BLUE | Prog: | app/bms/COADM01.bms:52 |
| PGMNAME | 2 | 7 | 8 | (ASKIP,FSET,NORM) | BLUE |  | app/bms/COADM01.bms:57 |
| TITLE02 | 2 | 21 | 40 | (ASKIP,FSET,NORM) | YELLOW |  | app/bms/COADM01.bms:61 |
|  | 2 | 65 | 5 | (ASKIP,NORM) | BLUE | Time: | app/bms/COADM01.bms:65 |
| CURTIME | 2 | 71 | 8 | (ASKIP,FSET,NORM) | BLUE | hh:mm:ss | app/bms/COADM01.bms:70 |
|  | 4 | 35 | 10 | (ASKIP,BRT) | NEUTRAL | Admin Menu | app/bms/COADM01.bms:75 |
| OPTN001 | 6 | 20 | 40 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COADM01.bms:80 |
| OPTN002 | 7 | 20 | 40 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COADM01.bms:85 |
| OPTN003 | 8 | 20 | 40 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COADM01.bms:90 |
| OPTN004 | 9 | 20 | 40 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COADM01.bms:95 |
| OPTN005 | 10 | 20 | 40 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COADM01.bms:100 |
| OPTN006 | 11 | 20 | 40 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COADM01.bms:105 |
| OPTN007 | 12 | 20 | 40 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COADM01.bms:110 |
| OPTN008 | 13 | 20 | 40 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COADM01.bms:115 |
| OPTN009 | 14 | 20 | 40 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COADM01.bms:120 |
| OPTN010 | 15 | 20 | 40 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COADM01.bms:125 |
| OPTN011 | 16 | 20 | 40 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COADM01.bms:130 |
| OPTN012 | 17 | 20 | 40 | (ASKIP,FSET,NORM) | BLUE |   | app/bms/COADM01.bms:135 |
|  | 20 | 15 | 25 | (ASKIP,BRT) | TURQUOISE | Please select an option : | app/bms/COADM01.bms:140 |
| OPTION | 20 | 41 | 2 | (FSET,IC,NORM,NUM,UNPROT) |  |  | app/bms/COADM01.bms:145 |
|  | 20 | 44 | 0 | (ASKIP,NORM) | GREEN |  | app/bms/COADM01.bms:150 |
| ERRMSG | 23 | 1 | 78 | (ASKIP,BRT,FSET) | RED |  | app/bms/COADM01.bms:154 |
|  | 24 | 1 | 23 | (ASKIP,NORM) | YELLOW | ENTER=Continue  F3=Exit | app/bms/COADM01.bms:158 |

## Function keys

| Key | Action | Target | Evidence |
|---|---|---|---|
| DFHENTER | WHEN DFHENTER |  | app/cbl/COADM01C.cbl:98 |
| DFHPF3 | WHEN DFHPF3 |  | app/cbl/COADM01C.cbl:100 |

## Validation and messages

Message literals for these programs are indexed in [Error handling](../../12-error-handling-messages.md).

## Behaviour

See the program specifications linked from the transaction catalog for first-time display and AID handling.

## Sources

- `app/bms/COADM01.bms:19`
- `docs/_work/online/screens/COADM01.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
