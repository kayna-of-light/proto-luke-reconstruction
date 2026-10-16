"""Batch 6, chapter 20 of the reconstruction: Luke 22:1–71."""
from buildlib import greek
from batch1_ch2 import U, A
from batch6_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}

T402 = T('4.40.2', '"Poterat et ab extraneo quolibet tradi: ne dicerem et in hoc psalmum expunctum: Qui mecum panem edit, levabit in me plantam. Poterat et sine praemio tradi."')
T403 = T('4.40.3', '"acceptum panem et distributum discipulis corpus suum illum fecit, Hoc est corpus meum dicendo, id est figura corporis mei… Aut si propterea panem corpus sibi finxit quia corporis carebat veritate, ergo panem debuit tradere pro nobis."')
T412 = T('4.41.2', '"Nam et Petrum praesumptorie aliquid elocutum negationi potius destinando, zeloten deum tibi ostendit. Debuit etiam osculo tradi…"')

ENTRIES = [
 A('22:1', G('22:1'), 'And the feast of the unleavened loaves, which is called Passover, was drawing near.',
   'present (Marc. 4.40.1)', [T('4.40.1', '"Nam ex tot festis Iudaeorum paschae diem elegit."')],
   wording='NA27. Tertullian attests only "Passover".'),
 U('22:2', G('22:2'), 'And the high priests and the scribes were seeking how they might do away with him, for they were afraid of the people.', 'Inside the attested paragraph 22:1–2.'),
 A('22:3', greek('22:3', text='Ἰούδας δὲ ὁ καλούμενος Ἰσκαριώτης, ὢν ἐκ τοῦ ἀριθμοῦ τῶν δώδεκα,'),
   'And Judas, the one called Iscariot, being of the number of the twelve,',
   'present (Marc. 4.40.2); "Satan entered into" not present (Marc. 5.6.7)',
   [T402, T('5.6.7', '"Scriptum est enim apud me satanam in Iudam introisse. Secundum autem Marcionem…"')],
   wording=('NA27 without "Satan entered into" (Εἰσῆλθεν δὲ Σατανᾶς εἰς). Tertullian writes that "in my text" (apud me) Satan entered Judas, and sets this against "according to Marcion"; Roth: "was not present". '
            'What the verse had in their place is not attested. The remaining words are printed in the nominative, so that the sentence runs on into 22:4; the case is an editorial adjustment, not an attested wording. '
            'Tertullian\'s "he could have been betrayed by any stranger" and Ps 41:9 ("he who eats bread with me") refer to Judas as one of the Twelve (Roth: wording possible only).')),
 A('22:4', G('22:4', [('τὸ πῶς αὐτοῖς παραδῷ αὐτόν.', 'τὸ πῶς αὐτὸν παραδῷ αὐτοῖς.')]),
   'went away and talked with the high priests and officers about how he might hand him over to them.',
   'present (Pan. 42.11.6, sch. 60; Marc. 4.40.2)',
   [E(60, '»συνελάλησε τοῖς στρατηγοῖς τὸ πῶς αὐτὸν παραδῷ αὐτοῖς«.'), T402],
   wording=('Marcionite word order adopted: τὸ πῶς αὐτὸν παραδῷ αὐτοῖς (NA27 αὐτοῖς παραδῷ αὐτόν). Epiphanius quotes it so in both listings; Roth: very likely, "the word order found in many manuscripts". '
            'Epiphanius has only "the officers"; whether the chief priests were named is unattested (Roth), and NA27 is printed. NA27 notes D it sys.c without "and officers".')),
 A('22:5', G('22:5'), 'And they rejoiced, and agreed to give him silver.',
   'present (Marc. 4.40.2)', [T402], wording='NA27. Tertullian attests the payment ("sine praemio"); Roth: ἀργύριον.'),
 U('22:6', G('22:6'), 'And he consented, and he was seeking a good opportunity to hand him over to them without a crowd.', 'Inside the attested paragraph 22:3–6.'),
 U('22:7', G('22:7'), 'And the day of the unleavened loaves came, on which the Passover had to be sacrificed;', 'Opens the attested paragraph 22:7–13. NA27 [ἐν] (SBLGNT without it).'),
 A('22:8', G('22:8'), 'and he sent Peter and John, saying, "Journey and make ready the Passover for us, so that we may eat."',
   'present (Pan. 42.11.6, sch. 61)', [E(61, '»καὶ εἶπεν τῷ Πέτρῳ καὶ τοῖς λοιποῖς· ἀπελθόντες ἑτοιμάσατε ἵνα φάγωμεν τὸ Πάσχα«.')],
   wording=('NA27. Epiphanius\' wording ("he said to Peter and the rest: go and prepare, that we may eat the Passover") is his own, with no support in the manuscripts; Roth: possible only. '
            'His point (elenchus 61) is that Jesus had the Passover prepared for himself.')),
 U('22:9', G('22:9'), 'And they said to him, "Where do you want us to make ready?"', 'Inside the attested paragraph 22:7–13.'),
 U('22:10', G('22:10'), 'And he said to them, "Look, when you have gone into the city, a person carrying a jar of water will meet you; follow him into the house which he goes into.', 'Inside the attested paragraph 22:7–13.'),
 U('22:11', G('22:11'), "And you will say to the master of the house, 'The teacher says to you: Where is the guest room, where I may eat the Passover with my learners?'", 'Inside the attested paragraph 22:7–13.'),
 U('22:12', G('22:12'), 'And that one will show you a large upper room, spread out; make ready there."', 'Inside the attested paragraph 22:7–13.'),
 U('22:13', G('22:13'), 'And going away, they found it just as he had told them, and they made ready the Passover.', 'Inside the attested paragraph 22:7–13.'),
 A('22:14', G('22:14'), 'And when the hour came, he reclined at table, and the emissaries with him.',
   'present (Pan. 42.11.6, sch. 62)', [E(62, '»καὶ ἀνέπεσε καὶ οἱ δώδεκα ἀπόστολοι σὺν αὐτῷ«.')],
   wording=('NA27. Epiphanius has "the twelve emissaries" (NA27: δώδεκα ἀπόστ. ℵ2 A C W Θ Ψ f1.13 𝔐 …; McionE), as Matt 26:20; Roth: δώδεκα probable only, since Epiphanius may follow Matthew. Not adopted. '
            'He does not quote "when the hour came"; Roth: unattested, not absent.')),
 A('22:15', G('22:15'), 'And he said to them, "With longing I have longed to eat this Passover with you before I suffer."',
   'present (Marc. 4.40.1, 3; Pan. 42.11.6, sch. 62)',
   [T('4.40.1', '"Ideo et affectum suum ostendit: Concupiscentia concupivi pascha edere vobiscum, antequam patiar."'),
    E(62, '»καὶ εἶπεν· ἐπιθυμίᾳ ἐπεθύμησα τοῦτο τὸ Πάσχα φαγεῖν μεθ\' ὑμῶν πρὸ τοῦ με παθεῖν«.')],
   wording='NA27. The two witnesses agree with NA27 except that Tertullian lacks "this" and Epiphanius "to them"; Roth treats both as the citers\' omissions. Roth also lists Eznik, De Deo 415 (not checked here).'),
 U('22:17', G('22:17'), 'And receiving a cup, having given thanks, he said, "Take this and divide it among yourselves;',
   'Inside the attested paragraph 22:14–20. Roth lists Adam. 108,27 ("taking bread and cup and blessing"); those words are spoken by Adamantius, the orthodox speaker, and are not evidence for Marcion\'s text.'),
 U('22:18', G('22:18'), 'for I tell you that from now on I will not drink at all of the produce of the vine until the kingdom of God comes."',
   'Inside the attested paragraph 22:14–20. Epiphanius says that 22:16 was absent; he says nothing of 22:18 (Roth, citing Schmid). NA27 [ὅτι] (SBLGNT without it).'),
 A('22:19', G('22:19'), 'And taking a loaf, having given thanks, he broke it and gave it to them, saying, "This is my body, which is given for you. Do this for my remembrance."',
   'present (Marc. 4.40.3, 4)', [T403, T('4.40.4', '"corpus suum vocans panem".')],
   wording=('NA27 (19b–20 printed without brackets, as in NA27). Tertullian attests "he took bread", "gave" and "this is my body"; Roth: very likely. His "then he should have handed over bread for us" alludes to "which is given for you" (Roth: possible). '
            '"Do this in remembrance of me" is unattested.'),
   western='19b–20 are a Western non-interpolation: D and part of the Old Latin end the verse at "my body". This text, attested by Tertullian, had at least part of 19b and 20.'),
 A('22:20', G('22:20'), 'And the cup likewise after they had eaten, saying, "This cup is the new covenant in my blood, which is poured out for you.',
   'present (Marc. 4.40.4, 6)',
   [T('4.40.4', '"Sic et in calicis mentione testamentum constituens sanguine suo obsignatum, substantiam corporis confirmavit."'),
    T('4.40.6', '"Ita et nunc sanguinem suum in vino consecravit, qui tunc vinum in sanguine figuravit."')],
   wording=('NA27. Tertullian attests the cup, the covenant and "my blood"; Roth: probable. Harnack removed "new" on Tertullian\'s silence; Roth: not certain, since Tertullian also adds "sealed". "Which is poured out for you" is unattested. '
            'The previous version omitted this verse as a Western non-interpolation; it is attested for this text.'),
   western='Omitted in D and part of the Old Latin (Western non-interpolation); see 22:19.'),
 U('22:21', G('22:21'), 'But look, the hand of the one who is handing me over is with me on the table;', 'Inside the attested paragraph 22:21–23.'),
 A('22:22', G('22:22'), 'because the son of the human journeys according to what has been fixed; but woe to that human through whom he is handed over."',
   'present for 22:22b (Marc. 4.41.1); 22:22a unattested', [T('4.41.1', '"Vae, ait, per quem traditur filius hominis."')],
   wording='NA27. Tertullian quotes "woe… by whom the son of the human is betrayed"; his "son of the human" may be his own clarification (Roth). Tsutsui\'s view that "as it has been determined" was removed rests on silence and is not adopted.'),
 U('22:23', G('22:23'), 'And they began to question among themselves which of them it might be who was about to do this.', 'Inside the attested paragraph 22:21–23.'),
 U('22:31', G('22:31'), '"Simon, Simon, look, Satan has asked to have you, to sift you like the wheat;', 'Inside the attested paragraph 22:31–34.'),
 U('22:32', G('22:32'), 'but I have begged for you, that your trust may not give out; and you, when once you have turned back, make your brothers firm."', 'Inside the attested paragraph 22:31–34.'),
 A('22:33', G('22:33'), 'And he said to him, "Lord, with you I am ready to journey both into prison and into death."',
   'present (Marc. 4.41.2)', [T412], wording='NA27. Roth: attested, but no insight into the wording.'),
 A('22:34', G('22:34'), 'But he said, "I tell you, Peter, a rooster will not crow today until you have disowned three times that you know me."',
   'present (Marc. 4.41.2)', [T412], wording='NA27. Tertullian attests the denial (ἀπαρνήσῃ).'),
 U('22:39', G('22:39'), 'And going out, he journeyed according to his custom to the Mountain of Olives; and the learners also followed him.', 'Opens the attested paragraph 22:39–46.'),
 U('22:40', G('22:40'), 'And when he was at the place, he said to them, "Pray that you do not come into testing."', 'Inside the attested paragraph 22:39–46.'),
 A('22:41', G('22:41'), "And he himself was drawn away from them about a stone's throw, and kneeling down he was praying,",
   'present (Pan. 42.11.6, sch. 65)', [E(65, '»ἀπεσπάσθη ἀπ\' αὐτῶν ὡσεὶ λίθου βολὴν καὶ θεὶς τὰ γόνατα προσηύχετο«.')],
   wording='NA27. Epiphanius\' quotation agrees with NA27; Roth: secure. His point is the visible kneeling of a body (elenchus 65).'),
 U('22:42', G('22:42'), 'saying, "Father, if you wish, take this cup away from me; yet not my will but yours be done."', 'Inside the attested paragraph 22:39–46.'),
 U('22:45', G('22:45'), 'And standing up from prayer, coming to the learners, he found them sleeping from grief,', 'Inside the attested paragraph 22:39–46.'),
 U('22:46', G('22:46'), 'and he said to them, "Why are you sleeping? Stand up and pray, so that you do not come into testing."', 'Inside the attested paragraph 22:39–46.'),
 A('22:47', G('22:47'), 'While he was still speaking, look, a crowd, and the one called Judas, one of the twelve, was going ahead of them, and he drew near to Jesus to kiss him.',
   'present (Pan. 42.11.6, sch. 66)', [E(66, '»καὶ ἤγγισε καταφιλῆσαι αὐτὸν Ἰούδας καὶ εἶπεν«.')],
   wording='NA27. Epiphanius\' καταφιλῆσαι and "and said" have no manuscript support in Luke and follow Matt 26:49 (Roth). Not adopted. His point is that Judas kissed real lips (elenchus 66).'),
 A('22:48', G('22:48'), 'But Jesus said to him, "Judas, with a kiss do you hand over the son of the human?"',
   'present (Marc. 4.41.2)', [T412], wording='NA27. Tertullian attests the kiss and the betrayal.'),
 A('22:63', G('22:63'), 'And the men who were holding him were mocking him, beating him,',
   'present (Pan. 42.11.6, sch. 68)', [E(68, '»οἱ συνέχοντες ἐνέπαιζον δέροντες καὶ τύπτοντες καὶ λέγοντες· προφήτευσον, τίς ἐστιν ὁ παίσας σε;«')],
   wording='NA27. Epiphanius abbreviates; the elements he quotes agree with NA27 (Roth: very likely).'),
 A('22:64', G('22:64'), 'and having covered him over, they were asking him, saying, "Prophesy: who is it who struck you?"',
   'present (Pan. 42.11.6, sch. 68)', [E(68, '»… τύπτοντες καὶ λέγοντες· προφήτευσον, τίς ἐστιν ὁ παίσας σε;«')],
   wording='NA27. Epiphanius\' "striking" agrees with A W Θ Ψ 𝔐 (ἔτυπτον αὐτοῦ τὸ πρόσωπον); Roth: possible only. Not adopted.'),
 U('22:65', G('22:65'), 'And they were saying many other things against him, blaspheming.', 'Inside the attested paragraph 22:63–65.'),
 A('22:66', G('22:66'), 'And when it became day, the council of elders of the people was gathered together, both high priests and scribes, and they led him away into their sanhedrin,',
   'present (Marc. 4.41.3)', [T('4.41.3', '"Perductus in consessum an ipse esset Christus interrogatur."')]),
 A('22:67', G('22:67'), 'saying, "If you are the Anointed One, tell us." But he said to them, "If I tell you, you will not trust at all;',
   'present (Marc. 4.41.3)', [T('4.41.3', '"Si dixero, enim inquit, vobis non credetis."')],
   wording='NA27. Tertullian\'s "interrogatur" may reflect the question form of D d ("Are you the Christ?"); Roth: undecided. The order "tell you" is uncertain (Roth).'),
 U('22:68', G('22:68'), 'and if I ask, you will not answer at all.', 'Inside the attested paragraph 22:66–71.'),
 A('22:69', G('22:69'), 'But from now on the son of the human will be seated at the right hand of the power of God."',
   'present (Marc. 4.41.4)', [T('4.41.4', '"Abhinc, inquit, erit filius hominis sedens ad dexteram virtutis dei."')],
   wording='NA27. Tertullian quotes the verse; Roth: secure, with δέ possibly present.'),
 A('22:70', G('22:70'), 'And they all said, "Are you then the son of God?" And he said to them, "You say that I am."',
   'present (Marc. 4.41.4–5)', [T('4.41.4', '"Ergo, inquiunt, tu dei filius es?… Sed respondit, Vos dicitis, quasi non ego."'),
                                T('4.41.5', '"Atquin confirmavit id se esse quod illi dixerant…"')],
   wording='NA27. Tertullian argues that "you say" was an affirmation.'),
 A('22:71', G('22:71'), 'And they said, "What further need do we have of testimony? For we ourselves have heard it from his mouth."',
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
      reason=('The messenger from heaven and the sweat like drops of blood. NA27 prints the verses in double brackets, as not part of its text: they are absent from 𝔓75 ℵ1 A B N T W 579 and others, present in ℵ*,2 D L Θ Ψ 0171 f1 𝔐 and known to Justin, Irenaeus and Hippolytus. '
              'No witness cites them for this text. They are not in the NA27 base and are not printed.'))),
 dict(ref='22:49', cls='U−', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='"Lord, shall we strike with the sword?" The swords of 22:38 are absent (sch. 64), and the blow that answers the question (22:50–51) is absent (sch. 67). The verse depends on both.')),
 dict(ref='22:50–51', cls='A−', app=dict(roth='absent', witnesses=[
      E(67, 'παρέκοψεν ὃ ἐποίησε Πέτρος, ὅτε ἐπάταξε καὶ ἀφείλετο τὸ οὖς τοῦ δούλου τοῦ ἀρχιερέως.')],
      decision='not printed', reason='Epiphanius states that the text lacked the cutting off of the slave\'s ear; his elenchus adds that the Lord healed it, so 22:51 was also absent (Roth). Tertullian passes from the kiss (22:48) to the council (22:66; 4.41.2–3).')),
 dict(ref='22:52–53', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='"Have you come out as against a robber…?" A separate NA27 paragraph with no attested verse.')),
 dict(ref='22:54–62', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='Peter\'s denial in the high priest\'s courtyard: a paragraph with no attested verse. The prediction of the denial (22:34) is attested; its fulfilment is not cited by either witness.')),
]

