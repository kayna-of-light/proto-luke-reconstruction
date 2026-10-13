"""Batch 6, chapter 20 of the reconstruction: Luke 22:1–71 (22:54–62 restored by method, METHOD §11)."""
from buildlib import greek, R
from batch1_ch2 import U, A
from batch6_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}

T402 = T('4.40.2', '"Poterat et ab extraneo quolibet tradi: ne dicerem et in hoc psalmum expunctum: Qui mecum panem edit, levabit in me plantam. Poterat et sine praemio tradi."')
T403 = T('4.40.3', '"acceptum panem et distributum discipulis corpus suum illum fecit, Hoc est corpus meum dicendo, id est figura corporis mei… Aut si propterea panem corpus sibi finxit quia corporis carebat veritate, ergo panem debuit tradere pro nobis."')
T412 = T('4.41.2', '"Nam et Petrum praesumptorie aliquid elocutum negationi potius destinando, zeloten deum tibi ostendit. Debuit etiam osculo tradi…"')

CR_22_54 = ('Peter\'s denial in the high priest\'s courtyard: a paragraph with no attested verse. The prediction of the denial (22:34) is attested; '
            'its fulfilment is not cited by either witness.')
GR_22_54 = ('by its words, the printed 22:63, "the men holding him (οἱ συνέχοντες αὐτόν)", needs someone to have taken hold of him, and in the printed text no one has '
            '(22:48 ends with the kiss); the seizing and the leading into the high priest\'s house are 22:54. The printed 22:66, "as it became day", follows a night '
            'the printed text does not tell. By its mechanics: the printed text sets up faith\'s failure and return three times (22:32 "when once you have turned back, '
            'strengthen your brothers"; 22:33; 22:34 "you will deny three times") and never shows them; 22:54–62 is the failure, the Lord\'s look, the remembering '
            'of his word, and the weeping. Reading: docs/research/correspondence/word_by_word.md, chapter 20, test of 22:54–62.')
W54 = lambda ref, en: R(ref, G(ref), en, 'U?', 'unattested', CR_22_54, GR_22_54, wording='NA27 (checked on the page image, p. 236).')

