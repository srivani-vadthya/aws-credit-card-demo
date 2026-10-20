# Layout CSUTLDWY

| Item | Value |
|---|---|
| Source | `app/cpy/CSUTLDWY.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 89 |
| Data items | 38 (88-levels: 21) |
| Semantic analysis | validated (batch B04) |

## Purpose

Working-storage copybook (level-10 items, copied inside a caller's 05 group) that supports the CSUTLDPY date edit paragraphs: the CCYYMMDD date under edit with century/month/day 88-levels, per-part result flags, binary dates for the not-in-future check, and the parameter block for CALL 'CSUTLDTC'. COACTUPC copies it inside WS-MISC-STORAGE; COTRTUPC also copies it. (Confirmed)

Evidence: `app/cpy/CSUTLDWY.cpy:4-85`, `app/cbl/COACTUPC.cbl:166`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 10 | &nbsp;&nbsp;WS-EDIT-DATE-CCYYMMDD |  |  | 1 | 8 | 8 |  |  |  | 4 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-EDIT-DATE-CCYY |  |  | 1 | 4 | 4 |  |  |  | 5 |
| 25 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-EDIT-DATE-CC | X(2) | DISPLAY | 1 | 2 | 2 |  |  |  | 6 |
| 25 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-EDIT-DATE-CC-N | 9(2) | DISPLAY | 1 | 2 | 2 |  | WS-EDIT-DATE-CC |  | 7 |
| 25 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-EDIT-DATE-YY | X(2) | DISPLAY | 3 | 4 | 2 |  |  |  | 11 |
| 25 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WS-EDIT-DATE-YY-N | 9(2) | DISPLAY | 3 | 4 | 2 |  | WS-EDIT-DATE-YY |  | 12 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-EDIT-DATE-CCYY-N | 9(4) | DISPLAY | 1 | 4 | 4 |  | WS-EDIT-DATE-CCYY |  | 14 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-EDIT-DATE-MM | X(2) | DISPLAY | 5 | 6 | 2 |  |  |  | 16 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-EDIT-DATE-MM-N | 9(2) | DISPLAY | 5 | 6 | 2 |  | WS-EDIT-DATE-MM |  | 17 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-EDIT-DATE-DD | X(2) | DISPLAY | 7 | 8 | 2 |  |  |  | 25 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-EDIT-DATE-DD-N | 9(2) | DISPLAY | 7 | 8 | 2 |  | WS-EDIT-DATE-DD |  | 26 |
| 10 | &nbsp;&nbsp;WS-EDIT-DATE-CCYYMMDD-N | 9(8) | DISPLAY | 1 | 8 | 8 |  | WS-EDIT-DATE-CCYYMMDD |  | 35 |
| 10 | &nbsp;&nbsp;WS-EDIT-DATE-BINARY | S9(9) | BINARY | 9 | 12 | 4 |  |  |  | 37 |
| 10 | &nbsp;&nbsp;WS-CURRENT-DATE |  |  | 13 | 24 | 12 |  |  |  | 38 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-CURRENT-DATE-YYYYMMDD | X(8) | DISPLAY | 13 | 20 | 8 |  |  |  | 39 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-CURRENT-DATE-YYYYMMDD-N | 9(8) | DISPLAY | 13 | 20 | 8 |  | WS-CURRENT-DATE-YYYYMMDD |  | 40 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-CURRENT-DATE-BINARY | S9(9) | BINARY | 21 | 24 | 4 |  |  |  | 42 |
| 10 | &nbsp;&nbsp;WS-EDIT-DATE-FLGS |  |  | 25 | 27 | 3 |  |  |  | 43 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-EDIT-YEAR-FLG | X(01) | DISPLAY | 25 | 25 | 1 |  |  |  | 46 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-EDIT-MONTH | X(01) | DISPLAY | 26 | 26 | 1 |  |  |  | 50 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-EDIT-DAY | X(01) | DISPLAY | 27 | 27 | 1 |  |  |  | 54 |
| 10 | &nbsp;&nbsp;WS-DATE-FORMAT | X(08) | DISPLAY | 28 | 35 | 8 |  |  | 'YYYYMMDD' | 58 |
| 10 | &nbsp;&nbsp;WS-DATE-VALIDATION-RESULT |  |  | 36 | 115 | 80 |  |  |  | 60 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-SEVERITY | X(04) | DISPLAY | 36 | 39 | 4 |  |  |  | 61 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-SEVERITY-N | 9(4) | DISPLAY | 36 | 39 | 4 |  | WS-SEVERITY |  | 62 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(11) | DISPLAY | 40 | 50 | 11 |  |  | 'Mesg Code:' | 64 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-MSG-NO | X(04) | DISPLAY | 51 | 54 | 4 |  |  |  | 66 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-MSG-NO-N | 9(4) | DISPLAY | 51 | 54 | 4 |  | WS-MSG-NO |  | 67 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(01) | DISPLAY | 55 | 55 | 1 |  |  | SPACE | 69 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-RESULT | X(15) | DISPLAY | 56 | 70 | 15 |  |  |  | 71 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(01) | DISPLAY | 71 | 71 | 1 |  |  | SPACE | 72 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(09) | DISPLAY | 72 | 80 | 9 |  |  | 'TstDate:' | 74 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-DATE | X(10) | DISPLAY | 81 | 90 | 10 |  |  |  | 76 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(01) | DISPLAY | 91 | 91 | 1 |  |  | SPACE | 77 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(10) | DISPLAY | 92 | 101 | 10 |  |  | 'Mask used:' | 79 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;WS-DATE-FMT | X(10) | DISPLAY | 102 | 111 | 10 |  |  |  | 81 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(01) | DISPLAY | 112 | 112 | 1 |  |  | SPACE | 82 |
| 20 | &nbsp;&nbsp;&nbsp;&nbsp;FILLER | X(03) | DISPLAY | 113 | 115 | 3 |  |  | SPACES | 84 |

## Level-88 conditions

| Field | Condition | Values | Line |
|---|---|---|---|
| WS-EDIT-DATE-CC-N | THIS-CENTURY | 20 | 9 |
| WS-EDIT-DATE-CC-N | LAST-CENTURY | 19 | 10 |
| WS-EDIT-DATE-MM-N | WS-VALID-MONTH | 1 THROUGH 12 | 19 |
| WS-EDIT-DATE-MM-N | WS-31-DAY-MONTH | 1, 3, 5, 7, 8, 10, 12 | 21 |
| WS-EDIT-DATE-MM-N | WS-FEBRUARY | 2 | 24 |
| WS-EDIT-DATE-DD-N | WS-VALID-DAY | 1 THROUGH 31 | 28 |
| WS-EDIT-DATE-DD-N | WS-DAY-31 | 31 | 30 |
| WS-EDIT-DATE-DD-N | WS-DAY-30 | 30 | 31 |
| WS-EDIT-DATE-DD-N | WS-DAY-29 | 29 | 32 |
| WS-EDIT-DATE-DD-N | WS-VALID-FEB-DAY | 1 THROUGH 28 | 33 |
| WS-EDIT-DATE-FLGS | WS-EDIT-DATE-IS-VALID | LOW-VALUES | 44 |
| WS-EDIT-DATE-FLGS | WS-EDIT-DATE-IS-INVALID | '000' | 45 |
| WS-EDIT-YEAR-FLG | FLG-YEAR-ISVALID | LOW-VALUES | 47 |
| WS-EDIT-YEAR-FLG | FLG-YEAR-NOT-OK | '0' | 48 |
| WS-EDIT-YEAR-FLG | FLG-YEAR-BLANK | 'B' | 49 |
| WS-EDIT-MONTH | FLG-MONTH-ISVALID | LOW-VALUES | 51 |
| WS-EDIT-MONTH | FLG-MONTH-NOT-OK | '0' | 52 |
| WS-EDIT-MONTH | FLG-MONTH-BLANK | 'B' | 53 |
| WS-EDIT-DAY | FLG-DAY-ISVALID | LOW-VALUES | 55 |
| WS-EDIT-DAY | FLG-DAY-NOT-OK | '0' | 56 |
| WS-EDIT-DAY | FLG-DAY-BLANK | 'B' | 57 |

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [COTRTUPC](../../07-programs/COTRTUPC.md) | cobol-program | COPY | active |  | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:76` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active |  | `app/cbl/COACTUPC.cbl:166` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| WS-EDIT-DATE-CCYYMMDD | 4 | COACTUPC (5): `app/cbl/COACTUPC.cbl:1479`, `app/cbl/COACTUPC.cbl:1491`, `app/cbl/COACTUPC.cbl:1504`, ... |
| WS-EDIT-DATE-CCYY | 5 | COACTUPC (3): `app/cpy/CSUTLDPY.cpy:30`, `app/cpy/CSUTLDPY.cpy:31`, `app/cpy/CSUTLDPY.cpy:48` |
| THIS-CENTURY | 9 | COACTUPC (1): `app/cpy/CSUTLDPY.cpy:70` |
| LAST-CENTURY | 10 | COACTUPC (1): `app/cpy/CSUTLDPY.cpy:71` |
| WS-EDIT-DATE-YY-N | 12 | COACTUPC (1): `app/cpy/CSUTLDPY.cpy:245` |
| WS-EDIT-DATE-CCYY-N | 14 | COACTUPC (1): `app/cpy/CSUTLDPY.cpy:251` |
| WS-EDIT-DATE-MM | 16 | COACTUPC (4): `app/cpy/CSUTLDPY.cpy:94`, `app/cpy/CSUTLDPY.cpy:95`, `app/cpy/CSUTLDPY.cpy:126`, ... |
| WS-EDIT-DATE-MM-N | 17 | COACTUPC (1): `app/cpy/CSUTLDPY.cpy:127` |
| WS-VALID-MONTH | 19 | COACTUPC (1): `app/cpy/CSUTLDPY.cpy:111` |
| WS-31-DAY-MONTH | 21 | COACTUPC (1): `app/cpy/CSUTLDPY.cpy:213` |
| WS-FEBRUARY | 24 | COACTUPC (2): `app/cpy/CSUTLDPY.cpy:228`, `app/cpy/CSUTLDPY.cpy:243` |
| WS-EDIT-DATE-DD | 25 | COACTUPC (4): `app/cpy/CSUTLDPY.cpy:154`, `app/cpy/CSUTLDPY.cpy:155`, `app/cpy/CSUTLDPY.cpy:170`, ... |
| WS-EDIT-DATE-DD-N | 26 | COACTUPC (1): `app/cpy/CSUTLDPY.cpy:171` |
| WS-VALID-DAY | 28 | COACTUPC (1): `app/cpy/CSUTLDPY.cpy:187` |
| WS-DAY-31 | 30 | COACTUPC (1): `app/cpy/CSUTLDPY.cpy:214` |
| WS-DAY-30 | 31 | COACTUPC (1): `app/cpy/CSUTLDPY.cpy:229` |
| WS-DAY-29 | 32 | COACTUPC (1): `app/cpy/CSUTLDPY.cpy:244` |
| WS-EDIT-DATE-CCYYMMDD-N | 35 | COACTUPC (1): `app/cpy/CSUTLDPY.cpy:346` |
| WS-EDIT-DATE-BINARY | 37 | COACTUPC (2): `app/cpy/CSUTLDPY.cpy:345`, `app/cpy/CSUTLDPY.cpy:350` |
| WS-CURRENT-DATE-YYYYMMDD | 39 | COACTUPC (1): `app/cpy/CSUTLDPY.cpy:343` |
| WS-CURRENT-DATE-YYYYMMDD-N | 40 | COACTUPC (1): `app/cpy/CSUTLDPY.cpy:348` |
| WS-CURRENT-DATE-BINARY | 42 | COACTUPC (2): `app/cpy/CSUTLDPY.cpy:347`, `app/cpy/CSUTLDPY.cpy:350` |
| WS-EDIT-DATE-FLGS | 43 | COACTUPC (5): `app/cbl/COACTUPC.cbl:1482`, `app/cbl/COACTUPC.cbl:1494`, `app/cbl/COACTUPC.cbl:1507`, ... |
| WS-EDIT-DATE-IS-VALID | 44 | COACTUPC (2): `app/cpy/CSUTLDPY.cpy:274`, `app/cpy/CSUTLDPY.cpy:327` |
| WS-EDIT-DATE-IS-INVALID | 45 | COACTUPC (1): `app/cpy/CSUTLDPY.cpy:19` |
| FLG-YEAR-ISVALID | 47 | COACTUPC (1): `app/cpy/CSUTLDPY.cpy:86` |
| FLG-YEAR-NOT-OK | 48 | COACTUPC (6): `app/cpy/CSUTLDPY.cpy:27`, `app/cpy/CSUTLDPY.cpy:50`, `app/cpy/CSUTLDPY.cpy:75`, ... |
| FLG-YEAR-BLANK | 49 | COACTUPC (1): `app/cpy/CSUTLDPY.cpy:33` |
| FLG-MONTH-ISVALID | 51 | COACTUPC (1): `app/cpy/CSUTLDPY.cpy:143` |
| FLG-MONTH-NOT-OK | 52 | COACTUPC (8): `app/cpy/CSUTLDPY.cpy:92`, `app/cpy/CSUTLDPY.cpy:115`, `app/cpy/CSUTLDPY.cpy:132`, ... |
| FLG-MONTH-BLANK | 53 | COACTUPC (1): `app/cpy/CSUTLDPY.cpy:97` |
| FLG-DAY-ISVALID | 55 | COACTUPC (3): `app/cpy/CSUTLDPY.cpy:152`, `app/cpy/CSUTLDPY.cpy:203`, `app/cpy/CSUTLDPY.cpy:319` |
| FLG-DAY-NOT-OK | 56 | COACTUPC (7): `app/cpy/CSUTLDPY.cpy:176`, `app/cpy/CSUTLDPY.cpy:191`, `app/cpy/CSUTLDPY.cpy:216`, ... |
| FLG-DAY-BLANK | 57 | COACTUPC (1): `app/cpy/CSUTLDPY.cpy:157` |
| WS-DATE-FORMAT | 58 | COACTUPC (2): `app/cpy/CSUTLDPY.cpy:291`, `app/cpy/CSUTLDPY.cpy:295` |
| WS-DATE-VALIDATION-RESULT | 60 | COACTUPC (2): `app/cpy/CSUTLDPY.cpy:290`, `app/cpy/CSUTLDPY.cpy:296` |
| WS-SEVERITY | 61 | COACTUPC (1): `app/cpy/CSUTLDPY.cpy:309` |
| WS-SEVERITY-N | 62 | COACTUPC (1): `app/cpy/CSUTLDPY.cpy:298` |
| WS-MSG-NO | 66 | COACTUPC (1): `app/cpy/CSUTLDPY.cpy:311` |

