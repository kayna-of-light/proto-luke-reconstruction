"""Stylometric baseline, as pre-registered in docs/stylometry/PREREGISTRATION.md.

Usage:  AUDIT_SRC=<sources> python3 scripts/stylometry/baseline.py [--strata roth|audit|audit_um|<edition>]
Writes docs/stylometry/results/<strata>/results.json, verse_scores.csv and features.csv.
"""
import argparse, csv, json, math, os, sys
from collections import Counter
import numpy as np
from scipy.stats import binomtest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from corpus import read_nt, roth_strata, expand, nfc
from features import (make_f1, verse_feature_counts, hawkins_lemmas, acts_lemmas, lemma_counts,
                      f5_categories, f5_counts)

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
SEED = 20261012
N2_DRAWS = 10000
FIRST_PERSON_SECOND = {nfc(x) for x in ('ἐγώ', 'σύ', 'ἡμεῖς', 'ὑμεῖς')}
STOP = {nfc(x) for x in ('ὁ', 'καί', 'δέ', 'αὐτός', 'εἰμί')}


# ---------------------------------------------------------------- statistics

def rate_ratio(kN, wN, kP, wP):
    a, b = (kN, kP) if kN > 0 and kP > 0 else (kN + 0.5, kP + 0.5)
    rr = (a / wN) / (b / wP)
    se = math.sqrt(1 / a + 1 / b)
    return rr, rr * math.exp(-1.96 * se), rr * math.exp(1.96 * se)


def binom_p(kN, wN, kP, wP, alternative):
    k = kN + kP
    if k == 0:
        return 1.0
    return binomtest(kN, k, wN / (wN + wP), alternative=alternative).pvalue


def holm(ps):
    order = sorted(range(len(ps)), key=lambda i: ps[i])
    adj, running = [0.0] * len(ps), 0.0
    for rank, i in enumerate(order):
        running = max(running, min(1.0, (len(ps) - rank) * ps[i]))
        adj[i] = running
    return adj


def log_rr(mask, f, w):
    kN, wN = f[mask].sum(), w[mask].sum()
    kP, wP = f[~mask].sum(), w[~mask].sum()
    if kN == 0 or kP == 0:
        kN, kP = kN + 0.5, kP + 0.5
    return math.log((kN / wN) / (kP / wP))


def log_rr_mh(mask, f, w, strata):
    """Mantel–Haenszel pooled log rate ratio across strata (labels array)."""
    num = den = 0.0
    for s in np.unique(strata):
        m = strata == s
        kN, wN = f[m & mask].sum(), w[m & mask].sum()
        kP, wP = f[m & ~mask].sum(), w[m & ~mask].sum()
        W = wN + wP
        if wN == 0 or wP == 0:
            continue
        num += kN * wP / W
        den += kP * wN / W
    return math.log(num / den) if num > 0 and den > 0 else float('nan')


def runs(mask):
    out, start = [], 0
    for i in range(1, len(mask) + 1):
        if i == len(mask) or mask[i] != mask[start]:
            out.append((bool(mask[start]), i - start))
            start = i
    return out


def null_masks(mask):
    """N1: all circular shifts. N2: block permutation (N-runs and P-runs permuted separately)."""
    n = len(mask)
    n1 = [np.roll(mask, s) for s in range(1, n)]
    rng = np.random.default_rng(SEED)
    rr = runs(mask)
    n_runs = [l for v, l in rr if v]
    p_runs = [l for v, l in rr if not v]
    first_is_n = rr[0][0]
    n2 = []
    for _ in range(N2_DRAWS):
        nr = rng.permutation(n_runs)
        pr = rng.permutation(p_runs)
        seq, ni, pi, turn_n = [], 0, 0, first_is_n
        while ni < len(nr) or pi < len(pr):
            if turn_n and ni < len(nr):
                seq.extend([True] * nr[ni]); ni += 1
            elif not turn_n and pi < len(pr):
                seq.extend([False] * pr[pi]); pi += 1
            turn_n = not turn_n
        n2.append(np.array(seq))
    return n1, n2