ENTRIES = [
 A('22:1', G('22:1'), 'Now the feast of Unleavened Bread drew near, which is called the Passover.',
   'present (Marc. 4.40.1)', [T('4.40.1', '"Nam ex tot festis Iudaeorum paschae diem elegit."')],
   wording='NA27. Tertullian attests only "Passover".'),
 U('22:2', G('22:2'), 'And the chief priests and the scribes were seeking how to put him to death, for they feared the people.', 'Inside the attested paragraph 22:1–2.'),
 A('22:3', greek('22:3', text='Ἰούδας δὲ ὁ καλούμενος Ἰσκαριώτης, ὢν ἐκ τοῦ ἀριθμοῦ τῶν δώδεκα,'),
   'Now Judas called Iscariot, who was of the number of the twelve,',
   'present (Marc. 4.40.2); "Satan entered into" not present (Marc. 5.6.7)',
   [T402, T('5.6.7', '"Scriptum est enim apud me satanam in Iudam introisse. Secundum autem Marcionem…"')],
   wording=('NA27 without "Satan entered into" (Εἰσῆλθεν δὲ Σατανᾶς εἰς). Tertullian writes that "in my text" (apud me) Satan entered Judas, and sets this against "according to Marcion"; Roth: "was not present". '
            'What the verse had in their place is not attested. The remaining words are printed in the nominative, so that the sentence runs on into 22:4; the case is an editorial adjustment, not an attested wording. '
            'Tertullian\'s "he could have been betrayed by any stranger" and Ps 41:9 ("he who eats bread with me") refer to Judas as one of the Twelve (Roth: wording possible only).')),
 A('22:4', G('22:4', [('τὸ πῶς αὐτοῖς παραδῷ αὐτόν.', 'τὸ πῶς αὐτὸν παραδῷ αὐτοῖς.')]),
   'went away and conferred with the chief priests and officers how he might hand him over to them.',
   'present (Pan. 42.11.6, sch. 60; Marc. 4.40.2)',
   [E(60, '»συνελάλησε τοῖς στρατηγοῖς τὸ πῶς αὐτὸν παραδῷ αὐτοῖς«.'), T402],
   wording=('Marcionite word order adopted: τὸ πῶς αὐτὸν παραδῷ αὐτοῖς (NA27 αὐτοῖς παραδῷ αὐτόν). Epiphanius quotes it so in both listings; Roth: very likely, "the word order found in many manuscripts". '
            'Epiphanius has only "the officers"; whether the chief priests were named is unattested (Roth), and NA27 is printed. NA27 notes D it sys.c without "and officers".')),
 A('22:5', G('22:5'), 'And they were glad, and agreed to give him money.',
   'present (Marc. 4.40.2)', [T402], wording='NA27. Tertullian attests the payment ("sine praemio"); Roth: ἀργύριον.'),
 U('22:6', G('22:6'), 'So he consented and sought an opportunity to hand him over to them in the absence of a crowd.', 'Inside the attested paragraph 22:3–6.'),
 U('22:7', G('22:7'), 'Then came the day of Unleavened Bread, on which the Passover lamb had to be sacrificed.', 'Opens the attested paragraph 22:7–13. NA27 [ἐν] (SBLGNT without it).'),
 A('22:8', G('22:8'), 'So he sent Peter and John, saying, "Go and prepare the Passover for us, that we may eat it."',
   'present (Pan. 42.11.6, sch. 61)', [E(61, '»καὶ εἶπεν τῷ Πέτρῳ καὶ τοῖς λοιποῖς· ἀπελθόντες ἑτοιμάσατε ἵνα φάγωμεν τὸ Πάσχα«.')],
   wording=('NA27. Epiphanius\' wording ("he said to Peter and the rest: go and prepare, that we may eat the Passover") is his own, with no support in the manuscripts; Roth: possible only. '
            'His point (elenchus 61) is that Jesus had the Passover prepared for himself.')),
 U('22:9', G('22:9'), 'They said to him, "Where will you have us prepare it?"', 'Inside the attested paragraph 22:7–13.'),
 U('22:10', G('22:10'), 'He said to them, "Look, when you have entered the city, a man carrying a jar of water will meet you. Follow him into the house that he enters,', 'Inside the attested paragraph 22:7–13.'),
 U('22:11', G('22:11'), 'and tell the master of the house, "The Teacher says to you, Where is the guest room, where I may eat the Passover with my disciples?"', 'Inside the attested paragraph 22:7–13.'),
 U('22:12', G('22:12'), 'And he will show you a large upper room furnished; prepare it there."', 'Inside the attested paragraph 22:7–13.'),
 U('22:13', G('22:13'), 'And they went and found it just as he had told them, and they prepared the Passover.', 'Inside the attested paragraph 22:7–13.'),
 A('22:14', G('22:14'), 'And when the hour came, he reclined at table, and the apostles with him.',
   'present (Pan. 42.11.6, sch. 62)', [E(62, '»καὶ ἀνέπεσε καὶ οἱ δώδεκα ἀπόστολοι σὺν αὐτῷ«.')],
   wording=('NA27. Epiphanius has "the twelve apostles" (NA27: δώδεκα ἀπόστ. ℵ2 A C W Θ Ψ f1.13 𝔐 …; McionE), as Matt 26:20; Roth: δώδεκα probable only, since Epiphanius may follow Matthew. Not adopted. '
            'He does not quote "when the hour came"; Roth: unattested, not absent.')),
 A('22:15', G('22:15'), 'And he said to them, "I have earnestly desired to eat this Passover with you before I suffer.',
   'present (Marc. 4.40.1, 3; Pan. 42.11.6, sch. 62)',
   [T('4.40.1', '"Ideo et affectum suum ostendit: Concupiscentia concupivi pascha edere vobiscum, antequam patiar."'),
    E(62, '»καὶ εἶπεν· ἐπιθυμίᾳ ἐπεθύμησα τοῦτο τὸ Πάσχα φαγεῖν μεθ\' ὑμῶν πρὸ τοῦ με παθεῖν«.')],
   wording='NA27. The two witnesses agree with NA27 except that Tertullian lacks "this" and Epiphanius "to them"; Roth treats both as the citers\' omissions. Roth also lists Eznik, De Deo 415 (not checked here).'),
 U('22:17', G('22:17'), 'And he took a cup, and when he had given thanks he said, "Take this, and divide it among yourselves.',
   'Inside the attested paragraph 22:14–20. Roth lists Adam. 108,27 ("taking bread and cup and blessing"); those words are spoken by Adamantius, the orthodox speaker, and are not evidence for Marcion\'s text.'),
 U('22:18', G('22:18'), 'For I tell you that from now on I shall not drink of the fruit of the vine until the kingdom of God comes."',
   'Inside the attested paragraph 22:14–20. Epiphanius says that 22:16 was absent; he says nothing of 22:18 (Roth, citing Schmid). NA27 [ὅτι] (SBLGNT without it).'),
 A('22:19', G('22:19'), 'And he took bread, and when he had given thanks, he broke it and gave it to them, saying, "This is my body, which is given for you. Do this in remembrance of me."',
   'present (Marc. 4.40.3, 4)', [T403, T('4.40.4', '"corpus suum vocans panem".')],
   wording=('NA27 (19b–20 printed without brackets, as in NA27). Tertullian attests "he took bread", "gave" and "this is my body"; Roth: very likely. His "then he should have handed over bread for us" alludes to "which is given for you" (Roth: possible). '
            '"Do this in remembrance of me" is unattested.'),
   western='19b–20 are a Western non-interpolation: D and part of the Old Latin end the verse at "my body". This text, attested by Tertullian, had at least part of 19b and 20.'),
 A('22:20', G('22:20'), 'And likewise the cup after they had eaten, saying, "This cup is the new covenant in my blood, which is poured out for you.',
   'present (Marc. 4.40.4, 6)',
   [T('4.40.4', '"Sic et in calicis mentione testamentum constituens sanguine suo obsignatum, substantiam corporis confirmavit."'),
    T('4.40.6', '"Ita et nunc sanguinem suum in vino consecravit, qui tunc vinum in sanguine figuravit."')],
   wording=('NA27. Tertullian attests the cup, the covenant and "my blood"; Roth: probable. Harnack removed "new" on Tertullian\'s silence; Roth: not certain, since Tertullian also adds "sealed". "Which is poured out for you" is unattested. '
            'The previous version omitted this verse as a Western non-interpolation; it is attested for this text.'),
   western='Omitted in D and part of the Old Latin (Western non-interpolation); see 22:19.'),
 U('22:21', G('22:21'), 'But see, the hand of him who betrays me is with me on the table.', 'Inside the attested paragraph 22:21–23.'),
 A('22:22', G('22:22'), 'For the son of man goes as it has been determined, but woe to that man by whom he is betrayed!"',
   'present for 22:22b (Marc. 4.41.1); 22:22a unattested', [T('4.41.1', '"Vae, ait, per quem traditur filius hominis."')],
   wording='NA27. Tertullian quotes "woe… by whom the son of man is betrayed"; his "son of man" may be his own clarification (Roth). Tsutsui\'s view that "as it has been determined" was removed rests on silence and is not adopted.'),
 U('22:23', G('22:23'), 'And they began to question one another, which of them it could be who was going to do this.', 'Inside the attested paragraph 22:21–23.'),
 U('22:31', G('22:31'), '"Simon, Simon, look, Satan has demanded to have you, that he might sift you like wheat,', 'Inside the attested paragraph 22:31–34.'),
 U('22:32', G('22:32'), 'but I have prayed for you that your faith may not fail. And when you have turned again, strengthen your brothers."', 'Inside the attested paragraph 22:31–34.'),
 A('22:33', G('22:33'), 'Peter said to him, "Lord, I am ready to go with you both to prison and to death."',
   'present (Marc. 4.41.2)', [T412], wording='NA27. Roth: attested, but no insight into the wording.'),
 A('22:34', G('22:34'), 'Jesus said, "I tell you, Peter, the cock will not crow this day until you deny three times that you know me."',
   'present (Marc. 4.41.2)', [T412], wording='NA27. Tertullian attests the denial (ἀπαρνήσῃ).'),
 U('22:39', G('22:39'), 'And he came out and went, as was his custom, to the Mount of Olives, and the disciples followed him.', 'Opens the attested paragraph 22:39–46.'),
 U('22:40', G('22:40'), 'And when he came to the place, he said to them, "Pray that you may not enter into temptation."', 'Inside the attested paragraph 22:39–46.'),
 A('22:41', G('22:41'), 'And he withdrew from them about a stone\'s throw, and knelt down and prayed,',
   'present (Pan. 42.11.6, sch. 65)', [E(65, '»ἀπεσπάσθη ἀπ\' αὐτῶν ὡσεὶ λίθου βολὴν καὶ θεὶς τὰ γόνατα προσηύχετο«.')],
   wording='NA27. Epiphanius\' quotation agrees with NA27; Roth: secure. His point is the visible kneeling of a body (elenchus 65).'),
 U('22:42', G('22:42'), 'saying, "Father, if you are willing, remove this cup from me. Nevertheless, not my will, but yours, be done."', 'Inside the attested paragraph 22:39–46.'),
 U('22:45', G('22:45'), 'And when he rose from prayer, he came to the disciples and found them sleeping for sorrow,', 'Inside the attested paragraph 22:39–46.'),
 U('22:46', G('22:46'), 'and he said to them, "Why are you sleeping? Rise and pray that you may not enter into temptation."', 'Inside the attested paragraph 22:39–46.'),
 A('22:47', G('22:47'), 'While he was still speaking, there came a crowd, and the man called Judas, one of the twelve, was leading them. He drew near to Jesus to kiss him,',
   'present (Pan. 42.11.6, sch. 66)', [E(66, '»καὶ ἤγγισε καταφιλῆσαι αὐτὸν Ἰούδας καὶ εἶπεν«.')],
   wording='NA27. Epiphanius\' καταφιλῆσαι and "and said" have no manuscript support in Luke and follow Matt 26:49 (Roth). Not adopted. His point is that Judas kissed real lips (elenchus 66).'),
 A('22:48', G('22:48'), 'but Jesus said to him, "Judas, would you betray the son of man with a kiss?"',
   'present (Marc. 4.41.2)', [T412], wording='NA27. Tertullian attests the kiss and the betrayal.'),
 W54('22:54', 'Then they seized him and led him away and brought him into the house of the high priest. And Peter was following at a distance.'),
 W54('22:55', 'When they had kindled a fire in the middle of the courtyard and sat down together, Peter sat in their midst.'),
 W54('22:56', 'And a servant girl, seeing him seated toward the light and looking intently at him, said, "This man also was with him."'),
 W54('22:57', 'But he denied it, saying, "Woman, I do not know him."'),
 W54('22:58', 'And a little later someone else saw him and said, "You also are one of them." But Peter said, "Man, I am not."'),
 W54('22:59', 'And after about an hour had passed, another kept insisting, saying, "Certainly this man also was with him, for he too is a Galilean."'),
 W54('22:60', 'But Peter said, "Man, I do not know what you are saying." And at once, while he was still speaking, the cock crowed.'),
 W54('22:61', 'And the Lord turned and looked at Peter. And Peter remembered the word of the Lord, how he had said to him, "Before the cock crows today, you will deny me three times."'),
 W54('22:62', 'And he went outside and wept bitterly.'),
 A('22:63', G('22:63'), 'Now the men who were holding Jesus in custody were mocking him as they beat him.',
   'present (Pan. 42.11.6, sch. 68)', [E(68, '»οἱ συνέχοντες ἐνέπαιζον δέροντες καὶ τύπτοντες καὶ λέγοντες· προφήτευσον, τίς ἐστιν ὁ παίσας σε;«')],
   wording='NA27. Epiphanius abbreviates; the elements he quotes agree with NA27 (Roth: very likely).'),
 A('22:64', G('22:64'), 'They also blindfolded him and kept asking him, "Prophesy! Who is it that struck you?"',
   'present (Pan. 42.11.6, sch. 68)', [E(68, '»… τύπτοντες καὶ λέγοντες· προφήτευσον, τίς ἐστιν ὁ παίσας σε;«')],
   wording='NA27. Epiphanius\' "striking" agrees with A W Θ Ψ 𝔐 (ἔτυπτον αὐτοῦ τὸ πρόσωπον); Roth: possible only. Not adopted.'),
 U('22:65', G('22:65'), 'And they said many other things against him, blaspheming him.', 'Inside the attested paragraph 22:63–65.'),
 A('22:66', G('22:66'), 'When day came, the assembly of the elders of the people gathered together, both chief priests and scribes. And they led him away to their council,',
   'present (Marc. 4.41.3)', [T('4.41.3', '"Perductus in consessum an ipse esset Christus interrogatur."')]),
 A('22:67', G('22:67'), 'and they said, "If you are the Anointed One, tell us." But he said to them, "If I tell you, you will not believe,',
   'present (Marc. 4.41.3)', [T('4.41.3', '"Si dixero, enim inquit, vobis non credetis."')],
   wording='NA27. Tertullian\'s "interrogatur" may reflect the question form of D d ("Are you the Christ?"); Roth: undecided. The order "tell you" is uncertain (Roth).'),
 U('22:68', G('22:68'), 'and if I ask you, you will not answer.', 'Inside the attested paragraph 22:66–71.'),
 A('22:69', G('22:69'), 'But from now on the son of man shall be seated at the right hand of the power of God."',
   'present (Marc. 4.41.4)', [T('4.41.4', '"Abhinc, inquit, erit filius hominis sedens ad dexteram virtutis dei."')],
   wording='NA27. Tertullian quotes the verse; Roth: secure, with δέ possibly present.'),
 A('22:70', G('22:70'), 'So they all said, "Are you the Son of God, then?" And he said to them, "You say that I am."',
   'present (Marc. 4.41.4–5)', [T('4.41.4', '"Ergo, inquiunt, tu dei filius es?… Sed respondit, Vos dicitis, quasi non ego."'),
                                T('4.41.5', '"Atquin confirmavit id se esse quod illi dixerant…"')],
   wording='NA27. Tertullian argues that "you say" was an affirmation.'),
 A('22:71', G('22:71'), 'Then they said, "What further testimony do we need? We have heard it ourselves from his own lips."',
   'present (Marc. 4.41.5)', [T('4.41.5', '"et adeo sic fuit pronuntiatio eius, ut perseveraverint in eo quod pronuntiatio sapiebat."')],
   wording='NA27. Roth: attested, but no insight into the wording.'),
]