PREAMBLE = (
 "The feast of unleavened bread is near, the night of leaving bondage, and something from within the circle of "
 "our own powers goes off to agree a price.\n\n"
 "At the table, truth gives itself away in the plainest things there are. Bread is broken and handed round: this"
 " is my body, given for you. A cup is passed: the new covenant. It has longed to eat this meal.\n\n"
 "The boldest part of us swears it is ready for prison and for death, and is told that before the cock crows it "
 "will have said three times that it does not know truth at all.\n\n"
 "A stone's throw away, alone, truth kneels and prays. Then the one from the table comes forward with a crowd "
 "and greets it with a kiss.\n\n"
 "When day comes, the highest authority in us sits in judgement. Are you the Anointed One? If I tell you, you "
 "will not trust. Are you the son of God, then?\n\n"
 "You say that I am."
)

NOTES = [
 dict(term='Judas without Satan (22:1–6)', cat='textual', refs=['22:1', '22:3', '22:4', '22:5'], text=(
  "Tertullian, Marc. 4.40.1–2: of all the Jewish feasts Jesus chose the day of the Passover; he could have been betrayed by "
  "a stranger and without a price, but was betrayed by one who ate bread with him, and for money, as the prophets said. In "
  "book 5 (5.6.7) Tertullian writes that \"in my text\" Satan entered Judas, against what holds \"according to Marcion\". The "
  "words \"Satan entered into\" (22:3) are therefore not printed, and the rest of the verse is put in the nominative. "
  "Epiphanius quotes 22:4 (sch. 60) with the order \"how he might hand him over to them\", which is printed.")),
 dict(term='The Passover meal (22:7–20)', cat='textual', refs=['22:8', '22:14', '22:15', '22:17', '22:18', '22:19', '22:20'], text=(
  "Epiphanius quotes the sending of the learners to prepare the Passover (sch. 61) and Jesus reclining with \"the twelve "
  "emissaries\" (sch. 62). Both witnesses quote \"With longing I have longed to eat this Passover with you before I suffer\" "
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
  "Epiphanius quotes \"he was drawn away from them about a stone's throw, and kneeling down he was praying\" (sch. 65) and argues from the "
  "kneeling that Jesus had a body. 22:43–44, the messenger from heaven and the sweat like drops of blood, are printed by NA27 "
  "in double brackets as not part of its text, and no witness cites them for this text; they are not printed. Judas draws "
  "near to kiss Jesus (sch. 66), and Tertullian notes that he was to be betrayed \"with a kiss\" (4.41.2). Epiphanius states "
  "that the cutting off of the slave's ear and its healing were not in the text (sch. 67); 22:49, which asks whether to "
  "strike with the sword, depends on the absent swords (22:38) and the absent blow and is not printed. 22:52–53 and Peter's "
  "denial (22:54–62) form paragraphs with no attested verse.")),
 dict(term='Mockery and council (22:63–71)', cat='textual', refs=['22:63', '22:64', '22:66', '22:67', '22:69', '22:70', '22:71'], text=(
  "Epiphanius quotes the mockery, the beating and \"Prophesy: who is it who struck you?\" (sch. 68), as proof of a body that "
  "could be struck. Tertullian (4.41.3–5) follows the council: asked whether he is the Christ, Jesus answers \"if I tell you, "
  "you will not trust at all\"; \"from now on the son of the human will be seated at the right hand of the power of God\" (Dan 7:13; "
  "Ps 110:1); asked \"are you then the son of God?\", he answers \"you say\", which Tertullian takes as an affirmation.")),
 dict(term='The betrayer and the meal', cat='theological', refs=['22:3', '22:15', '22:19', '22:20'], text=(
  "Interpretation. Without \"Satan entered into Judas\", the betrayal in this text is the act of one of the twelve, done for "
  "money, and the \"woe\" of 22:22 falls on him; Tertullian (4.41.1) argues from that \"woe\" that the God of this Jesus "
  "judges. The meal is a Passover that Jesus has \"longed with longing\" to eat. In the attested text he gives the bread as his "
  "body and the cup as the covenant in his blood. Which canonical words go beyond what the witness cites (\"do this in "
  "remembrance of me\", \"poured out for you\") is recorded verse by verse; the verse-level evidence does not support "
  "reading this text as a fellowship meal without the cup of the covenant.")),
 dict(term='ἡ ἑορτὴ τῶν ἀζύμων, "the feast of the unleavened loaves"', cat='translation', refs=['22:1'], text='τὰ ἄζυμα, the unleavened breads.'),
 dict(term='Πάσχα, "Passover"', cat='translation', refs=['22:1'], text='Πάσχα is the Aramaic pasḥa, Hebrew pesach. It is used for both the feast and the lamb (22:7).'),
 dict(term='ἀνέλωσιν, "do away with"', cat='translation', refs=['22:2'], text='ἀναιρέω, to take away, kill.'),
 dict(term='Ἰούδας… ὢν ἐκ τοῦ ἀριθμοῦ τῶν δώδεκα, "and Judas… being of the number of the twelve"', cat='translation', refs=['22:3'], text='This text lacks "Satan entered into Judas". The sentence runs straight on into 22:4.'),
 dict(term='Ἰσκαριώτης, "Iscariot"', cat='translation', refs=['22:3'], text='The form here differs from Ἰσκαριώθ at 6:16.'),
 dict(term='στρατηγοῖς, "officers"', cat='translation', refs=['22:4'], text='The commanders of the temple guard.'),
 dict(term='αὐτὸν παραδῷ αὐτοῖς, "hand him over to them"', cat='translation', refs=['22:4'], text='The reading of this text. παραδίδωμι, as at 9:44: "betray" is one use; the word says "hand over".'),
 dict(term='ἀργύριον, "silver"', cat='translation', refs=['22:5'], text='Money, as at 9:3.'),
 dict(term='ἐξωμολόγησεν, "he consented"', cat='translation', refs=['22:6'], text='To agree, promise.'),
 dict(term='εὐκαιρίαν, "a good opportunity"', cat='translation', refs=['22:6'], text='A fitting moment.'),
 dict(term='ἔδει θύεσθαι τὸ πάσχα, "the Passover had to be sacrificed"', cat='translation', refs=['22:7'], text='Here τὸ πάσχα is the lamb. δεῖ, as at 4:43.'),
 dict(term='κεράμιον, "a jar"', cat='translation', refs=['22:10'], text='A clay jar.'),
 dict(term='τῷ οἰκοδεσπότῃ, "the master of the house"', cat='translation', refs=['22:11'], text='As at 12:39.'),
 dict(term='τὸ κατάλυμα, "the guest room"', cat='translation', refs=['22:11'], text='A place to lodge.'),
 dict(term='ἀνάγαιον… ἐστρωμένον, "an upper room… spread out"', cat='translation', refs=['22:12'], text='A room above the ground floor, furnished with couches.'),
 dict(term='ἀνέπεσεν, "he reclined at table"', cat='translation', refs=['22:14'], text='As at 11:37.'),
 dict(term='οἱ ἀπόστολοι, "the emissaries"', cat='translation', refs=['22:14'], text='As at 6:13.'),
 dict(term='Ἐπιθυμίᾳ ἐπεθύμησα, "with longing I have longed"', cat='translation', refs=['22:15'], text='A Hebrew way of strengthening a verb by its own noun.'),
 dict(term='πρὸ τοῦ με παθεῖν, "before I suffer"', cat='translation', refs=['22:15'], text='πάσχω, to suffer.'),
 dict(term='εὐχαριστήσας, "having given thanks"', cat='translation', refs=['22:17'], text='εὐχαριστέω, as at 10:21.'),
 dict(term='τοῦ γενήματος τῆς ἀμπέλου, "the produce of the vine"', cat='translation', refs=['22:18'], text='What the vine yields.'),
 dict(term='ἄρτον, "a loaf"', cat='translation', refs=['22:19'], text='Without the article.'),
 dict(term='ὑπὲρ ὑμῶν, "for you"', cat='translation', refs=['22:19'], text='On your behalf.'),
 dict(term='εἰς τὴν ἐμὴν ἀνάμνησιν, "for my remembrance"', cat='translation', refs=['22:19'], text='ἀνάμνησις, a calling to mind. The Greek has the possessive adjective, "my remembrance".'),
 dict(term='ἡ καινὴ διαθήκη, "the new covenant"', cat='translation', refs=['22:20'], text='καινός, as at 5:36. διαθήκη is a covenant or a will.'),
 dict(term='ἐκχυννόμενον, "poured out"', cat='translation', refs=['22:20'], text='The present tense: "which is being poured out". It is the verb of the young wine poured out (5:37).'),
 dict(term='τοῦ παραδιδόντος με, "the one who is handing me over"', cat='translation', refs=['22:21'], text='A present participle.'),
 dict(term='κατὰ τὸ ὡρισμένον, "according to what has been fixed"', cat='translation', refs=['22:22'], text='ὁρίζω, to mark out a boundary, determine.'),
 dict(term='πορεύεται, "journeys"', cat='translation', refs=['22:22'], text='The road verb, as at 4:30 and 9:51.'),
 dict(term='συζητεῖν, "to question"', cat='translation', refs=['22:23'], text='To discuss, dispute together.'),
 dict(term='ὁ Σατανᾶς, "Satan"', cat='translation', refs=['22:31'], text='As at 11:18.'),
 dict(term='ἐξῃτήσατο ὑμᾶς, "has asked to have you"', cat='translation', refs=['22:31'], text='To ask for and obtain, to demand for oneself. "You" is plural: all of them.'),
 dict(term='σινιάσαι, "to sift"', cat='translation', refs=['22:31'], text='To shake in a sieve.'),
 dict(term='περὶ σοῦ… ἡ πίστις σου, "for you… your trust"', cat='translation', refs=['22:32'], text='Singular: Simon alone.'),
 dict(term='ἐκλίπῃ, "give out"', cat='translation', refs=['22:32'], text='As at 16:9.'),
 dict(term='ἐπιστρέψας, "when you have turned back"', cat='translation', refs=['22:32'], text='ἐπιστρέφω, as at 17:4.'),
 dict(term='στήρισον, "make firm"', cat='translation', refs=['22:32'], text='στηρίζω, as at 9:51.'),
 dict(term='ἀπαρνήσῃ, "you have disowned"', cat='translation', refs=['22:34'], text='ἀρνέομαι, as at 9:23 and 12:9.'),
 dict(term='κατὰ τὸ ἔθος, "according to his custom"', cat='translation', refs=['22:39'], text='As was his habit.'),
 dict(term='εἰς πειρασμόν, "into testing"', cat='translation', refs=['22:40'], text='As at 11:4.'),
 dict(term='ἀπεσπάσθη, "was drawn away"', cat='translation', refs=['22:41'], text='A passive: to be drawn off, to withdraw.'),
 dict(term='θεὶς τὰ γόνατα, "kneeling down"', cat='translation', refs=['22:41'], text='Literally "placing the knees".'),
 dict(term='Πάτερ, "Father"', cat='translation', refs=['22:42'], text='As at 11:2.'),
 dict(term='εἰ βούλει, "if you wish"', cat='translation', refs=['22:42'], text='βούλομαι, to will, decide, as at 10:22.'),
 dict(term='παρένεγκε, "take… away"', cat='translation', refs=['22:42'], text='To carry past, remove.'),
 dict(term='τὸ θέλημά μου… τὸ σόν, "my will… yours"', cat='translation', refs=['22:42'], text='θέλημα, what one wills, as at 12:47.'),
 dict(term='ἀναστάς, "standing up"', cat='translation', refs=['22:45'], text='ἀνίστημι.'),
 dict(term='ἀπὸ τῆς λύπης, "from grief"', cat='translation', refs=['22:45'], text='λύπη, sorrow, pain.'),
 dict(term='ἀναστάντες, "stand up"', cat='translation', refs=['22:46'], text='ἀνίστημι again.'),
 dict(term='προήρχετο, "was going ahead"', cat='translation', refs=['22:47'], text='To go before, lead.'),
 dict(term='φιλῆσαι, "to kiss"', cat='translation', refs=['22:47'], text='φιλέω, to kiss, to love as a friend.'),
 dict(term='φιλήματι… παραδίδως, "with a kiss do you hand over"', cat='translation', refs=['22:48'], text='παραδίδωμι, as at 9:44.'),
 dict(term='οἱ ἄνδρες οἱ συνέχοντες αὐτόν, "the men who were holding him"', cat='translation', refs=['22:63'], text='συνέχω, to hold fast, as at 8:45.'),
 dict(term='ἐνέπαιζον… δέροντες, "were mocking… beating"', cat='translation', refs=['22:63'], text='ἐμπαίζω, to make fun of, as of a child; δέρω, to beat, as at 12:47.'),
 dict(term='περικαλύψαντες, "having covered him over"', cat='translation', refs=['22:64'], text='Blindfolded.'),
 dict(term='Προφήτευσον, "prophesy"', cat='translation', refs=['22:64'], text='To speak as a prophet, here: say who struck you.'),
 dict(term='βλασφημοῦντες, "blaspheming"', cat='translation', refs=['22:65'], text='As at 5:21. The Greek uses the same word for insults against Jesus.'),
 dict(term='τὸ πρεσβυτέριον τοῦ λαοῦ, "the council of elders of the people"', cat='translation', refs=['22:66'], text='The body of elders.'),
 dict(term='τὸ συνέδριον, "sanhedrin"', cat='translation', refs=['22:66'], text='The council; συνέδριον, a sitting together.'),
 dict(term='οὐ μὴ πιστεύσητε, "you will not trust at all"', cat='translation', refs=['22:67'], text='πιστεύω, with the double negative.'),
 dict(term='ἐκ δεξιῶν τῆς δυνάμεως τοῦ θεοῦ, "at the right hand of the power of God"', cat='translation', refs=['22:69'], text='δύναμις, power, as at 6:19 and 9:1.'),
 dict(term='Ὑμεῖς λέγετε ὅτι ἐγώ εἰμι, "you say that I am"', cat='translation', refs=['22:70'], text='The Greek allows "You say it, because I am", or "You are saying that I am". It is neither a plain yes nor a plain no.'),
 dict(term='μαρτυρίας, "testimony"', cat='translation', refs=['22:71'], text='Evidence of witnesses.'),
]
