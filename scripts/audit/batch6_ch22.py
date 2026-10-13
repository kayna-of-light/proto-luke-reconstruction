"""Batch 6, chapter 22 of the reconstruction: Luke 24:1–53 (24:33–35, 24:44–46 and 24:47b–53 restored by method, METHOD §11)."""
from buildlib import greek, R
from batch1_ch2 import U, A
from batch6_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}

T431 = T('4.43.1', '"si nec mulierum illarum officium praeterit prophetia quae ante lucem convenerunt ad sepulcrum cum odorum paratura."')
T432 = T('4.43.2', '"Corpore autem non invento… Sed et duo ibidem angeli apparuerunt… Revertentes quoque a sepulcro mulieres, et ab illa angelorum visione… ad renuntiandam scilicet domini resurrectionem."')
T433 = T('4.43.3', '"Bene autem quod incredulitas discipulorum perseverabat… Nam cum duo ex illis iter agerent et dominus eis adhaesisset, non comparens quod ipse esset, etiam dissimulans de conscientia rei gestae, Nos autem putabamus, inquiunt, ipsum esse redemptorem Israelis…"')
T435 = T('4.43.5', '"Nam eadem et angeli ad mulieres: Rememoramini quae locutus sit vobis in Galilaea, dicens quod oportet tradi filium hominis et crucifigi et tertia die resurgere."')
T436 = T('4.43.6', '"cum haesitantibus eis ne phantasma esset, immo phantasma credentibus, Quid turbati estis? inquit, et quid cogitationes subeunt in corda vestra? Videte manus meas et pedes, quia ego ipse sum, quoniam spiritus ossa non habet, sicut me videtis habere."')
E76 = E(76, '»εἶπαν οἱ ἐν ἐσθῆτι λαμπρᾷ· τί ζητεῖτε τὸν ζῶντα μετὰ τῶν νεκρῶν; ἠγέρθη, μνήσθητε ὅσα ἐλάλησεν ἔτι ὢν μεθ\' ὑμῶν, ὅτι δεῖ τὸν υἱὸν τοῦ ἀνθρώπου παθεῖν καὶ παραδοθῆναι«.')
E77 = E(77, 'παρέκοψε τὸ εἰρημένον πρὸς Κλεόπαν καὶ τὸν ἄλλον, ὅτε συνήντησεν αὐτοῖς, τὸ »ὦ ἀνόητοι καὶ βραδεῖς τοῦ πιστεύειν πᾶσιν, οἷς ἐλάλησαν οἱ προφῆται· οὐχὶ ταῦτα ἔδει παθεῖν;« καὶ ἀντὶ δὲ τοῦ »ἐφ\' οἷς ἐλάλησαν οἱ προφῆται« ἐποίησεν »ἐφ\' οἷς ἐλάλησα ὑμῖν«. ἐλέγχεται δὲ ὅτι »ὅτε ἔκλασε τὸν ἄρτον, ἠνεῴχθησαν αὐτῶν οἱ ὀφθαλμοὶ καὶ ἐπέγνωσαν αὐτόν«.')
E78 = E(78, '»τί τεταραγμένοι ἐστέ; ἴδετε τὰς χεῖράς μου καὶ τοὺς πόδας μου, ὅτι πνεῦμα ὀστέα οὐκ ἔχει, καθὼς ἐμὲ θεωρεῖτε ἔχοντα«.')

CR_24_33 = 'The return to Jerusalem; "The Lord has risen indeed, and has appeared to Simon!" A paragraph with no attested verse (METHOD §4.3).'
GR_24_33 = ('by its words, the printed 24:36 opens "as they were saying these things (ταῦτα δὲ αὐτῶν λαλούντων), he himself stood in their midst", and in the printed '
            'text no one says anything after 24:31; "these things" are what is told in 24:35, and "their midst" is the eleven gathered (24:33). Without it, those who '
            'are terrified and think they see a spirit (24:37) are the two who have just recognized him at the bread. By its mechanics: the road of the text goes to '
            'Jerusalem (9:51); after the cross two go away from it (24:13), and 24:33 brings them back ("rising, they returned to Jerusalem"); 24:34 "he has appeared '
            'to Simon" is the "turning back" of 22:32. Reading: docs/research/correspondence/word_by_word.md, chapter 22, test of 24:32–35.')
CR_24_44 = ('Tertullian passes from the request for food (24:41; 4.43.8) to the sending to the nations (24:47; 4.43.9) and ends his book by claiming that he has shown '
            'Jesus to be the Christ of the prophets; these verses would have been his proof text. Epiphanius does not cite them either.')
