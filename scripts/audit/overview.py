import json, re, sys
d = json.load(open(sys.argv[1])); R = json.load(open(sys.argv[2]))
def expand(spec):
    # returns set of (ch, v) with optional part letter ignored
    spec = spec.replace('–', '-')
    m = re.match(r'^(\d+):(\d+)[a-d]?(?:-(?:(\d+):)?(\d+)[a-d]?)?$', spec)
    if not m: return set()
    c1, v1 = int(m.group(1)), int(m.group(2))
    if m.group(4) is None: return {(c1, v1)}
    c2 = int(m.group(3)) if m.group(3) else c1; v2 = int(m.group(4))
    out = set()
    if c1 == c2:
        for v in range(v1, v2 + 1): out.add((c1, v))
    else:
        for v in range(v1, 80): out.add((c1, v))
        for c in range(c1 + 1, c2): 
            for v in range(1, 80): out.add((c, v))
        for v in range(1, v2 + 1): out.add((c2, v))
    return out
status = {}
for r in R['present']:
    for cv in expand(r['verse']): status.setdefault(cv, []).append('P:' + r['verse'] + ' ' + r['loci'][:60])
for r in R['absent']:
    for cv in expand(r['verse']): status.setdefault(cv, []).append('A:' + r['verse'] + ' ' + r['loci'][:60])
for u in R['unattested']:
    for cv in expand(u): status.setdefault(cv, []).append('U:' + u)
for ch in d['chapters']:
    print(f"=== JSON ch {ch['chapter']}")
    for v in ch['verses']:
        ref = v['canonical_ref'].replace('Luke ', '')
        refs = set()
        for part in re.split(r'[,;]\s*', ref):
            refs |= expand(part.strip())
        st = sorted({s.split(' ')[0] for cv in refs for s in status.get(cv, ['?'])})
        print(f"  v{v['verse']:>2} {ref:<14} {' '.join(st)}")
