# Helpers for PROJECT_DOCUMENTATION.docx. Work-dir only. Does not change application source.

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing

function Get-Rgb([int]$R, [int]$G, [int]$B) {
    return ($R + ($G * 256) + ($B * 65536))
}

$script:Navy = Get-Rgb 31 78 121
$script:Teal = Get-Rgb 47 84 110
$script:Body = Get-Rgb 32 32 32
$script:EvidenceGray = Get-Rgb 89 89 89
$script:RowAlt = Get-Rgb 232 241 250
$script:White = Get-Rgb 255 255 255
$script:Amber = Get-Rgb 255 248 230
$script:AmberHead = Get-Rgb 122 78 20

function New-RoundedPath([int]$X, [int]$Y, [int]$W, [int]$H, [int]$Radius) {
    $path = New-Object System.Drawing.Drawing2D.GraphicsPath
    $d = $Radius * 2
    $path.AddArc($X, $Y, $d, $d, 180, 90)
    $path.AddArc(($X + $W - $d), $Y, $d, $d, 270, 90)
    $path.AddArc(($X + $W - $d), ($Y + $H - $d), $d, $d, 0, 90)
    $path.AddArc($X, ($Y + $H - $d), $d, $d, 90, 90)
    $path.CloseFigure()
    return $path
}

function Draw-Node($Graphics, [int]$X, [int]$Y, [int]$W, [int]$H, [string]$Text, [int]$FillR, [int]$FillG, [int]$FillB) {
    $path = New-RoundedPath $X $Y $W $H 14
    $fill = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb($FillR, $FillG, $FillB))
    $pen = New-Object System.Drawing.Pen ([System.Drawing.Color]::FromArgb(31, 78, 121), 2)
    $Graphics.FillPath($fill, $path)
    $Graphics.DrawPath($pen, $path)
    $font = New-Object System.Drawing.Font 'Segoe UI', 11
    $brush = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(20, 40, 60))
    $sf = New-Object System.Drawing.StringFormat
    $sf.Alignment = [System.Drawing.StringAlignment]::Center
    $sf.LineAlignment = [System.Drawing.StringAlignment]::Center
    $rect = New-Object System.Drawing.RectangleF (($X + 8), ($Y + 6), ($W - 16), ($H - 12))
    $Graphics.DrawString($Text, $font, $brush, $rect, $sf)
    $pen.Dispose(); $fill.Dispose(); $path.Dispose(); $font.Dispose(); $brush.Dispose(); $sf.Dispose()
}

function Draw-Arrow($Graphics, [int]$X1, [int]$Y1, [int]$X2, [int]$Y2) {
    $pen = New-Object System.Drawing.Pen ([System.Drawing.Color]::FromArgb(70, 100, 130), 2.2)
    $cap = New-Object System.Drawing.Drawing2D.AdjustableArrowCap 5, 6
    $pen.CustomEndCap = $cap
    $Graphics.DrawLine($pen, $X1, $Y1, $X2, $Y2)
    $pen.Dispose()
}

function Draw-Label($Graphics, [int]$X, [int]$Y, [string]$Text) {
    $font = New-Object System.Drawing.Font 'Segoe UI', 9, ([System.Drawing.FontStyle]::Italic)
    $brush = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(70, 90, 110))
    $Graphics.DrawString($Text, $font, $brush, $X, $Y)
    $font.Dispose(); $brush.Dispose()
}

function Save-Figure($Bitmap, $Graphics, [string]$Path) {
    $Bitmap.Save($Path, [System.Drawing.Imaging.ImageFormat]::Png)
    $Graphics.Dispose()
    $Bitmap.Dispose()
}

function New-Canvas([int]$W, [int]$H, [string]$Title) {
    $bmp = New-Object System.Drawing.Bitmap $W, $H
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::ClearTypeGridFit
    $g.Clear([System.Drawing.Color]::FromArgb(250, 252, 254))
    $font = New-Object System.Drawing.Font 'Segoe UI', 16, ([System.Drawing.FontStyle]::Bold)
    $brush = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(31, 78, 121))
    $g.DrawString($Title, $font, $brush, 28, 18)
    $font.Dispose(); $brush.Dispose()
    return @{ Bitmap = $bmp; Graphics = $g }
}

