"""Batch 1, chapter 2 of the reconstruction: Luke 5:1–6:11."""
from buildlib import greek

def U(ref, gr, en, reason='Inside an attested pericope.'):
    return dict(ref=ref, cls='U?', flag=True, gr=gr, en=en,
                app=dict(roth='unattested', witnesses=[], wording='NA27.',
                         decision='printed, flagged unattested', reason=reason))

def A(ref, gr, en, roth, witnesses, wording='NA27.', **kw):
    app = dict(roth=roth, witnesses=witnesses, wording=wording, decision='printed')
    app.update(kw)
    return dict(ref=ref, cls='A+', gr=gr, en=en, app=app)

T491 = {'source': 'Tertullian, Marc. 4.9.1', 'evidence': '"ut ab illa [piscatura] in apostolos sumeret Simonem et filios Zebedaei… dicens Petro trepidanti de copiosa indagine piscium, Ne time, abhinc enim homines eris capiens?"'}

ENTRIES = [
 U('5:1', greek('5:1'), 'Once, while the crowd was pressing in on him to hear the word of God, he was standing beside the lake of Gennesaret,',
   'Opens the attested pericope 5:1–11.'),
 A('5:2', greek('5:2'), 'and he saw two boats lying at the edge of the lake; the fishermen had stepped out of them and were washing their nets.',
   'present (Marc. 4.9.1)', [T491], reason='Tertullian names fishing as the trade from which the emissaries were taken.'),
 U('5:3', greek('5:3'), "He got into one of the boats, which was Simon's, and asked him to put out a little from the land. Then he sat down and taught the crowds from the boat."),
 U('5:4', greek('5:4'), 'When he had finished speaking, he said to Simon, "Put out into the deep water, and let down your nets for a catch."'),
 U('5:5', greek('5:5'), 'Simon answered, "Master, we worked hard all night and caught nothing. But at your word I will let down the nets."'),
 U('5:6', greek('5:6'), 'When they had done this, they enclosed a great number of fish, and their nets were beginning to break.'),
 U('5:7', greek('5:7'), 'So they signalled to their partners in the other boat to come and help them. They came and filled both boats, so that they began to sink.'),
 U('5:8', greek('5:8'), 'When Simon Peter saw it, he fell at the knees of Jesus, saying, "Go away from me, Lord, for I am a sinful man."'),
 A('5:9', greek('5:9'), 'For amazement had seized him and all who were with him at the catch of fish they had taken;',
   'present (Marc. 4.9.1)', [T491], reason='"Petro trepidanti de copiosa indagine piscium".'),
 A('5:10', greek('5:10'), 'and so also James and John, sons of Zebedee, who were partners with Simon. And Jesus said to Simon, "Do not be afraid; from now on you will be catching people alive."',
   'present (Marc. 4.9.1)', [T491],
   wording='NA27. Tertullian\'s "abhinc enim" suggests γάρ after ἀπὸ τοῦ νῦν (Roth: possible only); not adopted.'),
 A('5:11', greek('5:11'), 'And when they had brought the boats to land, they left everything and followed him.',
   'present (Marc. 4.9.2)', [{'source': 'Tertullian, Marc. 4.9.2', 'evidence': '"Denique relictis naviculis secuti sunt eum".'}]),
 A('5:12', greek('5:12', [('λέπρας· καὶ ἰδὼν τὸν Ἰησοῦν', 'λέπρας· ἰδὼν δὲ τὸν Ἰησοῦν')]),
   'While he was in one of the towns, there was a man full of leprosy. When he saw Jesus, he fell on his face and begged him, "Lord, if you are willing, you can make me clean."',
   'present (Marc. 4.9.3; Pan. 42.11.17, refutation 1)',
   [{'source': 'Tertullian, Marc. 4.9.3', 'evidence': 'The cleansing of the leper.'}],
   wording='NA27 (ἰδὼν δέ; SBLGNT καὶ ἰδών — checked on the page image).'),
 A('5:13', greek('5:13', [('εἰπών·', 'λέγων·')]),
   'He stretched out his hand and touched him, saying, "I am willing; be made clean." And immediately the leprosy left him.',
   'present (Marc. 4.9.4, 7; Pan. 42.11.17, refutation 1)',
   [{'source': 'Tertullian, Marc. 4.9.4–7', 'evidence': 'The touch and the cleansing.'}],
   wording='NA27 (λέγων; SBLGNT εἰπών — checked on the page image).'),
 A('5:14', greek('5:14', [('καθὼς προσέταξεν Μωϋσῆς εἰς μαρτύριον αὐτοῖς.', 'καθὼς προσέταξεν Μωϋσῆς, ἵνα ᾖ μαρτύριον τοῦτο ὑμῖν.')]),
   'And he ordered him to tell no one: "But go, show yourself to the priest, and make the offering for your cleansing as Moses commanded, so that this may be a testimony for you."',
   'present (Marc. 4.9.9–10; Pan. 42.11.6, sch. 1)',
   [{'source': 'Epiphanius, Pan. 42.11.6, sch. 1', 'evidence': '»ἀπελθὼν δεῖξον σεαυτὸν τῷ ἱερεῖ καὶ προσένεγκε περὶ τοῦ καθαρισμοῦ σου, καθὼς προσέταξε Μωυσῆς· ἵνα ᾖ μαρτύριον τοῦτο ὑμῖν« ἀνθ\' οὗ εἶπεν ὁ σωτὴρ »εἰς μαρτύριον αὐτοῖς«.'},
    {'source': 'Tertullian, Marc. 4.9.9–10', 'evidence': '"vetuit eum divulgare… Vade, ostende te sacerdoti, et offer munus quod praecepit Moyses… Itaque adiecit, Ut sit vobis in testimonium."'}],
   wording='Marcionite reading adopted: ἵνα ᾖ μαρτύριον τοῦτο ὑμῖν (Epiphanius\' Greek, confirmed in sense by Tertullian). NA27 apparatus: ἵνα εἰς μαρτύριον ᾖ ὑμῖν τοῦτο D it; (McionT,E). Tertullian\'s "in testimonium" and D have εἰς; Epiphanius does not; Roth prints εἰς. The Greek quotation is printed as it stands and εἰς is left open. Tertullian\'s "munus" (τὸ δῶρον) is rated possible by Roth; not adopted.',
   western='Agrees with D and the Old Latin in the ἵνα-clause and second person.'),
 U('5:15', greek('5:15'), 'But the report about him spread all the more, and great crowds gathered to hear him and to be healed of their illnesses.',
   'Inside the attested pericope 5:12–16.'),
 U('5:16', greek('5:16'), 'But he would withdraw to deserted places and pray.', 'Inside the attested pericope 5:12–16.'),
 A('5:17', greek('5:17'), 'One day, as he was teaching, Pharisees and teachers of the law were sitting there who had come from every village of Galilee and Judea and from Jerusalem; and the power of the Lord was with him to heal.',
   'present (Marc. 4.10.1)', [{'source': 'Tertullian, Marc. 4.10.1', 'evidence': '"Curatur et paralyticus, et quidem in coetu, spectante populo."'}]),
 A('5:18', greek('5:18', [('θεῖναι ἐνώπιον αὐτοῦ', 'θεῖναι αὐτὸν ἐνώπιον αὐτοῦ')]),
   'And some men came carrying on a stretcher a man who was paralysed, and they were trying to bring him in and lay him before him.',
   'present (Marc. 4.10.1)', [{'source': 'Tertullian, Marc. 4.10.1', 'evidence': '"Curatur et paralyticus".'}],
   wording='NA27, including the bracketed [αὐτόν] after θεῖναι (SBLGNT omits it).'),
 U('5:19', greek('5:19'), 'Finding no way to bring him in because of the crowd, they went up on the roof and let him down with his stretcher through the tiles into the middle, in front of Jesus.',
   'Inside the attested pericope 5:17–26.'),
 A('5:20', greek('5:20'), 'When he saw their faith, he said, "Man, your sins are forgiven you."',
   'present (Marc. 4.10.13–14)', [{'source': 'Tertullian, Marc. 4.10.14', 'evidence': '"in isto loco primum in quo primum peccata dimisit".'}]),
 A('5:21', greek('5:21'), 'And the scribes and the Pharisees began to question, saying, "Who is this who speaks blasphemies? Who can forgive sins but God alone?"',
   'present (Marc. 4.10.1, 13)', [{'source': 'Tertullian, Marc. 4.10.1, 13', 'evidence': '"Quis dimittet peccata nisi solus deus?"; "non posse hominem delicta dimittere, sed deum solum".'}]),
 U('5:22', greek('5:22'), 'But Jesus, knowing their thoughts, answered them, "Why do you question in your hearts?', 'Inside the attested pericope 5:17–26.'),
 U('5:23', greek('5:23'), 'Which is easier: to say, \'Your sins are forgiven you\', or to say, \'Get up and walk\'?', 'Inside the attested pericope 5:17–26.'),
 A('5:24', greek('5:24', [('ἔγειρε καὶ ἄρας τὸ κλινίδιόν σου πορεύου', 'ἔγειρε καὶ ἆρον τὸν κράβαττόν σου καὶ πορεύου')]),
   'But so that you may know that the son of man has authority on earth to forgive sins" — he said to the paralysed man — "I say to you, get up, and take up your mat, and go to your home."',
   'present (Marc. 4.10.1, 13; Pan. 42.11.6, sch. 2)',
   [{'source': 'Epiphanius, Pan. 42.11.6, sch. 2', 'evidence': '»ἵνα δὲ εἰδῆτε ὅτι ἐξουσίαν ἔχει ὁ υἱὸς τοῦ ἀνθρώπου ἀφιέναι ἁμαρτίας ἐπὶ τῆς γῆς«.'},
    {'source': 'Tertullian, Marc. 4.10.1', 'evidence': '"Exsurge, et tolle grabatum" (the Latin transcription on tertullian.org omits a line here; Evans\' English has "Arise and take up thy bed").'}],
   wording='5:24a: NA27 order kept; Epiphanius\' order (ἐξουσίαν ἔχει ὁ υἱὸς τοῦ ἀνθρώπου ἀφιέναι ἁμαρτίας ἐπὶ τῆς γῆς) is Mark\'s and Matthew\'s, and Roth marks the order uncertain. 5:24b: reading adopted from Tertullian (retroversion): ἆρον and καί, ℵ D 1424 pc; McionT; τὸν κράβαττον, D 1424 c r1; McionT (NA27 apparatus). Latin grabatum renders κράβαττος, not κλινίδιον. Roth: very likely.',
   western='Agrees with D and Old Latin c r1 (κράβαττον).'),
 U('5:25', greek('5:25'), 'And at once he stood up in front of them, took up what he had been lying on, and went home, glorifying God.', 'Inside the attested pericope 5:17–26.'),
 A('5:26', greek('5:26'), 'Amazement seized all of them, and they glorified God and were filled with awe, saying, "We have seen strange things today."',
   'present (Marc. 4.10.1)', [{'source': 'Tertullian, Marc. 4.10.1', 'evidence': '"spectante populo. Videbit enim, inquit Esaias, populus sublimitatem domini et gloriam dei" — applied to the onlookers.'}],
   reason='An allusion: Tertullian applies Isaiah\'s "the people shall see the glory of God" to the crowd\'s response. Accepted with Roth; the wording is not attested.'),
 A('5:27', greek('5:27'), 'After this he went out and saw a tax collector named Levi sitting at the tax booth, and he said to him, "Follow me."',
   'present (Marc. 4.11.1)', [{'source': 'Tertullian, Marc. 4.11.1', 'evidence': '"Publicanum adlectum a domino in argumentum deducit".'}]),
 U('5:28', greek('5:28'), 'And he left everything, got up and followed him.', 'Inside the attested pericope 5:27–32.'),
 U('5:29', greek('5:29'), 'Then Levi gave a great banquet for him in his house; and there was a large crowd of tax collectors and others reclining at table with them.', 'Inside the attested pericope 5:27–32.'),
 A('5:30', greek('5:30'), 'And the Pharisees and their scribes grumbled to his disciples, saying, "Why do you eat and drink with tax collectors and sinners?"',
   'present (Marc. 4.11.2)', [{'source': 'Tertullian, Marc. 4.11.1–2', 'evidence': 'The tax collectors and "ethnicos et publicanos, quos adlegebat".'}]),
 A('5:31', greek('5:31'), 'Jesus answered them, "Those who are well have no need of a physician, but those who are sick.',
   'present (Marc. 4.11.1)', [{'source': 'Tertullian, Marc. 4.11.1', 'evidence': '"dicendo medicum sanis non esse necessarium sed male habentibus".'}]),
 U('5:32', greek('5:32'), 'I have not come to call the righteous but sinners to repentance."', 'Inside the attested pericope 5:27–32.'),
 A('5:33', greek('5:33'), 'Then they said to him, "John\'s disciples fast often and say prayers, and so do those of the Pharisees, but yours eat and drink."',
   'present (Marc. 4.11.5; Ephrem, Hymns against Heresies 47.4)', [{'source': 'Tertullian, Marc. 4.11.5', 'evidence': '"discipulos Christi manducantes et bibentes ad formam discipulorum Ioannis assidue ieiunantium et orantium".'}]),
 A('5:34', greek('5:34', [('ὁ δὲ εἶπεν πρὸς αὐτούς', 'ὁ δὲ Ἰησοῦς εἶπεν πρὸς αὐτούς')]),
   'Jesus said to them, "Can you make the wedding guests fast while the bridegroom is with them?',
   'present (Marc. 4.11.6; Ephrem)', [{'source': 'Tertullian, Marc. 4.11.6', 'evidence': '"quod non possent ieiunare filii sponsi quamdiu cum eis esset sponsus".'}],
   wording='NA27, including ὁ Ἰησοῦς (SBLGNT omits it — checked on the page image). NA27 apparatus: δύνανται οἱ υἱοί… νηστεύειν ℵ* D it; (McionT). Roth: possible only; not adopted.',
   western='Tertullian\'s form agrees with ℵ* D it.'),
 A('5:35', greek('5:35'), 'But days will come when the bridegroom is taken away from them, and then they will fast in those days."',
   'present (Marc. 4.11.6)', [{'source': 'Tertullian, Marc. 4.11.6', 'evidence': '"postea vero ieiunaturos promittens cum ablatus ab eis sponsus esset".'}]),
 A('5:36', greek('5:36', [('εἰ δὲ μήγε', 'εἰ δὲ μή γε')]),
   'He also told them a parable: "No one tears a patch from a new garment and sews it on an old garment; otherwise he will tear the new, and the patch from the new will not match the old.',
   'present (Marc. 4.11.9–10; Pan. 42.2.1; Adam. 90,8–; Philastrius 45.2)', [{'source': 'Tertullian, Marc. 4.11.9', 'evidence': '"veteri, id est priori evangelio, pannum haereticae novitatis assuisti".'}],
   wording='NA27 (μή γε). Roth: the wording "can no longer be reconstructed"; the Marcionite discussion may have taken wine before patch.'),
 A('5:37', greek('5:37', [('εἰ δὲ μήγε', 'εἰ δὲ μή γε')]),
   'And no one puts new wine into old wineskins; otherwise the new wine will burst the skins, and it will be spilled, and the skins will be ruined.',
   'present (Marc. 4.11.9–10; Pan. 42.2.1; Ephrem)', [{'source': 'Tertullian, Marc. 4.11.9', 'evidence': '"Inflatus es utribus veteribus et excerebratus es novo vino".'}],
   wording='NA27 (μή γε).'),
 A('5:38', greek('5:38'), 'But new wine must be put into new wineskins."',
   'present, uncertain ([Adam. 90,5–7])', [{'source': 'Adamantius 90,5–7 (via Roth; attestation uncertain)', 'evidence': 'NA27 cites McionA for βάλλουσιν (ℵ* D it syp) and for the addition καὶ ἀμφότεροι συντηροῦνται.'}],
   wording='NA27. The Adamantius evidence is uncertain (Roth); not adopted.'),
 A('6:1', greek('6:1'), 'One sabbath he was going through the grainfields, and his disciples were plucking the heads of grain, rubbing them in their hands and eating them.',
   'present (Marc. 4.12.1, 5)', [{'source': 'Tertullian, Marc. 4.12.5', 'evidence': '"Esurierant discipuli ea die; spicas decerptas manibus efflixerant".'}]),
 A('6:2', greek('6:2'), 'But some of the Pharisees said, "Why are you doing what is not lawful on the sabbath?"',
   'present (Marc. 4.12.1, 5)', [{'source': 'Tertullian, Marc. 4.12.5', 'evidence': '"accusant pharisaei".'}]),
 A('6:3', greek('6:3', [('ὁπότε ἐπείνασεν', 'ὅτε ἐπείνασεν')]),
   'Jesus answered them, "Have you not read what David did when he and those who were with him were hungry,',
   'present (Marc. 4.12.5; Pan. 42.11.6, sch. 21)',
   [{'source': 'Epiphanius, Pan. 42.11.6, sch. 21', 'evidence': '»οὐδὲ τοῦτο ἀνέγνωτε, τί ἐποίησε Δαυίδ· εἰσῆλθεν εἰς τὸν οἶκον τοῦ θεοῦ«.'},
    {'source': 'Tertullian, Marc. 4.12.5', 'evidence': '"de exemplo David introgressi sabbatis templum".'}],
   wording='NA27 (ὅτε; SBLGNT ὁπότε), with the bracketed [ὄντες]. Epiphanius has τί for ὅ (= Matthew and Mark; Roth: probable only) and passes over the ὅτε-clause; a quotation that skips a clause is not evidence that the bracketed words were absent.'),
 A('6:4', greek('6:4'), 'how he entered the house of God and took the bread of the presence, and ate it and gave some to his companions, which it is not lawful for any but the priests to eat?"',
   'present (Marc. 4.12.5; Pan. 42.11.6, sch. 21)', [{'source': 'Epiphanius, Pan. 42.11.6, sch. 21', 'evidence': '»εἰσῆλθεν εἰς τὸν οἶκον τοῦ θεοῦ«.'},
    {'source': 'Tertullian, Marc. 4.12.5', 'evidence': '"fractis panibus propositionis".'}],
   wording='NA27 with the bracketed [ὡς] (see 6:3).'),
 A('6:5', greek('6:5', [('Κύριός ἐστιν τοῦ σαββάτου ὁ υἱὸς τοῦ ἀνθρώπου.', 'Κύριός ἐστιν ὁ υἱὸς τοῦ ἀνθρώπου καὶ τοῦ σαββάτου.')]),
   'And he said to them, "The son of man is lord even of the sabbath."',
   'present (Pan. 42.11.6, sch. 3; Marc. 4.12.11; Roth: position here or after 6:9 uncertain)',
   [{'source': 'Epiphanius, Pan. 42.11.6, sch. 3', 'evidence': '»κύριός ἐστιν ὁ υἱὸς τοῦ ἀνθρώπου καὶ τοῦ σαββάτου«.'},
    {'source': 'Tertullian, Marc. 4.12.11', 'evidence': '"Dominus sabbati dictus".'}],
   wording='Marcionite reading adopted from Epiphanius\' Greek. NA27 apparatus: ὁ υἱὸς τοῦ ἀνθρ. καὶ τοῦ σαβ. A D L Θ Ψ f1.13 33 𝔐 lat syh sa bopt; McionE. Roth: very likely. Kept in the canonical position; D places the verse after 6:10, and Roth leaves its place open.',
   western='Agrees with D in wording; D differs in position.'),
 A('6:6', greek('6:6'), 'On another sabbath he entered the assembly and taught. A man was there whose right hand was withered.',
   'present (Marc. 4.12.11, 14)', [{'source': 'Tertullian, Marc. 4.12.9–11', 'evidence': 'The healing on the sabbath of the man with the withered hand.'}]),
 A('6:7', greek('6:7'), 'The scribes and the Pharisees were watching him to see whether he would heal on the sabbath, so that they might find a way to accuse him.',
   'present (Marc. 4.12.9)', [{'source': 'Tertullian, Marc. 4.12.9', 'evidence': '"Exinde observant pharisaei si medicinas sabbatis ageret, ut accusarent eum".'}]),
 dict(ref='6:8', cls='U?', flag=True, gr=greek('6:8'),
      en='But he knew their thoughts, and he said to the man with the withered hand, "Get up and stand in the middle." And he got up and stood there.',
      app=dict(roth='present, uncertain ([Adam. 36,14]; ch. 9: "attestation uncertain")', witnesses=[], wording='NA27.',
               decision='printed, flagged unattested',
               reason='The only locus is an Adamantius passage whose tie to Marcion\'s text Roth himself marks uncertain (METHOD §2, rank 2 condition not met).')),
 A('6:9', greek('6:9'), 'Then Jesus said to them, "I ask you: is it lawful on the sabbath to do good or to do harm, to save life or to destroy it?"',
   'present (Marc. 4.12.11)', [{'source': 'Tertullian, Marc. 4.12.11', 'evidence': '"id operis permittens quod pro anima facturus esset".'}],
   wording='NA27. NA27 cites McionT for its text εἰ (against τί A Θ Ψ f1.13 𝔐) and ἀπολέσαι (against ἀποκτεῖναι A Θ 𝔐).'),
 U('6:10', greek('6:10'), 'And looking around at all of them, he said to him, "Stretch out your hand." He did so, and his hand was restored.',
   'Inside the attested pericope 6:6–11.'),
 U('6:11', greek('6:11'), 'But they were filled with fury and discussed with one another what they might do to Jesus.',
   'Inside the attested pericope 6:6–11.'),
]

