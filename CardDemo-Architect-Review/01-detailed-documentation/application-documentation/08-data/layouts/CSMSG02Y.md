# Layout CSMSG02Y

| Item | Value |
|---|---|
| Source | `app/cpy/CSMSG02Y.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 35 |
| Data items | 5 (88-levels: 0) |
| Semantic analysis | validated (batch B04) |

## Purpose

Defines ABEND-DATA, the work area for the common abend routine: abend code, culprit program, reason and message. COACTUPC fills it for an unexpected change-action state and in ABEND-ROUTINE sends it to the terminal before EXEC CICS ABEND ABCODE('9999'). It is also copied by other CardDemo online programs. (Confirmed)

Evidence: `app/cpy/CSMSG02Y.cpy:21-29`, `app/cbl/COACTUPC.cbl:2633-2640`, `app/cbl/COACTUPC.cbl:4203-4224`

## Record structure

Offsets come from `copybook_layout.py` (1-based, bytes); PIC/USAGE/OCCURS/REDEFINES/VALUE are parsed from the source.

| Lvl | Field | PIC | Usage | Start | End | Len | OCCURS | REDEFINES | VALUE | Line |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | ABEND-DATA |  |  | 1 | 134 | 134 |  |  |  | 21 |
| 05 | &nbsp;&nbsp;ABEND-CODE | X(4) | DISPLAY | 1 | 4 | 4 |  |  | SPACES | 22 |
| 05 | &nbsp;&nbsp;ABEND-CULPRIT | X(8) | DISPLAY | 5 | 12 | 8 |  |  | SPACES | 24 |
| 05 | &nbsp;&nbsp;ABEND-REASON | X(50) | DISPLAY | 13 | 62 | 50 |  |  | SPACES | 26 |
| 05 | &nbsp;&nbsp;ABEND-MSG | X(72) | DISPLAY | 63 | 134 | 72 |  |  | SPACES | 28 |

## Level-88 conditions

None.

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [COPAUS0C](../../07-programs/COPAUS0C.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl:141` |
| [COPAUS1C](../../07-programs/COPAUS1C.md) | cobol-program | COPY | active |  | `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl:135` |
| [COTRTUPC](../../07-programs/COTRTUPC.md) | cobol-program | COPY | active |  | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:274` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active |  | `app/cbl/COACTUPC.cbl:632` |
| [COACTVWC](../../07-programs/COACTVWC.md) | cobol-program | COPY | active |  | `app/cbl/COACTVWC.cbl:238` |
| [COCRDLIC](../../07-programs/COCRDLIC.md) | cobol-program | COPY | commented out |  | `app/cbl/COCRDLIC.cbl:283` |
| [COCRDSLC](../../07-programs/COCRDSLC.md) | cobol-program | COPY | active |  | `app/cbl/COCRDSLC.cbl:224` |
| [COCRDUPC](../../07-programs/COCRDUPC.md) | cobol-program | COPY | active |  | `app/cbl/COCRDUPC.cbl:343` |

## Field references by program

Programs that copy this member (directly or through another copybook) and name a field or 88-level in procedure code. Found by whole-word match outside comments and literals, including procedure copybooks those programs copy. A field used only through its parent group, through REDEFINES, or under a REPLACING alias is not counted here.

| Field | Line | Referenced by (count): first lines |
|---|---|---|
| ABEND-DATA | 21 | COACTUPC (2): `app/cbl/COACTUPC.cbl:4212`, `app/cbl/COACTUPC.cbl:4213`; COACTVWC (2): `app/cbl/COACTVWC.cbl:925`, `app/cbl/COACTVWC.cbl:926`; COCRDSLC (2): `app/cbl/COCRDSLC.cbl:866`, `app/cbl/COCRDSLC.cbl:867`; COCRDUPC (2): `app/cbl/COCRDUPC.cbl:1540`, `app/cbl/COCRDUPC.cbl:1541`; COTRTUPC (2): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1685`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1686` |
| ABEND-CODE | 22 | COACTUPC (1): `app/cbl/COACTUPC.cbl:2635`; COACTVWC (1): `app/cbl/COACTVWC.cbl:377`; COCRDSLC (1): `app/cbl/COCRDSLC.cbl:375`; COCRDUPC (1): `app/cbl/COCRDUPC.cbl:1021`; COTRTUPC (3): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1075`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1682`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1696` |
| ABEND-CULPRIT | 24 | COACTUPC (2): `app/cbl/COACTUPC.cbl:2634`, `app/cbl/COACTUPC.cbl:4209`; COACTVWC (2): `app/cbl/COACTVWC.cbl:376`, `app/cbl/COACTVWC.cbl:922`; COCRDSLC (2): `app/cbl/COCRDSLC.cbl:374`, `app/cbl/COCRDSLC.cbl:863`; COCRDUPC (2): `app/cbl/COCRDUPC.cbl:1020`, `app/cbl/COCRDUPC.cbl:1537`; COTRTUPC (2): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1074`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1681` |
| ABEND-REASON | 26 | COACTUPC (1): `app/cbl/COACTUPC.cbl:2636`; COACTVWC (1): `app/cbl/COACTVWC.cbl:378`; COCRDSLC (1): `app/cbl/COCRDSLC.cbl:376`; COCRDUPC (1): `app/cbl/COCRDUPC.cbl:1022`; COTRTUPC (1): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1076` |
| ABEND-MSG | 28 | COACTUPC (3): `app/cbl/COACTUPC.cbl:2638`, `app/cbl/COACTUPC.cbl:4205`, `app/cbl/COACTUPC.cbl:4206`; COACTVWC (2): `app/cbl/COACTVWC.cbl:918`, `app/cbl/COACTVWC.cbl:919`; COCRDSLC (2): `app/cbl/COCRDSLC.cbl:859`, `app/cbl/COCRDSLC.cbl:860`; COCRDUPC (3): `app/cbl/COCRDUPC.cbl:1024`, `app/cbl/COCRDUPC.cbl:1533`, `app/cbl/COCRDUPC.cbl:1534`; COTRTUPC (3): `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1078`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1677`, `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1678` |

## Key fields

| Field | Meaning | Source |
|---|---|---|
| ABEND-DATA | 134-byte block sent to the terminal by ABEND-ROUTINE before the task abends. | `app/cpy/CSMSG02Y.cpy:21` |
| ABEND-CODE | 4-character program abend code; COACTUPC sets '0001' for an unexpected state. | `app/cpy/CSMSG02Y.cpy:22-23` |
| ABEND-CULPRIT | Name of the program raising the abend (COACTUPC). | `app/cpy/CSMSG02Y.cpy:24-25` |
| ABEND-REASON | 50-byte reason text; set to spaces by COACTUPC. | `app/cpy/CSMSG02Y.cpy:26-27` |
| ABEND-MSG | 72-byte abend message, for example 'UNEXPECTED DATA SCENARIO'; defaulted to 'UNEXPECTED ABEND OCCURRED.' when empty. | `app/cpy/CSMSG02Y.cpy:28-29` |

## Observations

- conflict: The header comment names the member CABENDD.CPY, not CSMSG02Y; lines 1-4 and 21-29 carry sequence numbers while the licence block does not. (`app/cpy/CSMSG02Y.cpy:2`)

## Sources

- `app/cpy/CSMSG02Y.cpy`
- `docs/_work/structure/copybooks/CSMSG02Y.json`
- `docs/_work/layouts/CSMSG02Y.json`
- `docs/_work/semantic/copybooks/CSMSG02Y.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
