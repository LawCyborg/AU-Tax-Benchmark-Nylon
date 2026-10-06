# Design decisions: What the judge saw as each system's sources

One line per decision that applies to this folder. The full justification, known cost and source for each is in the register, [`../DECISIONS.md`](../DECISIONS.md), under the same id.

| # | Decision | Justification | Status |
|---|---|---|---|
| J1 | Show the judge the text each system actually retrieved, unedited | Verification primacy is meaningful only if the evidence is what the system had; cleaning or re-fetching would grade the benchmark's research, not the system's | Documented |
| J2 | Full-page captures not trimmed | As J1 | Documented |
| J3 | Accept citations to a system's private retrieval store, with no public address | Nylon subscribers can retrieve each cited extract from Nylon's library by its identifier and reproduce what the judge saw | Documented |
| P5 | Encrypt the questions and reference answers (`questions/questions.jsonl`) and the systems' answers (`responses/`, and the candidate-answer section of `judge-inputs/`); key on request from benchmark@usenylon.com, given an agreement not to use it to compete with CPA Australia | The questions and answers are, or may contain, copyrighted CPA Program material. CPA Australia has been asked for permission to release the questions; if it is granted, the questions and answers will be decrypted | Documented |
