"""Exploratory checks, NOT pre-registered (docs/stylometry/PREREGISTRATION.md §9 lists them).

E1  F2/F3 family tests with proper names removed (capitalized lemmas), and F1 without the two
    hapax counts (features 10 and 59), because these measure content more than style.
E2  Quotation-fragment check on Bilby's method: for the verses Roth attests, compare how many
    occurrences of each feature survive in Roth's attested wording (Bilby's normalized morph
    dataset, unaltered) against canonical Luke's wording of the same verses, for Bilby's Lk2
    signature features and for neutral control words. If the signature features survive at about
    the rate of the neutral words, a low Lk1 rate reflects selective quotation, not authorship.
"""
import json, math, os, re, sys
from collections import Counter
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from corpus import read_nt, roth_strata, roth_present, expand, nfc, SRC
from features import make_f1, verse_feature_counts, hawkins_lemmas, acts_lemmas, lemma_counts
import baseline as B

REPO = B.REPO


def e1(nt):
    luke, mt, mk, acts = nt['63-Lk'], nt['61-Mt'], nt['62-Mk'], nt['65-Ac']
    keys = list(luke.keys())
    cls = np.array([roth_strata(keys)[k] for k in keys])
    isN = cls != 'P'
    w = np.array([len(luke[k]) for k in keys], dtype=float)
    infancy = set(expand('1:1-2:52', keys)) | set(expand('3:23-38', keys))
    keep = np.array([k not in infancy for k in keys])
    proper = lambda l: l[:1].isupper()
    F2 = {l for l in hawkins_lemmas(luke, mt, mk) if not proper(l)}
    F3 = {l for l in acts_lemmas(acts, mt, mk) if not proper(l)}
    other = Counter()
    for code, book in nt.items():
        if code != '63-Lk':
            other.update(lemma_counts(book))
    ll = lemma_counts(luke)
    mmj = lemma_counts(mt) + lemma_counts(mk) + lemma_counts(nt['64-Jn'])
    F1 = [f for f in make_f1({l for l in ll if other[l] == 0}, {l for l in ll if mmj[l] == 0})
          if not f[0].startswith(('10 ', '59 '))]
    fam = {'F1 without hapax counts': np.array([sum(verse_feature_counts(luke[k], F1)) for k in keys], float),
           'F2 without names': np.array([sum(t.lemma in F2 for t in luke[k]) for k in keys], float),
           'F3 without names': np.array([sum(t.lemma in F3 for t in luke[k]) for k in keys], float)}
    out = {}
    for label, sel in (('full', np.ones(len(keys), bool)), ('no infancy/genealogy', keep)):
        res = {}
        m1, m2 = B.null_masks(isN[sel])
        for name, fv in fam.items():
            stat = lambda m: B.log_rr(m, fv[sel], w[sel])
            obs = stat(isN[sel])
            res[name] = B.null_summary(obs, np.array([stat(m) for m in m1]), np.array([stat(m) for m in m2]))
        out[label] = res
    return out


# ---- E2 ---------------------------------------------------------------------------------------

def roth_morph_tokens():
    """{(c, v): [(lemma, tag, uncertain)]} from Bilby's normalized morph file (Roth's wording)."""
    out = {}
    with open(f'{SRC}/bilby/roth_morph.txt', encoding='utf-8') as f:
        for ln in f:
            m = re.match(r'(\d\d)\.(\d\d)[a-d]?\.\w+\s+(.*)$', ln.strip())
            if not m:
                continue
            key = (int(m.group(1)), int(m.group(2)))
            depth, toks = 0, out.setdefault(key, [])
            for piece in re.findall(r'\(|\)|\[|\]|[^\s()\[\]]+', m.group(3)):
                if piece in '([':
                    depth += 1
                elif piece in ')]':
                    depth -= 1
                elif '@' in piece:
                    lemma, tag = piece.split('@', 1)
                    toks.append((nfc(lemma), tag, depth > 0))
    return out


def roth_counts(toks, certain_only):
    ts = [(l, t) for l, t, u in toks if not (certain_only and u)]
    c = Counter()
    for i, (l, t) in enumerate(ts):
        nxt = ts[i + 1] if i + 1 < len(ts) else ('', '')
        c['words'] += 1
        c['πρός + acc'] += l == nfc('πρός') and t.startswith('pa')
        c['participle + δέ'] += t.startswith('vp') and nxt[0] == nfc('δέ')
        c['λέγω … πρός'] += l == nfc('λέγω') and any(x[0] == nfc('πρός') for x in ts[i + 1:i + 3])
        c['καὶ ἐγένετο'] += l == nfc('καί') and nxt[0] == nfc('γίνομαι') and nxt[1].startswith('via')
        c['periphrastic'] += l == nfc('εἰμί') and nxt[1].startswith('vp')
        c['ἐν τῷ + inf'] += (l == nfc('ἐν') and nxt[0] == nfc('ὁ') and nxt[1].startswith('dd')
                             and any(x[1].startswith('vn') for x in ts[i + 2:i + 4]))
        c['δέ'] += l == nfc('δέ')
        c['καί'] += l == nfc('καί')
        c['article'] += t.startswith('d') and l == nfc('ὁ')
        c['αὐτός'] += l == nfc('αὐτός')
        c['nouns'] += t.startswith('n')
        c['finite verbs'] += t.startswith('vi')
    return c


