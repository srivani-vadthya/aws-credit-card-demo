# Technology stack

| Technology | Present | Evidence |
|---|---|---|
| Assembler | Yes | Yes. asm-program count 2. |
| BMS | Yes | Yes. bms-mapset count 21. |
| CA7 | Yes | Yes. scheduler-ca7 count 1. |
| CICS | Yes | Yes. CSD members are in the inventory. |
| Control-M | Yes | Yes. scheduler-controlm count 1. |
| DB2 | Yes | Yes. DDL and DCLGEN members are in the inventory. |
| FTP | Yes | Yes. FTPJCLS and the shell submit scripts. |
| GDG | Yes | Yes. DEFGDGB defines generation data groups. |
| IMS DB | Yes | Yes. DBD and PSB members are in the inventory. |
| MQ | Yes | Yes. Queue literals are in the vsammq programs. |
| VSAM | Yes | Yes. Dataset facts include KSDS, ESDS, RRDS, and AIX. |

Compile programs recorded in the build chains: IGYCRCTL, HEWL, DSNHPC, DFHECP1$, ASMA90, IEWL.

No product version is taken from a comment. Library names such as OEM.CICSTS.V05R06M0 appear as dataset names in sample PROCs (`samples/proc/BUILDONL.prc:28`).

## Sources

- `docs/_work/inventory.json`
- `docs/_work/ops/build.json`
- `samples/proc/BUILDONL.prc:28`

## Confidence

Confirmed facts are copied from the work files cited above. Header comments remain Unverified. Paragraph purposes remain Inferred where the program fact says so.