OMITTED = [
 dict(ref='22:16', cls='A−', app=dict(roth='absent', witnesses=[
      E(63, 'παρέκοψε τὸ »λέγω γὰρ ὑμῖν, οὐ μὴ φάγω αὐτὸ ἀπάρτι, ἕως ἂν πληρωθῇ ἐν τῇ βασιλείᾳ τοῦ θεοῦ«.')],
      decision='not printed', reason='Epiphanius states that the text lacked "I will not eat it until it is fulfilled in the kingdom of God". His explanation (elenchus 63) is that Marcion wanted no food or drink in the kingdom.')),
 dict(ref='22:24–30', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason=('The dispute about who is greatest and the thrones of the twelve: a paragraph with no attested verse (METHOD §4.3). '
              'In elenchus 63 Epiphanius cites "you will sit at my table, eating and drinking in the kingdom" against Marcion and adds "or he cut these out again", which suggests he did not find 22:30 in the text.'))),
 dict(ref='22:35–38', cls='A−', app=dict(roth='absent', witnesses=[
      E(64, 'παρέκοψε τὸ »ὅτε ἀπέστειλα ὑμᾶς, μή τινος ὑστερήσατε;« καὶ τὰ ἑξῆς, διὰ τὸ »καὶ τοῦτο τὸ γεγραμμένον δεῖ τελεσθῆναι, τό· καὶ μετὰ ἀνόμων συνελογίσθη«.')],
      decision='not printed', reason='Epiphanius states that the text lacked "when I sent you out… did you lack anything?" and what follows, for the sake of "this scripture must be fulfilled: he was counted among the lawless". The four verses belong together (Roth; Zahn; Harnack). Tertullian passes from 22:34 to 22:48 (4.41.2).')),
 dict(ref='22:43–44', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason=('The angel from heaven and the sweat like drops of blood. NA27 prints the verses in double brackets, as not part of its text: they are absent from 𝔓75 ℵ1 A B N T W 579 and others, present in ℵ*,2 D L Θ Ψ 0171 f1 𝔐 and known to Justin, Irenaeus and Hippolytus. '
              'No witness cites them for this text. They are not in the NA27 base and are not printed.'))),
 dict(ref='22:49', cls='U−', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='"Lord, shall we strike with the sword?" The swords of 22:38 are absent (sch. 64), and the blow that answers the question (22:50–51) is absent (sch. 67). The verse depends on both.')),
 dict(ref='22:50–51', cls='A−', app=dict(roth='absent', witnesses=[
      E(67, 'παρέκοψεν ὃ ἐποίησε Πέτρος, ὅτε ἐπάταξε καὶ ἀφείλετο τὸ οὖς τοῦ δούλου τοῦ ἀρχιερέως.')],
      decision='not printed', reason='Epiphanius states that the text lacked the cutting off of the servant\'s ear; his elenchus adds that the Lord healed it, so 22:51 was also absent (Roth). Tertullian passes from the kiss (22:48) to the council (22:66; 4.41.2–3).')),
 dict(ref='22:52–53', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='"Have you come out as against a robber…?" A separate NA27 paragraph with no attested verse.')),
]