GR_24_44 = ('by its words, the printed 24:47 "and that repentance… be proclaimed (καὶ κηρυχθῆναι)" is an infinitive that depends on 24:46 "thus it is written that"; '
            'without it the verse hangs, and the previous text marked the gap with an ellipsis. By its mechanics: the text veils the understanding on purpose (9:45) '
            'and lifts the veil in stages (24:8 remembering; 23:45 the veil of the sanctuary torn; 24:31 the eyes opened at the bread); the opening of the mind to '
            'understand the scriptures is the last stage. And 16:31 sets the condition that rising from the dead persuades only those who hear Moses and the prophets; '
            'in the printed text Moses and the prophets are never opened about rising except here. Reading: docs/research/correspondence/word_by_word.md, chapter 22, test of 24:44–46.')
CR_24_48 = ('No witness cites anything after 24:47, and METHOD §10 ends the text at the last attested verse by default. '
            '24:51b ("and was carried up into heaven") and 24:52a ("worshipped him") are Western non-interpolations (lacking in ℵ* D it sys), printed by NA27 without brackets.')
GR_24_48 = ('by its mechanics, at 9:51 the text names its own end: "the days of his taking up (ἀνάλημψις) were being fulfilled, and he set his face to go to Jerusalem". '
            'In the printed text the taking up is never told; the text stops at the command (24:47), before the end it announced. 24:50–51 is that end: the hands '
            'lifted, the blessing, the parting while he blesses, carried up into heaven; and the disciples return to Jerusalem with joy, to the temple. '
            'Reading: docs/research/correspondence/word_by_word.md, chapter 22, test of 24:48–53. This also departs from the default ending of METHOD §10 (overridden by the owner).')
W33 = lambda ref, en: R(ref, G(ref), en, 'U?', 'unattested', CR_24_33, GR_24_33, wording='NA27 (checked on the page image, p. 244).')
W44 = lambda ref, en, note='': R(ref, G(ref), en, 'U−', 'unattested', CR_24_44, GR_24_44, wording='NA27 (checked on the page image, p. 245).' + note)
W48 = lambda ref, en, page='245', note='': R(ref, G(ref), en, 'U?', 'unattested', CR_24_48, GR_24_48, wording=f'NA27 (checked on the page image, p. {page}).' + note)

