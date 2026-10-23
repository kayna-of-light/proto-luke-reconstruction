"""Feature families F1–F5 exactly as fixed in docs/stylometry/PREREGISTRATION.md §4."""
from collections import Counter
from corpus import bare, nfc

NOMINAL = {'N-', 'A-', 'RA', 'RP', 'RD', 'RI', 'RR'}
L = nfc  # lemma literal helper


def lem(t, x):
    return t.lemma == L(x)


def is_part(t):
    return t.mood == 'P'


def is_inf(t):
    return t.mood == 'N'


def count_where(toks, pred):
    return sum(1 for i in range(len(toks)) if pred(toks, i))


def f_pros_acc(ts, i):
    if not lem(ts[i], 'πρός'):
        return False
    for t in ts[i + 1:]:
        if t.pos in NOMINAL and t.case != '-':
            return t.case == 'A'
    return False


def f_after(lemma_a, pred_b, k):
    def f(ts, i):
        return lem(ts[i], lemma_a) and any(pred_b(t) for t in ts[i + 1:i + 1 + k])
    return f


def f_lemma(x, pos=None, mood=None, case=None):
    def f(ts, i):
        t = ts[i]
        return (lem(t, x) and (pos is None or t.pos == pos) and (mood is None or t.mood == mood)
                and (case is None or t.case == case))
    return f


def f_prefix(prefixes, pos=None):
    def f(ts, i):
        t = ts[i]
        return (pos is None or t.pos == pos) and bare(t.lemma).startswith(prefixes)
    return f


def f_part_de(ts, i):
    return is_part(ts[i]) and i + 1 < len(ts) and lem(ts[i + 1], 'δέ')


def f_kai_egeneto(ts, i):
    if not lem(ts[i], 'καί') or i + 1 >= len(ts):
        return False
    t = ts[i + 1]
    return lem(t, 'γίνομαι') and t.tense == 'A' and t.mood == 'I' and t.person == '3' and t.number == 'S'


def f_archo_inf(ts, i):
    t = ts[i]
    return lem(t, 'ἄρχω') and t.pos == 'V' + '-' and not is_inf(t) and any(is_inf(u) for u in ts[i + 1:i + 5])


def f_gen_art_inf(ts, i):
    return ts[i].pos == 'RA' and ts[i].case == 'G' and i + 1 < len(ts) and is_inf(ts[i + 1])


def f_lego_de_pros(ts, i):
    if not lem(ts[i], 'λέγω') or i + 1 >= len(ts) or not lem(ts[i + 1], 'δέ'):
        return False
    return any(lem(t, 'πρός') for t in ts[i + 2:i + 4])


def f_kata_acc_art(ts, i):
    return lem(ts[i], 'κατά') and i + 1 < len(ts) and ts[i + 1].pos == 'RA' and ts[i + 1].case == 'A'


def f_art_de_part(ts, i):
    return (ts[i].pos == 'RA' and i + 2 < len(ts) and lem(ts[i + 1], 'δέ') and is_part(ts[i + 2]))


def f_en_to_inf(ts, i):
    return (lem(ts[i], 'ἐν') and i + 1 < len(ts) and ts[i + 1].pos == 'RA' and ts[i + 1].case == 'D'
            and any(is_inf(t) for t in ts[i + 2:i + 4]))


def f_ou_me_subj(ts, i):
    return (lem(ts[i], 'οὐ') and i + 1 < len(ts) and lem(ts[i + 1], 'μή')
            and any(t.mood == 'S' for t in ts[i + 2:i + 5]))


def f_art_then(lemma, mood):
    def f(ts, i):
        return (ts[i].pos == 'RA' and i + 1 < len(ts) and lem(ts[i + 1], lemma) and ts[i + 1].mood == mood)
    return f


def f_eimi_part(ts, i):
    return lem(ts[i], 'εἰμί') and i + 1 < len(ts) and is_part(ts[i + 1])


