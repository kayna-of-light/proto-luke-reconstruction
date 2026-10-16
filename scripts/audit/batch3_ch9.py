"""Batch 3, chapter 9 of the reconstruction: Luke 11:1–54."""
from buildlib import greek
from batch1_ch2 import U, A
from batch3_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}
OR = lambda ev: {'source': 'Origen, fragment on Luke 11:3 (Rauer, GCS 35, 1930, p. 254, fr. XLVI; 2nd ed. fr. 180)', 'evidence': ev}
AD = lambda loc, ev: {'source': f'Dialogue of Adamantius {loc} (via Roth)', 'evidence': ev}

ENTRIES = [
 A('11:1', G('11:1'), 'And it happened, while he was praying in a certain place, that when he stopped, one of his learners said to him, "Lord, teach us to pray, just as John also taught his learners."',
   'present (Marc. 4.26.1)', [T('4.26.1', '"Cum in quodam loco orasset… aggressus eum ex discipulis quidam, Domine, inquit, doce nos orare, sicut et Ioannes discipulos suos docuit."')]),
 A('11:2', G('11:2', [('Πάτερ, ἁγιασθήτω τὸ ὄνομά σου·', 'Πάτερ, ἐλθέτω τὸ πνεῦμά σου τὸ ἅγιον·')]),
   'And he said to them, "When you pray, say: Father, let your holy spirit come; let your kingdom come.',
   'present (Marc. 4.26.3–5)',
   [T('4.26.3', '"Cui dicam, Pater?"'),
    T('4.26.4', '"A quo spiritum sanctum postulem?… Eius regnum optabo venire…"'),
    T('4.26.5', '"Hoc ordine qui alii deo supplicat…" — Tertullian has gone through the petitions in their order: Father, holy spirit, kingdom, bread, sins, temptation.')],
   wording=('Marcionite reading adopted in substance: a petition for the holy spirit stands where NA27 has "hallowed be your name". Tertullian turns each petition into a question, in the order of the prayer; the second question is "From whom shall I ask the holy spirit?", and there is none about the name. Roth: the holy spirit very likely, and "some sort of request for the Spirit in place of the first petition". NA27 itself cites Marcion (McionT, in parentheses: with differences) for the petition for the Spirit, which in 700 (162) and Gregory of Nyssa reads ἐλθέτω τὸ πνεῦμά σου τὸ ἅγιον ἐφ\' ἡμᾶς καὶ καθαρισάτω ἡμᾶς and replaces "your kingdom come". '
            'Tertullian does not give the wording. The Greek printed takes the verb and word order of that manuscript form and only the elements Tertullian attests ("your holy spirit"); ἐφ\' ἡμᾶς καὶ καθαρισάτω ἡμᾶς is not attested for this text and is not printed. Unlike the manuscripts, this text keeps "your kingdom come" (Tertullian: "regnum optabo venire"). '
            'The address is "Father" alone; NA27 cites McionT and Origen with 𝔓75 ℵ B for the text without "our, who art in heaven".')),
 A('11:3', G('11:3', [('τὸν ἄρτον ἡμῶν', 'τὸν ἄρτον σου')]),
   'Your bread for the coming day keep giving us day by day.',
   'present (Marc. 4.26.4; Origen, fragment on Luke 11:3)',
   [OR('Ἐπεὶ δὲ οἱ ἀπὸ Μαρκίωνος ἔχουσι τὴν λέξιν οὕτως· »τὸν ἄρτον σου τὸν ἐπιούσιον δίδου ἡμῖν τὸ καθ\' ἡμέραν«… τίς ἐστιν ὁ ἄρτος τοῦ θεοῦ; (read in the 1930 edition)'),
    T('4.26.4', '"Quis dabit mihi panem cotidianum?… qui etiam de caelo panem angelorum cotidianum populo suo praestitit?"')],
   wording='Marcionite reading adopted: τὸν ἄρτον σου ("your bread") for τὸν ἄρτον ἡμῶν. Origen quotes the Marcionites\' wording in Greek and asks them "what is the bread of God?"; Tertullian\'s question agrees in the rest. Roth: very likely. NA27 apparatus: σου McionOr. For ἐπιούσιος see the note.'),
 A('11:4', G('11:4'), 'And let go our sins for us, for we ourselves also let go for everyone who owes us. And do not bring us into testing."',
   'present (Marc. 4.26.4–5)', [T('4.26.4–5', '"Quis mihi delicta dimittet?… Quis non sinet nos deduci in temptationem?"')],
   wording=('NA27. Tertullian\'s question "Who will not let us be led into temptation?" was long taken (Harnack) as a Marcionite reading μὴ ἄφες ἡμᾶς εἰσενεχθῆναι. Roth rates it possible only: Tertullian turns every petition into a question, and he glosses the canonical "lead us not" the same way in his own works: "ne nos patiaris induci" (Or. 8.1); cf. Fug. 2.5, "ne nos induxeris in temptationem permittendo nos maligno". Not adopted. '
            'The clause "for we ourselves also let go…" is not cited. NA27 cites McionT and Origen for the text without "but deliver us from evil".')),
 A('11:5', G('11:5'), 'And he said to them, "Which of you will have a friend, and will go to him at midnight and say to him, \'Friend, lend me three loaves,',
   'present (Marc. 4.26.8; Pan. 42.11.6, sch. 24)',
   [E(24, '»τίς ἐξ ὑμῶν ἕξει φίλον, καὶ πορεύσεται πρὸς αὐτὸν μεσονυκτίου, αἰτῶν τρεῖς ἄρτους;«'),
    T('4.26.8', '"Sic et praemissa similitudo nocturnum panis petitorem amicum facit…"')],
   wording='NA27. Epiphanius summarizes the end of the verse ("asking for three loaves"); Roth: abbreviation.'),
 U('11:6', G('11:6'), "since a friend of mine has arrived to me from a journey, and I have nothing to set before him';", 'Inside the attested parable 11:5–8.'),
 A('11:7', G('11:7'), "and that one, answering from inside, will say, 'Do not give me trouble; the door has already been shut, and my children are with me in bed; I cannot get up and give to you'?",
   'present (Marc. 4.26.8)', [T('4.26.8', '"cubantem iam cum infantibus quos nasci voluerat… cuius ianuam norat".')]),
 A('11:8', G('11:8'), 'I tell you, even if he will not get up and give to him because he is his friend, yet because of his shamelessness he will rouse himself and give him as much as he needs.',
   'present (Marc. 4.26.9)', [T('4.26.9', '"is et exsurgit et dat, etsi iam non quasi amico… sed quasi molesto, inquit".')]),
 A('11:9', G('11:9'), 'And I say to you: ask, and it will be given to you; seek, and you will find; knock, and it will be opened to you.',
   'present (Marc. 4.26.5–6; Pan. 42.11.6, sch. 24)',
   [E(24, 'καὶ λοιπόν »αἰτεῖτε καὶ δοθήσεται«.'),
    T('4.26.5', '"Proinde a quo petam ut accipiam? apud quem quaeram ut inveniam? ad quem pulsabo ut aperiatur mihi?"')]),
 U('11:10', G('11:10'), 'For everyone who asks receives, and the one who seeks finds, and to the one who knocks it will be opened.', 'Inside the attested passage 11:9–13.'),
 A('11:11', G('11:11'), 'And which of you who is a father, if the son asks for a fish, will instead of a fish hand him a snake?',
   'present (Marc. 4.26.10; Pan. 42.11.6, sch. 24; Adam. 110,3–4)',
   [E(24, '»τίνα γὰρ ἐξ ὑμῶν τὸν πατέρα υἱὸς αἰτήσει ἰχθὺν καὶ ἀντὶ ἰχθύος ὄφιν ἐπιδώσει αὐτῷ«'),
    T('4.26.9', '"non serpentem pro pisce, nec scorpium pro ovo".')],
   wording='NA27. Epiphanius has γάρ and the order υἱὸς αἰτήσει (both found in 𝔓45); Roth: order uncertain, γάρ possible. Neither witness has the "bread and stone" pair that most manuscripts add here (NA27 cites McionE with 𝔓45.75 B for its absence).'),
 A('11:12', G('11:12'), 'Or if he asks for an egg, will hand him a scorpion?',
   'present (Marc. 4.26.10; Pan. 42.11.6, sch. 24; Adam. 110,4–5)', [E(24, '»ἢ ἀντὶ ᾠοῦ σκορπίον;«')]),
 A('11:13', G('11:13'), 'If you then, being evil, know how to give good gifts to your children, how much more will the Father who is from heaven give holy spirit to those who ask him!"',
   'present (Marc. 4.26.10; Pan. 42.11.6, sch. 24; Adam. 110,5–6)',
   [E(24, '»εἰ οὖν ὑμεῖς πονηροὶ οἴδατε δόματα ἀγαθά, πόσῳ μᾶλλον ὁ πατήρ;«'),
    T('4.26.10', '"Itaque et spiritum sanctum is dabit apud quem est et non sanctus."')],
   wording='NA27, with its bracketed [ὁ] before ἐξ οὐρανοῦ. Epiphanius\' quotation stops at "the Father"; Tertullian attests "will give the holy spirit".'),
 A('11:14', G('11:14'), 'And he was throwing out a daimon, and it was mute; and it happened, when the daimon had gone out, that the mute man spoke; and the crowds marvelled.',
   'present (Marc. 4.26.11)', [T('4.26.10', '"Cum surdum daemonium expulisset…"')],
   wording='NA27, including its bracketed [καὶ αὐτὸ ἦν] ("and it was"), which SBLGNT omits (checked on the page image). Tertullian\'s narrative summary does not show whether the words stood.'),
 A('11:15', G('11:15'), 'But some of them said, "By Beelzebul, the ruler of the daimons, he throws out the daimons."',
   'present (Marc. 4.26.11; 4.28.2)', [T('4.26.10', '"in Beelzebub dictus eicere daemonia".')]),
 U('11:16', G('11:16'), 'And others, testing him, were seeking from him a sign out of heaven.', 'Inside the attested paragraph 11:14–23.'),
 U('11:17', G('11:17'), 'But he, knowing their thoughts, said to them, "Every kingdom divided against itself is laid waste, and house falls upon house.', 'Inside the attested paragraph 11:14–23.'),
 A('11:18', G('11:18'), 'And if Satan too has been divided against himself, how will his kingdom stand? Because you say that I throw out the daimons by Beelzebul.',
   'present (Marc. 4.26.11)', [T('4.26.11', '"resistet tibi prior sensus, non posse satanam dividi adversus semetipsum".')]),
 A('11:19', G('11:19'), 'But if I throw out the daimons by Beelzebul, your sons, by whom do they throw them out? Therefore they will be your judges.',
   'present (Marc. 4.26.11)', [T('4.26.10', '"Si ego, inquit, in Beelzebub eicio daemonia, filii vestri in quo eiciunt?"')]),
 A('11:20', G('11:20'), 'But if I throw out the daimons by the finger of God, then the kingdom of God has arrived upon you.',
   'present (Marc. 4.26.11)', [T('4.26.11', '"Quodsi ego in digito dei expello daemonia, ergone appropinquavit in vos regnum dei?"')],
   wording='NA27, including its bracketed [ἐγώ] ("I"), which SBLGNT omits (checked on the page image); Tertullian has "ego". His "appropinquavit" (ἤγγικεν?) for ἔφθασεν is rated possible only; not adopted.'),
 A('11:21', G('11:21'), 'When the strong one, fully armed, guards his own courtyard, his possessions are in peace;',
   'present (Marc. 4.26.12)', [T('4.26.12', '"applicuit ad parabolam fortis illius armati…"')]),
 A('11:22', G('11:22'), 'but when one stronger than he comes upon him and conquers him, he takes away his full armour, on which he had relied, and distributes his spoils.',
   'present (Marc. 4.26.12)', [T('4.26.12', '"quem validior alius oppressit".')]),
 U('11:23', G('11:23'), 'The one who is not with me is against me, and the one who does not gather with me scatters."', 'Inside the attested paragraph 11:14–23.'),
 A('11:27', G('11:27'), 'And it happened, as he was saying these things, that a certain woman from the crowd, raising her voice, said to him, "Fortunate is the womb that carried you, and the breasts that you sucked!"',
   'present (Marc. 4.26.13; 3.11.3; Ephrem, Comm. Diat. 11.9)',
   [T('4.26.13', '"Exclamat mulier de turba beatum uterum qui illum portasset, et ubera quae illum educassent."')]),
 A('11:28', G('11:28'), 'But he said, "Rather, fortunate are those who hear the word of God and keep it."',
   'present (Marc. 4.26.13)', [T('4.26.13', '"Et dominus, Immo beati qui sermonem dei audiunt et faciunt".')],
   wording='NA27. Tertullian has "and do it" (ποιοῦντες?) for "and keep it"; Roth: possible only, since Tertullian links the saying at once to 8:21 ("hear and do"). Not adopted.'),
 A('11:29', G('11:29', [('σημεῖον οὐ δοθήσεται αὐτῇ εἰ μὴ τὸ σημεῖον Ἰωνᾶ.', 'σημεῖον οὐ δοθήσεται αὐτῇ.')]),
   'And as the crowds were gathering thickly, he began to say, "This generation is an evil generation; it seeks a sign, and a sign will not be given to it."',
   'present without the Jonah clause (Marc. 4.27.1; Pan. 42.11.6, sch. 25)',
   [E(25, 'παρέκοπτε τὸ περὶ Ἰωνᾶ τοῦ προφήτου. εἶχεν γὰρ »ἡ γενεὰ αὕτη, σημεῖον οὐ δοθήσεται αὐτῇ«. οὐκ εἶχεν δὲ περὶ Νινευὴ καὶ βασιλίσσης νότου καὶ Σαλομῶνος.'),
    T('4.27.1', '"iubet omni petenti dare, et ipse signum petentibus non dat".')],
   wording=('Attested omission: εἰ μὴ τὸ σημεῖον Ἰωνᾶ ("except the sign of Jonah") is not printed. Epiphanius says the text lacked "what is about Jonah the prophet", "for it had \'this generation — a sign will not be given to it\'"; his quotation ends there in the scholion and again in his refutation. Tertullian says that Christ "does not give a sign" to those who ask, with no exception. '
            'The words between "this generation" and "no sign" are not quoted by either witness; Roth takes Epiphanius\' quotation as abbreviated there, and they are printed in the NA27 wording.')),
 A('11:33', G('11:33'), '"No one, having lit a lamp, puts it in a hidden place, nor under the measuring basket, but on the lampstand, so that those who come in may see the light."',
   'present (Marc. 4.27.1)', [T('4.27.1', '"negat lucernam abstrudendam, sed confirmat super candelabrum proponendam, ut omnibus luceat".')],
   wording='NA27 (τὸ φῶς; SBLGNT τὸ φέγγος — checked on the page image), including its bracketed [οὐδὲ ὑπὸ τὸν μόδιον]. Tertullian\'s "so that it may shine for all" is the wording of Matthew 5:15, which he quotes elsewhere (Praescr. 26.4); Roth: possible only.'),
 A('11:37', G('11:37'), 'And as he was speaking, a Pharisee asks him to have the midday meal with him; and going in, he reclined at table.',
   'present (Marc. 4.27.2)', [T('4.27.2', '"pharisaeus, qui illum vocarat ad prandium… quam recubuisset".')]),
 A('11:38', greek('11:38', text='ὁ δὲ Φαρισαῖος ἤρξατο διακρινόμενος ἐν ἑαυτῷ λέγειν διὰ τί οὐ πρῶτον ἐβαπτίσθη πρὸ τοῦ ἀρίστου.'),
   'And the Pharisee began, debating within himself, to say: why was he not first washed before the meal?',
   'present (Marc. 4.27.2)', [T('4.27.2', '"retractabat penes se cur non prius tinctus esset quam recubuisset, secundum legem".')],
   wording=('Marcionite reading adopted (retroversion): the Pharisee debating within himself why Jesus had not washed, for NA27\'s "was amazed, seeing that he had not first washed". Tertullian\'s Latin cannot render NA27\'s ἰδὼν ἐθαύμασεν. The Greek printed is that of codex D, whose reading Tertullian matches (NA27 apparatus: ἤρξατο διακρινόμενος ἐν ἑαυτῷ λέγειν διὰ τί D (pc) lat syc; (McionT)). '
            'Roth rates "debating within himself" and "why… not first washed" very likely; ἤρξατο and λέγειν are possible only, and the Old Latin has the words in a different order.'),
   western='The reading of D, the Old Latin and the Old Syriac (syc).'),
 A('11:39', G('11:39'), 'But the lord said to him, "Now you, the Pharisees, cleanse the outside of the cup and of the platter, but your inside is full of plunder and evil.',
   'present (Marc. 4.27.2, 6)', [T('4.27.2', '"dicens illos calicis et catini exteriora emundare, interiora autem ipsorum plena esse rapina et iniquitate".')]),
 A('11:40', G('11:40'), 'Senseless ones! Did not the one who made the outside also make the inside?',
   'present (Marc. 4.27.2)', [T('4.27.2', '"Nonne qui exteriora fecit, id est carnem, et interiora fecit, id est animam?"')]),
 A('11:41', G('11:41'), 'But give what is inside as a gift of mercy, and look, all things are clean for you.',
   'present (Marc. 4.27.3, 6)', [T('4.27.3', '"Date quae habetis eleemosynam, et omnia munda erunt vobis."')],
   wording='NA27. Tertullian\'s "erunt" (ἔσται, the reading of 𝔓45 and D) and "quae habetis" are rated possible only by Roth; not adopted.'),
 A('11:42', G('11:42', [('παρέρχεσθε τὴν κρίσιν', 'παρέρχεσθε τὴν κλῆσιν')]),
   'But woe to you, the Pharisees, because you take a tenth of the mint and the rue and every garden herb, and pass by the calling and the love of God. But these you ought to have done, and not to have let the others go.',
   'present (Marc. 4.27.4, 6; Pan. 42.11.6, sch. 26)',
   [E(26, 'ἀντὶ τοῦ »παρέρχεσθε τὴν κρίσιν τοῦ θεοῦ« εἶχε »παρέρχεσθε τὴν κλῆσιν τοῦ θεοῦ«.'),
    T('4.27.4', '"Sic et holuscula decimantes, vocationem autem et dilectionem dei praetereuntes obiurgat. Cuius dei vocationem et dilectionem…?"'),
    T('4.27.6', '"eleemosynam et vocationem et dilectionem dei".')],
   wording='Marcionite reading adopted: τὴν κλῆσιν ("the calling") for τὴν κρίσιν ("justice"). Epiphanius states the difference; Tertullian has vocationem twice. Roth: very likely (the reading is otherwise unattested in the manuscripts). The final clause ("these you ought to have done…") is not cited by either witness; it is lacking in D. It is printed.'),
 A('11:43', G('11:43'), 'Woe to you, the Pharisees, because you love the first seat in the assemblies and the greetings in the marketplaces.',
   'present (Marc. 4.27.5)', [T('4.27.5', '"Primatum quoque captantes locorum et honorem salutationum cum incusat".')]),
 U('11:44', G('11:44'), 'Woe to you, because you are like the tombs that are not seen, and the people walking over them do not know it."', 'Inside the attested paragraph 11:37–44.'),
 U('11:45', G('11:45'), 'And one of the experts in the law answers and says to him, "Teacher, saying these things you insult us too."', 'Inside the attested paragraph 11:45–52.'),
 A('11:46', G('11:46'), 'But he said, "Woe to you, the experts in the law, too, because you load the people with loads hard to carry, and you yourselves do not touch the loads with one of your fingers.',
   'present (Marc. 4.27.6)', [T('4.27.6', '"Invehitur et in doctores ipsos legis, quod onerarent alios importabilibus oneribus, quae ipsi ne digito quidem aggredi auderent".')]),
 A('11:47', G('11:47'), 'Woe to you, because you build the tombs of the prophets, but your fathers killed them.',
   'present (Marc. 4.27.8; Pan. 42.11.6, sch. 27)',
   [E(27, '»οὐαὶ ὑμῖν, ὅτι οἰκοδομεῖτε τὰ μνήματα τῶν προφητῶν καὶ οἱ πατέρες ὑμῶν ἀπέκτειναν αὐτούς«.'),
    T('4.27.8', '"Cur autem Vae audiunt etiam quod aedificarent prophetis monimenta interemptis a patribus eorum…"')],
   wording='NA27. Epiphanius has τὰ μνήματα and καὶ οἱ for τὰ μνημεῖα and οἱ δέ; in his other quotation (33.10.4) he has τὰ μνημεῖα. Roth: possible only.'),
 A('11:48', G('11:48'), 'So you are witnesses, and consent to the works of your fathers, because they killed them, and you build.',
   'present (Marc. 4.27.8)', [T('4.27.8', '"laude potius digni, qui ex isto opere pietatis testabantur se non consentire factis patrum".')],
   wording=('NA27. Tertullian\'s comment, that the builders "testified that they did not consent to the deeds of their fathers", matches the reading of D, μαρτυρεῖτε μὴ συνευδοκεῖν ("you testify that you do not approve"), and NA27 cites McionT for μὴ συνευδοκεῖν. But the words stand in Tertullian\'s own argument, not in a quotation, and Roth rates the reading probable only. Not adopted; recorded.'),
   western='D (it) read "you testify that you do not approve".'),
 A('11:52', G('11:52'), 'Woe to you, the experts in the law, because you took away the key of knowledge; you yourselves did not go in, and those going in you hindered."',
   'present (Marc. 4.27.9; 4.28.2)', [T('4.27.9', '"Quam vero clavem habebant legis doctores nisi interpretationem legis? ad cuius intellectum neque ipsi adibant… neque alios admittebant".'),
                                       T('4.28.2', '"quae clavem agnitionis habens nec ipsa introiret nec alios sineret".')]),
]