function Build-Figures([string]$Dir) {
    $p1 = Join-Path $Dir 'context.png'
    $c = New-Canvas 1600 860 'How the application is put together'
    $g = $c.Graphics
    Draw-Node $g 40 90 280 90 "Person at a 3270-style screen" 226 238 248
    Draw-Node $g 460 80 340 110 "CICS online`rSign-on, menus, and maintenance" 214 230 245
    Draw-Node $g 980 80 560 110 "VSAM card data`rAccounts, cards, customers, transactions, users" 214 230 245
    Draw-Arrow $g 320 135 460 135
    Draw-Arrow $g 800 135 980 135
    Draw-Node $g 40 280 280 100 "Schedulers`rCA7 and Control-M exports" 232 242 224
    Draw-Node $g 460 270 340 120 "Batch jobs`rClose files, post, calculate interest, reopen" 232 242 224
    Draw-Node $g 980 290 560 80 "Same VSAM files, closed to online use during the update" 232 242 224
    Draw-Arrow $g 320 330 460 330
    Draw-Arrow $g 800 330 980 330
    Draw-Node $g 40 500 460 150 "Optional authorization module`rIMS pending authorizations, DB2 fraud rows, MQ requests" 245 236 224
    Draw-Node $g 540 500 480 150 "Optional transaction-type module`rDB2 reference data, maintained online and in batch" 245 236 224
    Draw-Node $g 1060 500 480 150 "Optional MQ account module`rAccount and date replies on named queues" 245 236 224
    Draw-Label $g 40 700 'Blue boxes are the base application. Green boxes are batch. Tan boxes are optional source folders.'
    Draw-Label $g 40 740 'The diagram shows confirmed source boundaries. It does not show a running region.'
    Save-Figure $c.Bitmap $g $p1

    $p2 = Join-Path $Dir 'signon.png'
    $c = New-Canvas 1500 980 'Sign-on outcomes'
    $g = $c.Graphics
    Draw-Node $g 560 80 360 70 'Transaction CC00 starts COSGN00C' 214 230 245
    Draw-Node $g 560 200 360 80 "User id and password are upper-cased`rand the user-security file is read" 214 230 245
    Draw-Arrow $g 740 150 740 200
    Draw-Node $g 40 360 320 90 "Blank user id`rPlease enter User ID" 252 228 228
    Draw-Node $g 400 360 320 90 "Blank password`rPlease enter Password" 252 228 228
    Draw-Node $g 760 360 320 90 "Read response 13`rUser not found" 252 228 228
    Draw-Node $g 1120 360 340 90 "Password does not match`rWrong Password" 252 228 228
    Draw-Arrow $g 620 280 200 360
    Draw-Arrow $g 680 280 560 360
    Draw-Arrow $g 800 280 920 360
    Draw-Arrow $g 860 280 1280 360
    Draw-Node $g 250 620 420 110 "Matching password and user type A`rTransfer to admin menu COADM01C" 220 236 214
    Draw-Node $g 820 620 460 110 "Matching password and any other type`rTransfer to user menu COMEN01C" 220 236 214
    Draw-Arrow $g 640 280 460 620
    Draw-Arrow $g 840 280 1050 620
    Draw-Node $g 400 820 700 80 'Any other non-zero read response: Unable to verify the User' 252 228 228
    Draw-Label $g 40 920 'Green boxes are successful routes. Red boxes redisplay the sign-on screen.'
    Save-Figure $c.Bitmap $g $p2

    $p3 = Join-Path $Dir 'batch.png'
    $c = New-Canvas 1600 520 'Batch around the online files'
    $g = $c.Graphics
    Draw-Node $g 40 140 280 90 "CLOSEFIL`rCEMT SET FIL CLO" 232 242 224
    Draw-Node $g 400 120 320 130 "POSTTRAN / CBTRN02C`rValidate, post, or reject`reach daily transaction" 214 230 245
    Draw-Node $g 800 140 250 90 "WAITSTEP`rCOBSWAIT" 232 242 224
    Draw-Node $g 1140 140 400 90 "OPENFIL`rCEMT SET FIL OPE" 220 236 214
    Draw-Arrow $g 320 185 400 185
    Draw-Arrow $g 720 185 800 185
    Draw-Arrow $g 1050 185 1140 185
    Draw-Node $g 400 320 320 110 "INTCALC / CBACT04C`rMonthly interest from category balance and disclosure rate" 245 236 224
    Draw-Label $g 40 460 'Control-M names a daily backup chain and a monthly interest chain. CA7 names a different posting chain. They are separate exports.'
    Save-Figure $c.Bitmap $g $p3

    $p4 = Join-Path $Dir 'data.png'
    $c = New-Canvas 1500 640 'Card data that the code joins together'
    $g = $c.Graphics
    Draw-Node $g 520 250 420 120 "Card cross-reference`rCard number, customer id, account id" 214 230 245
    Draw-Node $g 80 80 360 90 'Card record' 226 238 248
    Draw-Node $g 560 80 360 90 'Customer record' 226 238 248
    Draw-Node $g 1040 80 380 90 'Account record' 226 238 248
    Draw-Arrow $g 260 170 620 250
    Draw-Arrow $g 740 170 740 250
    Draw-Arrow $g 1200 170 860 250
    Draw-Node $g 80 450 420 100 "Transaction master`rPosted and online transactions" 232 242 224
    Draw-Node $g 560 450 420 100 "User security`rUser id, password, user type" 252 236 220
    Draw-Node $g 1040 450 380 100 "Category balance and disclosure group`rUsed by interest calculation" 245 236 224
    Draw-Label $g 40 580 'Arrows are fields cited on the cross-reference. Shared record lengths do not by themselves prove which copybook belongs to which file.'
    Save-Figure $c.Bitmap $g $p4

    $p5 = Join-Path $Dir 'report.png'
    $c = New-Canvas 1600 360 'How a transaction report is submitted'
    $g = $c.Graphics
    Draw-Node $g 30 140 300 100 "Online program CORPT00C`rTransaction CR00" 214 230 245
    Draw-Node $g 400 140 340 100 "CICS queue JOBS`rOne 80-byte line at a time" 214 230 245
    Draw-Node $g 810 140 340 100 "Job TRNRPT00`rPROC TRANREPT" 232 242 224
    Draw-Node $g 1220 140 340 100 "Program CBTRN03C`rAfter a copy and a sort" 232 242 224
    Draw-Arrow $g 330 190 400 190
    Draw-Arrow $g 740 190 810 190
    Draw-Arrow $g 1150 190 1220 190
    Draw-Label $g 30 280 'The last arrow depends on CICS region JCL for DD INREADER. That JCL is not in this repository, so the hand-off is unverified.'
    Save-Figure $c.Bitmap $g $p5

    return @{
        Context = $p1
        Signon = $p2
        Batch = $p3
        Data = $p4
        Report = $p5
    }
}

