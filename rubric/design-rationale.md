# Why the benchmark is built the way it is

The benchmark has one purpose: to grade AI tax research **the way a reviewing tax practitioner checks a draft advice**. A partner reviewing a junior's draft asks three questions:

1. Is it right, for the period the facts fix?
2. Can I check it from what is in front of me, without redoing the research?
3. Could I send it, or act on it, with only light edits?

Every element of the rubric, and every choice in how the systems were run and judged, follows from those three questions. This document explains each element, why it is there, and, where a choice can cost a system marks, why that cost reflects what a reviewer would do.

---

## 1. The reviewer's test, turned into grading standards

The judge's system prompt (`../judge/system-prompt.txt`) sets four standards before the rubric levels. Each one is what a reviewing practitioner already does.

### 1.0 The judge's role and jurisdiction line
The prompt opens by casting the judge as a senior tax lawyer grading a research assistant's answers against a reference. The rubric's opening line names three jurisdictions (New Zealand, Australia and the United Kingdom) and then tells the judge to limit itself to the jurisdictions the question set actually covers. This benchmark covers Australia only. The line names three because the rubric is intended for future New Zealand and United Kingdom runs, which have not yet been made (`../DECISIONS.md`, R15). It had no visible effect: no verdict grades any answer under another country's law (the only mentions of the UK in the verdicts concern a UK dividend in one question's facts). UK English matches Australian professional usage.

### 1.1 Verification primacy
**What it says.** A citation counts as verified only if the text the system actually retrieved contains the passage that supports the claim. Navigation menus, tables of contents, search-result teasers, and text cut off before the cited passage do not verify anything. A named authority whose text was not retrieved may be "plausibly correct", but it is unverified.

**Why.** A reviewer cannot sign off a proposition because a citation *looks* right. Models routinely cite real sections for propositions those sections do not contain, and they cite real pages they never opened. The only defensible test of "is this claim supported?" is whether the supporting words were in front of the writer. Grading against the citation label alone would reward confident-sounding references, which is exactly what a reviewer has to guard against.

**Effect on systems.** A system that cites a page it only saw as a search snippet earns less for that claim. This applies equally to every system. A reviewer would treat an unopened source the same way.

### 1.2 Claim-level anchoring
**What it says.** Each load-bearing claim must carry its citation at the claim. A bibliography at the end, or a block of sources against a whole section, does not ground individual claims, and the judge is told not to construct the mapping itself. Set-level citation caps Citation grounding at 3.

**Why.** This is how legal writing is reviewed. A reviewer checks a proposition by going from the sentence to its authority. If the draft leaves the reviewer to work out which of eight sources supports which sentence, the reviewer is doing the research again. If the judge built that mapping on a system's behalf, it would be grading the judge's research, not the system's.

### 1.3 Primary-source primacy
**What it says.** A proposition of statute law is fully grounded only in the legislation itself, with the operative words in view. ATO web pages, commentary and explanatory summaries are acceptable for practice, procedure, administrative rates and safe-harbour positions, but a statutory rule resting only on secondary material is at best partially verified. Case-law propositions need the case, or a passage quoting its holding.

**Why.** In Australian tax the Act is the law. ATO web guidance is not binding on the Commissioner, is not law, and is regularly out of date or simplified. A reviewer who sees a statutory rule supported only by an ATO web page has to go and read the section anyway. Public rulings and practical compliance guidelines are given their proper place, as the right authority for administrative positions, but they do not replace the section they interpret.

### 1.4 The practitioner standard
**What it says.** The judge grades as a reviewing partner grades a draft advice. The strongest answers:
- quote the operative words of each statutory rule from the legislation;
- lay computations out as a workings table;
- engage, and quote, the leading case where judicial authority decides the point;
- apply the law for the period the facts fix;
- assert nothing their sources do not bear out;
- close with a specific next step (the authority to read next, or the action to take).

It also says that a separate conclusion section, or writing section numbers out in prose, earns nothing by itself, and that narration of the research process counts against Correctness and Completeness.

**Why each element is there:**

