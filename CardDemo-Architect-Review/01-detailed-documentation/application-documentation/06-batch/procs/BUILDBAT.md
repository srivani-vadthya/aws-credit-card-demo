# PROC BUILDBAT

| Item | Value |
|---|---|
| Source | `samples/proc/BUILDBAT.prc` |
| Member | BUILDBAT |
| Job card | `` |
| CLASS / MSGCLASS |  /  |
| NOTIFY |  |
| Job COND |  |
| Steps | 3 |
| Module |  |

PROC/PEND statements: PROC BLDBAT `samples/proc/BUILDBAT.prc:24-30`

Executed by: CNJBATMP step BATCMP (`samples/jcl/BATCMP.jcl:42`)

## Purpose

No descriptive comment in the JCL.

## Step flow

```mermaid
flowchart TD
    S0["COMPILE: IGYCRCTL"]
    S1["CBLPRINT: IEBGENER"]
    S0 --> S1
    S2["LKED: HEWL"]
    S1 --> S2
```

## Steps

### COMPILE

| Item | Value |
|---|---|
| EXEC | `samples/proc/BUILDBAT.prc:35-36` |
| Program | IGYCRCTL |
| PROC |  |
| Application program |  |
| PARM | `(APOST,LIST,MAP,NUMBER,NOSEQ)` |
| COND |  |
| Function (earlier pass) |  |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| STEPLIB | &COBLIB | SHR |  |  |  | `samples/proc/BUILDBAT.prc:37` |
| SYSIN | &SOURCE(&MEM) | SHR |  |  |  | `samples/proc/BUILDBAT.prc:38` |
| SYSLIB | &CPYBKS | SHR |  |  |  | `samples/proc/BUILDBAT.prc:39` |
| SYSLIB (concat) | CEE.SCEESAMP | SHR |  |  |  | `samples/proc/BUILDBAT.prc:40` |
| SYSPRINT | &LISTING(&MEM) | SHR |  |  |  | `samples/proc/BUILDBAT.prc:41` |
| SYSLIN | &&LOADSET | (MOD,PASS) |  |  |  | `samples/proc/BUILDBAT.prc:42-43` |
| SYSUT1 |  |  |  |  |  | `samples/proc/BUILDBAT.prc:44` |
| SYSUT2 |  |  |  |  |  | `samples/proc/BUILDBAT.prc:45` |
| SYSUT3 |  |  |  |  |  | `samples/proc/BUILDBAT.prc:46` |
| SYSUT4 |  |  |  |  |  | `samples/proc/BUILDBAT.prc:47` |
| SYSUT5 |  |  |  |  |  | `samples/proc/BUILDBAT.prc:48` |
| SYSUT6 |  |  |  |  |  | `samples/proc/BUILDBAT.prc:49` |
| SYSUT7 |  |  |  |  |  | `samples/proc/BUILDBAT.prc:50` |
| SYSUT8 |  |  |  |  |  | `samples/proc/BUILDBAT.prc:51` |
| SYSUT9 |  |  |  |  |  | `samples/proc/BUILDBAT.prc:52` |
| SYSUT10 |  |  |  |  |  | `samples/proc/BUILDBAT.prc:53` |
| SYSUT11 |  |  |  |  |  | `samples/proc/BUILDBAT.prc:54` |
| SYSUT12 |  |  |  |  |  | `samples/proc/BUILDBAT.prc:55` |
| SYSUT13 |  |  |  |  |  | `samples/proc/BUILDBAT.prc:56` |
| SYSUT14 |  |  |  |  |  | `samples/proc/BUILDBAT.prc:57` |
| SYSUT15 |  |  |  |  |  | `samples/proc/BUILDBAT.prc:58` |
| SYSMDECK |  |  |  |  |  | `samples/proc/BUILDBAT.prc:59` |

### CBLPRINT

| Item | Value |
|---|---|
| EXEC | `samples/proc/BUILDBAT.prc:64` |
| Program | IEBGENER |
| PROC |  |
| Application program |  |
| PARM |  |
| COND |  |
| Function (earlier pass) |  |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| SYSPRINT | SYSOUT=* |  |  |  |  | `samples/proc/BUILDBAT.prc:65` |
| SYSUT1 | &LISTING(&MEM) | SHR |  |  |  | `samples/proc/BUILDBAT.prc:66` |
| SYSUT2 | SYSOUT=* |  |  |  |  | `samples/proc/BUILDBAT.prc:67` |
| SYSIN | DUMMY |  |  |  |  | `samples/proc/BUILDBAT.prc:68` |

### LKED

| Item | Value |
|---|---|
| EXEC | `samples/proc/BUILDBAT.prc:74` |
| Program | HEWL |
| PROC |  |
| Application program |  |
| PARM | `'LIST,XREF'` |
| COND | `(8,LT,COMPILE)` |
| Function (earlier pass) |  |

| DD | Dataset / output | DISP | DCB | Program file and OPEN mode | Control data | Line |
|---|---|---|---|---|---|---|
| SYSPRINT | SYSOUT=* |  |  |  |  | `samples/proc/BUILDBAT.prc:75` |
| SYSLIB | SYS1.LINKLIB | SHR |  |  |  | `samples/proc/BUILDBAT.prc:76` |
| SYSLIB (concat) | CSF.SCSFMOD0 | SHR |  |  |  | `samples/proc/BUILDBAT.prc:77` |
| SYSLIB (concat) | CEE.SCEELKED | SHR |  |  |  | `samples/proc/BUILDBAT.prc:78` |
| SYSLIB (concat) | CEE.SCEELKEX | SHR |  |  |  | `samples/proc/BUILDBAT.prc:79` |
| SYSLIB (concat) | &LOADLIB | SHR |  |  |  | `samples/proc/BUILDBAT.prc:80` |
| SYSLIN | &&LOADSET | (OLD,DELETE) |  |  |  | `samples/proc/BUILDBAT.prc:81` |
| SYSLMOD | &LOADLIB(&MEM) | SHR |  |  |  | `samples/proc/BUILDBAT.prc:82` |
| SYSUT1 |  |  | BLKSIZE=1024 |  |  | `samples/proc/BUILDBAT.prc:83` |

## Scheduling and dependencies

Not referenced by the CA7 or Control-M exports or the shell scripts (see the gap report).

## Parameters

Symbols left as parameters (not resolved): `&&LOADSET`, `&COBLIB`, `&CPYBKS`, `&LISTING`, `&LOADLIB`, `&MEM`, `&SOURCE`.

## Sources

- `samples/proc/BUILDBAT.prc`
- `docs/_work/structure/jcl/BUILDBAT.json`

## Confidence

Steps, DDs, conditions and control-data summaries are Confirmed from the JCL. OPEN modes come from the program source. Comments are Unverified.
