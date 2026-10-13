"""Screen the NA27 text of Luke against SBLGNT by OCR, to list every place where the printed NA27
wording may differ from SBLGNT. Each candidate is then checked by eye on the page image; the
screen only finds places to look, it decides nothing.

Steps: render the NA27 spreads (Drive parts p4, p5, p6; each PDF page = two book pages) at 220 dpi,
split into halves, OCR with tesseract (grc), keep words in the main-text font size, normalize,
align with SBLGNT Luke, and report differences with SBLGNT verse references.

Usage: AUDIT_SRC=<dir> python3 scripts/audit/na27_screen.py render|ocr|diff
"""
import csv, difflib, glob, os, re, subprocess, sys, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sbl import load as load_sbl

SRC = os.environ.get('AUDIT_SRC', '/tmp/audit-src')
NA = f'{SRC}/na27'
OUT = f'{NA}/screen'
PAGES = [('p4', range(25, 37)), ('p5', range(1, 37)), ('p6', range(1, 2))]


def render():
    os.makedirs(f'{OUT}/img', exist_ok=True)
    from PIL import Image
    for part, rng in PAGES:
        for n in rng:
            base = f'{OUT}/img/{part}-{n:02d}'
            if os.path.exists(base + '_R.png'):
                continue
            subprocess.run(['pdftoppm', '-f', str(n), '-l', str(n), '-r', '220', '-png', '-singlefile',
                            f'{NA}/{part}.pdf', base], check=True)
            im = Image.open(base + '.png'); w, h = im.size
            im.crop((0, 0, w // 2, h)).save(base + '_L.png')
            im.crop((w // 2, 0, w, h)).save(base + '_R.png')
            os.remove(base + '.png')


def ocr():
    os.makedirs(f'{OUT}/tsv', exist_ok=True)
    for png in sorted(glob.glob(f'{OUT}/img/*_[LR].png')):
        name = os.path.basename(png)[:-4]
        dst = f'{OUT}/tsv/{name}'
        if not os.path.exists(dst + '.tsv'):
            subprocess.run(['tesseract', png, dst, '-l', 'grc', '--psm', '4', 'tsv'],
                           check=True, stderr=subprocess.DEVNULL)


def order_key(name):
    part, rest = name.split('-')
    n, side = rest.split('_')
    return ({'p4': 0, 'p5': 1, 'p6': 2}[part], int(n), side)


def strip(s):
    d = unicodedata.normalize('NFD', s.lower())
    d = ''.join(ch for ch in d if unicodedata.category(ch) != 'Mn')
    return d.replace('ς', 'σ')


GREEK = re.compile(r'[α-ω]+')


def main_text_words():
    """Words in page order, keeping only those in the main-text font size. Returns
    [(page, raw, normalized_token, bracketed)]."""
    out = []
    for tsv in sorted(glob.glob(f'{OUT}/tsv/*.tsv'), key=lambda p: order_key(os.path.basename(p)[:-4])):
        page = os.path.basename(tsv)[:-4]
        rows = list(csv.DictReader(open(tsv, encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE))
        lines = {(r['block_num'], r['par_num'], r['line_num']): int(r['height'])
                 for r in rows if r['level'] == '4'}
        words = [r for r in rows if r['level'] == '5' and r['text'].strip()]
        if not words or not lines:
            continue
        # main text is set in a larger size than the apparatus and margins: filter by line height
        hs = sorted(lines.values())
        big = hs[int(len(hs) * 0.75)]
        keep = [r for r in words
                if lines.get((r['block_num'], r['par_num'], r['line_num']), 0) >= 0.72 * big]
        # join hyphenated line breaks
        pending = ''
        for r in keep:
            t = r['text']
            if pending:
                t = pending + t
                pending = ''
            if t.endswith('-') and len(t) > 1:
                pending = t[:-1]
                continue
            # drop NA27 sigla read as capitals (ᵀ ° ⸀ ⸂ → Τ Ο Γ Ξ …), marginal references and numbers
            core = re.sub(r'\W', '', t)
            if (re.search(r'\d', t) or (len(core) == 1 and core.isupper())
                    or (len(core) == 2 and core[0].isupper() and core[1] in 'ιςΙ')):
                continue
            norm = strip(t)
            m = GREEK.findall(norm)
            if not m:
                continue
            tok = max(m, key=len)
            out.append((page, t, tok, '[' in t or ']' in t))
    return out


def sbl_tokens():
    S = load_sbl()
    toks = []
    for (c, v), text in sorted(S.items()):
        for w in text.split():
            m = GREEK.findall(strip(w))
            if m:
                toks.append(((c, v), w, max(m, key=len)))
    return toks


def same(a, b):
    """OCR token a matches SBL token b, allowing a leading siglum letter (Γ, Τ, Ο, Ξ read as letters)."""
    if a == b or (len(a) > 2 and a[1:] == b):
        return True
    # only long words may differ by an OCR slip; short words (ἄν/ἐάν, δέ/τε, αὐτοῦ/αὐτῷ) must match exactly
    return min(len(a), len(b)) >= 7 and difflib.SequenceMatcher(None, a, b).ratio() >= 0.86


def diff():
    ocr = main_text_words()
    sbl = sbl_tokens()
    a = [t[2] for t in sbl]
    b = [t[2] for t in ocr]
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    rows = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            continue
        sw = sbl[i1:i2]; ow = ocr[j1:j2]
        # drop OCR-noise substitutions of equal length where all pairs are near-identical
        if op == 'replace' and len(sw) == len(ow) and all(same(o[2], s[2]) for s, o in zip(sw, ow)):
            continue
        if op == 'insert' and len(ow) > 4:
            continue  # leftover marginal or apparatus text
        ref = sbl[i1][0] if i1 < len(sbl) else sbl[-1][0]
        rows.append({'ref': f'{ref[0]}:{ref[1]}', 'op': op,
                     'sbl': ' '.join(s[1] for s in sw), 'na27_ocr': ' '.join(o[1] for o in ow),
                     'page': ow[0][0] if ow else (ocr[j1][0] if j1 < len(ocr) else ''),
                     'bracketed': any(o[3] for o in ow)})
    path = f'{OUT}/candidates.csv'
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=['ref', 'op', 'sbl', 'na27_ocr', 'page', 'bracketed'])
        w.writeheader(); w.writerows(rows)
    print(path, len(rows), 'candidates;', len(ocr), 'OCR words;', len(sbl), 'SBL words')


if __name__ == '__main__':
    {'render': render, 'ocr': ocr, 'diff': diff}[sys.argv[1]]()
