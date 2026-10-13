"""Batch 2 build: Luke 7:1–9:62 → reconstruction chapters 4–7.
Usage: AUDIT_SRC=<dir with local source copies> python3 -I scripts/audit/batch1.py"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from buildlib import REPO, build_chapter, write_apparatus, ref_key, dump_json
import batch2_ch4 as C4, batch2_ch5 as C5, batch2_ch6 as C6, batch2_ch7 as C7

CHAPTERS = [(4, C4), (5, C5), (6, C6), (7, C7)]
LUKE_RANGE = {7: range(1, 51), 8: range(1, 57), 9: range(1, 63)}

def expand(ref):
    c, vs = ref.split(':')
    c = int(c)
    if '–' in vs:
        a, b = vs.split('–')
        return [(c, v) for v in range(int(a), int(b) + 1)]
    return [(c, int(vs))]

def main():
    data = json.load(open(f'{REPO}/data/proto_luke.json', encoding='utf-8'))
    records, covered, problems = {}, {}, []
    new_chapters = {}
    for num, mod in CHAPTERS:
        ch = build_chapter(num, mod.PREAMBLE, mod.ENTRIES, mod.NOTES)
        new_chapters[num] = ch
        for i, e in enumerate(mod.ENTRIES, 1):
            rec = {'ref': e['ref'], 'class': e['cls']}
            rec.update(e['app'])
            rec['reconstruction'] = f'chapter {num}, verse {i}'
            lc = ref_key(e['ref'])[0]
            records.setdefault(lc, []).append(rec)
            for cv in expand(e['ref']):
                covered.setdefault(cv, []).append(e['ref'])
            if e.get('restored'):
                # printed by METHOD §11: keeps its class; must carry the reason and must not also be flagged
                if e.get('flag') or not e['app'].get('decision', '').startswith('printed, restored by method'):
                    problems.append(f'{e["ref"]} restored without the §11 decision, or also flagged')
            elif e['cls'] in ('A−', 'U−'):
                problems.append(f'{e["ref"]} printed but class {e["cls"]}')
            elif e['cls'] == 'U?' and not e.get('flag'):
                problems.append(f'{e["ref"]} U? printed without flag')
            if e['cls'] == 'A+' and e.get('flag'):
                problems.append(f'{e["ref"]} A+ flagged')
        for o in mod.OMITTED:
            rec = {'ref': o['ref'], 'class': o['cls']}
            rec.update(o['app'])
            lc = ref_key(o['ref'].split('–')[0])[0]
            records.setdefault(lc, []).append(rec)
            for cv in expand(o['ref']):
                covered.setdefault(cv, []).append(o['ref'])
    # coverage: every verse of the range has exactly one record
    for c, rng in LUKE_RANGE.items():
        for v in rng:
            n = len(covered.get((c, v), []))
            if n != 1:
                problems.append(f'{c}:{v} has {n} records {covered.get((c, v))}')
    # terminology
    blob = json.dumps(new_chapters, ensure_ascii=False)
    for bad in ['the Messenger', 'The Messenger', 'Soma Pneumatikon', 'spiritual body', 'NotebookLM', 'forensic', 'Forensic']:
        if bad in blob:
            problems.append(f'terminology: {bad!r} present')
    if problems:
        print('PROBLEMS:'); print('\n'.join(problems)); sys.exit(1)
    # write apparatus
    for lc, recs in records.items():
        recs.sort(key=lambda r: ref_key(r['ref'].split('–')[0]))
        write_apparatus(lc, recs, f'{REPO}/data/apparatus/luke_{lc:02d}.json')
    # replace the batch's chapters
    for i, ch in enumerate(data['chapters']):
        if ch['chapter'] in new_chapters:
            data['chapters'][i] = new_chapters[ch['chapter']]
    dump_json(data, f'{REPO}/data/proto_luke.json')
    for num, ch in new_chapters.items():
        fl = sum(1 for v in ch['verses'] if v.get('attestation') == 'unattested')
        rs = sum(1 for v in ch['verses'] if v.get('attestation') == 'restored')
        print(f'chapter {num}: {len(ch["verses"])} verses ({fl} flagged, {rs} restored), {len(ch["notes"])} notes')
    print('apparatus:', sorted(records))

if __name__ == '__main__':
    main()
