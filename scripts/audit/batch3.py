"""Batch 3 build: Luke 10:1–13:35 → reconstruction chapters 8–11.
Usage: AUDIT_SRC=<dir with local source copies> python3 -I scripts/audit/batch3.py"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from buildlib import REPO, build_chapter, write_apparatus, ref_key, dump_json
import batch3_ch8 as C8, batch3_ch9 as C9, batch3_ch10 as C10, batch3_ch11 as C11

CHAPTERS = [(8, C8), (9, C9), (10, C10), (11, C11)]
LUKE_RANGE = {10: range(1, 43), 11: range(1, 55), 12: range(1, 60), 13: range(1, 36)}

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
            if e['cls'] in ('A−', 'U−'):
                problems.append(f'{e["ref"]} printed but class {e["cls"]}')
            if e['cls'] == 'U?' and not e.get('flag'):
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
        fl = sum(1 for v in ch['verses'] if v.get('attestation'))
        print(f'chapter {num}: {len(ch["verses"])} verses ({fl} flagged), {len(ch["notes"])} notes')
    print('apparatus:', sorted(records))

if __name__ == '__main__':
    main()
