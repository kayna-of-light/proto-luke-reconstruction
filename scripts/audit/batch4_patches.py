"""NA27 corrections to the SBLGNT base for Luke 14–17, each found by the OCR screen
(scripts/audit/na27_screen.py) and confirmed on the NA27 page image (pp. 208–218)."""
from buildlib import greek

PATCHES = {
    '16:12': [('τίς δώσει ὑμῖν', 'τίς ὑμῖν δώσει')],                         # NA27 order
    '17:12': [('ἀπήντησαν δέκα', 'ἀπήντησαν αὐτῷ δέκα')],                    # NA27 [αὐτῷ]
    '17:23': [('Ἰδοὺ ἐκεῖ· Ἰδοὺ ὧδε', 'Ἰδοὺ ἐκεῖ, ἤ· Ἰδοὺ ὧδε')],             # NA27 [ἤ]
}


def G(ref, extra=()):
    """NA27 Greek: SBLGNT + verified NA27 corrections + any reading adopted for the verse."""
    return greek(ref, PATCHES.get(ref, []) + list(extra))
