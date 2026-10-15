---
name: build-deploy-security-analysis
description: >-
  Documents how a mainframe application is built, deployed, secured and
  operated: compile/translate/link/bind procedures (COBOL, CICS, DB2, IMS,
  MQ, BMS, Assembler), load libraries, CSD install, environment setup and
  data-load jobs, deployment/automation scripts, runtime packages for
  rehosting platforms, RACF and application-level security (users, roles,
  passwords), and operational run-book tasks. Use when producing build,
  deployment, security or operations documentation for a legacy system.
disable-model-invocation: true
---

# Build, Deploy, Security and Operations Analysis

Outputs: `<work_dir>/ops/build.json`, `<work_dir>/ops/deploy.json`,
`<work_dir>/ops/security.json`, `<work_dir>/ops/runbook.json`.

## Steps

```
- [ ] 1 Build chains per source type
- [ ] 2 Library / dataset naming used by build and runtime (as parameters)
- [ ] 3 Environment setup sequence (dataset definition, data load, CSD install, DB2/IMS setup)
- [ ] 4 Automation scripts (upload, compile, submit, refresh) and their order
- [ ] 5 Runtime packages for other platforms (archives) - list, do not unpack unless asked
- [ ] 6 Security: platform (RACF commands, CICS security attributes) and application-level
- [ ] 7 Operations run book: open/close files, NEWCOPY, restart, purge, backup, monitoring outputs
- [ ] 8 Configuration and environment parameters catalog
```

### 1 Build chains
For each compile JCL/PROC: steps in order with programs (e.g. DB2
precompiler, CICS translator, COBOL compiler, binder, BMS assembly for
map + DSECT, DBD/PSB gen, bind), key options (PARM), input/output
libraries, and which source types use it. Identify the mapping
source type -> build PROC from evidence (JCL comments, PROC names used by
sample compile jobs, scripts) - never from assumption.

### 3 Environment setup
Reconstruct the install/initialize order from READMEs (Unverified) and
confirm each step against the actual JCL (what it defines/loads). Record
prerequisites (DB2 subsystem, IMS, MQ queue manager, CICS region) as
parameters.

### 6 Security
- Platform: RACF ADDUSER/ADDGROUP/PERMIT/RDEFINE commands, CICS resource
  security attributes (RESSEC, CMDSEC), DB2 GRANTs, MQ authority if present.
- Application: sign-on logic, user store (file/table), user types/roles and
  where enforced, password handling (storage format, comparison, case),
  session context in COMMAREA, admin-only functions and how they are
  guarded. Report weaknesses as neutral findings (e.g. plain-text
  password comparison) with evidence - no exploit detail.
- Never reproduce credentials found in source/docs; reference their
  location only.

### 7 Run book
Per operational task: purpose, job/transaction/command, prerequisites,
inputs/outputs, expected result/RC, failure handling and restart, evidence.
Include CICS commands documented for operators (CEMT/CEDA/CECI) and jobs
that open/close CICS files around batch.

### 8 Parameters
Catalog every environment token (HLQ, schema, subsystem IDs, queue
manager, region names, symbolic parameters) with where it is defined and
used. Values only if defined in source; otherwise `deployment-provided`.
