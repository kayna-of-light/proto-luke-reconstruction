import pdfplumber, sys, re, collections
pdf = pdfplumber.open(sys.argv[1])
# locate start page: page whose text contains 'The Reconstruction of Marcion' and 'CHAPTER 9'
start = None
for i in range(380, len(pdf.pages)):
    t = pdf.pages[i].extract_text() or ''
    if 'CHAPTER 9' in t and 'Reconstruction of Marcion' in t:
        start = i; break
print('start', start, file=sys.stderr)
fonts = collections.Counter()
out = []
for i in range(start, min(start + 75, len(pdf.pages))):
    p = pdf.pages[i]
    words = p.extract_words(extra_attrs=['fontname', 'size'], keep_blank_chars=False, use_text_flow=True)
    lines = collections.OrderedDict()
    for w in words:
        if w['size'] < 9.0:  # footnotes smaller
            continue
        key = round(w['top'] / 3)
        lines.setdefault(key, []).append(w)
    for k, ws in lines.items():
        seg = []
        for w in sorted(ws, key=lambda w: w['x0']):
            f = w['fontname']; fonts[f] += 1
            b = 'Bold' in f or 'Semibold' in f
            it = 'Italic' in f or 'Oblique' in f or f.endswith('-It') or 'It' in f.split('+')[-1].split('-')[-1]
            tag = ('B' if b else '') + ('I' if it else '')
            seg.append((tag, w['text']))
        # merge runs
        s = ''; cur = None
        for tag, txt in seg:
            if tag != cur:
                if cur: s += '⟧'
                s += ('⟦' + tag + ':') if tag else ''
                cur = tag if tag else None
                if not tag: cur = None
            s += txt + ' '
        if cur: s += '⟧'
        out.append(s.strip())
    out.append(f'--- [pdf page {i}]')
open(sys.argv[2], 'w').write('\n'.join(out))
print(fonts.most_common(20), file=sys.stderr)
