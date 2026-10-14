"""Batch 3, chapter 8 of the reconstruction: Luke 10:1–42."""
from buildlib import greek
from batch1_ch2 import U, A
from batch3_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}

ENTRIES = [
 A('10:1', G('10:1', [('ἑβδομήκοντα δύο καὶ', 'ἑβδομήκοντα καὶ')]),
   'And after these things the lord appointed seventy others, and sent them two by two before his face into every city and place where he himself was about to come.',
   'present (Marc. 4.24.1–2)', [T('4.24.1', '"Adlegit et alios septuaginta apostolos super duodecim."'),
                                T('4.24.2', '"hi autem in civitates mittebantur".')],
   wording='NA27 has no καί before ἑτέρους (SBLGNT has it — checked on the page image). Marcionite reading adopted: "seventy" without NA27\'s bracketed [δύο] ("seventy-two"). Tertullian has septuaginta and builds his comparison on the seventy palm trees of Elim (Exod 15:27); Roth: "Tertullian here attests the former [seventy] as Marcion\'s reading" (rated very likely). A Marcion witness lacks the bracketed word, so it is not printed (METHOD §5.7). NA27 apparatus for the omission: ℵ A C L W Θ Ξ Ψ f1.13 𝔐 f q sy(s).p bo; Irlat Cl Or. The second bracketed [δύο] ("two by two") is not attested either way and is printed.'),
 U('10:2', G('10:2'), 'And he was saying to them, "The harvest is great, but the workers are few; so beg the lord of the harvest to drive out workers into his harvest.',
   'Inside the attested paragraph 10:1–12.'),
 U('10:3', G('10:3'), 'Go away; look, I am sending you out like lambs in the middle of wolves.', 'Inside the attested paragraph 10:1–12.'),
 A('10:4', G('10:4'), 'Do not carry a purse, nor a bag, nor sandals, and greet no one on the road.',
   'present (Marc. 4.24.2–3)', [T('4.24.2', '"Etiam calciamenta portare vetuit illos… Neminem, inquit, per viam salutaveritis."')],
   wording='NA27. Tertullian also says Christ forbade the disciples "even a staff" (4.24.1, nec virgam); no Greek manuscript has a staff in this verse, and Roth takes it from the mission of the twelve (9:3), brought in to match Elisha\'s staff (2 Kgs 4:29, quoted in 4.24.3).'),
 A('10:5', G('10:5'), "And whatever house you go into, first say, 'Peace to this house.'",
   'present (Marc. 4.24.4)', [T('4.24.4', '"Sic et dominus, in quam introissent domum, pacem ei dicere."')]),
 U('10:6', G('10:6'), 'And if a son of peace is there, your peace will rest upon him; but if not, it will turn back to you.',
   'Inside the attested paragraph 10:1–12. NA27 reads ἐκεῖ ᾖ and μή γε (SBLGNT ᾖ ἐκεῖ, μήγε — checked on the page image).'),
 A('10:7', G('10:7'), 'And stay in that same house, eating and drinking what comes from them, for the worker is worthy of his wage. Do not move from house to house.',
   'present (Marc. 4.24.4–5)', [T('4.24.4', '"Dignus autem operarius mercede sua" (Moreschini; Evans: "Dignus est autem…"), read as the Creator\'s own rule (Deut 25:4).')]),
 A('10:8', G('10:8'), 'And whatever city you go into and they receive you, eat what is set before you,',
   'present (Marc. 4.24.7)', [T('4.24.7', '"in salutem scilicet eorum qui annuntiationem eius recepissent" — an allusion to those who welcome them (δέχωνται).')]),
 A('10:9', G('10:9'), "and heal the weak in it, and say to them, 'The kingdom of God has come near to you.'",
   'present (Marc. 4.24.5–6)', [T('4.24.5', '"Regnum dei… dum illud iubet annuntiari appropinquasse."')],
   wording='NA27. Tertullian\'s report is indirect and does not show whether ἐφ\' ὑμᾶς ("to you") stood in this verse.'),
 A('10:10', G('10:10'), 'But whatever city you go into and they do not receive you, going out into its streets, say,',
   'present (Marc. 4.24.7)', [T('4.24.7', '"Etiam adicit, ut eis qui illos non recepissent dicerent…"')]),
 A('10:11', G('10:11'), "'Even the dust of your city that has stuck to us on our feet we wipe off against you; but know this, that the kingdom of God has come near.'",
   'present (Marc. 4.24.7)', [T('4.24.7', '"Scitote tamen appropinquasse regnum dei… Sic et pulverem iubet excuti in illos in testificationem."')],
   wording='NA27, which reads ἤγγικεν without ἐφ\' ὑμᾶς and cites Tertullian\'s Marcion for that text (McionT). "Shake off" (excuti) and "for a testimony" come from the mission of the twelve (9:5); Roth does not count them for this verse.'),
 A('10:16', G('10:16'), 'The one who hears you hears me, and the one who sets you aside sets me aside; and the one who sets me aside sets aside the one who sent me."',
   'present (Marc. 4.24.8)', [T('4.24.8', '"Qui vos spernit, me spernit."')]),
 U('10:17', G('10:17', [('οἱ ἑβδομήκοντα δύο μετὰ', 'οἱ ἑβδομήκοντα μετὰ')]),
   'And the seventy returned with joy, saying, "Lord, even the daimons are subject to us in your name."',
   'Inside the attested paragraph 10:17–20. NA27 brackets [δύο] here as at 10:1; the attested number at 10:1 is seventy, and the bracketed word is not printed here either.'),
 A('10:19', G('10:19'), '"Look, I have given you the authority to tread upon snakes and scorpions, and over all the power of the enemy, and nothing at all will wrong you.',
   'present (Marc. 4.24.9, 12)', [T('4.24.9', '"Quis nunc dabit potestatem calcandi super colubros et scorpios?"'),
                                  T('4.24.12', '"tunc et scorpios et serpentes sanctis suis subdidit".')]),
 U('10:20', G('10:20'), 'But do not rejoice in this, that the spirits are subject to you; but rejoice that your names have been written in the heavens."',
   'Inside the attested paragraph 10:17–20.'),
 A('10:21', G('10:21', [('Ἐξομολογοῦμαί σοι, πάτερ κύριε τοῦ οὐρανοῦ καὶ τῆς γῆς, ὅτι ἀπέκρυψας ταῦτα ἀπὸ σοφῶν καὶ συνετῶν, καὶ ἀπεκάλυψας αὐτὰ νηπίοις',
                         'Εὐχαριστῶ σοι, κύριε τοῦ οὐρανοῦ, ὅτι ἅτινα ἦν κρυπτὰ σοφοῖς καὶ συνετοῖς ἀπεκάλυψας νηπίοις')]),
   'In that very hour he exulted in the holy spirit and said, "I give thanks to you, Lord of heaven, that what was hidden from the wise and the understanding, you revealed to infants. Yes, the Father, for so it was well pleasing before you.',
   'present (Marc. 4.25.1, 3, 6; Pan. 42.11.6, sch. 22)',
   [E(22, '»εὐχαριστῶ σοι, κύριε τοῦ οὐρανοῦ«. οὐκ εἶχεν δὲ »καὶ τῆς γῆς«, οὔτε »πάτερ« εἶχεν. ἐλέγχεται δέ· κάτω γὰρ εἶχεν »ναί, ὁ πατήρ«.'),
    T('4.25.1', '"Gratias enim, inquit, ago, et confiteor, domine caeli, quod ea quae erant abscondita sapientibus et prudentibus, revelaveris parvulis."'),
    T('4.25.6', '"Sed in destructionem, inquis, uti traduceret eas" — the Marcionite reading of the verse, which requires that the God who reveals is not said to have hidden.')],
   wording=('Marcionite readings adopted. (1) εὐχαριστῶ σοι for ἐξομολογοῦμαί σοι: both witnesses (gratias ago; Roth: very likely). Tertullian\'s added "et confiteor" is in his text only and is not adopted (Roth: probable). '
            '(2) No vocative πάτερ and no καὶ τῆς γῆς: Epiphanius states both absences, and Tertullian\'s quotation lacks both (METHOD §5.3). NA27 apparatus for the omission of καὶ τῆς γῆς: 𝔓45; McionT,E. '
            '(3) "What was hidden from the wise and understanding you have revealed to little children": Tertullian\'s Latin has one verb of hiding, impersonal (ea quae erant abscondita), and cannot render NA27\'s "you hid these things… and revealed them". His reply in 4.25.6 answers a Marcionite reading that depends on God not being the subject of the hiding. The Greek printed is Roth\'s retroversion (after Harnack), rated very likely; the exact Greek words are not attested. '
            '(4) "Yes, the Father" is attested by Epiphanius; the closing clause is not cited and is printed in the NA27 wording. NA27\'s opening, with [ἐν] τῷ πνεύματι (SBLGNT without ἐν), is printed.')),
 A('10:22', G('10:22', [('τίς ἐστιν ὁ υἱὸς εἰ μὴ ὁ πατήρ, καὶ τίς ἐστιν ὁ πατὴρ εἰ μὴ ὁ υἱὸς',
                         'τίς ἐστιν ὁ πατὴρ εἰ μὴ ὁ υἱός, καὶ τίς ἐστιν ὁ υἱὸς εἰ μὴ ὁ πατὴρ')]),
   'All things were handed over to me by my Father, and no one knows who the Father is except the son, and who the son is except the Father, and the one to whom the son wishes to reveal him."',
   'present (Marc. 4.25.7, 10; Adam. 44,1–2; Eznik)',
   [T('4.25.7', '"Omnia sibi tradita dicit a patre."'),
    T('4.25.10', '"Sed, Nemo scit qui sit pater, nisi filius, et qui sit filius, nisi pater, et cuicunque filius revelaverit. Atque ita Christus ignotum deum praedicavit."')],
   wording=('Marcionite reading adopted: the Father named first ("who the Father is except the son, and who the son is except the Father"; Roth: very likely). Tertullian\'s quotation has this order; the words in brackets that follow it in the manuscripts of 4.25.10 are a copyist\'s addition from Matthew 11:27 (Roth, after Braun and the editors). '
            'Tertullian\'s "a patre" lacks μου ("my"); NA27 cites McionT for the omission with D a c l vgww sys. One witness, and Tertullian also writes "the Father" in Prax. 24.5; μου is printed. The present tense γινώσκει is confirmed by Tertullian\'s scit.')),
 A('10:23', G('10:23'), 'And turning to the learners privately, he said, "Fortunate are the eyes that see what you see.',
   'present (Marc. 4.25.12)', [T('4.25.12', '"Beati oculi qui vident quae videtis".')]),
 A('10:24', G('10:24'), 'For I tell you that many prophets and kings wanted to see what you see and did not see it, and to hear what you hear and did not hear it."',
   'present (Marc. 4.25.12–13)', [T('4.25.12', '"dico enim vobis, quia prophetae non viderunt quae vos videtis".')],
   wording='NA27. Tertullian\'s quotation is shorter: "the prophets did not see what you see", without "many", "and kings", "wanted to see" and the clause on hearing. NA27 cites McionT with D and the Old Latin for the omission of "and kings". One witness, which may abridge (Roth: possible only); NA27 printed and the evidence noted.',
   western='Without καὶ βασιλεῖς: D it with Tertullian\'s Marcion.'),
 A('10:25', G('10:25', [('ζωὴν αἰώνιον κληρονομήσω', 'ζωὴν κληρονομήσω')]),
   'And look, a certain expert in the law stood up, putting him to the test, saying, "Teacher, by doing what shall I inherit life?"',
   'present (Marc. 4.25.14–18; 4.19.7; Pan. 42.11.6, sch. 23)',
   [T('4.25.14', '"In evangelio veritatis legis doctor dominum aggressus, Quid faciens, inquit, vitam aeternam consequar? In haeretico vita solummodo posita est, sine aeternae mentione."'),
    T('4.25.18', '"Viderit nunc si aeternam nostri addiderunt."'),
    E(23, 'εἶπεν τῷ νομικῷ… (the lawyer\'s question is presupposed).')],
   wording='Marcionite reading adopted: ζωήν without αἰώνιον. Tertullian states it as a difference between the two texts ("in the heretical gospel only \'life\' is set down, with no mention of \'eternal\'"), and in 4.25.18 allows that his own side may have added the word. Roth: very likely. Tertullian does not quote "Teacher" (D also lacks it); one witness, printed.'),
 A('10:26', G('10:26'), 'And he said to him, "In the law, what is written? How do you read?"',
   'present (Pan. 42.11.6, sch. 23)', [E(23, 'εἶπεν τῷ νομικῷ »ἐν τῷ νόμῳ τί γέγραπται;«')]),
 A('10:27', G('10:27'), 'And he answered and said, "You shall love the Lord your God out of your whole heart, and with your whole soul, and with your whole strength, and with your whole mind; and your neighbour as yourself."',
   'present (Marc. 4.25.14–15)', [T('4.25.14', '"Diliges dominum deum tuum ex toto corde tuo et ex tota anima tua et totis viribus tuis".')],
   wording='NA27. Tertullian quotes three clauses (heart, soul, strength) and not the clause on the mind or the neighbour. NA27 cites McionT with D and the Old Latin for the omission of "and with all your mind". Tertullian\'s three clauses are those of Deut 6:5, which he quotes in that form in 4.27.4, so the shorter form may be his. One witness; NA27 printed and the evidence noted.',
   western='Without "and with all your mind": D it with Tertullian\'s Marcion.'),
 A('10:28', G('10:28'), 'And he said to him, "You have answered rightly; do this, and you will live."',
   'present (Pan. 42.11.6, sch. 23)', [E(23, 'καὶ ἀποκριθεὶς μετὰ τὴν ἀπόκρισιν τοῦ νομικοῦ εἶπεν »ὀρθῶς εἶπες, τοῦτο ποίει, καὶ ζήσῃ«.')],
   wording='NA27. Epiphanius has εἶπες ("you have said") for ἀπεκρίθης ("you have answered"); Roth: possible only. Not adopted.'),
]

