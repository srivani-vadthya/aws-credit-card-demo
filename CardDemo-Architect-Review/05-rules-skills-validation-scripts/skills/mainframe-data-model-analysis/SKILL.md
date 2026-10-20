---
name: mainframe-data-model-analysis
description: >-
  Reverse-engineers the data layer of a mainframe application: copybook
  record layouts with byte offsets (COMP, COMP-3, REDEFINES, OCCURS
  DEPENDING ON), VSAM clusters/AIX/paths, sequential and GDG datasets, DB2
  tables/indexes/DCLGEN, IMS DBD hierarchies and PSB sensitivity, MQ
  message formats, logical entity model, CRUD matrix and sample-data
  profiling. Use when documenting files, databases, record layouts, data
  dictionaries or data lineage of a legacy system.
disable-model-invocation: true
---

# Mainframe Data Model Analysis

Outputs: `<work_dir>/datasets/<NAME>.json` (schema
`dataset-facts.schema.json`), `<work_dir>/layouts/<COPYBOOK>.json|.md`,
`<work_dir>/data/entities.json`, `<work_dir>/xref/crud-matrix.json`.
Follow `cobol-source-reading` and `ims-db2-mq-reading` rules.

## Steps

```
- [ ] 1 Layouts: run copybook_layout.py on every record copybook; verify totals
- [ ] 2 Physical stores: VSAM (IDCAMS DEFINE + LISTCAT), sequential/GDG (JCL DCB), DB2, IMS, MQ, TS/TD queues
- [ ] 3 Store <-> layout binding: which copybook describes which store (FD, INTO(), DCLGEN, PCB/segment, MQ buffer)
- [ ] 4 Keys and indexes: primary keys, AIX/paths, DB2 indexes, IMS sequence fields/secondary indexes
- [ ] 5 Logical entities + relationships (keys shared across stores), with evidence
- [ ] 6 CRUD matrix: program/job x store with C/R/U/D/B
- [ ] 7 Data dictionary: field meaning, domain (88-levels), format, validation rules
- [ ] 8 Sample data profile (text samples only)
- [ ] 9 Discrepancies: length mismatches (copybook vs LRECL vs DDL vs DBD BYTES), unused fields
```

### 1 Layouts

```bash
python <skill_dir>/scripts/copybook_layout.py <copybook> \
    --json <work_dir>/layouts/<NAME>.json --md <work_dir>/layouts/<NAME>.md
```

- Fixed format by default; pass `--free` for free-format sources (check
  the `format` info in `inventory.json`).
- Copybooks without an 01 level are laid out as `(FRAGMENT)`; offsets are
  relative to where they are copied.
- Apply `COPY ... REPLACING` manually where used (prefix changes).
- Verify each total against every independent source: JCL LRECL (+4 for
  RECFM=V), IDCAMS RECORDSIZE, DBD `BYTES=`, comments (Unverified). Record
  agreements and mismatches.

### 2-4 Physical stores
- VSAM: from IDCAMS DEFINE in JCL/control cards: type, KEYS(len off),
  RECORDSIZE, AIX RELATE/UNIQUEKEY/UPGRADE, PATH. Cross-check with
  `LISTCAT` reports when present (attributes, counts, dates are
  point-in-time facts - label them as such).
- Online access names: CSD FILE -> DSNAME (base or PATH).
- DB2: DDL columns, types, nullability, PK/FK, indexes, tablespace; DCLGEN
  host-variable mapping; schema/database placeholders kept as parameters.
- IMS: DBD access method, segments (parent, bytes, sequence field), index
  DBDs (LCHILD/XDFLD), dataset DDs; PSB PCBs with PROCOPT per segment.
- MQ: message layouts (copybook or delimited string built with STRING/
  UNSTRING), queue roles. Queue definitions only if MQSC exists.

### 5 Entities
An entity is a business concept with an identifying key observed in code
(e.g. a key field carried across several stores). Relationships require
evidence: a program reading store B with a key taken from store A, an AIX
over a foreign key, a DB2 FK, an IMS parent/child. Render as Mermaid
`erDiagram`; label each relationship with its evidence type.

### 8 Sample data
- Text samples: count records, check record length vs layout, list
  observed distinct values for code fields (status, type) and compare with
  88-levels. Never copy personal-looking data verbatim into docs; show
  masked examples.
- Binary/EBCDIC samples: record existence, size, and implied record count
  (size / LRECL) only.

## Additional resources

- VSAM/DB2/IMS attribute glossaries and mismatch checks: [reference.md](reference.md)
