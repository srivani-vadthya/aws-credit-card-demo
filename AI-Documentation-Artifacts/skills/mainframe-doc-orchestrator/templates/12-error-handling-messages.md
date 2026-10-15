# Error Handling and Messages

## Error handling patterns

{{patterns}}
<!-- guide: Shared routines/copybooks for messages, file-status checks, RESP handling, abend routines (e.g. common abend paragraph calling LE), HANDLE ABEND, SQLCODE/DL/I status/MQ reason checks. -->

## User messages (online)

| Message text | Program | Condition | Severity | Rule | Lines |
|---|---|---|---|---|---|
{{online_message_rows}}

## Batch messages and displays

| Text / DISPLAY | Program | Condition | Destination (SYSOUT/report) | Lines |
|---|---|---|---|---|
{{batch_message_rows}}

## Abend and return codes

| Code | Kind (user abend / CICS ABCODE / RC) | Raised by | Condition | Operator action | Lines |
|---|---|---|---|---|---|
{{abend_rows}}

## Status code handling coverage

| Program | I/O operations | Checked | Unchecked | Notes |
|---|---|---|---|---|
{{coverage_rows}}

## Sources

{{sources}}

## Confidence

{{confidence_summary}}
