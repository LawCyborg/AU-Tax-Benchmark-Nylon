# Design decisions: Scoring script

One line per decision that applies to this folder. The full justification, known cost and source for each is in the register, [`../DECISIONS.md`](../DECISIONS.md), under the same id.

| # | Decision | Justification | Status |
|---|---|---|---|
| R14 | Weights 35 / 30 / 15 / 10 / 10 | An answer that cannot be verified cannot be relied on, so verification carries 65%; Correctness is partly enforced through Faithfulness and Citation grounding already | Documented; sensitivity in §5 |
| T1 | Paired bootstrap intervals (3,000 resamples, seed 0) | Pairs by question so differences reflect the same items | Documented |
| P5 | Encrypt the questions and reference answers (`questions/questions.jsonl`) and the systems' answers (`responses/`, and the candidate-answer section of `judge-inputs/`); key on request from benchmark@usenylon.com, given an agreement not to use it to compete with CPA Australia | The questions and answers are, or may contain, copyrighted CPA Program material. CPA Australia has been asked for permission to release the questions; if it is granted, the questions and answers will be decrypted | Documented |
