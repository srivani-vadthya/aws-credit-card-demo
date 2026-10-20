# Screen COACTVW

| Item | Value |
|---|---|
| Mapset | COACTVW |
| Maps | CACTVWA |
| Source | app/bms/COACTVW.bms:20 |
| Module | base |
| Programs |  |
| Transactions |  |

## Purpose

Mapset COACTVW is defined in the BMS source cited below. Field text in the mockup comes from BMS INITIAL and POS values already extracted.

## Map CACTVWA

## Layout mockup

```text
XXXXXXXXXX          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Date: mm/dd/yy
Prog: XXXXXXXX      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Time: hh:mm:ss

                                View Account
                  Account Number :   ___________        Active Y/N:  X
       Opened:  XXXXXXXXXX            Credit Limit        : XXXXXXXXXXXXXXX
       Expiry:  XXXXXXXXXX            Cash credit Limit   : XXXXXXXXXXXXXXX
       Reissue: XXXXXXXXXX            Current Balance     : XXXXXXXXXXXXXXX
                                      Current Cycle Credit: XXXXXXXXXXXXXXX
       Account Group: XXXXXXXXXX      Current Cycle Debit : XXXXXXXXXXXXXXX
                               Customer Details
       Customer id  : XXXXXXXXX                 SSN: XXXXXXXXXXXX
       Date of birth: XXXXXXXXXX                FICO Score: XXX
First Name                 Middle Name:               Last Name :
XXXXXXXXXXXXXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXX
Address: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   State     XX
         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   Zip       XXXXX
City     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   Country   XXX
Phone 1: XXXXXXXXXXXXX Government Issued Id Ref    :     XXXXXXXXXXXXXXXXXXXX
Phone 2: XXXXXXXXXXXXX EFT Account Id:  XXXXXXXXXX  Primary Card Holder Y/N: X

                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  F3=Exit
```

## Fields