ENTRIES = [
 A('24:1', G('24:1'), 'But on the first day of the week, at early dawn, they went to the tomb, taking the spices they had prepared.',
   'present (Marc. 4.43.1)', [T431], wording='NA27. Tertullian\'s "before light" renders ὄρθρου βαθέως (Roth).'),
 U('24:2', G('24:2'), 'And they found the stone rolled away from the tomb,', 'Inside the attested paragraph 24:1–8.'),
 A('24:3', G('24:3'), 'but when they went in they did not find the body of the Lord Jesus.',
   'present (Marc. 4.43.2)', [T432],
   wording='NA27. Tertullian attests "the body was not found". "Of the Lord Jesus" is unattested; his silence does not show it was absent (Roth), and it is printed with NA27.',
   western='"Of the Lord Jesus" is lacking in D and the Old Latin (a Western non-interpolation).'),
 A('24:4', G('24:4'), 'While they were perplexed about this, look, two men stood by them in dazzling clothing.',
   'present (Marc. 4.43.2; Pan. 42.11.6, sch. 76)', [T432, E76],
   wording=('NA27. Tertullian\'s "two angels" names the two men; Epiphanius introduces his quotation with "those in shining clothing" (ἐν ἐσθῆτι λαμπρᾷ). That introduction is his own summary (Roth); "dazzling" (ἀστραπτούσῃ) and "shining" (λαμπρᾷ) are both possible only. Not adopted.')),
 A('24:5', G('24:5'), 'And as they were frightened and bowed their faces to the ground, the men said to them, "Why do you seek the Living One among the dead?',
   'present (Pan. 42.11.6, sch. 76)', [E76], wording='NA27. Epiphanius quotes the question; Roth: secure.'),
 A('24:6', G('24:6', [('οὐκ ἔστιν ὧδε, ἀλλὰ ἠγέρθη. μνήσθητε ὡς ἐλάλησεν', 'ἠγέρθη. μνήσθητε ὅσα ἐλάλησεν')]),
   'He has been raised. Remember all that he told you while he was still in Galilee,',
   'present (Marc. 4.43.5; Pan. 42.11.6, sch. 76)', [T435, E76],
   wording=('Marcionite readings adopted. (1) "Remember all that he told you" (ὅσα, Tertullian "quae", Epiphanius ὅσα) for NA27 "how he told you" (ὡς); NA27: ὅσα D c sys.c; McionT,E; Roth: secure. '
            '(2) "He has been raised" without "He is not here, but". Epiphanius quotes "Why do you seek the Living One among the dead? He has been raised. Remember…" in one run. When he cites the verse in his own words he always writes "He is risen (ἀνέστη), he is not here" (elenchus 76; Pan. 56.2.8): here he writes Luke\'s ἠγέρθη, which he does not use himself, and no "he is not here". NA27 cites McionE for ἠγέρθη alone. Roth judges the omission unattested rather than absent; the citation habit is the basis for the departure. '
            'Tertullian has "to you… in Galilee" and Epiphanius "while he was still"; together they give NA27\'s wording.'),
   western='D and the Old Latin lack the whole of 6a, "he is not here, but he has been raised" (a Western non-interpolation). This text had "he has been raised".'),
 A('24:7', G('24:7'), 'saying that the son of man must be delivered into the hands of sinful men and be crucified and on the third day rise."',
   'present (Marc. 4.43.5; Pan. 42.11.6, sch. 76)', [T435, E76],
   wording=('NA27. Neither witness quotes "into the hands of sinful men". Epiphanius stops after "delivered" and uses Matthew\'s "suffer"; Tertullian\'s quotation is loose in its word order (Roth). The phrase would not have served either argument, so its absence from their quotations does not show that it was absent (Roth: speculative). Printed.')),
 U('24:8', G('24:8'), 'And they remembered his words,', 'Inside the attested paragraph 24:1–8.'),
 A('24:9', G('24:9'), 'and returning from the tomb they told all these things to the eleven and to all the rest.',
   'present (Marc. 4.43.2)', [T432],
   wording='NA27. Tertullian attests "returning from the tomb" and the report; Roth: very likely. The recipients are not named by him ("the disciples" in 4.43.3 refers to their unbelief, 24:11), so NA27 is printed.',
   western='"From the tomb" is lacking in D and the Old Latin; this text had it.'),
 U('24:10', G('24:10'), 'Now it was Mary Magdalene and Joanna and Mary the mother of James and the other women with them who told these things to the apostles,', 'Inside the attested paragraph 24:9–12.'),
 A('24:11', G('24:11'), 'but these words seemed to them an idle tale, and they did not believe them.',
   'present (Marc. 4.43.3)', [T433], wording='NA27. Tertullian attests the persisting unbelief.'),
 A('24:13', G('24:13'), 'That very day two of them were going to a village named Emmaus, about sixty stadia from Jerusalem,',
   'present (Marc. 4.43.3; Pan. 42.11.6, sch. 77)', [T433, E77], wording='NA27. Tertullian: "two of them were travelling" (Roth: δύο ἐξ αὐτῶν secure / very likely).'),
 U('24:14', G('24:14'), 'and they were talking with each other about all these things that had happened.', 'Inside the attested paragraph 24:13–27.'),
 A('24:15', G('24:15'), 'While they were talking and discussing together, Jesus himself drew near and went with them.',
   'present (Marc. 4.43.3; Pan. 42.11.6, sch. 77)', [T433, E77], wording='NA27. "The Lord joined them" (Tertullian); "when he met them" (Epiphanius).'),
 A('24:16', G('24:16'), 'But their eyes were kept from recognizing him.',
   'present (Marc. 4.43.3)', [T433], wording='NA27. Tertullian: "not showing that it was he" (Roth: no insight into the wording).'),
 U('24:17', G('24:17'), 'And he said to them, "What is this conversation that you are holding with each other as you walk?" And they stood still, looking sad.',
   'Inside the attested paragraph 24:13–27. Tertullian\'s "pretending not to know what had happened" may refer to this question or to 24:19 (Roth assigns it to 24:19).'),
 A('24:18', G('24:18'), 'Then one of them, named Cleopas, answered him, "Are you the only visitor to Jerusalem who does not know the things that have happened there in these days?"',
   'present (Pan. 42.11.6, sch. 77)', [E77], wording='NA27. Epiphanius names Cleopas ("to Cleopas and the other").'),
 A('24:19', G('24:19'), 'And he said to them, "What things?" And they said to him, "Concerning Jesus of Nazareth, a man who was a prophet mighty in deed and word before God and all the people,',
   'present for 24:19a (Marc. 4.43.3); 24:19b unattested', [T433],
   wording='NA27. Tertullian attests that Jesus asked as if he did not know ("etiam dissimulans"). 19b ("a prophet mighty in deed and word before God and all the people") is not cited by either witness. Class of 19b: U? (METHOD §3). Tertullian works through the passage in order (4.43.3–5): he paraphrases 24:15–19a and quotes 24:21, "we thought that he was the redeemer of Israel", arguing that Jesus would not have let the disciples hold an opinion of him that was false (4.43.4). The description of 19b would fit that argument, as the crowd\'s "a great prophet" does at 7:16 (4.18.3), but he had the stronger words of 24:21 and used them; his passing over 19b (and 24:20) is not the silence of a witness who needed the passage, so the U− test is not met. Epiphanius (sch. 77) does not touch 24:19–20. No witness reports the words missing, so they stay in the text (METHOD §5.3).'),
 U('24:20', G('24:20'), 'and how our chief priests and rulers delivered him up to be condemned to death, and crucified him.', 'Inside the attested paragraph 24:13–27.'),
 A('24:21', G('24:21', [('ἡμεῖς δὲ ἠλπίζομεν', 'ἡμεῖς δὲ ἐνομίζομεν')]),
   'But we thought that he was the one to redeem Israel. Yes, and besides all this, it is now the third day since these things happened.',
   'present for 24:21a (Marc. 4.43.3); 24:21b unattested', [T433, T('4.43.4–5', '"Ceterum non existimarent eum creatoris… nec post resurrectionem alium se eis ostendit quam quem existimatum sibi dixerant… quod existimaverant, id volens credi se, eum se confirmabat quem existimaverant…"')],
   wording=('Marcionite reading adopted (retroversion): "we thought" (ἐνομίζομεν, Tertullian "putabamus") for NA27 "we hoped" (ἠλπίζομεν). The Latin cannot render "hoped", and Tertullian builds 4.43.4–5 on what the disciples "thought" (existimare, five times). ἐνομίζομεν is also the reading of the Arabic and Persian Diatessaron and Ambrosiaster (Roth, citing IGNTP). Roth rates the verb possible only; this is a departure. '
            'Tertullian\'s "redeemer of Israel" can render "the one about to redeem Israel" and is probably his own noun (Roth, citing Lukas); NA27 is printed. 21b is unattested.')),
 U('24:22', G('24:22'), 'Moreover, some women of our company amazed us. They were at the tomb early in the morning,', 'Inside the attested paragraph 24:13–27.'),
 U('24:23', G('24:23'), 'and when they did not find his body, they came back saying that they had even seen a vision of angels, who said that he was alive.', 'Inside the attested paragraph 24:13–27.'),
 A('24:25', G('24:25', [('οἷς ἐλάλησαν οἱ προφῆται·', 'οἷς ἐλάλησεν πρὸς ὑμᾶς·')]),
   'And he said to them, "O foolish ones, and slow of heart to believe all that he spoke to you!',
   'present (Marc. 4.43.4; Pan. 42.11.6, sch. 77)',
   [T('4.43.4', '"Plane invectus est in illos: O insensati et tardi corde in non credendo omnibus quae locutus est ad vos. Quae locutus non alterius se dei esse probat, sed eiusdem dei."'), E77],
   wording=('Marcionite reading adopted (retroversion): "all that he spoke to you" (οἷς ἐλάλησεν πρὸς ὑμᾶς) for NA27 "all that the prophets have spoken". Both witnesses lack "the prophets": Epiphanius states that the text had "that I spoke to you" in place of "that the prophets spoke", and Tertullian quotes "all that he spoke to you" (NA27: ἐλάλησεν… πρὸς ὑμᾶς McionT,A; -σα McionA,E). '
            'Tertullian\'s third person is printed. Epiphanius\' own elenchus shows the difficulty of his first person: "if he had said \'I spoke to you\', they would have recognized him from that word; how then were their eyes opened at the breaking of bread?" The Adamantius Dialogue (198,5–7) also has the first person, but in the orthodox speaker\'s words. Roth: the final element uncertain.')),
 A('24:26', G('24:26'), 'Was it not necessary that the Anointed One should suffer these things and enter into his glory?"',
   'present (Pan. 42.11.6, sch. 77)', [E77], wording='NA27. Epiphanius quotes "was it not necessary that he suffer these things?"; the rest of the verse is unattested.'),
 U('24:28', G('24:28'), 'So they drew near to the village to which they were going. He acted as if he were going farther,', 'Inside the attested paragraph 24:28–32.'),
 U('24:29', G('24:29'), 'but they urged him strongly, saying, "Stay with us, for it is toward evening and the day is now far spent." So he went in to stay with them.', 'Inside the attested paragraph 24:28–32.'),
 A('24:30', G('24:30'), 'When he was at table with them, he took the bread and blessed and broke it and gave it to them.',
   'present (Pan. 42.11.6, sch. 77)', [E77], wording='NA27. Epiphanius: "when he broke the bread" (Roth: possible for the wording).'),
 A('24:31', G('24:31'), 'And their eyes were opened, and they recognized him. And he vanished from their sight.',
   'present for 24:31a (Pan. 42.11.6, sch. 77)', [E77],
   wording='NA27. Epiphanius quotes "their eyes were opened and they recognized him". "He vanished" appears only in his elenchus, which he expands for his argument (Roth); it is unattested and printed as part of the verse.'),
 W33('24:33', 'And they rose that same hour and returned to Jerusalem, and they found the eleven and those with them gathered together,'),
 W33('24:34', 'saying, "The Lord has really been raised, and has appeared to Simon!"'),
 W33('24:35', 'And they told what had happened on the road, and how he had been made known to them in the breaking of the bread.'),
 U('24:36', G('24:36'), 'As they were talking about these things, he himself stood among them, and said to them, "Peace to you!"', 'Opens the attested paragraph 24:36–43.'),
 A('24:37', G('24:37'), 'But they were startled and frightened and thought they saw a spirit.',
   'present (Marc. 4.43.6)', [T436],
   wording=('NA27. Tertullian: "when they hesitated whether he was a phantom, or rather believed him a phantom". D d read φάντασμα ("phantom") for πνεῦμα. "Phantom" (phantasma) is Tertullian\'s standing word for the Marcionite Christ (4.40.3; 4.42.7–8; 4.43.8), so his use of it here does not show the wording of the verse; Roth: possible only. Not adopted.')),
 A('24:38', G('24:38'), 'And he said to them, "Why are you troubled, and why do doubts arise in your hearts?',
   'present (Marc. 4.43.6; Pan. 42.11.6, sch. 78)', [T436, E78], wording='NA27. Both witnesses quote the question.'),
 A('24:39', G('24:39', [('ψηλαφήσατέ με καὶ ἴδετε, ', ''), ('πνεῦμα σάρκα καὶ ὀστέα', 'πνεῦμα ὀστέα')]),
   'See my hands and my feet, that it is I myself; for a spirit does not have bones as you see that I have."',
   'present (Marc. 4.43.6–8; Pan. 42.11.6, sch. 78); "handle me and see" and "flesh and" not present',
   [T436, T('4.43.7', '"Vult itaque sic dictum quasi, Spiritus ossa non habet sicut me videtis habentem, ad spiritum referatur, sicut me videtis habentem, id est non habentem ossa sicut et spiritus."'),
    T('4.43.8', '"Cur autem inspectui eorum manus et pedes suos offert, quae membra ex ossibus constant, si ossa non habebat?"'), E78],
   wording=('NA27 without "handle me and see" and without "flesh and" (attested omissions, METHOD §5.3). '
            '"Flesh and": both witnesses quote "a spirit does not have bones" (Tertullian twice). Epiphanius, when he cites the verse himself, has "flesh and bones" (Ancor. 91.6; Pan. 64.64.7; 77.9.5, as quoted by Roth), and in his elenchus here says that the Saviour has "bones and flesh"; his scholion has only "bones". NA27 cites McionT,E for the omission. '
            '"Handle me and see": Tertullian\'s quotation runs on from "it is I myself" to "for a spirit"; he argues from this verse that the body was real ("what could be clearer about the truth of the body?") and speaks only of hands and feet offered "for inspection" (4.43.8). An invitation to touch would have been his strongest evidence. Epiphanius\' quotation also lacks it, but he also skips "that it is I myself", so his evidence is weaker here. '
            'Roth rates both omissions "may not have been present"; the departure rests on the witnesses\' arguments and citation habits. Tertullian also cites the verse without both elements in Carn. Chr. 5.9 (as quoted by Roth), so the shorter form may not have been confined to Marcion\'s text.')),
 U('24:40', G('24:40'), 'And when he had said this, he showed them his hands and his feet.',
   'Inside the attested paragraph 24:36–43. Tertullian\'s "he offers his hands and feet for inspection" (4.43.8) refers to 24:39 (Roth).'),
 A('24:41', G('24:41'), 'And while they still disbelieved for joy and were marvelling, he said to them, "Have you anything here to eat?"',
   'present (Marc. 4.43.8)', [T('4.43.8', '"Atquin adhuc eis non credentibus propterea cibum desideravit, ut se ostenderet etiam dentes habere."')],
   wording='NA27. Tertullian attests the disbelief and the request for food (Roth: very likely). "For joy and marvelling" is unattested.'),
 U('24:42', G('24:42'), 'They gave him a piece of broiled fish,',
   'Inside the attested paragraph 24:36–43. Roth classes the verse present on Eznik, De Deo 407 (Marcionites abstain from fish now, "just as he too after his resurrection ate the fish"). The Armenian text was not checked here, so the verse is printed as unattested.'),
 U('24:43', G('24:43'), 'and he took it and ate before them.',
   'Inside the attested paragraph 24:36–43. See 24:42 (Eznik, as quoted by Roth). Tertullian\'s "he asked for food to show that he had teeth" (4.43.8) points to the eating.'),
 W44('24:44', 'Then he said to them, "These are my words that I spoke to you while I was still with you, that everything written about me in the law of Moses and the prophets and the psalms must be fulfilled."',
     note=' καὶ τοῖς προφήταις (SBLGNT καὶ προφήταις).'),
 W44('24:45', 'Then he opened their minds to understand the scriptures,'),
 W44('24:46', 'and he said to them, "Thus it is written, that the Anointed One should suffer and rise from the dead on the third day,'),
 A('24:47', G('24:47'),
   'and that repentance for the forgiveness of sins should be proclaimed in his name to all the nations. Beginning from Jerusalem,',
   'present (Marc. 4.43.9)', [T('4.43.9', '"siquidem et apostolos mittens ad praedicandum universis nationibus, in omnem terram exire sonum eorum et in terminos terrae voces eorum, psalmum adimplendo praecepit."')],
   wording=('NA27 (εἰς ἄφεσιν, as NA27; SBLGNT καὶ ἄφεσιν; NA27 punctuation, with "beginning from Jerusalem" opening the sentence of 24:48). Tertullian attests the sending to preach to all the nations, as Jesus\' command; Roth: κηρυχθῆναι… εἰς πάντα τὰ ἔθνη very likely. '
            'The infinitive depends on "thus it is written" in 24:46, printed as restored by method. 24:47b ("beginning from Jerusalem") is unattested and is printed as restored by method with 24:48–53 (METHOD §11); the previous text ended here with an ellipsis before the verse.')),
 W48('24:48', 'you are witnesses of these things.', note=' Without ἐστε (SBLGNT has it).'),
 W48('24:49', 'And look, I am sending the promise of my Father upon you; but stay in the city until you are clothed with power from on high."', note=' ἀποστέλλω (SBLGNT ἐξαποστέλλω); NA27 [ἰδού] printed without the brackets (METHOD §5.7).'),
 W48('24:50', 'Then he led them out as far as Bethany, and lifting up his hands he blessed them.', page='246', note=' NA27 [ἔξω] printed without the brackets (METHOD §5.7).'),
 W48('24:51', 'And while he was blessing them, he parted from them and was carried up into heaven.', page='246', note=' NA27 prints 51b without brackets (SBLGNT brackets it).'),
 W48('24:52', 'And they worshipped him and returned to Jerusalem with great joy,', page='246', note=' NA27 prints 52a without brackets (SBLGNT brackets it).'),
 W48('24:53', 'and they were continually in the temple blessing God.', page='246'),
]

