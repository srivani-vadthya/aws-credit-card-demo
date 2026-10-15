# MQ Interface {{interface_name}}

<!-- guide: Output to 08-data/mq/<INTERFACE>.md. One per request/reply pair or one-way flow. -->

| Item | Value |
|---|---|
| Interface id | {{interface_id}} |
| Pattern | {{pattern}} |
| Request queue | {{request_queue}} |
| Reply queue | {{reply_queue}} |
| Queue manager | {{queue_manager}} |
| Trigger | {{trigger}} |
| Programs | {{programs}} |

## Interaction

```mermaid
sequenceDiagram
    {{sequence_diagram}}
```

## Message formats

### Request

| # | Field | Format / length | Meaning | Parsed into | Evidence |
|---|---|---|---|---|---|
{{request_rows}}

### Reply

| # | Field | Format / length | Meaning | Built from | Evidence |
|---|---|---|---|---|---|
{{reply_rows}}

## MQ calls and options

| Program | Call | Key options (open/get/put options, wait, syncpoint, persistence) | Reason codes handled | Lines |
|---|---|---|---|---|
{{call_rows}}

## Error and edge handling

{{error_handling}}

## Sources

{{sources}}

## Confidence

{{confidence_summary}}