function Add-Block([string]$Style, [string]$Text) {
    $range = $script:Doc.Range()
    $range.Collapse(0)
    $range.Text = $Text
    if ($Style -eq 'Bullet') {
        $range.Style = 'Normal'
        $range.ListFormat.ApplyBulletDefault() | Out-Null
        $range.ParagraphFormat.LeftIndent = 18
        $range.ParagraphFormat.FirstLineIndent = 0
    } else {
        $range.Style = $Style
    }
    $range.InsertParagraphAfter() | Out-Null
}

function Add-Figure([string]$Path, [string]$Caption) {
    $range = $script:Doc.Range()
    $range.Collapse(0)
    $shape = $script:Doc.InlineShapes.AddPicture($Path, $false, $true, $range)
    $shape.LockAspectRatio = $true
    if ($shape.Width -gt 470) { $shape.Width = 470 }
    $after = $script:Doc.Range()
    $after.Collapse(0)
    $after.InsertParagraphAfter() | Out-Null
    Add-Block 'FigureCaption' $Caption
}

function Add-Table($Headers, $Rows) {
    $range = $script:Doc.Range()
    $range.Collapse(0)
    $colCount = $Headers.Count
    $rowCount = $Rows.Count + 1
    $table = $script:Doc.Tables.Add($range, $rowCount, $colCount)
    $table.Style = 'Table Grid'
    $table.PreferredWidthType = 2
    $table.PreferredWidth = 100
    $table.AllowAutoFit = $true
    for ($c = 0; $c -lt $colCount; $c++) {
        $cell = $table.Cell(1, ($c + 1))
        $cell.Range.Text = [string]$Headers[$c]
        $cell.Range.Font.Bold = $true
        $cell.Range.Font.Size = 9
        $cell.Range.Font.Name = 'Calibri'
        $cell.Range.Font.Color = $script:White
        $cell.Shading.BackgroundPatternColor = $script:Navy
        $cell.VerticalAlignment = 1
    }
    for ($r = 0; $r -lt $Rows.Count; $r++) {
        for ($c = 0; $c -lt $colCount; $c++) {
            $value = ''
            if ($c -lt $Rows[$r].Count) { $value = [string]$Rows[$r][$c] }
            $value = $value -replace '`', ''
            $cell = $table.Cell(($r + 2), ($c + 1))
            $cell.Range.Text = $value
            $cell.Range.Font.Size = 9
            $cell.Range.Font.Name = 'Calibri'
            $cell.Range.Font.Bold = $false
            $cell.Range.Font.Color = $script:Body
            if (($r % 2) -eq 1) {
                $cell.Shading.BackgroundPatternColor = $script:RowAlt
            }
            $cell.VerticalAlignment = 1
        }
    }
    $table.Rows.Item(1).HeadingFormat = $true
    $end = $script:Doc.Range()
    $end.Collapse(0)
    $end.InsertParagraphAfter() | Out-Null
}

