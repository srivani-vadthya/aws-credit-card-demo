---
name: mainframe-inventory-discovery
description: >-
  Builds a complete, evidence-backed inventory of a mainframe application
  repository by classifying every file by content signature (COBOL, copybook,
  BMS, CSD, JCL, PROC, control cards, IMS DBD/PSB, DB2 DDL/DCLGEN, Assembler,
  scheduler, scripts, data, docs), detecting encodings and fixed-format
  sequence areas, and producing a raw cross-reference scan. Use as the first
  step of mainframe reverse engineering or when asked to inventory a legacy
  codebase.
disable-model-invocation: true
---

# Mainframe Inventory Discovery

Produces `<work_dir>/inventory.json`, `<work_dir>/references.json` and an
unclassified-files report. Every later analysis step iterates over this
inventory.

## Steps

1. **Read the profile** (`docs-toolkit/project-profile.yaml`) for `work_dir`,
   `exclude`, `modules`, `data_samples`.
2. **Classify files** (deterministic, content-first):

   ```bash
   python <skill_dir>/scripts/classify_inventory.py <repo_root> \
       --out <work_dir>/inventory.json \
       --exclude "**/*.zip" --exclude "**/.git/**" \
       --module base=app/* --module ext-a=app/app-ext-a/**
   ```

   - Signatures live in [scripts/signatures.json](scripts/signatures.json);
     priority order matters (first match wins). Extend that file for new
     languages (PL/I, REXX, Easytrieve, Natural) instead of hardcoding.
   - Module globs: pass one `--module id=glob` per profile module. When
     several match, the longest (most specific) glob wins.
   - Scripts are Python 3.1+ compatible (no third-party packages).
3. **Scan references**:

   ```bash
   python <skill_dir>/scripts/scan_references.py <work_dir>/inventory.json \
       --out <work_dir>/references.json
   ```

   This gives raw `COPY`, `CALL`, `EXEC CICS/SQL/DLI` verbs and targets, MQ
   calls, `SELECT ... ASSIGN`, JCL `EXEC PGM/PROC`, DD/DSN, CSD `DEFINE`, and
   BMS map names, all with line numbers, comments and sequence areas
   excluded. It is a *baseline*; analysis skills confirm and enrich it.
4. **Review results**
   - Read `summary.by_type` and `unclassified`. For each unclassified file,
     open it and either add a signature, add a profile `path_hints` entry,
     or record it as a gap. Target: 0 unclassified.
   - Check `format.sequence_area` and `format.max_line_length` to decide the
     parsing mode (fixed vs free format) per file.
   - Binary/EBCDIC files are kept as `data-binary`; never parse them as text.
     Their layout comes from the copybook named in JCL or docs.
5. **Resolve references** (write `inventory.json` field `resolved_refs`):
   - Match each referenced member (copybook, program, PROC, mapset) to an
     inventory entry case-insensitively, ignoring extension.
   - Unmatched names: classify as `system` (known vendor members, see
     [reference.md](reference.md)) or `external-or-missing` -> gap entry.
6. **Record technologies found** per module (CICS, BMS, VSAM, DB2, IMS DB,
   IMS DC, MQ, Assembler, GDG, sort, FTP, schedulers...) with evidence, and
   update the profile `modules[].technologies`.

## Outputs checklist

- [ ] `inventory.json` validates against `schemas/inventory.schema.json`
      in the orchestrator skill
- [ ] `references.json` present
- [ ] Unclassified count = 0 or each listed in `gaps.md`
- [ ] Technology matrix per module recorded with evidence
- [ ] Orphans listed: copybooks never copied, programs never invoked by
      CSD/JCL/CALL/XCTL, jobs never scheduled (these are findings, not errors)

## Additional resources

- Taxonomy, signatures and system member lists: [reference.md](reference.md)
