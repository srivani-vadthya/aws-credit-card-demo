# Builds the architect review bundle (CardDemo-Architect-Review/ and CardDemo-Architect-Review.zip)
# from the already validated package. Run after the regeneration chain in docs-toolkit/README.md.
# Copies only; application source is never touched. Fails if the in-stream FTP secrets check fails.
param(
    [string]$SkillsRoot = "$env:LOCALAPPDATA\Cursor\AgentStores\cursor_agent_stores\t32020737-u455266838\files\skills",
    [string]$Bundle = "CardDemo-Architect-Review"
)
$ErrorActionPreference = 'Stop'
$repo = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
Set-Location $repo
$out = 'docs/application-documentation'
$work = 'docs/_work'

foreach ($p in @("$work/coverage/coverage.json", "$work/coverage/gaps.json", "$work/coverage/check_package.json",
                 "$work/rules/rules.json", "$out/14-cross-reference-traceability.md", 'COMBINED_DOCUMENTATION.md', $SkillsRoot)) {
    if (-not (Test-Path $p)) { throw "missing input: $p" }
}
$cov = Get-Content "$work/coverage/coverage.json" -Raw | ConvertFrom-Json
$gap = Get-Content "$work/coverage/gaps.json" -Raw | ConvertFrom-Json
$chk = Get-Content "$work/coverage/check_package.json" -Raw | ConvertFrom-Json
$rules = @((Get-Content "$work/rules/rules.json" -Raw | ConvertFrom-Json).rules)
if (-not $cov.all_pass) { throw "coverage_validate.py did not pass; fix before bundling" }

if (Test-Path $Bundle) { Remove-Item $Bundle -Recurse -Force }
$d1 = "$Bundle/01-detailed-documentation"
$d2 = "$Bundle/02-coverage-validation-report"
$d3 = "$Bundle/03-business-rules-and-traceability"
$d4 = "$Bundle/04-gap-report"
$d5 = "$Bundle/05-rules-skills-validation-scripts"
foreach ($d in @($d1, $d2, $d3, $d4, $d5)) { New-Item -ItemType Directory -Force $d | Out-Null }

Copy-Item $out "$d1/application-documentation" -Recurse
Copy-Item 'COMBINED_DOCUMENTATION.md' $d1

Copy-Item "$out/18-coverage/coverage-report.md" $d2
Copy-Item "$work/coverage/coverage.json" $d2
Copy-Item "$work/coverage/check_package.json" $d2
Copy-Item "$work/inventory.json" $d2

Copy-Item "$out/09-business-rules-catalog.md" $d3
Copy-Item "$out/14-cross-reference-traceability.md" $d3
Copy-Item "$out/17-dependencies" "$d3/17-dependencies" -Recurse
Copy-Item "$work/rules/rules.json" $d3
Copy-Item "$work/rules/by-program" "$d3/rules-by-program" -Recurse

Copy-Item "$out/18-coverage/gap-report.md" $d4
Copy-Item "$out/16-gaps-assumptions-open-questions.md" $d4
Copy-Item "$work/coverage/gaps.json" $d4
Copy-Item "$work/gaps.md" "$d4/gaps-register.md"

Copy-Item $SkillsRoot "$d5/skills" -Recurse
Get-ChildItem "$d5/skills" -Recurse -Directory -Filter '__pycache__' | Remove-Item -Recurse -Force
Copy-Item '.cursor/rules' "$d5/cursor-rules" -Recurse
Copy-Item 'docs-toolkit' "$d5/docs-toolkit" -Recurse
New-Item -ItemType Directory -Force "$d5/work-dir-scripts" | Out-Null
foreach ($f in @('build_combined_markdown.ps1', 'build_review_bundle.ps1', 'check_instream_secrets.py', 'progress.md')) {
    Copy-Item "$work/$f" "$d5/work-dir-scripts"
}

# ---------------------------------------------------------------- README
$commit = (git rev-parse --short HEAD 2>$null)
$crit = @($cov.criteria)
$critPass = @($crit | Where-Object { $_.pass }).Count
$compCounts = @{}
foreach ($c in @($gap.components)) { $compCounts[$c.status] = 1 + [int]$compCounts[$c.status] }
$byCat = $rules | Group-Object category | Sort-Object Name
$byConf = $rules | Group-Object confidence | Sort-Object Name
$ruleProgsAny = @($rules | ForEach-Object { @($_.implementations) | ForEach-Object { $_.program } } | Where-Object { $_ } | Sort-Object -Unique).Count
$srcRef = @($cov.summaries | Where-Object { $_.category -eq 'source-references' })[0]

