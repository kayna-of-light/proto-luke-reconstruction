"""Rerun of the exploratory checks E1 and E3 on the audit's classes (PREREGISTRATION §7: "the whole
analysis is rerun with the audit's own classes"). E2 measures Roth's attested wording, not the strata,
and is not rerun. Also lists the F2 lemmas that drive the N-versus-P difference outside Luke 1–2.

Usage: AUDIT_SRC=<sources> python3 scripts/stylometry/rerun_audit.py [audit|audit_um]
Writes docs/stylometry/results/<strata>/exploratory.json."""
import json, os, sys
from collections import Counter
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import exploratory as X
from corpus import read_nt, expand
from features import hawkins_lemmas

sys.path.insert(0, os.path.join(X.REPO, 'scripts', 'audit'))
from audit_strata import audit_strata


def main():
    name = sys.argv[1] if len(sys.argv) > 1 else 'audit'
    um = name == 'audit_um'
    # E1 and E3 call roth_strata(keys); point them at the audit's classes
    X.roth_strata = lambda keys, present_from='roth': audit_strata(keys, u_minus_as_absent=um)
    nt = read_nt()
    out = {'E1': X.e1(nt), 'E3': X.e3(nt)}

    luke, mt, mk = nt['63-Lk'], nt['61-Mt'], nt['62-Mk']
    keys = list(luke.keys())
    st = audit_strata(keys, u_minus_as_absent=um)
    infancy = set(expand('1:1-2:52', keys)) | set(expand('3:23-38', keys))
    F2 = hawkins_lemmas(luke, mt, mk)
    cN, cP, wN, wP = Counter(), Counter(), 0, 0
    for k in keys:
        if k in infancy:
            continue
        toks = luke[k]
        if st[k] == 'P':
            wP += len(toks); cP.update(t.lemma for t in toks if t.lemma in F2)
        else:
            wN += len(toks); cN.update(t.lemma for t in toks if t.lemma in F2)
    drivers = sorted(((l, cN[l], cP[l], (cN[l] / wN) / ((cP[l] + 0.5) / wP)) for l in F2 if cN[l] + cP[l] >= 5),
                     key=lambda r: -(r[1] - r[2] * wN / wP))[:15]
    out['F2_drivers_no_infancy'] = [{'lemma': l, 'k_N': a, 'k_P': b, 'RR': round(r, 2)} for l, a, b, r in drivers]
    out['words_no_infancy'] = {'N': wN, 'P': wP}

    path = os.path.join(X.REPO, 'docs', 'stylometry', 'results', name, 'exploratory.json')
    json.dump(out, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for lab, d in out['E1'].items():
        print('E1', lab)
        for n, x in d.items():
            print(f"   {n}: RR {x['observed_rr']:.3f} N1 p={x['N1_p']:.4f} N2 p={x['N2_p']:.4f}")
    for k, v in out['E3'].items():
        print('E3', k, {a: round(b, 4) for a, b in v.items()})
    print('F2 drivers:', ', '.join(f"{d['lemma']} {d['k_N']}/{d['k_P']}" for d in out['F2_drivers_no_infancy']))


if __name__ == '__main__':
    main()
