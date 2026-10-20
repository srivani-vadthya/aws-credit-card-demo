# Business Rules - Examples and Style

Examples use neutral names; replace with the real source names.

## Example: validation rule

```json
{
  "id": "BR-BASE-PGMX-003",
  "category": "validation",
  "statement": "Sign-on is refused when the entered password does not match the stored password for the user.",
  "trigger": "ENTER on sign-on screen",
  "conditions": [{"field": "SEC-USR-PWD", "op": "!=", "value_field": "WS-USER-PWD"}],
  "outcomes": [{"action": "redisplay screen", "message": "Wrong Password. Try again ..."}],
  "data": ["USRSEC file: SEC-USR-PWD"],
  "implementations": [{"program": "PGMX", "source": "path/PGMX.cbl:223-246"}],
  "confidence": "Confirmed",
  "notes": "Input is upper-cased before comparison (path/PGMX.cbl:133-136)."
}
```

## Example: calculation rule

```json
{
  "id": "BR-BASE-PGMY-001",
  "category": "calculation",
  "statement": "Monthly interest for a category balance is balance x annual rate / 1200.",
  "formula": "WS-MONTHLY-INT = (TRAN-CAT-BAL * DIS-INT-RATE) / 1200",
  "precision": "result PIC S9(09)V99, no ROUNDED -> truncation",
  "inputs": ["TRAN-CAT-BAL (category balance file)", "DIS-INT-RATE (disclosure group file)"],
  "implementations": [{"program": "PGMY", "source": "path/PGMY.cbl:NNN-NNN"}],
  "confidence": "Confirmed"
}
```

(The formula shown is illustrative of the format only; always copy the
actual expression from code.)

## Statement style

- Present tense, business subject first: "An account ...", "A card ...".
- Name the outcome precisely: rejected, written to reject file with reason
  code X, screen redisplayed with message, abend Unnnn.
- When business meaning comes from names only, add: "(Inferred from field
  names)".
- One rule per independent condition-outcome pair; group related rules by
  `group` (e.g. "account update field validations").

## Decision table format

| # | Condition A | Condition B | Outcome | Source |
|---|---|---|---|---|
| 1 | true | - | ... | path:line |
| 2 | false | true | ... | path:line |
| 3 | false | false | ... | path:line |