OMITTED = [
 dict(ref='11:24–26', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='The return of the unclean spirit. A separate NA27 paragraph with no attested verse (METHOD §4.3). Tertullian passes from 11:22 (4.26.12) to 11:27 (4.26.13).')),
 dict(ref='11:30–32', cls='A−', app=dict(roth='absent', witnesses=[
      E(25, 'παρέκοπτε τὸ περὶ Ἰωνᾶ τοῦ προφήτου… οὐκ εἶχεν δὲ περὶ Νινευὴ καὶ βασιλίσσης νότου καὶ Σαλομῶνος.')],
      decision='not printed', reason='Epiphanius states that the text did not have the sayings about Nineveh, the queen of the south and Solomon. Tertullian passes from 11:29 to 11:33 (4.27.1); Roth counts his silence as confirmation (tacitus).')),
 dict(ref='11:34–36', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='The lamp of the body. A separate NA27 paragraph with no attested verse (METHOD §4.3). Tertullian passes from 11:33 (4.27.1) to 11:37 (4.27.2).')),
 dict(ref='11:49–51', cls='A−', app=dict(roth='absent', witnesses=[
      E(28, 'οὐκ εἶχεν »διὰ τοῦτο εἶπεν ἡ σοφία τοῦ θεοῦ· ἀποστελῶ εἰς αὐτοὺς προφήτας« καὶ περὶ αἵματος Ζαχαρίου καὶ Ἄβελ καὶ τῶν προφητῶν ὅτι ἐκζητηθήσεται ἐκ τῆς γενεᾶς ταύτης.')],
      decision='not printed', reason='Epiphanius states that the text did not have the saying of "the wisdom of God" or the blood of the prophets from Abel to Zechariah required of this generation. Tertullian passes from 11:48 (4.27.8) to 11:52 (4.27.9).')),
 dict(ref='11:53–54', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='The scribes and Pharisees begin to press him hard. A separate NA27 paragraph with no attested verse (METHOD §4.3). Tertullian passes from 11:52 (4.27.9) to 12:1 (4.28.1).')),
]

