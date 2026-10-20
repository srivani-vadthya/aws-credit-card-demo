"""Build one full-detail Word document from every Markdown page of a documentation package.

Usage (from the repository root):
  python build_docx.py <output_dir> <docx_path> [--title TEXT] [--date TEXT]

Every *.md under <output_dir> is included in path order (folder overview pages
first, then the pages inside the folder). Headings, paragraphs, pipe tables,
bullet and numbered lists, block quotes, fenced code and Mermaid source are
converted; links between pages become internal bookmarks, other links keep
their text and target. Nothing is summarised or dropped: the page text is the
document text. Python 3.1+ standard library only (zipfile + WordprocessingML).
"""
import os
import re
import sys
import time
import zipfile

BAD_XML = re.compile("[\x00-\x08\x0b\x0c\x0e-\x1f]")
INLINE = re.compile(r"(`[^`]+`)|(\*\*[^*]+\*\*)|(!?\[[^\]]*\]\([^)]+\))|(<br\s*/?>)")
LINK = re.compile(r"!?\[([^\]]*)\]\(([^)]+)\)")


def xml(s):
    s = BAD_XML.sub("", s)
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def unescape_md(s):
    s = re.sub(r"\\([\\`*_{}\[\]()#+\-.!|<>])", r"\1", s)
    return s.replace("&nbsp;", "\u00a0").replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")


def read(path):
    f = open(path, "r", encoding="utf-8-sig")
    try:
        return f.read()
    finally:
        f.close()


