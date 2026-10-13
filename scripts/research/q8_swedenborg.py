"""Research question Q8 (docs/research_questions.md): Swedenborg's correspondential decoding of the
Lukan parables, by attestation class. Implements the protocol fixed on 2026-10-13 before extraction.

Inputs (not committed; public domain), under AUDIT_SRC:
  kjv/kjv.json                     KJV (thiagobodruk/bible en_kjv.json)
  swedenborg/arcanacoelestiah*.txt Arcana Coelestia, OCR text layers (Internet Archive, 1870 and 1915 eds.)
  swedenborg/apocalypseexplained0[1-6]swed.txt  Apocalypse Explained (1890 ed.)
Output: docs/research/q8/q8_results.json (+ q8_sections.json: the citing sections found, for checking).

Usage: AUDIT_SRC=<dir> python3 -I scripts/research/q8_swedenborg.py

Conventions fixed with the protocol:
- Element inventory: concrete nouns in the KJV text of the parable as delimited for Luke (for the
  controls, of the Matthean text). "Concrete" = WordNet lexicographer file of the first noun sense in
  {person, animal, plant, artifact, object, location, food, body, substance, quantity}, plus proper
  nouns and cardinal numbers. Fixed by rule, before extraction; the inventory is written to the output.
- Citing section: a numbered section of the corpus that cites, by book chapter verse, any verse of
  the parable or of its NA27 parallels. A bare reference ("xv. 22, 23", with or without parentheses)
  belongs to the nearest book named before it (parser corrected 2026-10-13: the first version read
  only parenthesized bare references and so missed most of the 1870 AC, e.g. AC 9391 on Luke 15:22-23).
- Decoded element: the element's word (singular or plural) within 25 words of one of: signifies,
  signified, denotes, "is meant", "are meant", means, represents, corresponds, in a citing section.

Revised measure (--revised; fixed 2026-10-13 after the precision check of the first run showed that
measure to be mostly noise, and before the revised run):
- Window: 300 words either side of each reference to a verse of the parable or its parallels.
- Decoded: the element's word stands within 6 words before a signification verb (signifies, signify,
  signified, denotes, denote, denoted, means, mean, "is/are meant", represents, represent,
  corresponds, correspond), or in "by ... X ... is/are meant/signified/denoted" with at most 12 words
  from "by" to the verb.
- Inventory: as above, without cardinal numbers, noun.quantity, and the closed-class words the tagger
  takes for nouns (thou, thee, ye, one, out, forth, well).
- --sample writes 30 random hits (seed 20261014, parable withheld) for the precision check and stops.
"""
import glob, json, os, re, sys
from collections import defaultdict

SRC = os.environ.get('AUDIT_SRC', '/tmp/audit-src')
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
OUT = os.path.join(REPO, 'docs', 'research', 'q8')

