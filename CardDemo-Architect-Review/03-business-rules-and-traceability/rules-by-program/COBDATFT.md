# COBDATFT

Draft from `docs/_work/rules/rules.json`.

## BR-BASE-COBDATFT-001

Date input type 1 is rejected when character 5 of the input is a hyphen or the requested output type is 2. Otherwise hyphens are inserted after the year and after the month.

- Category: validation
- Confidence: Confirmed
- Source: `app/asm/COBDATFT.asm:30-45`

## BR-BASE-COBDATFT-002

Date input type 2 is rejected when the requested output type is 1. Otherwise characters are copied while skipping the hyphen positions. The hyphen-position check for type 2 is present only as a comment.

- Category: validation
- Confidence: Confirmed
- Source: `app/asm/COBDATFT.asm:46-54`

## BR-BASE-COBDATFT-003

A date input type other than 1 or 2 moves INVALID INPUT into the error message field.

- Category: validation
- Confidence: Confirmed
- Source: `app/asm/COBDATFT.asm:34-56`