| Element | Why a reviewing practitioner wants it |
|---|---|
| Operative words quoted | The reviewer can check the rule against its text on the page. A paraphrase of a section has to be checked against the section; a quotation is the check. |
| Workings table | Tax answers are often computations. A reviewer checks a computation line by line; a figure stated without its workings has to be recomputed from scratch. |
| Leading case engaged and quoted | Where a court has decided the point (e.g. capital vs revenue, ordinary income), the case is the authority, not a summary of it. |
| Law for the period the facts fix | Rates, thresholds and rules change every year. An answer correct for the wrong year is wrong. |
| Nothing beyond the sources | Unsupported assertions are the main risk in AI-drafted advice. |
| Closing next step | A draft advice is finished when it tells the reader what to do with it: the action to take, or what to read before relying on it. A reviewer sends back a draft that stops at analysis. |
| No credit for form alone | Stops a system scoring on substance for a summary heading or a citation-heavy style that adds nothing. |
| Narration counts against | "I'll research…", "Let me search…" is the writer's working diary, not advice. A junior who left it in a draft would be asked to take it out. It is also a sign the text was not edited into a deliverable. |

**Narration versus legitimate caveats.** Narration is the research process. A statement of the *limits* of the advice ("there is no authority directly on this point", "this should be confirmed against the current compilation") is a caveat, and Helpfulness levels 4 and 5 reward caveats a professional would want. The judge does not always draw this line cleanly. In a number of answers it treated statements such as "I did not re-read those provisions" as narration. Those statements tell the reviewer the writer did not check something, which a reviewer would treat as a defect in the draft, but the distinction is worth recording.

**The ladder rule.** An answer reaches a level only when it meets everything that level describes, and a trait a level names is required at that level and above. This mirrors review: a draft that is excellent but leaves out the statutory text is not ready to send, however good the rest is.

**"5 means nothing a reviewing partner would change."** Without this anchor, judges compress towards 4–5 and the scale stops discriminating.

**How the systems' answers compare on these traits.** Nylon's output format already had these traits when the rubric was written; the rubric (v1.0, the first version) was written independently, from practitioners' account of what they value.

The comparison systems were given no instructions (§4.3), so none was told these traits are rewarded. The authors' view is that the overlap is correlation, not causation: Nylon's product and the rubric each identified the same practitioner needs. The traits matter most at the top of each ladder: Nylon's answers scored Correctness 5 in 62% of questions against 2–40% for the others, while at Correctness 4 or above Nylon and GPT-6 Astra tie (92%), and at 3 or above Fable, Astra and Opus are higher (97%, 98% and 95% against 92%; significantly so only for Astra).

---

## 2. The five dimensions and their levels

### 2.1 Correctness (15%)
| Level | Meaning | Reasoning |
|---|---|---|
| 1 | Wrong conclusion, or a rule that contradicts the reference | Advice that would mislead the client. |
| 2 | Material error; superseded law or the wrong period's figures where it matters; statutory rules stated only through secondary material; or a load-bearing claim the sources do not support | Each of these would make a reviewer stop and redo the work. A rule stated only from an ATO page sits here because the reviewer cannot yet rely on it (§1.3). |
| 3 | Right direction and current, statutory rules stated from the legislation, minor imprecision | Usable with correction. |
| 4 | Right conclusions and sections for the period, rules from the legislation, every claim borne out, no narration | What a reviewer would expect from a competent draft. |
| 5 | As 4, with the operative words of each load-bearing rule quoted and figures right throughout | Nothing to change. |

**Why only 15%.** In professional use a correct conclusion that cannot be verified is worth little: the reviewer still has to do the research to know it is correct. Correctness is also partly enforced through Faithfulness and Citation grounding, because a wrong claim cannot be verified by its sources, so weighting it more heavily on its own would count the same error twice.

### 2.2 Completeness (10%)
Levels run from "misses nearly all key points" (1) to "every key point, condition, exception and qualification in the reference; every computation shown as workings; the leading judgment engaged and quoted where it decides the point" (5). Level 3 requires the judicial authority to be at least referred to; level 4 requires the leading judgment to be engaged and quoted.

**Why.** Tax answers fail in practice through omitted conditions and exceptions more often than through wrong headline conclusions. The reference answer is the checklist. The case-law requirement reflects that many CPA questions turn on judge-made tests, where a reviewer expects the governing case.