OMITTED = [
 dict(ref='24:12', cls='U−', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason=('Peter runs to the tomb and sees the linen cloths. Neither witness cites it, and both follow the chapter closely here (Tertullian 4.43.2–3 goes from the report and the unbelief, 24:9–11, to Emmaus; Epiphanius from sch. 76 to 77). The linen cloths left in the tomb would have served Tertullian, who has just argued from the linen of the burial (4.42.7), and Epiphanius, who argues throughout for a real body. '
              'It is also lacking in D and the Old Latin (a Western non-interpolation). Classed probably absent.'))),
 dict(ref='24:24', cls='U−', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='"Some of those with us went to the tomb and found it just as the women had said, but him they did not see." It reports the visit of 24:12, which is classed probably absent.')),
 dict(ref='24:27', cls='U−', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason=('"Beginning with Moses and all the prophets, he interpreted to them in all the scriptures the things concerning himself." Tertullian\'s thesis in book 4 is that Jesus is the Christ of the prophets, and he closes it at this chapter (4.43.9: "I have shown Jesus Christ… from the teachings of the prophets"); Epiphanius\' scholion 77 turns on "the prophets" at 24:25. Neither cites the verse that would have proved their point. Classed probably absent.'))),
 dict(ref='24:32', cls='U−', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='"Did not our hearts burn within us… while he opened to us the scriptures?" Unattested; for the same reason as 24:27 it would have been cited if present. Classed probably absent.')),
]