# ---- parables (frozen with the protocol; groups from the apparatus classes, parallels from NA27) ----
PARABLES = [
    # name, group, Luke range, parallels
    ('Good Samaritan', 'absent', ('lk', 10, 29, 37), []),
    ('Barren fig tree', 'absent', ('lk', 13, 6, 9), []),
    ('Two sons', 'absent', ('lk', 15, 11, 32), []),
    ('Tenants', 'absent', ('lk', 20, 9, 18), [('mt', 21, 33, 46), ('mk', 12, 1, 12)]),
    ('Tower and king', 'unattested', ('lk', 14, 28, 33), []),
    ('Unworthy servants', 'unattested', ('lk', 17, 7, 10), []),
    ('Sower', 'attested', ('lk', 8, 4, 8), [('mt', 13, 1, 9), ('mk', 4, 1, 9)]),
    ('Friend at midnight', 'attested', ('lk', 11, 5, 8), []),
    ('Rich fool', 'attested', ('lk', 12, 16, 21), []),
    ('Mustard seed and leaven', 'attested', ('lk', 13, 18, 21), [('mt', 13, 31, 33), ('mk', 4, 30, 32)]),
    ('Great banquet', 'attested', ('lk', 14, 16, 24), [('mt', 22, 1, 10)]),
    ('Lost sheep and coin', 'attested', ('lk', 15, 3, 10), [('mt', 18, 12, 14)]),
    ('Unjust steward', 'attested', ('lk', 16, 1, 8), []),
    ('Rich man and Lazarus', 'attested', ('lk', 16, 19, 31), []),
    ('Unjust judge', 'attested', ('lk', 18, 1, 8), []),
    ('Pharisee and tax collector', 'attested', ('lk', 18, 9, 14), []),
    ('Minas', 'attested', ('lk', 19, 11, 27), [('mt', 25, 14, 30)]),
    ('Fig tree in leaf', 'attested', ('lk', 21, 29, 31), [('mt', 24, 32, 35), ('mk', 13, 28, 31)]),
    ('Wheat and tares', 'control', ('mt', 13, 24, 30), []),
    ('Treasure in the field', 'control', ('mt', 13, 44, 44), []),
    ('Pearl', 'control', ('mt', 13, 45, 46), []),
    ('Net', 'control', ('mt', 13, 47, 50), []),
    ('Labourers in the vineyard', 'control', ('mt', 20, 1, 16), []),
    ('Ten virgins', 'control', ('mt', 25, 1, 13), []),
]
BOOK_IDX = {'mt': 39, 'mk': 40, 'lk': 41}
CONCRETE = {'noun.person', 'noun.animal', 'noun.plant', 'noun.artifact', 'noun.object', 'noun.location',
            'noun.food', 'noun.body', 'noun.substance', 'noun.quantity'}
SIGNIF = re.compile(r"\b(signifies|signified|denotes|is\s+meant|are\s+meant|means|represents|corresponds)\b", re.I)
ROMAN = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100}


def roman(s):
    s = s.lower(); total = 0
    for i, ch in enumerate(s):
        v = ROMAN[ch]; nxt = ROMAN[s[i + 1]] if i + 1 < len(s) else 0
        total += -v if v < nxt else v
    return total


def kjv_text(kjv, book, ch, a, b):
    verses = kjv[BOOK_IDX[book]]['chapters'][ch - 1][a - 1:b]
    return ' '.join(re.sub(r'[{}]', '', v) for v in verses)


STOP = {'thou', 'thee', 'ye', 'one', 'out', 'forth', 'well'}
SIGNIF2 = re.compile(r"^(signifies|signify|signified|denotes|denote|denoted|means|mean|represents|represent|corresponds|correspond)$")


def inventory(text, revised=False):
    from nltk import pos_tag, word_tokenize
    from nltk.corpus import wordnet as wn
    from nltk.stem import WordNetLemmatizer
    lem = WordNetLemmatizer(); out = {}
    for w, t in pos_tag(word_tokenize(text)):
        if t in ('NNP', 'NNPS') and w[0].isupper() and w.lower() not in ('lord', 'god', 'o', 'i', 'jesus'):
            out.setdefault(w.lower(), {w.lower()})
        elif t in ('NN', 'NNS'):
            base = lem.lemmatize(w.lower(), 'n'); syn = wn.synsets(base, 'n')
            if revised and (base in STOP or w.lower() in STOP or (syn and syn[0].lexname() == 'noun.quantity')):
                continue
            if syn and syn[0].lexname() in CONCRETE:
                out.setdefault(base, set()).update({base, w.lower()})
        elif t == 'CD' and w.isalpha() and not revised:
            out.setdefault(w.lower(), {w.lower()})
    return {k: sorted(v) for k, v in out.items()}