### 2.3 Faithfulness (30%)
Levels are bands of the share of load-bearing claims anchored at the claim and verified from captured text: under 25% (1), 25–49% (2), 50–74% (3), 75–94% (4), 95%+ (5). From level 3 up, the operative words of the governing legislation (or of the governing professional standard or code, for ethics questions) must be set out verbatim.

**Why percentages.** Faithfulness is a count-like property: what proportion of the answer can be trusted without independent research. Fixed bands make the judge count rather than impress.

**Why verbatim words at level 3.** Without the governing words on the page, the reader has to take the rule on trust, and that is the failure this dimension measures. The professional-standard alternative exists because ethics questions turn on APES 110 / APES 220 and the Code of Professional Conduct, not on an Act.

**Level 5 test.** "A reviewer could audit the whole answer without leaving the page." That is the purpose of the benchmark stated as a level.

### 2.4 Helpfulness (10%)
| Level | Meaning |
|---|---|
| 1 | Does not usefully address the question |
| 2 | Hard to use professionally: off-point, consumer-grade, or lacking the working, the statutory text or the next step |
| 3 | Has the working elements of professional advice (statutory words, workings table for any computation, a concrete closing next step) but is off-point in parts, disorganised or mis-pitched |
| 4 | Has those elements and answers well; minor issues; relevant caveats not held against it |
| 5 | Has those elements; answers for the period in issue; tight, professionally pitched, with the caveats a professional wants; no padding |

**Why the "working elements" gate at level 3.** Helpfulness measures whether the answer can be used as professional advice, which is different from whether it reads well. An answer without the statutory text, without workings for its figures, or without a next step is consumer-grade, however clearly written, because the professional still has to supply those parts.

**On the closing next step specifically.** This is a format requirement any system can meet, and a reviewer expects it. It is the most contestable gate in the rubric. The rubric asks for a concrete closing action (the authority to read next or the action to take), not for a heading or label; an answer that ends with practical advice can meet it. It carries 10% weight, and the sensitivity check in §5 shows the ranking does not depend on it.

### 2.5 Citation grounding (35%)
Levels run from "nothing can be audited" (1), through "few claims auditable" (2) and "key claims cite relevant authority but set-level, unverified, or secondary where the statute was needed; a strong bibliography is capped here" (3), to "densely anchored, mostly verified primary text" (4) and "every material claim anchored to verifying captured text, statutes grounded in their own words, no irrelevant citations" (5).

**Why it carries the most weight.** Faithfulness asks "what share of the answer is supported?". Citation grounding asks "is the source set itself the right authority, used properly?". Together they measure the property that decides whether AI research saves a practitioner time: whether its output can be checked rather than redone. That is the central claim the benchmark tests, so it carries the central weight. Dense citation is explicitly *not* penalised when each citation is anchored and verified; only irrelevant, unverified or unsupportive citations count against an answer.

### 2.6 Weights
Composite = 35% citation grounding + 30% faithfulness + 15% correctness + 10% completeness + 10% helpfulness. The weights encode the benchmark's thesis: **for a reviewing practitioner, an answer that cannot be verified cannot be relied on**, so verification carries 65%. The composite is computed by `../scripts/score.py`, not by the judge, so the judge never sees the weights' effect.

---

## 3. The judge's pass / borderline / fail verdict, and why the benchmark ignores it

The judge's output schema (`../judge/output-schema.json`) ends with a `verdict` field: **pass** = usable as-is; **borderline** = usable with edits; **fail** = wrong or misleading. It is not part of the benchmark and does not enter the composite. Its counts are shown in `../results/summary.md` only as a check on the judge.

**What it is for.** The verdict is a sanity check that the judge was reviewing appropriately. After scoring five dimensions in detail, the judge commits to a plain overall call. If that call disagreed with its own scores (a "pass" on an answer it scored as wrong, or a "fail" on one it scored highly), the detailed scores could not be trusted. Across all 546 verdicts it agrees with them:

| Verdict | Answers | Mean composite | Correctness scores |
|---|---|---|---|
| Pass | 404 | 4.41 | all 3 or above |
| Borderline | 134 | 3.03 | mostly 2–4 |
| Fail | 8 | 2.48 | 7 of 8 at 2 or below |

