# Online Transaction Catalog

<!-- guide: One row per CICS TRANSACTION in any CSD, plus transids used in code but not defined (flag them). -->

## Transactions

| Transid | Program | Mapset / map | Function | Entry from | Role restriction | CSD group / file | Module | Doc |
|---|---|---|---|---|---|---|---|---|
{{transaction_rows}}

## Programs without a transaction

| Program | Invoked via (XCTL/LINK/CALL/trigger) | From | Doc |
|---|---|---|---|
{{no_transid_rows}}

## Other CICS resources

| Type | Name | Purpose | Used by | Attributes | Source |
|---|---|---|---|---|---|
{{resource_rows}}
<!-- guide: FILE (DSNAME, operations), LIBRARY, TDQUEUE, TSMODEL, DB2CONN/DB2ENTRY/DB2TRAN, others found. -->

## Definition discrepancies

{{discrepancies}}
<!-- guide: Defined but unused, used but undefined, attribute conflicts (e.g. FILE allows DELETE but no program deletes), README vs CSD differences. -->

## Related documents

- [Navigation flow](navigation-flow.md)
- [COMMAREA contract](commarea-contract.md)
- Screens: {{screen_links}}

## Sources

{{sources}}

## Confidence

{{confidence_summary}}
