import re, json, sys
# Build index {"4.43.6": latin text} from Evans Latin text (book 4 or 5)
src, book, out = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(src, encoding='utf-8').read()
lines = t.split('\n')
# Drop apparatus/footnote lines and page headers: apparatus lines start with "NN. " followed by sigla, or with page numbers; Evans footnotes like "43. a Isa..." or "43. 1 eripuit..."
body = []
for ln in lines:
    s = ln.strip()
    if re.match(r'^\d{1,2}\.\s+(\d+|[a-z])\s', s):  # apparatus / footnote lines
        continue
    if re.match(r'^\d{2,3}$', s) or s in ('TERTULLIAN',) or re.match(r'^(IV|V)\.\s*\d+$', s):
        continue
    body.append(ln)
text = '\n'.join(body)
idx = {}
chap = None
# chapter markers: line starting with "N.  [1]" ; section markers "[n]"
pos = 0
pattern = re.compile(r'(?m)^(\d{1,2})\.\s+\[1\]|\[(\d{1,2})\]')
cur_key = None; buf = []
for m in pattern.finditer(text):
    seg = text[pos:m.start()]
    if cur_key: idx[cur_key] = idx.get(cur_key, '') + seg
    if m.group(1):
        chap = int(m.group(1)); sec = 1
    else:
        sec = int(m.group(2))
    cur_key = f"{book}.{chap}.{sec}" if chap else None
    pos = m.end()
if cur_key: idx[cur_key] = idx.get(cur_key, '') + text[pos:]
for k in idx: idx[k] = re.sub(r'-\n(\s*)', '', idx[k]); idx[k] = re.sub(r'\s+', ' ', idx[k]).strip()
json.dump(idx, open(out, 'w'), ensure_ascii=False, indent=0)
print(len(idx), list(idx)[:5], list(idx)[-3:])