| Field | Row | Col | Len | Attributes | Color | Initial | Evidence |
|---|---|---|---|---|---|---|---|
|  | 1 | 1 | 5 | (ASKIP,NORM) | BLUE | Tran: | app/bms/COACTVW.bms:29 |
| TRNNAME | 1 | 7 | 4 | (ASKIP,FSET,NORM) | BLUE |  | app/bms/COACTVW.bms:34 |
| TITLE01 | 1 | 21 | 40 | (ASKIP,NORM) | YELLOW |  | app/bms/COACTVW.bms:38 |
|  | 1 | 65 | 5 | (ASKIP,NORM) | BLUE | Date: | app/bms/COACTVW.bms:42 |
| CURDATE | 1 | 71 | 8 | (ASKIP,NORM) | BLUE | mm/dd/yy | app/bms/COACTVW.bms:47 |
|  | 2 | 1 | 5 | (ASKIP,NORM) | BLUE | Prog: | app/bms/COACTVW.bms:52 |
| PGMNAME | 2 | 7 | 8 | (ASKIP,NORM) | BLUE |  | app/bms/COACTVW.bms:57 |
| TITLE02 | 2 | 21 | 40 | (ASKIP,NORM) | YELLOW |  | app/bms/COACTVW.bms:61 |
|  | 2 | 65 | 5 | (ASKIP,NORM) | BLUE | Time: | app/bms/COACTVW.bms:65 |
| CURTIME | 2 | 71 | 8 | (ASKIP,NORM) | BLUE | hh:mm:ss | app/bms/COACTVW.bms:70 |
|  | 4 | 33 | 12 |  | NEUTRAL | View Account | app/bms/COACTVW.bms:75 |
|  | 5 | 19 | 16 | (ASKIP,NORM) | TURQUOISE | Account Number : | app/bms/COACTVW.bms:79 |
| ACCTSID | 5 | 38 | 11 | (FSET,IC,NORM,UNPROT) | GREEN |  | app/bms/COACTVW.bms:84 |
|  | 5 | 50 | 0 |  |  |  | app/bms/COACTVW.bms:91 |
|  | 5 | 57 | 12 |  | TURQUOISE | Active Y/N:  | app/bms/COACTVW.bms:93 |
| ACSTTUS | 5 | 70 | 1 | (ASKIP) |  |  | app/bms/COACTVW.bms:97 |
|  | 5 | 72 | 0 |  |  |  | app/bms/COACTVW.bms:101 |
|  | 6 | 8 | 7 |  | TURQUOISE | Opened: | app/bms/COACTVW.bms:103 |
| ADTOPEN | 6 | 17 | 10 |  |  |  | app/bms/COACTVW.bms:107 |
|  | 6 | 28 | 0 |  |  |  | app/bms/COACTVW.bms:110 |
|  | 6 | 39 | 21 | (ASKIP,NORM) | TURQUOISE | Credit Limit        : | app/bms/COACTVW.bms:112 |
| ACRDLIM | 6 | 61 | 15 |  |  |  | app/bms/COACTVW.bms:117 |
|  | 6 | 77 | 0 |  |  |  | app/bms/COACTVW.bms:122 |
|  | 7 | 8 | 7 |  | TURQUOISE | Expiry: | app/bms/COACTVW.bms:124 |
| AEXPDT | 7 | 17 | 10 |  |  |  | app/bms/COACTVW.bms:128 |
|  | 7 | 28 | 0 |  |  |  | app/bms/COACTVW.bms:131 |
|  | 7 | 39 | 21 | (ASKIP,NORM) | TURQUOISE | Cash credit Limit   : | app/bms/COACTVW.bms:133 |
| ACSHLIM | 7 | 61 | 15 |  |  |  | app/bms/COACTVW.bms:138 |
|  | 7 | 77 | 0 |  |  |  | app/bms/COACTVW.bms:143 |
|  | 8 | 8 | 8 |  | TURQUOISE | Reissue: | app/bms/COACTVW.bms:145 |
| AREISDT | 8 | 17 | 10 |  |  |  | app/bms/COACTVW.bms:149 |
|  | 8 | 28 | 0 |  |  |  | app/bms/COACTVW.bms:152 |
|  | 8 | 39 | 21 | (ASKIP,NORM) | TURQUOISE | Current Balance     : | app/bms/COACTVW.bms:154 |
| ACURBAL | 8 | 61 | 15 |  |  |  | app/bms/COACTVW.bms:159 |
|  | 8 | 77 | 0 |  |  |  | app/bms/COACTVW.bms:164 |
|  | 9 | 39 | 21 | (ASKIP,NORM) | TURQUOISE | Current Cycle Credit: | app/bms/COACTVW.bms:166 |
| ACRCYCR | 9 | 61 | 15 |  |  |  | app/bms/COACTVW.bms:171 |
|  | 9 | 77 | 0 |  |  |  | app/bms/COACTVW.bms:176 |
|  | 10 | 8 | 14 |  | TURQUOISE | Account Group: | app/bms/COACTVW.bms:178 |
| AADDGRP | 10 | 23 | 10 |  |  |  | app/bms/COACTVW.bms:182 |
|  | 10 | 34 | 0 |  |  |  | app/bms/COACTVW.bms:185 |
|  | 10 | 39 | 21 | (ASKIP,NORM) | TURQUOISE | Current Cycle Debit : | app/bms/COACTVW.bms:187 |
| ACRCYDB | 10 | 61 | 15 |  |  |  | app/bms/COACTVW.bms:192 |
|  | 10 | 77 | 0 |  |  |  | app/bms/COACTVW.bms:197 |
|  | 11 | 32 | 16 |  | NEUTRAL | Customer Details | app/bms/COACTVW.bms:199 |
|  | 12 | 8 | 14 |  | TURQUOISE | Customer id  : | app/bms/COACTVW.bms:203 |
| ACSTNUM | 12 | 23 | 9 |  |  |  | app/bms/COACTVW.bms:207 |
|  | 12 | 33 | 0 |  |  |  | app/bms/COACTVW.bms:210 |
|  | 12 | 49 | 4 |  | TURQUOISE | SSN: | app/bms/COACTVW.bms:212 |
| ACSTSSN | 12 | 54 | 12 |  |  |  | app/bms/COACTVW.bms:216 |
|  | 12 | 67 | 0 |  |  |  | app/bms/COACTVW.bms:219 |
|  | 13 | 8 | 14 |  | TURQUOISE | Date of birth: | app/bms/COACTVW.bms:221 |
| ACSTDOB | 13 | 23 | 10 |  |  |  | app/bms/COACTVW.bms:225 |
|  | 13 | 34 | 0 |  |  |  | app/bms/COACTVW.bms:228 |
|  | 13 | 49 | 11 |  | TURQUOISE | FICO Score: | app/bms/COACTVW.bms:230 |
| ACSTFCO | 13 | 61 | 3 |  |  |  | app/bms/COACTVW.bms:234 |
|  | 13 | 65 | 0 |  |  |  | app/bms/COACTVW.bms:237 |
|  | 14 | 1 | 10 |  | TURQUOISE | First Name | app/bms/COACTVW.bms:239 |
|  | 14 | 28 | 13 |  | TURQUOISE | Middle Name:  | app/bms/COACTVW.bms:243 |
|  | 14 | 55 | 12 |  | TURQUOISE | Last Name :  | app/bms/COACTVW.bms:247 |
| ACSFNAM | 15 | 1 | 25 |  |  |  | app/bms/COACTVW.bms:251 |
|  | 15 | 27 | 0 |  |  |  | app/bms/COACTVW.bms:254 |
| ACSMNAM | 15 | 28 | 25 |  |  |  | app/bms/COACTVW.bms:256 |
|  | 15 | 54 | 0 |  |  |  | app/bms/COACTVW.bms:259 |
| ACSLNAM | 15 | 55 | 25 |  |  |  | app/bms/COACTVW.bms:261 |
|  | 16 | 1 | 8 |  | TURQUOISE | Address: | app/bms/COACTVW.bms:264 |
| ACSADL1 | 16 | 10 | 50 |  |  |  | app/bms/COACTVW.bms:268 |
|  | 16 | 61 | 0 |  |  |  | app/bms/COACTVW.bms:271 |
|  | 16 | 63 | 6 |  | TURQUOISE | State  | app/bms/COACTVW.bms:273 |
| ACSSTTE | 16 | 73 | 2 |  |  |  | app/bms/COACTVW.bms:277 |
|  | 16 | 76 | 0 |  |  |  | app/bms/COACTVW.bms:280 |
| ACSADL2 | 17 | 10 | 50 |  |  |  | app/bms/COACTVW.bms:282 |
|  | 17 | 61 | 0 |  |  |  | app/bms/COACTVW.bms:285 |
|  | 17 | 63 | 3 |  | TURQUOISE | Zip | app/bms/COACTVW.bms:287 |
| ACSZIPC | 17 | 73 | 5 |  |  |  | app/bms/COACTVW.bms:291 |
|  | 17 | 79 | 0 |  |  |  | app/bms/COACTVW.bms:295 |
|  | 18 | 1 | 5 |  | TURQUOISE | City  | app/bms/COACTVW.bms:297 |
| ACSCITY | 18 | 10 | 50 |  |  |  | app/bms/COACTVW.bms:301 |
|  | 18 | 61 | 0 |  |  |  | app/bms/COACTVW.bms:304 |
|  | 18 | 63 | 7 |  | TURQUOISE | Country | app/bms/COACTVW.bms:306 |
| ACSCTRY | 18 | 73 | 3 |  |  |  | app/bms/COACTVW.bms:310 |
|  | 18 | 77 | 0 |  |  |  | app/bms/COACTVW.bms:313 |
|  | 19 | 1 | 8 |  | TURQUOISE | Phone 1: | app/bms/COACTVW.bms:315 |
| ACSPHN1 | 19 | 10 | 13 |  |  |  | app/bms/COACTVW.bms:319 |
|  | 19 | 24 | 30 |  | TURQUOISE | Government Issued Id Ref    :  | app/bms/COACTVW.bms:322 |
| ACSGOVT | 19 | 58 | 20 |  |  |  | app/bms/COACTVW.bms:326 |
|  | 19 | 79 | 0 |  |  |  | app/bms/COACTVW.bms:329 |
|  | 20 | 1 | 8 |  | TURQUOISE | Phone 2: | app/bms/COACTVW.bms:331 |
| ACSPHN2 | 20 | 10 | 13 |  |  |  | app/bms/COACTVW.bms:335 |
|  | 20 | 24 | 16 |  | TURQUOISE | EFT Account Id:  | app/bms/COACTVW.bms:338 |
| ACSEFTC | 20 | 41 | 10 |  |  |  | app/bms/COACTVW.bms:342 |
|  | 20 | 52 | 0 |  |  |  | app/bms/COACTVW.bms:345 |
|  | 20 | 53 | 24 |  | TURQUOISE | Primary Card Holder Y/N: | app/bms/COACTVW.bms:347 |
| ACSPFLG | 20 | 78 | 1 |  |  |  | app/bms/COACTVW.bms:351 |
|  | 20 | 80 | 0 |  |  |  | app/bms/COACTVW.bms:354 |
| INFOMSG | 22 | 23 | 45 | (PROT) | NEUTRAL |  | app/bms/COACTVW.bms:356 |
|  | 22 | 69 | 0 |  |  |  | app/bms/COACTVW.bms:361 |
|  | 1 | 1 | 9 |  |  |  | app/bms/COACTVW.bms:363 |
| ERRMSG | 23 | 1 | 78 | (ASKIP,BRT,FSET) | RED |  | app/bms/COACTVW.bms:365 |
|  | 24 | 1 | 60 | (ASKIP,NORM) | TURQUOISE |   F3=Exit  | app/bms/COACTVW.bms:369 |

## Function keys

| Key | Action | Target | Evidence |
|---|---|---|---|
|   |   |   |   |

## Validation and messages

Message literals for these programs are indexed in [Error handling](../../12-error-handling-messages.md).

## Behaviour

See the program specifications linked from the transaction catalog for first-time display and AID handling.

## Sources

- `app/bms/COACTVW.bms:20`
- `docs/_work/online/screens/COACTVW.json`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