class Doc(object):
    def __init__(self, out_dir, pages):
        self.out_dir = out_dir
        self.body = []
        self.bm_id = 0
        self.page_bm = dict((rel, "p%d" % (i + 1)) for i, rel in enumerate(pages))

    # ------------------------------------------------------------ runs
    def run(self, text, bold=False, italic=False, code=False, size=None, link=False):
        if not text:
            return ""
        pr = '<w:rStyle w:val="Hyperlink"/>' if link else ""
        if code:
            pr += '<w:rFonts w:ascii="Consolas" w:hAnsi="Consolas" w:cs="Consolas"/>'
        if bold:
            pr += "<w:b/>"
        if italic:
            pr += "<w:i/>"
        if size:
            pr += '<w:sz w:val="%d"/><w:szCs w:val="%d"/>' % (size, size)
        return '<w:r>%s<w:t xml:space="preserve">%s</w:t></w:r>' % (("<w:rPr>%s</w:rPr>" % pr) if pr else "", xml(text))

    def link_target(self, page, dest):
        dest = dest.strip().split(" ")[0].strip("<>")
        if re.match(r"^(https?|mailto|ftp):", dest):
            return None, dest
        path = dest.split("#")[0]
        if not path:
            return self.page_bm.get(page), None
        full = os.path.normpath(os.path.join(os.path.dirname(os.path.join(self.out_dir, page)), path))
        rel = os.path.relpath(full, self.out_dir).replace("\\", "/")
        if rel in self.page_bm:
            return self.page_bm[rel], None
        repo = os.path.relpath(full, os.getcwd()).replace("\\", "/")
        return None, repo

    def inline(self, page, text, bold=False, size=None):
        out = []
        pos = 0
        for m in INLINE.finditer(text):
            if m.start() > pos:
                out.append(self.run(unescape_md(text[pos:m.start()]), bold=bold, size=size))
            tok = m.group(0)
            if m.group(1):
                out.append(self.run(tok[1:-1].replace("\\|", "|"), bold=bold, code=True, size=size))
            elif m.group(2):
                out.append(self.run(unescape_md(tok[2:-2]), bold=True, size=size))
            elif m.group(3):
                lm = LINK.match(tok)
                label, dest = lm.group(1), lm.group(2)
                anchor, other = self.link_target(page, dest)
                lab = unescape_md(label) or dest
                if anchor:
                    out.append('<w:hyperlink w:anchor="%s" w:history="1">%s</w:hyperlink>' %
                               (anchor, self.run(lab, bold=bold, size=size, link=True)))
                elif other and other != lab:
                    out.append(self.run(lab, bold=bold, size=size))
                    out.append(self.run(" (%s)" % other, italic=True, size=size))
                else:
                    out.append(self.run(lab, bold=bold, size=size))
            else:
                out.append("<w:r><w:br/></w:r>")
            pos = m.end()
        if pos < len(text):
            out.append(self.run(unescape_md(text[pos:]), bold=bold, size=size))
        return "".join(out)

    # ------------------------------------------------------------ blocks
    def para(self, runs, style=None, bookmark=None, page_break=False, ind=None, keep=False):
        ppr = ""
        if style:
            ppr += '<w:pStyle w:val="%s"/>' % style
        if keep:
            ppr += "<w:keepNext/>"
        if page_break:
            ppr += "<w:pageBreakBefore/>"
        if ind:
            ppr += '<w:ind w:left="%d" w:hanging="240"/>' % ind
        bm = ""
        if bookmark:
            self.bm_id += 1
            bm = '<w:bookmarkStart w:id="%d" w:name="%s"/><w:bookmarkEnd w:id="%d"/>' % (self.bm_id, bookmark, self.bm_id)
        self.body.append("<w:p>%s%s%s</w:p>" % (("<w:pPr>%s</w:pPr>" % ppr) if ppr else "", bm, runs))

    def table(self, page, rows):
        ncol = max(len(r) for r in rows)
        out = ['<w:tbl><w:tblPr><w:tblStyle w:val="DocTable"/><w:tblW w:w="5000" w:type="pct"/>'
               '<w:tblLayout w:type="autofit"/></w:tblPr><w:tblGrid>']
        out.append("".join('<w:gridCol w:w="%d"/>' % (14400 // ncol) for _ in range(ncol)))
        out.append("</w:tblGrid>")
        for i, r in enumerate(rows):
            r = r + [""] * (ncol - len(r))
            trpr = "<w:trPr><w:tblHeader/></w:trPr>" if i == 0 else ""
            cells = []
            for c in r:
                shade = '<w:shd w:val="clear" w:color="auto" w:fill="D9E2F3"/>' if i == 0 else ""
                cells.append('<w:tc><w:tcPr>%s</w:tcPr><w:p><w:pPr><w:pStyle w:val="TableText"/></w:pPr>%s</w:p></w:tc>' %
                             (shade, self.inline(page, c.strip(), bold=(i == 0))))
            out.append("<w:tr>%s%s</w:tr>" % (trpr, "".join(cells)))
        out.append("</w:tbl>")
        self.body.append("".join(out))
        self.para("", style="Spacer")


def split_row(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    cells, cur, i = [], "", 0
    in_code = False
    while i < len(s):
        ch = s[i]
        if ch == "\\" and i + 1 < len(s) and s[i + 1] == "|":
            cur += "\\|"
            i += 2
            continue
        if ch == "`":
            in_code = not in_code
        if ch == "|" and not in_code:
            cells.append(cur)
            cur = ""
        else:
            cur += ch
        i += 1
    cells.append(cur)
    return cells


def convert_page(doc, rel, text, shift, first_bookmark, page_break):
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    i, n = 0, len(lines)
    titled = False
    while i < n:
        line = lines[i]
        st = line.strip()
        fence = re.match(r"^\s*(```|~~~)\s*([\w-]*)", line)
        if fence:
            lang = fence.group(2).lower()
            i += 1
            block = []
            while i < n and not re.match(r"^\s*(```|~~~)\s*$", lines[i]):
                block.append(lines[i])
                i += 1
            i += 1
            if lang == "mermaid":
                doc.para(doc.run("Mermaid diagram source (open the Markdown page or a Mermaid viewer to see the drawing):", italic=True), style="Caption")
            for b in block or [""]:
                doc.para(doc.run(b.replace("\t", "    "), code=True), style="Code")
            continue
        h = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", line)
        if h:
            lvl = min(6, len(h.group(1)) + shift)
            bm = None
            pb = False
            if not titled:
                bm, pb, titled = first_bookmark, page_break, True
            doc.para(doc.inline(rel, h.group(2)), style="Heading%d" % lvl, bookmark=bm, page_break=pb, keep=True)
            if bm:
                doc.para(doc.run("Page: ", italic=True, size=16) + doc.run(rel, code=True, size=16), style="Caption")
            i += 1
            continue
        if st.startswith("|") and i + 1 < n and re.match(r"^\s*\|?\s*:?-{2,}", lines[i + 1]):
            rows = [split_row(line)]
            i += 2
            while i < n and lines[i].strip().startswith("|"):
                rows.append(split_row(lines[i]))
                i += 1
            doc.table(rel, rows)
            continue
        if not st or re.match(r"^(-{3,}|\*{3,}|_{3,})$", st) or re.match(r"^</?a\b[^>]*>(</a>)?$", st):
            i += 1
            continue
        lm = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$", line)
        if lm:
            depth = len(lm.group(1).replace("\t", "  ")) // 2
            mark = "\u2022" if lm.group(2) in "-*+" else lm.group(2)
            doc.para(doc.run(mark + "\t") + doc.inline(rel, lm.group(3)), style="ListText", ind=360 + 360 * depth)
            i += 1
            continue
        if st.startswith(">"):
            doc.para(doc.inline(rel, st.lstrip("> ")), style="Quote")
            i += 1
            continue
        buf = [st]
        i += 1
        while i < n and lines[i].strip() and not re.match(r"^\s*(#{1,6}\s|```|~~~|\||[-*+]\s|\d+[.)]\s|>)", lines[i]):
            buf.append(lines[i].strip())
            i += 1
        doc.para(doc.inline(rel, " ".join(buf)))


STYLES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:cs="Calibri"/><w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr></w:rPrDefault>
<w:pPrDefault><w:pPr><w:spacing w:after="80" w:line="252" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>
<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/></w:style>
<w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:basedOn w:val="Normal"/><w:pPr><w:spacing w:after="240"/></w:pPr><w:rPr><w:b/><w:sz w:val="48"/></w:rPr></w:style>
%s
<w:style w:type="paragraph" w:styleId="TOCHeading"><w:name w:val="TOC Heading"/><w:basedOn w:val="Heading1"/></w:style>
<w:style w:type="paragraph" w:styleId="Code"><w:name w:val="Code"/><w:basedOn w:val="Normal"/><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/><w:shd w:val="clear" w:color="auto" w:fill="F2F2F2"/></w:pPr><w:rPr><w:rFonts w:ascii="Consolas" w:hAnsi="Consolas" w:cs="Consolas"/><w:sz w:val="16"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="TableText"><w:name w:val="Table Text"/><w:basedOn w:val="Normal"/><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/></w:pPr><w:rPr><w:sz w:val="16"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="ListText"><w:name w:val="List Text"/><w:basedOn w:val="Normal"/><w:pPr><w:spacing w:after="40"/></w:pPr></w:style>
<w:style w:type="paragraph" w:styleId="Quote"><w:name w:val="Quote"/><w:basedOn w:val="Normal"/><w:pPr><w:ind w:left="567"/></w:pPr><w:rPr><w:i/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Caption"><w:name w:val="Caption"/><w:basedOn w:val="Normal"/><w:rPr><w:i/><w:color w:val="595959"/><w:sz w:val="16"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Spacer"><w:name w:val="Spacer"/><w:basedOn w:val="Normal"/><w:pPr><w:spacing w:after="60"/></w:pPr><w:rPr><w:sz w:val="8"/></w:rPr></w:style>
<w:style w:type="character" w:styleId="Hyperlink"><w:name w:val="Hyperlink"/><w:rPr><w:color w:val="0563C1"/><w:u w:val="single"/></w:rPr></w:style>
<w:style w:type="table" w:styleId="DocTable"><w:name w:val="Doc Table"/><w:tblPr><w:tblBorders>
<w:top w:val="single" w:sz="4" w:space="0" w:color="A6A6A6"/><w:left w:val="single" w:sz="4" w:space="0" w:color="A6A6A6"/>
<w:bottom w:val="single" w:sz="4" w:space="0" w:color="A6A6A6"/><w:right w:val="single" w:sz="4" w:space="0" w:color="A6A6A6"/>
<w:insideH w:val="single" w:sz="4" w:space="0" w:color="A6A6A6"/><w:insideV w:val="single" w:sz="4" w:space="0" w:color="A6A6A6"/></w:tblBorders>
<w:tblCellMar><w:left w:w="57" w:type="dxa"/><w:right w:w="57" w:type="dxa"/></w:tblCellMar></w:tblPr></w:style>
</w:styles>"""

HEADING = ('<w:style w:type="paragraph" w:styleId="Heading%d"><w:name w:val="heading %d"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/>'
           '<w:pPr><w:keepNext/><w:spacing w:before="%d" w:after="80"/><w:outlineLvl w:val="%d"/></w:pPr>'
           '<w:rPr><w:b/><w:color w:val="1F3864"/><w:sz w:val="%d"/></w:rPr></w:style>')

CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
<Override PartName="/word/settings.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"/>
<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
</Types>"""

RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
</Relationships>"""

DOC_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/settings" Target="settings.xml"/>
</Relationships>"""

SETTINGS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:settings xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:updateFields w:val="true"/><w:defaultTabStop w:val="360"/></w:settings>"""

CORE = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/"
 xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<dc:title>%s</dc:title><dc:creator>build_docx.py</dc:creator>
<dcterms:created xsi:type="dcterms:W3CDTF">%s</dcterms:created></cp:coreProperties>"""


def page_order(out_dir):
    rels = []
    for d, dirs, files in os.walk(out_dir):
        for fn in files:
            if fn.lower().endswith(".md"):
                rels.append(os.path.relpath(os.path.join(d, fn), out_dir).replace("\\", "/"))

    def key(rel):
        parts = rel.split("/")
        name = parts[-1][:-3].lower()
        return [p.lower() for p in parts[:-1]] + ["" if name in ("readme", "index") else name]
    return sorted(rels, key=key)


def main(argv):
    if len(argv) < 3:
        raise SystemExit(__doc__)
    out_dir, docx = argv[1], argv[2]
    title = argv[argv.index("--title") + 1] if "--title" in argv else "Application documentation"
    date = argv[argv.index("--date") + 1] if "--date" in argv else time.strftime("%d %B %Y")
    pages = page_order(out_dir)
    doc = Doc(out_dir, pages)
    doc.para(doc.run(title), style="Title")
    doc.para(doc.run("Document date: %s." % date))
    doc.para(doc.run("This document contains the full text of all %d Markdown pages under " % len(pages)) + doc.run(out_dir.replace("\\", "/"), code=True) +
             doc.run(", in folder order. Nothing is summarised. Links between pages are internal links. Source references keep the "
                     "path:line form of the pages. Mermaid diagrams are shown as their source text."))
    doc.para(doc.run("Contents"), style="TOCHeading", page_break=False)
    doc.body.append('<w:p><w:r><w:fldChar w:fldCharType="begin"/></w:r><w:r><w:instrText xml:space="preserve"> TOC \\o "1-2" \\h \\z \\u </w:instrText></w:r>'
                    '<w:r><w:fldChar w:fldCharType="separate"/></w:r><w:r><w:t>Right-click and choose Update Field to build the table of contents.</w:t></w:r>'
                    '<w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>')
    last_group = None
    for rel in pages:
        parts = rel.split("/")
        group = parts[0] if len(parts) > 1 else None
        if group and group != last_group:
            doc.para(doc.run("Folder " + group), style="Heading1", page_break=True, keep=True)
        last_group = group
        convert_page(doc, rel, read(os.path.join(out_dir, rel)), 1 if group else 0, doc.page_bm[rel], not group)
    body = "".join(doc.body)
    document = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
                'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><w:body>%s'
                '<w:sectPr><w:pgSz w:w="15840" w:h="12240" w:orient="landscape"/>'
                '<w:pgMar w:top="720" w:right="720" w:bottom="720" w:left="720" w:header="360" w:footer="360" w:gutter="0"/></w:sectPr>'
                '</w:body></w:document>') % body
    styles = STYLES % "\n".join(HEADING % (k, k, (360, 240, 200, 160, 120, 120)[k - 1], k - 1, (32, 28, 24, 22, 20, 20)[k - 1]) for k in range(1, 7))
    d = os.path.dirname(docx)
    if d and not os.path.isdir(d):
        os.makedirs(d)
    tmp = docx + ".tmp"
    z = zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED)
    try:
        z.writestr("[Content_Types].xml", CONTENT_TYPES)
        z.writestr("_rels/.rels", RELS)
        z.writestr("word/_rels/document.xml.rels", DOC_RELS)
        z.writestr("word/document.xml", document.encode("utf-8"))
        z.writestr("word/styles.xml", styles)
        z.writestr("word/settings.xml", SETTINGS)
        z.writestr("docProps/core.xml", CORE % (xml(title), time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())))
    finally:
        z.close()
    if os.path.exists(docx):
        os.remove(docx)
    os.rename(tmp, docx)
    sys.stdout.write("pages=%d paragraphs=%d bytes=%d path=%s\n" % (len(pages), body.count("<w:p>") + body.count("<w:p "), os.path.getsize(docx), docx))


if __name__ == "__main__":
    main(sys.argv)
