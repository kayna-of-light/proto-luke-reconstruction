"""Batch 5, chapter 18 of the reconstruction: Luke 20:1–47."""
from buildlib import greek
from batch1_ch2 import U, A
from batch5_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}

T384 = T('4.38.4', '"Sadducaei, resurrectionis negatores, de ea habentes interrogationem, proposuerant domino ex lege materiam mulieris quae septem fratribus ex ordine defunctis secundum praeceptum legale nupsisset, cuius viri deputanda esset in resurrectione."')

ENTRIES = [
 A('20:1', G('20:1'), 'And it happened on one of the days, as he was teaching the people in the temple and announcing the good news, that the high priests and the scribes with the elders came upon him,',
   'present (Marc. 4.38.1)', [T('4.38.1', '"Sciebat non responsuros sibi pharisaeos."')]),
 U('20:2', G('20:2'), 'and they spoke, saying to him, "Tell us, by what authority are you doing these things, or who is it who gave you this authority?"', 'Inside the attested pericope 20:1–8.'),
 U('20:3', G('20:3'), 'And answering, he said to them, "I too will ask you a word, and you tell me:', 'Inside the attested pericope 20:1–8.'),
 A('20:4', G('20:4'), 'the immersion of John, was it from heaven or from humans?"',
   'present (Marc. 4.38.1–2)', [T('4.38.1', '"Sciebat Christus baptisma Ioannis unde esset. Et cur quasi nesciens interrogabat?… Puta illos renuntiasse humanum Ioannis baptisma…"'),
                                 T('4.38.2', '"Sed de caelis fuit baptisma Ioannis."')]),
 A('20:5', G('20:5'), 'And they reasoned together among themselves, saying, "If we say, \'From heaven,\' he will say, \'Why did you not trust him?\'',
   'present (Marc. 4.38.2)', [T('4.38.2', '"Et quare, inquit Christus, non credidistis ei?"')],
   wording='NA27. Tertullian quotes "why did you not trust him?" as Christ\'s words, as the leaders expect him to say them.'),
 A('20:6', G('20:6'), 'But if we say, \'From humans,\' all the people will stone us to death, for they are persuaded that John was a prophet."',
   'present (Marc. 4.38.1)', [T('4.38.1', '"Puta illos renuntiasse humanum Ioannis baptisma, statim lapidibus elisi fuissent."')]),
 A('20:7', G('20:7'), 'And they answered that they did not know where it was from.',
   'present (Marc. 4.38.2)', [T('4.38.2', '"Certe nolentibus renuntiare quid saperent…"')], wording='NA27. Roth: attested, but no insight into the wording.'),
 A('20:8', G('20:8'), 'And Jesus said to them, "Neither do I tell you by what authority I do these things."',
   'present (Marc. 4.38.2)', [T('4.38.2', '"cum et ipse vicem opponit, Et ego non dico vobis in qua virtute haec facio".')]),
 A('20:19', greek('20:19', text='καὶ ἐζήτησαν οἱ γραμματεῖς καὶ οἱ ἀρχιερεῖς ἐπιβαλεῖν ἐπ’ αὐτὸν τὰς χεῖρας ἐν αὐτῇ τῇ ὥρᾳ, καὶ ἐφοβήθησαν τὸν λαόν.'),
   'And the scribes and the high priests sought to lay their hands on him in that very hour, and they were afraid of the people.',
   'present (Pan. 42.11.6, sch. 54)', [E(54, '»καὶ ἐζήτησαν ἐπιβαλεῖν ἐπ\' αὐτὸν τὰς χεῖρας καὶ ἐφοβήθησαν«.')],
   wording=('NA27, without its last clause, "for they perceived that he had told this parable against them". Epiphanius quotes the verse as present, but the parable of the tenants (20:9–17) is absent by his own statement (sch. 55). The clause referring to it is not quoted and is classed probably absent with the parable. '
            'In this text the verse follows the question about John\'s baptism (20:1–8), and the hostility it reports answers that exchange. Epiphanius\' refutation introduces the verse with the setting of 20:1 ("as he was teaching in the temple").')),
 U('20:20', G('20:20'), 'And watching closely, they sent spies who acted the part of being just, so that they might take hold of a word of his, so as to hand him over to the rule and the authority of the governor.', 'Inside the attested paragraph 20:20–26.'),
 U('20:21', G('20:21'), 'And they asked him, saying, "Teacher, we know that you speak and teach rightly, and do not receive a face, but teach the way of God in truth.', 'Inside the attested paragraph 20:20–26.'),
 U('20:22', G('20:22'), 'Is it permitted for us to give tribute to Caesar, or not?"', 'Inside the attested paragraph 20:20–26.'),
 U('20:23', G('20:23'), 'But perceiving their cunning, he said to them,', 'Inside the attested paragraph 20:20–26.'),
 A('20:24', G('20:24'), '"Show me a denarius. Whose image and inscription does it have?" And they said, "Caesar\'s."',
   'present (Marc. 4.38.3)', [T('4.38.3', '"Quae similia sunt denario Caesaris; imago scilicet et similitudo eius."')],
   wording='NA27 (οἱ δὲ εἶπαν; SBLGNT ἀποκριθέντες δὲ εἶπαν — checked on the page image).'),
 A('20:25', G('20:25'), 'And he said to them, "Then give back the things of Caesar to Caesar, and the things of God to God."',
   'present (Marc. 4.38.3)', [T('4.38.3', '"Reddite quae Caesaris Caesari, et quae sunt dei deo."')]),
 U('20:26', G('20:26'), 'And they were not able to take hold of his saying before the people, and marvelling at his answer, they fell silent.', 'Inside the attested paragraph 20:20–26. NA27 αὐτοῦ ῥήματος (SBLGNT τοῦ ῥήματος).'),
 A('20:27', G('20:27'), 'And some of the Sadducees came up, those who say in opposition that there is no rising, and they asked him,',
   'present (Marc. 4.38.4)', [T384]),
 A('20:28', G('20:28'), 'saying, "Teacher, Moses wrote for us: if someone\'s brother dies having a wife, and he is childless, his brother is to take the wife and raise up seed for his brother.',
   'present (Marc. 4.38.4)', [T384]),
 A('20:29', G('20:29'), 'So there were seven brothers; and the first, having taken a wife, died childless;',
   'present (Marc. 4.38.4)', [T384]),
 A('20:30', G('20:30'), 'and the second,',
   'present (Marc. 4.38.4)', [T384], wording='NA27. Roth: attested, but no insight into the wording.'),
 A('20:31', G('20:31'), 'and the third took her, and likewise also the seven did not leave children, and died.',
   'present (Marc. 4.38.4)', [T384], wording='NA27. Roth: attested, but no insight into the wording.'),
 U('20:32', G('20:32'), 'Afterwards the woman also died.', 'Inside the attested paragraph 20:27–40.'),
 A('20:33', G('20:33'), 'The woman, then, in the rising, whose wife does she become? For the seven had her as wife."',
   'present (Marc. 4.38.4)', [T384]),
 A('20:34', G('20:34'), 'And Jesus said to them, "The sons of this age marry and are given in marriage;',
   'present (Marc. 4.38.5, 8)', [T('4.38.5', '"Respondit igitur huius quidem aevi filios nubere."'), T('4.38.8', '"Filii huius aevi nubunt et nubuntur".')]),
 A('20:35', G('20:35', [('οἱ δὲ καταξιωθέντες τοῦ αἰῶνος', 'οὓς δὲ κατηξίωσεν ὁ θεὸς τοῦ αἰῶνος')]),
   'but those whom God has deemed worthy to attain that age and the rising from the dead neither marry nor are given in marriage;',
   'present (Marc. 4.38.5, 7–8)',
   [T('4.38.5', '"Quos vero dignatus sit deus illius aevi possessione et resurrectione a mortuis, neque nubere neque nubi".'),
    T('4.38.7', '"Nacti enim scripturae textum ita in legendo decucurrerunt: Quos autem dignatus est deus illius aevi. Illius aevi deo adiungunt, quo alium deum faciant illius aevi; cum sic legi oporteat: Quos autem dignatus est deus, ut facta hic distinctione post deum ad sequentia pertineat illius aevi…"')],
   wording=('Marcionite reading adopted, against Roth\'s grade (probable): "those whom God has deemed worthy" (οὓς δὲ κατηξίωσεν ὁ θεός) for NA27 "those who are deemed worthy" (οἱ δὲ καταξιωθέντες). Tertullian quotes the clause three times with God as subject. He reports that the Marcionites read "the God of that age" together, as a second God, and he argues against that punctuation but not against the text. Their reading requires the wording, as Roth notes ("the interpretation… requires ὁ θεός to be an external subject"). '
            'Only the attested element is changed. Roth\'s fuller retroversion (τῆς κληρονομίας for τυχεῖν, from possessione) is not adopted; NA27\'s τυχεῖν is kept, so that the Greek reads "whom God has deemed worthy to attain that age and the resurrection".')),
 A('20:36', G('20:36'), 'for they cannot die any more, for they are equal to messengers, and they are sons of God, being sons of the rising."',
   'present (Marc. 4.38.5, 7)', [T('4.38.5', '"quia nec morituri iam sint, cum similes angelorum fiant, dei et resurrectionis filii facti".')],
   wording='NA27. NA27 cites McionT for μέλλουσιν ("are about to") for δύνανται, with D W Θ it; Roth: probable only. Not adopted.'),
 A('20:39', G('20:39'), 'And answering, some of the scribes said, "Teacher, you have spoken finely."',
   'present (Marc. 4.38.9)', [T('4.38.9', '"Atque adeo scribae, Magister, inquiunt, bene dixisti."')]),
 U('20:40', G('20:40'), 'For they no longer dared to ask him anything.', 'Inside the attested paragraph 20:27–40.'),
 A('20:41', G('20:41'), 'And he said to them, "How do they say that the Anointed One is the son of David?',
   'present (Marc. 4.38.10)', [T('4.38.10', '"Si autem scribae Christum filium David existimabant, ipse autem David dominum eum appellat…"')]),
 U('20:42', G('20:42'), "For David himself says in the book of Psalms: 'The Lord said to my lord, Sit at my right hand,", 'Inside the attested paragraph 20:41–44.'),
 U('20:43', G('20:43'), "until I put your enemies as a footstool for your feet.'", 'Inside the attested paragraph 20:41–44.'),
 A('20:44', G('20:44'), 'David, then, calls him lord; and how is he his son?"',
   'present (Marc. 4.38.10)', [T('4.38.10', '"ipse autem David dominum eum appellat".')],
   wording='NA27 (κύριον αὐτόν; SBLGNT αὐτὸν κύριον — checked on the page image).'),
]

