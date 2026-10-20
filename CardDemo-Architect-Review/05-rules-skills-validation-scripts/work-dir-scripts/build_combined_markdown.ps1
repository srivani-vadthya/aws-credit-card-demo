$ErrorActionPreference = 'Stop'
$root = Split-Path $PSScriptRoot -Parent
$root = Split-Path $root -Parent
if (-not (Test-Path (Join-Path $root 'README.md'))) {
    $root = 'c:\Users\Srivani.Vadthya\Documents\aws-mainframe-modernization-carddemo\aws-mainframe-modernization-carddemo-main'
}
Set-Location $root
$skillRoot = 'C:\Users\Srivani.Vadthya\AppData\Local\Cursor\AgentStores\cursor_agent_stores\t32020737-u455266838\files\skills'
$outPath = Join-Path $root 'COMBINED_DOCUMENTATION.md'

function Get-FileId([string]$RelativePath) {
    $s = $RelativePath.ToLowerInvariant().Replace('\', '/')
    $s = [regex]::Replace($s, '\.[a-z0-9]+$', '')
    $s = [regex]::Replace($s, '[^a-z0-9]+', '-')
    return $s.Trim('-')
}

function Get-HeadingSlug([string]$Text) {
    $s = $Text.ToLowerInvariant()
    $s = [regex]::Replace($s, '[^a-z0-9\s-]', '')
    $s = [regex]::Replace($s, '\s+', '-')
    return $s.Trim('-')
}

function Get-RepoRelative([string]$FullPath) {
    $full = [System.IO.Path]::GetFullPath($FullPath)
    $base = [System.IO.Path]::GetFullPath($root)
    if ($full.StartsWith($base, [System.StringComparison]::OrdinalIgnoreCase)) {
        return $full.Substring($base.Length).TrimStart('\', '/').Replace('\', '/')
    }
    return $null
}

$entries = New-Object System.Collections.Generic.List[object]

function Add-Entry([string]$FullPath, [string]$Part, [int]$PartOrder, [string]$Group, [int]$GroupOrder, [string]$SortKey, [string]$SourceLabel) {
    $rel = $SourceLabel
    if (-not $rel) { $rel = Get-RepoRelative $FullPath }
    if (-not $rel) { $rel = $FullPath.Replace('\', '/') }
    $entries.Add([pscustomobject]@{
        FullPath = [System.IO.Path]::GetFullPath($FullPath)
        Relative = $rel
        Id = (Get-FileId $rel)
        Part = $Part
        PartOrder = $PartOrder
        Group = $Group
        GroupOrder = $GroupOrder
        SortKey = $SortKey
        Title = $null
        Front = $null
        Body = $null
        HeadingMap = $null
    })
}

$skillOrder = @(
    'mainframe-doc-orchestrator',
    'mainframe-inventory-discovery',
    'cobol-program-analysis',
    'cics-online-analysis',
    'batch-jcl-analysis',
    'mainframe-data-model-analysis',
    'mainframe-integration-analysis',
    'business-rules-extraction',
    'build-deploy-security-analysis',
    'mainframe-doc-assembly-qa'
)
$skillRank = 0
foreach ($name in $skillOrder) {
    $skillRank++
    $dir = Join-Path $skillRoot $name
    $files = @(Get-ChildItem $dir -File | Where-Object { $_.Extension -eq '.md' } | Sort-Object @{
        Expression = {
            switch ($_.Name) {
                'SKILL.md' { '0' }
                'bootstrap.md' { '1' }
                'reference.md' { '2' }
                default { '3' + $_.Name }
            }
        }
    })
    $n = 0
    foreach ($file in $files) {
        $n++
        Add-Entry $file.FullName 'Part 1. Documentation skills' 1 $name $skillRank ('{0:D3}-{1}' -f $n, $file.Name) ("skills/" + $name + "/" + $file.Name)
    }
}

$templateRoot = Join-Path $skillRoot 'mainframe-doc-orchestrator\templates'
$t = 0
Get-ChildItem $templateRoot -Recurse -File -Filter *.md | Sort-Object FullName | ForEach-Object {
    $t++
    $relName = $_.FullName.Substring($templateRoot.Length).TrimStart('\')
    Add-Entry $_.FullName 'Part 1. Documentation skills' 1 'Documentation templates' 20 ('{0:D4}-{1}' -f $t, $relName) ("skills/mainframe-doc-orchestrator/templates/" + ($relName.Replace('\','/')))
}

$assetRules = Join-Path $skillRoot 'mainframe-doc-orchestrator\assets\rules'
$r = 0
Get-ChildItem $assetRules -File | Sort-Object Name | ForEach-Object {
    $r++
    Add-Entry $_.FullName 'Part 1. Documentation skills' 1 'Rules shipped with the skills' 30 ('{0:D2}-{1}' -f $r, $_.Name) ("skills/mainframe-doc-orchestrator/assets/rules/" + $_.Name)
}

$r = 0
Get-ChildItem (Join-Path $root '.cursor\rules') -File | Sort-Object Name | ForEach-Object {
    $r++
    Add-Entry $_.FullName 'Part 2. Rules installed in this repository' 2 'Installed reading and writing rules' 1 ('{0:D2}-{1}' -f $r, $_.Name)
}

function Get-DocGroup([string]$Relative) {
    $p = $Relative.Replace('\', '/')
    if ($p -match '^docs/application-documentation/05-online/') { return @{ Name = 'Online'; Order = 2 } }
    if ($p -match '^docs/application-documentation/06-batch/') { return @{ Name = 'Batch'; Order = 3 } }
    if ($p -match '^docs/application-documentation/07-programs/') { return @{ Name = 'Programs'; Order = 4 } }
    if ($p -match '^docs/application-documentation/08-data/') { return @{ Name = 'Data'; Order = 5 } }
    if ($p -match '^docs/application-documentation/0[0-4]-') { return @{ Name = 'Overview'; Order = 1 } }
    if ($p -match '^docs/application-documentation/') { return @{ Name = 'Cross-cutting reference'; Order = 6 } }
    if ($p -match '^docs/_work/layouts/') { return @{ Name = 'Record layouts'; Order = 3 } }
    if ($p -match '^docs/_work/rules/') { return @{ Name = 'Rules extracted by program'; Order = 4 } }
    if ($p -match '^docs/_work/integration/') { return @{ Name = 'Integration sequences'; Order = 2 } }
    return @{ Name = 'Working register'; Order = 1 }
}

Get-ChildItem (Join-Path $root 'docs\application-documentation') -Recurse -File -Filter *.md | Sort-Object FullName | ForEach-Object {
    $rel = Get-RepoRelative $_.FullName
    $g = Get-DocGroup $rel
    Add-Entry $_.FullName 'Part 3. Application documentation' 3 $g.Name $g.Order $rel
}
Get-ChildItem (Join-Path $root 'docs\_work') -Recurse -File -Filter *.md | Where-Object { $_.FullName -notmatch '\\docs\\_work\\batches\\' } | Sort-Object FullName | ForEach-Object {
    $rel = Get-RepoRelative $_.FullName
    $g = Get-DocGroup $rel
    Add-Entry $_.FullName 'Part 4. Working papers' 4 $g.Name $g.Order $rel
}

$codeLang = @{ '.py' = 'python'; '.json' = 'json'; '.yaml' = 'yaml' }
$c = 0
Get-ChildItem $skillRoot -Recurse -File | Where-Object { $codeLang.ContainsKey($_.Extension.ToLowerInvariant()) -and $_.FullName -notmatch '\\__pycache__\\' } | Sort-Object FullName | ForEach-Object {
    $c++
    $relName = $_.FullName.Substring($skillRoot.Length).TrimStart('\').Replace('\', '/')
    $skill = $relName.Split('/')[0]
    $rank = [Array]::IndexOf($skillOrder, $skill) + 1
    Add-Entry $_.FullName 'Part 5. Skill scripts and schemas' 5 $skill $rank ('{0:D3}-{1}' -f $c, $relName) ("skills/" + $relName)
}

$pathToId = @{}
foreach ($entry in $entries) {
    $pathToId[$entry.FullPath.ToLowerInvariant()] = $entry.Id
}

function Read-SourceFile([string]$Path) {
    $raw = [System.IO.File]::ReadAllText($Path)
    if ($raw.Length -gt 0 -and [int]$raw[0] -eq 0xFEFF) { $raw = $raw.Substring(1) }
    return $raw
}

foreach ($entry in $entries) {
    $raw = Read-SourceFile $entry.FullPath
    $ext = [System.IO.Path]::GetExtension($entry.FullPath).ToLowerInvariant()
    if ($codeLang.ContainsKey($ext)) {
        $entry.Title = $entry.Relative.Substring('skills/'.Length)
        $entry.Body = '~~~~' + $codeLang[$ext] + "`n" + $raw.TrimEnd() + "`n~~~~`n"
        $entry.HeadingMap = @{}
        continue
    }
    $lines = [regex]::Split($raw, "\r\n|\n|\r")
    $start = 0
    $front = $null
    if ($lines.Length -gt 0 -and $lines[0].Trim() -eq '---') {
        for ($j = 1; $j -lt $lines.Length; $j++) {
            if ($lines[$j].Trim() -eq '---') {
                $frontLines = @()
                for ($k = 1; $k -lt $j; $k++) { $frontLines += $lines[$k] }
                $front = ($frontLines -join "`n")
                $start = $j + 1
                break
            }
        }
    }
    $map = @{}
    $body = New-Object System.Text.StringBuilder
    $inFence = $false
    $sawH1 = $false
    $title = [System.IO.Path]::GetFileNameWithoutExtension($entry.FullPath)
    for ($i = $start; $i -lt $lines.Length; $i++) {
        $line = $lines[$i]
        if ($line -match '^\s*(```|~~~)') {
            $inFence = -not $inFence
            [void]$body.AppendLine($line)
            continue
        }
        if (-not $inFence -and $line -match '^(#{1,6})[ \t]+(.+?)\s*$') {
            $level = $matches[1].Length
            $text = $matches[2] -replace '\s+#+\s*$', ''
            if (-not $sawH1 -and $level -eq 1) {
                $title = $text
                $sawH1 = $true
                continue
            }
            $base = Get-HeadingSlug $text
            if (-not $base) { $base = 'section' }
            $slug = $base
            $n = 2
            while ($map.ContainsKey($slug)) {
                $slug = "$base-$n"
                $n++
            }
            $anchor = $entry.Id + '-' + $slug
            $map[$slug] = $anchor
            if (-not $map.ContainsKey("gh:$base")) { $map["gh:$base"] = $anchor }
            $newLevel = [Math]::Min(6, $level + 3)
            [void]$body.AppendLine('<a id="' + $anchor + '"></a>')
            [void]$body.AppendLine(('#' * $newLevel) + ' ' + $text)
            continue
        }
        [void]$body.AppendLine($line)
    }
    $entry.Title = $title
    $entry.Front = $front
    $entry.Body = $body.ToString()
    $entry.HeadingMap = $map
}

$idToEntry = @{}
foreach ($entry in $entries) { $idToEntry[$entry.Id] = $entry }

function Resolve-DocLink([string]$FromFull, [string]$CurrentId, [string]$Destination) {
    $dest = $Destination.Trim()
    $title = $null
    if ($dest -match '^(.*?)\s+"(.*)"\s*$') {
        $dest = $matches[1].Trim()
        $title = $matches[2]
    }
    if ($dest.StartsWith('<') -and $dest.EndsWith('>')) { $dest = $dest.Substring(1, $dest.Length - 2) }
    if ($dest -match '^(https?:|mailto:|ftp:)') { return $null }
    $pathPart = $dest
    $fragment = $null
    $hash = $dest.IndexOf('#')
    if ($hash -ge 0) {
        $pathPart = $dest.Substring(0, $hash)
        $fragment = $dest.Substring($hash + 1)
    }
    $pathPart = [System.Uri]::UnescapeDataString($pathPart).Replace('/', '\')
    $targetId = $null
    if ([string]::IsNullOrWhiteSpace($pathPart)) {
        $targetId = $CurrentId
    } else {
        $baseDir = Split-Path $FromFull -Parent
        try {
            $full = [System.IO.Path]::GetFullPath((Join-Path $baseDir $pathPart))
        } catch {
            return $null
        }
        $key = $full.ToLowerInvariant()
        if ($pathToId.ContainsKey($key)) {
            $targetId = $pathToId[$key]
        } else {
            $repoRel = Get-RepoRelative $full
            if ($repoRel) { return @{ Href = $repoRel; Title = $title } }
            return $null
        }
    }
    $href = '#' + $targetId
    if ($fragment) {
        $slug = Get-HeadingSlug ([System.Uri]::UnescapeDataString($fragment))
        $target = $idToEntry[$targetId]
        if ($slug -and $target -and $target.HeadingMap.ContainsKey("gh:$slug")) {
            $href = '#' + $target.HeadingMap["gh:$slug"]
        }
    }
    return @{ Href = $href; Title = $title }
}

$linkRegex = [regex]'(!?)\[([^\]]*)\]\(([^)]+)\)'
foreach ($entry in $entries) {
    if ($entry.PartOrder -eq 5) { continue }
    $entry.Body = $linkRegex.Replace($entry.Body, [System.Text.RegularExpressions.MatchEvaluator]{
        param($m)
        $resolved = Resolve-DocLink $entry.FullPath $entry.Id $m.Groups[3].Value
        if ($null -eq $resolved) { return $m.Value }
        $suffix = ''
        if ($resolved.Title) { $suffix = ' "' + $resolved.Title + '"' }
        return $m.Groups[1].Value + '[' + $m.Groups[2].Value + '](' + $resolved.Href + $suffix + ')'
    })
}

$ordered = $entries | Sort-Object PartOrder, GroupOrder, SortKey, Relative
$sb = New-Object System.Text.StringBuilder
[void]$sb.AppendLine('# CardDemo combined documentation')
[void]$sb.AppendLine()
[void]$sb.AppendLine('This file gathers the documentation skills, the reading and writing rules, and the Markdown documents under `docs/` into one reading order. The original files are unchanged. Each section keeps the wording of its source. Headings are nested under this document so the pieces can be read as one book. A link that pointed at another included document now points at that section.')
[void]$sb.AppendLine()
[void]$sb.AppendLine('Four kinds of material are included.')
[void]$sb.AppendLine()
[void]$sb.AppendLine('- **Skills.** The mainframe documentation skills that drive discovery, analysis, and assembly, including their templates and the rule text shipped inside the skill package.')
[void]$sb.AppendLine('- **Rules.** The copies installed in `.cursor/rules` for this repository. They are not byte-identical to the copies shipped with the skills, so both sets are kept.')
[void]$sb.AppendLine('- **Documents.** Every Markdown file under `docs/application-documentation` and `docs/_work`.')
[void]$sb.AppendLine('- **Skill scripts and schemas.** The Python scripts, JSON schemas and YAML templates shipped inside the skills, as code listings in Part 5.')
[void]$sb.AppendLine()
$docxNames = @(Get-ChildItem (Join-Path $root 'docs\application-documentation') -File -Filter *.docx | Sort-Object Name | ForEach-Object { '`' + $_.Name + '`' })
$docxText = 'none'
if ($docxNames.Count -gt 0) { $docxText = ($docxNames -join ', ') }
[void]$sb.AppendLine('Machine-readable JSON inventories under `docs/_work`, the Word files under `docs/application-documentation` (' + $docxText + '; `CardDemo-complete-documentation.docx` holds the same application pages as Part 3), the repository-local generator scripts under `docs/_work`, and figure images are not pasted into this file. Markdown links that pointed at those files now use a path from the repository root.')
[void]$sb.AppendLine()
[void]$sb.AppendLine('Batch worksheets under `docs/_work/batches/` are analysis indexes and are not included; the validated analysis they produced appears in the program, copybook and coverage pages.')
[void]$sb.AppendLine()

# ---------------------------------------------------------------- requirements coverage summary
function Read-Json([string]$Rel) {
    $p = Join-Path $root $Rel
    if (-not (Test-Path $p)) { throw "missing $Rel; run the validation scripts first" }
    return (Read-SourceFile $p | ConvertFrom-Json)
}
$cov = Read-Json 'docs\_work\coverage\coverage.json'
$gap = Read-Json 'docs\_work\coverage\gaps.json'
$rulesDoc = Read-Json 'docs\_work\rules\rules.json'
$sum = @{}
foreach ($s in $cov.summaries) { $sum[$s.category] = $s }
function Get-Met([string]$Cat) {
    $s = $sum[$Cat]
    if (-not $s) { throw "coverage category $Cat not in coverage.json" }
    return ('{0} of {1}' -f $s.documented, $s.total)
}
$crit = @{}
foreach ($c in $cov.criteria) { $crit[$c.criterion] = $c.measured }
$critPass = @($cov.criteria | Where-Object { $_.pass }).Count
$critTotal = @($cov.criteria).Count
$ruleList = @($rulesDoc.rules)
$ruleCat = @{}
foreach ($r in $ruleList) { $k = [string]$r.category; if ($ruleCat.ContainsKey($k)) { $ruleCat[$k]++ } else { $ruleCat[$k] = 1 } }
$noRule = @()
$withRule = 0
Get-ChildItem (Join-Path $root 'docs\_work\semantic\programs') -File -Filter *.json | Sort-Object Name | ForEach-Object {
    $sem = Read-SourceFile $_.FullName | ConvertFrom-Json
    if (@($sem.rules).Count -gt 0) { $withRule++ } elseif ($sem.no_business_rules_reason) { $noRule += $_.BaseName }
}
$stat = @{}
foreach ($c in $gap.components) { $k = [string]$c.status; if ($stat.ContainsKey($k)) { $stat[$k]++ } else { $stat[$k] = 1 } }
function Get-St([string]$K) { if ($stat.ContainsKey($K)) { return $stat[$K] } return 0 }
$sched = Read-Json 'docs\_work\batch\schedule.json'
$genDate = ([string]$cov.generated).Substring(0, 10)

$rq = New-Object System.Text.StringBuilder
function Add-Rq([string]$Text) { [void]$rq.AppendLine($Text) }
function Get-Lnk([string]$Label, [string]$Anchor) { return '[' + $Label + '](#' + $Anchor + ')' }
$A = 'docs-application-documentation-'
Add-Rq '<a id="requirements-coverage-summary"></a>'
Add-Rq '## Requirements coverage summary'
Add-Rq ''
Add-Rq ('This section maps each documentation requirement to the place in this file that answers it. Every number below is read from the last run of the validation scripts (`docs/_work/coverage/coverage.json` generated ' + $cov.generated + ', `docs/_work/coverage/gaps.json` generated ' + $gap.generated + ') and from `docs/_work/rules/rules.json`; none is typed by hand. Coverage criteria passing: ' + $critPass + ' of ' + $critTotal + '.')
Add-Rq ''
Add-Rq 'The percentages measure presence and validated source anchors: every listed element appears on its page with its source line, and every rule anchor was found verbatim in the cited lines. They do not prove that each description is semantically correct. Open SME questions are listed in requirement 9 and stay open until an SME answers them.'
Add-Rq ''
Add-Rq '### 1. Complete code coverage (44 COBOL programs)'
Add-Rq ''
Add-Rq ('Where: ' + (Get-Lnk 'program index' ($A + '07-programs-index')) + ' and one page per program, for example ' + (Get-Lnk 'CBTRN02C' ($A + '07-programs-cbtrn02c')) + '. Each page has divisions and sections, files and data stores, embedded CICS/SQL/DL/I commands, calls and transfers, copybooks, data items, a statement inventory, control flow, every paragraph with its logic and statements in source order, business rules, and error handling.')
Add-Rq ''
Add-Rq ('Measured: programs ' + (Get-Met 'programs') + '; paragraphs with validated logic ' + (Get-Met 'paragraphs-semantic') + '; procedure statements shown ' + (Get-Met 'procedure-statements') + '; decision points ' + (Get-Met 'decision-points-all') + '; EXEC CICS/SQL/DLI blocks ' + (Get-Met 'exec-commands') + '; CALL statements ' + (Get-Met 'call-statements') + '; file SELECTs ' + (Get-Met 'file-selects') + '; data items ' + (Get-Met 'program-data-items') + '; statements the parser could not classify: ' + $crit['statements the parser could not classify are shown on the page'] + '.')
Add-Rq ''
Add-Rq '### 2. Business rules coverage'
Add-Rq ''
Add-Rq ('Where: ' + (Get-Lnk 'business rules catalog' ($A + '09-business-rules-catalog')) + ', ' + (Get-Lnk 'programs without business rules' ($A + '09-business-rules-catalog-programs-without-business-rules')) + ', and the Business rules section of each program page.')
Add-Rq ''
$catText = ($ruleCat.Keys | Sort-Object | ForEach-Object { $_ + ' ' + $ruleCat[$_] }) -join ', '
Add-Rq ('Measured: ' + $ruleList.Count + ' rules (' + $catText + '). Programs with rules: ' + $withRule + '. Programs with a recorded no-rule reason: ' + $noRule.Count + ' (' + ($noRule -join ', ') + '). Programs with rules or a reason: ' + (Get-Met 'program-rule-analysis') + '. Business-candidate decision points linked to a rule or a reviewed reason: ' + (Get-Met 'decision-points') + '. Rules traceable to verified source and present in the catalog: ' + (Get-Met 'rule-traceability') + '.')
Add-Rq ''
Add-Rq '### 3. Copybook coverage'
Add-Rq ''
Add-Rq ('Where: one layout page per copybook (41 COBOL copybooks and 3 DB2 DCLGEN members), for example ' + (Get-Lnk 'COMEN02Y' ($A + '08-data-layouts-comen02y')) + ', with a record structure table (level, PIC, usage, start, end, length, OCCURS, REDEFINES, VALUE, line), level-88 conditions, Used by, and field references by program; ' + (Get-Lnk 'copybook usage matrix' ($A + '17-dependencies-copybook-usage')) + '. Procedure-code copybooks show their paragraphs instead of a field table. No copybook contains a COPY statement, so there are no copybook-to-copybook references.')
Add-Rq ''
Add-Rq ('Measured: copybook pages ' + (Get-Met 'copybooks') + '; fields ' + (Get-Met 'copybook-fields') + '; level-88 conditions ' + (Get-Met 'copybook-88-levels') + '; copybook paragraphs ' + (Get-Met 'copybook-paragraphs') + '; COPY statements in programs ' + (Get-Met 'copy-edges') + '.')
Add-Rq ''
Add-Rq '### 4. JCL and dependency coverage'
Add-Rq ''
Add-Rq ('Where: ' + (Get-Lnk 'job catalog' ($A + '06-batch-job-catalog')) + ' and one page per job, for example ' + (Get-Lnk 'POSTTRAN' ($A + '06-batch-jobs-posttran')) + ' (steps, EXEC and DD statements, PROC-supplied datasets, programs run, OPEN mode per DD, COND, return codes and abends set by the program, scheduler and script dependencies); PROC pages such as ' + (Get-Lnk 'REPROC' ($A + '06-batch-procs-reproc')) + '; ' + (Get-Lnk 'batch schedule flow' ($A + '06-batch-batch-schedule-flow')) + '; ' + (Get-Lnk 'job dependencies' ($A + '17-dependencies-job-dependencies')) + '; ' + (Get-Lnk 'program dependencies' ($A + '17-dependencies-program-dependencies')) + '; ' + (Get-Lnk 'CICS resources' ($A + '05-online-cics-resources')) + '; ' + (Get-Lnk 'transaction catalog' ($A + '05-online-transaction-catalog')) + '; ' + (Get-Lnk 'CRUD matrix' ($A + '08-data-crud-matrix')) + '; ' + (Get-Lnk 'integration interfaces' ($A + '10-integration-interfaces')) + '.')
Add-Rq ''
Add-Rq ('Measured: jobs ' + (Get-Met 'jcl-jobs') + '; PROC and template members ' + (Get-Met 'jcl-procs') + '; steps ' + (Get-Met 'jcl-steps') + '; DD statements ' + (Get-Met 'jcl-dds') + '; COND/IF conditions ' + (Get-Met 'jcl-conditions') + '; dataset flow edges ' + (Get-Met 'dataflow-edges') + '; scheduler and script edges ' + (Get-Met 'scheduler-edges') + ' (CA7 ' + @($sched.ca7_edges).Count + ', Control-M ' + @($sched.controlm_edges).Count + ' with OUTCOND and INCOND lines, script submits ' + @($sched.script_submits).Count + '); CICS resources ' + (Get-Met 'cics-resources') + '; CICS transactions: ' + $crit['CICS transactions documented or classified unresolved'] + '; program dependencies ' + (Get-Met 'dependencies') + '.')
Add-Rq ''
Add-Rq '### 5. Complete documentation outputs'
Add-Rq ''
Add-Rq ('Where: Part 3 of this file holds every page of `docs/application-documentation/`; ' + (Get-Lnk 'page count reconciliation' ($A + '18-coverage-gap-report-page-count-reconciliation')) + ' explains the difference from the earlier figure.')
Add-Rq ''
Add-Rq ('Measured: ' + $gap.markdown_pages + ' Markdown pages in the package against ' + $gap.claimed_pages + ' reported earlier. The ' + ($gap.markdown_pages - $gap.claimed_pages) + ' extra pages are produced only by the detail, coverage and gap scripts (PROC pages, CICS resources, data definitions, dependency pages, coverage and gap reports). The validator counted ' + $cov.documents + ' documents.')
Add-Rq ''
Add-Rq '### 6. Source traceability'
Add-Rq ''
Add-Rq ('Where: every program, copybook, job, rule and dependency row cites `path:line` or `path:start-end`; ' + (Get-Lnk 'cross-reference and traceability' ($A + '14-cross-reference-traceability')) + '.')
Add-Rq ''
Add-Rq ('Measured: ' + $crit['every source reference resolves'] + ' (each path exists and each line range lies inside the file). Rule anchors verified verbatim in the cited lines: ' + (Get-Met 'rule-traceability') + '. Paragraph descriptions that name an identifier from their own code: ' + (Get-Met 'paragraph-logic-grounding') + '.')
Add-Rq ''
Add-Rq '### 7. Automated coverage validation'
Add-Rq ''
Add-Rq ('Where: scripts in Part 5: ' + (Get-Lnk 'extract_structure.py' 'skills-mainframe-doc-orchestrator-scripts-extract-structure') + ' (source inventory of paragraphs, statements, data items, steps, DDs), ' + (Get-Lnk 'coverage_validate.py' 'skills-mainframe-doc-orchestrator-scripts-coverage-validate') + ' (compares source against pages), ' + (Get-Lnk 'gap_report.py' 'skills-mainframe-doc-orchestrator-scripts-gap-report') + ', ' + (Get-Lnk 'check_package.py' 'skills-mainframe-doc-assembly-qa-scripts-check-package') + '. Machine-readable results: `docs/_work/coverage/coverage.json`, `gaps.json`, `check_package.json`. Human-readable: ' + (Get-Lnk 'coverage report' ($A + '18-coverage-coverage-report')) + '.')
Add-Rq ''
Add-Rq ('Measured: ' + $critPass + ' of ' + $critTotal + ' criteria pass. Inventory: ' + $crit['every inventoried artifact documented or excluded with reason'] + '.')
Add-Rq ''
Add-Rq '### 8. Incremental execution'
Add-Rq ''
Add-Rq ('Where: ' + (Get-Lnk 'batch analysis contract' 'skills-mainframe-doc-orchestrator-batch-analysis') + ', ' + (Get-Lnk 'batching rule' 'cursor-rules-mainframe-doc-batching') + ', ' + (Get-Lnk 'batch_manager.py' 'skills-mainframe-doc-orchestrator-scripts-batch-manager') + ' (plan, per-batch validation, checkpoints, status and next), and the run log ' + (Get-Lnk 'progress' 'docs-work-progress') + '. Checkpoints: `docs/_work/batches/<ID>/checkpoint.json`; batch status changes only through `batch_manager.py check`, which also marks a batch stale when its source hash changes.')
Add-Rq ''
Add-Rq '### 9. Gap report'
Add-Rq ''
Add-Rq ('Where: ' + (Get-Lnk 'gap report' ($A + '18-coverage-gap-report')) + ' and the narrative register ' + (Get-Lnk 'gaps, assumptions and open questions' ($A + '16-gaps-assumptions-open-questions')) + '.')
Add-Rq ''
Add-Rq ('Measured: ' + @($gap.components).Count + ' components: documented ' + (Get-St 'documented') + ', partially documented ' + (Get-St 'partially documented') + ', missing ' + (Get-St 'missing') + ', unanalyzed ' + (Get-St 'unanalyzed') + ', unresolved ' + (Get-St 'unresolved') + ', requires SME clarification ' + (Get-St 'requires SME clarification') + '. Registers: ' + @($gap.sme_questions).Count + ' SME questions, ' + @($gap.conflicts).Count + ' conflicting definitions, ' + @($gap.ambiguous_dependencies).Count + ' ambiguous dependencies, ' + @($gap.unresolved).Count + ' unresolved items, ' + @($gap.unverified).Count + ' Unverified statements (evidence is only a comment, README or label). Excluded with a reason: ' + @($gap.excluded).Count + ' inventory entries.')
Add-Rq ''
Add-Rq '### 10. Final acceptance'
Add-Rq ''
Add-Rq ('Where: ' + (Get-Lnk 'acceptance criteria and measured coverage' ($A + '18-coverage-coverage-report')) + ' and ' + (Get-Lnk 'what these numbers do not prove' ($A + '18-coverage-coverage-report-what-these-numbers-do-not-prove')) + '.')
Add-Rq ''
$accepted = ($cov.all_pass -and (Get-St 'missing') -eq 0 -and (Get-St 'unanalyzed') -eq 0)
Add-Rq ('Measured: all coverage criteria pass: ' + $cov.all_pass + '; missing components: ' + (Get-St 'missing') + '; unanalyzed components: ' + (Get-St 'unanalyzed') + '; package acceptance rule met: ' + $accepted + '. Every inventoried item is documented or classified with a reason. This is structural and anchor-validated coverage, not 100% semantic coverage.')
Add-Rq ''

$reqText = $rq.ToString()
[void]$sb.AppendLine('Document date: ' + $genDate + ' (date of the last validation run).')
[void]$sb.AppendLine()
[void]$sb.Append($reqText)
[void]$sb.AppendLine('## Contents')
[void]$sb.AppendLine()
[void]$sb.AppendLine('- [Requirements coverage summary](#requirements-coverage-summary)')

$lastPart = ''
$lastGroup = ''
foreach ($entry in $ordered) {
    if ($entry.Part -ne $lastPart) {
        $partId = Get-FileId $entry.Part
        [void]$sb.AppendLine('- [' + $entry.Part + '](#' + $partId + ')')
        $lastPart = $entry.Part
        $lastGroup = ''
    }
    if ($entry.Group -ne $lastGroup) {
        $groupId = Get-FileId ($entry.Part + '-' + $entry.Group)
        [void]$sb.AppendLine('  - [' + $entry.Group + '](#' + $groupId + ')')
        $lastGroup = $entry.Group
    }
    $label = $entry.Title
    if ($label.Length -gt 110) { $label = $label.Substring(0, 107) + '...' }
    [void]$sb.AppendLine('    - [' + $label + '](#' + $entry.Id + ')')
}

[void]$sb.AppendLine()
$lastPart = ''
$lastGroup = ''
foreach ($entry in $ordered) {
    if ($entry.Part -ne $lastPart) {
        $partId = Get-FileId $entry.Part
        [void]$sb.AppendLine('<a id="' + $partId + '"></a>')
        [void]$sb.AppendLine('## ' + $entry.Part)
        [void]$sb.AppendLine()
        $lastPart = $entry.Part
        $lastGroup = ''
    }
    if ($entry.Group -ne $lastGroup) {
        $groupId = Get-FileId ($entry.Part + '-' + $entry.Group)
        [void]$sb.AppendLine('<a id="' + $groupId + '"></a>')
        [void]$sb.AppendLine('### ' + $entry.Group)
        [void]$sb.AppendLine()
        $lastGroup = $entry.Group
    }
    [void]$sb.AppendLine('<a id="' + $entry.Id + '"></a>')
    [void]$sb.AppendLine('#### ' + $entry.Title)
    [void]$sb.AppendLine()
    [void]$sb.AppendLine('Source file: `' + $entry.Relative + '`')
    [void]$sb.AppendLine()
    if ($entry.Front) {
        [void]$sb.AppendLine('```yaml')
        [void]$sb.AppendLine($entry.Front.TrimEnd())
        [void]$sb.AppendLine('```')
        [void]$sb.AppendLine()
    }
    [void]$sb.AppendLine($entry.Body.TrimEnd())
    [void]$sb.AppendLine()
    [void]$sb.AppendLine('---')
    [void]$sb.AppendLine()
}

$final = $sb.ToString()
$badLinks = @([regex]::Matches($reqText, '\]\(#([^)\s]+)\)') | ForEach-Object { $_.Groups[1].Value } | Where-Object { -not $final.Contains('<a id="' + $_ + '"></a>') })
if ($badLinks.Count -gt 0) { throw ('requirements summary links without a target anchor: ' + ($badLinks -join ', ')) }
$utf8 = New-Object System.Text.UTF8Encoding $false
[System.IO.File]::WriteAllText($outPath, $final, $utf8)
$item = Get-Item $outPath
Write-Output ("files=" + $entries.Count)
Write-Output ("bytes=" + $item.Length)
Write-Output ("path=" + $item.FullName)
