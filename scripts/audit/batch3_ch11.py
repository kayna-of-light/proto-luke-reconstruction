"""Batch 3, chapter 11 of the reconstruction: Luke 13:1–35."""
from buildlib import greek
from batch1_ch2 import U, A
from batch3_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}

ENTRIES = [
 U('13:10', G('13:10'), 'And he was teaching in one of the assemblies on the sabbaths.', 'Opens the attested pericope 13:10–17.'),
 U('13:11', G('13:11'), 'And look, a woman having a spirit of weakness for eighteen years, and she was bent together and unable to straighten up at all.', 'Inside the attested pericope 13:10–17.'),
 U('13:12', G('13:12'), 'And seeing her, Jesus called to her and said to her, "Woman, you have been released from your weakness,"', 'Inside the attested pericope 13:10–17.'),
 U('13:13', G('13:13'), 'and he laid his hands on her; and at once she was made straight, and she was giving glory to God.', 'Inside the attested pericope 13:10–17.'),
 A('13:14', G('13:14'), 'But the ruler of the assembly, answering, indignant because Jesus had healed on the sabbath, was saying to the crowd, "There are six days on which one must work; so come on those and be healed, and not on the day of the sabbath."',
   'present (Marc. 4.30.1)', [T('4.30.1', '"Quaestionem rursus de curatione sabbato facta quomodo discussit?"')]),
 A('13:15', G('13:15'), 'But the lord answered him and said, "Play-actors! Does not each of you on the sabbath loose his ox or his donkey from the manger and lead it away to give it drink?',
   'present (Marc. 4.30.1)', [T('4.30.1', '"Unusquisque vestrum sabbatis non solvit asinum aut bovem suum a praesepi et ducit ad potum?"')],
   wording='NA27. Tertullian names the donkey first and has "on the sabbaths"; Roth: order uncertain, plural possible only.'),
 A('13:16', G('13:16'), 'And this woman, being a daughter of Abraham, whom Satan bound, look, eighteen years, was it not necessary that she be loosed from this bond on the day of the sabbath?"',
   'present (Pan. 42.11.6, sch. 39)', [E(39, '»ταύτην δὲ θυγατέρα Ἀβραάμ, ἣν ἔδησεν ὁ Σατανᾶς«.')]),
 U('13:17', G('13:17'), 'And as he was saying these things, all who were opposed to him were put to shame, and the whole crowd was rejoicing at all the glorious things being done by him.', 'Inside the attested pericope 13:10–17.'),
 U('13:18', G('13:18'), 'So he was saying, "What is the kingdom of God like, and to what shall I liken it?', 'Inside the attested paragraph 13:18–19.'),
 A('13:19', G('13:19'), 'It is like a grain of mustard, which a person took and threw into his own garden; and it grew and became a tree, and the birds of the sky settled in its branches."',
   'present (Marc. 4.30.1–2)', [T('4.30.1', '"Simile est regnum dei, inquit, grano sinapis, quod accepit homo et seminavit in horto suo."')],
   wording='NA27. Tertullian\'s "seminavit in horto suo" (ἔσπειρεν ἐν τῷ κήπῳ αὐτοῦ?) is rated possible only by Roth; not adopted.'),
 A('13:20', G('13:20'), 'And again he said, "To what shall I liken the kingdom of God?',
   'present (Marc. 4.30.3)', [T('4.30.3', '"De sequenti plane similitudine… Fermento enim comparavit illud".')]),
 A('13:21', G('13:21'), 'It is like leaven, which a woman took and hid in three measures of flour, until the whole was leavened."',
   'present (Marc. 4.30.3)', [T('4.30.3', '"Fermento enim comparavit illud, non azymis quae familiariora sunt creatori."')],
   wording='NA27 [ἐν]έκρυψεν, printed without the brackets (SBLGNT ἔκρυψεν — checked on the page image).'),
 U('13:23', G('13:23'), 'And someone said to him, "Lord, are those being saved few?" And he said to them,', 'Inside the attested paragraph 13:23–30.'),
 U('13:24', G('13:24'), '"Struggle to go in through the narrow door, because many, I tell you, will seek to go in and will not be strong enough.', 'Inside the attested paragraph 13:23–30.'),
 A('13:25', G('13:25'), "From the time the master of the house has got up and shut the door, and you begin to stand outside and to knock at the door, saying, 'Lord, open to us,' then answering he will say to you, 'I do not know you, where you are from.'",
   'present (Marc. 4.30.4)', [T('4.30.4', '"Cum surrexerit, inquit, pater familiae… et cluserit ostium… Quibus pulsantibus respondebit, Nescio unde sitis".')]),
 A('13:26', G('13:26'), "Then you will begin to say, 'We ate and drank before you, and you taught in our streets.'",
   'present (Marc. 4.30.4)', [T('4.30.4', '"et rursus enumerantibus quod coram illo ederint et biberint et in plateis eorum docuerit".')]),
 A('13:27', G('13:27'), "And he will say, speaking to you, 'I do not know you, where you are from. Stand away from me, all you workers of injustice.'",
   'present (Marc. 4.30.4)', [T('4.30.4', '"adiciet, Recedite a me omnes operarii iniquitatis."')],
   wording='NA27, including its bracketed [ὑμᾶς] (SBLGNT omits it — checked on the page image). Tertullian\'s iniquitatis may render ἀνομίας (Ps 6:9; D); Roth: possible only.'),
 A('13:28', G('13:28', [('ὅταν ὄψησθε Ἀβραὰμ καὶ Ἰσαὰκ καὶ Ἰακὼβ καὶ πάντας τοὺς προφήτας ἐν τῇ βασιλείᾳ τοῦ θεοῦ, ὑμᾶς δὲ ἐκβαλλομένους ἔξω.',
                         'ὅταν ὄψησθε πάντας τοὺς δικαίους ἐν τῇ βασιλείᾳ τοῦ θεοῦ, ὑμᾶς δὲ κρατουμένους ἔξω.')]),
   'There, there will be the weeping and the grinding of the teeth, when you see all the just in the kingdom of God, but yourselves held outside."',
   'present (Marc. 4.30.4–5; Pan. 42.11.6, sch. 40)',
   [E(40, 'παρέκοψε πάλιν τὸ »τότε ὄψεσθε Ἀβραὰμ καὶ Ἰσαὰκ καὶ Ἰακὼβ καὶ πάντας τοὺς προφήτας ἐν τῇ βασιλείᾳ τοῦ θεοῦ«· ἀντὶ δὲ τούτου ἐποίησεν »ὅτε πάντας τοὺς δικαίους ἴδητε ἐν τῇ βασιλείᾳ τοῦ θεοῦ, ὑμᾶς δὲ ἐκβαλλομένους« — ἐποίησε δὲ »κρατουμένους« — »ἔξω«.'),
    T('4.30.4–5', '"Illic erit fletus et frendor dentium. Ubi? foris scilicet, ubi erunt exclusi… cum videbunt iustos introeuntes in regnum dei, se vero detineri foris."')],
   wording=('Marcionite readings adopted: "all the just" for "Abraham and Isaac and Jacob and all the prophets", and κρατουμένους ("held") for ἐκβαλλομένους ("thrown out"). Epiphanius states both, correcting himself in the scholion from ἐκβαλλομένους to κρατουμένους; Tertullian has "iustos" and "se vero detineri foris". Roth: secure. '
            'Tertullian\'s "introeuntes" ("entering") is rated possible only and is not printed; "all" is Epiphanius\' and stood in NA27\'s phrase.')),
]

