---
name: batch-jcl-analysis
description: >-
  Reverse-engineers the batch layer of a mainframe application: JCL jobs and
  steps, PROC expansion and overrides, DD-to-dataset mapping, utilities
  (IDCAMS, SORT, IEBGENER, IKJEFT01/DB2, DFSRRC00/IMS, FTP), GDG usage,
  condition codes and restart, and the job dependency network from
  schedulers (CA7, Control-M, TWS) and driver scripts. Use when documenting
  batch jobs, batch schedules, run books or data flows of a legacy system.
disable-model-invocation: true
---

# Batch / JCL Analysis

Inputs: inventory, references (jcl-*), program facts. Outputs:
`<work_dir>/jobs/<JOBNAME>.json` (schema `job-facts.schema.json`),
`<work_dir>/batch/schedule.json`, `<work_dir>/batch/dataflow.json`.
Follow the `jcl-proc-reading` and `scheduler-reading` rules.

## Steps

```
- [ ] 1 Job catalog: every jcl-job (name, file, JOB card params, description comments [Unverified])
- [ ] 2 Step detail: program/PROC, PARM, COND/IF, DDs with DSN/DISP/DCB/SPACE
- [ ] 3 PROC expansion + symbolic resolution (only from source); unresolved -> parameters list
- [ ] 4 Step purpose: application program (link to program facts) or utility operation (parse SYSIN)
- [ ] 5 Dataset lineage: per DSN, which steps create/read/update/delete it (incl. GDG generations)
- [ ] 6 Restart/recovery: DISP abnormal actions, COND logic, checkpoints, rerun prerequisites
- [ ] 7 Schedule: edges from every scheduler/script source; calendars, times, cyclic jobs
- [ ] 8 Online-submitted jobs: jobs written to internal reader by CICS or other jobs
- [ ] 9 Unscheduled/orphan jobs, and scheduled jobs without JCL -> findings/gaps
```

### 2 DD -> program file mapping
Match each DD name to the program's `SELECT ... ASSIGN TO` (or CICS/ASM
DCB DDNAME). Unused DDs and unmatched SELECTs are both findings. Record
physical attributes from JCL, VSAM attributes from IDCAMS DEFINE or LISTCAT.

### 4 Utility operations
Summarize in plain language, citing control statements:
- IDCAMS: DELETE/DEFINE CLUSTER/AIX/PATH/GDG, REPRO (from -> to, key
  ranges), BLDINDEX, PRINT, LISTCAT, `SET MAXCC`, `IF LASTCC`.
- SORT/ICETOOL: key fields (position, length, format, order), INCLUDE/OMIT
  conditions, INREC/OUTREC/BUILD reformatting, SUM, OUTFIL splits. Map
  positions to copybook fields where the input layout is known.
- IEBGENER/IEBCOPY: source -> target; IEFBR14: allocation/deletion via DISP.
- IKJEFT01/IKJEFT1B: `DSN SYSTEM()` + `RUN PROGRAM() PLAN()`, BIND, or
  DSNTEP2/4, DSNTIAUL SQL; DB2 utilities (LOAD/UNLOAD).
- DFSRRC00: `PARM=(DLI|BMP|DBB,program,psb,...)` -> IMS program and PSB.
- FTP / TXT2PDF / SDSF / custom tools: inputs, outputs, target hosts as
  parameters (never invent hosts).

### 5 Dataset lineage
Build `dataflow.json` edges `job.step -> DSN (mode)`; use DISP and program
OPEN mode to classify create/read/update/delete. Combine with schedule to
produce the end-to-end batch data flow diagram (Mermaid flowchart).

### 7 Schedule reconstruction
- Merge sources but keep provenance per edge (CA7 trigger, Control-M
  condition, script order). Report disagreements explicitly.
- Express calendars as given (DAYS=ALL, weekday flags, SCHID) - do not
  translate to business meaning without evidence.
- Output a Mermaid flowchart per scheduler folder/application plus a
  combined critical path (Inferred) when sources agree.

## Additional resources

- Utility control-statement cheat sheet, DISP/COND semantics, GDG rules:
  [reference.md](reference.md)