def make_f1(luke_only_lemmas, gospel_hapax_lemmas):
    V = 'V-'
    feats = [
        ('01 πρός + acc', f_pros_acc),
        ('02 participle + δέ', f_part_de),
        ('03 λέγω participle', f_lemma('λέγω', mood='P')),
        ('04 passive participle', lambda ts, i: ts[i].mood == 'P' and ts[i].voice == 'P'),
        ('05 ἀρχ- root', f_prefix(('αρχ',))),
        ('06 λέγω … πρός (≤2)', f_after('λέγω', lambda t: lem(t, 'πρός'), 2)),
        ('07 aorist middle participle', lambda ts, i: ts[i].tense == 'A' and ts[i].voice == 'M' and ts[i].mood == 'P'),
        ('08 periphrastic εἰμί + ptc', f_eimi_part),
        ('09 ἄγγελος', f_lemma('ἄγγελος')),
        ('10 Lukan NT hapax', lambda ts, i: ts[i].lemma in luke_only_lemmas),
        ('11 ἄρχω (verb)', f_lemma('ἄρχω', pos=V)),
        ('12 γάρ', f_lemma('γάρ')),
        ('13 συ- verbs', f_prefix(('συ',), pos=V)),
        ('14 ἰδού', f_lemma('ἰδού')),
        ('15 καὶ ἐγένετο', f_kai_egeneto),
        ('16 πόλις', f_lemma('πόλις')),
        ('17 λαός', f_lemma('λαός')),
        ('18 γίνομαι participle', f_lemma('γίνομαι', mood='P')),
        ('19 ὄχλος', f_lemma('ὄχλος')),
        ('20 ἄρχω + infinitive', f_archo_inf),
        ('21 ἀποκρίνομαι participle', f_lemma('ἀποκρίνομαι', mood='P')),
        ('22 ἡμέρα', f_lemma('ἡμέρα')),
        ('23 ἕτερος', f_lemma('ἕτερος')),
        ('24 ἐνώπιον', f_lemma('ἐνώπιον')),
        ('25 gen. articular infinitive', f_gen_art_inf),
        ('26 λέγω δέ πρός', f_lego_de_pros),
        ('27 κατά + acc. article', f_kata_acc_art),
        ('28 λέγω infinitive', f_lemma('λέγω', mood='N')),
        ('29 ῥῆμα', f_lemma('ῥῆμα')),
        ('30 ἀρχι- compounds', f_prefix(('αρχι',))),
        ('31 ὁράω participle', f_lemma('ὁράω', mood='P')),
        ('32 article + δέ + participle', f_art_de_part),
        ('33 ἐπερωτάω', f_lemma('ἐπερωτάω')),
        ('34 ἑαυτοῦ', f_lemma('ἑαυτοῦ')),
        ('35 ἐν τῷ + infinitive', f_en_to_inf),
        ('36 πλήν', f_lemma('πλήν')),
        ('37 οὐ μή + subjunctive', f_ou_me_subj),
        ('38 ἔτος', f_lemma('ἔτος')),
        ('39 article + καλέω ptc', f_art_then('καλέω', 'P')),
        ('40 θέλω', f_lemma('θέλω')),
        ('41 καλέω participle', f_lemma('καλέω', mood='P')),
        ('42 θαυμάζω', f_lemma('θαυμάζω')),
        ('43 πίμπλημι', f_lemma('πίμπλημι')),
        ('44 present passive infinitive', lambda ts, i: ts[i].tense == 'P' and ts[i].voice == 'P' and ts[i].mood == 'N'),
        ('45 ἅπτω', f_lemma('ἅπτω')),
        ('46 ἕως', f_lemma('ἕως')),
        ('47 ὅστις', f_lemma('ὅστις')),
        ('48 καλέω', f_lemma('καλέω')),
        ('49 οὖν', f_lemma('οὖν')),
        ('50 μέλλω', f_lemma('μέλλω')),
        ('51 δεῖ', f_lemma('δεῖ')),
        ('52 ἅπας', f_lemma('ἅπας')),
        ('53 ἀλλήλων', f_lemma('ἀλλήλων')),
        ('54 πληρ- lemmas', f_prefix(('πληρ',))),
        ('55 article + γίνομαι ptc', f_art_then('γίνομαι', 'P')),
        ('56 superlative', lambda ts, i: ts[i].degree == 'S'),
        ('57 ὄνομα nominative', f_lemma('ὄνομα', case='N')),
        ('58 ἀνίστημι participle', f_lemma('ἀνίστημι', mood='P')),
        ('59 Gospel hapax (not Mt/Mk/Jn)', lambda ts, i: ts[i].lemma in gospel_hapax_lemmas),
        ('60 perfect participle', lambda ts, i: ts[i].tense == 'X' and ts[i].mood == 'P'),
        ('61 αὐτός', f_lemma('αὐτός')),
        ('62 κατα- verbs', f_prefix(('κατ', 'καθ'), pos=V)),
    ]
    return feats


def verse_feature_counts(verse_toks, feats):
    return [count_where(verse_toks, f) for _, f in feats]


def lemma_counts(book):
    c = Counter()
    for toks in book.values():
        c.update(t.lemma for t in toks)
    return c


def n_words(book):
    return sum(len(v) for v in book.values())


def hawkins_lemmas(luke, mt, mk):
    """F2: ≥4 in Luke, and absent from Mt+Mk or Luke count ≥ 2 × (Mt+Mk count)."""
    cl, cm, ck = lemma_counts(luke), lemma_counts(mt), lemma_counts(mk)
    return {l for l, n in cl.items() if n >= 4 and (cm[l] + ck[l] == 0 or n >= 2 * (cm[l] + ck[l]))}


def acts_lemmas(acts, mt, mk):
    """F3: ≥4 in Acts, and Acts rate ≥ 2 × (Mt+Mk) rate; or absent from Mt+Mk. No Luke data."""
    ca, cm, ck = lemma_counts(acts), lemma_counts(mt), lemma_counts(mk)
    wa, wmk = n_words(acts), n_words(mt) + n_words(mk)
    out = set()
    for l, n in ca.items():
        if n < 4:
            continue
        m = cm[l] + ck[l]
        if m == 0 or (n / wa) >= 2 * (m / wmk):
            out.add(l)
    return out


F5_FIELDS = [('POS', 'pos'), ('tense', 'tense'), ('voice', 'voice'), ('mood', 'mood')]


def f5_categories(luke):
    cats = set()
    for toks in luke.values():
        for t in toks:
            for name, attr in F5_FIELDS:
                val = getattr(t, attr)
                if val != '-':
                    cats.add((name, val))
    return sorted(cats)


def f5_counts(verse_toks, cats):
    c = Counter()
    for t in verse_toks:
        for name, attr in F5_FIELDS:
            val = getattr(t, attr)
            if val != '-':
                c[(name, val)] += 1
    return [c[k] for k in cats]
