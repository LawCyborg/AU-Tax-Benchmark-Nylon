# Design decisions: Rubric and weights

One line per decision that applies to this folder. The full justification, known cost and source for each is in the register, [`../DECISIONS.md`](../DECISIONS.md), under the same id.

| # | Decision | Justification | Status |
|---|---|---|---|
| R1 | Origin of the rubric | Developed from conversations with five or more Nylon customers about what they value in research advice, and written by an independent contractor. Customer identities are confidential and are not disclosed. v1.0 is the first version of the rubric. Nylon's output format predates the rubric; the rubric was created independently of it, and Nylon's answers are known for ending with follow-on steps. The authors' view of any overlap between Nylon's format and the rubric is that it is coincidence, not causation: Nylon's product and the rubric each identified the same practitioner needs from practitioner insight | Documented |
| R2 | Grade as a reviewing partner grades a draft advice | The benchmark's purpose: whether AI research saves a practitioner time depends on whether its output can be checked and sent, not only whether it is right | Documented |
| R3 | Verification primacy: a citation counts only if the retrieved text contains the supporting passage | Models cite real sections for propositions they do not contain, and pages they never opened; the only defensible test is whether the supporting words were in front of the writer | Documented |
| R4 | Claim-level anchoring; set-level citation caps Citation grounding at 3 | A reviewer checks a proposition by going from the sentence to its authority; a judge that built the mapping would be grading its own research | Documented |
| R5 | Primary-source primacy for statutory propositions | In Australian tax the Act is the law; ATO web guidance is not binding, not law, and often simplified or out of date | Documented |
| R6 | Quote operative statutory words | A quotation is the check; a paraphrase must itself be checked against the section | Documented |
| R7 | Workings table for computations | A reviewer checks a computation line by line; a figure without workings must be recomputed | Documented |
| R8 | Engage and quote the leading case | Where a court has decided the point, the case is the authority | Documented |
| R9 | Closing next step required for Helpfulness ≥3 | A draft advice is finished when it tells the reader what to do with it | Documented |
| R10 | Narration counts against Correctness and Completeness | Research narration is the writer's working diary, not advice; a reviewer would ask for it to be removed | Documented |
| R11 | Ladder rule: a level requires everything it names | Mirrors review: an excellent draft without the statutory text is not ready to send | Documented |
| R12 | "5 means nothing a reviewing partner would change" | Without the anchor, judges compress towards 4–5 | Documented |
| R13 | Faithfulness levels as percentage bands | A count-like property; fixed bands make the judge count | Documented |
| R14 | Weights 35 / 30 / 15 / 10 / 10 | An answer that cannot be verified cannot be relied on, so verification carries 65%; Correctness is partly enforced through Faithfulness and Citation grounding already | Documented; sensitivity in §5 |
| R15 | Rubric opening names NZ, AU and UK | Written for future use: NZ and UK runs are planned but have not been made, and the line tells the judge to limit itself to the jurisdictions the question set covers | Documented |
