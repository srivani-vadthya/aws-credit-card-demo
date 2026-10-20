# Layout CODATECN

| Item | Value |
|---|---|
| Source | `app/cpy/CODATECN.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 52 |
| Data items | 32 (88-levels: 4) |
| Semantic analysis | validated (batch B02) |

## Purpose

CODATECN defines the parameter record for the date-format conversion routine COBDATFT (assembler, app/asm/COBDATFT.asm). The caller sets an input format code and a 20-byte input date, an output format code, and receives the converted date and an error message. In this repository it is copied only by CBACT01C, which converts the account reissue date with input type '2' and output type '2'. (Confirmed)

Evidence: `app/cpy/CODATECN.cpy:17-52`, `app/cbl/CBACT01C.cbl:223-233`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | CODATECN-REC |  |  | 1 | 80 | 80 |  |  |  | 17 |
| 05 | &nbsp;&nbsp;CODATECN-IN-REC |  |  | 1 | 21 | 21 |  |  |  | 18 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CODATECN-TYPE | X | DISPLAY | 1 | 1 | 1 |  |  |  | 19 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CODATECN-INP-DATE | X(20) | DISPLAY | 2 | 21 | 20 |  |  |  | 22 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1INP |  |  | 2 | 21 | 20 |  | CODATECN-INP-DATE |  | 23 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1YYYY | XXXX | DISPLAY | 2 | 5 | 4 |  |  |  | 24 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1MM | XX | DISPLAY | 6 | 7 | 2 |  |  |  | 25 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1DD | XX | DISPLAY | 8 | 9 | 2 |  |  |  | 26 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1FIL | X(12) | DISPLAY | 10 | 21 | 12 |  |  |  | 27 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CODATECN-2INP |  |  | 2 | 21 | 20 |  | CODATECN-INP-DATE |  | 28 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1O-YYYY | XXXX | DISPLAY | 2 | 5 | 4 |  |  |  | 29 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1I-S1 | X | DISPLAY | 6 | 6 | 1 |  |  |  | 30 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1MM | XX | DISPLAY | 7 | 8 | 2 |  |  |  | 31 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1I-S2 | X | DISPLAY | 9 | 9 | 1 |  |  |  | 32 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-2YY | XX | DISPLAY | 10 | 11 | 2 |  |  |  | 33 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-2FIL | X(10) | DISPLAY | 12 | 21 | 10 |  |  |  | 34 |
| 05 | &nbsp;&nbsp;CODATECN-OUT-REC |  |  | 22 | 42 | 21 |  |  |  | 35 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CODATECN-OUTTYPE | X | DISPLAY | 22 | 22 | 1 |  |  |  | 36 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CODATECN-0UT-DATE | X(20) | DISPLAY | 23 | 42 | 20 |  |  |  | 39 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1OUT |  |  | 23 | 42 | 20 |  | CODATECN-0UT-DATE |  | 40 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1O-YYYY | XXXX | DISPLAY | 23 | 26 | 4 |  |  |  | 41 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1O-S1 | X | DISPLAY | 27 | 27 | 1 |  |  |  | 42 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1O-MM | XX | DISPLAY | 28 | 29 | 2 |  |  |  | 43 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1O-S2 | X | DISPLAY | 30 | 30 | 1 |  |  |  | 44 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1O-DD | XX | DISPLAY | 31 | 32 | 2 |  |  |  | 45 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-1OFIL | X(10) | DISPLAY | 33 | 42 | 10 |  |  |  | 46 |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;CODATECN-2OUT |  |  | 23 | 42 | 20 |  | CODATECN-0UT-DATE |  | 47 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-2O-YYYY | XXXX | DISPLAY | 23 | 26 | 4 |  |  |  | 48 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-2O-MM | XX | DISPLAY | 27 | 28 | 2 |  |  |  | 49 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-2O-DD | XX | DISPLAY | 29 | 30 | 2 |  |  |  | 50 |
| 15 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CODATECN-2OFIL | X(12) | DISPLAY | 31 | 42 | 12 |  |  |  | 51 |
| 05 | &nbsp;&nbsp;CODATECN-ERROR-MSG | X(38) | DISPLAY | 43 | 80 | 38 |  |  |  | 52 |

## Level-88 conditions

| Field | Condition | Values | Line |
|---|---|---|---|
| CODATECN-TYPE | YYYYMMDD-IN | "1" | 20 |
| CODATECN-TYPE | YYYY-MM-DD-IN | "2" | 21 |
| CODATECN-OUTTYPE | YYYY-MM-DD-OP | "1" | 37 |
| CODATECN-OUTTYPE | YYYYMMDD-OP | "2" | 38 |

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [CBACT01C](../../07-programs/CBACT01C.md) | cobol-program | COPY | active |  | `app/cbl/CBACT01C.cbl:90` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| CODATECN-REC | 17 | CBACT01C (1): `app/cbl/CBACT01C.cbl:231` |
| CODATECN-TYPE | 19 | CBACT01C (1): `app/cbl/CBACT01C.cbl:225` |
| CODATECN-INP-DATE | 22 | CBACT01C (1): `app/cbl/CBACT01C.cbl:223` |
| CODATECN-OUTTYPE | 36 | CBACT01C (1): `app/cbl/CBACT01C.cbl:226` |
| CODATECN-0UT-DATE | 39 | CBACT01C (1): `app/cbl/CBACT01C.cbl:233` |

Named in no procedure statement of the copying programs (may still be moved as part of a group): CODATECN-IN-REC (line 18), YYYYMMDD-IN (line 20), YYYY-MM-DD-IN (line 21), CODATECN-1INP (line 23), CODATECN-1YYYY (line 24), CODATECN-1MM (line 25), CODATECN-1DD (line 26), CODATECN-1FIL (line 27), CODATECN-2INP (line 28), CODATECN-1O-YYYY (line 29), CODATECN-1I-S1 (line 30), CODATECN-1MM (line 31), CODATECN-1I-S2 (line 32), CODATECN-2YY (line 33), CODATECN-2FIL (line 34), CODATECN-OUT-REC (line 35), YYYY-MM-DD-OP (line 37), YYYYMMDD-OP (line 38), CODATECN-1OUT (line 40), CODATECN-1O-YYYY (line 41), CODATECN-1O-S1 (line 42), CODATECN-1O-MM (line 43), CODATECN-1O-S2 (line 44), CODATECN-1O-DD (line 45), CODATECN-1OFIL (line 46), CODATECN-2OUT (line 47), CODATECN-2O-YYYY (line 48), CODATECN-2O-MM (line 49), CODATECN-2O-DD (line 50), CODATECN-2OFIL (line 51), CODATECN-ERROR-MSG (line 52).

## Key fields

| Field | Meaning | Source |
|---|---|---|
| CODATECN-REC | Parameter block passed to the date-conversion routine COBDATFT (CALL 'COBDATFT' USING CODATECN-REC in CBACT01C). | `app/cpy/CODATECN.cpy:17` |
| CODATECN-TYPE | Input date format code: '1' = YYYYMMDD (88 YYYYMMDD-IN), '2' = YYYY-MM-DD (88 YYYY-MM-DD-IN). | `app/cpy/CODATECN.cpy:19-21` |
| CODATECN-INP-DATE | 20-byte input date, redefined as YYYYMMDD (CODATECN-1INP) or YYYY-sep-MM-sep-xx (CODATECN-2INP). | `app/cpy/CODATECN.cpy:22-34` |
| CODATECN-OUTTYPE | Requested output format: '1' = YYYY-MM-DD (88 YYYY-MM-DD-OP), '2' = YYYYMMDD (88 YYYYMMDD-OP). Note the codes are reversed relative to CODATECN-TYPE. | `app/cpy/CODATECN.cpy:36-38` |
| CODATECN-0UT-DATE | 20-byte converted date returned by the routine (name uses digit zero '0UT'), redefined as YYYY-MM-DD (CODATECN-1OUT) or YYYYMMDD (CODATECN-2OUT). | `app/cpy/CODATECN.cpy:39-51` |
| CODATECN-ERROR-MSG | 38-byte error message area returned by the conversion routine. | `app/cpy/CODATECN.cpy:52` |

## Observations

- anomaly: Data names are duplicated inside the record: CODATECN-1MM appears in both CODATECN-1INP and CODATECN-2INP, and CODATECN-1O-YYYY appears in both CODATECN-2INP and CODATECN-1OUT; references need qualification. The day field of the dashed input layout is named CODATECN-2YY. (`app/cpy/CODATECN.cpy:24-41`)
- anomaly: The output date field is spelled CODATECN-0UT-DATE (zero instead of letter O), and the input/output type codes are inverted ('1' means YYYYMMDD for input but YYYY-MM-DD for output). (`app/cpy/CODATECN.cpy:36-39`)

## Sources

- `app/cpy/CODATECN.cpy`
- `docs/_work/structure/copybooks/CODATECN.json`
- `docs/_work/layouts/CODATECN.json`
- `docs/_work/semantic/copybooks/CODATECN.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