PREAMBLE = (
 "The Living One. At early dawn the women come to the tomb with spices and do not find the body. Two men in dazzling clothing "
 "say to them: \"Why do you seek the Living One among the dead? He has been raised. Remember all that he told you while he was "
 "still in Galilee.\" The women report it, and the disciples do not believe them. On the road to Emmaus Jesus joins two of them, "
 "Cleopas and another, who do not recognize him. They say: \"We thought that he was the one to redeem Israel.\" He answers: "
 "\"O foolish ones, and slow of heart to believe all that he spoke to you!\" At table he breaks the bread, and their eyes are "
 "opened. They rise and return to Jerusalem, where the eleven say \"the Lord has really been raised, and has appeared to "
 "Simon\" (24:33–35). Then he stands among the disciples. They are afraid and think they see a spirit. He says: \"See my hands and my feet, "
 "that it is I myself; for a spirit does not have bones as you see that I have.\" He asks for food. He opens their minds to "
 "understand the scriptures (24:44–46) and sends them to proclaim repentance for the forgiveness of sins in his name to all the "
 "nations. No witness cites the text beyond this point. The text continues to its end: he leads them out to Bethany, blesses "
 "them, parts from them and is carried up into heaven, and they return to Jerusalem with great joy (24:47b–53). The return "
 "(24:33–35), the opening of the scriptures (24:44–46) and the ending (24:47b–53) are printed as restored by method, because "
 "the printed text needs them (METHOD §11; see the notes)."
)