def sections(path):
    """Split an OCR text into numbered sections. Candidate markers are lines beginning with a number
    followed by a period, or (AE) by a lettered sub-part as OCR renders it ("422[«].", "423*", "426«").
    The markers kept are the longest chain in which each number exceeds the previous by 1–60, so that
    page numbers, sub-paragraph numbers and stray numerals do not split or derail the sequence."""
    text = open(path, encoding='utf-8', errors='replace').read()
    marks = [(m.start(), int(m.group(1))) for m in
             re.finditer(r'(?m)^\s*(\d{1,5})(?:\[[^\]\n]{0,3}\]\.?|[*«»]|\.)[,\s]', text)]
    n = len(marks); best = [1] * n; prev = [-1] * n
    for i in range(n):
        for j in range(max(0, i - 400), i):
            d = marks[i][1] - marks[j][1]
            if 0 < d <= 60 and best[j] + 1 > best[i]:
                best[i], prev[i] = best[j] + 1, j
    seq, i = [], (max(range(n), key=lambda k: best[k]) if n else -1)
    while i != -1:
        seq.append(marks[i]); i = prev[i]
    seq.reverse()
    out = []
    for k, (pos, num) in enumerate(seq):
        end = seq[k + 1][0] if k + 1 < len(seq) else len(text)
        out.append((num, text[pos:end]))
    return out


CITE = re.compile(r"\b(Luke|Luk\.|Matt\.?|Matthew|Mark)\s*[\(\[]?\s*([ivxlc]{1,7}|\d{1,2})\s*[\.,:]\s*([\d\s,\-–]+(?:\s*;\s*(?:[ivxlc]{1,7}|\d{1,2})\s*[\.,:]\s*[\d\s,\-–]+)*)", re.I)


INTRO = re.compile(r"\b(?:in|by)\s+(Luke|Matthew|Mark)\b", re.I)
# a bare reference, with or without parentheses (the 1870 AC prints '..." xv. 22, 23.')
BARE = re.compile(r"(?<![A-Za-z])\(?\s*([ivxlc]{1,7})\s*[\.,]\s*(\d[\d\s,\-–]*)", re.I)
BOOKS = re.compile(r"\b(Luke|Matthew|Matt|Mark|John|Acts|Genesis|Gen|Exodus|Exod|Leviticus|Levit|Lev|Numbers|Num|"
                   r"Deuteronomy|Deut|Joshua|Josh|Judges|Judg|Ruth|Samuel|Sam|Kings|Chronicles|Job|Psalms?|Ps|Proverbs|"
                   r"Prov|Lamentations|Lam|Isaiah|Isa|Jeremiah|Jer|Ezekiel|Ezek|Daniel|Dan|Hosea|Hos|Joel|Amos|Obadiah|"
                   r"Jonah|Micah|Nahum|Habakkuk|Zephaniah|Haggai|Zechariah|Zech|Malachi|Mal|Moses|David|Revelation|"
                   r"Apocalypse|Apoc|Romans|Rom)\b")


