# Layout CSSTRPFY

| Item | Value |
|---|---|
| Source | `app/cpy/CSSTRPFY.cpy` |
| Type | cobol-copybook |
| Content | procedure |
| Lines | 85 |
| Data items | 0 (88-levels: 0) |
| Semantic analysis | validated (batch B04) |

## Purpose

Procedure-division copybook holding paragraph YYYY-STORE-PFKEY and its exit. It translates the CICS attention identifier EIBAID into CCARD-AID values, treating PF13-PF24 as PF1-PF12. COACTUPC copies it at the end of its procedure division and performs it in 0000-MAIN before deciding which keys are valid; the same copybook is used by the other card/account online programs. (Confirmed)

Evidence: `app/cpy/CSSTRPFY.cpy:17-82`, `app/cbl/COACTUPC.cbl:898-899`, `app/cbl/COACTUPC.cbl:4199-4200`

## Procedure paragraphs

This copybook contains procedure-division code copied into programs.

| Paragraph | Lines | Decisions | Calculations | Performs |
|---|---|---|---|---|
| YYYY-STORE-PFKEY | `app/cpy/CSSTRPFY.cpy:17-79` | 29 | 0 |  |
| YYYY-STORE-PFKEY-EXIT | `app/cpy/CSSTRPFY.cpy:80-82` | 0 | 0 |  |

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [COTRTLIC](../../07-programs/COTRTLIC.md) | cobol-program | COPY | active |  | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl:2060` |
| [COTRTUPC](../../07-programs/COTRTUPC.md) | cobol-program | COPY | active |  | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1671` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active |  | `app/cbl/COACTUPC.cbl:4199` |
| [COACTVWC](../../07-programs/COACTVWC.md) | cobol-program | COPY | active |  | `app/cbl/COACTVWC.cbl:913` |
| [COCRDLIC](../../07-programs/COCRDLIC.md) | cobol-program | COPY | active |  | `app/cbl/COCRDLIC.cbl:1416` |
| [COCRDSLC](../../07-programs/COCRDSLC.md) | cobol-program | COPY | active |  | `app/cbl/COCRDSLC.cbl:855` |
| [COCRDUPC](../../07-programs/COCRDUPC.md) | cobol-program | COPY | active |  | `app/cbl/COCRDUPC.cbl:1528` |

## Key fields

| Field | Meaning | Source |
|---|---|---|
| YYYY-STORE-PFKEY | Maps EIBAID to the CCARD-AID condition names of CVCRD01Y: Enter, Clear, PA1, PA2, PF1-PF12, and PF13-PF24 folded onto PF1-PF12. | `app/cpy/CSSTRPFY.cpy:17-79` |
| YYYY-STORE-PFKEY-EXIT | Exit paragraph closing the PERFORM ... THRU range. | `app/cpy/CSSTRPFY.cpy:80-82` |

## Observations

- anomaly: The EVALUATE has no WHEN OTHER: any other AID (for example a light-pen or Clear-partition key) leaves CCARD-AID unchanged from the INITIALIZE done by the caller (Inferred). (`app/cpy/CSSTRPFY.cpy:21-78`)

## Sources

- `app/cpy/CSSTRPFY.cpy`
- `docs/_work/structure/copybooks/CSSTRPFY.json`
- `docs/_work/layouts/CSSTRPFY.json`
- `docs/_work/semantic/copybooks/CSSTRPFY.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
