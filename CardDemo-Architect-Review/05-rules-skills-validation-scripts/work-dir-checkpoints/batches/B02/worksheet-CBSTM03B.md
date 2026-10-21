# Worksheet CBSTM03B (app/cbl/CBSTM03B.CBL)

Lines: 230. Paragraphs: 14. Decision points: 18 (business candidates: 18).

Fill `docs/_work/semantic/programs/CBSTM03B.json`. Read the whole source; this list only indexes it.

## Paragraphs

| Paragraph | Lines | Performs | Performed by |
|---|---|---|---|
| 0000-START | 116-128 | 1000-TRNXFILE-PROC, 2000-XREFFILE-PROC, 3000-CUSTFILE-PROC, 4000-ACCTFILE-PROC |  |
| 9999-GOBACK | 130-131 |  | 0000-START |
| 1000-TRNXFILE-PROC | 133-149 |  | 0000-START |
| 1900-EXIT | 151-152 |  | 0000-START, 1000-TRNXFILE-PROC |
| 1999-EXIT | 154-155 |  | 0000-START |
| 2000-XREFFILE-PROC | 157-173 |  | 0000-START |
| 2900-EXIT | 175-176 |  | 0000-START, 2000-XREFFILE-PROC |
| 2999-EXIT | 178-179 |  | 0000-START |
| 3000-CUSTFILE-PROC | 181-198 |  | 0000-START |
| 3900-EXIT | 200-201 |  | 0000-START, 3000-CUSTFILE-PROC |
| 3999-EXIT | 203-204 |  | 0000-START |
| 4000-ACCTFILE-PROC | 206-223 |  | 0000-START |
| 4900-EXIT | 225-226 |  | 0000-START, 4000-ACCTFILE-PROC |
| 4999-EXIT | 228-229 |  | 0000-START |

## Decision points that look like business logic

Each line below must fall inside a rule `source` range or a `no_rule_decisions` range.

| Line | Paragraph | Type | Condition |
|---|---|---|---|
| 118 | 0000-START | EVALUATE | `LK-M03B-DD` |
| 119 | 0000-START | WHEN | `'TRNXFILE'` |
| 121 | 0000-START | WHEN | `'XREFFILE'` |
| 123 | 0000-START | WHEN | `'CUSTFILE'` |
| 125 | 0000-START | WHEN | `'ACCTFILE'` |
| 127 | 0000-START | WHEN | `OTHER` |
| 135 | 1000-TRNXFILE-PROC | IF | `M03B-OPEN` |
| 140 | 1000-TRNXFILE-PROC | IF | `M03B-READ` |
| 146 | 1000-TRNXFILE-PROC | IF | `M03B-CLOSE` |
| 159 | 2000-XREFFILE-PROC | IF | `M03B-OPEN` |
| 164 | 2000-XREFFILE-PROC | IF | `M03B-READ` |
| 170 | 2000-XREFFILE-PROC | IF | `M03B-CLOSE` |
| 183 | 3000-CUSTFILE-PROC | IF | `M03B-OPEN` |
| 188 | 3000-CUSTFILE-PROC | IF | `M03B-READ-K` |
| 195 | 3000-CUSTFILE-PROC | IF | `M03B-CLOSE` |
| 208 | 4000-ACCTFILE-PROC | IF | `M03B-OPEN` |
| 213 | 4000-ACCTFILE-PROC | IF | `M03B-READ-K` |
| 220 | 4000-ACCTFILE-PROC | IF | `M03B-CLOSE` |

## Calculations

