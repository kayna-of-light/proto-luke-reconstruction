"""Batch 3, chapter 10 of the reconstruction: Luke 12:1–59."""
from buildlib import greek
from batch1_ch2 import U, A
from batch3_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}

ENTRIES = [
 A('12:1', G('12:1'), 'Meanwhile, when the crowd had gathered in thousands, so that they trampled on one another, he began to say to his disciples first, "Beware of the leaven of the Pharisees, which is hypocrisy.',
   'present (Marc. 4.28.1)', [T('4.28.1', '"Cavete, inquit discipulis, a fermento pharisaeorum, quod est hypocrisis".')],
   wording='NA27. Tertullian has "of the Pharisees" before "which is hypocrisy", the order of 𝔓45 ℵ A C D W and the Byzantine text (NA27 cites McionT and Epiphanius for it). Roth: the order is uncertain, since Matt 16:6 and Mark 8:15 have the same phrase; not adopted.'),
 A('12:2', G('12:2'), 'Nothing is covered up that will not be revealed, or hidden that will not be known.',
   'present (Marc. 4.28.2)', [T('4.28.2', '"ideo adicit, Nihil autem opertum, quod non patefiet, et nihil absconditum, quod non dinoscetur".')]),
 A('12:3', G('12:3'), 'Therefore whatever you have said in the dark will be heard in the light, and what you have whispered in private rooms will be proclaimed on the housetops.',
   'present (Marc. 4.28.2)', [T('4.28.2', '"cum subiciat etiam quae inter se mussitarent vel tractarent… in apertum processura, et in ore hominum futura".')]),
 A('12:4', G('12:4'), 'I tell you, my friends, do not be afraid of those who kill the body and after that can do nothing more.',
   'present (Marc. 4.28.3–4; Pan. 42.11.6, sch. 29)',
   [E(29, '»λέγω τοῖς φίλοις μου· μὴ φοβηθῆτε ἀπὸ τῶν ἀποκτενόντων τὸ σῶμα…«'),
    T('4.28.3', '"Dico autem, inquit, vobis amicis, nolite terreri ab eis qui vos solummodo occidere possunt, nec post hoc ullam in vobis habent potestatem."')],
   wording='NA27. Epiphanius spells ἀποκτενόντων; NA27 prints ἀποκτεινόντων (spelling).'),
 A('12:5', G('12:5', [('ἔχοντα ἐξουσίαν ἐμβαλεῖν εἰς τὴν γέενναν', 'ἔχοντα ἐξουσίαν βαλεῖν εἰς γέενναν')]),
   'But I will show you whom to fear: fear the one who, after he has killed, has authority to cast into Gehenna. Yes, I tell you, fear him.',
   'present (Marc. 4.28.3; Pan. 42.11.6, sch. 29)',
   [E(29, '»φοβήθητε δὲ τὸν μετὰ τὸ ἀποκτεῖναι ἔχοντα ἐξουσίαν βαλεῖν εἰς γέενναν«.'),
    T('4.28.3', '"Demonstrabo autem vobis quem timeatis: Timete eum qui postquam occiderit, potestatem habet mittendi in gehennam… Itaque dico vobis, hunc timete."')],
   wording='Marcionite reading adopted: βαλεῖν εἰς γέενναν ("to cast into Gehenna") for NA27 ἐμβαλεῖν εἰς τὴν γέενναν. Epiphanius\' Greek, with Tertullian\'s "mittendi in gehennam"; Roth: secure. NA27 apparatus: βαλεῖν 𝔓45 (D) W; McionT,E Clex Thd.'),
 A('12:8', G('12:8', [('ἔμπροσθεν τῶν ἀγγέλων τοῦ θεοῦ', 'ἔμπροσθεν τοῦ θεοῦ')]),
   'I tell you, everyone who acknowledges me before people, the son of man also will acknowledge before God;',
   'present (Marc. 4.28.4; Pan. 42.11.6, sch. 30)',
   [E(30, 'ἀντὶ τοῦ »ὁμολογήσει ἐνώπιον τῶν ἀγγέλων τοῦ θεοῦ« »ἐνώπιον τοῦ θεοῦ« λέγει.'),
    T('4.28.4', '"Dico enim vobis, omnis qui confitebitur in me coram hominibus, confitebor in illo coram deo."')],
   wording='Marcionite reading adopted: "before God" without "the angels of" (both witnesses; Roth: secure). NA27 apparatus: □ τῶν ἀγγέλων bis ℵ*; McionT,(E). Tertullian\'s first person "I will acknowledge" is Matthew\'s wording (Matt 10:32), which he uses elsewhere; Roth: possible only. NA27\'s ἔμπροσθεν is kept (Epiphanius\' ἐνώπιον may be his own).'),
 A('12:9', G('12:9', [('ἐνώπιον τῶν ἀγγέλων τοῦ θεοῦ', 'ἐνώπιον τοῦ θεοῦ')]),
   'but whoever denies me before people will be denied before God.',
   'present (Marc. 4.28.4)', [T('4.28.4', '"Et omnis qui negaverit me coram hominibus, denegabitur coram deo."')],
   wording='Marcionite reading adopted: "before God" without "the angels of", as in 12:8 (Roth: secure; NA27 cites McionT for the omission in both verses). The two citations in the Dialogue of Adamantius give Matthew 10:33 and are no evidence here (Roth).'),
 A('12:10', G('12:10'), 'And everyone who speaks a word against the son of man will be forgiven; but whoever blasphemes against the holy spirit will not be forgiven.',
   'present (Marc. 4.28.6)', [T('4.28.6', '"Qui dixerit in filium hominis, remittetur illi, qui autem dixerit in spiritum sanctum, non remittetur ei."')],
   wording='NA27. Tertullian has the same verb in both halves ("whoever speaks against the holy spirit"); Roth rates that form probable only. Not adopted.'),
 A('12:11', G('12:11'), 'When they bring you before the synagogues and the rulers and the authorities, do not worry about how or what you are to answer, or what you are to say;',
   'present (Marc. 4.28.7)', [T('4.28.7', '"Perductos ad potestates prohibet ad interrogationem cogitare de responsione".')]),
 A('12:12', G('12:12'), 'for the holy spirit will teach you in that very hour what you ought to say."',
   'present (Marc. 4.28.7–8)', [T('4.28.7', '"Sanctus enim, inquit, spiritus docebit vos ipsa hora quid eloqui debeatis."')]),
 A('12:13', G('12:13'), 'Someone in the crowd said to him, "Teacher, tell my brother to divide the inheritance with me."',
   'present (Marc. 4.28.9)', [T('4.28.9', '"Christus vero postulatus a quodam ut inter illum et fratrem ipsius de dividunda haereditate componeret…"')]),
 A('12:14', G('12:14'), 'But he said to him, "Man, who appointed me a judge or arbitrator over you?"',
   'present (Marc. 4.28.9–10)', [T('4.28.10', '"Quis me, inquit, iudicem constituit super vos?"')],
   wording='NA27. Tertullian has only "judge"; Roth notes that "or arbitrator" may not have stood. Not adopted (one witness, which shapes the saying after Exod 2:14).'),
 U('12:15', G('12:15'), 'And he said to them, "Take care, and be on your guard against all greed; for one\'s life does not consist in the abundance of one\'s possessions."', 'Inside the attested paragraph 12:13–15.'),
 A('12:16', G('12:16'), 'And he told them a parable: "The land of a rich man produced plentifully.',
   'present (Marc. 4.28.11)', [T('4.28.11', '"parabola divitis blandientis sibi de proventu agrorum suorum".')]),
 U('12:17', G('12:17'), 'And he thought to himself, \'What shall I do, for I have nowhere to store my crops?\'', 'Inside the attested parable 12:16–21.'),
 U('12:18', G('12:18'), 'Then he said, \'I will do this: I will pull down my barns and build larger ones, and there I will store all my grain and my goods.', 'Inside the attested parable 12:16–21.'),
 A('12:19', G('12:19'), 'And I will say to my soul: Soul, you have ample goods laid up for many years; relax, eat, drink, be merry.\'',
   'present (Marc. 4.28.11)', [T('4.28.11', '"divitis blandientis sibi" — the rich man flattering himself.')],
   wording='NA27. Roth: attested, but no insight into the wording.'),
 A('12:20', G('12:20'), 'But God said to him, \'Fool! This night your soul is demanded of you; and the things you have prepared, whose will they be?\'',
   'present (Marc. 4.28.11)', [T('4.28.11', '"cui deus dicit, Stulte, hac nocte animam tuam reposcent; quae autem parasti, cuius erunt?"')]),
 U('12:21', G('12:21'), 'So it is with whoever stores up treasure for himself and is not rich toward God."', 'Inside the attested parable 12:16–21.'),
 A('12:22', G('12:22'), 'And he said to his disciples, "Therefore I tell you, do not worry about your life, what you will eat, nor about your body, what you will wear.',
   'present (Marc. 4.29.1)', [T('4.29.1', '"Quis nollet curam nos agere animae de victu et corpori de vestitu…?"')]),
 A('12:23', G('12:23'), 'For life is more than food, and the body more than clothing.',
   'present (Marc. 4.29.1)', [T('4.29.1', '"qui et substantiam ipsius animae accommodavit potiorem esca, et materiam ipsius corporis figuravit potiorem tunica".')]),
 A('12:24', G('12:24'), 'Consider the ravens: they neither sow nor reap, they have neither storehouse nor barn, and God feeds them. Of how much more value are you than the birds!',
   'present (Marc. 4.29.1)', [T('4.29.1', '"cuius et corvi non serunt nec metunt nec in apothecas condunt, et tamen aluntur ab ipso".')],
   wording='NA27. Tertullian rewrites the passage in rhetorical form (Braun, Roth). "Nor gather into barns" is Matthew\'s wording (Matt 6:26). Roth judges "and God feeds them" attested by Tertullian but probably not in the text, by analogy with 12:28, where Epiphanius states that "God clothes the grass" was lacking. No witness states that the clause at 12:24 was lacking, and it is printed.'),
 U('12:25', G('12:25'), 'And which of you by worrying can add a single cubit to his span of life?', 'Inside the attested paragraph 12:22–32.'),
 U('12:26', G('12:26'), 'If then you are not able to do so small a thing as that, why do you worry about the rest?', 'Inside the attested paragraph 12:22–32.'),
 A('12:27', G('12:27', [('πῶς αὐξάνει· οὐ κοπιᾷ οὐδὲ νήθει·', 'πῶς οὔτε νήθει οὔτε ὑφαίνει·')]),
   'Consider the lilies, how they neither spin nor weave; yet I tell you, even Solomon in all his glory was not clothed like one of these.',
   'present (Marc. 4.29.1)', [T('4.29.1', '"cuius et lilia et foenum non texunt nec nent… cuius et Salomon gloriosissimus, nec ullo tamen flosculo cultior".')],
   wording=('Marcionite reading adopted (retroversion): "neither spin nor weave" for NA27 "how they grow: they neither toil nor spin". Tertullian\'s "non texunt nec nent" (weave, spin) cannot render NA27\'s "toil… spin". The Greek printed is that of codex D, which has the same two verbs (NA27 apparatus: οὔτε νήθει οὔτε ὑφαίνει D sys.c (⸉ a; McionT) Cl). '
            'Roth rates the verbs very likely and their order uncertain; Tertullian\'s order (weave, spin) is that of the Old Latin a. D\'s order is printed.'),
   western='The reading of D, the Old Syriac (sys.c) and Clement of Alexandria.'),
 A('12:28', greek('12:28', text='πόσῳ μᾶλλον ὑμᾶς, ὀλιγόπιστοι.'),
   'How much more you, you of little faith!',
   'present for 12:28b (Marc. 4.29.2–3); 12:28a absent (Pan. 42.11.6, sch. 31)',
   [E(31, 'οὐκ ἔχει τὸ »ὁ θεὸς ἀμφιέννυσι τὸν χόρτον«.'),
    T('4.29.2', '"Interim cur illos modicae fidei incusat, id est cuius fidei?"')],
   wording=('Attested omission: 12:28a ("if God so clothes the grass of the field, which is alive today and tomorrow is thrown into the oven") is not printed. Epiphanius states that the text "does not have \'God clothes the grass\'". Tertullian\'s argument requires "of little faith" (12:28b). '
            'Tertullian does mention grass ("lilia et foenum… vestiuntur ab ipso", 4.29.1), but he joins the lilies and the grass in the same way in his own works (Idol. 12.2; Ux. 1.4.7), and Roth takes the allusion as his. The remaining words "how much more you" are not quoted by either witness and are printed in the NA27 wording.')),
 U('12:29', G('12:29'), 'And do not seek what you are to eat and what you are to drink, and do not be anxious.', 'Inside the attested paragraph 12:22–32.'),
 A('12:30', G('12:30'), 'For all the nations of the world seek these things, and your Father knows that you need them.',
   'present (Marc. 4.29.3; Pan. 42.11.6, sch. 32)',
   [E(32, '»ὑμῶν δὲ ὁ πατὴρ οἶδεν ὅτι χρῄζετε τούτων«, τῶν σαρκικῶν δή.'),
    T('4.29.3', '"Haec enim nationes mundi quaerunt… Scit autem pater opus esse haec vobis."')]),
 A('12:31', G('12:31', [('τὴν βασιλείαν αὐτοῦ', 'τὴν βασιλείαν τοῦ θεοῦ')]),
   'Instead, seek the kingdom of God, and these things will be added to you.',
   'present (Marc. 4.29.5; Pan. 42.11.6, sch. 33)',
   [E(33, '»ζητεῖτε δὲ τὴν βασιλείαν τοῦ θεοῦ καὶ ταῦτα πάντα προστεθήσεται ὑμῖν«.'),
    T('4.29.5', '"Quaerite enim inquit regnum dei, et haec vobis adicientur."')],
   wording='Marcionite reading adopted: "the kingdom of God" for "his kingdom" (both witnesses; Roth: secure). NA27 apparatus: τοῦ θεοῦ 𝔓45 A D1 Q W Θ 070 f1.13 33 𝔐 lat sy; McionE. Epiphanius\' "all" (πάντα) and "but" (δέ) are not in Tertullian; not adopted.'),
 A('12:32', G('12:32', [('ὁ πατὴρ ὑμῶν δοῦναι', 'ὁ πατὴρ δοῦναι')]),
   'Do not be afraid, little flock, for it has pleased the Father to give you the kingdom.',
   'present (Pan. 42.11.6, sch. 34)', [E(34, 'ἀντὶ τοῦ »ὁ πατὴρ ὑμῶν« »ὁ πατήρ« εἶχεν.')],
   wording='Marcionite reading adopted: "the Father" for "your Father". Epiphanius states the difference; Roth: "ὑμῶν attested as missing".'),
 A('12:35', G('12:35'), 'Let your loins be girded and your lamps burning,',
   'present (Marc. 4.29.6)', [T('4.29.6', '"Succingere debemus lumbos… Item lucernas ardentes habere".')]),
 A('12:36', G('12:36'), 'and be like people waiting for their master to come home from the wedding feast, so that they may open to him at once when he comes and knocks.',
   'present (Marc. 4.29.6)', [T('4.29.6', '"atque ita expectare dominum, id est Christum. Unde redeuntem? si a nuptiis, creatoris est, cuius nuptiae".')]),
 A('12:37', G('12:37'), 'Blessed are those servants whom the master finds awake when he comes; truly I tell you, he will gird himself and have them recline at table, and he will come and serve them.',
   'present (Marc. 4.29.6)', [T('4.29.6', '"Sumus servi, dominum enim habemus deum."')]),
 A('12:38', G('12:38', [('κἂν ἐν τῇ δευτέρᾳ κἂν ἐν τῇ τρίτῃ φυλακῇ', 'κἂν ἐν τῇ ἑσπερινῇ φυλακῇ')]),
   'If he comes in the evening watch and finds them so, blessed are they.',
   'present (Pan. 42.11.6, sch. 35)', [E(35, 'ἀντὶ τοῦ »δευτέρᾳ ἢ τρίτῃ φυλακῇ« εἶχεν »ἑσπερινῇ φυλακῇ«.')],
   wording='Marcionite reading adopted: "in the evening watch" for "in the second or the third watch". Epiphanius states the difference; Roth: very likely. D and several Old Latin manuscripts (with Irenaeus\' Latin) also have the evening watch, though all but b have the second and third watch as well (NA27 apparatus: D c (f1 it syc Irlat)). The Greek printed puts the attested phrase in place of NA27\'s.',
   western='The evening watch is in D and the Old Latin.'),
 A('12:39', G('12:39'), 'But know this: if the master of the house had known at what hour the thief was coming, he would not have let his house be broken into.',
   'present (Marc. 4.29.7)', [T('4.29.7', '"furem illum, cuius horam si pater familiae sciret non sineret suffodi domum suam".')],
   wording='NA27, without "he would have stayed awake and" (NA27 cites McionT with 𝔓75 ℵ* D for the shorter text).'),
 A('12:40', G('12:40'), 'You also must be ready, for the son of man is coming at an hour you do not expect."',
   'present (Marc. 4.29.7–8)', [T('4.29.7', '"propterea iubet ut parati simus, quia qua non putamus hora filius hominis adveniet".')]),
 A('12:41', G('12:41'), 'Peter said, "Lord, are you telling this parable for us or for all?"',
   'present (Marc. 4.29.9)', [T('4.29.9', '"Itaque interroganti Petro in illos an et in omnes parabolam dixisset…"')]),
 A('12:42', G('12:42'), 'And the Lord said, "Who then is the faithful and wise steward, whom his master will set over his household, to give them their portion of food at the proper time?',
   'present (Marc. 4.29.9)', [T('4.29.9', '"ad ipsos et ad universos qui ecclesiis praefuturi essent proponit actorum similitudinem".')],
   wording='NA27, including its bracketed [τό]. Roth: attested, but no insight into the wording.'),
 A('12:43', G('12:43'), 'Blessed is that servant whom his master will find so doing when he comes.',
   'present (Marc. 4.29.9)', [T('4.29.9', '"quorum qui bene tractaverit conservos absentia domini reverso eo…"')]),
 A('12:44', G('12:44'), 'Truly I tell you, he will set him over all his possessions.',
   'present (Marc. 4.29.9)', [T('4.29.9', '"omnibus bonis praeponetur".')]),
 A('12:45', G('12:45'), 'But if that servant says in his heart, \'My master is delayed in coming\', and begins to beat the menservants and the maidservants, and to eat and drink and get drunk,',
   'present (Marc. 4.29.9)', [T('4.29.9', '"qui vero secus egerit".')],
   wording='NA27. Roth: attested, but no insight into the wording.'),
 A('12:46', G('12:46'), 'the master of that servant will come on a day when he does not expect him and at an hour he does not know, and will cut him in pieces and put him with the unfaithful.',
   'present (Marc. 4.29.9–11; Pan. 42.11.6, sch. 36; Adam. 24,9–12)',
   [E(36, '»ἥξει ὁ κύριος τοῦ δούλου ἐκείνου καὶ διχοτομήσει αὐτὸν καὶ τὸ μέρος αὐτοῦ μετὰ τῶν ἀπίστων θήσει«.'),
    T('4.29.9', '"reverso domino qua die non putaverit, hora qua non scierit… segregabitur et pars eius cum infidelibus ponetur".')],
   wording='NA27. Tertullian renders διχοτομήσει as segregabitur ("will be separated") and reports the Marcionite reading of the verse as mild separation (4.29.10); that is reception, not a different text (Zahn, Roth).'),
 A('12:47', G('12:47'), 'That servant who knew his master\'s will but did not get ready or act according to his will shall receive a severe beating.',
   'present (Marc. 4.29.11; Adam. 112,10–11)', [T('4.29.11', '"Quem alium intellegam caedentem servos paucis aut multis plagis, et prout commisit illis ita et exigentem ab eis…?"')],
   wording='NA27. The Dialogue of Adamantius has only "did not act" (NA27: McionA with 𝔓45 D); Roth: possible only.'),
 A('12:48', G('12:48'), 'But the one who did not know, and did what deserved a beating, shall receive a light beating. Everyone to whom much was given, of him much will be required; and from the one to whom much was entrusted, they will demand the more.',
   'present (Marc. 4.29.11; Adam. 112,11–12)', [T('4.29.11', '"caedentem servos paucis aut multis plagis, et prout commisit illis ita et exigentem ab eis".')]),
 A('12:49', G('12:49'), 'I came to cast fire on the earth, and how I wish it were already kindled!',
   'present for 12:49a (Marc. 4.29.12–13; Adam. 68,2); 12:49b unattested',
   [T('4.29.12', '"Proclamat Christus tuus: Ignem veni mittere in terram."')],
   wording='NA27. Tertullian\'s "in terram" may render εἰς (𝔓45 D) rather than ἐπί; Roth: probable only. 12:49b is not cited; the verse is printed whole.'),
 U('12:50', G('12:50'), 'I have a baptism to be baptized with, and how I am constrained until it is accomplished!', 'Inside the attested paragraph 12:49–53.'),
 A('12:51', G('12:51'), 'Do you think that I have come to give peace on earth? No, I tell you, but rather division.',
   'present (Marc. 4.29.13–14; Adam. 68,1)',
   [T('4.29.13', '"Putatis venisse me pacem mittere in terram? non, dico vobis, sed separationem. Machaeram quidem scriptum est. Sed Marcion emendat".')],
   wording='NA27. Tertullian\'s "mittere" (βαλεῖν) and "sed" (ἀλλά) are cited for Marcion in NA27; Roth rates both possible only (Tertullian may echo Matt 10:34, and wrote "mittere" a few lines earlier). Not adopted. Tertullian\'s charge that Marcion changed "sword" to "division" confuses Matthew\'s wording with Luke\'s: every Greek manuscript of Luke has "division".'),
 U('12:52', G('12:52'), 'For from now on in one house there will be five divided, three against two and two against three.', 'Inside the attested paragraph 12:49–53.'),
 A('12:53', G('12:53', [('διαμερισθήσονται πατὴρ', 'διαμερισθήσεται πατὴρ')]),
   'Father will be divided against son and son against father, mother against daughter and daughter against mother, mother-in-law against her daughter-in-law and daughter-in-law against mother-in-law."',
   'present (Marc. 4.29.14)', [T('4.29.14', '"Denique, Dividetur, inquit, pater in filium et filius in patrem, et mater in filiam et filia in matrem, et nurus in socrum et socrus in nurum."')],
   wording='Marcionite reading adopted (retroversion): the singular διαμερισθήσεται ("will be divided") for NA27\'s plural, the reading of the Byzantine text. Tertullian quotes the verse ("inquit") with "dividetur"; Roth: very likely. The other small differences (his "and" before mother and daughter-in-law, no pronoun) are possible only and not adopted.'),
 U('12:54', G('12:54'), 'He also said to the crowds, "When you see a cloud rising in the west, you say at once, \'A shower is coming\', and so it happens.', 'Inside the attested paragraph 12:54–56. NA27 prints [τήν] before νεφέλην (SBLGNT omits it).'),
 U('12:55', G('12:55'), 'And when you see the south wind blowing, you say, \'There will be scorching heat\', and it happens.', 'Inside the attested paragraph 12:54–56.'),
 A('12:56', G('12:56', [('τὸ πρόσωπον τῆς γῆς καὶ τοῦ οὐρανοῦ', 'τὸ πρόσωπον τοῦ οὐρανοῦ καὶ τῆς γῆς')]),
   'Hypocrites! You know how to interpret the appearance of heaven and earth, but why do you not know how to interpret the present time?',
   'present (Marc. 4.29.15)', [T('4.29.15', '"Et ideo hypocritas pronuntiabat, caeli quidem et terrae faciem probantes, tempus vero illud non dinoscentes".')],
   wording='Marcionite reading adopted: "heaven and earth" for NA27 "earth and heaven". Tertullian\'s order is that of 𝔓45 𝔓75 ℵ2 D K L N and the Old Latin (NA27 apparatus); Roth: very likely. NA27 has τὸν καιρὸν δὲ τοῦτον (SBLGNT τὸν δὲ καιρὸν τοῦτον — checked on the page image).'),
 A('12:57', G('12:57'), 'And why do you not judge for yourselves what is right?',
   'present (Marc. 4.29.15–16)', [T('4.29.15', '"Merito exprobrat etiam quod iustum non a semetipsis iudicarent."')]),
 A('12:58', G('12:58', [('καὶ ὁ κριτής σε παραδώσει τῷ πράκτορι', 'καὶ ὁ κριτὴς παραδώσει σε τῷ πράκτορι')]),
   'As you go with your accuser before a magistrate, make an effort on the way to settle with him, so that he does not drag you to the judge, and the judge hand you over to the officer, and the officer throw you into prison.',
   'present (Marc. 4.29.16; Pan. 42.11.6, sch. 37)',
   [E(37, '»μή ποτε κατασύρῃ σε πρὸς τὸν κριτὴν καὶ ὁ κριτὴς παραδώσει σε τῷ πράκτορι«.'),
    T('4.29.16', '"Nam et iudicem, qui mittit in carcerem nec ducit inde nisi soluto etiam novissimo quadrante…"')],
   wording='Marcionite reading adopted: the word order παραδώσει σε (Epiphanius\' Greek, with 𝔓45 D 157 1241); Roth: very likely. Epiphanius quotes the verse in Matthew\'s wording elsewhere (Pan. 27.5.3), so here he follows the text before him.'),
 A('12:59', G('12:59'), 'I tell you, you will not get out of there until you have paid the very last copper."',
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
 "Fear and trust. Jesus warns his disciples against the leaven of the Pharisees and tells them not to fear those who can "
 "only kill the body, but the one who has authority to cast into Gehenna. Whoever acknowledges him will be acknowledged "
 "\"before God\" (this text has no angels in 12:8–9), and the holy spirit will teach them what to say. He refuses to divide "
 "an inheritance and tells of the rich fool. He tells them not to worry about food and clothing, but to seek the kingdom of "
 "God, which \"the Father\" is pleased to give them. Then come the parables of watchfulness: servants waiting for their "
 "master to return from a wedding \"in the evening watch\", the thief, and the steward. He has come to cast fire on the earth "
 "and to bring division, and he calls the crowds hypocrites who read the face of heaven and earth but not the present time. "
 "The five sparrows (12:6), which Epiphanius says the text lacked, and the saying on God clothing the grass (12:28a) are not "
 "printed."
)

NOTES = [
 dict(term='Whom to fear (12:1–12)', cat='textual', refs=['12:1', '12:2', '12:4', '12:5', '12:8', '12:9', '12:10', '12:12'], text=(
  "Tertullian, Marc. 4.28.1–8 follows the passage closely: the leaven of the Pharisees, nothing hidden that will not be "
  "known, \"do not fear those who can only kill\", \"fear him who after killing has power to cast into Gehenna\", which he says "
  "means the Creator, acknowledging and denying \"before God\", the sin against the holy spirit, and the spirit teaching in that "
  "hour. Epiphanius, sch. 29–30 quotes 12:4–5 in Greek (\"to cast into Gehenna\", βαλεῖν εἰς γέενναν) and states that the text "
  "had \"before God\" where canonical Luke has \"before the angels of God\". Both are printed. NA27 cites Marcion for the "
  "omission of \"the angels of\" in both 12:8 and 12:9.")),
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
  "to \"How much more you, you of little faith!\" 12:25–26 and 12:29 are not cited and are printed in grey. 12:33–34 (\"sell "
  "your possessions\") form a paragraph that no witness cites and are not printed.")),
 dict(term='Watchfulness (12:35–48)', cat='textual', refs=['12:35', '12:36', '12:38', '12:39', '12:40', '12:41', '12:46', '12:47'], text=(
  "Tertullian, Marc. 4.29.6–11 reads the girded loins and burning lamps as the life of faith, asks from whose wedding the "
  "master returns, and says that the thief is the devil, while the son of man comes as judge. He takes Peter's question to "
  "mean that the parable of the stewards is addressed to those \"who would preside over the churches\". Epiphanius, sch. 35 "
  "states that the master comes \"in the evening watch\", as in D and the Old Latin, not \"in the second or third watch\"; that "
  "reading is printed. Sch. 36 quotes 12:46. Tertullian reports that the Marcionites read \"cut him in pieces\" as mere "
  "separation (4.29.10); that is their reception, and the text has διχοτομήσει.")),
 dict(term='Fire and division (12:49–59)', cat='textual', refs=['12:49', '12:51', '12:53', '12:56', '12:57', '12:58', '12:59'], text=(
  "Tertullian, Marc. 4.29.12–16 quotes \"I came to cast fire on the earth\", \"Do you think I came to bring peace on the earth? "
  "No, I tell you, but division\", and the division of father and son, mother and daughter (Micah 7:6). He charges that "
  "\"sword\" is what is written and that Marcion changed it, but \"sword\" is Matthew's word (Matt 10:34); every Greek "
  "manuscript of Luke reads \"division\". He paraphrases 12:56 with \"heaven and earth\", the order of 𝔓45, 𝔓75 and D, which is "
  "printed. Epiphanius, sch. 37 quotes 12:58b. 12:50, 12:52 and 12:54–55 are not cited and are printed in grey.")),
 dict(term='The Father who gives', cat='theological', refs=['12:12', '12:30', '12:31', '12:32'], text=(
  "Interpretation. In this text the Father knows what the disciples need, gives them the kingdom, and the holy spirit teaches "
  "them what to say. Tertullian's argument through 4.28–4.29 is that the God who provides food and clothing and judges is one "
  "and the same. The text as attested does not separate a providing God from a judging one. It speaks of the Father who gives "
  "and of the one to be feared who can cast into Gehenna (12:5), and Tertullian identifies them. Whether the community behind "
  "the text read the two as one cannot be decided from the witnesses.")),
]