def canon_counts(toks):
    c = Counter()
    for i, t in enumerate(toks):
        nxt = toks[i + 1] if i + 1 < len(toks) else None
        L = t.lemma
        c['words'] += 1
        c['πρός + acc'] += 0  # filled below with the F1 definition
        c['δέ'] += L == nfc('δέ')
        c['καί'] += L == nfc('καί')
        c['article'] += t.pos == 'RA'
        c['αὐτός'] += L == nfc('αὐτός')
        c['nouns'] += t.pos == 'N-'
        c['finite verbs'] += t.pos == 'V-' and t.mood in 'ISDO'
    return c


def e2(nt):
    luke = nt['63-Lk']
    roth = roth_morph_tokens()
    P = roth_present()
    F1 = dict(make_f1(set(), set()))
    f1map = {'πρός + acc': '01 πρός + acc', 'participle + δέ': '02 participle + δέ',
             'λέγω … πρός': '06 λέγω … πρός (≤2)', 'καὶ ἐγένετο': '15 καὶ ἐγένετο',
             'periphrastic': '08 periphrastic εἰμί + ptc', 'ἐν τῷ + inf': '35 ἐν τῷ + infinitive'}
    res = {}
    for certain_only in (False, True):
        rc, cc = Counter(), Counter()
        for k in sorted(P):
            if k not in luke:
                continue
            rc.update(roth_counts(roth.get(k, []), certain_only))
            c = canon_counts(luke[k])
            for short, full in f1map.items():
                c[short] = sum(1 for i in range(len(luke[k])) if F1[full](luke[k], i))
            cc.update(c)
        rows = {}
        for feat in ['words', 'nouns', 'finite verbs', 'αὐτός', 'article', 'καί', 'δέ'] + list(f1map):
            rows[feat] = {'canonical_same_verses': cc[feat], 'roth_wording': rc[feat],
                          'retained': (rc[feat] / cc[feat]) if cc[feat] else None}
        res['certain words only' if certain_only else 'all words incl. uncertain'] = rows
    return res


def main():
    nt = read_nt()
    out = {'E1': e1(nt), 'E2': e2(nt)}
    path = os.path.join(REPO, 'docs', 'stylometry', 'results', 'roth', 'exploratory.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    for lab, d in out['E1'].items():
        print('E1', lab)
        for n, x in d.items():
            print(f"   {n}: RR {x['observed_rr']:.3f} | N1 q95 {x['N1_q95_rr']:.3f} p={x['N1_p']:.4f} | N2 q95 {x['N2_q95_rr']:.3f} p={x['N2_p']:.4f}")
    for lab, rows in out['E2'].items():
        print('E2', lab)
        for f, r in rows.items():
            print(f"   {f}: canonical {r['canonical_same_verses']}  Roth {r['roth_wording']}  retained {r['retained']:.2f}")


if __name__ == '__main__':
    main()


# ---- E3: block-shift null for the F4 Delta contrast (exploratory) -------------------------------

def e3(nt, nfw=100):
    luke, mk, acts = nt['63-Lk'], nt['62-Mk'], nt['65-Ac']
    keys = list(luke.keys())
    cls = np.array([roth_strata(keys)[k] for k in keys])
    isN = cls != 'P'
    ll = lemma_counts(luke)
    fw = [l for l, _ in ll.most_common(nfw)]
    idx = {l: i for i, l in enumerate(fw)}
    C = np.zeros((len(keys), nfw))
    w = np.array([len(luke[k]) for k in keys], float)
    for vi, k in enumerate(keys):
        for t in luke[k]:
            if t.lemma in idx:
                C[vi, idx[t.lemma]] += 1
    def ref(book):
        c = lemma_counts(book); n = sum(len(v) for v in book.values())
        return np.array([c[l] / n for l in fw])
    A, M = ref(acts), ref(mk)
    infancy = set(expand('1:1-2:52', keys)) | set(expand('3:23-38', keys))
    keep = np.array([k not in infancy for k in keys])

    def genre_of(toks):
        return any((t.pos == 'V-' and t.person in '12') or t.lemma in B.FIRST_PERSON_SECOND for t in toks)
    speech = np.array([genre_of(luke[k]) for k in keys])

    def stat(mask, sel):
        Cs, ws, ms = C[sel], w[sel], mask
        fP = Cs[~ms].sum(0) / ws[~ms].sum(); fN = Cs[ms].sum(0) / ws[ms].sum()
        Mx = np.vstack([fP, fN, A, M]); mu, sd = Mx.mean(0), Mx.std(0, ddof=1); sd[sd == 0] = 1
        Z = (Mx - mu) / sd
        d = lambda a, b: np.mean(np.abs(Z[a] - Z[b]))
        # positive when N is closer to Acts than P is, and P closer to Mark than N is
        return (d(0, 2) - d(1, 2)) + (d(1, 3) - d(0, 3))
    out = {}
    for label, sel in (('full', np.ones(len(keys), bool)), ('no infancy/genealogy', keep),
                       ('no infancy, narrative only', keep & ~speech), ('no infancy, speech only', keep & speech)):
        m = isN[sel]
        obs = stat(m, sel)
        m1, m2 = B.null_masks(m)
        n1 = np.array([stat(x, sel) for x in m1]); n2 = np.array([stat(x, sel) for x in m2])
        out[label] = {'observed': float(obs), 'N1_p': float((np.sum(n1 >= obs) + 1) / (len(n1) + 1)),
                      'N2_p': float((np.sum(n2 >= obs) + 1) / (len(n2) + 1))}
    return out


if __name__ == '__main__' and os.environ.get('RUN_E3'):
    r = e3(read_nt())
    path = os.path.join(REPO, 'docs', 'stylometry', 'results', 'roth', 'exploratory_e3.json')
    json.dump(r, open(path, 'w', encoding='utf-8'), indent=1)
    for k, v in r.items():
        print('E3', k, v)
