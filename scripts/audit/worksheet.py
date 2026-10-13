import json, os, re, sys, unicodedata
SP = os.environ.get('AUDIT_SRC', '/tmp/audit-src')  # local copies of the source editions (not committed)
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
luke_ch = int(sys.argv[1]); out = sys.argv[2]
# SBLGNT
sbl = {}
for ln in open(f'{SP}/sbl/63-Lk-morphgnt.txt', encoding='utf-8'):
    p = ln.split(); bcv = p[0]; c = int(bcv[2:4]); v = int(bcv[4:6])
    sbl.setdefault((c, v), []).append(re.sub("[⸀⸁⸂⸃⸄⸅]", "", p[3]))
# JSON
J = json.load(open(f'{REPO}/data/proto_luke.json'))
def expand(spec):
    spec = spec.replace('–', '-').strip()
    m = re.match(r'^(\d+):(\d+)[a-d]?(?:-(?:(\d+):)?(\d+)[a-d]?)?$', spec)
    if not m: return set()
    c1, v1 = int(m.group(1)), int(m.group(2))
    if m.group(4) is None: return {(c1, v1)}
    c2 = int(m.group(3)) if m.group(3) else c1; v2 = int(m.group(4))
    if c1 == c2: return {(c1, v) for v in range(v1, v2 + 1)}
    return {(c1, v) for v in range(v1, 90)} | {(c2, v) for v in range(1, v2 + 1)}
jmap = {}
for ch in J['chapters']:
    for v in ch['verses']:
        for part in re.split(r'[,;]\s*', v['canonical_ref'].replace('Luke ', '')):
            for cv in expand(part):
                jmap.setdefault(cv, []).append((ch['chapter'], v))
# Roth tables
R = json.load(open(f'{SP}/data/roth_tables.json'))
rstat = {}
for k in ('present', 'absent'):
    for r in R[k]:
        for cv in expand(r['verse']): rstat.setdefault(cv, []).append(f"{k.upper()} [{r['verse']}] {r['loci']}")
for u in R['unattested']:
    for cv in expand(u): rstat.setdefault(cv, []).append(f"UNATTESTED [{u}]")
# Roth ch9
ch9 = open(f'{SP}/data/roth_ch9_marked.txt', encoding='utf-8').read().split('\n')
r9 = {}
cur = None
for ln in ch9:
    m = re.match(r'^(\d{1,2}:\d{1,2}[a-d]?(?:[–-]\d{1,2}(?::\d{1,2})?[a-d]?)?)\s*(\[|—)', ln)
    if m:
        cur = m.group(1); r9.setdefault(cur, []).append(ln)
    elif cur and ln.strip() and not ln.startswith('---') and not re.match(r'^(The Reconstruction|\d+ CHAPTER 9|CHAPTER)', ln):
        r9[cur].append(ln)
    elif ln.startswith('---'):
        pass
r9cv = {}
for k, lines in r9.items():
    for cv in expand(k): r9cv.setdefault(cv, []).append(' '.join(lines))
# Epiphanius scholia
ep = {}
for ln in open(f'{REPO}/docs/audit/sources/epiphanius_pan42_scholia.md', encoding='utf-8'):
    if ln.startswith('| ') and re.match(r'^\| \d+ ', ln):
        cells = [c.strip() for c in ln.strip().strip('|').split('|')]
        n, lref, text, kind = cells[0], cells[1], cells[2], cells[3]
        for part in re.split(r'[,;]\s*', lref):
            part = part.strip()
            if ':' not in part and ep_last_ch: part = f'{ep_last_ch}:{part}'
            m = re.match(r'(\d+):', part); ep_last_ch = m.group(1) if m else None
            for cv in expand(re.sub(r'[a-d](?=$|[-–])', '', part)): ep.setdefault(cv, []).append(f'sch.{n} [{lref}] {text} — {kind}')
    else:
        ep_last_ch = None
T4 = json.load(open(f'{SP}/data/tert4.json'))
def tert_sections(loci):
    secs = []
    for m in re.finditer(r'Marc\.\s*(\d)\.(\d+)\.(\d+(?:[,–-]\s*\d+)*)', loci):
        b, c, ss = m.group(1), m.group(2), m.group(3)
        nums = []
        for part in re.split(r',\s*', ss):
            if re.search(r'[–-]', part):
                a, z = re.split(r'[–-]', part); nums += list(range(int(a), int(z) + 1))
            else: nums.append(int(part))
        for s in nums: secs.append(f'{b}.{c}.{s}')
    # also "; 42.1" style continuations
    return secs
o = []
maxv = max(v for (c, v) in sbl if c == luke_ch)
for v in range(1, maxv + 1):
    cv = (luke_ch, v)
    o.append(f'\n## Luke {luke_ch}:{v}\n')
    o.append('SBLGNT: ' + ' '.join(sbl.get(cv, [])))
    for (jc, jv) in jmap.get(cv, []):
        o.append(f"JSON ch{jc} v{jv['verse']} [{jv['canonical_ref']}]\n  GR: {jv['greek']}\n  EN: {jv['english']}")
    if cv not in jmap: o.append('JSON: — (not in reconstruction)')
    for s in rstat.get(cv, ['ROTH: not in tables']): o.append('ROTH: ' + s)
    for s in r9cv.get(cv, []): o.append('ROTH9: ' + s)
    for s in ep.get(cv, []): o.append('EPIPH: ' + s)
    secs = []
    for s in rstat.get(cv, []):
        secs += tert_sections(s)
    for s in dict.fromkeys(secs):
        if s.startswith('4.'):
            o.append(f'TERT {s}: ' + T4.get(s, '(missing)'))
open(out, 'w').write('\n'.join(o))
print('ok', out)
