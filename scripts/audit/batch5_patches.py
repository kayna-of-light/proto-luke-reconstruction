"""NA27 corrections to the SBLGNT base for Luke 18–21, each found by the OCR screen
(scripts/audit/na27_screen.py) and confirmed on the NA27 page image (pp. 218–232)."""
from buildlib import greek

PATCHES = {
    '18:13': [('ἔτυπτε τὸ', 'ἔτυπτεν τὸ')],                                   # NA27 ἔτυπτεν
    '18:21': [('ἐκ νεότητος μου.', 'ἐκ νεότητος.')],                          # NA27 without μου
    '19:36': [('τὰ ἱμάτια ἑαυτῶν', 'τὰ ἱμάτια αὐτῶν')],                       # NA27 αὐτῶν (restored, METHOD §11)
    '19:38': [('ὁ ἐρχόμενος βασιλεὺς', 'ὁ ἐρχόμενος ὁ βασιλεὺς')],           # NA27 ὁ βασιλεύς
    '19:40': [('ὑμῖν, ὅτι ἐὰν', 'ὑμῖν, ἐὰν')],                                # NA27 without ὅτι
    '20:24': [('ἀποκριθέντες δὲ εἶπαν', 'οἱ δὲ εἶπαν')],                      # NA27 οἱ δέ
    '20:26': [('ἐπιλαβέσθαι τοῦ ῥήματος', 'ἐπιλαβέσθαι αὐτοῦ ῥήματος')],      # NA27 αὐτοῦ
    '20:44': [('αὐτὸν κύριον καλεῖ', 'κύριον αὐτὸν καλεῖ')],                  # NA27 order
    '21:11': [('φόβητρά τε καὶ σημεῖα ἀπ’ οὐρανοῦ μεγάλα', 'φόβητρά τε καὶ ἀπ’ οὐρανοῦ σημεῖα μεγάλα')],  # NA27 order
}


def G(ref, extra=()):
    """NA27 Greek: SBLGNT + verified NA27 corrections + any reading adopted for the verse."""
    return greek(ref, PATCHES.get(ref, []) + list(extra))
