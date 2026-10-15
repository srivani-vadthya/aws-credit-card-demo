$ErrorActionPreference = 'Stop'
$root = Split-Path $PSScriptRoot -Parent
$root = Split-Path $root -Parent
if (-not (Test-Path (Join-Path $root 'README.md'))) {
    $root = 'c:\Users\Srivani.Vadthya\Documents\aws-mainframe-modernization-carddemo\aws-mainframe-modernization-carddemo-main'
}
Set-Location $root
. (Join-Path $root 'docs\_work\docx-lib.ps1')
$script:RepoRoot = $root
$script:Word = $null
$script:Doc = $null

function Stop-Word {
    if ($script:Doc -ne $null) {
        try { $script:Doc.Close($false) } catch { }
    }
    if ($script:Word -ne $null) {
        try { $script:Word.Quit() } catch { }
    }
}

try {
    Write-Output 'figures'
    $figDir = Join-Path $root 'docs\_work\docx-figures'
    New-Item -ItemType Directory -Force -Path $figDir | Out-Null
    $script:Figures = Build-Figures $figDir
    Write-Output 'word'
    Start-ProjectDocument
    Write-Output 'chapters 1-2'
    . (Join-Path $root 'docs\_work\docx-content-a.ps1')
    Write-Output 'chapter 3'
    . (Join-Path $root 'docs\_work\docx-content-b.ps1')
    Write-Output 'chapters 4-6'
    . (Join-Path $root 'docs\_work\docx-content-c.ps1')
    Write-Output 'headers'
    Set-HeadersAndFooters
    $out = Join-Path $root 'PROJECT_DOCUMENTATION.docx'
    Write-Output "save $out"
    Finish-ProjectDocument $out
    $script:Doc = $null
    $script:Word = $null
    Write-Output "bytes $((Get-Item $out).Length)"
} catch {
    Stop-Word
    Write-Output $_.Exception.ToString()
    Write-Output $_.ScriptStackTrace
    exit 1
}
