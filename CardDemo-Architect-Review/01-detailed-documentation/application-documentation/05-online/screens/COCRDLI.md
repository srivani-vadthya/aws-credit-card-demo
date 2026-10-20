# Screen COCRDLI

| Item | Value |
|---|---|
| Mapset | COCRDLI |
| Maps | CCRDLIA |
| Source | app/bms/COCRDLI.bms:20 |
| Module | base |
| Programs |  |
| Transactions |  |

## Purpose

Mapset COCRDLI is defined in the BMS source cited below. Field text in the mockup comes from BMS INITIAL and POS values already extracted.

## Map CCRDLIA

## Layout mockup

```text
Tran: XXXX          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Date: mm/dd/yy
Prog: XXXXXXXX      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Time: hh:mm:ss

                              List Credit Cards                      Page  XXX

                     Account Number    :   ___________
                     Credit Card Number:   ________________

         Select     Account Number           Card Number         Active
         ------    ---------------        ---------------       --------
           X         XXXXXXXXXXX          XXXXXXXXXXXXXXXX        X
           X X       XXXXXXXXXXX          XXXXXXXXXXXXXXXX        X
           X X       XXXXXXXXXXX          XXXXXXXXXXXXXXXX        X
           X X       XXXXXXXXXXX          XXXXXXXXXXXXXXXX        X
           X X       XXXXXXXXXXX          XXXXXXXXXXXXXXXX        X
           X X       XXXXXXXXXXX          XXXXXXXXXXXXXXXX        X
           X X       XXXXXXXXXXX          XXXXXXXXXXXXXXXX        X


                  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  F3=Exit F7=Backward  F8=Forward
```

## Fields

