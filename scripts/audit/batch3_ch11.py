"""Batch 3, chapter 11 of the reconstruction: Luke 13:1–35."""
from buildlib import greek
from batch1_ch2 import U, A
from batch3_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}

ENTRIES = [
 U('13:10', G('13:10'), 'Now he was teaching in one of the synagogues on the sabbath.', 'Opens the attested pericope 13:10–17.'),
 U('13:11', G('13:11'), 'And behold, there was a woman who had had a spirit of weakness for eighteen years; she was bent over and could not straighten herself at all.', 'Inside the attested pericope 13:10–17.'),
 U('13:12', G('13:12'), 'When Jesus saw her, he called her over and said to her, "Woman, you are freed from your weakness."', 'Inside the attested pericope 13:10–17.'),
 U('13:13', G('13:13'), 'And he laid his hands on her, and immediately she stood up straight and glorified God.', 'Inside the attested pericope 13:10–17.'),
 A('13:14', G('13:14'), 'But the leader of the synagogue, indignant that Jesus had healed on the sabbath, said to the crowd, "There are six days on which work ought to be done; come on those days and be healed, and not on the sabbath day."',
   'present (Marc. 4.30.1)', [T('4.30.1', '"Quaestionem rursus de curatione sabbato facta quomodo discussit?"')]),
 A('13:15', G('13:15'), 'The Lord answered him, "Hypocrites! Does not each of you on the sabbath untie his ox or his donkey from the manger and lead it away to water it?',
   'present (Marc. 4.30.1)', [T('4.30.1', '"Unusquisque vestrum sabbatis non solvit asinum aut bovem suum a praesepi et ducit ad potum?"')],
   wording='NA27. Tertullian names the donkey first and has "on the sabbaths"; Roth: order uncertain, plural possible only.'),
 A('13:16', G('13:16'), 'And this woman, a daughter of Abraham whom Satan bound for eighteen long years, ought she not to be set free from this bond on the sabbath day?"',
   'present (Pan. 42.11.6, sch. 39)', [E(39, '»ταύτην δὲ θυγατέρα Ἀβραάμ, ἣν ἔδησεν ὁ Σατανᾶς«.')]),
 U('13:17', G('13:17'), 'As he said this, all his opponents were put to shame, and the whole crowd rejoiced at all the glorious things he was doing.', 'Inside the attested pericope 13:10–17.'),
 U('13:18', G('13:18'), 'He said therefore, "What is the kingdom of God like, and to what shall I compare it?', 'Inside the attested paragraph 13:18–19.'),
 A('13:19', G('13:19'), 'It is like a grain of mustard seed that a man took and sowed in his garden; and it grew and became a tree, and the birds of the sky made nests in its branches."',
   'present (Marc. 4.30.1–2)', [T('4.30.1', '"Simile est regnum dei, inquit, grano sinapis, quod accepit homo et seminavit in horto suo."')],
   wording='NA27. Tertullian\'s "seminavit in horto suo" (ἔσπειρεν ἐν τῷ κήπῳ αὐτοῦ?) is rated possible only by Roth; not adopted.'),
 A('13:20', G('13:20'), 'And again he said, "To what shall I compare the kingdom of God?',
   'present (Marc. 4.30.3)', [T('4.30.3', '"De sequenti plane similitudine… Fermento enim comparavit illud".')]),
 A('13:21', G('13:21'), 'It is like leaven that a woman took and hid in three measures of flour, until it was all leavened."',
   'present (Marc. 4.30.3)', [T('4.30.3', '"Fermento enim comparavit illud, non azymis quae familiariora sunt creatori."')],
   wording='NA27 [ἐν]έκρυψεν, printed without the brackets (SBLGNT ἔκρυψεν — checked on the page image).'),
 U('13:23', G('13:23'), 'Someone said to him, "Lord, will those who are saved be few?" He said to them,', 'Inside the attested paragraph 13:23–30.'),
 U('13:24', G('13:24'), '"Strive to enter through the narrow door; for many, I tell you, will seek to enter and will not be able.', 'Inside the attested paragraph 13:23–30.'),
 A('13:25', G('13:25'), 'Once the master of the house has risen and shut the door, and you begin to stand outside and to knock at the door, saying, \'Lord, open to us\', he will answer you, \'I do not know where you come from.\'',
   'present (Marc. 4.30.4)', [T('4.30.4', '"Cum surrexerit, inquit, pater familiae… et cluserit ostium… Quibus pulsantibus respondebit, Nescio unde sitis".')]),
 A('13:26', G('13:26'), 'Then you will begin to say, \'We ate and drank in your presence, and you taught in our streets.\'',
   'present (Marc. 4.30.4)', [T('4.30.4', '"et rursus enumerantibus quod coram illo ederint et biberint et in plateis eorum docuerit".')]),
 A('13:27', G('13:27'), 'But he will say to you, \'I do not know where you come from. Depart from me, all you workers of injustice!\'',
   'present (Marc. 4.30.4)', [T('4.30.4', '"adiciet, Recedite a me omnes operarii iniquitatis."')],
   wording='NA27, including its bracketed [ὑμᾶς] (SBLGNT omits it — checked on the page image). Tertullian\'s iniquitatis may render ἀνομίας (Ps 6:9; D); Roth: possible only.'),
 A('13:28', G('13:28', [('ὅταν ὄψησθε Ἀβραὰμ καὶ Ἰσαὰκ καὶ Ἰακὼβ καὶ πάντας τοὺς προφήτας ἐν τῇ βασιλείᾳ τοῦ θεοῦ, ὑμᾶς δὲ ἐκβαλλομένους ἔξω.',
                         'ὅταν ὄψησθε πάντας τοὺς δικαίους ἐν τῇ βασιλείᾳ τοῦ θεοῦ, ὑμᾶς δὲ κρατουμένους ἔξω.')]),
   'There will be weeping and gnashing of teeth, when you see all the righteous in the kingdom of God, and yourselves held outside.',
   'present (Marc. 4.30.4–5; Pan. 42.11.6, sch. 40)',
   [E(40, 'παρέκοψε πάλιν τὸ »τότε ὄψεσθε Ἀβραὰμ καὶ Ἰσαὰκ καὶ Ἰακὼβ καὶ πάντας τοὺς προφήτας ἐν τῇ βασιλείᾳ τοῦ θεοῦ«· ἀντὶ δὲ τούτου ἐποίησεν »ὅτε πάντας τοὺς δικαίους ἴδητε ἐν τῇ βασιλείᾳ τοῦ θεοῦ, ὑμᾶς δὲ ἐκβαλλομένους« — ἐποίησε δὲ »κρατουμένους« — »ἔξω«.'),
    T('4.30.4–5', '"Illic erit fletus et frendor dentium. Ubi? foris scilicet, ubi erunt exclusi… cum videbunt iustos introeuntes in regnum dei, se vero detineri foris."')],
   wording=('Marcionite readings adopted: "all the righteous" for "Abraham and Isaac and Jacob and all the prophets", and κρατουμένους ("held") for ἐκβαλλομένους ("thrown out"). Epiphanius states both, correcting himself in the scholion from ἐκβαλλομένους to κρατουμένους; Tertullian has "iustos" and "se vero detineri foris". Roth: secure. '
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
 "Healing on the sabbath, and the kingdom compared. Jesus heals a woman bent over for eighteen years, \"a daughter of "
 "Abraham whom Satan bound\", and answers the leader of the synagogue with the ox or donkey watered on the sabbath. He "
 "compares the kingdom of God to a mustard seed sown in a garden and to leaven. Those who come to the door once the master "
 "has shut it will be told \"I do not know where you come from\", and will weep \"when you see all the righteous in the "
 "kingdom of God, and yourselves held outside\". In this text it is \"the righteous\", not Abraham, Isaac, Jacob and the "
 "prophets, whom they see in the kingdom. Two blocks of canonical Luke are not in this text, by Epiphanius' statement. The "
 "first is the Galileans killed by Pilate, the tower of Siloam and the barren fig tree (13:1–9). The second is the many "
 "coming from east and west, the warning about Herod and the lament over Jerusalem (13:29–35)."
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
 dict(term='The shut door and \"all the righteous\" (13:23–28)', cat='textual', refs=['13:23', '13:24', '13:25', '13:26', '13:27', '13:28'], text=(
  "Tertullian, Marc. 4.30.4–6: the master of the house rises and shuts the door; to those knocking he answers \"I do not know "
  "where you are from\"; to those who say they ate and drank before him and that he taught in their streets, \"Depart from me, "
  "all workers of iniquity. There will be weeping and gnashing of teeth\", \"when they see the righteous entering the kingdom "
  "of God and themselves held outside\". Epiphanius, sch. 40 confirms the wording: the text had \"all the righteous\" where "
  "canonical Luke has \"Abraham and Isaac and Jacob and all the prophets\", and \"held\" (κρατουμένους) outside. 13:23–24 are not "
  "cited and are printed in grey.")),
 dict(term='Not printed: 13:29–35', cat='excision', refs=['13:28'], text=(
  "Epiphanius, sch. 41 names every saying of 13:29–35 as absent: people coming from east and west to recline in the kingdom, "
  "\"the last will be first\", the Pharisees' warning about Herod, the answer to \"that fox\", \"no prophet can perish outside "
  "Jerusalem\", and the lament \"Jerusalem, Jerusalem\" with \"you will not see me until you say, Blessed…\". Tertullian goes "
  "from 13:28 to 14:12.")),
 dict(term='The righteous in the kingdom', cat='theological', refs=['13:16', '13:28'], text=(
  "Interpretation. In the attested text those seen in the kingdom are \"all the righteous\", not the patriarchs and prophets "
  "by name, while the woman healed on the sabbath is still \"a daughter of Abraham\" (13:16). The text therefore does not cut "
  "the tie to Abraham. It describes the kingdom by righteousness, not by descent. The leader of the Jerusalem community was "
  "remembered as James \"the Just\" (Gospel of Thomas 12; Carriers of Living Water §3.1). Whether \"the righteous\" in this "
  "saying reflects that usage cannot be shown from the witnesses. The readings themselves are attested by two witnesses; why "
  "canonical Luke has the patriarchs instead (as Matt 8:11 does) they do not say.")),
]
