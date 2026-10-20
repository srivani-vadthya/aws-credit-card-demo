# Batch semantic analysis (analyst contract)

This file is the contract for one analyst (human or agent) working on one
batch from `<work_dir>/batches/manifest.json`. Structural facts are already
extracted by `scripts/extract_structure.py`; the analyst adds meaning that a
parser cannot: paragraph logic, business rules, copybook purpose, anomalies
and SME questions. Every claim must be checkable against the source.

## Inputs per batch

- `batches/<ID>/worksheet-<PGM>.md` - paragraph index with line ranges,
  decision points that look like business logic, calculations, existing
  rules to review. It is an index only: read the whole source.
- `structure/programs/<PGM>.json` - full structural facts if needed.
- The program source and every copybook it copies (paths in
  `structure/copybook-usage.json`).

## Outputs per batch (write nothing else)

- `semantic/programs/<PGM>.json` for each program in the batch (a skeleton
  is already there - fill it, keep `program`, `source_path`,
  `source_sha256`, `batch`).
- `semantic/copybooks/<CPY>.json` for each copybook in `copybooks_owned`.

Never edit application source, structure files, other batches' files,
`manifest.json`, or `rules/rules.json`.

## Program semantics fields

| Field | Content |
|---|---|
| `status` | `complete` when finished (validator rejects `skeleton`) |
| `summary.text` | 3-8 sentences: what the program does, runtime (batch/CICS/IMS/MQ), inputs, outputs, main flow. |
| `summary.evidence` | list of `path:start-end` ranges supporting the summary |
| `paragraphs[]` | one entry per structural paragraph, same `name`; `logic` = 1-4 concrete sentences naming fields, files, conditions and outcomes; `confidence` `Confirmed` (direct paraphrase of code) or `Inferred` (intent summarized - say why). The checker warns when a description names no identifier, literal or paragraph name from that paragraph's code (`ungrounded_paragraphs`); finish with zero |
| `rules[]` | see below |
| `existing_rules_reviewed[]` | one per pre-existing rule listed in the worksheet: `verdict` `confirmed`/`corrected`/`disputed`, `source` (corrected range if needed), `anchor`, `note` |
| `no_rule_decisions[]` | `{source, reason}` for business-candidate decision lines that are NOT business rules (presentation attributes, cursor placement, defensive/technical checks, message housekeeping) |
| `no_business_rules_reason` | required when `rules` is empty: explain what the program does instead (e.g. a pure file-dump utility) |
| `observations[]` | `{kind, text, source}`; kind = `anomaly`, `dead-code`, `unchecked-io`, `hardcoded-value`, `conflict`, `security` |
| `sme_questions[]` | `{question, source}` for behaviour that the code cannot settle |

## What is a business rule here

Validations, calculations, processing decisions (record selection and
filtering, routing/navigation choices driven by data or user role,
pagination limits, status transitions), data transformations with
business meaning, error policies that change business outcome (reject,
skip, abend with a return code), and security/authorization checks.
Do not invent rules for code that only moves data, opens files, or sets
screen attributes. A program may have zero rules; then say why.

Rule fields:

```json
{
  "id": "BR-<PGM>-001",
  "category": "validation|calculation|decision|transformation|error-policy|security|data-integrity|routing",
  "statement": "Plain-language rule, precise about fields, values and outcome.",
  "paragraph": "<exact paragraph name containing source>",
  "source": "<path>:<start>-<end>",
  "anchor": "<verbatim code fragment that appears inside source>",
  "additional_sources": ["<path>:<start>-<end>"],
  "conditions": "condition text in business terms",
  "outcome": "what happens (message literal, reject code, file written)",
  "data": ["FIELD-NAMES"],
  "messages": ["literal text"],
  "confidence": "Confirmed|Inferred"
}
```

- `source` is a tight range (the IF/EVALUATE block or COMPUTE), inside the
  named paragraph. For logic in a copybook, set `"copybook": "<CPY>"` and
  cite the copybook path.
- `anchor` is copied from the code (whitespace and case are normalised by
  the checker; comment lines are ignored). Pick a distinctive fragment, e.g.
  `IF ACCT-CREDIT-LIMIT >= WS-TEMP-BAL`.
- Never cite a line you have not read. Never quote a literal you have not seen.

## Decision coverage

Every line listed under "Decision points that look like business logic" in
the worksheet must fall inside a rule `source`/`additional_sources` range, an
existing-rule review `source`, or a `no_rule_decisions` range. The checker
reports uncovered lines as warnings; finish with zero.

## Statements the parser records

`structure/programs/<PGM>.json` lists, per paragraph, every procedure
statement: decisions, calculations, file I/O, EXEC blocks, CALLs, PERFORMs,
GO TOs, literal MOVEs, field-to-field MOVEs (`data_moves`, with `from`/`to`),
SETs, DISPLAYs, terminations, other verbs (STRING, INITIALIZE, procedure
COPY, ENTRY, NEXT SENTENCE), and `unclassified` for anything else. Use it to
check that a description does not skip a step; the rendered page lists all
of them in source order.

## Legacy rules of non-COBOL members

Legacy rules implemented in Assembler or other members outside the COBOL
batches are reviewed in `semantic/reviews/<MEMBER>.json`:

```json
{
  "member": "<MEMBER>", "language": "Assembler",
  "source_path": "<path>", "source_sha256": "<sha256 of the file>",
  "summary": "what the member does, with path:line evidence",
  "existing_rules_reviewed": [
    {"id": "<legacy rule id>", "verdict": "confirmed|corrected|disputed",
     "source": "<path>:<start>-<end>", "anchor": "<verbatim fragment>", "note": "why (20+ characters)"}
  ],
  "observations": ["text with path:line and confidence"]
}
```

Validate with `batch_manager.py check-reviews docs/_work`; it checks the
hash, the rule ids, verdicts, notes and anchors, and writes
`batches/reviews-checkpoint.json`. `check all` runs it too.

## Copybook semantics fields

`purpose` (2-5 sentences: what record/structure it defines, who uses it),
`evidence` (`path:line` ranges), `key_fields[]` `{name, meaning, source}`
where `name` is an exact data item, 88-level or paragraph name of that
copybook, `observations[]`. Set `status` to `complete`.

## Checkpoint and validation

After each program (not only at the end) run from the repository root:

```
$env:PYTHONIOENCODING='utf-8'
python <skills>/mainframe-doc-orchestrator/scripts/batch_manager.py check docs/_work <PGM-or-CPY> --no-manifest
```

Fix every issue until the status is `validated` and no uncovered decision
warning remains. The per-batch `batches/<ID>/checkpoint.json` records the
result, so an interrupted batch resumes at the first program that is not
`validated`. The orchestrator later runs `check all` (which updates the
manifest) and the package validator.
