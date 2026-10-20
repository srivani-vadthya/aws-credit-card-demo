# Layout CSSETATY

| Item | Value |
|---|---|
| Source | `app/cpy/CSSETATY.cpy` |
| Type | cobol-copybook |
| Content | data |
| Lines | 30 |
| Data items | 0 (88-levels: 0) |
| Semantic analysis | validated (batch B04) |

## Purpose

Procedure-division fragment (no data items) used with COPY ... REPLACING to set the screen attribute of one field. With (TESTVAR1), (SCRNVAR2) and (MAPNAME3) replaced, it colours the field red when FLG-<field>-NOT-OK or FLG-<field>-BLANK is set on a re-entry and also shows '*' in the field when it was blank. COACTUPC copies it 39 times in 3300-SETUP-SCREEN-ATTRS, once per editable field; COTRTUPC also uses it. (Confirmed)

Evidence: `app/cpy/CSSETATY.cpy:17-27`, `app/cbl/COACTUPC.cbl:3208-3435`

## Used by

| Used by | Type | Statement | State | REPLACING | Line |
|---|---|---|---|---|---|
| [COTRTUPC](../../07-programs/COTRTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==DESCRIPTION== ==(SCRNVAR2)== BY ==TRTYDSC== ==(MAPNAME3)== BY ==CTRTUPA== | `app/app-transaction-type-db2/cbl/COTRTUPC.cbl:1358-1361` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==ACCT-STATUS== ==(SCRNVAR2)== BY ==ACSTTUS== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3208-3211` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==OPEN-YEAR== ==(SCRNVAR2)== BY ==OPNYEAR== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3214-3217` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==OPEN-MONTH== ==(SCRNVAR2)== BY ==OPNMON== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3220-3223` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==OPEN-DAY== ==(SCRNVAR2)== BY ==OPNDAY== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3226-3229` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==CRED-LIMIT== ==(SCRNVAR2)== BY ==ACRDLIM== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3232-3235` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==EXPIRY-YEAR== ==(SCRNVAR2)== BY ==EXPYEAR== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3238-3241` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==EXPIRY-MONTH== ==(SCRNVAR2)== BY ==EXPMON== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3244-3247` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==EXPIRY-DAY== ==(SCRNVAR2)== BY ==EXPDAY== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3250-3253` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==CASH-CREDIT-LIMIT== ==(SCRNVAR2)== BY ==ACSHLIM== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3256-3259` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==REISSUE-YEAR== ==(SCRNVAR2)== BY ==RISYEAR== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3262-3265` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==REISSUE-MONTH== ==(SCRNVAR2)== BY ==RISMON== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3268-3271` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==REISSUE-DAY== ==(SCRNVAR2)== BY ==RISDAY== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3274-3277` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==CURR-BAL== ==(SCRNVAR2)== BY ==ACURBAL== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3280-3283` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==CURR-CYC-CREDIT== ==(SCRNVAR2)== BY ==ACRCYCR== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3286-3289` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==CURR-CYC-DEBIT== ==(SCRNVAR2)== BY ==ACRCYDB== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3292-3295` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==EDIT-US-SSN-PART1== ==(SCRNVAR2)== BY ==ACTSSN1== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3298-3301` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==EDIT-US-SSN-PART2== ==(SCRNVAR2)== BY ==ACTSSN2== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3304-3307` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==EDIT-US-SSN-PART3== ==(SCRNVAR2)== BY ==ACTSSN3== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3310-3313` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==DT-OF-BIRTH-YEAR== ==(SCRNVAR2)== BY ==DOBYEAR== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3316-3319` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==DT-OF-BIRTH-MONTH== ==(SCRNVAR2)== BY ==DOBMON== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3322-3325` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==DT-OF-BIRTH-DAY== ==(SCRNVAR2)== BY ==DOBDAY== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3328-3331` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==FICO-SCORE== ==(SCRNVAR2)== BY ==ACSTFCO== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3334-3337` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==FIRST-NAME== ==(SCRNVAR2)== BY ==ACSFNAM== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3340-3343` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==MIDDLE-NAME== ==(SCRNVAR2)== BY ==ACSMNAM== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3346-3349` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==LAST-NAME== ==(SCRNVAR2)== BY ==ACSLNAM== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3352-3355` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==ADDRESS-LINE-1== ==(SCRNVAR2)== BY ==ACSADL1== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3358-3361` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==STATE== ==(SCRNVAR2)== BY ==ACSSTTE== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3364-3367` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==ADDRESS-LINE-2== ==(SCRNVAR2)== BY ==ACSADL2== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3370-3373` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==ZIPCODE== ==(SCRNVAR2)== BY ==ACSZIPC== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3376-3379` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==CITY== ==(SCRNVAR2)== BY ==ACSCITY== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3382-3385` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==COUNTRY== ==(SCRNVAR2)== BY ==ACSCTRY== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3388-3391` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==PHONE-NUM-1A== ==(SCRNVAR2)== BY ==ACSPH1A== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3394-3397` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==PHONE-NUM-1B== ==(SCRNVAR2)== BY ==ACSPH1B== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3400-3403` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==PHONE-NUM-1C== ==(SCRNVAR2)== BY ==ACSPH1C== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3405-3408` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==PHONE-NUM-2A== ==(SCRNVAR2)== BY ==ACSPH2A== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3411-3414` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==PHONE-NUM-2B== ==(SCRNVAR2)== BY ==ACSPH2B== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3417-3420` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==PHONE-NUM-2C== ==(SCRNVAR2)== BY ==ACSPH2C== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3422-3425` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==PRI-CARDHOLDER== ==(SCRNVAR2)== BY ==ACSPFLG== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3427-3430` |
| [COACTUPC](../../07-programs/COACTUPC.md) | cobol-program | COPY | active | ==(TESTVAR1)== BY ==EFT-ACCOUNT-ID== ==(SCRNVAR2)== BY ==ACSEFTC== ==(MAPNAME3)== BY ==CACTUPA== | `app/cbl/COACTUPC.cbl:3432-3435` |

## Observations

- anomaly: The comment line ends with a stray 'ACSHLIM' token, apparently left from an edit; it is comment text and has no effect. (`app/cpy/CSSETATY.cpy:17`)
- anomaly: In COACTUPC the comments above the last two COPY CSSETATY statements are swapped: 'EFT Account Id' precedes the PRI-CARDHOLDER copy and 'Primary Card Holder' precedes the EFT-ACCOUNT-ID copy. The code itself is correct. (`app/cbl/COACTUPC.cbl:3426-3435`)

## Sources

- `app/cpy/CSSETATY.cpy`
- `docs/_work/structure/copybooks/CSSETATY.json`
- `docs/_work/layouts/CSSETATY.json`
- `docs/_work/semantic/copybooks/CSSETATY.json`

## Confidence

Field definitions, offsets and usage edges are Confirmed from source. Purpose and key-field meanings are Inferred by the batch analysis.