def cited_verses(sec, positions=False):
    found = set(); pos_of = defaultdict(set)
    # "In Luke: '...' (xv. 11-32)": a bare reference applies to the last Gospel named before it
    intros = [(m.start(), m.group(1).lower()) for m in INTRO.finditer(sec)]
    named = [(m.start(), m.group(1).lower()) for m in BOOKS.finditer(sec)]
    for m in BARE.finditer(sec):
        prev = [b for (pos, b) in named if pos < m.start() and m.start() - pos < 3000]
        if prev and prev[-1] in ('luke', 'matthew', 'matt', 'mark'):
            book = {'luke': 'lk', 'matthew': 'mt', 'matt': 'mt', 'mark': 'mk'}[prev[-1]]
            ch = roman(m.group(1))
            for part in re.split(r'\s*,\s*', m.group(2).strip()):
                r = re.match(r'(\d{1,3})(?:\s*[-–]\s*(\d{1,3}))?', part)
                if r:
                    a = int(r.group(1)); b = int(r.group(2) or a)
                    if 0 < a <= b <= a + 60:
                        for v in range(a, b + 1):
                            found.add((book, ch, v)); pos_of[(book, ch, v)].add(m.start())
    for m in CITE.finditer(sec):
        book = {'luke': 'lk', 'luk.': 'lk', 'matt': 'mt', 'matt.': 'mt', 'matthew': 'mt', 'mark': 'mk'}[m.group(1).lower()]
        groups = [(m.group(2), m.group(3))]
        rest = m.group(3)
        if ';' in rest:
            first, *more = rest.split(';')
            groups = [(m.group(2), first)]
            for g in more:
                mm = re.match(r'\s*([ivxlc]{1,7}|\d{1,2})\s*[\.,:]\s*([\d\s,\-–]+)', g, re.I)
                if mm:
                    groups.append((mm.group(1), mm.group(2)))
        for chs, vs in groups:
            ch = int(chs) if chs.isdigit() else roman(chs)
            for part in re.split(r'\s*,\s*', vs.strip()):
                r = re.match(r'(\d{1,3})(?:\s*[-–]\s*(\d{1,3}))?', part)
                if r:
                    a = int(r.group(1)); b = int(r.group(2) or a)
                    if 0 < a <= b <= a + 60:
                        for v in range(a, b + 1):
                            found.add((book, ch, v)); pos_of[(book, ch, v)].add(m.start())
    return pos_of if positions else found


def revised_hits(sec, ref_pos, forms):
    """Word positions of `forms` that count as decoded under the revised measure, inside the windows."""
    toks = [(m.start(), m.group().lower()) for m in re.finditer(r"[A-Za-z']+", sec)]
    starts = [p for p, _ in toks]; low = [w for _, w in toks]
    import bisect
    inwin = set()
    for p in ref_pos:
        i = bisect.bisect_left(starts, p)
        inwin.update(range(max(0, i - 300), min(len(low), i + 301)))
    verbs = [i for i in range(len(low)) if SIGNIF2.match(low[i])
             or (low[i] in ('is', 'are') and i + 1 < len(low) and low[i + 1] == 'meant')]
    pas = [i for i in range(len(low) - 1) if low[i] in ('is', 'are') and low[i + 1] in ('meant', 'signified', 'denoted')]
    hits = []
    for i in sorted(inwin):
        if low[i] not in forms:
            continue
        if any(0 < j - i <= 6 for j in verbs):
            hits.append(i); continue
        for j in pas:
            if 0 < j - i <= 12 and 'by' in low[max(0, j - 12):i]:
                hits.append(i); break
    return hits, toks


