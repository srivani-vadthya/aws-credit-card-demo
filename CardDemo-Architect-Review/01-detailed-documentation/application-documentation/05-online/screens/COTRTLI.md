# Screen COTRTLI

| Item | Value |
|---|---|
| Mapset | COTRTLI |
| Maps | CTRTLIA |
| Source | app/app-transaction-type-db2/bms/COTRTLI.bms:20 |
| Module | trantype |
| Programs |  |
| Transactions |  |

## Purpose

Mapset COTRTLI is defined in the BMS source cited below. Field text in the mockup comes from BMS INITIAL and POS values already extracted.

## Map CTRTLIA

## Layout mockup

```text
Tran: XXXX          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Date: mm/dd/yy
Prog: XXXXXXXX      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Time: hh:mm:ss

                           Maintain Transaction Type                 Page  XXX

                             Type Filter:  __

   Description Filter:  __________________________________________________

   Select      Type                      Description
   ------     -----     ------------------------------------------------ -
     X          XX      __________________________________________________
     X          XX      __________________________________________________
     X          XX      __________________________________________________
     X          XX      __________________________________________________
     X          XX      __________________________________________________
     X          XX      __________________________________________________
     X          XX      __________________________________________________
     X          XX      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

                  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
F2=Add   F3=Exit  F7=Page Up   F8=Page Dn  F10=Save
```

## Fields

