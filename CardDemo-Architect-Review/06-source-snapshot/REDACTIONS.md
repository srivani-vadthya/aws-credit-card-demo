# Source snapshot

Read-only copy of 241 in-scope source and definition files from the repository, at their repository-relative paths, so that every `path:line` citation in this bundle can be opened and checked without the repository. Each file is byte-identical to the analysed source (sha256 in `../02-coverage-validation-report/inventory.json`) except the redacted lines below.

Not included (by inventory type): data-binary 14, data-text 9, diagram 12, excluded 2, placeholder 48, repo-meta 5. These are listed in the inventory and documented on their pages; they are images, binary data or test data, not code.

## Redactions

Lines replaced by `<<REDACTED: in-stream FTP connection line withheld from the review bundle>>`. The original lines hold FTP connection data (host, user id, password) and are deliberately not reproduced anywhere in the bundle. The line count is unchanged, so citations to other lines still resolve.

| File | Line |
|---|---|
| `app/jcl/FTPJCL.JCL` | 33 |
| `app/jcl/FTPJCL.JCL` | 34 |
| `app/jcl/FTPJCL.JCL` | 35 |
