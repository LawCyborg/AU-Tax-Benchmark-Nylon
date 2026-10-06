# Design decisions: Scoring, intervals and cost

One line per decision that applies to this folder. The full justification, known cost and source for each is in the register, [`../DECISIONS.md`](../DECISIONS.md), under the same id.

| # | Decision | Justification | Status |
|---|---|---|---|
| R14 | Weights 35 / 30 / 15 / 10 / 10 | An answer that cannot be verified cannot be relied on, so verification carries 65%; Correctness is partly enforced through Faithfulness and Citation grounding already | Documented; sensitivity in §5 |
| G7 | Pass / borderline / fail verdict kept out of the composite | The verdict has no levels or criteria; it is a coherence check on the detailed scores | Documented |
| T1 | Paired bootstrap intervals (3,000 resamples, seed 0) | Pairs by question so differences reflect the same items | Documented |
| T2 | Comparison costs from token usage, excluding web-search charges; Nylon's cost not published | Nylon's cost per answer is commercially sensitive | Documented |
| T3 | Weight sensitivity check (equal weights; correctness + completeness only) | Shows whether the ranking depends on the weights | Documented |
| P7 | Whitepaper Discussion says Nylon's answers most often earned a perfect correctness score | The authors treat a correct answer as one with a perfect Correctness score (5 out of 5). On that measure Nylon leads every system: 62% of its answers, against 40% for Claude Fable 5.1 and 2–18% for the others, with every paired 95% interval clear of zero (`scripts/checks.py` §1). The rubric was designed so that the total scores reflect each answer's value to a reviewing practitioner, not for any single lower Correctness level to be read as a separate measure of correctness. Nylon also gives an estimated certainty rating with each answer, which alerts users to likely inaccuracies | Documented |