| Field | Row | Col | Len | Attributes | Color | Initial | Evidence |
|---|---|---|---|---|---|---|---|
|  | 1 | 1 | 5 | (ASKIP,NORM) | BLUE | Tran: | app/app-transaction-type-db2/bms/COTRTLI.bms:29 |
| TRNNAME | 1 | 7 | 4 | (ASKIP,FSET,NORM) | BLUE |  | app/app-transaction-type-db2/bms/COTRTLI.bms:34 |
| TITLE01 | 1 | 21 | 40 | (ASKIP,NORM) | YELLOW |  | app/app-transaction-type-db2/bms/COTRTLI.bms:38 |
|  | 1 | 65 | 5 | (ASKIP,NORM) | BLUE | Date: | app/app-transaction-type-db2/bms/COTRTLI.bms:42 |
| CURDATE | 1 | 71 | 8 | (ASKIP,NORM) | BLUE | mm/dd/yy | app/app-transaction-type-db2/bms/COTRTLI.bms:47 |
|  | 2 | 1 | 5 | (ASKIP,NORM) | BLUE | Prog: | app/app-transaction-type-db2/bms/COTRTLI.bms:52 |
| PGMNAME | 2 | 7 | 8 | (ASKIP,NORM) | BLUE |  | app/app-transaction-type-db2/bms/COTRTLI.bms:57 |
| TITLE02 | 2 | 21 | 40 | (ASKIP,NORM) | YELLOW |  | app/app-transaction-type-db2/bms/COTRTLI.bms:61 |
|  | 2 | 65 | 5 | (ASKIP,NORM) | BLUE | Time: | app/app-transaction-type-db2/bms/COTRTLI.bms:65 |
| CURTIME | 2 | 71 | 8 | (ASKIP,NORM) | BLUE | hh:mm:ss | app/app-transaction-type-db2/bms/COTRTLI.bms:70 |
|  | 4 | 28 | 25 |  | NEUTRAL | Maintain Transaction Type | app/app-transaction-type-db2/bms/COTRTLI.bms:75 |
|  | 4 | 70 | 5 |  |  | Page  | app/app-transaction-type-db2/bms/COTRTLI.bms:79 |
| PAGENO | 4 | 76 | 3 |  |  |  | app/app-transaction-type-db2/bms/COTRTLI.bms:82 |
|  | 6 | 30 | 12 | (ASKIP,NORM) | TURQUOISE | Type Filter: | app/app-transaction-type-db2/bms/COTRTLI.bms:84 |
| TRTYPE | 6 | 44 | 2 | (FSET,IC,NORM,UNPROT) | GREEN |  | app/app-transaction-type-db2/bms/COTRTLI.bms:89 |
|  | 6 | 47 | 0 |  |  |  | app/app-transaction-type-db2/bms/COTRTLI.bms:94 |
|  | 8 | 4 | 19 | (ASKIP,NORM) | TURQUOISE | Description Filter: | app/app-transaction-type-db2/bms/COTRTLI.bms:96 |
| TRDESC | 8 | 25 | 50 | (FSET,NORM,UNPROT) | GREEN |  | app/app-transaction-type-db2/bms/COTRTLI.bms:101 |
|  | 8 | 76 | 0 |  |  |  | app/app-transaction-type-db2/bms/COTRTLI.bms:106 |
|  | 10 | 4 | 10 |  | NEUTRAL | Select     | app/app-transaction-type-db2/bms/COTRTLI.bms:108 |
|  | 10 | 16 | 4 |  | NEUTRAL | Type | app/app-transaction-type-db2/bms/COTRTLI.bms:112 |
|  | 10 | 42 | 11 |  | NEUTRAL | Description | app/app-transaction-type-db2/bms/COTRTLI.bms:116 |
|  | 11 | 4 | 6 |  | NEUTRAL | ------ | app/app-transaction-type-db2/bms/COTRTLI.bms:120 |
|  | 11 | 15 | 5 |  | NEUTRAL | ----- | app/app-transaction-type-db2/bms/COTRTLI.bms:124 |
|  | 11 | 25 | 50 |  | NEUTRAL | ------------------------------------------------ --- | app/app-transaction-type-db2/bms/COTRTLI.bms:128 |
| TRTSEL1 | 12 | 6 | 1 | (FSET,NORM,PROT) | DEFAULT |  | app/app-transaction-type-db2/bms/COTRTLI.bms:133 |
|  | 12 | 8 | 0 |  |  |  | app/app-transaction-type-db2/bms/COTRTLI.bms:138 |
| TRTTYP1 | 12 | 17 | 2 | (FSET,NORM,PROT) | DEFAULT |  | app/app-transaction-type-db2/bms/COTRTLI.bms:140 |
|  | 12 | 20 | 0 |  |  |  | app/app-transaction-type-db2/bms/COTRTLI.bms:145 |
| TRTYPD1 | 12 | 25 | 50 | (FSET,NORM,UNPROT) | DEFAULT |  | app/app-transaction-type-db2/bms/COTRTLI.bms:147 |
|  | 12 | 76 | 0 |  |  |  | app/app-transaction-type-db2/bms/COTRTLI.bms:152 |
| TRTSEL2 | 13 | 6 | 1 | (FSET,NORM,PROT) | DEFAULT |  | app/app-transaction-type-db2/bms/COTRTLI.bms:154 |
|  | 13 | 8 | 0 |  |  |  | app/app-transaction-type-db2/bms/COTRTLI.bms:159 |
| TRTTYP2 | 13 | 17 | 2 | (FSET,NORM,PROT) | DEFAULT |  | app/app-transaction-type-db2/bms/COTRTLI.bms:161 |
|  | 13 | 20 | 0 |  |  |  | app/app-transaction-type-db2/bms/COTRTLI.bms:166 |
| TRTYPD2 | 13 | 25 | 50 | (FSET,NORM,UNPROT) | DEFAULT |  | app/app-transaction-type-db2/bms/COTRTLI.bms:168 |
|  | 13 | 76 | 0 |  |  |  | app/app-transaction-type-db2/bms/COTRTLI.bms:173 |
| TRTSEL3 | 14 | 6 | 1 | (FSET,NORM,PROT) | DEFAULT |  | app/app-transaction-type-db2/bms/COTRTLI.bms:175 |
|  | 14 | 8 | 0 |  |  |  | app/app-transaction-type-db2/bms/COTRTLI.bms:180 |
| TRTTYP3 | 14 | 17 | 2 | (FSET,NORM,PROT) | DEFAULT |  | app/app-transaction-type-db2/bms/COTRTLI.bms:182 |
|  | 14 | 20 | 0 |  |  |  | app/app-transaction-type-db2/bms/COTRTLI.bms:187 |
| TRTYPD3 | 14 | 25 | 50 | (FSET,NORM,UNPROT) | DEFAULT |  | app/app-transaction-type-db2/bms/COTRTLI.bms:189 |
|  | 14 | 76 | 0 |  |  |  | app/app-transaction-type-db2/bms/COTRTLI.bms:194 |
| TRTSEL4 | 15 | 6 | 1 | (FSET,NORM,PROT) | DEFAULT |  | app/app-transaction-type-db2/bms/COTRTLI.bms:196 |
|  | 15 | 8 | 0 |  |  |  | app/app-transaction-type-db2/bms/COTRTLI.bms:201 |
| TRTTYP4 | 15 | 17 | 2 | (FSET,NORM,PROT) | DEFAULT |  | app/app-transaction-type-db2/bms/COTRTLI.bms:203 |
|  | 15 | 20 | 0 |  |  |  | app/app-transaction-type-db2/bms/COTRTLI.bms:208 |
| TRTYPD4 | 15 | 25 | 50 | (FSET,NORM,UNPROT) | DEFAULT |  | app/app-transaction-type-db2/bms/COTRTLI.bms:210 |
|  | 15 | 76 | 0 |  |  |  | app/app-transaction-type-db2/bms/COTRTLI.bms:215 |
| TRTSEL5 | 16 | 6 | 1 | (FSET,NORM,PROT) | DEFAULT |  | app/app-transaction-type-db2/bms/COTRTLI.bms:217 |
|  | 16 | 8 | 0 |  |  |  | app/app-transaction-type-db2/bms/COTRTLI.bms:222 |
| TRTTYP5 | 16 | 17 | 2 | (FSET,NORM,PROT) | DEFAULT |  | app/app-transaction-type-db2/bms/COTRTLI.bms:224 |
|  | 16 | 20 | 0 |  |  |  | app/app-transaction-type-db2/bms/COTRTLI.bms:229 |
| TRTYPD5 | 16 | 25 | 50 | (FSET,NORM,UNPROT) | DEFAULT |  | app/app-transaction-type-db2/bms/COTRTLI.bms:231 |
|  | 16 | 76 | 0 |  |  |  | app/app-transaction-type-db2/bms/COTRTLI.bms:236 |
| TRTSEL6 | 17 | 6 | 1 | (FSET,NORM,PROT) | DEFAULT |  | app/app-transaction-type-db2/bms/COTRTLI.bms:238 |
|  | 17 | 8 | 0 |  |  |  | app/app-transaction-type-db2/bms/COTRTLI.bms:243 |
| TRTTYP6 | 17 | 17 | 2 | (FSET,NORM,PROT) | DEFAULT |  | app/app-transaction-type-db2/bms/COTRTLI.bms:245 |
|  | 17 | 20 | 0 |  |  |  | app/app-transaction-type-db2/bms/COTRTLI.bms:250 |
| TRTYPD6 | 17 | 25 | 50 | (FSET,NORM,UNPROT) | DEFAULT |  | app/app-transaction-type-db2/bms/COTRTLI.bms:252 |
|  | 17 | 76 | 0 |  |  |  | app/app-transaction-type-db2/bms/COTRTLI.bms:257 |
| TRTSEL7 | 18 | 6 | 1 | (FSET,NORM,PROT) | DEFAULT |  | app/app-transaction-type-db2/bms/COTRTLI.bms:259 |
|  | 18 | 8 | 0 |  |  |  | app/app-transaction-type-db2/bms/COTRTLI.bms:264 |
| TRTTYP7 | 18 | 17 | 2 | (FSET,NORM,PROT) | DEFAULT |  | app/app-transaction-type-db2/bms/COTRTLI.bms:266 |
|  | 18 | 20 | 0 |  |  |  | app/app-transaction-type-db2/bms/COTRTLI.bms:271 |
| TRTYPD7 | 18 | 25 | 50 | (FSET,NORM,UNPROT) | DEFAULT |  | app/app-transaction-type-db2/bms/COTRTLI.bms:273 |
|  | 18 | 76 | 0 |  |  |  | app/app-transaction-type-db2/bms/COTRTLI.bms:278 |
| TRTSELA | 19 | 6 | 1 | (FSET,NORM,PROT) | DEFAULT |  | app/app-transaction-type-db2/bms/COTRTLI.bms:280 |
|  | 19 | 8 | 0 |  |  |  | app/app-transaction-type-db2/bms/COTRTLI.bms:285 |
| TRTTYPA | 19 | 17 | 2 | (FSET,NORM,PROT) | DEFAULT |  | app/app-transaction-type-db2/bms/COTRTLI.bms:287 |
|  | 19 | 20 | 0 |  |  |  | app/app-transaction-type-db2/bms/COTRTLI.bms:292 |
| TRTDSCA | 19 | 25 | 50 | (FSET,NORM,PROT) | DEFAULT |  | app/app-transaction-type-db2/bms/COTRTLI.bms:294 |
|  | 19 | 76 | 0 |  |  |  | app/app-transaction-type-db2/bms/COTRTLI.bms:299 |
| INFOMSG | 21 | 19 | 45 | (PROT) | NEUTRAL |  | app/app-transaction-type-db2/bms/COTRTLI.bms:301 |
|  | 21 | 65 | 0 |  |  |  | app/app-transaction-type-db2/bms/COTRTLI.bms:306 |
| ERRMSG | 23 | 1 | 78 | (ASKIP,BRT,FSET) | RED |  | app/app-transaction-type-db2/bms/COTRTLI.bms:308 |
| BUTNF02 | 24 | 1 | 7 | (ASKIP,NORM) | TURQUOISE | F2=Add | app/app-transaction-type-db2/bms/COTRTLI.bms:312 |
| BUTNF03 | 24 | 10 | 7 | (ASKIP,NORM) | TURQUOISE | F3=Exit | app/app-transaction-type-db2/bms/COTRTLI.bms:317 |
| BUTNF07 | 24 | 19 | 10 | (ASKIP,NORM) | TURQUOISE | F7=Page Up | app/app-transaction-type-db2/bms/COTRTLI.bms:322 |
| BUTNF08 | 24 | 32 | 10 | (ASKIP,NORM) | TURQUOISE | F8=Page Dn | app/app-transaction-type-db2/bms/COTRTLI.bms:327 |
| BUTNF10 | 24 | 44 | 8 | (ASKIP,NORM) | TURQUOISE | F10=Save | app/app-transaction-type-db2/bms/COTRTLI.bms:332 |

## Function keys

| Key | Action | Target | Evidence |
|---|---|---|---|
|   |   |   |   |

## Validation and messages

Message literals for these programs are indexed in [Error handling](../../12-error-handling-messages.md).

## Behaviour

See the program specifications linked from the transaction catalog for first-time display and AID handling.

## Sources

- `app/app-transaction-type-db2/bms/COTRTLI.bms:20`
- `docs/_work/online/screens/COTRTLI.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
