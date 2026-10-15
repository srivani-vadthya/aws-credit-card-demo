# CBPAUP0C

Draft from `docs/_work/rules/rules.json`.

## BR-AUTH-CBPAUP0C-001

A pending authorization qualifies for delete when the computed day difference is greater than or equal to the expiry days. Expiry days are the numeric parm value, or 5 when that parm is not numeric.

- Category: temporal
- Confidence: Confirmed
- Source: `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:280-286`
- Source: `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:196-199`

## BR-AUTH-CBPAUP0C-001

A pending authorization qualifies for delete when the computed day difference is greater than or equal to the expiry days. Expiry days are the numeric parm value, or 5 when that parm is not numeric.

- Category: temporal
- Confidence: Confirmed
- Source: `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:280-286`
- Source: `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:196-199`

## BR-AUTH-CBPAUP0C-002

When a pending authorization qualifies for delete and its response code is 00, the approved count and approved amount are reduced. Any other response code reduces the declined count and the declined amount.

- Category: calculation
- Confidence: Confirmed
- Source: `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl:287-293`