OMITTED = [
 dict(ref='20:9–17', cls='A−', app=dict(roth='absent', witnesses=[
      E(55, 'πάλιν ἀπέκοψε τὰ περὶ τοῦ ἀμπελῶνος τοῦ ἐκδεδομένου γεωργοῖς καὶ τὸ »τί οὖν ἐστι τό· λίθον ὃν ἀπεδοκίμασαν οἱ οἰκοδομοῦντες;«')],
      decision='not printed', reason='Epiphanius states that the text lacked the parable of the vineyard let out to tenants and "What then is this that is written: the stone that the builders rejected?" Tertullian passes from 20:8 (4.38.2) to 20:24–25 (4.38.3); Roth counts his silence as confirmation (tacitus).')),
 dict(ref='20:18', cls='U−', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='"Everyone who falls on that stone will be broken to pieces…" It refers to the stone of 20:17, which Epiphanius says the text lacked, and ends the parable.')),
 dict(ref='20:37–38', cls='A−', app=dict(roth='absent (20:37–38a); unattested (20:38b)', witnesses=[
      E(56, 'ἀπέκοψε τὸ »ὅτι δὲ ἐγείρονται οἱ νεκροὶ Μωυσῆς ἐμήνυσε ἐπὶ τῆς βάτου, καθὼς λέγει κύριον τὸν θεὸν Ἀβραὰμ καὶ Ἰσαὰκ καὶ Ἰακώβ. θεὸς δέ ἐστι ζώντων καὶ οὐχὶ νεκρῶν«.'),
      E(57, 'οὐκ εἶχε ταῦτα »ὅτι δὲ ἐγείρονται οἱ νεκροὶ καὶ Μωυσῆς ἐμήνυσε λέγων θεὸν Ἀβραὰμ καὶ θεὸν Ἰσαὰκ καὶ θεὸν Ἰακὼβ θεὸν ζώντων«.')],
      decision='not printed', reason=('Epiphanius states twice that the text lacked the proof of the resurrection from Moses at the bush and "he is the God not of the dead but of the living" (20:37–38a). Tertullian goes from 20:36 to 20:39 (4.38.8–9). '
              '20:38b ("for all live to him") is unattested and completes the same sentence; it is not printed.'))),
 dict(ref='20:45–47', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='"Beware of the scribes, who like to walk around in long robes… who devour widows\' houses." A separate NA27 paragraph with no attested verse (METHOD §4.3). Tertullian passes from 20:44 (4.38.10) to 21:8 (4.39.1).')),
]

