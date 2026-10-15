---
name: mainframe-integration-analysis
description: >-
  Documents integration and middleware interactions of a mainframe
  application: MQ request/reply and trigger patterns, IMS DL/I call
  sequences and PSB scheduling, DB2 SQL/cursor/commit behaviour, CICS
  two-phase commit and SYNCPOINT, file transfers (FTP), internal-reader job
  submission, program-to-program interfaces and external system touchpoints.
  Use when describing interfaces, message formats, transactional boundaries
  or external dependencies of a legacy system.
disable-model-invocation: true
---

# Mainframe Integration Analysis

Outputs: `<work_dir>/integration/interfaces.json` (one entry per
interface), `<work_dir>/integration/sequences/<name>.md` (Mermaid
`sequenceDiagram` drafts). Inputs: program facts, online and batch facts,
data facts. Follow the `ims-db2-mq-reading` rule.

## Interface catalog (one entry each)

| Field | Content |
|---|---|
| id | `IF-<module>-NNN` |
| type | MQ, IMS-DLI, DB2, CICS-LINK, CICS-START, TDQ, TSQ, FILE-TRANSFER, INTRDR, CALL-API, OTHER |
| direction | inbound / outbound / bidirectional / internal |
| producer / consumer | programs, jobs, external parties (as parameters if unnamed) |
| endpoint | queue, PSB/DBD, table, host/dataset (placeholders kept) |
| trigger | terminal, MQ trigger, schedule, START interval, batch step |
| message/record format | layout ref (copybook or delimited fields in order) |
| transactional behaviour | syncpoint scope, commit/rollback, retry, poison handling |
| error handling | reason/status codes handled, replies on error, logging |
| evidence | `path:line` list |

## Patterns to recognise

### MQ
- Trigger start: CICS transaction started by the trigger monitor;
  `EXEC CICS RETRIEVE` into MQTM gives the queue name. Document the
  queue as `runtime-provided (from trigger message)` unless defined
  elsewhere.
- Request/reply: MQGET on request queue, MQPUT/MQPUT1 to `ReplyToQ` from
  the MQMD or a fixed reply queue; note correlation (MsgId -> CorrelId).
- Loop shape: get-wait loops, browse vs destructive get, max messages
  per task, syncpoint options (MQGMO_SYNCPOINT / NO_SYNCPOINT).
- Message parsing: UNSTRING DELIMITED BY ',' etc. - list field order and
  types; build output via STRING.

### IMS DL/I
- CICS: `EXEC DLI SCHD PSB(x)` ... calls ... `TERM`; batch: PCB masks via
  `ENTRY 'DLITCBL' USING` or PROCEDURE DIVISION USING; `CALL 'CBLTDLI'`
  with function codes.
- Record each call: function (GU/GHU/GN/GHN/GNP/GHNP/ISRT/REPL/DLET/CHKP/
  XRST/ROLB), PCB, segment(s) and SSA qualification, status checks.
- Checkpoint/restart (CHKP/XRST) frequency and restart data.

### DB2
- Static SQL statements, cursors (scrollable, WITH HOLD, FOR UPDATE OF),
  COMMIT/ROLLBACK placement, isolation if stated, plan/package names.
- Dynamic SQL (PREPARE/EXECUTE) - capture the statement text source.

### Units of work
- CICS: SYNCPOINT, SYNCPOINT ROLLBACK, implicit at task end; resources in
  the same UOW (VSAM recoverable files, DB2, IMS, MQ under syncpoint).
- Batch: COMMIT frequency, IMS CHKP, restartability.
- Draw one sequence diagram per significant flow (e.g. inbound request ->
  validation -> data updates -> reply).

### Files and jobs
- FTP steps / scripts: direction, local dataset, remote target as
  parameter; text vs binary mode; credentials source (never copy secrets).
- Internal reader: who submits which job, with what substitution.
- Shell/remote scripts that upload, compile or submit: these are
  operational interfaces - link to build-deploy-security-analysis output.

## Quality bar

- No interface without at least one code or definition evidence line.
- External parties named only as they appear (queue/host names,
  comments tagged Unverified). Missing counterpart = gap.
