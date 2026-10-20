# Bootstrapping a Repository

Run once per target repository before Phase A.

## 1. Install rules

Copy every file from [assets/rules/](assets/rules/) into the target repo's
`.cursor/rules/`. Do not edit their content per repo; repo-specific facts go
into the profile. If the repo uses extensions not covered by a rule's
`globs`, extend the glob list in the installed copy only.

## 2. Create the profile

1. Copy [assets/project-profile.template.yaml](assets/project-profile.template.yaml)
   to `docs-toolkit/project-profile.yaml`.
2. Fill it from evidence only:
   - List top-level directories and file-extension counts (case-insensitive).
   - Identify source roots (directories containing program, copybook, JCL,
     map or definition sources).
   - Identify modules: a module is a directory or naming group that the repo
     itself documents or structures as a unit (README, sub-tree, CSD group,
     scheduler application). Record the evidence for each module.
   - Record existing documentation (READMEs, diagrams, data-model files) as
     `existing_docs`. They are secondary evidence (`Unverified` until
     confirmed by code).
   - Record binary or non-analyzable content in `exclude` (archives, images,
     EBCDIC data) with a reason; excluded files are still listed in the
     inventory with `type: excluded`.
   - Record placeholder / symbolic tokens observed (e.g. `&HLQ`, `<<name>>`).
3. Leave any value you cannot confirm as `null` and add a gap entry.

## 3. Create work and output folders

Create `work_dir` and `output_dir` from the profile (empty). Copy
`templates/` only if the user wants repo-local template overrides; point
`template_overrides` at that folder.

## 4. Validate

- Every `source_roots` path exists.
- Every module path exists.
- `output_dir` is not inside a source root.
