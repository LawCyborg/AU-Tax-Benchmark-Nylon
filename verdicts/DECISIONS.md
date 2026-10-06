# Design decisions: Verdicts

One line per decision that applies to this folder. The full justification, known cost and source for each is in the register, [`../DECISIONS.md`](../DECISIONS.md), under the same id.

| # | Decision | Justification | Status |
|---|---|---|---|
| G3 | Judge not told which system wrote each answer; one answer per call; no other systems' answers | A verdict cannot be influenced by comparison or order; and one answer per call keeps the judge's context short, which avoids degraded accuracy over long contexts. The difference in how sources are presented (next column) is kept because it reflects what a practitioner sees from each system | Documented |
| G4 | Justification before each score; strict JSON schema | The judge commits to its reasons, which are published so every score can be challenged | Documented |
| G5 | One judge call per answer at default temperature | Repeated judging was not run, for cost and time reasons | Documented |
| G7 | Pass / borderline / fail verdict kept out of the composite | The verdict has no levels or criteria; it is a coherence check on the detailed scores | Documented |
| G9 | Same system prompt for every judge call | Every call used `judge/system-prompt.txt`; Kimi K3's context window is large, and the authors do not believe any input was cut | Documented |
| P7 | Whitepaper Discussion says Nylon's answers most often earned a perfect correctness score | The authors treat a correct answer as one with a perfect Correctness score (5 out of 5). On that measure Nylon leads every system: 62% of its answers, against 40% for Claude Fable 5.1 and 2–18% for the others, with every paired 95% interval clear of zero (`scripts/checks.py` §1). The rubric was designed so that the total scores reflect each answer's value to a reviewing practitioner, not for any single lower Correctness level to be read as a separate measure of correctness. Nylon also gives an estimated certainty rating with each answer, which alerts users to likely inaccuracies | Documented |
