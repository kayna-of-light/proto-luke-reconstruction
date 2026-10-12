import re, json, sys
src = sys.argv[1]; out = sys.argv[2]
L = open(src, encoding='utf-8').read().split('\n')
def seg(a, b): return L[a-1:b-1]
present_lines = seg(2268, 3394); absent_lines = seg(3394, 3460); unatt_lines = seg(3460, 3546)
vre = re.compile(r'^(\d{1,2}:\d{1,2}[a-d]?(?:[–-]\d{1,2}(?::\d{1,2})?[a-d]?)?)(\d{0,3})\s{2,}(.*)$')
def parse_rows(lines):
    rows = []; cur = None
    for ln in lines:
        m = vre.match(ln)
        if m:
            cur = {'verse': m.group(1), 'fn': m.group(2), 'cols': [m.group(3)]}; rows.append(cur)
        elif cur and ln.startswith(' ' * 6) and ln.strip() and not re.match(r'^\s*\d+\s', ln) and len(rows) and not ln.strip().startswith(('Verse', 'Luke', 'Dialogue', 'Table', 'Sources', 'CHAPTER')):
            cur['cols'].append(ln)
        elif not ln.strip():
            pass
        else:
            cur = None
    return rows
P = parse_rows(present_lines); A = parse_rows(absent_lines)
U = []
for ln in unatt_lines:
    for tok in re.findall(r'(\d{1,2}:\d{1,2}[a-d]?(?:[–-]\d{1,2}(?::\d{1,2})?[a-d]?)?)', ln):
        U.append(tok)
def clean(r):
    t = ' | '.join(c.strip() for c in r['cols'])
    t = re.sub(r'\s{2,}', ' ; ', t)
    return {'verse': r['verse'], 'loci': t}
json.dump({'present': [clean(r) for r in P], 'absent': [clean(r) for r in A], 'unattested': U}, open(out, 'w'), ensure_ascii=False, indent=0)
print(len(P), len(A), len(U))
