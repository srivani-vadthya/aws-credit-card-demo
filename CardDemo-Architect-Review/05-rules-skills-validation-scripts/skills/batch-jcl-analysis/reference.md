# Batch / JCL Reference

## DISP

`DISP=(status,normal-end,abnormal-end)`

| Field | Values |
|---|---|
| status | NEW (create), OLD (exclusive), SHR (shared), MOD (append/create) |
| normal-end | CATLG, KEEP, PASS, DELETE, UNCATLG |
| abnormal-end | same as normal-end (defaults to normal-end value) |

CRUD mapping: NEW -> Create; OLD/SHR + program INPUT -> Read; OLD + OUTPUT
-> Replace; MOD/EXTEND -> Append; I-O -> Update; DELETE -> Delete.

## COND / IF

- `COND=(code,op,stepname)` on EXEC: step is **bypassed** when the test is
  true (inverse logic). `COND=EVEN` / `ONLY` relate to abends.
- `// IF (STEP.RC <= 4) THEN ... // ELSE ... // ENDIF` - normal logic.
- JOB-level COND applies to all steps.

## GDG

- Base defined by `IDCAMS DEFINE GDG(NAME(x) LIMIT(n) [SCRATCH|NOSCRATCH]
  [EMPTY|NOEMPTY])`.
- `(+1)` new generation in this job, `(0)` current, `(-1)` previous; all
  relative numbers in a job refer to the state at job start.

## IDCAMS DEFINE CLUSTER essentials

`NAME`, `INDEXED|NONINDEXED|NUMBERED|LINEAR` (KSDS/ESDS/RRDS/LDS),
`KEYS(length offset)` (offset is 0-based), `RECORDSIZE(avg max)`,
`SHAREOPTIONS`, `FREESPACE`, `CISZ`, `REUSE`, DATA/INDEX components.
AIX: `RELATE(base)`, `KEYS`, `UNIQUEKEY|NONUNIQUEKEY`, `UPGRADE`; PATH:
`PATHENTRY(aix)`; `BLDINDEX INDATASET OUTDATASET`.

## DFSORT essentials

- `SORT FIELDS=(pos,len,fmt,A|D,...)`; formats CH, ZD, PD, BI, FI, AC.
- `INCLUDE/OMIT COND=(pos,len,fmt,op,value)`.
- `INREC/OUTREC FIELDS|BUILD=(...)`, `OVERLAY`, `IFTHEN`.
- `SUM FIELDS=NONE` removes duplicates.
- `OUTFIL FNAMES=dd,INCLUDE=...` splits outputs.
Positions are 1-based; for RECFM=V add 4 bytes for the RDW.

## IMS batch (DFSRRC00)

`PARM='DLI,pgm,psb'` (DL/I batch), `'BMP,pgm,psb'` (BMP, needs IMS
online), `'DBB,...'`; DDs: IMS (DBD/PSB libraries), DFSRESLB, IEFRDER
(log), database DDs matching DBD DATASET DD1 names.

## DB2 batch

- `IKJEFT01` + SYSTSIN: `DSN SYSTEM(ssid)`, `RUN PROGRAM(p) PLAN(pl)
  LIB(...)`, `BIND PLAN/PACKAGE`, `FREE`.
- `DSNTEP2/DSNTEP4` execute SQL from SYSIN; `DSNTIAUL` unloads to SYSREC
  with generated LOAD control (SYSPUNCH).
- `DSNUTILB` utilities: LOAD, UNLOAD, REORG, RUNSTATS.

## Internal reader

`//dd DD SYSOUT=(A,INTRDR)` or a CICS TDQUEUE whose DD points to INTRDR:
JCL written to it is submitted as a new job. Record the submitter and the
generated job card/steps.

## Return codes

Program `RETURN-CODE`/`MOVE n TO RETURN-CODE`, `CEE3ABD` user abends
(Unnnn), system abends (Sxxx: S0C7 data exception, S0C4 protection, S806
module not found, S013 open DCB conflict, S322 time, SB37/SD37/SE37 space).