NOTES = [
 dict(term='At the tomb (24:1–11)', cat='textual', refs=['24:1', '24:3', '24:4', '24:5', '24:6', '24:7', '24:9', '24:11'], text=(
  "Tertullian (4.43.1–5) follows the women who came \"before light\" with spices, the body not found, the two \"angels\", the "
  "women's return \"from the tomb\" and the disciples' persisting unbelief; he quotes the words of the two men: \"Remember all that "
  "he told you in Galilee, that the son of man must be delivered and crucified and on the third day rise.\" Epiphanius (sch. 76) "
  "quotes \"Why do you seek the Living One among the dead? He has been raised. Remember all that he told you while he was still "
  "with you.\" Two readings of this text are printed in 24:6: \"all that\" (ὅσα, both witnesses) and \"he has been raised\" "
  "without \"he is not here, but\" (Epiphanius, against his own habit of citation). \"Of the Lord Jesus\" (24:3) and \"into the "
  "hands of sinful men\" (24:7) are not cited and are printed with NA27.")),
 dict(term='Emmaus (24:13–31)', cat='textual', refs=['24:13', '24:15', '24:16', '24:18', '24:19', '24:21', '24:25', '24:26', '24:30', '24:31'], text=(
  "Tertullian (4.43.3–5): two of them were travelling; the Lord joined them without showing who he was, and even pretended "
  "not to know what had happened; they said \"we thought that he was the redeemer of Israel\", and he rebuked them: \"O "
  "foolish and slow of heart to believe all that he spoke to you.\" Epiphanius (sch. 77) names Cleopas and states that the text "
  "read \"that I spoke to you\" where canonical Luke has \"that the prophets spoke\", and quotes \"was it not necessary that he "
  "suffer these things?\" and the opening of their eyes when he broke the bread. Both witnesses agree that the rebuke was "
  "about Jesus' own words, not about the prophets. Tertullian's \"we thought\" and \"he spoke to you\" are printed. \"A prophet "
  "mighty in deed and word\" (24:19b) is not cited by either witness; it stands in the text as part of an attested verse.")),
 dict(term='The appearance to the disciples (24:36–43)', cat='textual', refs=['24:36', '24:37', '24:38', '24:39', '24:40', '24:41', '24:42', '24:43'], text=(
  "Tertullian (4.43.6–8) quotes: \"Why are you troubled, and why do thoughts arise in your hearts? See my hands and my feet, "
  "that it is I myself, for a spirit does not have bones as you see me having\", and adds that Jesus asked for food \"to show "
  "that he had teeth\". Epiphanius (sch. 78) quotes the same verse with \"bones\" only. In this text there is no \"handle me and "
  "see\" and no \"flesh and\". Tertullian reports how Marcion read the end of the verse: \"as you see me having\" refers to the "
  "spirit, that is, \"not having bones, as a spirit has none\" (4.43.7). Eznik reports that the Marcionites based their "
  "abstinence from fish on Jesus' eating fish after his resurrection (De Deo 407, as quoted by Roth). \"Peace to you\" (24:36) "
  "and the showing of hands and feet (24:40), both lacking in D and the Old Latin, are not cited and are printed in grey.")),
 dict(term='Not printed: 24:12, 24, 27, 32', cat='excision', refs=['24:11', '24:23', '24:26', '24:31'], text=(
  "No witness cites Peter's visit to the tomb (24:12) or the report of it (24:24); both are classed probably absent, since the "
  "linen cloths would have served Tertullian's argument and 24:12 is also lacking in D and the Old Latin. The interpretation "
  "of \"Moses and all the prophets\" (24:27) and the burning hearts \"while he opened to us the scriptures\" (24:32) would have "
  "been Tertullian's proof that Jesus is the Christ of the prophets, the thesis with which he ends his book; neither witness "
  "cites them, and they are classed probably absent. The correspondential reading tested all four at their places; they "
  "continue the line, but the printed text does not need them (24:27 is not needed once 24:44–46 is printed).")),
 dict(term='Restored by method: the return to Jerusalem (24:33–35)', cat='textual', refs=['24:31', '24:33', '24:34', '24:35', '24:36', '24:37'], text=(
  "No witness cites 24:33–35; it forms a paragraph with no attested verse (U?). It is printed as restored by method (METHOD "
  "§11). By its words: 24:36 opens \"as they were saying these things, he himself stood in their midst\", and without 24:33–35 "
  "no one says anything after 24:31; \"these things\" are what is told in 24:35, and \"their midst\" is the eleven gathered "
  "(24:33). Without it, those who are terrified and think they see a spirit (24:37) would be the two who have just recognized "
  "him at the bread. By its mechanics: the text's road goes to Jerusalem (9:51), and after the cross two go away from it "
  "(24:13); \"rising that same hour, they returned to Jerusalem\" brings them back, and \"he has appeared to Simon\" is the "
  "turning back foretold at 22:32. The Greek is NA27, checked on the page image (p. 244).")),
 dict(term='Restored by method: the scriptures opened (24:44–46)', cat='textual', refs=['24:44', '24:45', '24:46', '24:47'], text=(
  "No witness cites 24:44–46, and the class is U−: Tertullian passes from the request for food (24:41; 4.43.8) to the "
  "sending to the nations (24:47; 4.43.9) and ends his book by claiming that he has shown Jesus to be the Christ of the "
  "prophets, for which these verses would have been his proof text. The passage is printed as restored by method (METHOD "
  "§11), against that class. By its words: the attested 24:47, \"and that repentance… be proclaimed\", is an infinitive that "
  "depends on 24:46, \"thus it is written that…\"; the previous text printed it after an ellipsis. By its mechanics: the text "
  "veils the understanding on purpose (9:45; 18:34) and lifts the veil in stages — remembering (24:8), the veil of the "
  "sanctuary torn (23:45), the eyes opened at the bread (24:31). \"He opened their minds to understand the scriptures\" is "
  "the last stage. And 16:31 sets the condition that rising from the dead persuades only those who hear Moses and the "
  "prophets; here Moses and the prophets are opened about rising \"from the dead on the third day\". The Greek is NA27, checked "
  "on the page image (p. 245); at 24:44 NA27 reads καὶ τοῖς προφήταις.")),
 dict(term='Restored by method: the ending (24:47b–53)', cat='textual', refs=['24:47', '24:48', '24:49', '24:50', '24:51', '24:52', '24:53'], text=(
  "Tertullian ends his commentary on the gospel with Jesus \"sending the apostles to preach to all the nations\" (4.43.9), and "
  "no witness cites anything after 24:47. METHOD §10 ended the text at the last attested verse by default; the owner has "
  "overridden that default, and 24:47b–53 is printed as restored by method (METHOD §11). By its mechanics: at 9:51 the text "
  "names its own end, \"the days of his taking up (ἀνάλημψις) were being fulfilled, and he set his face to go to Jerusalem\". "
  "Without 24:50–51 the taking up is never told and the text stops at the command, before the end it announced. Here he "
  "lifts his hands and blesses them, parts from them while blessing, and is carried up into heaven; they return to Jerusalem "
  "with great joy and are continually in the temple. The Greek is NA27, checked on the page images (pp. 245–246): NA27 punctuates "
  "\"beginning from Jerusalem\" with 24:48 and reads ὑμεῖς μάρτυρες (without ἐστε), ἀποστέλλω, [ἰδού] and [ἔξω] (printed without "
  "brackets, METHOD §5.7). 24:51b (\"and was carried up into heaven\") and 24:52a (\"worshipped him\") are lacking in ℵ* D and the "
  "Old Latin (Western non-interpolations); NA27 prints them in its text, and a Western omission does not by itself remove "
  "words from this text.")),
 dict(term='The Living One', cat='theological', refs=['24:5', '24:6', '24:25', '24:31', '24:39', '24:41'], text=(
  "Interpretation. Three layers are kept apart. (a) Text: the two men at the tomb call Jesus \"the Living One\" and say \"he has been "
  "raised\"; the disciples recognize him in the breaking of the bread; he answers their fear of a spirit by showing hands and "
  "feet and saying that a spirit does not have bones \"as you see that I have\"; he asks for food; he sends them to all the "
  "nations; the rebuke on the road is about believing his own words. (b) Canonical Luke has in addition the touch and the "
  "flesh (24:39), Peter at the tomb (24:12, 24), the proof from Moses and the prophets on the road (24:27, 32), and the passages "
  "this edition prints as restored by method (24:33–35, 44–46, 47b–53). On the Semler model these are a common original's; on "
  "the Schwegler model, additions; the witnesses show only that they do not cite them. (c) Reception: the Marcionites "
  "read 24:39 as Jesus saying that he had no bones, like a spirit (Tertullian 4.43.7), and kept the meal of fish as the basis "
  "of their own practice (Eznik). The text itself holds together the Living One who is not found among the dead and a risen "
  "Jesus who can be seen, who eats, and who is recognized at table.")),
]
