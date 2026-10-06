#!/usr/bin/env python3
"""Recompute every results table from the files in this folder (no network, standard library only).

    python3 scripts/score.py            # prints the tables and writes results/summary.md

Quality: the mean over the 91 questions (one answer per system per question).
Differences: paired by question, with a 95% bootstrap interval (3,000 resamples, seed 0).
Speed: seconds from request to the last token of the answer, over every answer.
"""
import json, os, random, statistics as S
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIMS = ['correctness', 'completeness', 'helpfulness', 'faithfulness', 'citation_grounding', 'composite']
NAMES = {'nylon-october-snapshot': 'Nylon (October Snapshot)', 'openai-gpt-6-astra': 'OpenAI GPT-6 Astra',
         'anthropic-claude-fable-5.1': 'Anthropic Claude Fable 5.1', 'anthropic-claude-opus-5.5': 'Anthropic Claude Opus 5.5',
         'openai-gpt-6-sol': 'OpenAI GPT-6 Sol', 'google-gemini-3.1-pro': 'Google Gemini 3.1 Pro'}
COST = {  # mean USD per answer; see results/cost.md for method (Nylon's cost is not published)
    'openai-gpt-6-astra': 0.836, 'anthropic-claude-fable-5.1': 3.236,
    'anthropic-claude-opus-5.5': 1.124, 'openai-gpt-6-sol': 0.192, 'google-gemini-3.1-pro': 0.184}


def per_question(key):
    per = {}
    for l in open(f'{ROOT}/verdicts/{key}.jsonl'):
        v = json.loads(l)
        per.setdefault(v['id'], []).append({d: (v[d] if d == 'composite' else v[d]['score']) for d in DIMS})
    return {q: {d: S.mean(x[d] for x in xs) for d in DIMS} for q, xs in per.items()}


def speed(key):
    t = [json.loads(l)['seconds_to_completion'] for l in open(f'{ROOT}/responses/{key}.jsonl')]
    t = sorted(x for x in t if x)
    return S.mean(t), S.median(t), t[int(0.9 * len(t))]


def ci(dd):
    random.seed(0)
    b = sorted(S.mean(random.choices(dd, k=len(dd))) for _ in range(3000))
    return b[75], b[2924]


data = {k: per_question(k) for k in NAMES}
order = sorted(NAMES, key=lambda k: -S.mean(v['composite'] for v in data[k].values()))
out = ['# Results — 91 current-law questions, Nylon Practitioner Rubric v1.0, judged by Kimi K3', '',
       '| Rank | System | Correctness | Completeness | Helpfulness | Faithfulness | Citation grounding | Composite |',
       '|---|---|---|---|---|---|---|---|']
for i, k in enumerate(order, 1):
    d = data[k]
    out.append(f'| {i} | {NAMES[k]} | ' + ' | '.join(f'{S.mean(v[x] for v in d.values()):.2f}' for x in DIMS[:-1]) + f' | **{S.mean(v["composite"] for v in d.values()):.3f}** |')
nyl = data['nylon-october-snapshot']
out += ['', '## Nylon minus each system (paired by question; 95% bootstrap interval)', '',
        '| System | Correctness | Completeness | Helpfulness | Faithfulness | Citation grounding | Composite |', '|---|---|---|---|---|---|---|']
for k in order:
    if k == 'nylon-october-snapshot': continue
    qs = [q for q in nyl if q in data[k]]
    cells = []
    for x in DIMS:
        dd = [nyl[q][x] - data[k][q][x] for q in qs]; lo, hi = ci(dd)
        cells.append(f'{S.mean(dd):+.2f} [{lo:+.2f}, {hi:+.2f}]')
    out.append(f'| {NAMES[k]} | ' + ' | '.join(cells) + ' |')
out += ['', '## Judge consistency check: pass / borderline / fail (not part of the benchmark)', '',
        'A coarse overall call the judge makes after scoring, used only to confirm its scores are coherent; see rubric/design-rationale.md section 3.', '',
        '| System | Pass | Borderline | Fail |', '|---|---|---|---|']
for k in order:
    vs = [json.loads(l)['verdict'] for l in open(f'{ROOT}/verdicts/{k}.jsonl')]
    out.append(f'| {NAMES[k]} | {vs.count("pass")} | {vs.count("borderline")} | {vs.count("fail")} |')
out += ['', '## Speed and cost per answer', '', '| System | Mean time to completion (s) | Median (s) | 90th percentile (s) | Mean cost (USD) |', '|---|---|---|---|---|']
for k in order:
    m, med, p90 = speed(k)
    out.append(f'| {NAMES[k]} | {m:.0f} | {med:.0f} | {p90:.0f} | {f"{COST[k]:.2f}" if k in COST else "not published"} |')
text = '\n'.join(out) + '\n'
open(f'{ROOT}/results/summary.md', 'w').write(text)
print(text)
