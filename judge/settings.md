# How each answer is judged

- **Judge model:** Kimi K3 (`moonshotai/kimi-k3`, Moonshot AI), via OpenRouter. The judge is from a different developer from every system tested.
- **One call per answer.** The judge grades a single answer against the reference answer. It is not told which system wrote the answer and never sees other systems' answers.
- **Messages:** one system message (`system-prompt.txt`, rendered from `../rubric/nylon-practitioner-rubric-v1.0.json`) and one user message (template below). No tools, no prior turns, no examples.
- **Output:** strict JSON schema (`output-schema.json`): for each of the five dimensions, a justification and then an integer score from 1 to 5, followed by a one-line summary and a pass / borderline / fail verdict.
- **Settings:** maximum output 16,384 tokens (40,000 for a few long verdicts); the model's default temperature and reasoning settings.
- **Composite score:** the weighted mean of the five dimension scores, computed afterwards (not by the judge): citation grounding 35%, faithfulness 30%, correctness 15%, completeness 10%, helpfulness 10%.

## User message template

```text
QUESTION:
{question}

GOLD ANSWER (reference):
{reference answer}

CANDIDATE ANSWER (to grade):
{the system's answer, with its citations renumbered as [[1]], [[2]], …}

CANDIDATE CITED SOURCES ({n}):
{for each cited source: number, title, type, date, and the text the system actually retrieved for it}

Grade the candidate answer against the reference now.
```

The cited-sources list shows the text each system actually retrieved (a library passage or the web page it read), so faithfulness and citation grounding are judged against what the system saw, not against what a citation claims. The exact user message sent for every answer, and the judge's full output, are in `../judge-inputs/`.
