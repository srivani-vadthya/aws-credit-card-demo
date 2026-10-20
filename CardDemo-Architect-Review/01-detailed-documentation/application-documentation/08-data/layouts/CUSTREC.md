# Layout CUSTREC

| Item | Value |
|---|---|
| Source | `app/cpy/CUSTREC.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 26 |
| Data items | 20 (88-levels: 0) |
| Semantic analysis | validated (batch B02) |

## Purpose

CUSTREC defines CUSTOMER-RECORD, the 500-byte customer entity: id, names, three address lines, state/country/ZIP, two phone numbers, SSN, government id, date of birth, EFT account id, primary card holder indicator and FICO score. It is a variant of CVCUS01Y used only by the statement program CBSTM03A, which receives the customer record from CBSTM03B and prints name, address and FICO score on statements. (Confirmed)

Evidence: `app/cpy/CUSTREC.cpy:1-23`, `app/cbl/CBSTM03A.CBL:55`, `app/cbl/CBSTM03A.CBL:462-484`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | CUSTOMER-RECORD |  |  | 1 | 500 | 500 |  |  |  | 4 |
| 05 | &nbsp;&nbsp;CUST-ID | 9(09) | DISPLAY | 1 | 9 | 9 |  |  |  | 5 |
| 05 | &nbsp;&nbsp;CUST-FIRST-NAME | X(25) | DISPLAY | 10 | 34 | 25 |  |  |  | 6 |
| 05 | &nbsp;&nbsp;CUST-MIDDLE-NAME | X(25) | DISPLAY | 35 | 59 | 25 |  |  |  | 7 |
| 05 | &nbsp;&nbsp;CUST-LAST-NAME | X(25) | DISPLAY | 60 | 84 | 25 |  |  |  | 8 |
| 05 | &nbsp;&nbsp;CUST-ADDR-LINE-1 | X(50) | DISPLAY | 85 | 134 | 50 |  |  |  | 9 |
| 05 | &nbsp;&nbsp;CUST-ADDR-LINE-2 | X(50) | DISPLAY | 135 | 184 | 50 |  |  |  | 10 |
| 05 | &nbsp;&nbsp;CUST-ADDR-LINE-3 | X(50) | DISPLAY | 185 | 234 | 50 |  |  |  | 11 |
| 05 | &nbsp;&nbsp;CUST-ADDR-STATE-CD | X(02) | DISPLAY | 235 | 236 | 2 |  |  |  | 12 |
| 05 | &nbsp;&nbsp;CUST-ADDR-COUNTRY-CD | X(03) | DISPLAY | 237 | 239 | 3 |  |  |  | 13 |
| 05 | &nbsp;&nbsp;CUST-ADDR-ZIP | X(10) | DISPLAY | 240 | 249 | 10 |  |  |  | 14 |
| 05 | &nbsp;&nbsp;CUST-PHONE-NUM-1 | X(15) | DISPLAY | 250 | 264 | 15 |  |  |  | 15 |
| 05 | &nbsp;&nbsp;CUST-PHONE-NUM-2 | X(15) | DISPLAY | 265 | 279 | 15 |  |  |  | 16 |
| 05 | &nbsp;&nbsp;CUST-SSN | 9(09) | DISPLAY | 280 | 288 | 9 |  |  |  | 17 |
| 05 | &nbsp;&nbsp;CUST-GOVT-ISSUED-ID | X(20) | DISPLAY | 289 | 308 | 20 |  |  |  | 18 |
| 05 | &nbsp;&nbsp;CUST-DOB-YYYYMMDD | X(10) | DISPLAY | 309 | 318 | 10 |  |  |  | 19 |
| 05 | &nbsp;&nbsp;CUST-EFT-ACCOUNT-ID | X(10) | DISPLAY | 319 | 328 | 10 |  |  |  | 20 |
| 05 | &nbsp;&nbsp;CUST-PRI-CARD-HOLDER-IND | X(01) | DISPLAY | 329 | 329 | 1 |  |  |  | 21 |
| 05 | &nbsp;&nbsp;CUST-FICO-CREDIT-SCORE | 9(03) | DISPLAY | 330 | 332 | 3 |  |  |  | 22 |
| 05 | &nbsp;&nbsp;FILLER | X(168) | DISPLAY | 333 | 500 | 168 |  |  |  | 23 |

## Level-88 conditions

None.

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [CBSTM03A](../../07-programs/CBSTM03A.md) | cobol-program | COPY | active |  | `app/cbl/CBSTM03A.CBL:55` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| CUSTOMER-RECORD | 4 | CBSTM03A (1): `app/cbl/CBSTM03A.CBL:388` |
| CUST-FIRST-NAME | 6 | CBSTM03A (1): `app/cbl/CBSTM03A.CBL:462` |
| CUST-MIDDLE-NAME | 7 | CBSTM03A (1): `app/cbl/CBSTM03A.CBL:464` |
| CUST-LAST-NAME | 8 | CBSTM03A (1): `app/cbl/CBSTM03A.CBL:466` |
| CUST-ADDR-LINE-1 | 9 | CBSTM03A (1): `app/cbl/CBSTM03A.CBL:470` |
| CUST-ADDR-LINE-2 | 10 | CBSTM03A (1): `app/cbl/CBSTM03A.CBL:471` |
| CUST-ADDR-LINE-3 | 11 | CBSTM03A (1): `app/cbl/CBSTM03A.CBL:472` |
| CUST-ADDR-STATE-CD | 12 | CBSTM03A (1): `app/cbl/CBSTM03A.CBL:474` |
| CUST-ADDR-COUNTRY-CD | 13 | CBSTM03A (1): `app/cbl/CBSTM03A.CBL:476` |
| CUST-ADDR-ZIP | 14 | CBSTM03A (1): `app/cbl/CBSTM03A.CBL:478` |
| CUST-FICO-CREDIT-SCORE | 22 | CBSTM03A (1): `app/cbl/CBSTM03A.CBL:485` |

Named in no procedure statement of the copying programs (may still be moved as part of a group): CUST-ID (line 5), CUST-PHONE-NUM-1 (line 15), CUST-PHONE-NUM-2 (line 16), CUST-SSN (line 17), CUST-GOVT-ISSUED-ID (line 18), CUST-DOB-YYYYMMDD (line 19), CUST-EFT-ACCOUNT-ID (line 20), CUST-PRI-CARD-HOLDER-IND (line 21).

## Key fields

| Field | Meaning | Source |
|---|---|---|
| CUSTOMER-RECORD | 500-byte customer master record (header comment RECLN 500; field sizes add up to 500). | `app/cpy/CUSTREC.cpy:4` |
| CUST-ID | 9-digit customer identifier, key of the customer file. | `app/cpy/CUSTREC.cpy:5` |
| CUST-FIRST-NAME | Customer first name; with middle and last name forms the statement name line in CBSTM03A. | `app/cpy/CUSTREC.cpy:6` |
| CUST-ADDR-LINE-1 | First of three 50-byte address lines, followed by state, country and ZIP codes. | `app/cpy/CUSTREC.cpy:9-14` |
| CUST-SSN | 9-digit social security number (sensitive). | `app/cpy/CUSTREC.cpy:17` |
| CUST-DOB-YYYYMMDD | Date of birth, 10 bytes (name differs from CVCUS01Y's CUST-DOB-YYYY-MM-DD). | `app/cpy/CUSTREC.cpy:19` |
| CUST-FICO-CREDIT-SCORE | 3-digit FICO credit score, printed on statements. | `app/cpy/CUSTREC.cpy:22` |

## Observations

- anomaly: Lines 6-22 begin with tab characters instead of spaces, so the source is not aligned to standard fixed-format columns; compilers or tools that do not expand tabs may misread it. (`app/cpy/CUSTREC.cpy:6-22`)
- conflict: Near-duplicate of CVCUS01Y: same 500-byte layout, but the date-of-birth field is named CUST-DOB-YYYYMMDD here and CUST-DOB-YYYY-MM-DD in CVCUS01Y. (`app/cpy/CUSTREC.cpy:19`)

## Sources

- `app/cpy/CUSTREC.cpy`
- `docs/_work/structure/copybooks/CUSTREC.json`
- `docs/_work/layouts/CUSTREC.json`
- `docs/_work/semantic/copybooks/CUSTREC.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
