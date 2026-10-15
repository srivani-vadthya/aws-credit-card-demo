# COMMAREA and Inter-Program Contracts

<!-- guide: One section per distinct COMMAREA / LINKAGE contract (shared copybook or program-specific extension). -->

## {{contract_name}}

| Item | Value |
|---|---|
| Copybook | {{copybook}} |
| Length | {{length}} |
| Programs using it | {{programs}} |
| Extensions | {{extensions}} |
<!-- guide: Programs often append a program-specific area after the shared one; document each extension and its owner. -->

### Layout

{{layout_table}}
<!-- guide: From work_dir/layouts/<COPYBOOK>.md (offset, length, PIC, 88-levels). -->

### Field usage

| Field | Meaning | Set by (program:paragraph) | Read by | Evidence |
|---|---|---|---|---|
{{usage_rows}}

### State protocol

{{state_protocol}}
<!-- guide: How first-entry / re-entry / return-from-called is signalled; who resets fields; what must be set before XCTL. -->

## Other inter-program interfaces

| Caller | Callee | Mechanism | Parameters (USING / COMMAREA / CHANNEL) | Return info | Evidence |
|---|---|---|---|---|---|
{{call_rows}}

## Sources

{{sources}}

## Confidence

{{confidence_summary}}
