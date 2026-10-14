"""Batch 3, chapter 10 of the reconstruction: Luke 12:1–59."""
from buildlib import greek
from batch1_ch2 import U, A
from batch3_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}

ENTRIES = [
 A('12:1', G('12:1'), 'Meanwhile, when the tens of thousands of the crowd had gathered together, so that they were trampling one another, he began to say to his learners first, "Keep yourselves away from the leaven of the Pharisees, which is play-acting.',
   'present (Marc. 4.28.1)', [T('4.28.1', '"Cavete, inquit discipulis, a fermento pharisaeorum, quod est hypocrisis".')],
   wording='NA27. Tertullian has "of the Pharisees" before "which is hypocrisy", the order of 𝔓45 ℵ A C D W and the Byzantine text (NA27 cites McionT and Epiphanius for it). Roth: the order is uncertain, since Matt 16:6 and Mark 8:15 have the same phrase; not adopted.'),
 A('12:2', G('12:2'), 'And nothing is covered over that will not be uncovered, and hidden that will not be known.',
   'present (Marc. 4.28.2)', [T('4.28.2', '"ideo adicit, Nihil autem opertum, quod non patefiet, et nihil absconditum, quod non dinoscetur".')]),
 A('12:3', G('12:3'), 'Because of this, whatever you said in the darkness will be heard in the light, and what you spoke into the ear in the inner rooms will be proclaimed upon the roofs.',
   'present (Marc. 4.28.2)', [T('4.28.2', '"cum subiciat etiam quae inter se mussitarent vel tractarent… in apertum processura, et in ore hominum futura".')]),
 A('12:4', G('12:4'), 'And I say to you, my friends, do not be afraid of those who kill the body and after these things have nothing more they can do.',
   'present (Marc. 4.28.3–4; Pan. 42.11.6, sch. 29)',
   [E(29, '»λέγω τοῖς φίλοις μου· μὴ φοβηθῆτε ἀπὸ τῶν ἀποκτενόντων τὸ σῶμα…«'),
    T('4.28.3', '"Dico autem, inquit, vobis amicis, nolite terreri ab eis qui vos solummodo occidere possunt, nec post hoc ullam in vobis habent potestatem."')],
   wording='NA27. Epiphanius spells ἀποκτενόντων; NA27 prints ἀποκτεινόντων (spelling).'),
 A('12:5', G('12:5', [('ἔχοντα ἐξουσίαν ἐμβαλεῖν εἰς τὴν γέενναν', 'ἔχοντα ἐξουσίαν βαλεῖν εἰς γέενναν')]),
   'But I will show you whom you should fear: fear the one who, after killing, has authority to throw into Gehenna. Yes, I tell you, fear this one.',
   'present (Marc. 4.28.3; Pan. 42.11.6, sch. 29)',
   [E(29, '»φοβήθητε δὲ τὸν μετὰ τὸ ἀποκτεῖναι ἔχοντα ἐξουσίαν βαλεῖν εἰς γέενναν«.'),
    T('4.28.3', '"Demonstrabo autem vobis quem timeatis: Timete eum qui postquam occiderit, potestatem habet mittendi in gehennam… Itaque dico vobis, hunc timete."')],
   wording='Marcionite reading adopted: βαλεῖν εἰς γέενναν ("to throw into Gehenna") for NA27 ἐμβαλεῖν εἰς τὴν γέενναν. Epiphanius\' Greek, with Tertullian\'s "mittendi in gehennam"; Roth: secure. NA27 apparatus: βαλεῖν 𝔓45 (D) W; McionT,E Clex Thd.'),
 A('12:8', G('12:8', [('ἔμπροσθεν τῶν ἀγγέλων τοῦ θεοῦ', 'ἔμπροσθεν τοῦ θεοῦ')]),
   'And I tell you, everyone who acknowledges me before the humans, the son of the human also will acknowledge him before God;',
   'present (Marc. 4.28.4; Pan. 42.11.6, sch. 30)',
   [E(30, 'ἀντὶ τοῦ »ὁμολογήσει ἐνώπιον τῶν ἀγγέλων τοῦ θεοῦ« »ἐνώπιον τοῦ θεοῦ« λέγει.'),
    T('4.28.4', '"Dico enim vobis, omnis qui confitebitur in me coram hominibus, confitebor in illo coram deo."')],
   wording='Marcionite reading adopted: "before God" without "the messengers of" (both witnesses; Roth: secure). NA27 apparatus: □ τῶν ἀγγέλων bis ℵ*; McionT,(E). Tertullian\'s first person "I will acknowledge" is Matthew\'s wording (Matt 10:32), which he uses elsewhere; Roth: possible only. NA27\'s ἔμπροσθεν is kept (Epiphanius\' ἐνώπιον may be his own).'),
 A('12:9', G('12:9', [('ἐνώπιον τῶν ἀγγέλων τοῦ θεοῦ', 'ἐνώπιον τοῦ θεοῦ')]),
   'but the one who disowns me before the humans will be disowned before God.',
   'present (Marc. 4.28.4)', [T('4.28.4', '"Et omnis qui negaverit me coram hominibus, denegabitur coram deo."')],
   wording='Marcionite reading adopted: "before God" without "the messengers of", as in 12:8 (Roth: secure; NA27 cites McionT for the omission in both verses). The two citations in the Dialogue of Adamantius give Matthew 10:33 and are no evidence here (Roth).'),
 A('12:10', G('12:10'), 'And everyone who will speak a word against the son of the human, it will be let go for him; but for the one who has blasphemed against the holy spirit, it will not be let go.',
   'present (Marc. 4.28.6)', [T('4.28.6', '"Qui dixerit in filium hominis, remittetur illi, qui autem dixerit in spiritum sanctum, non remittetur ei."')],
   wording='NA27. Tertullian has the same verb in both halves ("whoever speaks against the holy spirit"); Roth rates that form probable only. Not adopted.'),
 A('12:11', G('12:11'), 'And when they bring you in before the assemblies and the rulers and the authorities, do not be anxious how or what you should answer in defence, or what you should say;',
   'present (Marc. 4.28.7)', [T('4.28.7', '"Perductos ad potestates prohibet ad interrogationem cogitare de responsione".')]),
 A('12:12', G('12:12'), 'for the holy spirit will teach you in that very hour what you must say."',
   'present (Marc. 4.28.7–8)', [T('4.28.7', '"Sanctus enim, inquit, spiritus docebit vos ipsa hora quid eloqui debeatis."')]),
 A('12:13', G('12:13'), 'And someone from the crowd said to him, "Teacher, tell my brother to divide the inheritance with me."',
   'present (Marc. 4.28.9)', [T('4.28.9', '"Christus vero postulatus a quodam ut inter illum et fratrem ipsius de dividunda haereditate componeret…"')]),
 A('12:14', G('12:14'), 'But he said to him, "Human, who set me up as judge or divider over you?"',
   'present (Marc. 4.28.9–10)', [T('4.28.10', '"Quis me, inquit, iudicem constituit super vos?"')],
   wording='NA27. Tertullian has only "judge"; Roth notes that "or arbitrator" may not have stood. Not adopted (one witness, which shapes the saying after Exod 2:14).'),
 U('12:15', G('12:15'), 'And he said to them, "Look, and guard yourselves against every kind of wanting more, because a person\'s life is not in having more than enough of his possessions."', 'Inside the attested paragraph 12:13–15.'),
 A('12:16', G('12:16'), 'And he spoke a parable to them, saying, "The land of a certain rich man bore well.',
   'present (Marc. 4.28.11)', [T('4.28.11', '"parabola divitis blandientis sibi de proventu agrorum suorum".')]),
 U('12:17', G('12:17'), "And he was reasoning within himself, saying, 'What shall I do, because I have nowhere to gather my fruits?'", 'Inside the attested parable 12:16–21.'),
 U('12:18', G('12:18'), "And he said, 'This I will do: I will pull down my barns and build bigger ones, and I will gather there all my grain and my good things,", 'Inside the attested parable 12:16–21.'),
 A('12:19', G('12:19'), "and I will say to my soul: Soul, you have many good things laid up for many years; rest, eat, drink, be glad.'",
   'present (Marc. 4.28.11)', [T('4.28.11', '"divitis blandientis sibi" — the rich man flattering himself.')],
   wording='NA27. Roth: attested, but no insight into the wording.'),
 A('12:20', G('12:20'), "But God said to him, 'Senseless one, this night they are demanding your soul back from you; and the things you have made ready, whose will they be?'",
   'present (Marc. 4.28.11)', [T('4.28.11', '"cui deus dicit, Stulte, hac nocte animam tuam reposcent; quae autem parasti, cuius erunt?"')]),
 U('12:21', G('12:21'), 'So is the one who stores up treasure for himself and is not rich toward God."', 'Inside the attested parable 12:16–21.'),
 A('12:22', G('12:22'), 'And he said to his learners, "For this reason I tell you, do not be anxious for the soul, what you will eat, nor for the body, what you will put on.',
   'present (Marc. 4.29.1)', [T('4.29.1', '"Quis nollet curam nos agere animae de victu et corpori de vestitu…?"')]),
 A('12:23', G('12:23'), 'For the soul is more than the food, and the body than the clothing.',
   'present (Marc. 4.29.1)', [T('4.29.1', '"qui et substantiam ipsius animae accommodavit potiorem esca, et materiam ipsius corporis figuravit potiorem tunica".')]),
 A('12:24', G('12:24'), 'Consider the ravens, that they do not sow nor reap; they have no storeroom nor barn, and God feeds them. How much more are you worth than the birds!',
   'present (Marc. 4.29.1)', [T('4.29.1', '"cuius et corvi non serunt nec metunt nec in apothecas condunt, et tamen aluntur ab ipso".')],
   wording='NA27. Tertullian rewrites the passage in rhetorical form (Braun, Roth). "Nor gather into barns" is Matthew\'s wording (Matt 6:26). Roth judges "and God feeds them" attested by Tertullian but probably not in the text, by analogy with 12:28, where Epiphanius states that "God clothes the grass" was lacking. No witness states that the clause at 12:24 was lacking, and it is printed.'),
 U('12:25', G('12:25'), 'And which of you, by being anxious, can add a cubit to his stature?', 'Inside the attested paragraph 12:22–32.'),
 U('12:26', G('12:26'), 'If then you cannot do even the least thing, why are you anxious about the rest?', 'Inside the attested paragraph 12:22–32.'),
 A('12:27', G('12:27', [('πῶς αὐξάνει· οὐ κοπιᾷ οὐδὲ νήθει·', 'πῶς οὔτε νήθει οὔτε ὑφαίνει·')]),
   'Consider the lilies, how they neither spin nor weave; but I tell you, not even Solomon in all his glory was clothed like one of these.',
   'present (Marc. 4.29.1)', [T('4.29.1', '"cuius et lilia et foenum non texunt nec nent… cuius et Salomon gloriosissimus, nec ullo tamen flosculo cultior".')],
   wording=('Marcionite reading adopted (retroversion): "neither spin nor weave" for NA27 "how they grow: they neither toil nor spin". Tertullian\'s "non texunt nec nent" (weave, spin) cannot render NA27\'s "toil… spin". The Greek printed is that of codex D, which has the same two verbs (NA27 apparatus: οὔτε νήθει οὔτε ὑφαίνει D sys.c (⸉ a; McionT) Cl). '
            'Roth rates the verbs very likely and their order uncertain; Tertullian\'s order (weave, spin) is that of the Old Latin a. D\'s order is printed.'),
   western='The reading of D, the Old Syriac (sys.c) and Clement of Alexandria.'),
 A('12:28', greek('12:28', text='πόσῳ μᾶλλον ὑμᾶς, ὀλιγόπιστοι.'),
   'How much more you, you of little trust.',
   'present for 12:28b (Marc. 4.29.2–3); 12:28a absent (Pan. 42.11.6, sch. 31)',
   [E(31, 'οὐκ ἔχει τὸ »ὁ θεὸς ἀμφιέννυσι τὸν χόρτον«.'),
    T('4.29.2', '"Interim cur illos modicae fidei incusat, id est cuius fidei?"')],
   wording=('Attested omission: 12:28a ("if God so clothes the grass of the field, which is alive today and tomorrow is thrown into the oven") is not printed. Epiphanius states that the text "does not have \'God clothes the grass\'". Tertullian\'s argument requires "of little trust" (12:28b). '
            'Tertullian does mention grass ("lilia et foenum… vestiuntur ab ipso", 4.29.1), but he joins the lilies and the grass in the same way in his own works (Idol. 12.2; Ux. 1.4.7), and Roth takes the allusion as his. The remaining words "how much more you" are not quoted by either witness and are printed in the NA27 wording.')),
 U('12:29', G('12:29'), 'And you, do not seek what you will eat and what you will drink, and do not be held in suspense;', 'Inside the attested paragraph 12:22–32.'),
 A('12:30', G('12:30'), 'for all these things the nations of the world seek after, but your Father knows that you need them.',
   'present (Marc. 4.29.3; Pan. 42.11.6, sch. 32)',
   [E(32, '»ὑμῶν δὲ ὁ πατὴρ οἶδεν ὅτι χρῄζετε τούτων«, τῶν σαρκικῶν δή.'),
    T('4.29.3', '"Haec enim nationes mundi quaerunt… Scit autem pater opus esse haec vobis."')]),
 A('12:31', G('12:31', [('τὴν βασιλείαν αὐτοῦ', 'τὴν βασιλείαν τοῦ θεοῦ')]),
   'But seek the kingdom of God, and these things will be added to you.',
   'present (Marc. 4.29.5; Pan. 42.11.6, sch. 33)',
   [E(33, '»ζητεῖτε δὲ τὴν βασιλείαν τοῦ θεοῦ καὶ ταῦτα πάντα προστεθήσεται ὑμῖν«.'),
    T('4.29.5', '"Quaerite enim inquit regnum dei, et haec vobis adicientur."')],
   wording='Marcionite reading adopted: "the kingdom of God" for "his kingdom" (both witnesses; Roth: secure). NA27 apparatus: τοῦ θεοῦ 𝔓45 A D1 Q W Θ 070 f1.13 33 𝔐 lat sy; McionE. Epiphanius\' "all" (πάντα) and "but" (δέ) are not in Tertullian; not adopted.'),
 A('12:32', G('12:32', [('ὁ πατὴρ ὑμῶν δοῦναι', 'ὁ πατὴρ δοῦναι')]),
   'Do not be afraid, little flock, because the Father has been well pleased to give you the kingdom.',
   'present (Pan. 42.11.6, sch. 34)', [E(34, 'ἀντὶ τοῦ »ὁ πατὴρ ὑμῶν« »ὁ πατήρ« εἶχεν.')],
   wording='Marcionite reading adopted: "the Father" for "your Father". Epiphanius states the difference; Roth: "ὑμῶν attested as missing".'),
 A('12:35', G('12:35'), 'Let your loins be girded and your lamps burning,',
   'present (Marc. 4.29.6)', [T('4.29.6', '"Succingere debemus lumbos… Item lucernas ardentes habere".')]),
 A('12:36', G('12:36'), 'and you, be like humans waiting for their lord, when he will return from the wedding, so that when he comes and knocks they may open to him at once.',
   'present (Marc. 4.29.6)', [T('4.29.6', '"atque ita expectare dominum, id est Christum. Unde redeuntem? si a nuptiis, creatoris est, cuius nuptiae".')]),
 A('12:37', G('12:37'), 'Fortunate are those slaves whom the lord, when he comes, will find keeping awake. Amen, I tell you that he will gird himself and have them recline at table, and he will come by and serve them.',
   'present (Marc. 4.29.6)', [T('4.29.6', '"Sumus servi, dominum enim habemus deum."')]),
 A('12:38', G('12:38', [('κἂν ἐν τῇ δευτέρᾳ κἂν ἐν τῇ τρίτῃ φυλακῇ', 'κἂν ἐν τῇ ἑσπερινῇ φυλακῇ')]),
   'And if he comes in the evening watch and finds them so, fortunate are those.',
   'present (Pan. 42.11.6, sch. 35)', [E(35, 'ἀντὶ τοῦ »δευτέρᾳ ἢ τρίτῃ φυλακῇ« εἶχεν »ἑσπερινῇ φυλακῇ«.')],
   wording='Marcionite reading adopted: "in the evening watch" for "in the second or the third watch". Epiphanius states the difference; Roth: very likely. D and several Old Latin manuscripts (with Irenaeus\' Latin) also have the evening watch, though all but b have the second and third watch as well (NA27 apparatus: D c (f1 it syc Irlat)). The Greek printed puts the attested phrase in place of NA27\'s.',
   western='The evening watch is in D and the Old Latin.'),
 A('12:39', G('12:39'), 'But know this, that if the master of the house had known at what hour the thief is coming, he would not have let his house be dug through.',
   'present (Marc. 4.29.7)', [T('4.29.7', '"furem illum, cuius horam si pater familiae sciret non sineret suffodi domum suam".')],
   wording='NA27, without "he would have stayed awake and" (NA27 cites McionT with 𝔓75 ℵ* D for the shorter text).'),
 A('12:40', G('12:40'), 'You also, be ready, because the son of the human is coming at an hour you do not think."',
   'present (Marc. 4.29.7–8)', [T('4.29.7', '"propterea iubet ut parati simus, quia qua non putamus hora filius hominis adveniet".')]),
 A('12:41', G('12:41'), 'And Peter said, "Lord, are you saying this parable to us, or to all as well?"',
   'present (Marc. 4.29.9)', [T('4.29.9', '"Itaque interroganti Petro in illos an et in omnes parabolam dixisset…"')]),
 A('12:42', G('12:42'), 'And the lord said, "Who then is the trustworthy steward, the sensible one, whom the lord will set over his household servants, to give the measure of grain at the right time?',
   'present (Marc. 4.29.9)', [T('4.29.9', '"ad ipsos et ad universos qui ecclesiis praefuturi essent proponit actorum similitudinem".')],
   wording='NA27, including its bracketed [τό]. Roth: attested, but no insight into the wording.'),
 A('12:43', G('12:43'), 'Fortunate is that slave whom his lord, when he comes, will find doing so.',
   'present (Marc. 4.29.9)', [T('4.29.9', '"quorum qui bene tractaverit conservos absentia domini reverso eo…"')]),
 A('12:44', G('12:44'), 'Truly I tell you that he will set him over all his possessions.',
   'present (Marc. 4.29.9)', [T('4.29.9', '"omnibus bonis praeponetur".')]),
 A('12:45', G('12:45'), "But if that slave says in his heart, 'My lord is taking his time in coming,' and begins to beat the slave boys and the slave girls, and to eat and drink and get drunk,",
   'present (Marc. 4.29.9)', [T('4.29.9', '"qui vero secus egerit".')],
   wording='NA27. Roth: attested, but no insight into the wording.'),
 A('12:46', G('12:46'), 'the lord of that slave will come on a day when he is not expecting and at an hour he does not know, and will cut him in two, and will put his portion with the untrustworthy.',
   'present (Marc. 4.29.9–11; Pan. 42.11.6, sch. 36; Adam. 24,9–12)',
   [E(36, '»ἥξει ὁ κύριος τοῦ δούλου ἐκείνου καὶ διχοτομήσει αὐτὸν καὶ τὸ μέρος αὐτοῦ μετὰ τῶν ἀπίστων θήσει«.'),
    T('4.29.9', '"reverso domino qua die non putaverit, hora qua non scierit… segregabitur et pars eius cum infidelibus ponetur".')],
   wording='NA27. Tertullian renders διχοτομήσει as segregabitur ("will be separated") and reports the Marcionite reading of the verse as mild separation (4.29.10); that is reception, not a different text (Zahn, Roth).'),
 A('12:47', G('12:47'), 'But that slave who knew the will of his lord and did not make ready or act according to his will will be beaten with many blows;',
   'present (Marc. 4.29.11; Adam. 112,10–11)', [T('4.29.11', '"Quem alium intellegam caedentem servos paucis aut multis plagis, et prout commisit illis ita et exigentem ab eis…?"')],
   wording='NA27. The Dialogue of Adamantius has only "did not act" (NA27: McionA with 𝔓45 D); Roth: possible only.'),
 A('12:48', G('12:48'), 'but the one who did not know, and did things deserving blows, will be beaten with few. And everyone to whom much was given, much will be sought from him; and the one to whom they entrusted much, they will ask the more of him.',
   'present (Marc. 4.29.11; Adam. 112,11–12)', [T('4.29.11', '"caedentem servos paucis aut multis plagis, et prout commisit illis ita et exigentem ab eis".')]),
 A('12:49', G('12:49'), 'Fire I came to throw upon the earth, and what do I want, if it has already been kindled?',
   'present for 12:49a (Marc. 4.29.12–13; Adam. 68,2); 12:49b unattested',
   [T('4.29.12', '"Proclamat Christus tuus: Ignem veni mittere in terram."')],
   wording='NA27. Tertullian\'s "in terram" may render εἰς (𝔓45 D) rather than ἐπί; Roth: probable only. 12:49b is not cited; the verse is printed whole.'),
 U('12:50', G('12:50'), 'And I have an immersion to be immersed in, and how I am held fast until it is completed!', 'Inside the attested paragraph 12:49–53.'),
 A('12:51', G('12:51'), 'Do you think that I arrived to give peace on the earth? No, I tell you, but rather division.',
   'present (Marc. 4.29.13–14; Adam. 68,1)',
   [T('4.29.13', '"Putatis venisse me pacem mittere in terram? non, dico vobis, sed separationem. Machaeram quidem scriptum est. Sed Marcion emendat".')],
   wording='NA27. Tertullian\'s "mittere" (βαλεῖν) and "sed" (ἀλλά) are cited for Marcion in NA27; Roth rates both possible only (Tertullian may echo Matt 10:34, and wrote "mittere" a few lines earlier). Not adopted. Tertullian\'s charge that Marcion changed "sword" to "division" confuses Matthew\'s wording with Luke\'s: every Greek manuscript of Luke has "division".'),
 U('12:52', G('12:52'), 'For from now on there will be five in one house divided, three against two and two against three;', 'Inside the attested paragraph 12:49–53.'),
 A('12:53', G('12:53', [('διαμερισθήσονται πατὴρ', 'διαμερισθήσεται πατὴρ')]),
   'father will be divided against son and son against father, mother against daughter and daughter against the mother, mother-in-law against her daughter-in-law and daughter-in-law against the mother-in-law."',
   'present (Marc. 4.29.14)', [T('4.29.14', '"Denique, Dividetur, inquit, pater in filium et filius in patrem, et mater in filiam et filia in matrem, et nurus in socrum et socrus in nurum."')],
   wording='Marcionite reading adopted (retroversion): the singular διαμερισθήσεται ("will be divided") for NA27\'s plural, the reading of the Byzantine text. Tertullian quotes the verse ("inquit") with "dividetur"; Roth: very likely. The other small differences (his "and" before mother and daughter-in-law, no pronoun) are possible only and not adopted.'),
 U('12:54', G('12:54'), 'And he was also saying to the crowds, "When you see the cloud rising in the west, at once you say, \'A rainstorm is coming,\' and so it happens;', 'Inside the attested paragraph 12:54–56. NA27 prints [τήν] before νεφέλην (SBLGNT omits it).'),
 U('12:55', G('12:55'), "and when you see the south wind blowing, you say, 'There will be scorching heat,' and it happens.", 'Inside the attested paragraph 12:54–56.'),
 A('12:56', G('12:56', [('τὸ πρόσωπον τῆς γῆς καὶ τοῦ οὐρανοῦ', 'τὸ πρόσωπον τοῦ οὐρανοῦ καὶ τῆς γῆς')]),
   'Play-actors! The face of the sky and of the earth you know how to test, but this time, how is it that you do not know how to test it?',
   'present (Marc. 4.29.15)', [T('4.29.15', '"Et ideo hypocritas pronuntiabat, caeli quidem et terrae faciem probantes, tempus vero illud non dinoscentes".')],
   wording='Marcionite reading adopted: "heaven and earth" for NA27 "earth and heaven". Tertullian\'s order is that of 𝔓45 𝔓75 ℵ2 D K L N and the Old Latin (NA27 apparatus); Roth: very likely. NA27 has τὸν καιρὸν δὲ τοῦτον (SBLGNT τὸν δὲ καιρὸν τοῦτον — checked on the page image).'),
 A('12:57', G('12:57'), 'And why do you not judge even of yourselves what is just?',
   'present (Marc. 4.29.15–16)', [T('4.29.15', '"Merito exprobrat etiam quod iustum non a semetipsis iudicarent."')]),
 A('12:58', G('12:58', [('καὶ ὁ κριτής σε παραδώσει τῷ πράκτορι', 'καὶ ὁ κριτὴς παραδώσει σε τῷ πράκτορι')]),
   'For as you are going away with your opponent at law before a ruler, on the road make an effort to be released from him, so that he does not drag you to the judge, and the judge hand you over to the officer, and the officer throw you into prison.',
   'present (Marc. 4.29.16; Pan. 42.11.6, sch. 37)',
   [E(37, '»μή ποτε κατασύρῃ σε πρὸς τὸν κριτὴν καὶ ὁ κριτὴς παραδώσει σε τῷ πράκτορι«.'),
    T('4.29.16', '"Nam et iudicem, qui mittit in carcerem nec ducit inde nisi soluto etiam novissimo quadrante…"')],
   wording='Marcionite reading adopted: the word order παραδώσει σε (Epiphanius\' Greek, with 𝔓45 D 157 1241); Roth: very likely. Epiphanius quotes the verse in Matthew\'s wording elsewhere (Pan. 27.5.3), so here he follows the text before him.'),
 A('12:59', G('12:59'), 'I tell you, you will not come out from there until you have paid back even the last lepton."',
   'present (Marc. 4.29.16)', [T('4.29.16', '"nec ducit inde nisi soluto etiam novissimo quadrante".')],
   wording='NA27. Tertullian\'s quadrans is Matthew\'s κοδράντης (Matt 5:26); Roth: possible only.'),
]

