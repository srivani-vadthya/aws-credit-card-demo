# Worksheet PAUDBLOD (app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL)

Lines: 369. Paragraphs: 17. Decision points: 17 (business candidates: 1).

Fill `docs/_work/semantic/programs/PAUDBLOD.json`. Read the whole source; this list only indexes it.

## Paragraphs

| Paragraph | Lines | Performs | Performed by |
|---|---|---|---|
| MAIN-PARA | 169-187 | 1000-INITIALIZE, 2000-READ-ROOT-SEG-FILE, 3000-READ-CHILD-SEG-FILE, 4000-FILE-CLOSE |  |
| 1000-INITIALIZE | 190-215 | 9999-ABEND | MAIN-PARA |
| 1000-EXIT | 218-219 |  | MAIN-PARA |
| 2000-READ-ROOT-SEG-FILE | 222-237 | 2100-INSERT-ROOT-SEG | MAIN-PARA |
| 2000-EXIT | 239-240 |  | MAIN-PARA |
| 2100-INSERT-ROOT-SEG | 242-263 | 9999-ABEND | 2000-READ-ROOT-SEG-FILE |
| 2100-EXIT | 264-265 |  | 2000-READ-ROOT-SEG-FILE |
| 3000-READ-CHILD-SEG-FILE | 269-289 | 3100-INSERT-CHILD-SEG | MAIN-PARA |
| 3000-EXIT | 290-291 |  | MAIN-PARA |
| 3100-INSERT-CHILD-SEG | 292-314 | 3200-INSERT-IMS-CALL, 9999-ABEND | 3000-READ-CHILD-SEG-FILE |
| 3100-EXIT | 315-316 |  | 3000-READ-CHILD-SEG-FILE |
| 3200-INSERT-IMS-CALL | 318-336 | 9999-ABEND | 3100-INSERT-CHILD-SEG |
| 3200-EXIT | 338-339 |  | 3100-INSERT-CHILD-SEG |
| 4000-FILE-CLOSE | 341-356 |  | MAIN-PARA |
| 4000-EXIT | 357-358 |  | MAIN-PARA |
| 9999-ABEND | 360-366 |  | 1000-INITIALIZE, 2100-INSERT-ROOT-SEG, 3100-INSERT-CHILD-SEG, 3200-INSERT-IMS-CALL |
| 9999-EXIT | 368-369 |  |  |

## Decision points that look like business logic

Each line below must fall inside a rule `source` range or a `no_rule_decisions` range.

| Line | Paragraph | Type | Condition |
|---|---|---|---|
| 275 | 3000-READ-CHILD-SEG-FILE | IF | `ROOT-SEG-KEY IS NUMERIC` |

## Calculations

