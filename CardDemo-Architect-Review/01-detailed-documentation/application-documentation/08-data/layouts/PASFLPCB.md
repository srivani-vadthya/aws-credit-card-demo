# Layout PASFLPCB

| Item | Value |
|---|---|
| Source | `app/app-authorization-ims-db2-mq/cpy/PASFLPCB.CPY` |
| Type | cobol-copybook |
| Content | data |
| Lines | 26 |
| Data items | 10 (88-levels: 0) |
| Semantic analysis | validated (batch B01) |

## Purpose

Linkage-section PCB mask for the GSAM dataset that receives pending authorization summary records (second PCB of PSB DLIGSAMP, DBD PASFLDBD). DBUNLDGS passes it to CBLTDLI ISRT to write each PAUTSUM0 summary and checks PASFL-PCB-STATUS. (Confirmed)

Evidence: `app/app-authorization-ims-db2-mq/cpy/PASFLPCB.CPY:17-26`, `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:300-315`, `app/app-authorization-ims-db2-mq/ims/DLIGSAMP.PSB:21`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | PASFLPCB |  |  | 1 | 136 | 136 |  |  |  | 17 |
| 05 | &nbsp;&nbsp;PASFL-DBDNAME | X(08) | DISPLAY | 1 | 8 | 8 |  |  |  | 18 |
| 05 | &nbsp;&nbsp;PASFL-SEG-LEVEL | X(02) | DISPLAY | 9 | 10 | 2 |  |  |  | 19 |
| 05 | &nbsp;&nbsp;PASFL-PCB-STATUS | X(02) | DISPLAY | 11 | 12 | 2 |  |  |  | 20 |
| 05 | &nbsp;&nbsp;PASFL-PCB-PROCOPT | X(04) | DISPLAY | 13 | 16 | 4 |  |  |  | 21 |
| 05 | &nbsp;&nbsp;FILLER | S9(05) | COMP | 17 | 20 | 4 |  |  |  | 22 |
| 05 | &nbsp;&nbsp;PASFL-SEG-NAME | X(08) | DISPLAY | 21 | 28 | 8 |  |  |  | 23 |
| 05 | &nbsp;&nbsp;PASFL-KEYFB-NAME | S9(05) | COMP | 29 | 32 | 4 |  |  |  | 24 |
| 05 | &nbsp;&nbsp;PASFL-NUM-SENSEGS | S9(05) | COMP | 33 | 36 | 4 |  |  |  | 25 |
| 05 | &nbsp;&nbsp;PASFL-KEYFB | X(100) | DISPLAY | 37 | 136 | 100 |  |  |  | 26 |

## Level-88 conditions

None.

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [DBUNLDGS](../../07-programs/DBUNLDGS.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:155` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| PASFLPCB | 17 | DBUNLDGS (3): `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:160`, `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:166`, `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:303` |
| PASFL-PCB-STATUS | 20 | DBUNLDGS (2): `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:311`, `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:312` |
| PASFL-KEYFB | 26 | DBUNLDGS (1): `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL:313` |

Named in no procedure statement of the copying programs (may still be moved as part of a group): PASFL-DBDNAME (line 18), PASFL-SEG-LEVEL (line 19), PASFL-PCB-PROCOPT (line 21), PASFL-SEG-NAME (line 23), PASFL-KEYFB-NAME (line 24), PASFL-NUM-SENSEGS (line 25).

## Key fields

| Field | Meaning | Source |
|---|---|---|
| PASFL-PCB-STATUS | GSAM status after ISRT; non-blank causes DBUNLDGS to abend. | `app/app-authorization-ims-db2-mq/cpy/PASFLPCB.CPY:20` |
| PASFL-KEYFB | Key feedback area (100 bytes) displayed on failure. | `app/app-authorization-ims-db2-mq/cpy/PASFLPCB.CPY:26` |

## Observations

- anomaly: PASFL-KEYFB is 100 bytes while the otherwise identical PADFLPCB and PAUTBPCB masks use 255 bytes. (`app/app-authorization-ims-db2-mq/cpy/PASFLPCB.CPY:26`)

## Sources

- `app/app-authorization-ims-db2-mq/cpy/PASFLPCB.CPY`
- `docs/_work/structure/copybooks/PASFLPCB.json`
- `docs/_work/layouts/PASFLPCB.json`
- `docs/_work/semantic/copybooks/PASFLPCB.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