OMITTED = [
 dict(ref='5:39', cls='U−', app=dict(roth='unattested', witnesses=[
      {'source': 'Tertullian, Marc. 4.11.9–11', 'evidence': 'Argues at length that old and new belong to one God.'}],
      decision='not printed',
      reason='Tertullian discusses the patch and wineskins (5:36–38) at length to show that old and new belong to the same God. A saying that the old is better would have served him; he does not cite it. NA27: vs 39 omitted by D it; Eus.',
      western='Absent also from D and the Old Latin.')),
]

PREAMBLE = (
 "Five scenes from Galilee: the call of the fishermen, the cleansing of a leper, the healing of a paralysed man, the call of a "
 "tax collector with the question about fasting, and two sabbath disputes. Tertullian works through all of them in order "
 "(Marc. 4.9–4.12) and Epiphanius quotes from three. The section is set inside Jewish practice. The cleansed leper is sent to the "
 "priest with the offering Moses commanded; in this text the reason given is \"so that this may be a testimony for you\". "
 "The sabbath disputes argue from what David did and from what the law permits. The witnesses also show the Marcionite church "
 "explaining some of this away: Tertullian reports that Marcion read the leper's offering as a concession to the man's habit. "
 "A community does not insert into its own scripture a passage it has to explain away, so these passages are older than the "
 "Marcionite reading of them (interpretation)."
)

