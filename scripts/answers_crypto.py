#!/usr/bin/env python3
"""Encrypt or decrypt the questions, reference answers and systems' answers (standard library plus the openssl command).

    NYLON_BENCH_KEY=<key> python3 scripts/answers_crypto.py decrypt   # writes plaintext copies to decrypted/
    NYLON_BENCH_KEY=<key> python3 scripts/answers_crypto.py encrypt   # (authors only) encrypts the plaintext fields in place
    NYLON_BENCH_KEY=<key> python3 scripts/answers_crypto.py encrypt-questions <dataset.jsonl>
        # (authors only) adds the encrypted question and reference answer to questions/questions.jsonl, after checking
        # each against its published SHA-256 fingerprint

Each answer is encrypted separately with AES-256-CBC, a random salt and PBKDF2 (100,000 iterations), as produced by
`openssl enc -aes-256-cbc -pbkdf2 -iter 100000 -salt -a -A`, so any single answer can also be decrypted by hand:

    printf '%s' '<ciphertext>' | openssl enc -d -aes-256-cbc -pbkdf2 -iter 100000 -a -A -pass env:NYLON_BENCH_KEY

Encrypted fields:
  questions/questions.jsonl  `question_encrypted` and `reference_answer_encrypted` (the decrypted text matches the
                        published `sha256_question` and `sha256_reference_answer` fingerprints)
  responses/*.jsonl     `response` is replaced by `response_encrypted`
  judge-inputs/*.jsonl  the CANDIDATE ANSWER section of `user_message` is replaced by a placeholder, and the section
                        itself is stored in `candidate_answer_encrypted`
Everything else (ids, timings, cited URLs, cited source text, verdicts) stays in plain text.
The key is never stored in this folder; see README for how to request it.
"""
import hashlib, json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEYS = ['nylon-october-snapshot', 'anthropic-claude-fable-5.1', 'openai-gpt-6-astra',
        'anthropic-claude-opus-5.5', 'openai-gpt-6-sol', 'google-gemini-3.1-pro']
OPENSSL = ['openssl', 'enc', '-aes-256-cbc', '-pbkdf2', '-iter', '100000', '-a', '-A', '-pass', 'env:NYLON_BENCH_KEY']
START, END = 'CANDIDATE ANSWER (to grade):\n', '\n\nCANDIDATE CITED SOURCES'
PLACEHOLDER = '[encrypted — see candidate_answer_encrypted; decrypt with scripts/answers_crypto.py]'


def _run(args, data):
    p = subprocess.run(args, input=data.encode(), capture_output=True, check=True)
    return p.stdout.decode()


def enc(text):
    return _run(OPENSSL + ['-salt'], text)


def dec(cipher):
    return _run(OPENSSL + ['-d'], cipher)


def load(path):
    return [json.loads(l) for l in open(path, encoding='utf-8')]


def write(path, rows):
    with open(path, 'w', encoding='utf-8') as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')


def decrypted(kind, key):
    """Rows of responses/ or judge-inputs/ for one system, with answers in plain text (needs NYLON_BENCH_KEY)."""
    rows = load(f'{ROOT}/{kind}/{key}.jsonl')
    with ThreadPoolExecutor(16) as ex:
        if kind == 'responses':
            texts = list(ex.map(lambda r: dec(r['response_encrypted']) if 'response_encrypted' in r else r['response'], rows))
            for r, t in zip(rows, texts):
                r.pop('response_encrypted', None); r['response'] = t
        else:
            texts = list(ex.map(lambda r: dec(r['candidate_answer_encrypted']) if 'candidate_answer_encrypted' in r else None, rows))
            for r, t in zip(rows, texts):
                if t is not None:
                    r['user_message'] = r['user_message'].replace(PLACEHOLDER, t, 1); r.pop('candidate_answer_encrypted')
    return rows


def encrypt_questions(src):
    sha = lambda t: hashlib.sha256(t.encode('utf-8')).hexdigest()
    by_hash = {sha(r['question']): r for r in load(src)}
    p = f'{ROOT}/questions/questions.jsonl'; rows = load(p)
    pairs = []
    for r in rows:
        d = by_hash[r['sha256_question']]
        assert sha(d['answer']) == r['sha256_reference_answer'], r['id']
        pairs.append((d['question'], d['answer']))
    with ThreadPoolExecutor(16) as ex:
        qs = list(ex.map(lambda x: enc(x[0]), pairs)); ans = list(ex.map(lambda x: enc(x[1]), pairs))
    for r, (q, a), cq, ca in zip(rows, pairs, qs, ans):
        assert dec(cq) == q and dec(ca) == a
        r['question_encrypted'], r['reference_answer_encrypted'] = cq, ca
    write(p, rows)
    print(f'encrypted {len(rows)} questions and reference answers')


def decrypted_questions():
    """questions/questions.jsonl with the question and reference answer in plain text (needs NYLON_BENCH_KEY)."""
    rows = load(f'{ROOT}/questions/questions.jsonl')
    with ThreadPoolExecutor(16) as ex:
        qs = list(ex.map(lambda r: dec(r.pop('question_encrypted')), rows))
        ans = list(ex.map(lambda r: dec(r.pop('reference_answer_encrypted')), rows))
    for r, q, a in zip(rows, qs, ans):
        r['question'], r['reference_answer'] = q, a
    return rows


def encrypt_all():
    with ThreadPoolExecutor(16) as ex:
        for k in KEYS:
            p = f'{ROOT}/responses/{k}.jsonl'; rows = load(p)
            todo = [r for r in rows if 'response' in r]
            for r, c in zip(todo, ex.map(lambda r: enc(r['response']), todo)):
                assert dec(c) == r['response']
                r['response_encrypted'] = c; del r['response']
            write(p, [{**{x: r[x] for x in r if x != 'response_encrypted'}, 'response_encrypted': r['response_encrypted']} for r in rows])

            p = f'{ROOT}/judge-inputs/{k}.jsonl'; rows = load(p)
            todo = [r for r in rows if 'candidate_answer_encrypted' not in r]
            secs = []
            for r in todo:
                m = r['user_message']; a = m.index(START) + len(START); b = m.index(END, a)
                secs.append((a, b, m[a:b]))
            for r, (a, b, t), c in zip(todo, secs, ex.map(lambda s: enc(s[2]), secs)):
                assert dec(c) == t
                r['user_message'] = r['user_message'][:a] + PLACEHOLDER + r['user_message'][b:]
                r['candidate_answer_encrypted'] = c
            write(p, rows)
            print('encrypted', k)


def decrypt_all():
    out = f'{ROOT}/decrypted'
    os.makedirs(f'{out}/questions', exist_ok=True)
    write(f'{out}/questions/questions.jsonl', decrypted_questions())
    for kind in ('responses', 'judge-inputs'):
        os.makedirs(f'{out}/{kind}', exist_ok=True)
        for k in KEYS:
            write(f'{out}/{kind}/{k}.jsonl', decrypted(kind, k))
    print(f'plain-text copies written to {out}/')


if __name__ == '__main__':
    if not os.environ.get('NYLON_BENCH_KEY'):
        sys.exit('Set NYLON_BENCH_KEY to the key (see README for how to request it).')
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'decrypt'
    if cmd == 'encrypt-questions':
        encrypt_questions(sys.argv[2])
    else:
        {'encrypt': encrypt_all, 'decrypt': decrypt_all}[cmd]()
