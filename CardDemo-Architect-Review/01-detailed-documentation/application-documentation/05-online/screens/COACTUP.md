# Screen COACTUP

| Item | Value |
|---|---|
| Mapset | COACTUP |
| Maps | CACTUPA |
| Source | app/bms/COACTUP.bms:20 |
| Module | base |
| Programs |  |
| Transactions |  |

## Purpose

Mapset COACTUP is defined in the BMS source cited below. Field text in the mockup comes from BMS INITIAL and POS values already extracted.

## Map CACTUPA

## Layout mockup

```text
XXXXXXXXXX          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Date: mm/dd/yy
Prog: XXXXXXXX      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Time: hh:mm:ss

                                Update Account
                  Account Number :   ___________        Active Y/N:  _
       Opened : ____ - __ - __        Credit Limit        : _______________
       Expiry : ____ - __ - __        Cash credit Limit   : _______________
       Reissue: ____ - __ - __        Current Balance     : _______________
                                      Current Cycle Credit: _______________
       Account Group: __________      Current Cycle Debit : _______________
                               Customer Details
       Customer id  : _________                 SSN:  999 - 99 - 9999
       Date of birth: ____ - __ - __            FICO Score:  ___
First Name                 Middle Name:               Last Name :
_________________________  _________________________  _________________________
Address: __________________________________________________   State     __
         __________________________________________________   Zip       _____
City     __________________________________________________   Country   ___
Phone 1: ___ ___ ____  Government Issued Id Ref    :     ____________________
Phone 2: ___ ___ ____  EFT Account Id:  __________  Primary Card Holder Y/N: _

                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
ENTER=Process F3=Exit F5=Save F12=Cancel
```

## Fields