def main():
    revised = '--revised' in sys.argv or '--sample' in sys.argv
    kjv = json.load(open(f'{SRC}/kjv/kjv.json', encoding='utf-8-sig'))
    files = sorted(glob.glob(f'{SRC}/swedenborg/arcanacoelestiah*.txt')) + sorted(glob.glob(f'{SRC}/swedenborg/apocalypseexplained0*.txt'))
    corpus = []
    seen = set()
    for f in files:
        work = 'AC' if 'arcana' in f else 'AE'
        for n, sec in sections(f):
            key = (work, n)
            if key in seen:       # AC volumes from two editions overlap: keep the first copy
                continue
            seen.add(key)
            corpus.append((work, n, sec, cited_verses(sec, positions=True)))
    coverage = {w: sorted(n for (ww, n) in seen if ww == w) for w in ('AC', 'AE')}

    results, citing_dump, samples = [], {}, []
    for name, group, main_rng, par in PARABLES:
        rngs = [main_rng] + par
        targets = {(b, c, v) for (b, c, a, z) in rngs for v in range(a, z + 1)}
        inv = inventory(kjv_text(kjv, *main_rng), revised)
        citing = [(w, n, sec, set().union(*(cv[t] for t in targets if t in cv)))
                  for (w, n, sec, cv) in corpus if targets & set(cv)]
        decoded = defaultdict(list)
        for w, n, sec, refpos in citing:
            if revised:
                for el, forms in inv.items():
                    hits, toks = revised_hits(sec, refpos, set(forms))
                    if hits:
                        decoded[el].append(f'{w} {n}')
                        for i in hits:
                            samples.append((name, el, f'{w} {n}', ' '.join(t for _, t in toks[max(0, i - 30):i + 30])))
                continue
            words = re.findall(r"[A-Za-z']+", sec)
            low = [x.lower() for x in words]
            sig_pos = [i for i in range(len(low)) if SIGNIF.match(' '.join(low[i:i + 2]))]
            for el, forms in inv.items():
                fs = set(forms)
                for i, x in enumerate(low):
                    if x in fs and any(abs(i - j) <= 25 for j in sig_pos):
                        decoded[el].append(f'{w} {n}'); break
        share = len(decoded) / len(inv) if inv else 0.0
        results.append({'parable': name, 'group': group, 'luke_or_main': main_rng, 'parallels': par,
                        'elements': inv, 'n_elements': len(inv), 'citing_sections': len(citing),
                        'decoded_elements': {k: sorted(set(v)) for k, v in decoded.items()},
                        'n_decoded': len(decoded), 'share_decoded': round(share, 3)})
        citing_dump[name] = [f'{w} {n}' for w, n, _, _ in citing]

    if '--sample' in sys.argv:
        import random
        rnd = random.Random(20261014); pick = rnd.sample(samples, 30)
        path = sys.argv[sys.argv.index('--sample') + 1]
        with open(path, 'w', encoding='utf-8') as f:
            for k, (_, el, loc, ctx) in enumerate(pick, 1):
                f.write(f'#{k} [{el}] {loc}: {ctx}\n\n')
        with open(path + '.key', 'w', encoding='utf-8') as f:
            for k, (nm, el, loc, _) in enumerate(pick, 1):
                f.write(f'#{k} {nm}\n')
        print(len(samples), 'hits; sample written'); return

    # comparison: absent vs attested, one-sided Mann-Whitney (exact permutation over group labels)
    import itertools
    A = [r['share_decoded'] for r in results if r['group'] == 'absent']
    P = [r['share_decoded'] for r in results if r['group'] == 'attested']
    def U(x, y):
        return sum((a > b) + 0.5 * (a == b) for a in x for b in y)
    obs = U(A, P); pool = A + P; k = len(A); cnt = tot = 0
    for idx in itertools.combinations(range(len(pool)), k):
        x = [pool[i] for i in idx]; y = [pool[i] for i in range(len(pool)) if i not in idx]
        tot += 1; cnt += U(x, y) >= obs
    med = lambda v: sorted(v)[len(v) // 2] if len(v) % 2 else sum(sorted(v)[len(v) // 2 - 1:len(v) // 2 + 1]) / 2
    summary = {'absent_median_share': med(A), 'attested_median_share': med(P), 'U': obs, 'p_one_sided': cnt / tot,
               'n_absent': len(A), 'n_attested': len(P)}
    os.makedirs(OUT, exist_ok=True)
    tag = '_revised' if revised else ''
    json.dump({'protocol': 'docs/research_questions.md Q8 (fixed 2026-10-13)', 'measure': 'revised' if revised else 'first', 'coverage_sections': {w: [len(v), v[0], v[-1]] for w, v in coverage.items()},
               'results': results, 'summary': summary}, open(f'{OUT}/q8_results{tag}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(citing_dump, open(f'{OUT}/q8_sections{tag}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('coverage', {w: (len(v), v[0], v[-1]) for w, v in coverage.items()})
    for r in results:
        print(f"{r['group']:10s} {r['parable']:28s} elements {r['n_elements']:3d}  citing {r['citing_sections']:3d}  decoded {r['n_decoded']:3d}  share {r['share_decoded']:.2f}")
    print(summary)


if __name__ == '__main__':
    main()