function Add-Callout([string]$Label, [string]$Text) {
    $range = $script:Doc.Range()
    $range.Collapse(0)
    $table = $script:Doc.Tables.Add($range, 2, 1)
    $table.PreferredWidthType = 2
    $table.PreferredWidth = 100
    $head = $table.Cell(1, 1)
    $head.Range.Text = $Label
    $head.Range.Font.Bold = $true
    $head.Range.Font.Size = 11
    $head.Range.Font.Name = 'Calibri'
    $head.Range.Font.Color = $script:White
    $head.Shading.BackgroundPatternColor = $script:AmberHead
    $body = $table.Cell(2, 1)
    $body.Range.Text = $Text
    $body.Range.Font.Size = 11
    $body.Range.Font.Name = 'Calibri'
    $body.Range.Font.Color = $script:Body
    $body.Shading.BackgroundPatternColor = $script:Amber
    $end = $script:Doc.Range()
    $end.Collapse(0)
    $end.InsertParagraphAfter() | Out-Null
}

function Get-FirstMarkdownTable([string]$Path) {
    $lines = Get-Content -Path $Path -Encoding UTF8
    $headers = $null
    $rows = New-Object System.Collections.Generic.List[object]
    $started = $false
    foreach ($line in $lines) {
        if ($line -match '^\|') {
            $started = $true
            if ($line -match '^\|\s*-') { continue }
            $parts = $line.Trim().Trim('|') -split '\|'
            $cells = @()
            foreach ($part in $parts) { $cells += $part.Trim() }
            if ($null -eq $headers) { $headers = $cells }
            else { $rows.Add($cells) }
        } elseif ($started) {
            break
        }
    }
    return @{ Headers = $headers; Rows = $rows }
}

