# Layout CSLKPCDY

| Item | Value |
|---|---|
| Source | `app/cpy/CSLKPCDY.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 1318 |
| Data items | 5 (88-levels: 5) |
| Semantic analysis | validated (batch B04) |

## Purpose

Lookup-table copybook of three 01-level edit fields whose 88-level VALUE lists hold reference data: North American telephone area codes (all, general purpose, and easily recognizable), US state and territory codes, and valid state + first-two-zip-digit combinations. A program moves a value into the edit field and tests the 88-level. Only COACTUPC copies it, using VALID-GENERAL-PURP-CODE for phone area codes, VALID-US-STATE-CODE for the customer state and VALID-US-STATE-ZIP-CD2-COMBO for the state/zip cross edit. (Confirmed)

Evidence: `app/cpy/CSLKPCDY.cpy:1-7`, `app/cpy/CSLKPCDY.cpy:24-30`, `app/cpy/CSLKPCDY.cpy:521-521`, `app/cpy/CSLKPCDY.cpy:931-931`, `app/cpy/CSLKPCDY.cpy:1012-1014`, `app/cpy/CSLKPCDY.cpy:1071-1074`, `app/cpy/CSLKPCDY.cpy:1313-1314`, `app/cbl/COACTUPC.cbl:2295-2298`, `app/cbl/COACTUPC.cbl:2493-2495`, `app/cbl/COACTUPC.cbl:2537-2542`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | WS-US-PHONE-AREA-CODE-TO-EDIT | XXX | DISPLAY | 1 | 3 | 3 |  |  |  | 24 |
| 01 | US-STATE-CODE-TO-EDIT | X(2) | DISPLAY | 1 | 2 | 2 |  |  |  | 1012 |
| 01 | US-STATE-ZIPCODE-TO-EDIT |  |  | 1 | 7 | 7 |  |  |  | 1071 |
| 02 | &nbsp;&nbsp;US-STATE-AND-FIRST-ZIP2 | X(4) | DISPLAY | 1 | 4 | 4 |  |  |  | 1072 |
| 02 | &nbsp;&nbsp;LAST-3-OF-ZIP | X(3) | DISPLAY | 5 | 7 | 3 |  |  |  | 1314 |

## Level-88 conditions

| Field | Condition | Values | Line |
|---|---|---|---|
| WS-US-PHONE-AREA-CODE-TO-EDIT | VALID-PHONE-AREA-CODE | '201', '202', '203', '204', '205', '206', '207', '208', '209', '210', '212', '213', '214', '215', '216', '217', '218', '219', '220', '223', '224', '225', '226', '228', '229', '231', '234', '236', '239 | 30 |
| WS-US-PHONE-AREA-CODE-TO-EDIT | VALID-GENERAL-PURP-CODE | '201', '202', '203', '204', '205', '206', '207', '208', '209', '210', '212', '213', '214', '215', '216', '217', '218', '219', '220', '223', '224', '225', '226', '228', '229', '231', '234', '236', '239 | 521 |
| WS-US-PHONE-AREA-CODE-TO-EDIT | VALID-EASY-RECOG-AREA-CODE | '200', '211', '222', '233', '244', '255', '266', '277', '288', '299', '300', '311', '322', '333', '344', '355', '366', '377', '388', '399', '400', '411', '422', '433', '444', '455', '466', '477', '488 | 931 |
| US-STATE-CODE-TO-EDIT | VALID-US-STATE-CODE | 'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'N | 1013 |
| US-STATE-AND-FIRST-ZIP2 | VALID-US-STATE-ZIP-CD2-COMBO | 'AA34', 'AE90', 'AE91', 'AE92', 'AE93', 'AE94', 'AE95', 'AE96', 'AE97', 'AE98', 'AK99', 'AL35', 'AL36', 'AP96', 'AR71', 'AR72', 'AS96', 'AZ85', 'AZ86', 'CA90', 'CA91', 'CA92', 'CA93', 'CA94', 'CA95', | 1073 |

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active |  | `app/cbl/COACTUPC.cbl:602` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| WS-US-PHONE-AREA-CODE-TO-EDIT | 24 | COACTUPC (1): `app/cbl/COACTUPC.cbl:2297` |
| VALID-GENERAL-PURP-CODE | 521 | COACTUPC (1): `app/cbl/COACTUPC.cbl:2298` |
| US-STATE-CODE-TO-EDIT | 1012 | COACTUPC (1): `app/cbl/COACTUPC.cbl:2494` |
| VALID-US-STATE-CODE | 1013 | COACTUPC (1): `app/cbl/COACTUPC.cbl:2495` |
| US-STATE-AND-FIRST-ZIP2 | 1072 | COACTUPC (1): `app/cbl/COACTUPC.cbl:2540` |
| VALID-US-STATE-ZIP-CD2-COMBO | 1073 | COACTUPC (1): `app/cbl/COACTUPC.cbl:2542` |

Named in no procedure statement of the copying programs (may still be moved as part of a group): VALID-PHONE-AREA-CODE (line 30), VALID-EASY-RECOG-AREA-CODE (line 931), US-STATE-ZIPCODE-TO-EDIT (line 1071), LAST-3-OF-ZIP (line 1314).

## Key fields

| Field | Meaning | Source |
|---|---|---|
| WS-US-PHONE-AREA-CODE-TO-EDIT | 3-character area code to look up; carries the three area-code 88-level lists. | `app/cpy/CSLKPCDY.cpy:24` |
| VALID-PHONE-AREA-CODE | All North American area codes in the list (general purpose plus easily recognizable codes), 490 values from the NANPA report cited in the comment; not used by COACTUPC. | `app/cpy/CSLKPCDY.cpy:30-520` |
| VALID-GENERAL-PURP-CODE | 410 general-purpose area codes; the list COACTUPC checks for phone numbers. | `app/cpy/CSLKPCDY.cpy:521-930` |
| VALID-EASY-RECOG-AREA-CODE | 80 easily recognizable codes (repeating-digit patterns such as 200, 211, 222 ... 999); not used by COACTUPC. | `app/cpy/CSLKPCDY.cpy:931-1010` |
| US-STATE-CODE-TO-EDIT | 2-character state code to look up. | `app/cpy/CSLKPCDY.cpy:1012` |
| VALID-US-STATE-CODE | 56 upper-case codes: the 50 states, DC, and territories AS, GU, MP, PR, VI. | `app/cpy/CSLKPCDY.cpy:1013-1069` |
| US-STATE-AND-FIRST-ZIP2 | State code followed by the first two zip digits. | `app/cpy/CSLKPCDY.cpy:1072` |
| VALID-US-STATE-ZIP-CD2-COMBO | 240 valid state + zip-prefix combinations (for example 'AK99', 'WY83'), including military codes AA and AE. | `app/cpy/CSLKPCDY.cpy:1073-1313` |
| LAST-3-OF-ZIP | Remaining 3 zip characters; not referenced by COACTUPC. | `app/cpy/CSLKPCDY.cpy:1314` |

## Observations

- anomaly: Combinations for military codes AA and AE (and others outside the state list) can never match in COACTUPC, because the state must first pass VALID-US-STATE-CODE, which does not contain AA or AE (Inferred). (`app/cpy/CSLKPCDY.cpy:1074-1083`)
- hardcoded-value: Area-code lists are static literals taken from the NANPA report (https://nationalnanpa.com/nanp1/npa_report.csv per the comment); new area codes need a source change and recompile of every program copying the member. (`app/cpy/CSLKPCDY.cpy:25-29`)
- anomaly: The comment 'Search list of valid Phone area codes' sits above the state code list, not the area-code lists. (`app/cpy/CSLKPCDY.cpy:1011`)
- anomaly: Value lines are indented with tab characters rather than fixed-column spaces. (`app/cpy/CSLKPCDY.cpy:31-40`)

## Sources

- `app/cpy/CSLKPCDY.cpy`
- `docs/_work/structure/copybooks/CSLKPCDY.json`
- `docs/_work/layouts/CSLKPCDY.json`
- `docs/_work/semantic/copybooks/CSLKPCDY.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
