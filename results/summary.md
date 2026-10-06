# Results — 91 current-law questions, Nylon Practitioner Rubric v1.0, judged by Kimi K3

| Rank | System | Correctness | Completeness | Helpfulness | Faithfulness | Citation grounding | Composite |
|---|---|---|---|---|---|---|---|
| 1 | Nylon (October Snapshot) | 4.46 | 4.63 | 4.85 | 4.75 | 4.67 | **4.675** |
| 2 | Anthropic Claude Fable 5.1 | 4.20 | 4.57 | 4.40 | 4.33 | 4.27 | **4.321** |
| 3 | OpenAI GPT-6 Astra | 4.08 | 4.46 | 3.81 | 4.32 | 4.41 | **4.277** |
| 4 | Anthropic Claude Opus 5.5 | 3.80 | 4.32 | 4.20 | 4.02 | 4.12 | **4.071** |
| 5 | OpenAI GPT-6 Sol | 3.78 | 4.15 | 3.47 | 3.97 | 4.11 | **3.958** |
| 6 | Google Gemini 3.1 Pro | 3.24 | 3.98 | 2.91 | 2.51 | 2.97 | **2.965** |

## Nylon minus each system (paired by question; 95% bootstrap interval)

| System | Correctness | Completeness | Helpfulness | Faithfulness | Citation grounding | Composite |
|---|---|---|---|---|---|---|
| Anthropic Claude Fable 5.1 | +0.26 [+0.04, +0.47] | +0.05 [-0.13, +0.24] | +0.45 [+0.27, +0.64] | +0.42 [+0.19, +0.66] | +0.40 [+0.23, +0.56] | +0.35 [+0.19, +0.52] |
| OpenAI GPT-6 Astra | +0.38 [+0.22, +0.54] | +0.16 [+0.04, +0.29] | +1.03 [+0.87, +1.20] | +0.43 [+0.27, +0.59] | +0.26 [+0.10, +0.44] | +0.40 [+0.29, +0.51] |
| Anthropic Claude Opus 5.5 | +0.66 [+0.44, +0.86] | +0.31 [+0.13, +0.48] | +0.65 [+0.48, +0.81] | +0.73 [+0.54, +0.93] | +0.55 [+0.38, +0.73] | +0.60 [+0.47, +0.76] |
| OpenAI GPT-6 Sol | +0.68 [+0.48, +0.87] | +0.47 [+0.34, +0.62] | +1.37 [+1.21, +1.54] | +0.78 [+0.59, +0.97] | +0.56 [+0.40, +0.71] | +0.72 [+0.60, +0.84] |
| Google Gemini 3.1 Pro | +1.22 [+1.02, +1.41] | +0.65 [+0.48, +0.81] | +1.93 [+1.75, +2.12] | +2.24 [+2.01, +2.46] | +1.70 [+1.53, +1.88] | +1.71 [+1.56, +1.85] |

## Judge consistency check: pass / borderline / fail (not part of the benchmark)

A coarse overall call the judge makes after scoring, used only to confirm its scores are coherent; see rubric/design-rationale.md section 3.

| System | Pass | Borderline | Fail |
|---|---|---|---|
| Nylon (October Snapshot) | 80 | 11 | 0 |
| Anthropic Claude Fable 5.1 | 79 | 11 | 1 |
| OpenAI GPT-6 Astra | 81 | 10 | 0 |
| Anthropic Claude Opus 5.5 | 78 | 13 | 0 |
| OpenAI GPT-6 Sol | 65 | 26 | 0 |
| Google Gemini 3.1 Pro | 21 | 63 | 7 |

## Speed and cost per answer

| System | Mean time to completion (s) | Median (s) | 90th percentile (s) | Mean cost (USD) |
|---|---|---|---|---|
| Nylon (October Snapshot) | 108 | 112 | 135 | not published |
| Anthropic Claude Fable 5.1 | 126 | 112 | 210 | 3.24 |
| OpenAI GPT-6 Astra | 106 | 84 | 201 | 0.84 |
| Anthropic Claude Opus 5.5 | 101 | 95 | 164 | 1.12 |
| OpenAI GPT-6 Sol | 98 | 103 | 139 | 0.19 |
| Google Gemini 3.1 Pro | 101 | 99 | 135 | 0.18 |