PREAMBLE = (
 "Questions in the temple. Asked by what authority he acts, Jesus asks in return whether John's baptism was from heaven or "
 "from men, and when the leaders will not answer, he will not tell them either. The leaders seek to seize him but fear the "
 "people. To the question about tribute he answers, \"Give back to Caesar what is Caesar's, and to God what is God's.\" To "
 "the Sadducees' question about the woman with seven husbands he answers that the sons of this age marry, \"but those whom "
 "God has deemed worthy to attain to that age and to the resurrection from the dead neither marry nor are given in "
 "marriage… they are equal to messengers and are sons of God\". He asks how the Christ can be David's son when David calls him "
 "Lord. The parable of the tenants with the rejected stone (20:9–18) and the proof of the resurrection from Moses at the bush "
 "(20:37–38) are absent: Epiphanius states that the text lacked them."
)

NOTES = [
 dict(term='John\'s baptism (20:1–8)', cat='textual', refs=['20:1', '20:4', '20:5', '20:6', '20:8'], text=(
  "Tertullian, Marc. 4.38.1–2: Christ knew where John's baptism came from, and asked so that the Pharisees would judge "
  "themselves. \"Why did you not trust him?\" shows that he wanted John to be believed, and so that John's baptism was the "
  "Creator's. The leaders' fear of being stoned and Jesus' \"Neither do I tell you by what power I do these things\" are "
  "both cited. 20:2–3 are not cited and are printed in grey.")),
 dict(term='Not printed: the tenants (20:9–18)', cat='excision', refs=['20:8', '20:19'], text=(
  "Epiphanius, sch. 55: Marcion \"again cut out what concerns the vineyard let out to tenants, and 'What then is this: the "
  "stone which the builders rejected?'\". 20:18, on falling on that stone, goes with it. Epiphanius does quote 20:19 (sch. 54), "
  "the leaders seeking to seize Jesus and fearing the people. It is printed without its last clause, \"for they knew that he "
  "had told this parable against them\", which refers to the absent parable. In this text the leaders' hostility follows the "
  "exchange about John.")),
 dict(term='Caesar and God (20:20–26)', cat='textual', refs=['20:20', '20:24', '20:25', '20:26'], text=(
  "Tertullian, Marc. 4.38.3 quotes \"Render to Caesar the things that are Caesar's, and to God the things that are God's\". "
  "He explains that what is God's is what bears his image and likeness, the human being, so the saying gives man back to "
  "his maker. 20:20–23 and 20:26 are not cited and are printed in grey.")),
 dict(term='"Those whom God has deemed worthy" (20:27–40)', cat='textual', refs=['20:27', '20:33', '20:34', '20:35', '20:36', '20:39'], text=(
  "Tertullian, Marc. 4.38.4–9 follows the Sadducees' question and the reply closely. He quotes the reply three times as "
  "\"those whom God has deemed worthy of that age and of the resurrection from the dead\". He reports that the Marcionites "
  "read \"the God of that age\" together, a second God who grants the resurrection, and he argues for a different "
  "punctuation, not a different text. The active \"whom God has deemed worthy\" is printed; canonical Luke has the passive "
  "\"those who are deemed worthy\". Epiphanius states twice (sch. 56–57) that the text lacked the proof from Moses at the "
  "bush, \"he is God not of the dead but of the living\" (20:37–38). It is not printed. The scribes' \"Teacher, you have "
  "spoken finely\" (20:39) follows directly on the sayings about the resurrection.")),
 dict(term='Resurrection without the patriarchs', cat='theological', refs=['20:35', '20:36'], text=(
  "Interpretation. In this text the answer about the resurrection is that the worthy \"neither marry nor are given in "
  "marriage, for they cannot die any more, for they are equal to messengers, and they are sons of God, being sons of the "
  "rising\". There is no argument from the God of Abraham, Isaac and Jacob, as there are no patriarchs in the kingdom "
  "at 13:28. The resurrection is described as a state God grants to the worthy, \"equal to messengers\" and \"sons of "
  "God\". It is not described as the return of the body that was buried. The witnesses do not say how the community behind "
  "the text pictured it.")),
 dict(term='David\'s Lord (20:41–44)', cat='textual', refs=['20:41', '20:44'], text=(
  "Tertullian, Marc. 4.38.10: the scribes thought the Christ was David's son; David calls him Lord. Tertullian connects this "
  "with the blind man's \"son of David\" (18:38): Jesus accepted that title then and now shows he is also David's Lord. "
  "20:42–43, the quotation of Psalm 110:1, are not cited and are printed in grey. 20:45–47, the warning against the "
  "scribes, form a paragraph with no attested verse and are not printed.")),
 dict(term='εὐαγγελιζομένου, "announcing the good news"', cat='translation', refs=['20:1'], text='As at 4:43.'),
 dict(term='ἐπέστησαν, "came upon him"', cat='translation', refs=['20:1'], text='To stand over, come up suddenly.'),
 dict(term='οἱ ἀρχιερεῖς, "the high priests"', cat='translation', refs=['20:1'], text='As at 9:22.'),
 dict(term='λόγον, "a word"', cat='translation', refs=['20:3'], text='Here a question, a matter.'),
 dict(term='Τὸ βάπτισμα Ἰωάννου, "the immersion of John"', cat='translation', refs=['20:4'], text='βάπτισμα, a dipping, immersion, as at 12:50. "Baptism" is the Greek word left untranslated.'),
 dict(term='ἐξ οὐρανοῦ… ἐξ ἀνθρώπων, "from heaven… from humans"', cat='translation', refs=['20:4'], text='"Heaven" was a way of saying "God" without naming him.'),
 dict(term='ἐπιστεύσατε, "trust"', cat='translation', refs=['20:5'], text='πιστεύω, as at 8:50.'),
 dict(term='καταλιθάσει, "will stone us to death"', cat='translation', refs=['20:6'], text='To stone down, kill by stoning.'),
 dict(term='πεπεισμένος, "persuaded"', cat='translation', refs=['20:6'], text='πείθω, perfect passive.'),
 dict(term='καὶ ἐφοβήθησαν, "and they were afraid"', cat='translation', refs=['20:19'], text='καί, "and": the Greek does not say "but".'),
 dict(term='παρατηρήσαντες, "watching closely"', cat='translation', refs=['20:20'], text='As at 6:7.'),
 dict(term='ἐγκαθέτους, "spies"', cat='translation', refs=['20:20'], text='Agents planted in secret.'),
 dict(term='ὑποκρινομένους, "who acted the part"', cat='translation', refs=['20:20'], text='The verb of ὑποκριτής (6:42): playing a role.'),
 dict(term='τῇ ἀρχῇ καὶ τῇ ἐξουσίᾳ τοῦ ἡγεμόνος, "the rule and the authority of the governor"', cat='translation', refs=['20:20'], text='ἡγεμών, the governor (3:1).'),
 dict(term='οὐ λαμβάνεις πρόσωπον, "do not receive a face"', cat='translation', refs=['20:21'], text='A Hebrew idiom: to show partiality, to judge by appearance.'),
 dict(term='ἐπ\' ἀληθείας, "in truth"', cat='translation', refs=['20:21'], text='Truly, on the basis of truth.'),
 dict(term='φόρον, "tribute"', cat='translation', refs=['20:22'], text='The tax paid to Rome by a subject people.'),
 dict(term='πανουργίαν, "cunning"', cat='translation', refs=['20:23'], text='Literally "readiness to do anything": craftiness.'),
 dict(term='εἰκόνα καὶ ἐπιγραφήν, "image and inscription"', cat='translation', refs=['20:24'], text="The emperor's head and his name on the coin."),
 dict(term='ἀπόδοτε, "give back"', cat='translation', refs=['20:25'], text='ἀποδίδωμι, to give back, pay what is owed.'),
 dict(term='αὐτοῦ ῥήματος, "his saying"', cat='translation', refs=['20:26'], text='ῥῆμα, as at 5:5. The order αὐτοῦ ῥήματος is that of NA27.'),
 dict(term='Σαδδουκαίων, "Sadducees"', cat='translation', refs=['20:27'], text='A party of the priestly aristocracy.'),
 dict(term='ἀνάστασιν, "rising"', cat='translation', refs=['20:27'], text='ἀνάστασις, a standing up, as at 14:14.'),
 dict(term='ἐξαναστήσῃ σπέρμα, "raise up seed"', cat='translation', refs=['20:28'], text='To raise up offspring: the law of the levirate (Deut 25:5–6). The verb is a form of ἀνίστημι, as in "rising".'),
 dict(term='καὶ ὁ δεύτερος, "and the second"', cat='translation', refs=['20:30'], text='The verse in NA27 is only these words. Later manuscripts fill it out.'),
 dict(term='κατέλιπον, "leave"', cat='translation', refs=['20:31'], text='καταλείπω, as at 5:28.'),
 dict(term='γίνεται, "does she become"', cat='translation', refs=['20:33'], text='The present tense: in the rising, whose does she become?'),
 dict(term='Οἱ υἱοὶ τοῦ αἰῶνος τούτου, "the sons of this age"', cat='translation', refs=['20:34'], text='As at 16:8.'),
 dict(term='γαμοῦσιν καὶ γαμίσκονται, "marry and are given in marriage"', cat='translation', refs=['20:34'], text='The men marry, the women are given.'),
 dict(term='οὓς δὲ κατηξίωσεν ὁ θεὸς τοῦ αἰῶνος ἐκείνου τυχεῖν, "but those whom God has deemed worthy to attain that age"', cat='translation', refs=['20:35'], text='The reading of this text, with "God" named. The Greek words can also be grouped "whom the God of that age has deemed worthy to attain". Tertullian says the Marcionites read it that way (Marc. 4.38.7). The English follows the order of the Greek, which allows both; the grouping shown is the ordinary one.'),
 dict(term='καὶ τῆς ἀναστάσεως τῆς ἐκ νεκρῶν, "and the rising from the dead"', cat='translation', refs=['20:35'], text='ἀνάστασις, as at 20:27.'),
 dict(term='ἰσάγγελοι, "equal to messengers"', cat='translation', refs=['20:36'], text='One word: "equal to messengers". ἄγγελος, as at 9:26.'),
 dict(term='υἱοί… θεοῦ… τῆς ἀναστάσεως υἱοί, "sons of God… sons of the rising"', cat='translation', refs=['20:36'], text='The Semitic "sons of": those who belong to God, those who belong to the rising.'),
 dict(term='καλῶς, "finely"', cat='translation', refs=['20:39'], text='καλός, as at 6:43.'),
 dict(term='ἐτόλμων, "dared"', cat='translation', refs=['20:40'], text='The imperfect: they no longer dared.'),
 dict(term='τὸν χριστόν, "the Anointed One"', cat='translation', refs=['20:41'], text='As at 4:41.'),
 dict(term='Εἶπεν κύριος τῷ κυρίῳ μου, "the Lord said to my lord"', cat='translation', refs=['20:42'], text='Ps 110:1. The first κύριος renders the divine name, so it is capitalised; the second is "my lord", a title of the king. The Greek uses one word for both; the Hebrew has two (YHWH and adoni).'),
 dict(term='ἐκ δεξιῶν μου, "at my right hand"', cat='translation', refs=['20:42'], text='Literally "out of my right parts": at the place of honour.'),
 dict(term='ὑποπόδιον, "a footstool"', cat='translation', refs=['20:43'], text='The stool under the feet: the enemy placed under foot.'),
 dict(term='κύριον αὐτὸν καλεῖ, "calls him lord"', cat='translation', refs=['20:44'], text='Lower case, as in 20:42.'),
]