$L = New-Object System.Collections.Generic.List[string]
function A([string]$s) { $L.Add($s) }
A '# CardDemo documentation - architect review bundle'
A ''
A ("Built by ``docs/_work/build_review_bundle.ps1`` from repository commit ``{0}``. Validation data generated {1} (``coverage.json``)." -f $commit, $cov.generated)
A 'Everything here is a copy of validated pipeline output; no application source was changed. All metrics below are read from the JSON files in this bundle, not typed by hand.'
A ''
A '## Contents'
A ''
A '| Folder | What it answers | Start with |'
A '|---|---|---|'
A '| `01-detailed-documentation/` | Full detailed documentation: one page per program, copybook, job, proc, screen, dataset, table, IMS database, plus the reading copy and Word file | `application-documentation/README.md` or `COMBINED_DOCUMENTATION.md` |'
A '| `02-coverage-validation-report/` | Coverage of every in-scope COBOL program, copybook, JCL job and proc, CICS resource, dataset and other inventoried component; 33 measured acceptance criteria | `coverage-report.md` |'
A '| `03-business-rules-and-traceability/` | Every business rule mapped to program, paragraph, source lines, CICS transactions and JCL steps; online and batch technical flows; call, copy, data and scheduler dependencies | `14-cross-reference-traceability.md`, then `09-business-rules-catalog.md` |'
A '| `04-gap-report/` | Missing, partially analysed, unresolved, Unverified and SME-dependent items, conflicts and exclusions | `gap-report.md` |'
A '| `05-rules-skills-validation-scripts/` | The Cursor rules, skills, scripts and project profile that produce and validate the package, so the run can be repeated | `docs-toolkit/README.md`, `skills/mainframe-doc-orchestrator/SKILL.md` |'
A ''
A 'Pages in folders 02 to 04 are copies of pages in `01-detailed-documentation/application-documentation/`. Their links to other pages (for example `07-programs/...`) resolve only inside that folder, so follow links from there.'
A ''
A '## Headline results'
A ''
A '| Measure | Value |'
A '|---|---|'
A ("| Acceptance criteria passed (``coverage_validate.py``) | {0} of {1} |" -f $critPass, $crit.Count)
A ("| Markdown pages in the package | {0} (earlier progress log claimed {1}; reconciled in ``04-gap-report/gap-report.md``) |" -f $gap.markdown_pages, $gap.claimed_pages)
$chkIssues = 0
foreach ($n in @('uncovered_artifacts', 'broken_links', 'placeholders', 'template_guides_left', 'mermaid_warnings', 'missing_sources_section')) {
    $chkIssues += @($chk.$n | Where-Object { $_ }).Count
}
A ("| Package check (``check_package.py``) | {0} documents, {1} issues (uncovered artifacts, broken links, placeholders, template guides, Mermaid warnings, missing Sources sections) |" -f $chk.documents, $chkIssues)
A ("| Source references (``path:line``) checked against the files | {0} of {1} valid |" -f $srcRef.documented, $srcRef.total)
$ruleProgSet = @($rules | ForEach-Object { @($_.implementations) | ForEach-Object { $_.program } } | Where-Object { $_ } | Sort-Object -Unique)
$cobol = @($gap.components | Where-Object { $_.kind -eq 'cobol-program' } | ForEach-Object { $_.name })
$asm = @($gap.components | Where-Object { $_.kind -eq 'asm-program' } | ForEach-Object { $_.name })
$cobolNoRule = @($cobol | Where-Object { $ruleProgSet -notcontains $_ } | Sort-Object)
$asmRule = @($asm | Where-Object { $ruleProgSet -contains $_ } | Sort-Object)
A ("| Business rules | {0} rules in {1} programs: {2} of {3} COBOL programs plus Assembler {4}. COBOL programs with no business rule (logic documented on their pages, reason in the rules catalog): {5} |" -f $rules.Count, $ruleProgsAny, ($cobol.Count - $cobolNoRule.Count), $cobol.Count, ($asmRule -join ', '), ($cobolNoRule -join ', '))
A ("| Rules by confidence | {0} |" -f (($byConf | ForEach-Object { "$($_.Name) $($_.Count)" }) -join ', '))
A ("| Rules by category | {0} |" -f (($byCat | ForEach-Object { "$($_.Name) $($_.Count)" }) -join ', '))
A ("| Components classified in gap report | {0}: {1} |" -f @($gap.components).Count, (($compCounts.Keys | Sort-Object | ForEach-Object { "$_ $($compCounts[$_])" }) -join ', '))
A ("| Open items | {0} SME questions, {1} Unverified statements, {2} unresolved items, {3} conflicts, {4} ambiguous dependencies |" -f @($gap.sme_questions).Count, @($gap.unverified).Count, @($gap.unresolved).Count, @($gap.conflicts).Count, @($gap.ambiguous_dependencies).Count)
A ("| Excluded paths (with reasons) | {0} |" -f @($gap.excluded).Count)
A ''
A '## Coverage by category'
A ''
A 'From `02-coverage-validation-report/coverage.json`. "Other" counts items deliberately classified outside the category (for example excluded or non-application files); they are listed in the coverage report.'
A ''
A '| Category | Kind | Documented | Partial | Missing | Other | Total | % documented |'
A '|---|---|---|---|---|---|---|---|'
foreach ($s in @($cov.summaries)) {
    A ("| {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} |" -f $s.category, $s.kind, $s.documented, $s.partial, $s.missing, $s.classified_other, $s.total, $s.percent_documented)
}
A ''
A '## What these numbers do not claim'
A ''
A '- 100% in a structural category means every item was extracted and appears on a page with a source citation. It does not mean every behaviour is semantically confirmed.'
A ('- {0} components are classified "requires SME clarification" and {1} "unresolved"; the reasons and questions are in `04-gap-report/gap-report.md`.' -f [int]$compCounts['requires SME clarification'], [int]$compCounts['unresolved'])
A ('- {0} statements rest only on comments, READMEs or unresolved symbolics and are tagged Unverified (gap report, section "Unverified statements").' -f @($gap.unverified).Count)
A '- Placeholders and symbolics (`&HLQ`, `&SYSUID`, schema names) are documented as parameters; no values were invented.'
A '- The FTP host and login values in `app/jcl/FTPJCL.JCL` are not reproduced anywhere in this bundle (checked by `check_instream_secrets.py`, result below).'
A '- `AI-Documentation-Artifacts/` and `AI-Documentation-Artifacts.zip` in the repository root are an older snapshot (2026-10-15) and are superseded by this bundle.'
A ''
A '## Repeating the run'
A ''
A 'The full command sequence is in `05-rules-skills-validation-scripts/docs-toolkit/README.md`. In short, with the skills installed under the Cursor user store and `$env:PYTHONIOENCODING=''utf-8''`:'
A ''
A '```powershell'
A '$S = "<skills>\mainframe-doc-orchestrator\scripts"; $Q = "<skills>\mainframe-doc-assembly-qa\scripts"'
A 'python "$S\batch_manager.py" check docs/_work all'
A 'python "$S\schedule_lines.py" docs/_work'
A 'python "$S\render_detail.py" docs/_work docs/application-documentation'
A 'python "$S\coverage_validate.py" docs/_work docs/application-documentation'
A 'python "$S\gap_report.py" docs/_work docs/application-documentation --claimed-pages 404'
A 'python "$Q\check_package.py" docs/_work/inventory.json docs/application-documentation --json docs/_work/coverage/check_package.json'
A 'python "$Q\build_docx.py" docs/application-documentation docs/application-documentation/CardDemo-complete-documentation.docx --title "CardDemo application documentation (complete)"'
A 'powershell -NoProfile -File docs/_work/build_combined_markdown.ps1'
A 'powershell -NoProfile -File docs/_work/build_review_bundle.ps1'
A '```'
A ''
A 'Semantic batches resume from `docs/_work/batches/<id>/checkpoint.json`; `docs/_work/progress.md` (copied to `work-dir-scripts/`) records every pass.'
A ''

# ---------------------------------------------------------------- secrets check
$secOut = & python "$work/check_instream_secrets.py" 'app/jcl/FTPJCL.JCL' $Bundle 2>&1
$secCode = $LASTEXITCODE
A '## Secrets check'
A ''
A '```text'
foreach ($secLine in $secOut) { A ([string]$secLine) }
A '```'
[System.IO.File]::WriteAllLines((Join-Path $repo "$Bundle/README.md"), $L, (New-Object System.Text.UTF8Encoding($false)))
if ($secCode -ne 0) { throw "in-stream secrets found in bundle; see $Bundle/README.md" }

# ---------------------------------------------------------------- zip
$zip = "$Bundle.zip"
if (Test-Path $zip) { Remove-Item $zip -Force }
Compress-Archive -Path $Bundle -DestinationPath $zip
$files = @(Get-ChildItem $Bundle -Recurse -File).Count
Write-Output ("bundle={0} files={1} zip={2} bytes={3} criteria={4}/{5} secrets_findings=0" -f $Bundle, $files, $zip, (Get-Item $zip).Length, $critPass, $crit.Count)