| Field | Row | Col | Len | Attributes | Color | Initial | Evidence |
|---|---|---|---|---|---|---|---|
|  | 1 | 1 | 5 | (ASKIP,NORM) | BLUE | Tran: | app/bms/COACTUP.bms:29 |
| TRNNAME | 1 | 7 | 4 | (ASKIP,FSET,NORM) | BLUE |  | app/bms/COACTUP.bms:34 |
| TITLE01 | 1 | 21 | 40 | (ASKIP,NORM) | YELLOW |  | app/bms/COACTUP.bms:38 |
|  | 1 | 65 | 5 | (ASKIP,NORM) | BLUE | Date: | app/bms/COACTUP.bms:42 |
| CURDATE | 1 | 71 | 8 | (ASKIP,NORM) | BLUE | mm/dd/yy | app/bms/COACTUP.bms:47 |
|  | 2 | 1 | 5 | (ASKIP,NORM) | BLUE | Prog: | app/bms/COACTUP.bms:52 |
| PGMNAME | 2 | 7 | 8 | (ASKIP,NORM) | BLUE |  | app/bms/COACTUP.bms:57 |
| TITLE02 | 2 | 21 | 40 | (ASKIP,NORM) | YELLOW |  | app/bms/COACTUP.bms:61 |
|  | 2 | 65 | 5 | (ASKIP,NORM) | BLUE | Time: | app/bms/COACTUP.bms:65 |
| CURTIME | 2 | 71 | 8 | (ASKIP,NORM) | BLUE | hh:mm:ss | app/bms/COACTUP.bms:70 |
|  | 4 | 33 | 14 |  | NEUTRAL | Update Account | app/bms/COACTUP.bms:75 |
|  | 5 | 19 | 16 | (ASKIP,NORM) | TURQUOISE | Account Number : | app/bms/COACTUP.bms:79 |
| ACCTSID | 5 | 38 | 11 | (IC,UNPROT) |  |  | app/bms/COACTUP.bms:84 |
|  | 5 | 50 | 0 |  |  |  | app/bms/COACTUP.bms:88 |
|  | 5 | 57 | 12 |  | TURQUOISE | Active Y/N:  | app/bms/COACTUP.bms:90 |
| ACSTTUS | 5 | 70 | 1 | (UNPROT) |  |  | app/bms/COACTUP.bms:94 |
|  | 5 | 72 | 0 |  |  |  | app/bms/COACTUP.bms:98 |
|  | 6 | 8 | 8 |  | TURQUOISE | Opened : | app/bms/COACTUP.bms:100 |
| OPNYEAR | 6 | 17 | 4 | (FSET,UNPROT) |  |  | app/bms/COACTUP.bms:104 |
|  | 6 | 22 | 1 |  |  | - | app/bms/COACTUP.bms:109 |
| OPNMON | 6 | 24 | 2 | (UNPROT) |  |  | app/bms/COACTUP.bms:112 |
|  | 6 | 27 | 1 |  |  | - | app/bms/COACTUP.bms:117 |
| OPNDAY | 6 | 29 | 2 | (UNPROT) |  |  | app/bms/COACTUP.bms:120 |
|  | 6 | 32 | 0 |  |  |  | app/bms/COACTUP.bms:125 |
|  | 6 | 39 | 21 | (ASKIP,NORM) | TURQUOISE | Credit Limit        : | app/bms/COACTUP.bms:127 |
| ACRDLIM | 6 | 61 | 15 | (FSET,UNPROT) |  |  | app/bms/COACTUP.bms:132 |
|  | 6 | 77 | 0 |  |  |  | app/bms/COACTUP.bms:136 |
|  | 7 | 8 | 8 |  | TURQUOISE | Expiry : | app/bms/COACTUP.bms:138 |
| EXPYEAR | 7 | 17 | 4 | (UNPROT) |  |  | app/bms/COACTUP.bms:142 |
|  | 7 | 22 | 1 |  |  | - | app/bms/COACTUP.bms:147 |
| EXPMON | 7 | 24 | 2 | (UNPROT) |  |  | app/bms/COACTUP.bms:150 |
|  | 7 | 27 | 1 |  |  | - | app/bms/COACTUP.bms:155 |
| EXPDAY | 7 | 29 | 2 | (UNPROT) |  |  | app/bms/COACTUP.bms:158 |
|  | 7 | 32 | 0 |  |  |  | app/bms/COACTUP.bms:163 |
|  | 7 | 39 | 21 | (ASKIP,NORM) | TURQUOISE | Cash credit Limit   : | app/bms/COACTUP.bms:165 |
| ACSHLIM | 7 | 61 | 15 | (FSET,UNPROT) |  |  | app/bms/COACTUP.bms:170 |
|  | 7 | 77 | 0 |  |  |  | app/bms/COACTUP.bms:174 |
|  | 8 | 8 | 8 |  | TURQUOISE | Reissue: | app/bms/COACTUP.bms:176 |
| RISYEAR | 8 | 17 | 4 | (UNPROT) |  |  | app/bms/COACTUP.bms:180 |
|  | 8 | 22 | 1 |  |  | - | app/bms/COACTUP.bms:185 |
| RISMON | 8 | 24 | 2 | (UNPROT) |  |  | app/bms/COACTUP.bms:188 |
|  | 8 | 27 | 1 |  |  | - | app/bms/COACTUP.bms:193 |
| RISDAY | 8 | 29 | 2 | (UNPROT) |  |  | app/bms/COACTUP.bms:196 |
|  | 8 | 32 | 0 |  |  |  | app/bms/COACTUP.bms:201 |
|  | 8 | 39 | 21 | (ASKIP,NORM) | TURQUOISE | Current Balance     : | app/bms/COACTUP.bms:203 |
| ACURBAL | 8 | 61 | 15 | (FSET,UNPROT) |  |  | app/bms/COACTUP.bms:208 |
|  | 8 | 77 | 0 |  |  |  | app/bms/COACTUP.bms:212 |
|  | 9 | 39 | 21 | (ASKIP,NORM) | TURQUOISE | Current Cycle Credit: | app/bms/COACTUP.bms:214 |
| ACRCYCR | 9 | 61 | 15 | (FSET,UNPROT) |  |  | app/bms/COACTUP.bms:219 |
|  | 9 | 77 | 0 |  |  |  | app/bms/COACTUP.bms:223 |
|  | 10 | 8 | 14 |  | TURQUOISE | Account Group: | app/bms/COACTUP.bms:225 |
| AADDGRP | 10 | 23 | 10 | (UNPROT) |  |  | app/bms/COACTUP.bms:229 |
|  | 10 | 34 | 0 |  |  |  | app/bms/COACTUP.bms:233 |
|  | 10 | 39 | 21 | (ASKIP,NORM) | TURQUOISE | Current Cycle Debit : | app/bms/COACTUP.bms:235 |
| ACRCYDB | 10 | 61 | 15 | (FSET,UNPROT) |  |  | app/bms/COACTUP.bms:240 |
|  | 10 | 77 | 0 |  |  |  | app/bms/COACTUP.bms:244 |
|  | 11 | 32 | 16 |  | NEUTRAL | Customer Details | app/bms/COACTUP.bms:246 |
|  | 12 | 8 | 14 |  | TURQUOISE | Customer id  : | app/bms/COACTUP.bms:250 |
| ACSTNUM | 12 | 23 | 9 | (UNPROT) |  |  | app/bms/COACTUP.bms:254 |
|  | 12 | 33 | 0 |  |  |  | app/bms/COACTUP.bms:258 |
|  | 12 | 49 | 4 |  | TURQUOISE | SSN: | app/bms/COACTUP.bms:260 |
| ACTSSN1 | 12 | 55 | 3 | (UNPROT) |  | 999 | app/bms/COACTUP.bms:264 |
|  | 12 | 59 | 1 |  |  | - | app/bms/COACTUP.bms:269 |
| ACTSSN2 | 12 | 61 | 2 | (UNPROT) |  | 99 | app/bms/COACTUP.bms:272 |
|  | 12 | 64 | 1 |  |  | - | app/bms/COACTUP.bms:277 |
| ACTSSN3 | 12 | 66 | 4 | (UNPROT) |  | 9999 | app/bms/COACTUP.bms:280 |
|  | 12 | 71 | 0 |  |  |  | app/bms/COACTUP.bms:285 |
|  | 13 | 8 | 14 |  | TURQUOISE | Date of birth: | app/bms/COACTUP.bms:287 |
| DOBYEAR | 13 | 23 | 4 | (UNPROT) |  |  | app/bms/COACTUP.bms:291 |
|  | 13 | 28 | 1 |  |  | - | app/bms/COACTUP.bms:296 |
| DOBMON | 13 | 30 | 2 | (UNPROT) |  |  | app/bms/COACTUP.bms:299 |
|  | 13 | 33 | 1 |  |  | - | app/bms/COACTUP.bms:304 |
| DOBDAY | 13 | 35 | 2 | (UNPROT) |  |  | app/bms/COACTUP.bms:307 |
|  | 13 | 38 | 0 |  |  |  | app/bms/COACTUP.bms:312 |
|  | 13 | 49 | 11 |  | TURQUOISE | FICO Score: | app/bms/COACTUP.bms:314 |
| ACSTFCO | 13 | 62 | 3 | (UNPROT) |  |  | app/bms/COACTUP.bms:318 |
|  | 13 | 66 | 0 |  |  |  | app/bms/COACTUP.bms:322 |
|  | 14 | 1 | 10 |  | TURQUOISE | First Name | app/bms/COACTUP.bms:324 |
|  | 14 | 28 | 13 |  | TURQUOISE | Middle Name:  | app/bms/COACTUP.bms:328 |
|  | 14 | 55 | 12 |  | TURQUOISE | Last Name :  | app/bms/COACTUP.bms:332 |
| ACSFNAM | 15 | 1 | 25 | (UNPROT) |  |  | app/bms/COACTUP.bms:336 |
|  | 15 | 27 | 0 |  |  |  | app/bms/COACTUP.bms:340 |
| ACSMNAM | 15 | 28 | 25 | (UNPROT) |  |  | app/bms/COACTUP.bms:342 |
|  | 15 | 54 | 0 |  |  |  | app/bms/COACTUP.bms:346 |
| ACSLNAM | 15 | 55 | 25 | (UNPROT) |  |  | app/bms/COACTUP.bms:348 |
|  | 16 | 1 | 8 |  | TURQUOISE | Address: | app/bms/COACTUP.bms:352 |
| ACSADL1 | 16 | 10 | 50 | (UNPROT) |  |  | app/bms/COACTUP.bms:356 |
|  | 16 | 61 | 0 |  |  |  | app/bms/COACTUP.bms:360 |
|  | 16 | 63 | 6 |  | TURQUOISE | State  | app/bms/COACTUP.bms:362 |
| ACSSTTE | 16 | 73 | 2 | (UNPROT) |  |  | app/bms/COACTUP.bms:366 |
|  | 16 | 76 | 0 |  |  |  | app/bms/COACTUP.bms:370 |
| ACSADL2 | 17 | 10 | 50 | (UNPROT) |  |  | app/bms/COACTUP.bms:372 |
|  | 17 | 61 | 0 |  |  |  | app/bms/COACTUP.bms:376 |
|  | 17 | 63 | 3 |  | TURQUOISE | Zip | app/bms/COACTUP.bms:378 |
| ACSZIPC | 17 | 73 | 5 | (UNPROT) |  |  | app/bms/COACTUP.bms:382 |
|  | 17 | 79 | 0 |  |  |  | app/bms/COACTUP.bms:386 |
|  | 18 | 1 | 5 |  | TURQUOISE | City  | app/bms/COACTUP.bms:388 |
| ACSCITY | 18 | 10 | 50 | (UNPROT) |  |  | app/bms/COACTUP.bms:392 |
|  | 18 | 61 | 0 |  |  |  | app/bms/COACTUP.bms:396 |
|  | 18 | 63 | 7 |  | TURQUOISE | Country | app/bms/COACTUP.bms:398 |
| ACSCTRY | 18 | 73 | 3 | (UNPROT) |  |  | app/bms/COACTUP.bms:402 |
|  | 18 | 77 | 0 |  |  |  | app/bms/COACTUP.bms:406 |
|  | 19 | 1 | 8 |  | TURQUOISE | Phone 1: | app/bms/COACTUP.bms:408 |
| ACSPH1A | 19 | 10 | 3 | (UNPROT) |  |  | app/bms/COACTUP.bms:412 |
| ACSPH1B | 19 | 14 | 3 | (UNPROT) |  |  | app/bms/COACTUP.bms:417 |
| ACSPH1C | 19 | 18 | 4 | (UNPROT) |  |  | app/bms/COACTUP.bms:422 |
|  | 19 | 23 | 0 |  |  |  | app/bms/COACTUP.bms:427 |
|  | 19 | 24 | 30 |  | TURQUOISE | Government Issued Id Ref    :  | app/bms/COACTUP.bms:429 |
| ACSGOVT | 19 | 58 | 20 | (UNPROT) |  |  | app/bms/COACTUP.bms:433 |
|  | 19 | 79 | 0 |  |  |  | app/bms/COACTUP.bms:437 |
|  | 20 | 1 | 8 |  | TURQUOISE | Phone 2: | app/bms/COACTUP.bms:439 |
| ACSPH2A | 20 | 10 | 3 | (UNPROT) |  |  | app/bms/COACTUP.bms:443 |
| ACSPH2B | 20 | 14 | 3 | (UNPROT) |  |  | app/bms/COACTUP.bms:448 |
| ACSPH2C | 20 | 18 | 4 | (UNPROT) |  |  | app/bms/COACTUP.bms:453 |
|  | 20 | 23 | 0 |  |  |  | app/bms/COACTUP.bms:458 |
|  | 20 | 24 | 16 |  | TURQUOISE | EFT Account Id:  | app/bms/COACTUP.bms:460 |
| ACSEFTC | 20 | 41 | 10 | (UNPROT) |  |  | app/bms/COACTUP.bms:464 |
|  | 20 | 52 | 0 |  |  |  | app/bms/COACTUP.bms:468 |
|  | 20 | 53 | 24 |  | TURQUOISE | Primary Card Holder Y/N: | app/bms/COACTUP.bms:470 |
| ACSPFLG | 20 | 78 | 1 | (UNPROT) |  |  | app/bms/COACTUP.bms:474 |
|  | 20 | 80 | 0 |  |  |  | app/bms/COACTUP.bms:478 |
| INFOMSG | 22 | 23 | 45 | (ASKIP) | NEUTRAL |  | app/bms/COACTUP.bms:480 |
|  | 22 | 69 | 0 |  |  |  | app/bms/COACTUP.bms:485 |
|  | 1 | 1 | 9 |  |  |  | app/bms/COACTUP.bms:487 |
| ERRMSG | 23 | 1 | 78 | (ASKIP,BRT,FSET) | RED |  | app/bms/COACTUP.bms:489 |
| FKEYS | 24 | 1 | 21 | (ASKIP,NORM) | YELLOW | ENTER=Process F3=Exit | app/bms/COACTUP.bms:493 |
| FKEY05 | 24 | 23 | 7 | (ASKIP,DRK) | YELLOW | F5=Save | app/bms/COACTUP.bms:498 |
| FKEY12 | 24 | 31 | 10 | (ASKIP,DRK) | YELLOW | F12=Cancel | app/bms/COACTUP.bms:503 |

## Function keys

| Key | Action | Target | Evidence |
|---|---|---|---|
|   |   |   |   |

## Validation and messages

Message literals for these programs are indexed in [Error handling](../../12-error-handling-messages.md).

## Behaviour

See the program specifications linked from the transaction catalog for first-time display and AID handling.

## Sources

- `app/bms/COACTUP.bms:20`
- `docs/_work/online/screens/COACTUP.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
