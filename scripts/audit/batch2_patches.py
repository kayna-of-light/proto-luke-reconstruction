"""NA27 corrections to the SBLGNT base for Luke 7–9, each found by the OCR screen
(scripts/audit/na27_screen.py) and confirmed on the NA27 page image (pp. 175–190)."""
from buildlib import greek

PATCHES = {
    '7:22': [('λεπροὶ καθαρίζονται, κωφοὶ', 'λεπροὶ καθαρίζονται καὶ κωφοὶ')],   # NA27 °καί
    '8:20': [('ἰδεῖν σε θέλοντες', 'ἰδεῖν θέλοντές σε')],                       # NA27 order
    '9:18': [('Τίνα με οἱ ὄχλοι λέγουσιν εἶναι;', 'Τίνα με λέγουσιν οἱ ὄχλοι εἶναι;')],
    '9:48': [('Ὃς ἂν δέξηται τοῦτο', 'Ὃς ἐὰν δέξηται τοῦτο')],
    '9:62': [('εἶπεν δὲ ὁ Ἰησοῦς·', 'εἶπεν δὲ πρὸς αὐτὸν ὁ Ἰησοῦς·')],          # NA27 [πρὸς αὐτόν]
}


def G(ref, extra=()):
    """NA27 Greek: SBLGNT + verified NA27 corrections + any reading adopted for the verse."""
    return greek(ref, PATCHES.get(ref, []) + list(extra))
