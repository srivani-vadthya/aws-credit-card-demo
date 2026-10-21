# Builds the architect review bundle (CardDemo-Architect-Review/ and CardDemo-Architect-Review.zip)
# from the already validated package. Run after the regeneration chain in docs-toolkit/README.md.
# Copies only; application source is never touched. Stops when verification or the secrets check fails.
param(
    [string]$SkillsRoot = "$env:LOCALAPPDATA\Cursor\AgentStores\cursor_agent_stores\t32020737-u455266838\files\skills",
    [string]$Bundle = "CardDemo-Architect-Review"
)
$ErrorActionPreference = 'Stop'
$env:PYTHONIOENCODING = 'utf-8'
$repo = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
Set-Location $repo
$out = 'docs/application-documentation'
$work = 'docs/_work'

foreach ($p in @("$work/coverage/coverage.json", "$work/coverage/gaps.json", "$work/coverage/check_package.json",
                 "$work/rules/rules.json", "$out/14-cross-reference-traceability.md", "$out/18-coverage/gap-register.md",
                 'COMBINED_DOCUMENTATION.md', "$work/review-changelog.md", $SkillsRoot)) {
    if (-not (Test-Path $p)) { throw "missing input: $p" }
}
$cov = Get-Content "$work/coverage/coverage.json" -Raw | ConvertFrom-Json
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

Copy-Item "$out/18-coverage/gap-register.md" $d4
Copy-Item "$out/18-coverage/gap-report.md" $d4
Copy-Item "$out/16-gaps-assumptions-open-questions.md" $d4
Copy-Item "$work/coverage/gaps.json" $d4

Copy-Item $SkillsRoot "$d5/skills" -Recurse
Copy-Item '.cursor/rules' "$d5/cursor-rules" -Recurse
Copy-Item 'docs-toolkit' "$d5/docs-toolkit" -Recurse
New-Item -ItemType Directory -Force "$d5/work-dir-scripts" | Out-Null
foreach ($f in @('build_combined_markdown.ps1', 'build_review_bundle.ps1', 'prepare_review_bundle.py', 'verify_review_bundle.py',
                 'write_review_readme.py', 'check_instream_secrets.py', 'zip_review_bundle.py', 'zip_entry_check.py', 'progress.md')) {
    Copy-Item "$work/$f" "$d5/work-dir-scripts"
}
New-Item -ItemType Directory -Force "$d5/work-dir-checkpoints" | Out-Null
Copy-Item "$work/batches" "$d5/work-dir-checkpoints/batches" -Recurse
Copy-Item "$work/semantic" "$d5/work-dir-checkpoints/semantic" -Recurse
Copy-Item "$work/review-changelog.md" "$Bundle/CHANGELOG.md"

& python "$work/prepare_review_bundle.py" $Bundle --redact 'app/jcl/FTPJCL.JCL'
if ($LASTEXITCODE -ne 0) { throw "prepare_review_bundle.py failed" }
& python "$work/verify_review_bundle.py" $Bundle --repo .
$verifyCode = $LASTEXITCODE
$commit = (git rev-parse --short HEAD 2>$null)
$srcChanges = @(git status --porcelain -- app samples scripts 2>$null)
$srcState = if ($srcChanges.Count -eq 0) { 'clean' } elseif (@($srcChanges | Where-Object { $_ -notlike '`?`? *' }).Count -eq 0) { 'untracked' } else { 'modified' }
$regenerated = @('README.md', '02-coverage-validation-report/bundle-verification.md', '02-coverage-validation-report/bundle-verification.json')
$changed = @(git status --porcelain --untracked-files=all -- $Bundle 2>$null | ForEach-Object { $_.Substring(3).Trim('"') } |
             ForEach-Object { $_.Substring($Bundle.Length + 1) } | Where-Object { $regenerated -notcontains $_ } | Sort-Object)
& python "$work/write_review_readme.py" $Bundle $commit $srcState ($changed -join ';')
if ($LASTEXITCODE -ne 0) { throw "write_review_readme.py failed" }
if ($verifyCode -ne 0) { throw "verify_review_bundle.py reported failures; see $Bundle/02-coverage-validation-report/bundle-verification.md" }

& python "$work/check_instream_secrets.py" 'app/jcl/FTPJCL.JCL' $Bundle
if ($LASTEXITCODE -ne 0) { throw "in-stream secrets found in bundle" }

$zip = "$Bundle.zip"
& python "$work/zip_review_bundle.py" $Bundle $zip
if ($LASTEXITCODE -ne 0) { throw "zip_review_bundle.py failed" }
& python "$work/zip_entry_check.py" $zip $Bundle
if ($LASTEXITCODE -ne 0) { throw "ZIP entries use backslashes or lie outside $Bundle/" }

$tmp = Join-Path $env:TEMP ("carddemo-bundle-check-" + [guid]::NewGuid().ToString('N'))
Expand-Archive -Path $zip -DestinationPath $tmp
& python "$work/verify_review_bundle.py" (Join-Path $tmp $Bundle) --no-write
$zipCode = $LASTEXITCODE
$zipFiles = @(Get-ChildItem (Join-Path $tmp $Bundle) -Recurse -File).Count
Remove-Item $tmp -Recurse -Force
if ($zipCode -ne 0) { throw "verification of the unzipped bundle failed" }

$files = @(Get-ChildItem $Bundle -Recurse -File).Count
Write-Output ("bundle={0} files={1} zip={2} bytes={3} unzipped_files={4} unzipped_verification=pass" -f $Bundle, $files, $zip, (Get-Item $zip).Length, $zipFiles)