OMITTED = [
 dict(ref='12:6', cls='A−', app=dict(roth='absent', witnesses=[
      E(29, 'οὐκ εἶχεν δὲ »οὐχὶ πέντε στρουθία ἀσσαρίων δύο πωλοῦνται καὶ ἓν ἐξ αὐτῶν οὐκ ἔστιν ἐπιλελησμένον ἐνώπιον τοῦ θεοῦ«.')],
      decision='not printed', reason='Epiphanius states that the text did not have the saying on the five sparrows. Tertullian passes from 12:5 to 12:8 (4.28.3–4); Roth counts his silence as confirmation (tacitus).')),
 dict(ref='12:7', cls='U−', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason=('"Even the hairs of your head are all numbered. Do not be afraid; you are of more value than many sparrows." The verse ends on the sparrows of 12:6, which Epiphanius says the text lacked. '
              'Tertullian goes from 12:5 to 12:8 with "I can also take from what follows" (4.28.4). He spends 4.29.1–5 arguing that the God who provides food and clothing is the Creator, and a saying that God has numbered the hairs of the head would have served that argument. NA27 places 12:4–7 in one paragraph.'))),
 dict(ref='12:33–34', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='"Sell your possessions and give alms… where your treasure is, there your heart will be also." A separate NA27 paragraph with no attested verse (METHOD §4.3). Tertullian passes from 12:31 (4.29.5) to 12:35 (4.29.6); Epiphanius from 12:32 (sch. 34) to 12:38 (sch. 35).')),
]

