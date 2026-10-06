# Design decisions: Judge model, prompt and settings

One line per decision that applies to this folder. The full justification, known cost and source for each is in the register, [`../DECISIONS.md`](../DECISIONS.md), under the same id.

| # | Decision | Justification | Status |
|---|---|---|---|
| R15 | Rubric opening names NZ, AU and UK | Written for future use: NZ and UK runs are planned but have not been made, and the line tells the judge to limit itself to the jurisdictions the question set covers | Documented |
| G1 | Judge from a developer with no tested model | No tested developer's model grades its own family's work. Nylon's October Snapshot does not use Kimi K3 | Documented |
| G2 | Kimi K3 specifically, among such models | The largest available model with the strongest reasoning-benchmark results at the time of the run, among models not tested in the benchmark | Documented |
| G3 | Judge not told which system wrote each answer; one answer per call; no other systems' answers | A verdict cannot be influenced by comparison or order; and one answer per call keeps the judge's context short, which avoids degraded accuracy over long contexts. The difference in how sources are presented (next column) is kept because it reflects what a practitioner sees from each system | Documented |
| G4 | Justification before each score; strict JSON schema | The judge commits to its reasons, which are published so every score can be challenged | Documented |
| G5 | One judge call per answer at default temperature | Repeated judging was not run, for cost and time reasons | Documented |
| G6 | No human-graded calibration set | Resources were not available for practitioner grading, and the authors have high confidence in the reference answers | Documented |
| G7 | Pass / borderline / fail verdict kept out of the composite | The verdict has no levels or criteria; it is a coherence check on the detailed scores | Documented |
| G8 | Judge models and judging runs tried before this one | No other judge models were tested, and judging with Kimi K3 was run once: no judging run was made and set aside. Judging several times and averaging was too expensive (see G5). The rubric has not been used to grade any other run (NZ and UK runs are planned but have not been made) | Documented |
| G9 | Same system prompt for every judge call | Every call used `judge/system-prompt.txt`; Kimi K3's context window is large, and the authors do not believe any input was cut | Documented |
