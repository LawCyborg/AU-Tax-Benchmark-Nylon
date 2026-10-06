#!/usr/bin/env python3
"""Recompute the checks cited in DECISIONS.md and rubric/design-rationale.md (no network, standard library only).

    python3 scripts/checks.py                              # sections 1-3, and 4 in part
    NYLON_BENCH_KEY=<key> python3 scripts/checks.py        # every section (section 4 reads the encrypted answers)

1. Share of answers at Correctness 4 or above and at 5, with paired 95% bootstrap intervals for Nylon minus each system.
2. Nylon's lead over each system under alternative weightings, with paired 95% bootstrap intervals.
3. Composites excluding the 12 answers whose progress-message removal was imperfect (design-rationale §4.5).
4. Run dates (S6).
"""
import json, os, random, re, statistics as S
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEYS = ['nylon-october-snapshot', 'anthropic-claude-fable-5.1', 'openai-gpt-6-astra',
        'anthropic-claude-opus-5.5', 'openai-gpt-6-sol', 'google-gemini-3.1-pro']
DIMS = ['correctness', 'completeness', 'helpfulness', 'faithfulness', 'citation_grounding']
NARRATION = {'q1.15', 'q2.4', 'q2.9', 'q2.11', 'q2.27', 'q3.5', 'q4.7', 'q5.4', 'q5.6', 'q5.10', 'q5.17', 'q1.3'}

def load(path):
    return [json.loads(l) for l in open(f'{ROOT}/{path}')]


HAVE_KEY = bool(os.environ.get('NYLON_BENCH_KEY'))  # answers are encrypted; see README and scripts/answers_crypto.py
if HAVE_KEY:
    import sys; sys.dont_write_bytecode = True; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from answers_crypto import decrypted


def ci(dd):
    random.seed(0)
    b = sorted(S.mean(random.choices(dd, k=len(dd))) for _ in range(3000))
    return b[75], b[2924]


def fmt(dd):
    lo, hi = ci(dd)
    return f'{S.mean(dd):+.3f} [{lo:+.3f}, {hi:+.3f}]'


V = {k: {v['id']: v for v in load(f'verdicts/{k}.jsonl')} for k in KEYS}
ny = V[KEYS[0]]

print('## 1. Share of answers at Correctness 4 or above and at 5\n')
print('| System | >=4 | 5 |')
print('|---|---|---|')
for k in KEYS:
    c = [v['correctness']['score'] for v in V[k].values()]
    print(f'| {k} | ' + ' | '.join(f'{sum(x >= t for x in c) / len(c):.2f}' for t in (4, 5)) + ' |')
print('\nNylon minus each system, share at or above level (paired 95% interval):\n')
print('| System | >=4 | 5 |')
print('|---|---|---|')
for k in KEYS[1:]:
    print(f'| {k} | ' + ' | '.join(
        fmt([(ny[q]['correctness']['score'] >= t) - (V[k][q]['correctness']['score'] >= t) for q in ny]) for t in (4, 5)) + ' |')

WEIGHTS = {
    'published': {'citation_grounding': .35, 'faithfulness': .30, 'correctness': .15, 'completeness': .10, 'helpfulness': .10},
    'equal': {d: .2 for d in DIMS},
    'correctness only': {'correctness': 1},
    'correctness + completeness (15:10)': {'correctness': .6, 'completeness': .4},
}
print('\n## 2. Nylon minus each system under alternative weightings (paired 95% interval)\n')
print('| System | ' + ' | '.join(WEIGHTS) + ' |')
print('|---|' + '---|' * len(WEIGHTS))
for k in KEYS[1:]:
    cells = []
    for w in WEIGHTS.values():
        sc = lambda v: sum(v[d]['score'] * x for d, x in w.items()) / sum(w.values())
        cells.append(fmt([sc(ny[q]) - sc(V[k][q]) for q in ny]))
    print(f'| {k} | ' + ' | '.join(cells) + ' |')

print('\n## 3. Composite excluding the 12 narration-affected questions (for every system)\n')
print('| System | All 91 | Excluding 12 |')
print('|---|---|---|')
for k in KEYS:
    vs = V[k].values()
    print(f'| {k} | {S.mean(v["composite"] for v in vs):.3f} | {S.mean(v["composite"] for v in vs if v["id"] not in NARRATION):.3f} |')

print('\n## 4. Run dates (S6)\n')
print('| System | ATO PDF "Generated on" dates in captured sources | Answers stating a 1 October 2026 date |')
print('|---|---|---|')
GEN = re.compile(r'Generated on: (\d{1,2} \w+ 20\d\d)')
for k in KEYS:
    gen = sorted({d for j in load(f'judge-inputs/{k}.jsonl') for d in GEN.findall(j['user_message'])})
    oct1 = ', '.join(r['id'] for r in decrypted('responses', k) if re.search(r'\b1 October 2026', r['response'])) if HAVE_KEY else '(needs key)'
    print(f'| {k} | {", ".join(gen) or "-"} | {oct1 or "-"} |')
