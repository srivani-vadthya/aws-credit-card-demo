# Layout CSUTLDPY

| Item | Value |
|---|---|
| Source | `app/cpy/CSUTLDPY.cpy` |
| Type | cobol-copybook |
| Content | procedure |
| Lines | 375 |
| Data items | 0 (88-levels: 0) |
| Semantic analysis | validated (batch B04) |

## Purpose

Procedure-division copybook with reusable date edit paragraphs operating on the CSUTLDWY work fields and the caller's INPUT-ERROR, WS-RETURN-MSG and WS-EDIT-VARIABLE-NAME. PERFORM EDIT-DATE-CCYYMMDD THRU EDIT-DATE-CCYYMMDD-EXIT validates year (century 19/20), month, day, day/month combinations including leap years, and finally calls CSUTLDTC (LE date service); EDIT-DATE-OF-BIRTH rejects dates not before today. Only COACTUPC copies it, for open, expiry, reissue dates and date of birth. (Confirmed)

Evidence: `app/cpy/CSUTLDPY.cpy:18-372`, `app/cbl/COACTUPC.cbl:1478-1543`, `app/cbl/COACTUPC.cbl:4232`

## Procedure paragraphs

This copybook contains procedure-division code copied into programs.

| Paragraph | Lines | Decisions | Calculations | Performs |
|---|---|---|---|---|
| EDIT-DATE-CCYYMMDD | `app/cpy/CSUTLDPY.cpy:18-20` | 0 | 0 |  |
| EDIT-YEAR-CCYY | `app/cpy/CSUTLDPY.cpy:25-87` | 6 | 0 |  |
| EDIT-YEAR-CCYY-EXIT | `app/cpy/CSUTLDPY.cpy:88-90` | 0 | 0 |  |
| EDIT-MONTH | `app/cpy/CSUTLDPY.cpy:91-144` | 6 | 1 |  |
| EDIT-MONTH-EXIT | `app/cpy/CSUTLDPY.cpy:145-147` | 0 | 0 |  |
| EDIT-DAY | `app/cpy/CSUTLDPY.cpy:150-204` | 6 | 1 |  |
| EDIT-DAY-EXIT | `app/cpy/CSUTLDPY.cpy:205-207` | 0 | 0 |  |
| EDIT-DAY-MONTH-YEAR | `app/cpy/CSUTLDPY.cpy:209-279` | 9 | 1 |  |
| EDIT-DAY-MONTH-YEAR-EXIT | `app/cpy/CSUTLDPY.cpy:280-282` | 0 | 0 |  |
| EDIT-DATE-LE | `app/cpy/CSUTLDPY.cpy:284-321` | 3 | 0 |  |
| EDIT-DATE-LE-EXIT | `app/cpy/CSUTLDPY.cpy:323-328` | 0 | 0 |  |
| EDIT-DATE-CCYYMMDD-EXIT | `app/cpy/CSUTLDPY.cpy:329-331` | 0 | 0 |  |
| EDIT-DATE-OF-BIRTH | `app/cpy/CSUTLDPY.cpy:341-369` | 2 | 2 |  |
| EDIT-DATE-OF-BIRTH-EXIT | `app/cpy/CSUTLDPY.cpy:370-372` | 0 | 0 |  |

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active |  | `app/cbl/COACTUPC.cbl:4232` |

## Key fields

| Field | Meaning | Source |
|---|---|---|
| EDIT-DATE-CCYYMMDD | Entry point: marks the date invalid and falls through the year, month, day, combination and LE paragraphs; callers PERFORM it THRU EDIT-DATE-CCYYMMDD-EXIT. | `app/cpy/CSUTLDPY.cpy:18-20` |
| EDIT-YEAR-CCYY | Year required, numeric, century 19 or 20. | `app/cpy/CSUTLDPY.cpy:25-87` |
| EDIT-MONTH | Month required and 1-12. | `app/cpy/CSUTLDPY.cpy:91-144` |
| EDIT-DAY | Day required, numeric and 1-31. | `app/cpy/CSUTLDPY.cpy:150-204` |
| EDIT-DAY-MONTH-YEAR | Rejects day 31 in short months, day 30 in February and day 29 in February outside leap years (YY=00 divisible by 400, else by 4); skips LE validation unless all three parts are valid. | `app/cpy/CSUTLDPY.cpy:209-279` |
| EDIT-DATE-LE | Calls CSUTLDTC with format YYYYMMDD; non-zero severity is an input error. | `app/cpy/CSUTLDPY.cpy:284-321` |
| EDIT-DATE-LE-EXIT | Exit label that also contains SET WS-EDIT-DATE-IS-VALID TO TRUE. | `app/cpy/CSUTLDPY.cpy:323-328` |
| EDIT-DATE-CCYYMMDD-EXIT | End of the full date edit range. | `app/cpy/CSUTLDPY.cpy:329-331` |
| EDIT-DATE-OF-BIRTH | Separately performed check that the date is strictly before today (INTEGER-OF-DATE comparison). | `app/cpy/CSUTLDPY.cpy:341-369` |

## Observations

- anomaly: On CSUTLDTC failure, GO TO EDIT-DATE-LE-EXIT falls into SET WS-EDIT-DATE-IS-VALID TO TRUE, resetting the part flags to valid although INPUT-ERROR remains set. (`app/cpy/CSUTLDPY.cpy:315-328`)
- anomaly: Each part edit's GO TO targets only its own exit paragraph (comment: 'Intentional violation of structured programming norms'), so a failing year still runs the month and day edits; only the first message is kept because of the WS-RETURN-MSG-OFF guard. (`app/cpy/CSUTLDPY.cpy:41-42`)
- anomaly: EDIT-MONTH tests WS-VALID-MONTH on the numeric redefinition before checking TEST-NUMVAL, so non-numeric month text is evaluated against a numeric 88-level first (Inferred). (`app/cpy/CSUTLDPY.cpy:111-126`)
- conflict: Header refers to working storage 'CSUTLDTR'; the actual companion copybook is CSUTLDWY. (`app/cpy/CSUTLDPY.cpy:5`)
- hardcoded-value: Date format mask 'YYYYMMDD' is fixed for the CSUTLDTC call. (`app/cpy/CSUTLDPY.cpy:291`)

## Sources

- `app/cpy/CSUTLDPY.cpy`
- `docs/_work/structure/copybooks/CSUTLDPY.json`
- `docs/_work/layouts/CSUTLDPY.json`
- `docs/_work/semantic/copybooks/CSUTLDPY.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
