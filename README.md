# Nylon Australian Tax Research Benchmark — October 2026

An evaluation of AI research systems on Australian tax questions, graded against expert reference answers. To our knowledge there is no established public benchmark for AI tax research in Australia or New Zealand; this benchmark covers Australian tax.

Everything needed to check the results is in this folder: fingerprints of the questions and reference answers, the rubric, the judge's exact instructions and output schema, every system's answers, every verdict (with the judge's reasons), the exact message the judge received for each answer, and a script that recomputes every table.

## Questions
- Source: the 120 end-of-module review questions, with suggested answers, in *CPA Program Australia Taxation*, 6th edition (2023). The question text and suggested answers are the publishers' copyright and are included only in encrypted form.
- Extraction: the book's text layer was extracted locally from the PDF, sliced by module, and each module's review questions were transcribed together with their back-of-book suggested answers by a language model, then checked row by row against a fingerprint record of the extraction. No manual editing was applied.
- `questions/questions.jsonl` lists each graded question's id, module and topic, with a SHA-256 fingerprint of the exact question text and suggested answer used (UTF-8), so anyone holding the book can confirm the items match, and the question and suggested answer themselves, encrypted.
- 91 questions are graded. 29 are excluded: 21 because the law has changed since the 2022–23 reference answers, and 8 because the reference answer is incorrect under the law it applies. See `questions/excluded.md`.
- Questions were kept only where the reference answer still holds under the law in force at the run date; each answer was graded against that reference.

## Systems
| System | How it was run |
|---|---|
| Nylon (October Snapshot) | A snapshot of Nylon's standard research service, run between 28 September and 1 October 2026 |
| OpenAI GPT-6 Astra | Provider API with web search and page reading |
| Anthropic Claude Fable 5.1 | Provider API with web search and page reading |
| Anthropic Claude Opus 5.5 | Provider API with web search and page reading |
| OpenAI GPT-6 Sol | Provider API with web search and page reading |
| Google Gemini 3.1 Pro | Provider API with web search and page reading |

Each system answered each question once and received the question text alone, with no system prompt or instructions.

The comparison systems all used the same web search and page-reading tools. OpenAI's API limits tool calls to 20 per request, so GPT-6 Astra and GPT-6 Sol could make at most 20 per question. Gemini 3.1 Pro, Claude Fable 5.1 and Claude Opus 5.5 had no ceiling (Fable's and Opus's maximums were 30 and 29 calls). GPT-6 Sol reached the ceiling on 52 of 91 questions, so its score may understate what it would achieve without one; Astra reached it on 7. Nylon has no ceiling (its maximum was 28 calls). The six systems were run between 28 September and 1 October 2026. Nylon's answers were completed last, by 1 October, because of problems with the Nylon API and with capturing its sources; the systems were not re-run together. Response times depend on provider load at the time of the run. For two systems (Claude Fable 5.1 and Claude Opus 5.5) the benchmark harness captured the interim progress messages the model writes between tool calls ("I'll research…", "Let me read…") together with its answer; these progress messages were removed automatically before grading. The removal was imperfect in about a dozen answers, which still open with narration or with a stray fragment; they were graded as they stand (see `rubric/design-rationale.md` §4.5).

## Grading
- Rubric: `rubric/nylon-practitioner-rubric-v1.0.json` (five dimensions, levels 1–5). Judge: Kimi K3 (Moonshot AI), one call per answer, not told which system wrote it. Details: `judge/settings.md`.
- Composite = 35% citation grounding + 30% faithfulness + 15% correctness + 10% completeness + 10% helpfulness.
- The judge also gives each answer a pass / borderline / fail verdict. It is a consistency check on the judge, not part of the benchmark (`rubric/design-rationale.md` §3).
- Why each rubric element and design choice is as it is: `rubric/design-rationale.md`.

## Reproduce
```
python3 scripts/score.py      # rewrites results/summary.md
python3 scripts/checks.py     # prints the checks cited in DECISIONS.md and the design rationale
                              # (sections that read the answers need the key: NYLON_BENCH_KEY=<key> python3 scripts/checks.py)
NYLON_BENCH_KEY=<key> python3 scripts/answers_crypto.py   # writes decrypted copies of the answers to decrypted/
```

## Folder
| Path | Contents |
|---|---|
| `DECISIONS.md` | register of every design decision, its justification, known cost and source; each folder has a `DECISIONS.md` for its own decisions |
| `questions/` | `questions.jsonl` (ids, topics, fingerprints and the encrypted text of the 91 graded questions and reference answers), `excluded.md` |
| `rubric/` | the rubric, and `design-rationale.md` explaining each element and design choice |
| `judge/` | system prompt, output schema, call settings and user-message template |
| `responses/` | every answer (encrypted), with time to completion and cited URLs |
| `verdicts/` | every verdict: five scores with the judge's reasons, composite, summary |
| `judge-inputs/` | the exact user message the judge received for each answer (question and reference answer withheld; the candidate answer encrypted), and its raw output |
| `results/` | `summary.md`, `per-question-scores.csv`, `cost.md` |
| `scripts/` | `score.py`, `checks.py`, `answers_crypto.py` (decrypts the answers with the key) |
| `whitepaper/` | the design decisions behind the whitepaper's claims; the whitepaper itself is published separately (P2) |

> **Encrypted answers.** Due to the copyrighted nature of the benchmark questions, we have encrypted the questions and answers, as the answers may contain copyrighted material. But, we have detailed how to recreate the test, with the appropriate judging criteria. If you would like to request the key to the answers, please message benchmark@usenylon.com with your agreement to not use to compete with CPA Australia. We have reached out to CPA Australia for permission to release the questions to the public domain. We will decrypt both questions and answers if they grant us permission.
>
> The questions and reference answers (`questions/questions.jsonl`) and the systems' answers (`responses/`, and the candidate-answer section of each message in `judge-inputs/`) are encrypted with AES-256 (`scripts/answers_crypto.py` explains the format and decrypts them with the key; each decrypted question and reference answer matches its published fingerprint). Everything else, including the sources each system cited, every verdict with the judge's reasons, and every score, is in plain text.