**Why it is not the measure.** It has none of what makes the rubric a practitioner's review:
- **No levels and no criteria.** The rubric gives each dimension five defined levels tied to the reviewer's standards (§1–§2). The verdict has a one-line description and nothing else, so it records the judge's impression, not a graded assessment.
- **No nuance.** Three bins cannot separate answers a reviewer would treat very differently. "Pass" covers answers with composites from 2.95 to 5.00: an answer whose claims a reviewer can verify on the page, and one the reviewer must re-research before relying on it, both land in it.
- **No practitioner insight.** "Usable with edits" does not say whether the edits are a typo or a day of research, whether the authority is the Act or an ATO web page, or whether the computation can be followed. Those are exactly the questions a reviewing practitioner asks, and they are what the five dimensions measure.

A benchmark that reported the verdict as its result would be ranking systems on the judge's least-informed output. It is published so that anyone can confirm the judge's detailed scores are coherent, which they are.

---

## 4. How the systems were run and judged

### 4.1 Questions and references
**Choice.** The 120 end-of-module review questions in *CPA Program Australia Taxation* (6th edn, 2023), with their back-of-book answers as references.

**Why.** They are written by the profession to test what a practitioner must know, they span the syllabus, and they come with expert answers fixed in advance by someone other than the benchmark's authors. Writing our own questions would invite the criticism that they were chosen to suit one system.

**Fingerprints.** The text is copyright, so each item is published as a SHA-256 fingerprint of the exact text used. The text was transcribed by a language model from the PDF's text layer, so a re-transcription may differ in whitespace or punctuation. The fingerprints confirm the items against this transcription, not against an independent one.

### 4.2 Current law, and the 29 exclusions
**Choice.** Only questions whose reference answer still holds under the law at the run date are kept, and each answer is graded against that reference. Two screens were applied to the questions and references alone: 21 questions where the law has since changed materially, and 8 where the reference answer is wrong under the law it applies (`../questions/excluded.md`, each with the authority).

**Why.** A practitioner advises on today's law. The alternative was to grade every answer under 2022–23 law, the period the references apply, which would keep all 120 questions. Current law was chosen because that is what a practitioner advises on, and because systems that research live sources naturally answer under current law: grading them against a 2022–23 reference would mark them down for being right today. Once the current-law test is chosen, a reference that is out of date, or wrong, would penalise the correct answer. Rewriting those references would mean the benchmark's authors writing the gold answers, so they were excluded instead, and every remaining reference is the publisher's own.

**Consequence.** Most law-changed exclusions involve rates, thresholds and caps, so the graded set leans towards doctrine more than the full book does (module 4, individuals, keeps 6 questions).

### 4.3 The systems
Each system received the question text alone: no system prompt, instructions or examples were given to any system, Nylon included, so no system was told what the rubric rewards. The comparison systems used each provider's API with the same web-search and page-reading tools, so differences reflect the model, not the tools. OpenAI's API limits tool calls to 20 per request, so GPT-6 Astra and GPT-6 Sol could make at most 20 per question; Gemini 3.1 Pro, Claude Fable 5.1 and Claude Opus 5.5 had no ceiling (Fable's and Opus's maximums were 30 and 29 calls). GPT-6 Sol reached the ceiling on 52 of 91 questions and Astra on 7, so Sol's score may understate what it would achieve without one. Nylon has no ceiling (its maximum was 28 calls). Nylon was run as its standard service and treated as a black box: only its answer and the sources it cited were used. Running Nylon as a product and the comparison systems as their providers' models is deliberate (register S2). Each provider trains its model to a default answer format, and that default is what a practitioner receives unless they write their own instructions, so output format is part of what is being compared. Formatting matters to the practitioner: draft advice that does not set out the statutory words, the workings, the leading case and a next step has to be reworked before it can be checked or sent (§1.4). In the authors' view, generic model output does not present research the way a practitioner needs, and producing that format is part of what a specialist product does. Giving the comparison systems instructions written to match Nylon's format would test a product the authors built, not the providers' models. Each system answered each question once, as a practitioner would ask once.

### 4.4 What the judge sees as each system's sources
**Choice.** For each cited source the judge sees the text **that system actually retrieved**, unedited: a library passage where that is what the system retrieved, the page text where the system opened a web page, and, clearly labelled as such, only the search snippet where the system cited a page it never opened.

