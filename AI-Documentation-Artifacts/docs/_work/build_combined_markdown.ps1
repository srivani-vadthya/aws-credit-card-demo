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
Get-ChildItem (Join-Path $root 'docs\_work') -Recurse -File -Filter *.md | Sort-Object FullName | ForEach-Object {
    $rel = Get-RepoRelative $_.FullName
    $g = Get-DocGroup $rel
    Add-Entry $_.FullName 'Part 4. Working papers' 4 $g.Name $g.Order $rel
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
[void]$sb.AppendLine('Three kinds of material are included.')
[void]$sb.AppendLine()
[void]$sb.AppendLine('- **Skills.** The mainframe documentation skills that drive discovery, analysis, and assembly, including their templates and the rule text shipped inside the skill package.')
[void]$sb.AppendLine('- **Rules.** The copies installed in `.cursor/rules` for this repository. They are not byte-identical to the copies shipped with the skills, so both sets are kept.')
[void]$sb.AppendLine('- **Documents.** Every Markdown file under `docs/application-documentation` and `docs/_work`.')
[void]$sb.AppendLine()
[void]$sb.AppendLine('Machine-readable JSON inventories under `docs/_work`, the Word file `docs/application-documentation/CardDemo-end-to-end.docx`, generator scripts, and figure images are not pasted into this file. Markdown links that pointed at those files now use a path from the repository root.')
[void]$sb.AppendLine()
[void]$sb.AppendLine('Document date: 13 October 2026.')
[void]$sb.AppendLine()
[void]$sb.AppendLine('## Contents')
[void]$sb.AppendLine()

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

$utf8 = New-Object System.Text.UTF8Encoding $false
[System.IO.File]::WriteAllText($outPath, $sb.ToString(), $utf8)
$item = Get-Item $outPath
Write-Output ("files=" + $entries.Count)
Write-Output ("bytes=" + $item.Length)
Write-Output ("path=" + $item.FullName)
