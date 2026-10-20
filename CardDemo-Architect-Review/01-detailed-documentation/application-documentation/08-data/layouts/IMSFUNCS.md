# Layout IMSFUNCS

| Item | Value |
|---|---|
| Source | `app/app-authorization-ims-db2-mq/cpy/IMSFUNCS.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 27 |
| Data items | 11 (88-levels: 0) |
| Semantic analysis | validated (batch B01) |

## Purpose

Defines FUNC-CODES, the 4-character DL/I function code literals (GU, GHU, GN, GHN, GNP, GHNP, REPL, ISRT, DLET) and a parameter count used as the first argument of CALL 'CBLTDLI'. It is copied by the batch IMS utilities PAUDBUNL, PAUDBLOD and DBUNLDGS, which use the call interface instead of EXEC DLI. (Confirmed)

Evidence: `app/app-authorization-ims-db2-mq/cpy/IMSFUNCS.cpy:17-27`, `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:212-216`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | FUNC-CODES |  |  | 1 | 40 | 40 |  |  |  | 17 |
| 05 | &nbsp;&nbsp;FUNC-GU | X(04) | DISPLAY | 1 | 4 | 4 |  |  | 'GU ' | 18 |
| 05 | &nbsp;&nbsp;FUNC-GHU | X(04) | DISPLAY | 5 | 8 | 4 |  |  | 'GHU ' | 19 |
| 05 | &nbsp;&nbsp;FUNC-GN | X(04) | DISPLAY | 9 | 12 | 4 |  |  | 'GN ' | 20 |
| 05 | &nbsp;&nbsp;FUNC-GHN | X(04) | DISPLAY | 13 | 16 | 4 |  |  | 'GHN ' | 21 |
| 05 | &nbsp;&nbsp;FUNC-GNP | X(04) | DISPLAY | 17 | 20 | 4 |  |  | 'GNP ' | 22 |
| 05 | &nbsp;&nbsp;FUNC-GHNP | X(04) | DISPLAY | 21 | 24 | 4 |  |  | 'GHNP' | 23 |
| 05 | &nbsp;&nbsp;FUNC-REPL | X(04) | DISPLAY | 25 | 28 | 4 |  |  | 'REPL' | 24 |
| 05 | &nbsp;&nbsp;FUNC-ISRT | X(04) | DISPLAY | 29 | 32 | 4 |  |  | 'ISRT' | 25 |
| 05 | &nbsp;&nbsp;FUNC-DLET | X(04) | DISPLAY | 33 | 36 | 4 |  |  | 'DLET' | 26 |
| 05 | &nbsp;&nbsp;PARMCOUNT | S9(05) | COMP-5 | 37 | 40 | 4 |  |  | +4 COMP-5 | 27 |

## Level-88 conditions

None.

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [DBUNLDGS](../../07-programs/DBUNLDGS.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:136` |
| [PAUDBLOD](../../07-programs/PAUDBLOD.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:142` |
| [PAUDBUNL](../../07-programs/PAUDBUNL.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:132` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| FUNC-GU | 18 | PAUDBLOD (1): `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:296` |
| FUNC-GN | 20 | DBUNLDGS (1): `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:222`; PAUDBUNL (1): `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:213` |
| FUNC-GNP | 22 | DBUNLDGS (1): `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:267`; PAUDBUNL (1): `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:257` |
| FUNC-ISRT | 25 | DBUNLDGS (2): `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:302`, `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:321`; PAUDBLOD (2): `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:244`, `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:321` |

Named in no procedure statement of the copying programs (may still be moved as part of a group): FUNC-CODES (line 17), FUNC-GHU (line 19), FUNC-GHN (line 21), FUNC-GHNP (line 23), FUNC-REPL (line 24), FUNC-DLET (line 26), PARMCOUNT (line 27).

## Key fields

| Field | Meaning | Source |
|---|---|---|
| FUNC-GN | 'GN  ' get next; used for sequential root reads. | `app/app-authorization-ims-db2-mq/cpy/IMSFUNCS.cpy:20` |
| FUNC-GNP | 'GNP ' get next within parent; used for child reads. | `app/app-authorization-ims-db2-mq/cpy/IMSFUNCS.cpy:22` |
| FUNC-GU | 'GU  ' get unique; used by PAUDBLOD to position on a root. | `app/app-authorization-ims-db2-mq/cpy/IMSFUNCS.cpy:18` |
| FUNC-ISRT | 'ISRT' insert; used for segment loads and GSAM writes. | `app/app-authorization-ims-db2-mq/cpy/IMSFUNCS.cpy:25` |

## Observations

- dead-code: FUNC-GHU, FUNC-GHN, FUNC-GHNP, FUNC-REPL, FUNC-DLET and PARMCOUNT are not used by any program that copies IMSFUNCS. (`app/app-authorization-ims-db2-mq/cpy/IMSFUNCS.cpy:19-27`)

## Sources

- `app/app-authorization-ims-db2-mq/cpy/IMSFUNCS.cpy`
- `docs/_work/structure/copybooks/IMSFUNCS.json`
- `docs/_work/layouts/IMSFUNCS.json`
- `docs/_work/semantic/copybooks/IMSFUNCS.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