**Why.** Verification primacy (§1.1) is only meaningful if the evidence is what the system really had. Cleaning, trimming or re-fetching sources on a system's behalf would mean the benchmark doing the system's research for it, and would grade the cleaned version, not the system. Showing the snippet label is simply accurate: the system did not read that page.

**Consequence.** Systems present evidence differently. A passage-level retrieval shows the judge exactly the cited passage; a full web page puts it among navigation text, which the judge must search past. The judge is instructed to verify any passage that is present, wherever it appears, and full-page captures were not penalised for their length: answers with the largest captures scored above their system's average. Where a system cited material from its own retrieval store rather than a public web address, the folder publishes the exact text the judge saw, so the judge's reading can be checked, but a reader cannot re-fetch that source from a URL.

### 4.5 Progress messages
For Claude Fable 5.1 and Claude Opus 5.5, the harness captured the progress messages the model writes between tool calls together with its answer. These were removed before grading so that neither system was penalised for text that is not part of its answer. The removal was automatic and imperfect: in about a dozen answers it left research narration at the start, or cut the opening of the answer and left a stray formatting fragment (Fable: q1.15, q2.4, q2.9, q2.11, q2.27, q3.5, q4.7, q5.4, q5.6, q5.10, q5.17; Opus: q1.3). Those answers were graded as they stand in `../responses/`. Excluding those 12 questions for every system, Nylon's composite is 4.657 and Fable's 4.392 (published 4.675 and 4.321), so Nylon's lead over Fable narrows from 0.35 to 0.27 and the ranking is unchanged (`../scripts/checks.py`).

### 4.6 The judge
**Choice.** Kimi K3 (Moonshot AI), via OpenRouter, one call per answer, not told which system wrote it, never seeing other systems' answers, with a strict JSON schema in which each score is preceded by its justification.

**Why.** The judge comes from a developer whose models are not among those tested, so no tested developer's model grades its own family's work. One call per answer, without the system's name, means a verdict cannot be influenced by comparison or by order. The judging is not blind in effect, though: Nylon's sources are library extracts with labels such as "Primary Legislation · dated 2009-01-01 · s90-5", while every comparison system's are web addresses with page captures, so the judge could tell Nylon's answers apart. The presentation was kept because it is what a practitioner sees from each system (§4.4). No judge output names Nylon. Justification-before-score makes the judge commit to its reasons, and publishes them so every score can be challenged. Calls used the model's default temperature and reasoning settings. Each answer was judged once, so per-question scores carry judge noise; the paired bootstrap intervals in `../results/summary.md` reflect variation across questions, not repeated judging.

---

## 5. Sensitivity of the ranking to the weights

The weights encode a view (§2.6), so it matters whether the ranking depends on them. Recomputed from `../verdicts/`:

| System | Published composite | Equal weights | Correctness + completeness only |
|---|---|---|---|
| Nylon (October Snapshot) | 4.675 | 4.67 | 4.54 |
| Anthropic Claude Fable 5.1 | 4.321 | 4.35 | 4.38 |
| OpenAI GPT-6 Astra | 4.277 | 4.22 | 4.27 |
| Anthropic Claude Opus 5.5 | 4.071 | 4.09 | 4.06 |
| OpenAI GPT-6 Sol | 3.958 | 3.90 | 3.97 |
| Google Gemini 3.1 Pro | 2.965 | 3.12 | 3.61 |

The first place holds under each weighting. The margin is largest under the published weights, which put most weight on verification.

Paired 95% intervals for Nylon's lead over the runner-up, Claude Fable 5.1 (same method as `../results/summary.md`; every system in `../scripts/checks.py`):

| Weighting | Nylon minus Fable |
|---|---|
| Published | +0.35 [+0.19, +0.52] |
| Equal weights | +0.32 [+0.16, +0.48] |
| Correctness only | +0.26 [+0.04, +0.47] |
| Correctness + completeness only | +0.18 [−0.004, +0.36] |

On correctness and completeness alone, the interval includes zero: on that weighting Nylon's lead over Fable is not statistically clear. Both ladders still include format requirements (§1.4).