Named in no procedure statement of the copying programs (may still be moved as part of a group): WS-EDIT-DATE-CC (line 6), WS-EDIT-DATE-CC-N (line 7), WS-EDIT-DATE-YY (line 11), WS-VALID-FEB-DAY (line 33), WS-CURRENT-DATE (line 38), WS-EDIT-YEAR-FLG (line 46), WS-EDIT-MONTH (line 50), WS-EDIT-DAY (line 54), WS-MSG-NO-N (line 67), WS-RESULT (line 71), WS-DATE (line 76), WS-DATE-FMT (line 81).

## Key fields

| Field | Meaning | Source |
|---|---|---|
| WS-EDIT-DATE-CCYYMMDD | Date under edit, split into century, year, month and day with numeric redefinitions; loaded by the caller before PERFORM EDIT-DATE-CCYYMMDD. | `app/cpy/CSUTLDWY.cpy:4-34` |
| THIS-CENTURY | Century 20 is accepted. | `app/cpy/CSUTLDWY.cpy:9` |
| LAST-CENTURY | Century 19 is accepted. | `app/cpy/CSUTLDWY.cpy:10` |
| WS-VALID-MONTH | Month 1 through 12. | `app/cpy/CSUTLDWY.cpy:19-20` |
| WS-31-DAY-MONTH | Months with 31 days: 1, 3, 5, 7, 8, 10, 12. | `app/cpy/CSUTLDWY.cpy:21-23` |
| WS-FEBRUARY | Month 2. | `app/cpy/CSUTLDWY.cpy:24` |
| WS-VALID-DAY | Day 1 through 31. | `app/cpy/CSUTLDWY.cpy:28-29` |
| WS-VALID-FEB-DAY | Day 1 through 28; defined but not tested by CSUTLDPY. | `app/cpy/CSUTLDWY.cpy:33-34` |
| WS-EDIT-DATE-FLGS | Year, month and day result flags (LOW-VALUES valid, '0' not ok, 'B' blank); group 88 WS-EDIT-DATE-IS-VALID / WS-EDIT-DATE-IS-INVALID. COACTUPC copies it into the per-date flag groups. | `app/cpy/CSUTLDWY.cpy:43-57` |
| WS-DATE-FORMAT | Format mask 'YYYYMMDD' passed to CSUTLDTC. | `app/cpy/CSUTLDWY.cpy:58-59` |
| WS-DATE-VALIDATION-RESULT | Result block returned by CALL 'CSUTLDTC': severity, message number, result text, tested date and mask. | `app/cpy/CSUTLDWY.cpy:60-85` |
| WS-CURRENT-DATE | Current date and its INTEGER-OF-DATE value used by the date-of-birth check. | `app/cpy/CSUTLDWY.cpy:38-42` |

## Observations

- hardcoded-value: Only centuries 19 and 20 are valid; years from 2100 onward are rejected. (`app/cpy/CSUTLDWY.cpy:9-10`)
- conflict: CSUTLDPY's header says the accompanying working storage is 'CSUTLDTR', but the working storage actually copied is CSUTLDWY. (`app/cpy/CSUTLDPY.cpy:5`)

## Sources

- `app/cpy/CSUTLDWY.cpy`
- `docs/_work/structure/copybooks/CSUTLDWY.json`
- `docs/_work/layouts/CSUTLDWY.json`
- `docs/_work/semantic/copybooks/CSUTLDWY.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