OMITTED = [
 dict(ref='10:12–15', cls='U−', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason=('Sodom on that day (10:12) and the woes on Chorazin, Bethsaida and Capernaum (10:13–15). Tertullian\'s commentary is continuous here (4.24.7 on 10:11, 4.24.8 on 10:16). '
              'At 10:11 he argues that the command must carry a threat of judgement, "or he commands it in vain", and that the testimony "portends threats" (4.24.7–8). '
              'A saying that names the judgement on Sodom, the Creator\'s own, and a series of woes would have been his proof; he infers the threat instead. In 4.27.1 he counts Christ\'s "woe" as a mark of the Creator. '
              '10:12 closes the NA27 paragraph 10:1–12; 10:13–15 form a paragraph of their own.'))),
 dict(ref='10:18', cls='U−', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason=('"I saw Satan fall like lightning from heaven." At 10:19 Tertullian explains the snakes and scorpions as spiritual powers whose prince the Creator calls serpent and dragon, and quotes Ps 91:13 and Isa 27:1 for Christ\'s victory over him (4.24.10). '
              'A saying of Jesus describing the fall of Satan from heaven, the image of Isa 14:12, would have served that argument better than the texts he brings in. Its citation by Marinus in the Dialogue of Adamantius (134,5–6) is not evidence for Marcion\'s text (Roth).'))),
 dict(ref='10:29–37', cls='U−', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason=('The parable of the Samaritan. In both witnesses the exchange with the lawyer closes at 10:28: Epiphanius\' sch. 23 ends with "do this and you will live" and sch. 24 is on 11:5; Tertullian passes from 10:28 (4.25.14–18) to 11:1 (4.26.1). '
              'Tertullian\'s aim in 4.25.14–18 is to show that Christ taught the "head of the law" of the Creator; a parable expounding the law\'s own command (Lev 19:18), with a priest and a Levite in it, would have been his best evidence, and any Marcionite use of it against the Creator\'s cult would have drawn an answer. '
              'Neither witness has the neighbour clause of 10:27, which the parable explains. NA27 begins a new paragraph at 10:29.'))),
 dict(ref='10:38–42', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason=('Martha and Mary. A separate NA27 paragraph with no attested verse (METHOD §4.3). Neither witness mentions it: Tertullian passes from 10:28 to 11:1, Epiphanius from 10:28 to 11:5. '
              'Nothing in the passage bears on Tertullian\'s or Epiphanius\' arguments, so their silence does not show absence; the class is "undetermined", not "attested absent".'))),
]

