# Design decisions: Question set, reference answers and exclusions

One line per decision that applies to this folder. The full justification, known cost and source for each is in the register, [`../DECISIONS.md`](../DECISIONS.md), under the same id.

| # | Decision | Justification | Status |
|---|---|---|---|
| Q1 | Use the 120 end-of-module review questions in *CPA Program Australia Taxation* (6th edn, 2023), with the back-of-book answers as references | Written by the profession to test what a practitioner must know; span the syllabus; reference answers fixed in advance by someone other than the benchmark's authors, so the questions cannot have been chosen to suit any system | Documented |
| Q2 | Publish SHA-256 fingerprints, and the text only in encrypted form | The text is the publishers' copyright; fingerprints let anyone holding the book confirm the items, and the encrypted text (P5) can be released if CPA Australia permits | Documented |
| Q3 | Transcribe by language model from the PDF text layer, with no manual editing | No manual editing means the authors did not alter any question or reference | Documented |
| Q4 | Keep only questions whose reference answer still holds under the law in force at the run date (October 2026); grade each answer against that reference | A practitioner advises on today's law; systems that research live sources answer under current law and would be marked down for being right today | Documented |
| Q5 | Exclude 21 questions where the law has changed materially | Once the current-law test is chosen, an out-of-date reference would penalise the correct answer; rewriting it would mean the authors writing gold answers | Documented |
| Q6 | Exclude 8 questions where the reference is wrong under the law it applies | Grading against a wrong reference penalises the correct answer; correcting it would mean the authors writing gold answers | Documented, except as Q7 |
| Q7 | Who confirmed the 8 incorrect references | Confirmed by Claude Fable 5.1 and Claude Opus 5.5, each checking the authors' reading against the primary sources cited in excluded.md §B | Documented |
| Q8 | Exclusions fixed before any system was run | The references were checked for accuracy by Claude Fable 5.1 and Claude Opus 5.5 during extraction of the questions, and the exclusions were identified then, on the questions and references alone. None of the 29 excluded questions was run on any system | Documented |
| Q9 | Whether any of the 120 questions were used in developing Nylon | None of the 120 CPA questions, or their answers, were used in fine-tuning or developing Nylon. Nylon's precedent system was turned off for the run | Documented |
| P5 | Encrypt the questions and reference answers (`questions/questions.jsonl`) and the systems' answers (`responses/`, and the candidate-answer section of `judge-inputs/`); key on request from benchmark@usenylon.com, given an agreement not to use it to compete with CPA Australia | The questions and answers are, or may contain, copyrighted CPA Program material. CPA Australia has been asked for permission to release the questions; if it is granted, the questions and answers will be decrypted | Documented |
