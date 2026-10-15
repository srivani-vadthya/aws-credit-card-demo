# QA Checklist (Phase B)

Run `check_package.py` first (mainframe-doc-assembly-qa); then verify the
semantic items below. Record results in `16-gaps-assumptions-open-questions.md`.

## Automated (must be zero)

- [ ] Uncovered artifacts
- [ ] Broken relative links
- [ ] Leftover `{{placeholders}}` / template guide comments
- [ ] Mermaid warnings
- [ ] Documents without a Sources section

## Accuracy (sample at least 10% of each document type, minimum 3)

- [ ] Cited lines actually contain the stated logic
- [ ] Record lengths and offsets match the layout script output
- [ ] Transaction -> program mapping matches CSD
- [ ] Job step programs and DSNs match JCL
- [ ] Schedule edges match scheduler definitions
- [ ] Business rule statements match code conditions (no added meaning without Inferred tag)
- [ ] No placeholder or symbolic parameter was replaced with an invented value

## Consistency

- [ ] Same artifact named identically everywhere
- [ ] Counts in executive summary equal counts in inventory/catalogs
- [ ] Each rule referenced from its program spec(s) and vice versa
- [ ] Glossary covers every acronym used

## Readability

- [ ] Executive summary understandable without mainframe knowledge
- [ ] Each detail doc starts with purpose in plain language
- [ ] Diagrams render and are readable (split when > ~40 nodes)

## Safety

- [ ] No credentials, personal data or real card numbers reproduced (masked examples only)
- [ ] Security weaknesses described neutrally without exploit detail