PREAMBLE = (
 "The mission of the seventy and what follows from it. Jesus sends out seventy others, two by two, with the instructions "
 "Tertullian reads as the Creator's own: no sandals, no greetings on the road, peace to the house, \"the worker is worthy of his "
 "wage\", and the dust wiped off against a town that refuses them, \"but know this, that the kingdom of God has come near\". "
 "Whoever rejects them rejects him; he gives them authority over snakes and scorpions. He then thanks the \"Lord of heaven\" "
 "that what was hidden from the wise has been revealed to little children, and says that no one knows who the Father is "
 "except the son. To a lawyer who asks what he must do to inherit life (\"life\", not \"eternal life\", as Tertullian points "
 "out) he answers with the command to love God, and \"do this and you will live\". Canonical Luke's judgement on Sodom and the "
 "woes on the Galilean towns, \"I saw Satan fall\", the parable of the Samaritan and the visit to Martha and Mary are not "
 "cited by either witness and are not printed."
)

NOTES = [
 dict(term='The seventy (10:1–11)', cat='textual', refs=['10:1', '10:4', '10:5', '10:7', '10:9', '10:10', '10:11'], text=(
  "Tertullian, Marc. 4.24.1–7 follows the instructions in order: seventy others appointed, sent into towns, no sandals, no "
  "greetings on the road (as Elisha told Gehazi, 2 Kgs 4:29), peace to the house (as Elisha to the Shunammite, 2 Kgs 4:26), "
  "\"the worker is worthy of his wage\" (as the law on the ox, Deut 25:4), the kingdom announced as \"near\", and the words to a "
  "town that refuses them. The number is seventy: Tertullian sets the seventy beside the seventy palms of Elim as he sets the "
  "twelve beside its twelve springs (Exod 15:27). NA27 prints \"seventy [two]\" with the second word bracketed; it is not "
  "printed here (METHOD §5.7). 10:2–3 and 10:6 are not cited and are printed in grey.")),
 dict(term='Not printed: 10:12–15', cat='excision', refs=['10:11', '10:16'], text=(
  "Sodom \"on that day\" and the woes on Chorazin, Bethsaida and Capernaum. Tertullian goes from 10:11 to 10:16 and argues, at "
  "length, that the dust saying implies a judgement: \"if he does not command it as a threat, he commands it in vain\" "
  "(4.24.7). The verses that state the judgement in so many words, and name the Creator's judgement on Sodom, would have ended "
  "the argument. He does not cite them. They are classed \"unattested, probably absent\".")),
 dict(term='Authority over the enemy (10:16–20)', cat='textual', refs=['10:16', '10:17', '10:19', '10:20'], text=(
  "Tertullian quotes \"The one who sets you aside sets me aside\" (4.24.8) and asks who will give power \"to tread upon snakes and "
  "scorpions\" if not the Lord of all creatures (4.24.9). He reads the snakes and scorpions as the spiritual powers of "
  "wickedness and their prince as the serpent and dragon of Ps 91:13 and Isa 27:1 (4.24.10). \"I saw Satan fall like "
  "lightning from heaven\" (10:18), which would have suited that reading, is not cited and is not printed. 10:17 and 10:20 are "
  "printed in grey. \"Seventy\" at 10:17 follows 10:1.")),
 dict(term='"I give thanks to you, Lord of heaven" (10:21)', cat='textual', refs=['10:21'], text=(
  "Both witnesses quote the thanksgiving. Epiphanius, sch. 22: \"I give thanks to you, Lord of heaven\"; the text \"did not have 'and of "
  "the earth', nor did it have 'Father'\", but it did have \"Yes, the Father\" further on. Tertullian, Marc. 4.25.1: \"Gratias ago, et "
  "confiteor, domine caeli, quod ea quae erant abscondita sapientibus et prudentibus, revelaveris parvulis.\" The address "
  "without \"and of the earth\" is also the reading of 𝔓45. In Tertullian the hiding has no stated subject: what was hidden, "
  "God has revealed. His later reply that the Marcionite God, revealing what the Creator had hidden, would have been doing the "
  "Creator's work (4.25.6) presupposes that wording. The Greek printed is Roth's retroversion; the sense is attested, the "
  "exact words are not. Tertullian's \"et confiteor\" (= canonical ἐξομολογοῦμαι) is in his text only and is not printed.")),
 dict(term='"Who the Father is" (10:22)', cat='textual', refs=['10:22'], text=(
  "Tertullian, Marc. 4.25.10 quotes the saying with the Father first: \"No one knows who the Father is except the son, and who "
  "the son is except the Father\" (canonical Luke has the son first). The order is attested also by the Dialogue of "
  "Adamantius and by Eznik, and is found in some manuscripts and fathers (Roth). Tertullian comments: \"and so Christ preached "
  "an unknown God\" — the Marcionite reading of the saying, which he answers from Isaiah (\"Israel did not know me\", Isa "
  "1:3). The words in brackets after the quotation in the manuscripts of Tertullian give Matthew's wording and are a copyist's "
  "addition.")),
 dict(term='The lawyer\'s question (10:25–28)', cat='textual', refs=['10:25', '10:26', '10:27', '10:28'], text=(
  "Tertullian, Marc. 4.25.14: \"In the gospel of truth the lawyer asks, 'What must I do to obtain eternal life?' In the "
  "heretical one only 'life' is set down, with no mention of 'eternal'.\" This is one of the few places where Tertullian states "
  "a difference between the two texts, and in 4.25.18 he allows that \"ours\" may have added the word. The text printed reads "
  "\"inherit life\". Epiphanius, sch. 23 quotes Jesus' question \"What is written in the law?\" and his reply \"You have said "
  "rightly; do this and you will live\" (10:26, 28). Tertullian's quotation of the command (10:27) has three clauses (heart, "
  "soul, strength) and no neighbour clause; NA27 cites his Marcion for the lack of \"with all your mind\". These are noted, "
  "not adopted (one witness).")),
 dict(term='Not printed: 10:29–42', cat='excision', refs=['10:28'], text=(
  "The parable of the Samaritan (10:29–37) and the visit to Martha and Mary (10:38–42). In both witnesses the exchange with "
  "the lawyer ends at 10:28; Tertullian goes on to 11:1 and Epiphanius to 11:5. For the parable, silence counts: it expounds "
  "the law's own command of love, the point Tertullian was arguing (\"he set before him the head of the law\", 4.25.15), and "
  "it would have served him. It is classed \"unattested, probably absent\". The Martha and Mary passage touches nothing either "
  "father argues, so their silence shows nothing; it is \"unattested, undetermined\" and, as a paragraph with no attested "
  "verse, is not printed (METHOD §4.3).")),
 dict(term='Life and the law', cat='theological', refs=['10:25', '10:27', '10:28'], text=(
  "Interpretation. In the attested text the way to \"life\" is the command of Deuteronomy 6:5, and Jesus' answer is \"do "
  "this, and you will live\" (cf. Lev 18:5). Tertullian takes the shorter question to concern the long life the law promises "
  "(4.25.14); the text itself does not say which life is meant. What it does show is a teacher who answers a question about "
  "life with the law's first command and a call to do it — the pattern of 6:46 and 8:21 in this reconstruction, and of the "
  "Epistle of James (\"be doers of the word\", Jas 1:22).")),
 dict(term='ἑβδομήκοντα, "seventy"', cat='translation', refs=['10:1'], text='The reading of this text: seventy, without "two".'),
 dict(term='ὁ κύριος, "the lord"', cat='translation', refs=['10:1'], text="The narrator's name for Jesus, as at 7:13."),
 dict(term='ἀνέδειξεν, "appointed"', cat='translation', refs=['10:1'], text='To show forth, designate.'),
 dict(term='πρὸ προσώπου αὐτοῦ, "before his face"', cat='translation', refs=['10:1'], text='A Hebrew idiom for "ahead of him", kept as at 9:52.'),
 dict(term='τοῦ κυρίου τοῦ θερισμοῦ, "the lord of the harvest"', cat='translation', refs=['10:2'], text='The owner of the harvest. Lower case: the image is of a landowner.'),
 dict(term='ἐκβάλῃ, "drive out"', cat='translation', refs=['10:2'], text='ἐκβάλλω, the verb used for driving out daimons (9:40). "Send out" softens it.'),
 dict(term='δεήθητε, "beg"', cat='translation', refs=['10:2'], text='δέομαι, to ask out of need.'),
 dict(term='ἀσπάσησθε, "greet"', cat='translation', refs=['10:4'], text='Greetings on the road were long and formal.'),
 dict(term='υἱὸς εἰρήνης, "a son of peace"', cat='translation', refs=['10:6'], text='A Semitic idiom: one who belongs to peace.'),
 dict(term='ἐπαναπαήσεται, "will rest upon"', cat='translation', refs=['10:6'], text='To come to rest on.'),
 dict(term='μισθοῦ, "wage"', cat='translation', refs=['10:7'], text='As at 6:23.'),
 dict(term='ἀσθενεῖς, "the weak"', cat='translation', refs=['10:9'], text='Those without strength, the sick.'),
 dict(term='Ἤγγικεν, "has come near"', cat='translation', refs=['10:9'], text='A perfect: it has drawn near and is near.'),
 dict(term='ἀπομασσόμεθα, "we wipe off"', cat='translation', refs=['10:11'], text='To wipe off, as one wipes off something unclean.'),
 dict(term='ἀθετῶν, "sets aside"', cat='translation', refs=['10:16'], text='To set aside, treat as nothing, reject.'),
 dict(term='ὑποτάσσεται, "are subject"', cat='translation', refs=['10:17'], text='To be placed under, to submit.'),
 dict(term='ὄφεων, "snakes"', cat='translation', refs=['10:19'], text='ὄφις, serpent, snake.'),
 dict(term='οὐδὲν… οὐ μή, "nothing at all"', cat='translation', refs=['10:19'], text='A double negative, the strongest Greek denial.'),
 dict(term='ἀδικήσῃ, "wrong"', cat='translation', refs=['10:19'], text='To do wrong to, injure.'),
 dict(term='ἐγγέγραπται, "have been written"', cat='translation', refs=['10:20'], text='A perfect: written in, and standing written.'),
 dict(term='ἐν τοῖς οὐρανοῖς, "in the heavens"', cat='translation', refs=['10:20'], text='Plural, as the Greek has it.'),
 dict(term='ἠγαλλιάσατο, "exulted"', cat='translation', refs=['10:21'], text='To leap for joy, exult.'),
 dict(term='Εὐχαριστῶ, "I give thanks"', cat='translation', refs=['10:21'], text='The reading of this text. Canonical Luke has ἐξομολογοῦμαι, "I acknowledge, praise".'),
 dict(term='κύριε τοῦ οὐρανοῦ, "Lord of heaven"', cat='translation', refs=['10:21'], text='Addressed to God, so capitalised. This text lacks "Father" before it and "and of earth" after it.'),
 dict(term='ἅτινα ἦν κρυπτά… ἀπεκάλυψας, "what was hidden… you revealed"', cat='translation', refs=['10:21'], text='The reading of this text: things that were hidden. Canonical Luke has "you hid these things… and revealed them".'),
 dict(term='νηπίοις, "infants"', cat='translation', refs=['10:21'], text='Literally "not yet speaking": babies, the simple.'),
 dict(term='ναὶ ὁ πατήρ, "yes, the Father"', cat='translation', refs=['10:21'], text='The nominative with the article used as an address, word for word.'),
 dict(term='εὐδοκία, "well pleasing"', cat='translation', refs=['10:21'], text='Good pleasure, what seems good.'),
 dict(term='παρεδόθη, "were handed over"', cat='translation', refs=['10:22'], text='παραδίδωμι, as at 9:44.'),
 dict(term='ὁ υἱός, "the son"', cat='translation', refs=['10:22'], text='Lower case, as the Greek has no capitals.'),
 dict(term='βούληται, "wishes"', cat='translation', refs=['10:22'], text='To will, decide.'),
 dict(term='νομικός, "expert in the law"', cat='translation', refs=['10:25'], text='One skilled in the law of Moses.'),
 dict(term='ἀνέστη ἐκπειράζων, "stood up, putting him to the test"', cat='translation', refs=['10:25'], text='ἀνίστημι; ἐκπειράζω, to test thoroughly.'),
 dict(term='ζωήν, "life"', cat='translation', refs=['10:25'], text='The reading of this text, "life" alone. Canonical Luke has "life of the age".'),
 dict(term='κληρονομήσω, "inherit"', cat='translation', refs=['10:25'], text="To receive as one's lot or share."),
 dict(term='πῶς ἀναγινώσκεις, "how do you read?"', cat='translation', refs=['10:26'], text='Literally that: how do you read it?'),
 dict(term='κύριον τὸν θεόν σου, "the Lord your God"', cat='translation', refs=['10:27'], text='Quoting Deut 6:5. κύριος stands for the divine name, so it is capitalised.'),
 dict(term='ἐξ… καὶ ἐν…, "out of… and with…"', cat='translation', refs=['10:27'], text='The Greek changes the preposition after the first member.'),
 dict(term='διανοίᾳ, "mind"', cat='translation', refs=['10:27'], text='Understanding, the thinking mind.'),
 dict(term='τὸν πλησίον, "your neighbour"', cat='translation', refs=['10:27'], text='Literally "the one near".'),
]
