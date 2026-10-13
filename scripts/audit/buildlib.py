"""Shared helpers for the audit build scripts (one script per batch)."""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sbl import load as load_sbl

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
SBL = load_sbl()


def dump_json(obj, path):
    """Write JSON in the repository's layout: indent 2, scalar lists on one line."""
    t = json.dumps(obj, ensure_ascii=False, indent=2)
    t = re.sub(r'\[\s*\n\s*((?:-?\d+|"[^"\n]*")(?:,\s*\n\s*(?:-?\d+|"[^"\n]*"))*)\s*\n\s*\]',
               lambda m: '[' + re.sub(r',\s*\n\s*', ', ', m.group(1)) + ']', t)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(t + '\n')


def ref_key(ref):
    c, v = ref.split(':')
    return int(c), int(re.match(r'\d+', v).group())


def greek(ref, patches=(), text=None):
    """NA27 Greek for a verse: SBLGNT base with patches (old, new) checked against
    the NA27 page image. Each patch must match exactly once."""
    g = text if text is not None else SBL[ref_key(ref)]
    for old, new in patches:
        n = g.count(old)
        if n != 1:
            raise SystemExit(f'{ref}: patch {old!r} matched {n} times in {g!r}')
        g = g.replace(old, new)
    return g


def build_chapter(number, preamble, entries, notes, title=None):
    verses = []
    for i, e in enumerate(entries, 1):
        v = {'verse': i, 'canonical_ref': 'Luke ' + e['ref'],
             'english': e['en'], 'greek': e['gr']}
        if e.get('flag'):
            v['attestation'] = 'unattested'
        verses.append(v)
    index = {e['ref']: i for i, e in enumerate(entries, 1)}
    out_notes = []
    for j, n in enumerate(notes, 1):
        refs = []
        for r in n['refs']:
            if r not in index:
                raise SystemExit(f'note {n["term"]!r}: {r} not printed in chapter {number}')
            refs.append(index[r])
        out_notes.append({'id': j, 'term': n['term'], 'verse_refs': refs,
                          'category': n['cat'], 'explanation': n['text']})
    return {'chapter': number, 'title': title or f'Proto-Luke Chapter {number}',
            'preamble': preamble, 'verses': verses, 'notes': out_notes}


def write_apparatus(luke_ch, records, path):
    doc = {
        'luke_chapter': luke_ch,
        'base_text': 'NA27 (= NA28 in Luke), checked against the page images',
        'classes': {'A+': 'attested present', 'A−': 'attested absent',
                    'U−': 'unattested, probably absent', 'U?': 'unattested, undetermined'},
        'method': 'docs/audit/METHOD.md',
        'records': records,
    }
    dump_json(doc, path)
