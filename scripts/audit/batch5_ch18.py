"""Batch 5, chapter 18 of the reconstruction: Luke 20:1–47."""
from buildlib import greek
from batch1_ch2 import U, A
from batch5_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}

T384 = T('4.38.4', '"Sadducaei, resurrectionis negatores, de ea habentes interrogationem, proposuerant domino ex lege materiam mulieris quae septem fratribus ex ordine defunctis secundum praeceptum legale nupsisset, cuius viri deputanda esset in resurrectione."')

ENTRIES = [
 A('20:1', G('20:1'), 'One day, as he was teaching the people in the temple and proclaiming the good news, the chief priests and the scribes with the elders came up',
   'present (Marc. 4.38.1)', [T('4.38.1', '"Sciebat non responsuros sibi pharisaeos."')]),
 U('20:2', G('20:2'), 'and said to him, "Tell us by what authority you do these things, or who it is that gave you this authority."', 'Inside the attested pericope 20:1–8.'),
 U('20:3', G('20:3'), 'He answered them, "I also will ask you a question. Now tell me:', 'Inside the attested pericope 20:1–8.'),
 A('20:4', G('20:4'), 'was the baptism of John from heaven or from men?"',
   'present (Marc. 4.38.1–2)', [T('4.38.1', '"Sciebat Christus baptisma Ioannis unde esset. Et cur quasi nesciens interrogabat?… Puta illos renuntiasse humanum Ioannis baptisma…"'),
                                 T('4.38.2', '"Sed de caelis fuit baptisma Ioannis."')]),
 A('20:5', G('20:5'), 'And they discussed it with one another, saying, "If we say, \'From heaven\', he will say, \'Why did you not believe him?\'',
   'present (Marc. 4.38.2)', [T('4.38.2', '"Et quare, inquit Christus, non credidistis ei?"')],
   wording='NA27. Tertullian quotes "why did you not believe him?" as Christ\'s words, as the leaders expect him to say them.'),
 A('20:6', G('20:6'), 'But if we say, \'From men\', all the people will stone us, for they are convinced that John was a prophet."',
   'present (Marc. 4.38.1)', [T('4.38.1', '"Puta illos renuntiasse humanum Ioannis baptisma, statim lapidibus elisi fuissent."')]),
 A('20:7', G('20:7'), 'So they answered that they did not know where it came from.',
   'present (Marc. 4.38.2)', [T('4.38.2', '"Certe nolentibus renuntiare quid saperent…"')], wording='NA27. Roth: attested, but no insight into the wording.'),
 A('20:8', G('20:8'), 'And Jesus said to them, "Neither will I tell you by what authority I do these things."',
   'present (Marc. 4.38.2)', [T('4.38.2', '"cum et ipse vicem opponit, Et ego non dico vobis in qua virtute haec facio".')]),
 A('20:19', greek('20:19', text='καὶ ἐζήτησαν οἱ γραμματεῖς καὶ οἱ ἀρχιερεῖς ἐπιβαλεῖν ἐπ’ αὐτὸν τὰς χεῖρας ἐν αὐτῇ τῇ ὥρᾳ, καὶ ἐφοβήθησαν τὸν λαόν.'),
   'The scribes and the chief priests sought to lay hands on him at that very hour, but they feared the people.',
   'present (Pan. 42.11.6, sch. 54)', [E(54, '»καὶ ἐζήτησαν ἐπιβαλεῖν ἐπ\' αὐτὸν τὰς χεῖρας καὶ ἐφοβήθησαν«.')],
   wording=('NA27, without its last clause, "for they perceived that he had told this parable against them". Epiphanius quotes the verse as present, but the parable of the tenants (20:9–17) is absent by his own statement (sch. 55). The clause referring to it is not quoted and is classed probably absent with the parable. '
            'In this text the verse follows the question about John\'s baptism (20:1–8), and the hostility it reports answers that exchange. Epiphanius\' refutation introduces the verse with the setting of 20:1 ("as he was teaching in the temple").')),
 U('20:20', G('20:20'), 'So they watched him, and sent spies, who pretended to be sincere, that they might catch him in something he said, so as to deliver him up to the authority and jurisdiction of the governor.', 'Inside the attested paragraph 20:20–26.'),
 U('20:21', G('20:21'), 'So they asked him, "Teacher, we know that you speak and teach rightly, and show no partiality, but truly teach the way of God.', 'Inside the attested paragraph 20:20–26.'),
 U('20:22', G('20:22'), 'Is it lawful for us to give tribute to Caesar, or not?"', 'Inside the attested paragraph 20:20–26.'),
 U('20:23', G('20:23'), 'But he perceived their craftiness, and said to them,', 'Inside the attested paragraph 20:20–26.'),
 A('20:24', G('20:24'), '"Show me a denarius. Whose image and inscription does it have?" They said, "Caesar\'s."',
   'present (Marc. 4.38.3)', [T('4.38.3', '"Quae similia sunt denario Caesaris; imago scilicet et similitudo eius."')],
   wording='NA27 (οἱ δὲ εἶπαν; SBLGNT ἀποκριθέντες δὲ εἶπαν — checked on the page image).'),
 A('20:25', G('20:25'), 'He said to them, "Then give back to Caesar the things that are Caesar\'s, and to God the things that are God\'s."',
   'present (Marc. 4.38.3)', [T('4.38.3', '"Reddite quae Caesaris Caesari, et quae sunt dei deo."')]),
 U('20:26', G('20:26'), 'And they were not able in the presence of the people to catch him in what he said, but marvelling at his answer they became silent.', 'Inside the attested paragraph 20:20–26. NA27 αὐτοῦ ῥήματος (SBLGNT τοῦ ῥήματος).'),
 A('20:27', G('20:27'), 'There came to him some Sadducees, those who deny that there is a resurrection, and they asked him,',
   'present (Marc. 4.38.4)', [T384]),
 A('20:28', G('20:28'), 'saying, "Teacher, Moses wrote for us that if a man\'s brother dies, having a wife but no children, the man must take the widow and raise up offspring for his brother.',
   'present (Marc. 4.38.4)', [T384]),
 A('20:29', G('20:29'), 'Now there were seven brothers. The first took a wife, and died without children.',
   'present (Marc. 4.38.4)', [T384]),
 A('20:30', G('20:30'), 'And the second',
   'present (Marc. 4.38.4)', [T384], wording='NA27. Roth: attested, but no insight into the wording.'),
 A('20:31', G('20:31'), 'and the third took her, and likewise all seven left no children and died.',
   'present (Marc. 4.38.4)', [T384], wording='NA27. Roth: attested, but no insight into the wording.'),
 U('20:32', G('20:32'), 'Afterwards the woman also died.', 'Inside the attested paragraph 20:27–40.'),
 A('20:33', G('20:33'), 'In the resurrection, therefore, whose wife will the woman be? For the seven had her as wife."',
   'present (Marc. 4.38.4)', [T384]),
 A('20:34', G('20:34'), 'And Jesus said to them, "The sons of this age marry and are given in marriage,',
   'present (Marc. 4.38.5, 8)', [T('4.38.5', '"Respondit igitur huius quidem aevi filios nubere."'), T('4.38.8', '"Filii huius aevi nubunt et nubuntur".')]),
 A('20:35', G('20:35', [('οἱ δὲ καταξιωθέντες τοῦ αἰῶνος', 'οὓς δὲ κατηξίωσεν ὁ θεὸς τοῦ αἰῶνος')]),
   'but those whom God has deemed worthy to attain to that age and to the resurrection from the dead neither marry nor are given in marriage;',
   'present (Marc. 4.38.5, 7–8)',
   [T('4.38.5', '"Quos vero dignatus sit deus illius aevi possessione et resurrectione a mortuis, neque nubere neque nubi".'),
    T('4.38.7', '"Nacti enim scripturae textum ita in legendo decucurrerunt: Quos autem dignatus est deus illius aevi. Illius aevi deo adiungunt, quo alium deum faciant illius aevi; cum sic legi oporteat: Quos autem dignatus est deus, ut facta hic distinctione post deum ad sequentia pertineat illius aevi…"')],
   wording=('Marcionite reading adopted, against Roth\'s grade (probable): "those whom God has deemed worthy" (οὓς δὲ κατηξίωσεν ὁ θεός) for NA27 "those who are deemed worthy" (οἱ δὲ καταξιωθέντες). Tertullian quotes the clause three times with God as subject. He reports that the Marcionites read "the God of that age" together, as a second God, and he argues against that punctuation but not against the text. Their reading requires the wording, as Roth notes ("the interpretation… requires ὁ θεός to be an external subject"). '
            'Only the attested element is changed. Roth\'s fuller retroversion (τῆς κληρονομίας for τυχεῖν, from possessione) is not adopted; NA27\'s τυχεῖν is kept, so that the Greek reads "whom God has deemed worthy to attain that age and the resurrection".')),
 A('20:36', G('20:36'), 'for they cannot die any more, because they are equal to angels and are sons of God, being sons of the resurrection.',
   'present (Marc. 4.38.5, 7)', [T('4.38.5', '"quia nec morituri iam sint, cum similes angelorum fiant, dei et resurrectionis filii facti".')],
   wording='NA27. NA27 cites McionT for μέλλουσιν ("are about to") for δύνανται, with D W Θ it; Roth: probable only. Not adopted.'),
 A('20:39', G('20:39'), 'Then some of the scribes answered, "Teacher, you have spoken well."',
   'present (Marc. 4.38.9)', [T('4.38.9', '"Atque adeo scribae, Magister, inquiunt, bene dixisti."')]),
 U('20:40', G('20:40'), 'For they no longer dared to ask him any question.', 'Inside the attested paragraph 20:27–40.'),
 A('20:41', G('20:41'), 'But he said to them, "How can they say that the Anointed One is David\'s son?',
   'present (Marc. 4.38.10)', [T('4.38.10', '"Si autem scribae Christum filium David existimabant, ipse autem David dominum eum appellat…"')]),
 U('20:42', G('20:42'), 'For David himself says in the Book of Psalms, \'The Lord said to my Lord, Sit at my right hand,', 'Inside the attested paragraph 20:41–44.'),
 U('20:43', G('20:43'), 'until I make your enemies your footstool.\'', 'Inside the attested paragraph 20:41–44.'),
 A('20:44', G('20:44'), 'David thus calls him Lord, so how is he his son?"',
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
 "marriage… they are equal to angels and are sons of God\". He asks how the Christ can be David's son when David calls him "
 "Lord. The parable of the tenants with the rejected stone (20:9–18) and the proof of the resurrection from Moses at the bush "
 "(20:37–38) are absent: Epiphanius states that the text lacked them."
)

NOTES = [
 dict(term='John\'s baptism (20:1–8)', cat='textual', refs=['20:1', '20:4', '20:5', '20:6', '20:8'], text=(
  "Tertullian, Marc. 4.38.1–2: Christ knew where John's baptism came from, and asked so that the Pharisees would judge "
  "themselves. \"Why did you not believe him?\" shows that he wanted John to be believed, and so that John's baptism was the "
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
  "spoken well\" (20:39) follows directly on the sayings about the resurrection.")),
 dict(term='Resurrection without the patriarchs', cat='theological', refs=['20:35', '20:36'], text=(
  "Interpretation. In this text the answer about the resurrection is that the worthy \"neither marry nor are given in "
  "marriage, for they cannot die any more, because they are equal to angels and are sons of God, being sons of the "
  "resurrection\". There is no argument from the God of Abraham, Isaac and Jacob, as there are no patriarchs in the kingdom "
  "at 13:28. The resurrection is described as a state God grants to the worthy, \"equal to angels\" and \"sons of "
  "God\". It is not described as the return of the body that was buried. The witnesses do not say how the community behind "
  "the text pictured it.")),
 dict(term='David\'s Lord (20:41–44)', cat='textual', refs=['20:41', '20:44'], text=(
  "Tertullian, Marc. 4.38.10: the scribes thought the Christ was David's son; David calls him Lord. Tertullian connects this "
  "with the blind man's \"son of David\" (18:38): Jesus accepted that title then and now shows he is also David's Lord. "
  "20:42–43, the quotation of Psalm 110:1, are not cited and are printed in grey. 20:45–47, the warning against the "
  "scribes, form a paragraph with no attested verse and are not printed.")),
]
