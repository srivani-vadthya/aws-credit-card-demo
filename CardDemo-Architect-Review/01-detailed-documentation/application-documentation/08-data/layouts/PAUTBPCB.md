# Layout PAUTBPCB

| Item | Value |
|---|---|
| Source | `app/app-authorization-ims-db2-mq/cpy/PAUTBPCB.CPY` |
| Type | cobol-copybook |
| Content | data |
| Lines | 26 |
| Data items | 10 (88-levels: 0) |
| Semantic analysis | validated (batch B01) |

## Purpose

Linkage-section DB PCB mask for the pending authorization database (DBPAUTP0, segments PAUTSUM0/PAUTDTL1). PAUDBUNL, PAUDBLOD and DBUNLDGS receive it through ENTRY 'DLITCBL' / PROCEDURE DIVISION USING and pass it to CBLTDLI calls; programs test PAUT-PCB-STATUS after each call and display PAUT-KEYFB on failure. (Confirmed)

Evidence: `app/app-authorization-ims-db2-mq/cpy/PAUTBPCB.CPY:17-26`, `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:150-158`, `app/app-authorization-ims-db2-mq/ims/PSBPAUTB.psb:17-20`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | PAUTBPCB |  |  | 1 | 291 | 291 |  |  |  | 17 |
| 05 | &nbsp;&nbsp;PAUT-DBDNAME | X(08) | DISPLAY | 1 | 8 | 8 |  |  |  | 18 |
| 05 | &nbsp;&nbsp;PAUT-SEG-LEVEL | X(02) | DISPLAY | 9 | 10 | 2 |  |  |  | 19 |
| 05 | &nbsp;&nbsp;PAUT-PCB-STATUS | X(02) | DISPLAY | 11 | 12 | 2 |  |  |  | 20 |
| 05 | &nbsp;&nbsp;PAUT-PCB-PROCOPT | X(04) | DISPLAY | 13 | 16 | 4 |  |  |  | 21 |
| 05 | &nbsp;&nbsp;FILLER | S9(05) | COMP | 17 | 20 | 4 |  |  |  | 22 |
| 05 | &nbsp;&nbsp;PAUT-SEG-NAME | X(08) | DISPLAY | 21 | 28 | 8 |  |  |  | 23 |
| 05 | &nbsp;&nbsp;PAUT-KEYFB-NAME | S9(05) | COMP | 29 | 32 | 4 |  |  |  | 24 |
| 05 | &nbsp;&nbsp;PAUT-NUM-SENSEGS | S9(05) | COMP | 33 | 36 | 4 |  |  |  | 25 |
| 05 | &nbsp;&nbsp;PAUT-KEYFB | X(255) | DISPLAY | 37 | 291 | 255 |  |  |  | 26 |

## Level-88 conditions

None.

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [DBUNLDGS](../../07-programs/DBUNLDGS.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:154` |
| [PAUDBLOD](../../07-programs/PAUDBLOD.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:161` |
| [PAUDBUNL](../../07-programs/PAUDBUNL.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:150` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| PAUTBPCB | 17 | DBUNLDGS (4): `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:159`, `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:165`, `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:223`, ...; PAUDBLOD (5): `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:165`, `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:171`, `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:245`, ...; PAUDBUNL (4): `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:153`, `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:158`, `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:214`, ... |
| PAUT-PCB-STATUS | 20 | DBUNLDGS (10): `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:221`, `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:232`, `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:249`, ...; PAUDBLOD (12): `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:253`, `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:256`, `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:259`, ...; PAUDBUNL (10): `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:212`, `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:223`, `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:239`, ... |
| PAUT-KEYFB | 26 | DBUNLDGS (2): `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:255`, `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:292`; PAUDBLOD (2): `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:312`, `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL:334`; PAUDBUNL (2): `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:245`, `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL:281` |

Named in no procedure statement of the copying programs (may still be moved as part of a group): PAUT-DBDNAME (line 18), PAUT-SEG-LEVEL (line 19), PAUT-PCB-PROCOPT (line 21), PAUT-SEG-NAME (line 23), PAUT-KEYFB-NAME (line 24), PAUT-NUM-SENSEGS (line 25).

## Key fields

| Field | Meaning | Source |
|---|---|---|
| PAUT-DBDNAME | DBD name of the PCB. | `app/app-authorization-ims-db2-mq/cpy/PAUTBPCB.CPY:18` |
| PAUT-PCB-STATUS | DL/I status code after each call (spaces OK, GB end of DB, GE not found, II duplicate). | `app/app-authorization-ims-db2-mq/cpy/PAUTBPCB.CPY:20` |
| PAUT-SEG-NAME | Name of the last segment accessed. | `app/app-authorization-ims-db2-mq/cpy/PAUTBPCB.CPY:23` |
| PAUT-KEYFB | Key feedback area (255 bytes) displayed in error diagnostics. | `app/app-authorization-ims-db2-mq/cpy/PAUTBPCB.CPY:26` |

## Sources

- `app/app-authorization-ims-db2-mq/cpy/PAUTBPCB.CPY`
- `docs/_work/structure/copybooks/PAUTBPCB.json`
- `docs/_work/layouts/PAUTBPCB.json`
- `docs/_work/semantic/copybooks/PAUTBPCB.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