function Start-ProjectDocument {
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $word.DisplayAlerts = 0
    $doc = $word.Documents.Add()
    $script:Word = $word
    $script:Doc = $doc

    $doc.PageSetup.TopMargin = 64
    $doc.PageSetup.BottomMargin = 64
    $doc.PageSetup.LeftMargin = 68
    $doc.PageSetup.RightMargin = 68
    $doc.PageSetup.HeaderDistance = 28
    $doc.PageSetup.FooterDistance = 28

    $normal = $doc.Styles.Item('Normal')
    $normal.Font.Name = 'Calibri'
    $normal.Font.Size = 11
    $normal.Font.Color = $script:Body
    $normal.ParagraphFormat.SpaceAfter = 8
    $normal.ParagraphFormat.SpaceBefore = 0
    $normal.ParagraphFormat.LineSpacingRule = 5
    $normal.ParagraphFormat.LineSpacing = 14

    $h1 = $doc.Styles.Item('Heading 1')
    $h1.Font.Name = 'Calibri'
    $h1.Font.Size = 20
    $h1.Font.Bold = $true
    $h1.Font.Color = $script:Navy
    $h1.ParagraphFormat.SpaceBefore = 0
    $h1.ParagraphFormat.SpaceAfter = 10
    $h1.ParagraphFormat.PageBreakBefore = $false
    $h1.ParagraphFormat.KeepWithNext = $true

    $h2 = $doc.Styles.Item('Heading 2')
    $h2.Font.Name = 'Calibri'
    $h2.Font.Size = 15
    $h2.Font.Bold = $true
    $h2.Font.Color = $script:Navy
    $h2.ParagraphFormat.SpaceBefore = 14
    $h2.ParagraphFormat.SpaceAfter = 6
    $h2.ParagraphFormat.KeepWithNext = $true

    $h3 = $doc.Styles.Item('Heading 3')
    $h3.Font.Name = 'Calibri'
    $h3.Font.Size = 12
    $h3.Font.Bold = $true
    $h3.Font.Color = $script:Teal
    $h3.ParagraphFormat.SpaceBefore = 10
    $h3.ParagraphFormat.SpaceAfter = 4
    $h3.ParagraphFormat.KeepWithNext = $true

    $title = $doc.Styles.Item('Title')
    $title.Font.Name = 'Calibri'
    $title.Font.Size = 28
    $title.Font.Bold = $true
    $title.Font.Color = $script:Navy
    $title.ParagraphFormat.Alignment = 1
    $title.ParagraphFormat.SpaceAfter = 6

    $subtitle = $doc.Styles.Item('Subtitle')
    $subtitle.Font.Name = 'Calibri'
    $subtitle.Font.Size = 16
    $subtitle.Font.Color = $script:Teal
    $subtitle.ParagraphFormat.Alignment = 1
    $subtitle.ParagraphFormat.SpaceAfter = 10

    $caption = $doc.Styles.Add('FigureCaption', 1)
    $caption.Font.Name = 'Calibri'
    $caption.Font.Size = 9
    $caption.Font.Italic = $true
    $caption.Font.Color = $script:EvidenceGray
    $caption.ParagraphFormat.Alignment = 1
    $caption.ParagraphFormat.SpaceBefore = 2
    $caption.ParagraphFormat.SpaceAfter = 12

    $evidence = $doc.Styles.Add('Evidence', 1)
    $evidence.Font.Name = 'Calibri'
    $evidence.Font.Size = 9
    $evidence.Font.Italic = $true
    $evidence.Font.Color = $script:EvidenceGray
    $evidence.ParagraphFormat.SpaceBefore = 0
    $evidence.ParagraphFormat.SpaceAfter = 8

    $tree = $doc.Styles.Add('TreeText', 1)
    $tree.Font.Name = 'Consolas'
    $tree.Font.Size = 8
    $tree.Font.Color = $script:Body
    $tree.ParagraphFormat.SpaceAfter = 0
    $tree.ParagraphFormat.SpaceBefore = 0
    $tree.ParagraphFormat.LineSpacingRule = 0
}