| Field | Row | Col | Len | Attributes | Color | Initial | Evidence |
|---|---|---|---|---|---|---|---|
|  | 1 | 1 | 5 | (ASKIP,NORM) | BLUE | Tran: | app/bms/COCRDLI.bms:29 |
| TRNNAME | 1 | 7 | 4 | (ASKIP,FSET,NORM) | BLUE |  | app/bms/COCRDLI.bms:34 |
| TITLE01 | 1 | 21 | 40 | (ASKIP,NORM) | YELLOW |  | app/bms/COCRDLI.bms:38 |
|  | 1 | 65 | 5 | (ASKIP,NORM) | BLUE | Date: | app/bms/COCRDLI.bms:42 |
| CURDATE | 1 | 71 | 8 | (ASKIP,NORM) | BLUE | mm/dd/yy | app/bms/COCRDLI.bms:47 |
|  | 2 | 1 | 5 | (ASKIP,NORM) | BLUE | Prog: | app/bms/COCRDLI.bms:52 |
| PGMNAME | 2 | 7 | 8 | (ASKIP,NORM) | BLUE |  | app/bms/COCRDLI.bms:57 |
| TITLE02 | 2 | 21 | 40 | (ASKIP,NORM) | YELLOW |  | app/bms/COCRDLI.bms:61 |
|  | 2 | 65 | 5 | (ASKIP,NORM) | BLUE | Time: | app/bms/COCRDLI.bms:65 |
| CURTIME | 2 | 71 | 8 | (ASKIP,NORM) | BLUE | hh:mm:ss | app/bms/COCRDLI.bms:70 |
|  | 4 | 31 | 17 |  | NEUTRAL | List Credit Cards | app/bms/COCRDLI.bms:75 |
|  | 4 | 70 | 5 |  |  | Page  | app/bms/COCRDLI.bms:79 |
| PAGENO | 4 | 76 | 3 |  |  |  | app/bms/COCRDLI.bms:82 |
|  | 6 | 22 | 19 | (ASKIP,NORM) | TURQUOISE | Account Number    : | app/bms/COCRDLI.bms:84 |
| ACCTSID | 6 | 44 | 11 | (FSET,IC,NORM,UNPROT) | GREEN |  | app/bms/COCRDLI.bms:89 |
|  | 6 | 56 | 0 |  |  |  | app/bms/COCRDLI.bms:94 |
|  | 7 | 22 | 19 | (ASKIP,NORM) | TURQUOISE | Credit Card Number: | app/bms/COCRDLI.bms:96 |
| CARDSID | 7 | 44 | 16 | (FSET,NORM,UNPROT) | GREEN |  | app/bms/COCRDLI.bms:101 |
|  | 7 | 61 | 0 |  |  |  | app/bms/COCRDLI.bms:106 |
|  | 9 | 10 | 10 |  | NEUTRAL | Select     | app/bms/COCRDLI.bms:108 |
|  | 9 | 21 | 14 |  | NEUTRAL | Account Number | app/bms/COCRDLI.bms:112 |
|  | 9 | 45 | 13 |  | NEUTRAL |  Card Number  | app/bms/COCRDLI.bms:116 |
|  | 9 | 66 | 7 |  | NEUTRAL | Active  | app/bms/COCRDLI.bms:120 |
|  | 10 | 10 | 6 |  | NEUTRAL | ------ | app/bms/COCRDLI.bms:124 |
|  | 10 | 20 | 15 |  | NEUTRAL | --------------- | app/bms/COCRDLI.bms:128 |
|  | 10 | 43 | 15 |  | NEUTRAL | --------------- | app/bms/COCRDLI.bms:132 |
|  | 10 | 65 | 8 |  | NEUTRAL | -------- | app/bms/COCRDLI.bms:136 |
| CRDSEL1 | 11 | 12 | 1 | (FSET,NORM,PROT) | DEFAULT |  | app/bms/COCRDLI.bms:140 |
|  | 11 | 14 | 0 |  |  |  | app/bms/COCRDLI.bms:145 |
| ACCTNO1 | 11 | 22 | 11 | (NORM,PROT) | DEFAULT |  | app/bms/COCRDLI.bms:147 |
| CRDNUM1 | 11 | 43 | 16 | (NORM,PROT) | DEFAULT |  | app/bms/COCRDLI.bms:152 |
| CRDSTS1 | 11 | 67 | 1 | (NORM,PROT) | DEFAULT |  | app/bms/COCRDLI.bms:157 |
| CRDSEL2 | 12 | 12 | 1 | (FSET,NORM,PROT) | DEFAULT |  | app/bms/COCRDLI.bms:162 |
|  | 12 | 14 | 0 |  |  |  | app/bms/COCRDLI.bms:167 |
| CRDSTP2 | 12 | 14 | 1 | (ASKIP,DRK,FSET) | DEFAULT |  | app/bms/COCRDLI.bms:169 |
| ACCTNO2 | 12 | 22 | 11 | (NORM,PROT) | DEFAULT |  | app/bms/COCRDLI.bms:174 |
| CRDNUM2 | 12 | 43 | 16 | (NORM,PROT) | DEFAULT |  | app/bms/COCRDLI.bms:179 |
| CRDSTS2 | 12 | 67 | 1 | (NORM,PROT) | DEFAULT |  | app/bms/COCRDLI.bms:184 |
| CRDSEL3 | 13 | 12 | 1 | (FSET,NORM,PROT) | DEFAULT |  | app/bms/COCRDLI.bms:189 |
|  | 13 | 14 | 0 |  |  |  | app/bms/COCRDLI.bms:194 |
| CRDSTP3 | 13 | 14 | 1 | (ASKIP,DRK,FSET) | DEFAULT |  | app/bms/COCRDLI.bms:196 |
| ACCTNO3 | 13 | 22 | 11 | (NORM,PROT) | DEFAULT |  | app/bms/COCRDLI.bms:201 |
| CRDNUM3 | 13 | 43 | 16 | (NORM,PROT) | DEFAULT |  | app/bms/COCRDLI.bms:206 |
| CRDSTS3 | 13 | 67 | 1 | (NORM,PROT) | DEFAULT |  | app/bms/COCRDLI.bms:211 |
| CRDSEL4 | 14 | 12 | 1 | (FSET,NORM,PROT) | DEFAULT |  | app/bms/COCRDLI.bms:216 |
|  | 14 | 14 | 0 |  |  |  | app/bms/COCRDLI.bms:221 |
| CRDSTP4 | 14 | 14 | 1 | (ASKIP,DRK,FSET) | DEFAULT |  | app/bms/COCRDLI.bms:223 |
| ACCTNO4 | 14 | 22 | 11 | (NORM,PROT) | DEFAULT |  | app/bms/COCRDLI.bms:228 |
| CRDNUM4 | 14 | 43 | 16 | (NORM,PROT) | DEFAULT |  | app/bms/COCRDLI.bms:233 |
| CRDSTS4 | 14 | 67 | 1 | (NORM,PROT) | DEFAULT |  | app/bms/COCRDLI.bms:238 |
| CRDSEL5 | 15 | 12 | 1 | (FSET,NORM,PROT) | DEFAULT |  | app/bms/COCRDLI.bms:243 |
|  | 15 | 14 | 0 |  |  |  | app/bms/COCRDLI.bms:248 |
| CRDSTP5 | 15 | 14 | 1 | (ASKIP,DRK,FSET) | DEFAULT |  | app/bms/COCRDLI.bms:250 |
| ACCTNO5 | 15 | 22 | 11 | (NORM,PROT) | DEFAULT |  | app/bms/COCRDLI.bms:255 |
| CRDNUM5 | 15 | 43 | 16 | (NORM,PROT) | DEFAULT |  | app/bms/COCRDLI.bms:260 |
| CRDSTS5 | 15 | 67 | 1 | (NORM,PROT) | DEFAULT |  | app/bms/COCRDLI.bms:265 |
| CRDSEL6 | 16 | 12 | 1 | (FSET,NORM,PROT) | DEFAULT |  | app/bms/COCRDLI.bms:270 |
|  | 16 | 14 | 0 |  |  |  | app/bms/COCRDLI.bms:275 |
| CRDSTP6 | 16 | 14 | 1 | (ASKIP,DRK,FSET) | DEFAULT |  | app/bms/COCRDLI.bms:277 |
| ACCTNO6 | 16 | 22 | 11 | (NORM,PROT) | DEFAULT |  | app/bms/COCRDLI.bms:282 |
| CRDNUM6 | 16 | 43 | 16 | (NORM,PROT) | DEFAULT |  | app/bms/COCRDLI.bms:287 |
| CRDSTS6 | 16 | 67 | 1 | (NORM,PROT) | DEFAULT |  | app/bms/COCRDLI.bms:292 |
| CRDSEL7 | 17 | 12 | 1 | (FSET,NORM,PROT) | DEFAULT |  | app/bms/COCRDLI.bms:297 |
|  | 17 | 14 | 0 |  |  |  | app/bms/COCRDLI.bms:302 |
| CRDSTP7 | 17 | 14 | 1 | (ASKIP,DRK,FSET) | DEFAULT |  | app/bms/COCRDLI.bms:304 |
| ACCTNO7 | 17 | 22 | 11 | (NORM,PROT) | DEFAULT |  | app/bms/COCRDLI.bms:309 |
| CRDNUM7 | 17 | 43 | 16 | (NORM,PROT) | DEFAULT |  | app/bms/COCRDLI.bms:314 |
| CRDSTS7 | 17 | 67 | 1 | (NORM,PROT) | DEFAULT |  | app/bms/COCRDLI.bms:319 |
| INFOMSG | 20 | 19 | 45 | (PROT) | NEUTRAL |  | app/bms/COCRDLI.bms:324 |
|  | 20 | 65 | 0 |  |  |  | app/bms/COCRDLI.bms:329 |
| ERRMSG | 23 | 1 | 78 | (ASKIP,BRT,FSET) | RED |  | app/bms/COCRDLI.bms:331 |
|  | 24 | 1 | 78 | (ASKIP,NORM) | TURQUOISE |   F3=Exit F7=Backward  F8=Forward | app/bms/COCRDLI.bms:335 |

## Function keys

| Key | Action | Target | Evidence |
|---|---|---|---|
|   |   |   |   |

## Validation and messages

Message literals for these programs are indexed in [Error handling](../../12-error-handling-messages.md).

## Behaviour

See the program specifications linked from the transaction catalog for first-time display and AID handling.

## Sources

- `app/bms/COCRDLI.bms:20`
- `docs/_work/online/screens/COCRDLI.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
