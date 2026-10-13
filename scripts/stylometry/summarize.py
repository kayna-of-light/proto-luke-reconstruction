"""Tabulate results across strata runs and apply the pre-registered decision labels (PREREG §6)."""
import json, os

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
RES = os.path.join(REPO, 'docs', 'stylometry', 'results')
RUNS = ['roth', 'audit', 'audit_um', 'harnack', 'klinghardt', 'nicolotti', 'beduhn', 'hahn', 'zahn']
KEY_CONDS = ['full', 'full, genre MH', 'no infancy/genealogy', 'no infancy/genealogy, genre MH',
             'markan only', 'non-markan only', 'no infancy, non-markan', 'no infancy, tradition MH',
             'strict P vs A', 'strict P vs A, no infancy']


def beyond(x):
    """Beyond the 95th percentile of both nulls."""
    return x['N1_p'] < 0.05 and x['N2_p'] < 0.05


def label(ft, fam):
    a = beyond(ft['full'][fam])
    b = beyond(ft['full, genre MH'][fam])
    c = beyond(ft['no infancy/genealogy'][fam]) and beyond(ft['no infancy/genealogy, genre MH'][fam])
    if a and b and c:
        return 'supported'
    if not c and not b:
        return 'not observed'
    return 'underdetermined'


def main():
    lines = []
    out = {}
    for run in RUNS:
        p = os.path.join(RES, run, 'results.json')
        if not os.path.exists(p):
            continue
        R = json.load(open(p, encoding='utf-8'))
        ft = R['family_tests']
        out[run] = {'counts': R['counts'], 'verse_score_auc': R['verse_score']['cv_auc'],
                    'labels': {f: label(ft, f) for f in ('F1', 'F2', 'F3')},
                    'conditions': {c: {f: {'RR': round(ft[c][f]['observed_rr'], 3),
                                           'N1_p': round(ft[c][f]['N1_p'], 4),
                                           'N2_p': round(ft[c][f]['N2_p'], 4)}
                                       for f in ('F1', 'F2', 'F3')} for c in KEY_CONDS if c in ft}}
        lines.append(f"{run}: P={R['counts']['P']} A={R['counts']['A']} U={R['counts']['U']} "
                     f"AUC={R['verse_score']['cv_auc']:.3f} labels={out[run]['labels']}")
        for c in KEY_CONDS:
            if c in ft:
                lines.append('   ' + c + ': ' + '  '.join(
                    f"{f} {ft[c][f]['observed_rr']:.2f}{'*' if beyond(ft[c][f]) else ''}" for f in ('F1', 'F2', 'F3')))
    with open(os.path.join(RES, 'summary.json'), 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
