"""Strata for the pre-registered stylometric rerun (docs/stylometry/PREREGISTRATION.md §7), taken from
the audit's own classes in data/apparatus/luke_NN.json.

Mapping (primary run, --strata audit):  A+ → P;  A− → A;  U− and U? → U.
Sensitivity (--strata audit_um):        A+ → P;  A− and U− → A;  U? → U.
Luke 1:1–2:52 has no apparatus file: it is absent on explicit testimony (Tertullian, Marc. 4.7.1;
Epiphanius, Pan. 42.11.4) and is mapped to A, as in the Roth run.
A record covering part of a verse (e.g. 22:3, 21:35) carries the class of the verse as recorded."""
import glob, json, os, re

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _span(ref):
    m = re.match(r'^(\d+):(\d+)[a-z]?(?:–(\d+)[a-z]?)?$', ref)
    c, a = int(m.group(1)), int(m.group(2))
    b = int(m.group(3)) if m.group(3) else a
    return [(c, v) for v in range(a, b + 1)]


def audit_classes():
    out = {}
    for path in sorted(glob.glob(os.path.join(REPO, 'data', 'apparatus', 'luke_*.json'))):
        for r in json.load(open(path, encoding='utf-8'))['records']:
            for k in _span(r['ref']):
                if k in out:
                    raise SystemExit(f'{k} has two records')
                out[k] = r['class']
    return out


def audit_strata(luke_keys, u_minus_as_absent=False):
    cls = audit_classes()
    to = {'A+': 'P', 'A−': 'A', 'U?': 'U', 'U−': 'A' if u_minus_as_absent else 'U'}
    strata, missing = {}, []
    for k in luke_keys:
        if k[0] <= 2:
            strata[k] = 'A'
        elif k in cls:
            strata[k] = to[cls[k]]
        else:
            missing.append(k)
    if missing:
        raise SystemExit(f'no audit class for {missing[:10]}')
    return strata