PREAMBLE = (
 "Fear and trust. Jesus warns his learners against the leaven of the Pharisees and tells them not to fear those who can "
 "only kill the body, but the one who has authority to throw into Gehenna. Whoever acknowledges him will be acknowledged "
 "\"before God\" (this text has no messengers in 12:8–9), and the holy spirit will teach them what to say. He refuses to divide "
 "an inheritance and tells of the rich fool. He tells them not to worry about food and clothing, but to seek the kingdom of "
 "God, which \"the Father\" is pleased to give them. Then come the parables of watchfulness: slaves waiting for their "
 "master to return from a wedding \"in the evening watch\", the thief, and the steward. He has come to throw fire upon the earth "
 "and to bring division, and he calls the crowds play-actors who read the face of heaven and earth but not the present time. "
 "The five sparrows (12:6), which Epiphanius says the text lacked, and the saying on God clothing the grass (12:28a) are not "
 "printed."
)

NOTES = [
 dict(term='Whom to fear (12:1–12)', cat='textual', refs=['12:1', '12:2', '12:4', '12:5', '12:8', '12:9', '12:10', '12:12'], text=(
  "Tertullian, Marc. 4.28.1–8 follows the passage closely: the leaven of the Pharisees, nothing hidden that will not be "
  "known, \"do not fear those who can only kill\", \"fear him who after killing has power to throw into Gehenna\", which he says "
  "means the Creator, acknowledging and denying \"before God\", the sin against the holy spirit, and the spirit teaching in that "
  "hour. Epiphanius, sch. 29–30 quotes 12:4–5 in Greek (\"to throw into Gehenna\", βαλεῖν εἰς γέενναν) and states that the text "
  "had \"before God\" where canonical Luke has \"before the messengers of God\". Both are printed. NA27 cites Marcion for the "
  "omission of \"the messengers of\" in both 12:8 and 12:9.")),
 dict(term='Not printed: the sparrows (12:6–7)', cat='excision', refs=['12:5', '12:8'], text=(
  "Epiphanius, sch. 29: the text \"did not have 'Are not five sparrows sold for two pennies? And not one of them is forgotten "
  "before God'\". In his refutation he presses Marcion with it: \"nothing happens without God, even if you take away what is "
  "about the sparrows\". 12:7 (\"the hairs of your head are all numbered… you are of more value than many sparrows\") depends "
  "on 12:6, and Tertullian, who goes straight from 12:5 to 12:8, does not cite it, though it would have suited his argument "
  "for the Creator's care. It is classed \"unattested, probably absent\".")),
 dict(term='The rich fool (12:13–21)', cat='textual', refs=['12:13', '12:14', '12:16', '12:19', '12:20'], text=(
  "Tertullian, Marc. 4.28.9–11. He sets Jesus' refusal to divide the inheritance (\"Who made me a judge over you?\") against "
  "Moses, who was rejected with the same words when he tried to make peace between two Hebrews (Exod 2:14), and quotes God's "
  "words to the rich man: \"Fool, this night they will demand your soul; and what you have prepared, whose will it be?\" "
  "12:15, 12:17–18 and 12:21 are not cited and are printed in grey.")),
 dict(term='Food and clothing (12:22–32)', cat='textual', refs=['12:22', '12:24', '12:27', '12:28', '12:30', '12:31', '12:32'], text=(
  "Tertullian, Marc. 4.29.1–5 recasts the passage rhetorically, but the lilies \"neither weave nor spin\" (D: \"neither spin "
  "nor weave\"), not \"toil nor spin\" as in canonical Luke, and he quotes \"Seek the kingdom of God\". Epiphanius, sch. 31–34 "
  "states that the text lacked \"God clothes the grass\" (12:28a), quotes 12:30b and 12:31 (\"the kingdom of God\"), and states "
  "that 12:32 read \"the Father\", not \"your Father\". The text printed therefore goes from Solomon not clothed like the lilies "
  "to \"How much more you, you of little trust!\" 12:25–26 and 12:29 are not cited and are printed in grey. 12:33–34 (\"sell "
  "your possessions\") form a paragraph that no witness cites and are not printed.")),
 dict(term='Watchfulness (12:35–48)', cat='textual', refs=['12:35', '12:36', '12:38', '12:39', '12:40', '12:41', '12:46', '12:47'], text=(
  "Tertullian, Marc. 4.29.6–11 reads the girded loins and burning lamps as the life of faith, asks from whose wedding the "
  "master returns, and says that the thief is the devil, while the son of the human comes as judge. He takes Peter's question to "
  "mean that the parable of the stewards is addressed to those \"who would preside over the churches\". Epiphanius, sch. 35 "
  "states that the master comes \"in the evening watch\", as in D and the Old Latin, not \"in the second or third watch\"; that "
  "reading is printed. Sch. 36 quotes 12:46. Tertullian reports that the Marcionites read \"cut him in two\" as mere "
  "separation (4.29.10); that is their reception, and the text has διχοτομήσει.")),
 dict(term='Fire and division (12:49–59)', cat='textual', refs=['12:49', '12:51', '12:53', '12:56', '12:57', '12:58', '12:59'], text=(
  "Tertullian, Marc. 4.29.12–16 quotes \"Fire I came to throw upon the earth\", \"Do you think I came to bring peace on the earth? "
  "No, I tell you, but division\", and the division of father and son, mother and daughter (Micah 7:6). He charges that "
  "\"sword\" is what is written and that Marcion changed it, but \"sword\" is Matthew's word (Matt 10:34); every Greek "
  "manuscript of Luke reads \"division\". He paraphrases 12:56 with \"heaven and earth\", the order of 𝔓45, 𝔓75 and D, which is "
  "printed. Epiphanius, sch. 37 quotes 12:58b. 12:50, 12:52 and 12:54–55 are not cited and are printed in grey.")),
 dict(term='The Father who gives', cat='theological', refs=['12:12', '12:30', '12:31', '12:32'], text=(
  "Interpretation. In this text the Father knows what the learners need, gives them the kingdom, and the holy spirit teaches "
  "them what to say. Tertullian's argument through 4.28–4.29 is that the God who provides food and clothing and judges is one "
  "and the same. The text as attested does not separate a providing God from a judging one. It speaks of the Father who gives "
  "and of the one to be feared who can cast into Gehenna (12:5), and Tertullian identifies them. Whether the community behind "
  "the text read the two as one cannot be decided from the witnesses.")),
 dict(term='μυριάδων, "tens of thousands"', cat='translation', refs=['12:1'], text='μυριάς, ten thousand, a countless number.'),
 dict(term='Προσέχετε ἑαυτοῖς ἀπό, "keep yourselves away from"', cat='translation', refs=['12:1'], text='To watch oneself, be on guard against.'),
 dict(term='ζύμης, "leaven"', cat='translation', refs=['12:1'], text='Sourdough, fermenting dough used to raise bread.'),
 dict(term='ὑπόκρισις, "play-acting"', cat='translation', refs=['12:1'], text='The acting of a part on stage (cf. ὑποκριτής, 6:42). "Hypocrisy" is the Greek word left untranslated.'),
 dict(term='συγκεκαλυμμένον… ἀποκαλυφθήσεται, "covered over… uncovered"', cat='translation', refs=['12:2'], text='One verb, καλύπτω, "cover", with two prefixes. "Revealed" is the second, and is uncovering.'),
 dict(term='ἐν τοῖς ταμείοις, "in the inner rooms"', cat='translation', refs=['12:3'], text='The innermost room of a house, the storeroom.'),
 dict(term='ἐπὶ τῶν δωμάτων, "upon the roofs"', cat='translation', refs=['12:3'], text='Flat roofs, where people talked across to each other.'),
 dict(term='σῶμα, "body"', cat='translation', refs=['12:4'], text='The body.'),
 dict(term='βαλεῖν εἰς γέενναν, "throw into Gehenna"', cat='translation', refs=['12:5'], text='The reading of this text, βαλεῖν. Gehenna is the valley of Hinnom outside Jerusalem, a place of burning that became an image of judgement. "Hell" imports a later picture.'),
 dict(term='ὁμολογήσῃ ἐν ἐμοί, "acknowledges me"', cat='translation', refs=['12:8'], text='Literally "acknowledges in me", a Semitic idiom: to declare oneself for someone.'),
 dict(term='ἔμπροσθεν τοῦ θεοῦ, "before God"', cat='translation', refs=['12:8', '12:9'], text='The reading of this text, "before God". Canonical Luke has "before the messengers of God".'),
 dict(term='ἀρνησάμενος… ἀπαρνηθήσεται, "disowns… will be disowned"', cat='translation', refs=['12:9'], text='ἀρνέομαι, as at 9:23.'),
 dict(term='ἀφεθήσεται αὐτῷ, "it will be let go for him"', cat='translation', refs=['12:10'], text='ἀφίημι, passive.'),
 dict(term='βλασφημήσαντι, "blasphemed"', cat='translation', refs=['12:10'], text='As at 5:21.'),
 dict(term='ἀρχάς, "rulers"', cat='translation', refs=['12:11'], text='Literally "beginnings": those first in rank.'),
 dict(term='μὴ μεριμνήσητε, "do not be anxious"', cat='translation', refs=['12:11'], text='μεριμνάω, to be anxious, to be pulled in different directions by worry. The same verb runs through 12:22–26.'),
 dict(term='ἀπολογήσησθε, "answer in defence"', cat='translation', refs=['12:11'], text="To make one's defence in court."),
 dict(term='Ἄνθρωπε, "Human"', cat='translation', refs=['12:14'], text='As at 5:20.'),
 dict(term='μεριστήν, "divider"', cat='translation', refs=['12:14'], text='One who divides an inheritance; a word from μερίζω, "divide" (12:13).'),
 dict(term='πλεονεξίας, "wanting more"', cat='translation', refs=['12:15'], text='πλεονεξία is literally "having more", the desire for more than one\'s share. "Greed" gives the sense.'),
 dict(term='ἐν τῷ περισσεύειν, "in having more than enough"', cat='translation', refs=['12:15'], text='To have a surplus, abundance.'),
 dict(term='εὐφόρησεν ἡ χώρα, "the land bore well"', cat='translation', refs=['12:16'], text='The land itself produced richly.'),
 dict(term='τοὺς καρπούς μου, "my fruits"', cat='translation', refs=['12:17'], text='καρπός, fruit, produce.'),
 dict(term='τὰ ἀγαθά μου, "my good things"', cat='translation', refs=['12:18'], text='ἀγαθός, good, as at 6:45. In 12:19 the same word: "many good things".'),
 dict(term='τῇ ψυχῇ μου· Ψυχή, "my soul: Soul"', cat='translation', refs=['12:19'], text='ψυχή, the living self. He speaks to himself.'),
 dict(term='εὐφραίνου, "be glad"', cat='translation', refs=['12:19'], text='To make merry, rejoice.'),
 dict(term='Ἄφρων, "senseless one"', cat='translation', refs=['12:20'], text='As at 11:40.'),
 dict(term='ἀπαιτοῦσιν, "they are demanding… back"', cat='translation', refs=['12:20'], text='A plural with no named subject, "they demand back", as of a loan. The present tense: it is happening now.'),
 dict(term='θησαυρίζων, "stores up treasure"', cat='translation', refs=['12:21'], text='From θησαυρός, treasure (6:45).'),
 dict(term='εἰς θεὸν πλουτῶν, "rich toward God"', cat='translation', refs=['12:21'], text='εἰς, "toward, into".'),
 dict(term='τῇ ψυχῇ, "for the soul"', cat='translation', refs=['12:22'], text='ψυχή, as at 9:24. Here "life" in the sense of the self that must eat.'),
 dict(term='ἐνδύσησθε, "put on"', cat='translation', refs=['12:22'], text='To clothe oneself.'),
 dict(term='τοὺς κόρακας, "the ravens"', cat='translation', refs=['12:24'], text='Unclean birds under the law.'),
 dict(term='διαφέρετε, "are you worth more"', cat='translation', refs=['12:24'], text='To differ, to be worth more.'),
 dict(term='ἡλικίαν, "stature"', cat='translation', refs=['12:25'], text='Height, or length of life. A cubit is a measure of length. The image can be read either way.'),
 dict(term='ἐλάχιστον, "the least thing"', cat='translation', refs=['12:26'], text='The superlative of μικρός.'),
 dict(term='οὔτε νήθει οὔτε ὑφαίνει, "neither spin nor weave"', cat='translation', refs=['12:27'], text='The reading of this text, with D. Canonical Luke has "they neither toil nor spin".'),
 dict(term='περιεβάλετο, "was clothed"', cat='translation', refs=['12:27'], text='To throw around oneself, to wrap.'),
 dict(term='Πόσῳ μᾶλλον ὑμᾶς, ὀλιγόπιστοι, "how much more you, you of little trust"', cat='translation', refs=['12:28'], text='This text does not have the first half of the verse ("if God so clothes the grass…"). The clause stands without its verb, and the English leaves it without one.'),
 dict(term='ὀλιγόπιστοι, "you of little trust"', cat='translation', refs=['12:28'], text='ὀλίγος, "little", and πίστις, "trust".'),
 dict(term='μὴ μετεωρίζεσθε, "do not be held in suspense"', cat='translation', refs=['12:29'], text='Literally "do not be raised up in the air": to be unsettled, in suspense, anxious.'),
 dict(term='τὰ ἔθνη τοῦ κόσμου, "the nations of the world"', cat='translation', refs=['12:30'], text='ἔθνη, the nations, the peoples other than Israel.'),
 dict(term='χρῄζετε, "you need"', cat='translation', refs=['12:30'], text='To have need of.'),
 dict(term='προστεθήσεται, "will be added"', cat='translation', refs=['12:31'], text='To be put to, added.'),
 dict(term='ποίμνιον, "flock"', cat='translation', refs=['12:32'], text='A small flock of sheep.'),
 dict(term='ὁ πατήρ, "the Father"', cat='translation', refs=['12:32'], text='The reading of this text: "the Father", not "your Father".'),
 dict(term='αἱ ὀσφύες περιεζωσμέναι, "your loins be girded"', cat='translation', refs=['12:35'], text='The long garment tucked up into the belt, for work or travel.'),
 dict(term='τὸν κύριον ἑαυτῶν, "their lord"', cat='translation', refs=['12:36'], text='κύριος, the owner, the master of the house. "Lord" is kept here and in what follows, as everywhere in this text.'),
 dict(term='ἀναλύσῃ ἐκ τῶν γάμων, "return from the wedding"', cat='translation', refs=['12:36'], text='To loosen, depart; γάμοι, wedding festivities.'),
 dict(term='δοῦλοι, "slaves"', cat='translation', refs=['12:37'], text='As at 7:2.'),
 dict(term='γρηγοροῦντας, "keeping awake"', cat='translation', refs=['12:37'], text='To stay awake, keep watch.'),
 dict(term='ἀνακλινεῖ, "have them recline"', cat='translation', refs=['12:37'], text='Make them lie down at table.'),
 dict(term='διακονήσει, "serve"', cat='translation', refs=['12:37'], text='διακονέω, to wait at table, as at 8:3.'),
 dict(term='ἐν τῇ ἑσπερινῇ φυλακῇ, "in the evening watch"', cat='translation', refs=['12:38'], text='The reading of this text. Canonical Luke has "in the second or the third watch".'),
 dict(term='ὁ οἰκοδεσπότης, "the master of the house"', cat='translation', refs=['12:39'], text='One word: the house-master. A different word from κύριος.'),
 dict(term='διορυχθῆναι, "be dug through"', cat='translation', refs=['12:39'], text='Walls of mud brick were broken into by digging.'),
 dict(term='ᾗ ὥρᾳ οὐ δοκεῖτε, "at an hour you do not think"', cat='translation', refs=['12:40'], text='δοκέω, think, suppose.'),
 dict(term='ὁ κύριος, "the lord"', cat='translation', refs=['12:42'], text='Twice in one verse: the narrator\'s "the lord" (Jesus) and the lord of the parable. The Greek uses the same word.'),
 dict(term='πιστὸς οἰκονόμος, "trustworthy steward"', cat='translation', refs=['12:42'], text='πιστός, trustworthy; οἰκονόμος, manager of a house.'),
 dict(term='φρόνιμος, "sensible"', cat='translation', refs=['12:42'], text='Prudent, thoughtful.'),
 dict(term='τῆς θεραπείας αὐτοῦ, "his household servants"', cat='translation', refs=['12:42'], text='θεραπεία, the word for healing, also means the body of servants who attend a master.'),
 dict(term='σιτομέτριον, "the measure of grain"', cat='translation', refs=['12:42'], text='The ration of food.'),
 dict(term='Χρονίζει, "is taking his time"', cat='translation', refs=['12:45'], text='To delay, linger.'),
 dict(term='τοὺς παῖδας καὶ τὰς παιδίσκας, "the slave boys and the slave girls"', cat='translation', refs=['12:45'], text='παῖς and παιδίσκη, the young slaves of the house.'),
 dict(term='μεθύσκεσθαι, "get drunk"', cat='translation', refs=['12:45'], text='To become drunk.'),
 dict(term='διχοτομήσει, "will cut him in two"', cat='translation', refs=['12:46'], text='Word for word "cut in two". Some read it as "cut him off", a figure of speech; the Greek says the harsh thing.'),
 dict(term='τῶν ἀπίστων, "the untrustworthy"', cat='translation', refs=['12:46'], text='ἄπιστος, the opposite of πιστός (12:42).'),
 dict(term='δαρήσεται πολλάς, "will be beaten with many blows"', cat='translation', refs=['12:47'], text='δέρω, to flay, to beat.'),
 dict(term='παρέθεντο, "they entrusted"', cat='translation', refs=['12:48'], text='They deposited with him, gave into his keeping. The verb is plural, with no named subject.'),
 dict(term='ἀνήφθη, "has been kindled"', cat='translation', refs=['12:49'], text='To light, set on fire.'),
 dict(term='τί θέλω εἰ, "what do I want, if"', cat='translation', refs=['12:49'], text='Word for word. Often read as a wish: "how I wish it were already kindled!" The Greek allows both.'),
 dict(term='βάπτισμα… βαπτισθῆναι, "an immersion to be immersed in"', cat='translation', refs=['12:50'], text='βαπτίζω, to dip, plunge, immerse. Here an image of being overwhelmed, as by flood waters.'),
 dict(term='συνέχομαι, "I am held fast"', cat='translation', refs=['12:50'], text='To be held together, pressed hard, gripped.'),
 dict(term='τελεσθῇ, "is completed"', cat='translation', refs=['12:50'], text='To bring to its end, accomplish.'),
 dict(term='διαμερισμόν, "division"', cat='translation', refs=['12:51'], text='Splitting apart.'),
 dict(term='διαμερισθήσεται, "will be divided"', cat='translation', refs=['12:53'], text='The reading of this text, with the Byzantine manuscripts.'),
 dict(term='νύμφην, "daughter-in-law"', cat='translation', refs=['12:53'], text='Literally "bride": the son\'s wife in the father\'s house.'),
 dict(term='ἐπὶ δυσμῶν, "in the west"', cat='translation', refs=['12:54'], text='Where the sun sets: over the sea.'),
 dict(term='νότον, "south wind"', cat='translation', refs=['12:55'], text='The wind from the desert.'),
 dict(term='ὑποκριταί, "play-actors"', cat='translation', refs=['12:56'], text='As at 6:42.'),
 dict(term='τοῦ οὐρανοῦ καὶ τῆς γῆς, "of the sky and of the earth"', cat='translation', refs=['12:56'], text='The reading of this text: the sky first.'),
 dict(term='δοκιμάζειν, "to test"', cat='translation', refs=['12:56'], text='To test, assess, examine.'),
 dict(term='τὸν καιρόν, "this time"', cat='translation', refs=['12:56'], text='καιρός, the right or decisive time, a season.'),
 dict(term='τὸ δίκαιον, "what is just"', cat='translation', refs=['12:57'], text='δίκαιος, as at 5:32.'),
 dict(term='ἀντιδίκου, "opponent at law"', cat='translation', refs=['12:58'], text='The other party in a lawsuit.'),
 dict(term='δὸς ἐργασίαν, "make an effort"', cat='translation', refs=['12:58'], text='Literally "give work".'),
 dict(term='ἀπηλλάχθαι, "to be released"', cat='translation', refs=['12:58'], text='To be set free from, to settle.'),
 dict(term='παραδώσει σε, "hand you over"', cat='translation', refs=['12:58'], text='The reading of this text. παραδίδωμι, as at 9:44.'),
 dict(term='τῷ πράκτορι, "the officer"', cat='translation', refs=['12:58'], text='The officer who collected debts and fines.'),
 dict(term='λεπτόν, "lepton"', cat='translation', refs=['12:59'], text='The smallest copper coin.'),
]
