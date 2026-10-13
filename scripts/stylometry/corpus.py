"""Corpus loading for the stylometric baseline (docs/stylometry/PREREGISTRATION.md §2).

Sources are read from AUDIT_SRC (default /tmp/audit-src); nothing licensed is committed.
  AUDIT_SRC/sbl/NN-Xx-morphgnt.txt         MorphGNT/SBLGNT (github.com/morphgnt/sblgnt)
  AUDIT_SRC/bilby/roth_norm.txt            Bilby's normalized Roth dataset (Dataverse doi:10.7910/DVN/BYPOOR)
"""
import os, re, unicodedata
from collections import OrderedDict

SRC = os.environ.get('AUDIT_SRC', '/tmp/audit-src')

BOOKS = ['61-Mt', '62-Mk', '63-Lk', '64-Jn', '65-Ac', '66-Ro', '67-1Co', '68-2Co', '69-Ga', '70-Eph',
         '71-Php', '72-Col', '73-1Th', '74-2Th', '75-1Ti', '76-2Ti', '77-Tit', '78-Phm', '79-Heb',
         '80-Jas', '81-1Pe', '82-2Pe', '83-1Jn', '84-2Jn', '85-3Jn', '86-Jud', '87-Re']


def nfc(s):
    return unicodedata.normalize('NFC', s)


def bare(s):
    """Lower case without diacritics, for prefix tests (ἀρχ-, συ-, κατ-)."""
    d = unicodedata.normalize('NFD', s.lower())
    return ''.join(ch for ch in d if unicodedata.category(ch) != 'Mn')


class Tok:
    __slots__ = ('pos', 'person', 'tense', 'voice', 'mood', 'case', 'number', 'gender', 'degree', 'word', 'lemma')

    def __init__(self, pos, parse, word, lemma):
        self.pos = pos
        (self.person, self.tense, self.voice, self.mood,
         self.case, self.number, self.gender, self.degree) = parse
        self.word = nfc(word)
        self.lemma = nfc(lemma)


def read_book(code):
    """Return OrderedDict (chapter, verse) -> [Tok]."""
    verses = OrderedDict()
    with open(f'{SRC}/sbl/{code}-morphgnt.txt', encoding='utf-8') as f:
        for ln in f:
            p = ln.split()
            bcv, pos, parse, text, word, norm, lemma = p[0], p[1], p[2], p[3], p[4], p[5], p[6]
            key = (int(bcv[2:4]), int(bcv[4:6]))
            verses.setdefault(key, []).append(Tok(pos, parse, word, lemma))
    return verses


def read_nt():
    return {code: read_book(code) for code in BOOKS}


# ---- Marcion strata (Roth 2015 via Bilby's normalized dataset) -------------------------------

# Roth 2015, §3.2.2 (attested not present). 3:2–20 is in Roth's unattested list (§3.2.3: "though
# indirectly attested as not present"); it was wrongly in the pre-registered enumeration (PREREG §9.2).
ROTH_ABSENT = ['1:1-2:52', '3:21-38', '4:1-13', '8:19', '11:30-32', '11:49-51', '12:6',
               '13:1-9', '13:29-35', '15:11-32', '18:31-33', '19:29-46', '20:9-17', '20:37', '21:18',
               '21:21-22', '22:16', '22:35-38', '22:50-51', '23:43']


def expand(spec, luke_keys):
    m = re.match(r'^(\d+):(\d+)(?:-(?:(\d+):)?(\d+))?$', spec)
    c1, v1 = int(m.group(1)), int(m.group(2))
    if m.group(4) is None:
        return [(c1, v1)]
    c2 = int(m.group(3)) if m.group(3) else c1
    v2 = int(m.group(4))
    return [k for k in luke_keys if (c1, v1) <= k <= (c2, v2)]


def roth_present():
    """Verse keys with an entry in Bilby's normalized Roth dataset (P). Entries whose only content
    is an omission mark "([])" (23:34a, 23:34b) are not P (PREREGISTRATION §2)."""
    present = set()
    with open(f'{SRC}/bilby/roth_norm.txt', encoding='utf-8') as f:
        for ln in f:
            m = re.match(r'(\d\d)\.(\d\d)[a-d]?\.\w+\s+(.*)$', ln.strip())
            if not m:
                continue
            body = m.group(3)
            content = re.sub(r'[\(\)\[\]\s]', '', body)
            # "()" = attested, wording not recoverable (present); "([])" = attested as omitted (not present)
            if content or '[' not in body:
                present.add((int(m.group(1)), int(m.group(2))))
    return present


RECON_FILES = {'roth': 'roth_norm.txt', 'harnack': 'harnack_norm.txt', 'klinghardt': 'klinghardt_norm.txt',
               'nicolotti': 'nicolotti_norm.txt', 'beduhn': 'beduhn_norm.txt', 'hahn': 'hahn_norm.txt',
               'zahn': 'zahn_norm.txt'}


def recon_present(name):
    """Verse keys a reconstruction prints (Bilby's normalized datasets on Dataverse). A verse counts
    as present unless its only content is an omission mark "[]"."""
    if name == 'roth':
        return roth_present()
    present = set()
    with open(f'{SRC}/bilby/{RECON_FILES[name]}', encoding='utf-8-sig') as f:
        for ln in f:
            ln = ln.strip()
            if name == 'beduhn':
                m = re.match(r'"(\d+)","(\d+)[a-d]?","[^"]*","(.*)"\s*$', ln)
            else:
                m = re.match(r'(\d\d)\.(\d\d)[a-d]?\.\w+\s*(.*)$', ln)
            if not m or int(m.group(2)) == 0:
                continue
            body = m.group(3)
            content = re.sub(r'[\(\)\[\]\s]', '', body)
            if content or '[' not in body:
                present.add((int(m.group(1)), int(m.group(2))))
    return present


def roth_strata(luke_keys, present_from='roth'):
    P = recon_present(present_from)
    A = set()
    for spec in ROTH_ABSENT:
        A.update(expand(spec, luke_keys))
    A -= P
    return {k: ('P' if k in P else 'A' if k in A else 'U') for k in luke_keys}