PREAMBLE = (
 "It starts with asking how to ask. The prayer given here wants the spirit first, then the kingdom, then bread "
 "enough for the day, and it lets go of what is owed to us as readily as it asks to be let go.\n\n"
 "Asking turns out to be a matter of knocking at midnight on a door already shut for the night, and going on "
 "knocking without shame. And what answers is a father: it will not hand us a snake.\n\n"
 "Then something that has kept us mute goes out, and we speak, and at once part of us suspects the cure. A "
 "strong one guards its courtyard and all its goods are at peace, until a stronger one comes.\n\n"
 "The chapter ends at a table, before a cup polished on the outside. We clean what can be seen, count out our "
 "tenths of mint and rue, sit in the first seats, and keep hold of a key we never use.\n\n"
 "Whoever made the outside made the inside as well."
)

NOTES = [
 dict(term='The prayer (11:1–4)', cat='textual', refs=['11:1', '11:2', '11:3', '11:4'], text=(
  "Tertullian, Marc. 4.26.1–5 does not quote the prayer. He turns each petition into a question about which God it is "
  "addressed to, in the order of the prayer, and then says \"in this order\" (hoc ordine): \"To whom shall I say, Father?… "
  "From whom shall I ask the holy spirit?… Whose kingdom shall I wish to come?… Who will give me daily bread?… Who will "
  "forgive me my sins?… Who will not let us be led into temptation?\" There is no question about the hallowing of the name. "
  "The text therefore asked for the holy spirit where canonical Luke has \"hallowed be your name\", and kept \"your kingdom "
  "come\". Tertullian does not give the wording of the request for the spirit. The Greek printed takes the form of the only "
  "Greek witnesses with such a petition in Luke (minuscules 700 and 162, Gregory of Nyssa), shortened to what Tertullian "
  "attests. In those witnesses it replaces \"your kingdom come\"; here it stands beside it. Origen quotes the bread petition of "
  "\"those from Marcion\" in Greek: \"your bread\" (τὸν ἄρτον σου), not \"our bread\". He asks them \"what is the bread of "
  "God?\" ἐπιούσιος is translated \"for the coming day\"; Tertullian has \"daily\" (cotidianum).")),
 dict(term='The holy spirit asked and given (11:2, 11:13)', cat='theological', refs=['11:2', '11:13'], text=(
  "Interpretation. In this text the prayer opens with a request for the holy spirit, and the teaching that follows ends with "
  "the Father who will \"give holy spirit to those who ask him\" (11:13; Tertullian 4.26.10). The unit begins and ends with "
  "the spirit. The bread asked for is the Father's (\"your bread\"), and Origen's question to the Marcionites, \"what is the "
  "bread of God?\", shows that they read it as more than food. This is the reception, and the text does not settle that "
  "reading. What the text itself shows is a prayer centred on receiving from the Father. The library reads "
  "such receiving as influx into a vessel (The River and the Vessel).")),
 dict(term='Asking, seeking, knocking (11:5–13)', cat='textual', refs=['11:5', '11:7', '11:8', '11:9', '11:11', '11:12', '11:13'], text=(
  "Epiphanius, sch. 24 quotes 11:5, 11:9a and 11:11–13 in one scholion; Tertullian, Marc. 4.26.5–10 alludes to the friend at "
  "midnight, the door already shut with the children in bed, the request granted because of persistence, the asking, seeking "
  "and knocking, and the snake and scorpion. Neither witness has the pair \"bread and stone\" that most manuscripts add at 11:11 "
  "(it is also absent in 𝔓45, 𝔓75 and B). 11:6 and 11:10 are not cited and are printed in grey.")),
 dict(term='The finger of God (11:14–23)', cat='textual', refs=['11:14', '11:15', '11:18', '11:19', '11:20', '11:21', '11:22'], text=(
  "Tertullian, Marc. 4.26.10–12 quotes \"If I cast out daimons by Beelzebul, by whom do your sons cast them out?\" and \"If I by "
  "the finger of God cast out daimons, has the kingdom of God not come near to you?\" He points out that the Egyptian magicians "
  "called the Creator's power \"the finger of God\" (Exod 8:19), and that the stronger man of the parable overcomes the prince "
  "of daimons. NA27 prints [καὶ αὐτὸ ἦν] at 11:14 and [ἐγώ] at 11:20 in brackets; both are printed (SBLGNT omits them). 11:16–17 "
  "and 11:23 are not cited and are printed in grey. The return of the unclean spirit (11:24–26), a paragraph that no witness "
  "cites, is not printed.")),
 dict(term='No sign (11:29; 11:30–32 not printed)', cat='excision', refs=['11:29'], text=(
  "Epiphanius, sch. 25: \"he cut out what is about Jonah the prophet; for he had 'this generation — a sign will not be given to it'; "
  "he did not have what is about Nineveh and the queen of the south and Solomon.\" Tertullian: Christ \"does not give a sign to "
  "those who ask\" (4.27.1). The saying in this text ends \"a sign will not be given to it\". Canonical Luke adds \"except the sign "
  "of Jonah\" and the sayings on the Ninevites and the queen of the south (11:30–32, Matthew 12:39–42). The verbs \"he cut\" are "
  "Epiphanius' charge. What they report as content is that the words were not there.")),
 dict(term='At the Pharisee\'s table (11:37–44)', cat='textual', refs=['11:37', '11:38', '11:39', '11:40', '11:41', '11:42', '11:43', '11:44'], text=(
  "Tertullian, Marc. 4.27.2–5. The Pharisee \"was debating within himself why he had not first been washed before reclining, "
  "according to the law\". That is the reading of codex D and the Old Latin, and it is printed in D's Greek. Canonical Luke has "
  "the Pharisee \"amazed\". Jesus' reply on the outside and inside of the cup, \"Did not the one who made the outside also make the "
  "inside?\", is glossed by Tertullian as flesh and soul made by one God. At 11:42 both witnesses read that the Pharisees "
  "pass over \"the calling (κλῆσις) and the love of God\", not \"justice (κρίσις) and the love of God\"; Tertullian repeats "
  "\"calling\" in 4.27.6. The reading is printed. 11:44 is not cited and is printed in grey.")),
 dict(term='Woes on the experts in the law (11:45–52; 11:49–51 not printed)', cat='textual', refs=['11:45', '11:46', '11:47', '11:48', '11:52'], text=(
  "Tertullian, Marc. 4.27.6–9; Epiphanius, sch. 27–28. The experts in the law load others with burdens hard to bear; they build the tombs "
  "of the prophets their fathers killed; they have taken the key of knowledge (Tertullian: \"the interpretation of the law\"). "
  "Epiphanius states that the text did not have the saying \"Therefore the wisdom of God said, 'I will send them prophets…'\" or "
  "the blood of the prophets from Abel to Zechariah \"required of this generation\" (11:49–51). At 11:48 Tertullian's comment "
  "(\"they testified that they did not consent to the deeds of their fathers\") agrees with the reading of D, \"you testify that "
  "you do not approve\"; it is not a quotation and is recorded, not adopted. 11:45 is not cited and is printed in grey. 11:53–54 "
  "form a paragraph that no witness cites and are not printed.")),
 dict(term='Calling and love', cat='theological', refs=['11:42'], text=(
  "Interpretation. In the attested text the charge against the Pharisees is that they tithe herbs and pass over \"the calling "
  "and the love of God\". Tertullian reads \"calling\" as God calling Israel out of Egypt and \"love\" as the first "
  "commandment (Deut 6:5), quoted in that form (4.27.4). The pairing fits the reconstruction's earlier sayings: the expert in the law is "
  "answered with the command to love God (10:27). It also fits a criticism of religious leaders made from within the law, "
  "for neglecting what the law puts first.")),
 dict(term='Κύριε, "Lord"', cat='translation', refs=['11:1'], text='"Lord, sir": the capital is only the start of the address.'),
 dict(term='Πάτερ, "Father"', cat='translation', refs=['11:2'], text='The address, without "our" and without "who are in the heavens".'),
 dict(term='ἐλθέτω τὸ πνεῦμά σου τὸ ἅγιον, "let your holy spirit come"', cat='translation', refs=['11:2'], text='The petition of this text, in place of canonical Luke\'s "let your name be held holy". Its exact wording is not given by the witnesses. Manuscript 700 and Gregory of Nyssa read it with "upon us, and let it cleanse us"; those words are not printed and are not translated.'),
 dict(term='ἐλθέτω, "let… come"', cat='translation', refs=['11:2'], text='A third-person imperative: "let it come". "May it come" softens it into a wish.'),
 dict(term='τὸν ἄρτον σου, "your bread"', cat='translation', refs=['11:3'], text='The reading of this text, "your" (God\'s) bread. Canonical Luke has "our bread".'),
 dict(term='τὸν ἐπιούσιον, "for the coming day"', cat='translation', refs=['11:3'], text='The word occurs almost nowhere outside this prayer, and its meaning is not known for certain. Proposals: "for the coming day" (from ἡ ἐπιοῦσα, "the next day"), "needed for existence" (from οὐσία, "being"), and "supersubstantial", the Latin of Jerome. The first fits "day by day" and is the most likely; the others are possible.'),
 dict(term='δίδου… τὸ καθ\' ἡμέραν, "keep giving… day by day"', cat='translation', refs=['11:3'], text='A present imperative: give, and go on giving.'),
 dict(term='ἄφες… ἀφίομεν, "let go… we let go"', cat='translation', refs=['11:4'], text="ἀφίημι, as at 5:20. One verb for both: God's letting go and ours."),
 dict(term='παντὶ ὀφείλοντι ἡμῖν, "everyone who owes us"', cat='translation', refs=['11:4'], text="A debtor. The prayer's own image is of debts released."),
 dict(term='πειρασμόν, "testing"', cat='translation', refs=['11:4'], text='πειρασμός is a test, a trial, a putting to the proof. "Temptation", an enticement to sin, is one kind of testing.'),
 dict(term='χρῆσον, "lend"', cat='translation', refs=['11:5'], text='To lend.'),
 dict(term='κόπους, "trouble"', cat='translation', refs=['11:7'], text='Labour, bother.'),
 dict(term='ἀναίδειαν, "shamelessness"', cat='translation', refs=['11:8'], text='ἀναίδεια means shamelessness, a lack of shame. "Persistence" is not what the word means. Whose shamelessness is not quite clear: most read it as the asker\'s, some as the sleeper\'s wish to avoid shame.'),
 dict(term='ἀναστάς… ἐγερθείς, "get up… rouse himself"', cat='translation', refs=['11:8'], text='ἀνίστημι and ἐγείρω, both in one sentence.'),
 dict(term='αἰτεῖτε… ζητεῖτε… κρούετε, "ask… seek… knock"', cat='translation', refs=['11:9'], text='Present imperatives: keep asking, keep seeking, keep knocking.'),
 dict(term='τίνα… τὸν πατέρα, "which of you who is a father"', cat='translation', refs=['11:11'], text='The Greek is loose: "which of you, the father, will the son ask…".'),
 dict(term='πονηροὶ ὑπάρχοντες, "being evil"', cat='translation', refs=['11:13'], text='πονηρός, as at 6:45.'),
 dict(term='ὁ πατὴρ ὁ ἐξ οὐρανοῦ, "the Father who is from heaven"', cat='translation', refs=['11:13'], text='ἐξ, "out of, from".'),
 dict(term='πνεῦμα ἅγιον, "holy spirit"', cat='translation', refs=['11:13'], text='Without the article: "holy spirit", not "the Holy Spirit".'),
 dict(term='κωφόν, "mute"', cat='translation', refs=['11:14'], text='κωφός means both deaf and mute; here, mute.'),
 dict(term='Βεελζεβούλ, "Beelzebul"', cat='translation', refs=['11:15'], text='A Semitic name, probably "lord of the dwelling" or "lord of the height".'),
 dict(term='ἄρχοντι, "ruler"', cat='translation', refs=['11:15'], text='ἄρχων, as at 8:41.'),
 dict(term='ἐρημοῦται, "is laid waste"', cat='translation', refs=['11:17'], text='Made a desert (ἔρημος).'),
 dict(term='ὁ Σατανᾶς, "Satan"', cat='translation', refs=['11:18'], text='A Hebrew word, "the adversary", left untranslated in the Greek and here.'),
 dict(term='ἔφθασεν, "has arrived"', cat='translation', refs=['11:20'], text='φθάνω, to come before, reach, arrive.'),
 dict(term='αὐλήν, "courtyard"', cat='translation', refs=['11:21'], text='The enclosed court of a house.'),
 dict(term='ἐν εἰρήνῃ, "in peace"', cat='translation', refs=['11:21'], text='Undisturbed.'),
 dict(term='ἐπεποίθει, "had relied"', cat='translation', refs=['11:22'], text='πείθω in the perfect, "to be persuaded, rely on". Not πίστις, "trust".'),
 dict(term='σκῦλα, "spoils"', cat='translation', refs=['11:22'], text='Arms stripped from a defeated enemy.'),
 dict(term='Μακαρία, "fortunate"', cat='translation', refs=['11:27'], text='As at 6:20.'),
 dict(term='κοιλία, "womb"', cat='translation', refs=['11:27'], text='Literally the belly, the womb.'),
 dict(term='Μενοῦν, "rather"', cat='translation', refs=['11:28'], text='It corrects or strengthens what was said: "rather", "yes, but".'),
 dict(term='φυλάσσοντες, "keep"', cat='translation', refs=['11:28'], text='To guard, keep watch over.'),
 dict(term='σημεῖον οὐ δοθήσεται αὐτῇ, "a sign will not be given to it"', cat='translation', refs=['11:29'], text='The reading of this text, without "except the sign of Jonah".'),
 dict(term='κρύπτην, "a hidden place"', cat='translation', refs=['11:33'], text='A cellar or vault.'),
 dict(term='τὸν μόδιον, "the measuring basket"', cat='translation', refs=['11:33'], text='A grain measure.'),
 dict(term='ἐρωτᾷ, "asks"', cat='translation', refs=['11:37'], text='The present tense in past narration, kept.'),
 dict(term='ἀριστήσῃ, "have the midday meal"', cat='translation', refs=['11:37'], text='ἄριστον, the first meal of the day, taken toward noon.'),
 dict(term='διακρινόμενος ἐν ἑαυτῷ, "debating within himself"', cat='translation', refs=['11:38'], text="The reading of this text, with D's Greek."),
 dict(term='ἐβαπτίσθη, "was washed"', cat='translation', refs=['11:38'], text='βαπτίζω, to dip, immerse: a ritual washing before the meal. It is the verb behind "baptiser" (7:20).'),
 dict(term='ὁ κύριος, "the lord"', cat='translation', refs=['11:39'], text='As at 7:13.'),
 dict(term='πίνακος, "platter"', cat='translation', refs=['11:39'], text='A dish, a board for food.'),
 dict(term='ἁρπαγῆς, "plunder"', cat='translation', refs=['11:39'], text='Robbery, what is seized. "Greed" weakens it.'),
 dict(term='ἄφρονες, "senseless ones"', cat='translation', refs=['11:40'], text='Without sense, foolish.'),
 dict(term='τὰ ἐνόντα, "what is inside"', cat='translation', refs=['11:41'], text='The contents, what is within.'),
 dict(term='ἐλεημοσύνην, "a gift of mercy"', cat='translation', refs=['11:41'], text='From ἔλεος, mercy: alms.'),
 dict(term='ἀποδεκατοῦτε, "you take a tenth"', cat='translation', refs=['11:42'], text='You tithe.'),
 dict(term='τὴν κλῆσιν, "the calling"', cat='translation', refs=['11:42'], text='The reading of this text. Canonical Luke has τὴν κρίσιν, "justice, judgement".'),
 dict(term='παρεῖναι, "to have let go"', cat='translation', refs=['11:42'], text='παρίημι, to let pass, neglect.'),
 dict(term='πρωτοκαθεδρίαν, "first seat"', cat='translation', refs=['11:43'], text='The seat of honour.'),
 dict(term='τὰ ἄδηλα, "that are not seen"', cat='translation', refs=['11:44'], text='Unmarked, invisible. Contact with a tomb made a person unclean.'),
 dict(term='λέγει, "says"', cat='translation', refs=['11:45'], text='The present tense in past narration, kept.'),
 dict(term='ὑβρίζεις, "insult"', cat='translation', refs=['11:45'], text='To treat with outrage.'),
 dict(term='φορτίζετε… φορτία, "load… loads"', cat='translation', refs=['11:46'], text='One root, kept as one English word.'),
 dict(term='δυσβάστακτα, "hard to carry"', cat='translation', refs=['11:46'], text='Difficult to bear.'),
 dict(term='συνευδοκεῖτε, "consent to"', cat='translation', refs=['11:48'], text='To approve together with.'),
 dict(term='κλεῖδα τῆς γνώσεως, "the key of knowledge"', cat='translation', refs=['11:52'], text='γνῶσις, knowledge.'),
 dict(term='ἐκωλύσατε, "hindered"', cat='translation', refs=['11:52'], text='To prevent, hold back.'),
]