PREAMBLE = (
 "The Passover, the betrayal and the council. The feast of Unleavened Bread draws near. Judas, one of the twelve, agrees "
 "with the chief priests and officers to hand Jesus over for money; in this text he is not said to be entered by Satan "
 "(Tertullian, Marc. 5.6.7). Jesus has the Passover prepared and eats it with the apostles: \"I have earnestly desired to "
 "eat this Passover with you before I suffer.\" He gives the bread as his body and the cup as the covenant in his blood "
 "(Tertullian, Marc. 4.40.3–6). He foretells Peter's denial, prays kneeling a stone's throw from the disciples, and is "
 "betrayed with a kiss. He is seized and led to the high priest's house, where Peter denies him three times, and the "
 "Lord turns and looks at Peter (22:54–62, printed as restored by method; see the notes). He is mocked and beaten, and before the council says that from now on the son of man will be "
 "seated at the right hand of the power of God. Epiphanius states that the text lacked the saying about not eating the "
 "Passover again until the kingdom (22:16), the purse and the swords with \"he was counted among the lawless\" "
 "(22:35–38), and the servant's ear (22:50–51)."
)

NOTES = [
 dict(term='Judas without Satan (22:1–6)', cat='textual', refs=['22:1', '22:3', '22:4', '22:5'], text=(
  "Tertullian, Marc. 4.40.1–2: of all the Jewish feasts Jesus chose the day of the Passover; he could have been betrayed by "
  "a stranger and without a price, but was betrayed by one who ate bread with him, and for money, as the prophets said. In "
  "book 5 (5.6.7) Tertullian writes that \"in my text\" Satan entered Judas, against what holds \"according to Marcion\". The "
  "words \"Satan entered into\" (22:3) are therefore not printed, and the rest of the verse is put in the nominative. "
  "Epiphanius quotes 22:4 (sch. 60) with the order \"how he might hand him over to them\", which is printed.")),
 dict(term='The Passover meal (22:7–20)', cat='textual', refs=['22:8', '22:14', '22:15', '22:17', '22:18', '22:19', '22:20'], text=(
  "Epiphanius quotes the sending of the disciples to prepare the Passover (sch. 61) and Jesus reclining with \"the twelve "
  "apostles\" (sch. 62). Both witnesses quote \"I have earnestly desired to eat this Passover with you before I suffer\" "
  "(Tertullian 4.40.1; sch. 62). Epiphanius states that \"I will not eat it until it is fulfilled in the kingdom of God\" "
  "(22:16) was not in the text (sch. 63). Tertullian (4.40.3–6) argues from the bread, \"this is my body\", and from the cup, "
  "\"establishing the covenant sealed in his blood\", that the body was real flesh. 22:17–18 are not cited and are printed "
  "in grey.")),
 dict(term='The long text of the Supper (22:19–20)', cat='textual', refs=['22:19', '22:20'], text=(
  "22:19b–20 (\"which is given for you… the new covenant in my blood, which is poured out for you\") are absent from D and "
  "part of the Old Latin, and Westcott and Hort counted them among the Western non-interpolations. Tertullian's allusion to "
  "the cup and the covenant in Jesus' blood (4.40.4) shows that the text he read had at least 22:20 in some form, and his "
  "\"then he should have handed over bread for us\" points to \"given for you\". The second-century text attested here "
  "therefore stands with the long text, not with D (Roth, 259 n. 390). Both verses are printed as NA27 has them; the words "
  "the witness does not cite are noted.")),
 dict(term='Not printed: 22:16, 22:24–30, 22:35–38', cat='excision', refs=['22:15', '22:23', '22:34'], text=(
  "22:16 is absent by Epiphanius' statement (sch. 63). 22:24–30, the dispute about greatness and the twelve thrones, form a "
  "paragraph with no attested verse; Epiphanius' \"or he cut these out again\" (elenchus 63) suggests that 22:30 was not in the "
  "text. 22:35–38, the purse, the bag and the two swords with \"he was counted among the lawless\" (Isa 53:12), are absent "
  "by Epiphanius' statement (sch. 64).")),
 dict(term='Gethsemane and the arrest (22:39–53)', cat='textual', refs=['22:41', '22:47', '22:48'], text=(
  "Epiphanius quotes \"he withdrew from them about a stone's throw and knelt down and prayed\" (sch. 65) and argues from the "
  "kneeling that Jesus had a body. 22:43–44, the angel from heaven and the sweat like drops of blood, are printed by NA27 "
  "in double brackets as not part of its text, and no witness cites them for this text; they are not printed. Judas draws "
  "near to kiss Jesus (sch. 66), and Tertullian notes that he was to be betrayed \"with a kiss\" (4.41.2). Epiphanius states "
  "that the cutting off of the servant's ear and its healing were not in the text (sch. 67); 22:49, which asks whether to "
  "strike with the sword, depends on the absent swords (22:38) and the absent blow and is not printed. 22:52–53 forms a "
  "paragraph with no attested verse and is not printed; the correspondential reading tested it and it closes no gap.")),
 dict(term='Restored by method: Peter\'s denial (22:54–62)', cat='textual', refs=['22:34', '22:54', '22:61', '22:62', '22:63', '22:66'], text=(
  "No witness cites Peter's denial in the high priest's courtyard; it forms a paragraph with no attested verse, and its "
  "absence is undetermined (U?). The prediction (22:34) is attested (Tertullian, Marc. 4.41.2). The passage is printed as "
  "restored by method (METHOD §11). By its words, the printed text needs it: 22:63, \"the men holding him (οἱ συνέχοντες "
  "αὐτόν)\", presupposes that someone has taken hold of him, and in the printed text no one has (22:48 ends with the kiss); the "
  "seizing and the leading into the high priest's house are 22:54. 22:66, \"as it became day\", follows a night the printed "
  "text does not otherwise tell. By its mechanics: the printed text sets up faith's failure and return three times — \"when once "
  "you have turned back, strengthen your brothers\" (22:32), \"I am ready to go with you to prison and to death\" (22:33), \"you "
  "will deny three times\" (22:34) — and without this passage never shows them. Here faith fails; the Lord turns and looks; "
  "Peter remembers his word, goes outside and weeps. The reading is in docs/research/correspondence/word_by_word.md (chapter 20, "
  "test of 22:54–62). The Greek is NA27, checked on the page image (p. 236); at 22:61 NA27 reads ῥήματος (SBLGNT λόγου).")),
 dict(term='Mockery and council (22:63–71)', cat='textual', refs=['22:63', '22:64', '22:66', '22:67', '22:69', '22:70', '22:71'], text=(
  "Epiphanius quotes the mockery, the beating and \"Prophesy, who is it that struck you?\" (sch. 68), as proof of a body that "
  "could be struck. Tertullian (4.41.3–5) follows the council: asked whether he is the Christ, Jesus answers \"if I tell you, "
  "you will not believe\"; \"from now on the son of man shall be seated at the right hand of the power of God\" (Dan 7:13; "
  "Ps 110:1); asked \"are you the Son of God?\", he answers \"you say\", which Tertullian takes as an affirmation.")),
 dict(term='The betrayer and the meal', cat='theological', refs=['22:3', '22:15', '22:19', '22:20'], text=(
  "Interpretation. Without \"Satan entered into Judas\", the betrayal in this text is the act of one of the twelve, done for "
  "money, and the \"woe\" of 22:22 falls on him; Tertullian (4.41.1) argues from that \"woe\" that the God of this Jesus "
  "judges. The meal is a Passover that Jesus has \"earnestly desired\" to eat. In the attested text he gives the bread as his "
  "body and the cup as the covenant in his blood. Which canonical words go beyond what the witness cites (\"do this in "
  "remembrance of me\", \"poured out for you\") is recorded verse by verse; the verse-level evidence does not support "
  "reading this text as a fellowship meal without the cup of the covenant.")),
]