function Add-PageBreak {
    $range = $script:Doc.Range()
    $range.Collapse(0)
    $range.InsertBreak(7) | Out-Null
}

function Add-SectionBreak {
    $range = $script:Doc.Range()
    $range.Collapse(0)
    $range.InsertBreak(2) | Out-Null
}

function Set-HeadersAndFooters {
    $doc = $script:Doc
    $doc.PageSetup.OddAndEvenPagesHeaderFooter = $false
    $doc.PageSetup.DifferentFirstPageHeaderFooter = $false
    for ($i = 1; $i -le $doc.Sections.Count; $i++) {
        $sec = $doc.Sections.Item($i)
        $sec.PageSetup.OddAndEvenPagesHeaderFooter = $false
        $sec.PageSetup.DifferentFirstPageHeaderFooter = $false
        foreach ($kind in 1, 2, 3) {
            $sec.Headers.Item($kind).LinkToPrevious = $false
            $sec.Footers.Item($kind).LinkToPrevious = $false
            $sec.Headers.Item($kind).Range.Text = ''
            $sec.Footers.Item($kind).Range.Text = ''
        }
        if ($i -eq 1) { continue }
        $header = $sec.Headers.Item(1)
        $header.Range.Text = 'AWS Mainframe Credit Card Demo    |    Project Documentation'
        $header.Range.Font.Name = 'Calibri'
        $header.Range.Font.Size = 9
        $header.Range.Font.Bold = $false
        $header.Range.Font.Color = $script:Navy
        $header.Range.ParagraphFormat.Alignment = 1
        $header.Range.ParagraphFormat.Borders.Item(-3).LineStyle = 1
        $header.Range.ParagraphFormat.Borders.Item(-3).LineWidth = 6

        $footer = $sec.Footers.Item(1)
        $footer.Range.Text = "Evidence-based description of the CardDemo repository`t"
        $footer.Range.Font.Name = 'Calibri'
        $footer.Range.Font.Size = 9
        $footer.Range.Font.Color = $script:EvidenceGray
        $footer.Range.ParagraphFormat.Alignment = 0
        $footer.Range.ParagraphFormat.TabStops.ClearAll()
        $null = $footer.Range.ParagraphFormat.TabStops.Add(476, 2)
        $pageNo = $footer.Range.Duplicate
        $pageNo.SetRange($footer.Range.End - 1, $footer.Range.End - 1)
        $null = $doc.Fields.Add($pageNo, 33)
        if ($i -eq 2) {
            $sec.Footers.Item(1).PageNumbers.RestartNumberingAtSection = $true
            $sec.Footers.Item(1).PageNumbers.StartingNumber = 1
        }
    }
}

function Finish-ProjectDocument([string]$Path) {
    $doc = $script:Doc
    if ($doc.TablesOfContents.Count -ge 1) {
        $doc.TablesOfContents.Item(1).Update()
    }
    $doc.Fields.Update() | Out-Null
    $doc.Repaginate()
    [string]$staging = Join-Path $script:RepoRoot 'docs\_work\project-documentation-build.docx'
    if (Test-Path $staging) { Remove-Item $staging -Force }
    $doc.SaveAs([ref]$staging)
    $doc.Close($false)
    $script:Word.Quit()
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($doc) | Out-Null
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($script:Word) | Out-Null
    [GC]::Collect()
    [GC]::WaitForPendingFinalizers()
    $script:Doc = $null
    $script:Word = $null
    Start-Sleep -Seconds 2
    try {
        $openWord = [Runtime.InteropServices.Marshal]::GetActiveObject('Word.Application')
        for ($i = $openWord.Documents.Count; $i -ge 1; $i--) {
            $openDoc = $openWord.Documents.Item($i)
            if ($openDoc.FullName -eq $Path) { $openDoc.Close(0) }
        }
    } catch { }
    Copy-Item $staging $Path -Force
}
