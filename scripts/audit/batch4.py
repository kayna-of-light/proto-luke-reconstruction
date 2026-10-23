"""Batch 4 build: Luke 14:1–17:37 → reconstruction chapters 12–15 (with 4:27 inside 17:12–14).
Usage: AUDIT_SRC=<dir with local source copies> python3 -I scripts/audit/batch4.py"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from buildlib import REPO, build_chapter, write_apparatus, ref_key, dump_json
import batch4_ch12 as C12, batch4_ch13 as C13, batch4_ch14 as C14, batch4_ch15 as C15

CHAPTERS = [(12, C12), (13, C13), (14, C14), (15, C15)]
LUKE_RANGE = {14: range(1, 36), 15: range(1, 33), 16: range(1, 32), 17: [v for v in range(1, 38) if v != 36]}  # NA27 has no 17:36

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
    # write apparatus; a verse printed outside its Luke chapter (4:27) updates the record
    # already in that chapter's file instead of replacing the file
    for lc, recs in records.items():
        path = f'{REPO}/data/apparatus/luke_{lc:02d}.json'
        if lc not in LUKE_RANGE:
            doc = json.load(open(path, encoding='utf-8'))
            for rec in recs:
                hit = [i for i, r in enumerate(doc['records']) if r['ref'] == rec['ref']]
                if len(hit) != 1:
                    sys.exit(f'{rec["ref"]}: expected one existing record in {path}')
                doc['records'][hit[0]] = rec
            dump_json(doc, path)
            continue
        recs.sort(key=lambda r: ref_key(r['ref'].split('–')[0]))
        write_apparatus(lc, recs, path)
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
