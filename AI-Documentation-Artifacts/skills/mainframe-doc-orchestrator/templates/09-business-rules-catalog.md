# Business Rules Catalog

<!-- guide: From work_dir/rules/rules.json. Group by business area (derived from module/entity), then category. IDs are stable. -->

## Summary

| Area | Validation | Calculation | Decision | Routing | Authorization | Data integrity | Lifecycle | Reference | Temporal | Batch selection | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|
{{summary_rows}}

## {{area_name}}

### {{rule_id}} - {{rule_title}}

| Item | Value |
|---|---|
| Category | {{category}} |
| Statement | {{statement}} |
| Trigger | {{trigger}} |
| Conditions | {{conditions}} |
| Outcomes | {{outcomes}} |
| Data | {{data}} |
| Messages | {{messages}} |
| Implementations | {{implementations}} |
| Confidence | {{confidence}} |

{{rule_details}}
<!-- guide: Formula (calculations), decision table (3+ branches), notes on inconsistencies between implementations. Repeat block per rule. -->

## Candidate parameters (hardcoded values)

| Value | Meaning | Used in rules | Locations |
|---|---|---|---|
{{constant_rows}}

## Inconsistencies

{{inconsistencies}}

## Sources

{{sources}}

## Confidence

{{confidence_summary}}
