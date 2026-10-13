"""NA27 corrections to the SBLGNT base for Luke 10–13, each found by the OCR screen
(scripts/audit/na27_screen.py) and confirmed on the NA27 page image (pp. 190–207)."""
from buildlib import greek

PATCHES = {
    '10:1': [('ὁ κύριος καὶ ἑτέρους', 'ὁ κύριος ἑτέρους')],                  # NA27 without καί
    '10:6': [('καὶ ἐὰν ᾖ ἐκεῖ', 'καὶ ἐὰν ἐκεῖ ᾖ'), ('μήγε', 'μή γε')],      # NA27 order
    '10:21': [('ἠγαλλιάσατο τῷ πνεύματι', 'ἠγαλλιάσατο ἐν τῷ πνεύματι'), ('ναί, ὁ πατήρ', 'ναὶ ὁ πατήρ')],   # NA27 [ἐν]; punctuation
    '11:14': [('δαιμόνιον κωφόν', 'δαιμόνιον καὶ αὐτὸ ἦν κωφόν')],          # NA27 [καὶ αὐτὸ ἦν]
    '11:20': [('θεοῦ ἐκβάλλω', 'θεοῦ ἐγὼ ἐκβάλλω')],                         # NA27 [ἐγώ]
    '11:33': [('τὸ φέγγος', 'τὸ φῶς')],                                       # NA27 φῶς
    '12:54': [('ἴδητε νεφέλην', 'ἴδητε τὴν νεφέλην')],                       # NA27 [τήν]
    '12:56': [('τὸν δὲ καιρὸν τοῦτον', 'τὸν καιρὸν δὲ τοῦτον')],             # NA27 order
    '13:21': [('ἔκρυψεν', 'ἐνέκρυψεν')],                                      # NA27 [ἐν]έκρυψεν
    '13:27': [('Οὐκ οἶδα πόθεν', 'Οὐκ οἶδα ὑμᾶς πόθεν')],                     # NA27 [ὑμᾶς]
}


def G(ref, extra=()):
    """NA27 Greek: SBLGNT + verified NA27 corrections + any reading adopted for the verse."""
    return greek(ref, PATCHES.get(ref, []) + list(extra))