OMITTED = [
 dict(ref='13:1–9', cls='A−', app=dict(roth='absent', witnesses=[
      E(38, 'ἦν παρακεκομμένον ἀπὸ τοῦ »ἦλθόν τινες ἀναγγέλλοντες αὐτῷ περὶ τῶν Γαλιλαίων…« ἕως ὅπου λέγει περὶ τῶν ἐν τῷ Σιλωὰμ δεκαοκτὼ ἀποθανόντων ἐν τῷ πύργῳ, καὶ τὸ »ἐὰν μὴ μετανοήσητε« καὶ τὰ ἑξῆς ἕως τῆς παραβολῆς τῆς συκῆς…')],
      decision='not printed', reason='Epiphanius states that everything from the report about the Galileans whose blood Pilate mixed with their sacrifices, through the tower in Siloam and "unless you repent", to the parable of the fig tree, was not in the text. Tertullian passes from 12:59 (4.29.16) to 13:14 (4.30.1); Roth counts his silence as confirmation (tacitus).')),
 dict(ref='13:22', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='"He went through towns and villages, teaching and journeying toward Jerusalem." A one-verse NA27 paragraph with no attested verse (METHOD §4.3).')),
 dict(ref='13:29–35', cls='A−', app=dict(roth='absent', witnesses=[
      E(41, 'παρέκοψε πάλιν τὸ »ἥξουσιν ἀπὸ ἀνατολῶν καὶ δυσμῶν…« καὶ τὸ »οἱ ἔσχατοι ἔσονται πρῶτοι« καὶ τὸ »προσῆλθον οἱ Φαρισαῖοι λέγοντες, ἔξελθε καὶ πορεύου, ὅτι Ἡρῴδης σε θέλει ἀποκτεῖναι«… ἕως ὅπου εἶπεν »οὐκ ἐνδέχεται προφήτην ἀπολέσθαι ἔξω Ἱερουσαλήμ« καὶ τὸ »Ἱερουσαλήμ, Ἱερουσαλήμ…« … καὶ τὸ »οὐ μὴ ἴδητέ με, ἕως οὗ εἴπητε· εὐλογημένος«.')],
      decision='not printed', reason='Epiphanius lists each saying of 13:29–35 as absent: the many coming from east and west, the last who will be first, the warning about Herod and the reply to "that fox", no prophet perishing outside Jerusalem, and the lament over Jerusalem. Tertullian passes from 13:28 (4.30.6) to 14:12 (4.31.1); Roth counts his silence as confirmation (tacitus).')),
]

