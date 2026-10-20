# Change log - final architect review pass (2026-10-20)

Changes relative to the first `CardDemo-Architect-Review.zip` (commit e27ca5c). Application source was not modified.

## Findings from the audit

| # | Finding | Resolution |
|---|---|---|
| 1 | Report copies in folders 02-04 linked to pages such as `07-programs/...` that do not exist next to the copy (broken links in the bundle) | Links in the copies now point into `01-detailed-documentation/application-documentation/`; checked by V5 |
| 2 | Two compiled Python files (`build_docx.pyc`, `batch_manager.pyc`) in the skills copy; Python 3.1 writes them beside the sources, so the `__pycache__` cleanup missed them | Removed by `prepare_review_bundle.py`; checked by V6 |
| 3 | `04-gap-report/gaps-register.md` and `16-gaps-assumptions-open-questions.md` were the same register under two names | Only `16-gaps-assumptions-open-questions.md` is kept |
| 4 | The README said "392 rules in 40 programs" without explaining 41 vs 44 copybooks, 46 vs 55 JCL members, 6 vs 7 PROC pages, 15 vs 14 unresolved, 48 vs 120 SME | Each count is recounted from source (V1) and explained in README section 4 |
| 5 | The 74 "conflicting definitions" mixed open code-vs-comment conflicts with informational DD reuse, closed rule corrections and parser reconciliation notes | Each conflict carries a kind; only 18 code-vs-comment-or-definition rows are open |
| 6 | Gap items had no impact, status, owner or next action; 13 unresolved JCL items, 24 parser notes and 2 CA7 items cited a file without a line | New gap register (`gap-register.md`, 290 rows) with evidence class, line-level source, supported impact, status, owner and next action; 0 rows without a line |
| 7 | 155 rules named no paragraph on the traceability page | The page shows the enclosing paragraph or division looked up from the cited line, marked *(derived)*; the 3 Assembler rules are labelled as such |
| 8 | Citations could only be checked with the repository at hand | `06-source-snapshot/` holds the in-scope source (sha256 matches the inventory; 226 files only after CRLF-to-LF normalisation, see #13) with the three FTP connection lines of `FTPJCL.JCL` redacted in place |
| 9 | Checks were the pipeline's own; nothing re-derived the counts independently | `verify_review_bundle.py`: 13 checks (V1-V10, V4 split into four) using its own counting (extensions, JOB cards, Area A labels), run on the folder and again on the unzipped ZIP |
| 10 | Unverified statements were described as "not used as evidence for any Confirmed fact", which no script measures | Restated as a process rule of `mainframe-doc-core.mdc` |
| 11 | `project-profile.yaml` exclude entry for `AI-Documentation-Artifacts/**` was indented under the previous item (fixed in the previous pass); the `DFHMSD` citation moved to line 117 | Kept; inventory evidence line and gaps register updated |
| 12 | The draft README said the 21 BMS symbolic-map copybooks (`app/cpy-bms`, `app/app-*/cpy-bms`) were "documented with their screens"; no screen page cites them | Not changed in the documentation. The README now says they have no page of their own and are listed with the copying program on `17-dependencies/copybook-usage.md` (checked by V1); listed as a limitation |
| 13 | The inventory sha256 values were taken on LF files; the working tree is now CRLF (`core.autocrlf=true`), so 226 files differ byte-wise | Line numbers are unaffected; V8 reports raw matches and matches after normalisation separately |
| 14 | BR-BASE-COACTUPC-007 cites `app/cpy/CSUTLDPY.cpy:273-321`, which starts 11 lines before paragraph `EDIT-DATE-LE` (line 284) | Left as is and reported as the V4c warning; the cited code is inside the range |
| 15 | `app/`, `samples/` and `scripts/` are untracked in this git repository, so commit e27ca5c does not identify the application source version | README states this; the analysed version is identified by the inventory sha256 values, checked by V8 |
| 16 | The README and gap register showed 138 open "SME clarification" items next to "120 SME questions" without saying how they relate | Recounted from the register entries: 138 = 120 SME questions (GAP-S) + 18 open code-vs-comment conflicts (GAP-C). The 120 match the semantic files one-to-one (111 written during analysis + 9 from copybook dead-code observations, 48 components). Neither count changed; the owner summaries now have a "Made up of" column, and V9 checks the breakdown and the source match |

## Scripts and skills changed

- `skills/mainframe-doc-orchestrator/scripts/gap_report.py`: gap register (`18-coverage/gap-register.md`, `register` in `gaps.json`), conflict kinds, line-level sources for JCL symbolics, parser notes and CA7 mappings, "How the counts relate" section.
- `skills/mainframe-doc-orchestrator/scripts/render_detail.py`: derived paragraph/division locations on the traceability page; repeated resolved call targets listed once.
- `docs/_work/prepare_review_bundle.py` (new): source snapshot, redaction, link repair, cleanup.
- `docs/_work/verify_review_bundle.py` (new): independent bundle verification.
- `docs/_work/write_review_readme.py` (new): architect README generated from the bundle's JSON.
- `docs/_work/build_review_bundle.ps1`: new build order, ZIP re-verification.
- `docs-toolkit/README.md`, `skills/mainframe-doc-orchestrator/SKILL.md`, `docs/_work/progress.md`: updated commands and description.