NOTES = [
 dict(term='The call of the fishermen (5:1–11)', cat='textual', refs=['5:2', '5:9', '5:10', '5:11'], text=(
  "Tertullian, Marc. 4.9.1–2: Jesus took Simon and the sons of Zebedee from fishing, \"saying to Peter, who was afraid at the "
  "abundant catch of fish, Do not fear, for from now on you will be catching men\"; \"they left their boats and followed him\". "
  "This attests 5:2, 5:9–11 and the catch itself. 5:1 and 5:3–8 are not cited and are printed in grey. One library document "
  "(No Original Exists, App. B) lists ἐπιστάτα at 5:5 as a Marcionite reading; no witness cites 5:5, so the claim is not "
  "supported and is listed for correction.")),
 dict(term='The leper and the priest (5:12–14)', cat='textual', refs=['5:12', '5:13', '5:14'], text=(
  "Tertullian, Marc. 4.9.3–10, and Epiphanius, sch. 1 with refutation 1. NA27 reads ἰδὼν δέ at 5:12 and λέγων at 5:13 "
  "(SBLGNT: καὶ ἰδών, εἰπών); checked on the NA27 page. At 5:14 Epiphanius quotes the ending as »ἵνα ᾖ μαρτύριον τοῦτο ὑμῖν« "
  "and contrasts it with the canonical »εἰς μαρτύριον αὐτοῖς«; Tertullian has \"Ut sit vobis in testimonium\" (4.9.10). Two "
  "witnesses agree on the purpose clause and the second person; the Greek of Epiphanius is printed. D and the Old Latin read "
  "ἵνα εἰς μαρτύριον ᾖ ὑμῖν τοῦτο, and NA27 cites Marcion there. Whether εἰς stood in the text (Tertullian's \"in "
  "testimonium\", D) is left open. Tertullian also has \"offer the gift\" (munus); one witness, not adopted.")),
 dict(term='"So that this may be a testimony for you"', cat='theological', refs=['5:14'], text=(
  "Interpretation. Both witnesses attest that Jesus sends the man to the priest to make the offering Moses commanded. In "
  "canonical Luke the testimony is \"to them\" (the priests); in this text it is \"for you\" (the man and his community), and it "
  "rests on doing what the Torah prescribes. Tertullian records the Marcionite explanation: Jesus, being kind and knowing the man "
  "would keep the law anyway, allowed it (Marc. 4.9.10). That is reception (METHOD §7): the community that read this text had to "
  "explain away its Torah observance, so the passage was not written to fit that community's theology. The observance is "
  "consistent with the library's thesis of a Torah-keeping Jewish community behind the text (Carriers of Living Water §3.4).")),
 dict(term='The paralysed man (5:17–26)', cat='textual', refs=['5:17', '5:18', '5:20', '5:21', '5:24', '5:26'], text=(
  "Tertullian, Marc. 4.10.1–14, and Epiphanius, sch. 2. Tertullian cites the scribes' objection (\"Who forgives sins but God "
  "alone?\") and the command \"Arise and take up your mat\". The Latin of 4.10.1 as transcribed on tertullian.org breaks off "
  "after \"tolle\"; Evans' English translation of the same edition reads \"Arise and take up thy bed\", and NA27 cites Marcion "
  "for τὸν κράβαττον. The reading ἔγειρε καὶ ἆρον τὸν κράβαττόν σου καὶ πορεύου is printed: ἆρον and καί with ℵ D 1424; "
  "κράβαττον with D 1424 and the Old Latin c r1. This is a retroversion from Latin; grabatum is the Latin form of κράβαττος, "
  "not of κλινίδιον. Epiphanius quotes 5:24a in the order of Mark and Matthew; Roth marks the order uncertain, and NA27's order "
  "is kept. 5:18 includes NA27's bracketed [αὐτόν]. 5:19, 5:22–23 and 5:25 are not cited and are printed in grey.")),
 dict(term='The son of man', cat='translation', refs=['5:24'], text=(
  "ὁ υἱὸς τοῦ ἀνθρώπου is rendered \"the son of man\" in lower case throughout. Tertullian (Marc. 4.10.13–14) reads it through "
  "Daniel; that is his argument, and the translation does not import it.")),
 dict(term='Levi and the question of fasting (5:27–38)', cat='textual', refs=['5:27', '5:30', '5:31', '5:33', '5:34', '5:35', '5:36', '5:37', '5:38'], text=(
  "Tertullian, Marc. 4.11.1–10: the tax collector chosen, the physician saying (\"medicum sanis non esse necessarium sed male "
  "habentibus\"), John's disciples who fast and pray, the bridegroom, and the patch and wineskins. 5:28–29 and 5:32 are not cited "
  "and are printed in grey. At 5:34 NA27 has ὁ Ἰησοῦς (SBLGNT omits it); Tertullian's \"non possent ieiunare filii sponsi\" "
  "agrees with ℵ* D it (δύνανται… νηστεύειν), which Roth rates possible, so it is noted, not printed. At 5:38 NA27 cites the "
  "Dialogue of Adamantius (McionA) for βάλλουσιν and \"both are preserved\"; Roth marks the attestation uncertain.")),
 dict(term='Absent: 5:39 ("the old is good")', cat='excision', refs=['5:38'], text=(
  "\"No one after drinking old wine wants new, for he says, The old is good.\" No witness cites it. Tertullian spends Marc. "
  "4.11.9–11 arguing that old and new come from one God, and the saying would have served that argument. It is classed "
  "\"unattested, probably absent\" and not printed. It is also absent from D and the Old Latin (NA27).")),
 dict(term='The sabbath disputes (6:1–11)', cat='textual', refs=['6:1', '6:3', '6:4', '6:5', '6:6', '6:7', '6:9'], text=(
  "Tertullian, Marc. 4.12.1–14; Epiphanius, sch. 21 (6:3–4) and sch. 3 (6:5). NA27 reads ὅτε at 6:3 (SBLGNT ὁπότε) and "
  "brackets [ὄντες] (6:3) and [ὡς] (6:4); the bracketed words are printed, because Epiphanius' quotation skips the clause "
  "rather than reading it without them. At 6:5 Epiphanius quotes »κύριός ἐστιν ὁ υἱὸς τοῦ ἀνθρώπου καὶ τοῦ σαββάτου«; this "
  "is the reading of A D L Θ Ψ and the Byzantine text, cited in NA27 for Marcion (McionE), and is printed. D places 6:5 after "
  "6:10; Roth leaves the position open, and the canonical position is kept. At 6:9 NA27 cites Marcion for its own text "
  "(εἰ ἔξεστιν; ἀπολέσαι). 6:8 is cited only in a passage of Adamantius whose link to Marcion's text Roth marks uncertain; it "
  "is printed in grey with 6:10–11.")),
 dict(term='Lord of the sabbath', cat='theological', refs=['6:5', '6:9'], text=(
  "Interpretation. The disputes are argued from inside the law: the precedent of David from scripture, and the question what the "
  "law permits on the sabbath (to do good, to save life). Tertullian reads \"lord of the sabbath\" as proof that Jesus belonged "
  "to the Creator (4.12.11); that is his polemic. On the text alone the sabbath is not set aside; its proper use is argued, as in "
  "other Jewish debates of the period.")),
]