PREAMBLE = (
 "Something in us has been held fast for so long that it has forgotten what it was to be free. On the day set "
 "apart for rest, it is loosed.\n\n"
 "Whatever keeps the order of our worship is indignant. There are other days for that. And yet every one of us "
 "unties an animal on that same day and leads it to water.\n\n"
 "What grows in us starts smaller than anything: a seed thrown into our own garden that ends up with birds in "
 "its branches, a little leaven hidden in the whole of the dough until all of it rises.\n\n"
 "And there is a door. One day it is shut, and some of us are outside, knocking, reminding the master that we "
 "ate and drank with him. He does not know where we are from."
)

NOTES = [
 dict(term='Not printed: 13:1–9', cat='excision', refs=['13:10'], text=(
  "Epiphanius, sch. 38: the text \"was cut off\" from \"some came and told him about the Galileans whose blood Pilate had mixed "
  "with their sacrifices\", through the eighteen killed by the tower in Siloam and \"unless you repent\", to the parable of the "
  "fig tree and the vinedresser's \"I will dig and put on manure; and if it does not bear fruit, cut it down\". Tertullian goes "
  "from 12:59 to the sabbath healing (13:14). The charge of cutting is Epiphanius'. What it reports as content is that the "
  "passage was not in the text.")),
 dict(term='The bent woman (13:10–17)', cat='textual', refs=['13:10', '13:14', '13:15', '13:16', '13:17'], text=(
  "Tertullian, Marc. 4.30.1: asked again about a healing on the sabbath, Christ answers \"Does not each of you on the sabbaths "
  "untie his donkey or ox from the manger and lead it to drink?\" Tertullian concludes that he \"confirmed the law, not "
  "dissolved it\", since the law permits work done to save a life. Epiphanius, sch. 39 quotes 13:16: \"this daughter of Abraham, "
  "whom Satan bound\". 13:10–13 and 13:17 are not cited and are printed in grey.")),
 dict(term='Mustard seed and leaven (13:18–21)', cat='textual', refs=['13:18', '13:19', '13:20', '13:21'], text=(
  "Tertullian, Marc. 4.30.1–3 quotes the mustard seed \"which a man took and sowed in his garden\" and asks whose garden the "
  "world is. Of the leaven he says mockingly that the kingdom of the other God might be compared to leaven because the "
  "Creator prefers unleavened bread. 13:18 is not cited and is printed in grey. 13:22, a travel notice, forms a paragraph "
  "that no witness cites and is not printed.")),
 dict(term='The shut door and \"all the just\" (13:23–28)', cat='textual', refs=['13:23', '13:24', '13:25', '13:26', '13:27', '13:28'], text=(
  "Tertullian, Marc. 4.30.4–6: the master of the house rises and shuts the door; to those knocking he answers \"I do not know "
  "where you are from\"; to those who say they ate and drank before him and that he taught in their streets, \"Depart from me, "
  "all workers of iniquity. There will be weeping and gnashing of teeth\", \"when they see the just entering the kingdom "
  "of God and themselves held outside\". Epiphanius, sch. 40 confirms the wording: the text had \"all the just\" where "
  "canonical Luke has \"Abraham and Isaac and Jacob and all the prophets\", and \"held\" (κρατουμένους) outside. 13:23–24 are not "
  "cited and are printed in grey.")),
 dict(term='Not printed: 13:29–35', cat='excision', refs=['13:28'], text=(
  "Epiphanius, sch. 41 names every saying of 13:29–35 as absent: people coming from east and west to recline in the kingdom, "
  "\"the last will be first\", the Pharisees' warning about Herod, the answer to \"that fox\", \"no prophet can perish outside "
  "Jerusalem\", and the lament \"Jerusalem, Jerusalem\" with \"you will not see me until you say, Blessed…\". Tertullian goes "
  "from 13:28 to 14:12.")),
 dict(term='The just in the kingdom', cat='theological', refs=['13:16', '13:28'], text=(
  "Interpretation. In the attested text those seen in the kingdom are \"all the just\", not the patriarchs and prophets "
  "by name, while the woman healed on the sabbath is still \"a daughter of Abraham\" (13:16). The text therefore does not cut "
  "the tie to Abraham. It describes the kingdom by justness, not by descent. The leader of the Jerusalem community was "
  "remembered as James \"the Just\" (Gospel of Thomas 12; Carriers of Living Water §3.1). Whether \"the just\" in this "
  "saying reflects that usage cannot be shown from the witnesses. The readings themselves are attested by two witnesses; why "
  "canonical Luke has the patriarchs instead (as Matt 8:11 does) they do not say.")),
 dict(term='ἐν τοῖς σάββασιν, "on the sabbaths"', cat='translation', refs=['13:10'], text='Plural, as at 4:31.'),
 dict(term='πνεῦμα ἔχουσα ἀσθενείας, "having a spirit of weakness"', cat='translation', refs=['13:11'], text='Word for word. In 13:16 the text names its cause: Satan bound her.'),
 dict(term='συγκύπτουσα, "bent together"', cat='translation', refs=['13:11'], text='Bent double, stooped.'),
 dict(term='ἀνακύψαι εἰς τὸ παντελές, "straighten up at all"', cat='translation', refs=['13:11'], text='To raise oneself up. εἰς τὸ παντελές can mean "at all" or "fully".'),
 dict(term='Γύναι, "Woman"', cat='translation', refs=['13:12'], text='A plain, respectful address, as the Greek has it.'),
 dict(term='ἀπολέλυσαι, "you have been released"', cat='translation', refs=['13:12'], text='ἀπολύω, to set free, as at 6:37. A perfect passive: released, and remaining free.'),
 dict(term='ἀνωρθώθη, "she was made straight"', cat='translation', refs=['13:13'], text='A passive: she was set upright.'),
 dict(term='ὁ ἀρχισυνάγωγος, "the ruler of the assembly"', cat='translation', refs=['13:14'], text='As at 8:49.'),
 dict(term='ἀγανακτῶν, "indignant"', cat='translation', refs=['13:14'], text='Angry, vexed.'),
 dict(term='δεῖ, "one must"', cat='translation', refs=['13:14'], text='Necessity, as at 4:43. In 13:16 Jesus answers with the same word, ἔδει.'),
 dict(term='ὁ κύριος, "the lord"', cat='translation', refs=['13:15'], text='As at 7:13.'),
 dict(term='Ὑποκριταί, "play-actors"', cat='translation', refs=['13:15'], text='Plural, as at 12:56.'),
 dict(term='λύει, "loose"', cat='translation', refs=['13:15'], text='λύω, to untie, loose. 13:16 uses the same verb of the woman.'),
 dict(term='ποτίζει, "give it drink"', cat='translation', refs=['13:15'], text='To water.'),
 dict(term='ἔδησεν ὁ Σατανᾶς, "Satan bound"', cat='translation', refs=['13:16'], text='δέω, to bind. As at 11:18, the Hebrew word "adversary" left untranslated.'),
 dict(term='δέκα καὶ ὀκτώ, "eighteen"', cat='translation', refs=['13:16'], text='Here "ten and eight", as the Greek has it; in 13:11 it is the single word δεκαοκτώ.'),
 dict(term='οὐκ ἔδει, "was it not necessary"', cat='translation', refs=['13:16'], text='The same word as in 13:14: what must be done.'),
 dict(term='λυθῆναι ἀπὸ τοῦ δεσμοῦ, "be loosed from this bond"', cat='translation', refs=['13:16'], text='λύω, as in 13:15.'),
 dict(term='οἱ ἀντικείμενοι, "who were opposed"', cat='translation', refs=['13:17'], text='Literally "lying against", adversaries.'),
 dict(term='τοῖς ἐνδόξοις, "the glorious things"', cat='translation', refs=['13:17'], text='From δόξα, glory.'),
 dict(term='κόκκῳ σινάπεως, "a grain of mustard"', cat='translation', refs=['13:19'], text='A single seed of mustard.'),
 dict(term='ἔβαλεν, "threw"', cat='translation', refs=['13:19'], text='βάλλω, to throw, cast, sow by casting.'),
 dict(term='κατεσκήνωσεν, "settled"', cat='translation', refs=['13:19'], text='To pitch a tent, take up a dwelling, as at 9:58.'),
 dict(term='ἐνέκρυψεν, "hid"', cat='translation', refs=['13:21'], text='To hide in.'),
 dict(term='ἀλεύρου σάτα τρία, "three measures of flour"', cat='translation', refs=['13:21'], text="σάτον, a Hebrew measure (se'ah). Three of them make a very large amount of dough."),
 dict(term='οἱ σῳζόμενοι, "those being saved"', cat='translation', refs=['13:23'], text='A present participle: those who are being saved.'),
 dict(term='Ἀγωνίζεσθε, "struggle"', cat='translation', refs=['13:24'], text='To contend, as in an athletic contest.'),
 dict(term='οὐκ ἰσχύσουσιν, "will not be strong enough"', cat='translation', refs=['13:24'], text='ἰσχύω, to have strength.'),
 dict(term='ὁ οἰκοδεσπότης, "the master of the house"', cat='translation', refs=['13:25'], text='As at 12:39.'),
 dict(term='ἐγερθῇ, "has got up"', cat='translation', refs=['13:25'], text='ἐγείρω.'),
 dict(term='Οὐκ οἶδα ὑμᾶς πόθεν ἐστέ, "I do not know you, where you are from"', cat='translation', refs=['13:25'], text='The Greek puts "you" first, then "where you are from".'),
 dict(term='ἀπόστητε ἀπ\' ἐμοῦ, "stand away from me"', cat='translation', refs=['13:27'], text='ἀφίστημι, to stand off, withdraw.'),
 dict(term='ἐργάται ἀδικίας, "workers of injustice"', cat='translation', refs=['13:27'], text='ἀδικία, wrong, injustice, the opposite of what is δίκαιος.'),
 dict(term='ὁ κλαυθμὸς καὶ ὁ βρυγμὸς τῶν ὀδόντων, "the weeping and the grinding of the teeth"', cat='translation', refs=['13:28'], text='With the article: "the weeping and the grinding", as of something known.'),
 dict(term='πάντας τοὺς δικαίους, "all the just"', cat='translation', refs=['13:28'], text='The reading of this text. Canonical Luke has "Abraham and Isaac and Jacob and all the prophets".'),
 dict(term='κρατουμένους ἔξω, "held outside"', cat='translation', refs=['13:28'], text='The reading of this text. Canonical Luke has "thrown out".'),
]
