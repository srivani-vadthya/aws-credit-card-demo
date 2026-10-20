# Layout UNUSED1Y

| Item | Value |
|---|---|
| Source | `app/cpy/UNUSED1Y.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 10 |
| Data items | 7 (88-levels: 0) |
| Semantic analysis | validated (batch B10) |

## Purpose

Defines group UNUSED-DATA, an 80-byte record of six alphanumeric fields: id, first name, last name, password, type and filler. No program in the repository copies it, so it has no runtime role in this code base. The field shape mirrors a user record, but that is an observation from pictures and names, not from any usage. (Inferred)

Evidence: `app/cpy/UNUSED1Y.cpy:1-7`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | UNUSED-DATA |  |  | 1 | 80 | 80 |  |  |  | 1 |
| 05 | &nbsp;&nbsp;UNUSED-ID | X(08) | DISPLAY | 1 | 8 | 8 |  |  |  | 2 |
| 05 | &nbsp;&nbsp;UNUSED-FNAME | X(20) | DISPLAY | 9 | 28 | 20 |  |  |  | 3 |
| 05 | &nbsp;&nbsp;UNUSED-LNAME | X(20) | DISPLAY | 29 | 48 | 20 |  |  |  | 4 |
| 05 | &nbsp;&nbsp;UNUSED-PWD | X(08) | DISPLAY | 49 | 56 | 8 |  |  |  | 5 |
| 05 | &nbsp;&nbsp;UNUSED-TYPE | X(01) | DISPLAY | 57 | 57 | 1 |  |  |  | 6 |
| 05 | &nbsp;&nbsp;UNUSED-FILLER | X(23) | DISPLAY | 58 | 80 | 23 |  |  |  | 7 |

## Level-88 conditions

None.

## Used by

No program or copybook copies this member.

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

No COBOL program copies this member, so no field references exist.

## Key fields

| Field | Meaning | Source |
|---|---|---|
| UNUSED-ID | 8-byte identifier at the start of the 80-byte record; the same picture as the user id in CSUSR01Y (Inferred from matching PIC only). | `app/cpy/UNUSED1Y.cpy:2` |
| UNUSED-PWD | 8-byte password-like field (name only; no program reads it). | `app/cpy/UNUSED1Y.cpy:5` |
| UNUSED-TYPE | 1-byte type code (name only; no program reads it). | `app/cpy/UNUSED1Y.cpy:6` |

## Observations

- dead-code: No COPY or EXEC SQL INCLUDE of UNUSED1Y exists in any inventoried program or copybook (docs/_work/structure/copybook-usage.json). Its 8+20+20+8+1+23 = 80-byte shape matches the user-security layout in CSUSR01Y; whether it is a retired copy of that layout needs SME confirmation. (`app/cpy/UNUSED1Y.cpy:1`)

## Sources

- `app/cpy/UNUSED1Y.cpy`
- `docs/_work/structure/copybooks/UNUSED1Y.json`
- `docs/_work/layouts/UNUSED1Y.json`
- `docs/_work/semantic/copybooks/UNUSED1Y.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
