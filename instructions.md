Find below for the points that I would I want you to consider for refining the process of document geeration. Complete Code Coverage: Cursor has identified all 44 COBOL programs, but we need to ensure that the entire logic of each program is documented, not just the program summary.
Business Rules Coverage: Currently, 50 business rules are mapped to only 12 programs. Review the remaining 32 programs and identify any missing business rules, validations, calculations, and processing logic.
Copybook Coverage: Ensure all 41 copybooks are analyzed and documented, including field definitions, data structures, and their usage across programs.
JCL and Dependency Coverage: Validate that all 55 JCL jobs, program calls, file dependencies, CICS transactions, and database interactions are properly documented.
Missing Documentation: The generated artifacts refer to around 404 detailed documentation pages. Ensure the complete documentation is included in the final output, not just the summary Word/Markdown documents.
Source Code Traceability: Every documented business rule and technical flow should reference the corresponding source program, paragraph, or code location.
Coverage Validation: Introduce an automated validation script to compare the original source inventory against generated documentation and identify missing programs, paragraphs, and other components.
Cursor Execution Improvement: Instead of processing the entire repository in one go, process smaller groups of related programs using Cursor Rules/Skills and maintain checkpoints to avoid missing logic due to context limitations.
Gap Report: Generate a report showing what has been documented, what is missing, what could not be analyzed, and what requires SME clarification.
Final Acceptance: Our goal is 100% accounting of the in-scope codebase, with all relevant logic documented or explicitly marked as unresolved. We should not consider the use case complete based only on the number of generated documents.






Act as a senior mainframe architect and code-documentation engineer. Review the existing CardDemo repository, Cursor rules/skills, analysis artifacts, validation scripts, and generated documentation. Refine and execute the documentation-generation process to address all the requirements below.

1. **Complete code coverage:** Analyze all 44 COBOL programs in detail, documenting their divisions, paragraphs, sections, control flow, validations, calculations, file operations, calls, error handling, and business logic—not just summaries.

2. **Business rules coverage:** Review all 44 programs, especially the 32 programs not adequately covered by the existing 50 business rules. Extract all identifiable business rules, validations, calculations, and processing decisions. Do not assume every program contains a business rule; document its actual logic and explain when no business rules are identified.

3. **Copybook coverage:** Analyze all 41 copybooks, documenting field definitions, PIC/USAGE, lengths, OCCURS, REDEFINES, level-88 conditions, record structures, and references from programs and other copybooks.

4. **JCL and dependency coverage:** Analyze all 55 JCL jobs, including job steps, EXEC/DD statements, procedures, programs executed, input/output datasets, conditions, return codes, job dependencies, CICS transactions, database operations, and other integrations.

5. **Complete documentation outputs:** Include all detailed program, copybook, JCL, CICS, data, dependency, and workflow documentation in the final output—not only the summary DOCX or Markdown. Verify the reported 404 detailed pages against the actual files and explain any discrepancy.

6. **Source traceability:** Link every documented rule and technical flow to the actual source file, paragraph/section, job step, transaction, SQL statement, or relevant code location. Never invent line numbers or claim unsupported behavior.

7. **Automated coverage validation:** Create or improve scripts that compare the original source inventory against generated documentation. Detect missing programs, paragraphs, copybooks, JCL jobs and steps, CICS transactions, data definitions, dependencies, and source references. Produce machine-readable results and a human-readable coverage report.

8. **Incremental execution:** Improve Cursor Rules/Skills to process related programs and components in small batches. Maintain persistent checkpoints, intermediate results, and resumable progress so context limitations do not silently omit logic.

9. **Gap report:** Generate a report classifying items as documented, partially documented, missing, unanalyzed, unresolved, or requiring SME clarification. Identify conflicting definitions and ambiguous dependencies explicitly.

10. **Final acceptance:** Establish measurable coverage metrics for every in-scope component. Require every inventoried item to be documented or explicitly classified with a reason. Do not claim 100% semantic coverage merely because every file has a documentation page.

First inspect the existing repository, rules, skills, and artifacts to avoid duplicating work. Preserve the original source code. Update the rules, skills, scripts, and templates as necessary, then execute the improved workflow, validate the outputs, and regenerate the complete documentation package.

Prioritize correctness, evidence, completeness, and resumability. Do not fabricate results or mark a requirement complete without validation. Finish by reporting the files created or updated, validation results, coverage percentages, unresolved gaps, and exact locations of the complete documentation outputs.