def null_summary(obs, n1, n2):
    return {'observed_log_rr': obs, 'observed_rr': math.exp(obs),
            'N1_p': float((np.sum(n1 >= obs) + 1) / (len(n1) + 1)),
            'N1_q95_rr': float(math.exp(np.quantile(n1, 0.95))),
            'N2_p': float((np.sum(n2 >= obs) + 1) / (len(n2) + 1)),
            'N2_q95_rr': float(math.exp(np.quantile(n2, 0.95)))}


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--strata', default='roth',
                    choices=['roth', 'audit', 'audit_um', 'harnack', 'klinghardt', 'nicolotti', 'beduhn', 'hahn', 'zahn'])
    args = ap.parse_args()

    nt = read_nt()
    luke, mt, mk, jn, acts = nt['63-Lk'], nt['61-Mt'], nt['62-Mk'], nt['64-Jn'], nt['65-Ac']
    keys = list(luke.keys())

    if args.strata not in ('audit', 'audit_um'):
        # P from the named reconstruction; A = Roth's attested-absent list minus P; U = the rest
        strata = roth_strata(keys, present_from=args.strata)
    else:
        sys.path.insert(0, os.path.join(REPO, 'scripts', 'audit'))
        from audit_strata import audit_strata  # written when the audit is complete (PREREG §7)
        strata = audit_strata(keys, u_minus_as_absent=(args.strata == 'audit_um'))

    cls = np.array([strata[k] for k in keys])
    w = np.array([len(luke[k]) for k in keys], dtype=float)
    isN = cls != 'P'

    # lemma sets
    other_nt = Counter()
    for code, book in nt.items():
        if code != '63-Lk':
            other_nt.update(lemma_counts(book))
    luke_lem = lemma_counts(luke)
    luke_only = {l for l in luke_lem if other_nt[l] == 0}
    mmj = lemma_counts(mt) + lemma_counts(mk) + lemma_counts(jn)
    gospel_hapax = {l for l in luke_lem if mmj[l] == 0}
    F1 = make_f1(luke_only, gospel_hapax)
    F2 = hawkins_lemmas(luke, mt, mk)
    F3 = acts_lemmas(acts, mt, mk)
    F5c = f5_categories(luke)

    # per-verse matrices
    f1 = np.array([verse_feature_counts(luke[k], F1) for k in keys], dtype=float)
    f2 = np.array([sum(t.lemma in F2 for t in luke[k]) for k in keys], dtype=float)
    f3 = np.array([sum(t.lemma in F3 for t in luke[k]) for k in keys], dtype=float)
    f5 = np.array([f5_counts(luke[k], F5c) for k in keys], dtype=float)

    # genre
    def speech(toks):
        for t in toks:
            if t.pos == 'V-' and t.person in ('1', '2'):
                return True
            if t.lemma in FIRST_PERSON_SECOND:
                return True
        return False
    genre = np.array(['speech' if speech(luke[k]) else 'narrative' for k in keys])

    # infancy narrative and genealogy
    infancy = set(expand('1:1-2:52', keys)) | set(expand('3:23-38', keys))
    keep_noinf = np.array([k not in infancy for k in keys])

    # Markan detector
    def bigrams(toks):
        ls = [t.lemma for t in toks if t.lemma not in STOP]
        return {(a, b) for a, b in zip(ls, ls[1:])}
    index = {}
    for mkey, toks in mk.items():
        for bg in bigrams(toks):
            index.setdefault(bg, set()).add(mkey)
    markan = []
    for k in keys:
        hits = Counter()
        for bg in bigrams(luke[k]):
            for mkey in index.get(bg, ()):
                hits[mkey] += 1
        markan.append(any(v >= 2 for v in hits.values()))
    markan = np.array(markan)
    detector_ok = 250 <= markan.sum() <= 550
    tradition = np.where(markan, 'markan', 'non-markan')

    R = {'strata': args.strata,
         'counts': {c: int((cls == c).sum()) for c in ('P', 'A', 'U')},
         'words': {c: int(w[cls == c].sum()) for c in ('P', 'A', 'U')},
         'family_sizes': {'F1': len(F1), 'F2_lemmas': len(F2), 'F3_lemmas': len(F3), 'F5_categories': len(F5c)},
         'genre_counts': {g: int((genre == g).sum()) for g in ('speech', 'narrative')},
         'markan_detector': {'flagged': int(markan.sum()), 'accepted': bool(detector_ok)}}

    # ---- per-feature tests (full text, P vs N)
    def feature_rows(names, mat, alternative):
        rows, ps = [], []
        wN, wP = w[isN].sum(), w[~isN].sum()
        for j, name in enumerate(names):
            kN, kP = int(mat[isN, j].sum()), int(mat[~isN, j].sum())
            rr, lo, hi = rate_ratio(kN, wN, kP, wP)
            p = binom_p(kN, wN, kP, wP, alternative)
            rows.append({'feature': name, 'k_N': kN, 'k_P': kP, 'rate_N': 1000 * kN / wN,
                         'rate_P': 1000 * kP / wP, 'RR': rr, 'CI_low': lo, 'CI_high': hi, 'p': p})
            ps.append(p)
        for r, a in zip(rows, holm(ps)):
            r['p_holm'] = a
        return rows

    R['F1'] = feature_rows([n for n, _ in F1], f1, 'greater')
    R['F2_F3_sums'] = feature_rows(['F2 Hawkins Luke vocabulary (sum)', 'F3 Acts vocabulary (sum)'],
                                   np.column_stack([f2, f3]), 'greater')
    # single lemmas of F2 and F3
    def lemma_mat(lemset):
        ls = sorted(lemset)
        idx = {l: i for i, l in enumerate(ls)}
        m = np.zeros((len(keys), len(ls)))
        for vi, k in enumerate(keys):
            for t in luke[k]:
                if t.lemma in idx:
                    m[vi, idx[t.lemma]] += 1
        return ls, m
    l2, m2 = lemma_mat(F2)
    l3, m3 = lemma_mat(F3)
    R['F2_lemmas'] = feature_rows(l2, m2, 'greater')
    R['F3_lemmas'] = feature_rows(l3, m3, 'greater')
    R['F5'] = feature_rows([f'{a}={b}' for a, b in F5c], f5, 'two-sided')

    # ---- family statistic under nulls and controls
    fam = {'F1': f1.sum(axis=1), 'F2': f2, 'F3': f3}
    conds = {}

    def run_cond(label, sel, mask_all, strat=None):
        out = {}
        wsel, msel = w[sel], mask_all[sel]
        m1, m2 = null_masks(msel)
        for name, fv in fam.items():
            fsel = fv[sel]
            if strat is None:
                stat = lambda m: log_rr(m, fsel, wsel)
            else:
                ssel = strat[sel]
                stat = lambda m: log_rr_mh(m, fsel, wsel, ssel)
            obs = stat(msel)
            n1 = np.array([stat(m) for m in m1])
            n2 = np.array([stat(m) for m in m2])
            out[name] = null_summary(obs, n1, n2)
        out['n_verses'] = int(sel.sum()); out['n_N'] = int((msel).sum())
        conds[label] = out

    allv = np.ones(len(keys), dtype=bool)
    run_cond('full', allv, isN)
    run_cond('full, genre MH', allv, isN, genre)
    run_cond('speech only', genre == 'speech', isN)
    run_cond('narrative only', genre == 'narrative', isN)
    run_cond('no infancy/genealogy', keep_noinf, isN)
    run_cond('no infancy/genealogy, genre MH', keep_noinf, isN, genre)
    if detector_ok:
        run_cond('markan only', markan, isN)
        run_cond('non-markan only', ~markan, isN)
        run_cond('no infancy, non-markan', ~markan & keep_noinf, isN)
        run_cond('no infancy, tradition MH', keep_noinf, isN, tradition)
    strictsel = cls != 'U'
    run_cond('strict P vs A', strictsel, cls == 'A')
    run_cond('strict P vs A, no infancy', strictsel & keep_noinf, cls == 'A')
    R['family_tests'] = conds

    # ---- F4 Delta
    def seg_freq(lemma_counter, total, fw):
        return np.array([lemma_counter[l] / total for l in fw])
    def seg_counter(sel):
        c = Counter()
        for k, s in zip(keys, sel):
            if s:
                c.update(t.lemma for t in luke[k])
        return c, sum(len(luke[k]) for k, s in zip(keys, sel) if s)
    delta = {}
    segs_src = {'P': ~isN, 'N': isN, 'A': cls == 'A', 'N_no_infancy': isN & keep_noinf}
    for nfw in (50, 100, 200):
        fw = [l for l, _ in luke_lem.most_common(nfw)]
        segs = {}
        for name, sel in segs_src.items():
            c, tot = seg_counter(sel)
            segs[name] = seg_freq(c, tot, fw)
        for name, book in (('Acts', acts), ('Mark', mk), ('Matthew', mt)):
            segs[name] = seg_freq(lemma_counts(book), sum(len(v) for v in book.values()), fw)
        names = list(segs)
        M = np.vstack([segs[n] for n in names])
        mu, sd = M.mean(axis=0), M.std(axis=0, ddof=1)
        sd[sd == 0] = 1
        Z = (M - mu) / sd
        D = {a: {b: float(np.mean(np.abs(Z[i] - Z[j]))) for j, b in enumerate(names)} for i, a in enumerate(names)}
        delta[str(nfw)] = D
    R['F4_delta'] = delta

    # ---- §7 verse score
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import StratifiedKFold, cross_val_predict
    from sklearn.metrics import roc_auc_score
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    fw100 = [l for l, _ in luke_lem.most_common(100)]
    fidx = {l: i for i, l in enumerate(fw100)}
    X = np.zeros((len(keys), 102))
    for vi, k in enumerate(keys):
        n = len(luke[k])
        for t in luke[k]:
            if t.lemma in fidx:
                X[vi, fidx[t.lemma]] += 1 / n
        X[vi, 100] = f2[vi] / n
        X[vi, 101] = f3[vi] / n
    train = (cls != 'U') & keep_noinf
    y = (cls[train] == 'A').astype(int)
    model = make_pipeline(StandardScaler(), LogisticRegression(C=1.0, max_iter=5000))
    cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=SEED)
    prob = cross_val_predict(model, X[train], y, cv=cv, method='predict_proba')[:, 1]
    auc = roc_auc_score(y, prob)
    model.fit(X[train], y)
    score_all = model.predict_proba(X)[:, 1]
    R['verse_score'] = {'n_train_P': int((y == 0).sum()), 'n_train_A': int((y == 1).sum()),
                        'cv_auc': float(auc), 'usable': bool(auc >= 0.70)}

    out = os.path.join(REPO, 'docs', 'stylometry', 'results', args.strata)
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, 'results.json'), 'w', encoding='utf-8') as fh:
        json.dump(R, fh, ensure_ascii=False, indent=1)
    with open(os.path.join(out, 'verse_scores.csv'), 'w', newline='', encoding='utf-8') as fh:
        wr = csv.writer(fh)
        wr.writerow(['ref', 'class', 'genre', 'markan', 'words', 'F1', 'F2', 'F3', 'score_absent'])
        for vi, k in enumerate(keys):
            wr.writerow([f'{k[0]}:{k[1]}', cls[vi], genre[vi], int(markan[vi]), int(w[vi]),
                         int(f1[vi].sum()), int(f2[vi]), int(f3[vi]), round(float(score_all[vi]), 4)])
    with open(os.path.join(out, 'lemma_sets.json'), 'w', encoding='utf-8') as fh:
        json.dump({'F2_hawkins': sorted(F2), 'F3_acts': sorted(F3)}, fh, ensure_ascii=False, indent=0)
    print(json.dumps({k: R[k] for k in ('counts', 'words', 'family_sizes', 'genre_counts', 'markan_detector', 'verse_score')}, ensure_ascii=False))


if __name__ == '__main__':
    main()
