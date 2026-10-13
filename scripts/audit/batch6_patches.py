"""NA27 corrections to the SBLGNT base for Luke 22–24, each found by the OCR screen
(scripts/audit/na27_screen.py) or by reading the page, and confirmed on the NA27 page image
(pp. 232–243)."""
from buildlib import greek

PATCHES = {
    '22:7': [('ἀζύμων, ᾗ ἔδει', 'ἀζύμων, ἐν ᾗ ἔδει')],                       # NA27 [ἐν]
    '22:18': [('ὑμῖν, οὐ μὴ πίω', 'ὑμῖν, ὅτι οὐ μὴ πίω')],                    # NA27 [ὅτι]
    '22:19': [('μου [τὸ ὑπὲρ', 'μου τὸ ὑπὲρ')],                               # NA27 prints 19b–20 without brackets
    '22:20': [('ἐκχυννόμενον].', 'ἐκχυννόμενον.')],
    '23:2': [('λέγοντα αὑτὸν', 'λέγοντα ἑαυτὸν')],                          # NA27 ἑαυτόν
    '23:12': [('πρὸς αὑτούς', 'πρὸς αὐτούς')],                              # NA27 αὐτούς
    '23:20': [('προσεφώνησεν, θέλων', 'προσεφώνησεν αὐτοῖς θέλων')],       # NA27 αὐτοῖς
    '23:50': [('ὑπάρχων, ἀνὴρ ἀγαθὸς', 'ὑπάρχων καὶ ἀνὴρ ἀγαθὸς')],       # NA27 [καί]
    '23:56': [('κατὰ τὴν ἐντολήν,', 'κατὰ τὴν ἐντολήν.')],                  # NA27 ends the verse
    '24:3': [('οὐχ εὗρον τὸ σῶμα.', 'οὐχ εὗρον τὸ σῶμα τοῦ κυρίου Ἰησοῦ.')],  # NA27 prints the words (WNI)
    '24:36': [('ἐν μέσῳ αὐτῶν.', 'ἐν μέσῳ αὐτῶν καὶ λέγει αὐτοῖς· Εἰρήνη ὑμῖν.')],  # NA27 prints 36b (WNI)
    '24:40': [('[καὶ τοῦτο', 'καὶ τοῦτο'), ('τοὺς πόδας.]', 'τοὺς πόδας.')],  # NA27 prints the verse without brackets
    '24:47': [('μετάνοιαν καὶ ἄφεσιν', 'μετάνοιαν εἰς ἄφεσιν')],              # NA27 εἰς
}


def G(ref, extra=()):
    """NA27 Greek: SBLGNT + verified NA27 corrections + any reading adopted for the verse."""
    return greek(ref, PATCHES.get(ref, []) + list(extra))
