"""Batch 1, chapter 3 of the reconstruction: Luke 6:12–49."""
from buildlib import greek
from batch1_ch2 import U, A

T4171 = {'source': 'Tertullian, Marc. 4.17.11', 'evidence': '"Sed caecus caecum ducit in foveam… Sed non est discipulus super magistrum… Eximat et de oculo suo trabem haereticus, tunc in oculo Christiani si quam putat stipulam revincat. Proinde et arbor bona non proferat malum fructum… nec mala bonum… Sic nec Marcion aliquid boni de thesauro Cerdonis malo protulit".'}

ENTRIES = [
 A('6:12', greek('6:12'), 'And it happened in these days that he went out into the mountain to pray, and he was spending the whole night in the prayer of God.',
   'present (Marc. 4.13.1)', [{'source': 'Tertullian, Marc. 4.13.1', 'evidence': '"ascendit in montem et illic pernoctat in oratione".'}]),
 A('6:13', greek('6:13'), 'And when it became day, he called his learners to him, and choosing twelve from them, whom he also named emissaries:',
   'present (Marc. 4.13.4)', [{'source': 'Tertullian, Marc. 4.13.4', 'evidence': 'The number twelve and its figures; "Totidem enim apostoli portendebantur".'}]),
 A('6:14', greek('6:14'), 'Simon, whom he also named Peter, and Andrew his brother, and Jacob and John, and Philip and Bartholomew,',
   'present (Marc. 4.13.6)', [{'source': 'Tertullian, Marc. 4.13.6', 'evidence': 'Why Simon was given the name Peter ("petra et lapis Christus").'}],
   wording='NA27. Only the naming of Simon as Peter is cited; the other names are printed in the NA27 wording within the attested verse.'),
 U('6:15', greek('6:15', [('Ζηλωτὴν', 'ζηλωτὴν')]), 'and Matthew and Thomas, and Jacob son of Alphaeus, and Simon called the zealot,',
   'Inside the attested list 6:13–16. The previous text printed ellipses here (research question Q3c); the verse is now printed and flagged.'),
 A('6:16', greek('6:16'), 'and Judas of Jacob, and Judas Iscarioth, who became a traitor.',
   'present (Marc. 2.28.2; Pan. 42.11.6, sch. 4)',
   [{'source': 'Epiphanius, Pan. 42.11.6, sch. 4', 'evidence': '»Ἰούδαν Ἰσκαριώτην, ὃς ἐγένετο προδότης« (Holl\'s text; manuscripts V and M read -ώθ).'},
    {'source': 'Tertullian, Marc. 2.28.2 (via Roth loci)', 'evidence': 'Judas the traitor.'}],
   wording='NA27 (Ἰσκαριώθ). NA27 cites McionE for Ἰσκαριώτην on the basis of Holl\'s emended text; the Epiphanius manuscripts V and M have -ώθ. Roth leaves the form open. Not changed.'),
 A('6:17', greek('6:17'), 'And coming down with them, he stood on a level place, and a large crowd of his learners, and a great multitude of the people from all Judea and Jerusalem and the seacoast of Tyre and Sidon,',
   'present (Marc. 4.13.7; Pan. 42.11.6, sch. 4)',
   [{'source': 'Epiphanius, Pan. 42.11.6, sch. 4', 'evidence': 'ἀντὶ δὲ τοῦ »κατέβη μετ\' αὐτῶν« ἔχει »κατέβη ἐν αὐτοῖς«.'},
    {'source': 'Tertullian, Marc. 4.13.6', 'evidence': '"Conveniunt a Tyro et ex aliis regionibus multitudo etiam transmarina."'}],
   wording='NA27. Epiphanius reports ἐν αὐτοῖς for μετ\' αὐτῶν (Roth: probable only). Tertullian\'s "transmarina" agrees in sense with καὶ τῆς περαίας (ℵ* W ff2; "et trans fretum" it vgmss; Roth: possible). Both noted, not adopted.'),
 U('6:18', greek('6:18'), 'who came to hear him and to be cured of their diseases; and those troubled by unclean spirits were being healed.',
   'Inside the attested passage 6:17–19.'),
 A('6:19', greek('6:19', [('ἐζήτουν', 'ἐζήτει')]), 'And the whole crowd was seeking to touch him, because power was going out from him and curing all.',
   'present (Pan. 42.11.6, sch. 5)',
   [{'source': 'Epiphanius, Pan. 42.11.6, sch. 5', 'evidence': '»καὶ πᾶς ὁ ὄχλος ἐζήτει ἅπτεσθαι αὐτοῦ. καὶ αὐτὸς ἐπάρας τοὺς ὀφθαλμοὺς αὐτοῦ« καὶ τὰ ἑξῆς.'}],
   wording='Marcionite reading adopted: ἐζήτει (Epiphanius\' Greek; Roth: very likely). NA27 ἐζήτουν; the singular is also the Byzantine reading. A singular verb with a collective subject could be Epiphanius\' own correction; noted.'),
 A('6:20', greek('6:20', [('ὅτι ὑμετέρα ἐστὶν', 'ὅτι αὐτῶν ἐστιν')]),
   'And he, lifting up his eyes to his learners, was saying, "Fortunate are the destitute, because theirs is the kingdom of God.',
   'present (Marc. 4.14.1, 9, 13; Pan. 42.11.6, sch. 5; Eznik, De Deo 405)',
   [{'source': 'Tertullian, Marc. 4.14.1', 'evidence': '"Beati mendici (sic enim exigit interpretatio vocabuli quod in Graeco est), quoniam illorum est regnum dei."'},
    {'source': 'Tertullian, Marc. 4.14.13', 'evidence': '"Beati mendici, quoniam illorum est regnum caelorum."'},
    {'source': 'Epiphanius, Pan. 42.11.6, sch. 5', 'evidence': '»καὶ αὐτὸς ἐπάρας τοὺς ὀφθαλμοὺς αὐτοῦ« (6:20a).'}],
   wording='Marcionite reading adopted: αὐτῶν for ὑμετέρα. Latin "illorum" cannot render ὑμετέρα. NA27 apparatus: αὐτῶν W ff2 sys sa bomss; McionT. Roth: very likely. No "in spirit" (τῷ πνεύματι is added in ℵ2 Q Θ f1.13 33 al).',
   western='Agrees with W, Old Latin ff2 and the Old Syriac (sys).'),
 A('6:21', greek('6:21'), 'Fortunate are those who hunger now, because you will be fed. Fortunate are those who weep now, because you will laugh.',
   'present (Marc. 4.14.9, 11, 13)',
   [{'source': 'Tertullian, Marc. 4.14.9, 13', 'evidence': '"Beati esurientes, quoniam ipsi saturabuntur"; "Beati qui esuriunt, quoniam saturabuntur… Beati qui plorant, quoniam ridebunt."'}],
   wording='NA27. Tertullian has the third person and no "now" twice. NA27 apparatus: νῦν om. bis McionT (Eus); -σονται ℵ*.c pc it sys samss; McionT Or; -σουσιν W e sys samss; McionT. Roth: possible only. Noted, not adopted.'),
 A('6:22', greek('6:22'), 'Fortunate are you when the humans hate you, and when they set you apart and reproach you and throw out your name as evil because of the son of the human.',
   'present (Marc. 4.14.14)',
   [{'source': 'Tertullian, Marc. 4.14.14', 'evidence': '"Beati eritis cum vos odio habebunt homines et exprobrabunt et eicient nomen vestrum velut nequam propter filium hominis."'}],
   wording='NA27. Tertullian lacks "and when they set you apart" (NA27: om. 2542 McionT) and has future verbs (Roth: possible). Noted, not adopted.'),
 A('6:23', greek('6:23'), 'Rejoice in that day and leap, for look, your wage is great in heaven; for their fathers were doing the same things to the prophets.',
   'present (Marc. 4.15.1; Pan. 42.11.6, sch. 6)',
   [{'source': 'Epiphanius, Pan. 42.11.6, sch. 6', 'evidence': '»κατὰ τὰ αὐτὰ ἐποίουν τοῖς προφήταις οἱ πατέρες ὑμῶν«.'},
    {'source': 'Tertullian, Marc. 4.15.1', 'evidence': '"Secundum haec, inquit, faciebant prophetis patres eorum."'}],
   wording='NA27. The witnesses disagree: Epiphanius "your fathers", Tertullian "their fathers" (= NA27). Neither has γάρ, but both quote from the start of the clause. Not changed.'),
 A('6:24', greek('6:24'), 'But woe to you, the rich, because you are holding your comfort in full.',
   'present (Marc. 4.15.3, 9; Eznik, De Deo 405)',
   [{'source': 'Tertullian, Marc. 4.15.8–9', 'evidence': '"a Christo dirigitur in divites… Vae divitibus… Quoniam, inquit, recepistis advocationem vestram".'}]),
 A('6:25', greek('6:25'), 'Woe to you who have been filled up now, because you will hunger. Woe, those who laugh now, because you will mourn and weep.',
   'present (Marc. 4.15.13)',
   [{'source': 'Tertullian, Marc. 4.15.13', 'evidence': '"Ingerit Vae etiam saturatis, quia esurient, etiam ridentibus nunc, quia lugebunt."'}],
   wording='NA27. Tertullian has no "now" with "full" (NA27: om. A D K P Γ Ψ 565 2542* 𝔐 lat syp; McionT Irlat). Roth rates the absence "likely"; one witness. Noted, not adopted.'),
 A('6:26', greek('6:26', [('καλῶς ὑμᾶς εἴπωσιν', 'ὑμᾶς καλῶς εἴπωσιν')]),
   'Woe when all the humans speak well of you, for their fathers were doing the same things to the false prophets.',
   'present (Marc. 4.15.14)',
   [{'source': 'Tertullian, Marc. 4.15.14', 'evidence': '"Vae, cum vobis benedixerint homines. Secundum haec faciebant et pseudoprophetis patres illorum."'}],
   wording='NA27 (ὑμᾶς καλῶς; SBLGNT καλῶς ὑμᾶς — checked on the page image). Tertullian lacks "all" (NA27: οἱ ἄνθρωποι without πάντες D L Γ Δ 892* pm vgcl sys.p bomss; McionT; Roth: "may not have been present"). Noted, not adopted.'),
 A('6:27', greek('6:27'), 'But to you I say, to those who are hearing: love your enemies, do good to those who hate you,',
   'present (Marc. 4.16.1; Adam. 26,20–21; 88,26)',
   [{'source': 'Tertullian, Marc. 4.16.1', 'evidence': '"Sed vobis dico, inquit, qui auditis… diligite inimicos vestros, et benedicite eos qui vos oderunt, et orate pro eis qui vos calumniantur."'}],
   wording='NA27. Tertullian compresses 6:27b–28a into "bless those who hate you" (Roth: possible). The previous text printed that compressed form; NA27 is restored.'),
 A('6:28', greek('6:28'), 'bless those who curse you, pray for those who mistreat you.',
   'present (Marc. 4.16.1; Adam. 26,20–21)', [{'source': 'Tertullian, Marc. 4.16.1', 'evidence': 'see 6:27.'}]),
 A('6:29', greek('6:29'), 'To the one who strikes you on the jaw, offer the other also; and from the one who takes away your cloak, do not withhold the tunic either.',
   'present (Marc. 4.16.2, 6; Adam. 32,5–6; 38,2–3)',
   [{'source': 'Tertullian, Marc. 4.16.2, 6', 'evidence': '"alteram amplius maxillam offerri iubens, et super tunicam pallio quoque cedi"; "non modo non retinendi tunicam sed et amplius et pallium concedendi".'}],
   wording='NA27. Tertullian has the garments in Matthew\'s order, tunic then cloak (Roth: possible). Noted, not adopted.'),
 A('6:30', greek('6:30'), 'To everyone who asks you, keep giving; and from the one who takes away what is yours, do not ask it back.',
   'present for 6:30a (Marc. 4.16.8); 6:30b unattested',
   [{'source': 'Tertullian, Marc. 4.16.8', 'evidence': '"Omni petenti te dato".'}],
   wording='NA27. 6:30b is not cited; printed within the attested verse.'),
 A('6:31', greek('6:31'), 'And just as you want the humans to do to you, do to them likewise.',
   'present (Marc. 4.16.13, 16)',
   [{'source': 'Tertullian, Marc. 4.16.13', 'evidence': '"Et sicut vobis fieri vultis ab hominibus, ita et vos facite illis."'}],
   wording='NA27. Tertullian\'s form is passive ("as you wish it to be done to you by people") and has "you also" (καὶ ὑμεῖς: ℵ A D L W Θ Ξ Ψ f1.13 33 𝔐; (McionT) in NA27). Roth rates ὑμῖν γίνεσθαι θέλετε παρὰ ἀνθρώπων very likely. Only Tertullian attests it, and a Latin writer can recast the voice of a clause; the NA27 Greek can stand behind his Latin (METHOD §5.4). Noted, not adopted.'),
 U('6:32', greek('6:32'), 'And if you love those who love you, what kind of favour is that to you? For even the sinners love those who love them.',
   'Inside the attested passage 6:27–36.'),
 U('6:33', greek('6:33', [('καὶ ἐὰν ἀγαθοποιῆτε', 'καὶ γὰρ ἐὰν ἀγαθοποιῆτε')]), 'For indeed, if you do good to those who do good to you, what kind of favour is that to you? The sinners also do the same.',
   'Inside the attested passage 6:27–36. NA27 brackets [γάρ]; printed.'),
 A('6:34', greek('6:34'), 'And if you lend to those from whom you hope to receive, what kind of favour is that to you? Sinners too lend to sinners, so that they may receive back the equal amount.',
   'present for 6:34a (Marc. 4.17.1); 6:34b unattested',
   [{'source': 'Tertullian, Marc. 4.17.1', 'evidence': '"Et si feneraveritis a quibus speratis vos recepturos, quae gratia est vobis?"'}],
   wording='NA27, with the bracketed [ἐστίν]. Tertullian\'s "recepturos" is read by Roth as ἀπολαβεῖν (very likely), but "recipere" is also the Latin for λαβεῖν here (so the Vulgate), and no Greek manuscript in NA27 reads ἀπολαβεῖν. Noted, not adopted. 6:34b is not cited.'),
 A('6:35', greek('6:35'), 'But love your enemies, and do good, and lend, despairing of nothing; and your wage will be great, and you will be sons of the Highest, because he is kind toward the ungrateful and evil.',
   'present for 6:35b (Marc. 4.17.5–6); 6:35a unattested',
   [{'source': 'Tertullian, Marc. 4.17.5–6', 'evidence': '"Ille me nunc rursus filium nuncupat… Quia ipse, inquit, suavis est adversus ingratos et malos."'}],
   wording='NA27. 6:35a is not cited; printed within the attested verse. Roth reads υἱοὶ θεοῦ for υἱοὶ ὑψίστου (possible only); not adopted.'),
 A('6:36', greek('6:36'), 'Become compassionate, just as your Father is compassionate.',
   'present (Marc. 4.17.8)',
   [{'source': 'Tertullian, Marc. 4.17.8', 'evidence': '"Estote, inquit, misericordes, sicut pater vester misertus est vestri."'}],
   wording='NA27 without its bracketed [καί]: Tertullian has "sicut", not "sicut et", and NA27 cites McionT with ℵ B L W Ξ Ψ for the omission. Tertullian\'s "misertus est vestri" (ᾤκτειρεν ὑμᾶς) is rated possible by Roth; noted, not adopted.'),
 A('6:37', greek('6:37', [('καὶ οὐ μὴ κριθῆτε', 'ἵνα μὴ κριθῆτε'), ('καὶ οὐ μὴ καταδικασθῆτε', 'ἵνα μὴ καταδικασθῆτε')]),
   'And do not judge, so that you may not be judged; and do not condemn, so that you may not be condemned. Release, and you will be released.',
   'present (Marc. 4.17.9)',
   [{'source': 'Tertullian, Marc. 4.17.9', 'evidence': '"Nolite iudicare, ne iudicemini. Nolite condemnare, ne condemnemini. Dimittite, et dimittemini."'}],
   wording='Marcionite reading adopted: ἵνα μή twice. Latin "ne" with the subjunctive renders ἵνα μή, not καὶ οὐ μή. NA27 apparatus: ἵνα A D W Ψ pc a c e f sys sa bopt; McionT (first clause); ἵνα D W* it sys sa; McionT (second). Roth: very likely. Tertullian has no "and" before either prohibition (Roth: καί "likely not present"); one witness, not adopted.',
   western='Agrees with D, W and the Old Latin and Old Syriac.'),
 A('6:38', greek('6:38', [('ᾧ γὰρ μέτρῳ μετρεῖτε', 'τῷ γὰρ αὐτῷ μέτρῳ ᾧ μετρεῖτε')]),
   'Give, and it will be given to you: a fine measure, pressed down, shaken, pouring over, they will give into your fold. For by the same measure by which you measure, it will be measured back to you."',
   'present (Marc. 4.17.9; Adam. 32,17–18; 66,32–33)',
   [{'source': 'Tertullian, Marc. 4.17.9', 'evidence': '"Date, et dabitur vobis, mensuram bonam, pressam ac fluentem, dabunt in sinum vestrum. Eadem qua mensi eritis mensura, remetietur vobis."'}],
   wording='Marcionite reading adopted: τῷ γὰρ αὐτῷ μέτρῳ ᾧ. Latin "eadem" requires αὐτῷ. NA27 apparatus: 𝔓45vid A C Θ Ψ f13 𝔐 lat syh; McionT. Roth: very likely. Tertullian lacks "shaken together" (Roth: "may have been present"); not adopted.'),
 A('6:39', greek('6:39'), 'And he also said a parable to them: "Can a blind person lead a blind person? Will they not both fall into a pit?',
   'present (Marc. 4.17.11)', [T4171]),
 A('6:40', greek('6:40'), 'A learner is not above the teacher; but everyone who has been fully trained will be like his teacher.',
   'present (Marc. 4.17.11)', [T4171],
   wording='NA27 (no αὐτοῦ after the first διδάσκαλον, which A C Ψ 𝔐 add; Tertullian "magistrum" without "suum").'),
 A('6:41', greek('6:41'), "Why do you look at the splinter in your brother's eye, but the beam in your own eye you do not consider?",
   'present (Marc. 4.17.11)', [T4171]),
 A('6:42', greek('6:42', [('ὀφθαλμῷ σοῦ δοκὸν', 'ὀφθαλμῷ σου δοκὸν'), ('ὀφθαλμοῦ σοῦ, καὶ', 'ὀφθαλμοῦ σου, καὶ')]),
   "How can you say to your brother, 'Brother, let me throw out the splinter in your eye,' when you yourself do not see the beam in your eye? Play-actor, first throw the beam out of your eye, and then you will see clearly to throw out the splinter in your brother's eye.",
   'present (Marc. 4.17.11)', [T4171]),
 A('6:43', greek('6:43'), 'For there is no fine tree producing rotten fruit, nor again a rotten tree producing fine fruit.',
   'present (Marc. 4.17.11; Adam. 56,14–16; 58,11–13; Origen, Princ. 2.5.4; Hippolytus, Haer. 10.19.3; Ps.-Tertullian 6.2; Philastrius 45.2)', [T4171],
   wording='NA27. Roth: the wording is obscured by the many citations; good tree before bad tree, and the verb ποιέω, are clear. NA27 agrees.'),
 U('6:44', greek('6:44'), 'For each tree is known by its own fruit; for they do not gather figs from thorns, nor do they harvest a bunch of grapes from a bramble.',
   'Inside the attested passage 6:43–45; Tertullian passes from the trees to the treasure.'),
 A('6:45', greek('6:45', [('τῆς καρδίας αὐτοῦ προφέρει', 'τῆς καρδίας προφέρει')]),
   'The good person brings out the good from the good treasure of the heart, and the evil one brings out the evil from the evil; for out of the overflow of the heart his mouth speaks.',
   'present (Marc. 4.17.11; [Adam. 58,18–20]; Origen, Princ. 2.5.4)', [T4171],
   wording='NA27 (no αὐτοῦ after καρδίας; SBLGNT has it — checked on the page image).'),
 A('6:46', greek('6:46'), "Why do you call me 'lord, lord', and do not do what I say?",
   'present (Marc. 4.17.12–13)',
   [{'source': 'Tertullian, Marc. 4.17.12–13', 'evidence': '"quis videbitur dixisse, Quid vocas, Domine, domine?… Quis item adiecisse potuisset, Et non facitis quae dico?"'}]),
 U('6:47', greek('6:47'), 'Everyone who comes to me and hears my words and does them, I will show you whom he is like:',
   'Inside the passage opened by the attested 6:46.'),
 U('6:48', greek('6:48'), 'he is like a person building a house, who dug and went deep and laid a foundation on the rock; and when a flood came, the river broke against that house, and was not strong enough to shake it, because it had been built well.',
   'Inside the passage opened by the attested 6:46.'),
 U('6:49', greek('6:49'), 'But the one who heard and did not do is like a person who built a house on the ground without a foundation, against which the river broke, and at once it collapsed, and the breaking of that house became great."',
   'Inside the passage opened by the attested 6:46.'),
]

OMITTED = []

PREAMBLE = (
 "Some things are only settled at night, high up and alone. When day comes they do not stay up there. They come "
 "down and stand on level ground, where every part of us can reach them, from the centre to the farthest shore.\n\n"
 "What is said there turns our accounts upside down. Emptiness is called fortunate, and fullness is told it has "
 "already been paid. Whatever measure we use comes back to us, pressed down and running over.\n\n"
 "Then the voice comes closer, right up to the eye. There is a splinter we see very clearly, and something much "
 "larger that we do not see at all.\n\n"
 "We say \"lord, lord\" so easily."
)

NOTES = [
 dict(term='The twelve (6:12–16)', cat='textual', refs=['6:12', '6:13', '6:14', '6:15', '6:16'], text=(
  "Tertullian, Marc. 4.13.1–6: he went up the mountain and spent the night in prayer, chose twelve (with figures of the number "
  "from the Creator's scriptures), and named Simon Peter. Epiphanius, sch. 4: »Ἰούδαν Ἰσκαριώτην, ὃς ἐγένετο προδότης«. The "
  "other names are not cited. 6:14 is printed whole because the verse is attested; 6:15 is printed in grey. The previous text "
  "replaced 6:15 with ellipses (research question Q3c); that is superseded. On the form of Judas' surname: NA27 prints "
  "Ἰσκαριώθ and cites Marcion (McionE) for Ἰσκαριώτην, but that rests on Holl's emendation of Epiphanius; his manuscripts V and "
  "M read -ώθ. The NA27 form is kept. The previous note presented Ἰσκαριώθ as a Marcionite reading; it is withdrawn.")),
 dict(term='The descent and the crowd (6:17–19)', cat='textual', refs=['6:17', '6:18', '6:19'], text=(
  "Epiphanius, sch. 4: instead of \"coming down with them\" the text had \"he came down among them\" (κατέβη ἐν αὐτοῖς). "
  "Tertullian, Marc. 4.13.6: \"they gather from Tyre and other regions, a multitude even from across the sea\", which agrees in "
  "sense with the reading καὶ τῆς περαίας of ℵ* W and ff2. Roth rates both as probable or possible; they are noted, not printed. "
  "Epiphanius, sch. 5 quotes 6:19a with the singular ἐζήτει, printed here (Roth: very likely; NA27 ἐζήτουν). 6:18 is not cited "
  "and is printed in grey.")),
 dict(term='"Fortunate are the destitute, because theirs is the kingdom of God" (6:20)', cat='textual', refs=['6:20'], text=(
  "Tertullian, Marc. 4.14.1: \"Beati mendici (sic enim exigit interpretatio vocabuli quod in Graeco est), quoniam illorum est "
  "regnum dei\", repeated at 4.14.13. \"Illorum\" (theirs) cannot translate ὑμετέρα (yours). NA27 records αὐτῶν in W, the Old "
  "Latin ff2, the Old Syriac (sys) and the Sahidic, and cites Marcion (McionT). Roth: very likely. It is printed. Tertullian's "
  "beatitude has no \"in spirit\". Epiphanius, sch. 5 attests 6:20a.")),
 dict(term='The destitute as a named group', cat='theological', refs=['6:20', '6:24'], text=(
  "Interpretation. In the third person the beatitude describes a class of people, the destitute (οἱ πτωχοί), and assigns the kingdom to them; it "
  "is not only an address to the listeners. Paul's letters use the same word (οἱ πτωχοί, \"the poor\") for the Jerusalem community (Gal 2:10; Rom 15:26), "
  "and the Epistle of James says that God chose the poor of the world to be heirs of the kingdom (Jas 2:5) and pronounces woe on "
  "the rich (Jas 5:1; cf. Lk 6:24). Later writers name a Jewish-Christian group the Ebionites (from Hebrew ebyonim, \"the "
  "poor\"). The library identifies the community behind the text with that group (Carriers of Living Water §1). The attested "
  "wording of 6:20 is consistent with that identification. It does not prove it: the third person also stands in W, the Old "
  "Syriac and the Old Latin ff2.")),
 dict(term='The other beatitudes (6:21–23)', cat='textual', refs=['6:21', '6:22', '6:23'], text=(
  "Tertullian, Marc. 4.14.9–14 and 4.15.1; Epiphanius, sch. 6. Tertullian twice gives 6:21 in the third person and without "
  "\"now\" (\"Beati esurientes, quoniam ipsi saturabuntur\"; \"Beati qui plorant, quoniam ridebunt\"), and NA27 cites him for "
  "both. Roth rates these possible only, and the NA27 wording is printed. At 6:22 Tertullian lacks \"and when they set you apart\". "
  "6:23c is quoted by both witnesses, but they differ on the pronoun: Epiphanius has \"your fathers\" and Tertullian \"their "
  "fathers\" (= NA27). The previous note said 6:23c was a later addition to the text; both witnesses contradict that, and the note "
  "is withdrawn.")),
 dict(term='The woes (6:24–26)', cat='textual', refs=['6:24', '6:25', '6:26'], text=(
  "Tertullian, Marc. 4.15.3–14; Eznik, De Deo 405 (via Roth). Tertullian argues at length that woe on the rich is the Creator's "
  "language, which shows the woes stood in Marcion's text. At 6:25 he has no \"now\" after \"full\", and at 6:26 no \"all\"; "
  "NA27 cites Marcion for both omissions, with A D and others at 6:25 and D L and others at 6:26. Each rests on one witness and is "
  "noted, not printed. At 6:26 NA27's order ὑμᾶς καλῶς is printed (SBLGNT has καλῶς ὑμᾶς).")),
 dict(term='Love of enemies (6:27–31)', cat='textual', refs=['6:27', '6:28', '6:29', '6:30', '6:31'], text=(
  "Tertullian, Marc. 4.16.1–16; Adamantius (via Roth). Tertullian gives 6:27–28 as \"love your enemies, and bless those who hate "
  "you, and pray for those who slander you\". The previous text printed that compressed form, which Roth rates possible only; "
  "the NA27 wording is restored. At 6:29 Tertullian has the garments in Matthew's order. 6:30b is not cited. At 6:31 Tertullian's "
  "form is \"as you wish it to be done to you by people, so you also do to them\"; NA27 cites him for \"you also\". Only "
  "Tertullian attests it, and a Latin writer can recast the voice of a clause, so NA27 is printed (METHOD §5.4).")),
 dict(term='Lending, mercy, judging (6:32–38)', cat='textual', refs=['6:32', '6:33', '6:34', '6:35', '6:36', '6:37', '6:38'], text=(
  "Tertullian, Marc. 4.17.1–10. 6:32–33 are not cited and are printed in grey (6:33 with NA27's bracketed [γάρ]); 6:34b and 6:35a "
  "are not cited. Three Marcionite readings are printed because the Latin cannot render the NA27 Greek and Greek manuscripts carry "
  "the same reading (NA27 cites Marcion each time). At 6:36 there is no \"also\" (καί), with ℵ B L W. At 6:37 Tertullian has "
  "\"Nolite iudicare, ne iudicemini. Nolite condemnare, ne condemnemini\" (ἵνα μή twice), with D W and the Old Latin and Old "
  "Syriac. At 6:38 \"eadem qua mensi eritis mensura\" gives \"with the same measure\" (τῷ γὰρ αὐτῷ μέτρῳ), with 𝔓45vid A C "
  "and the Byzantine text. At 6:34 Tertullian's \"recepturos\" can render NA27's λαβεῖν, so the text is unchanged.")),
 dict(term='"Rain and sun": Tertullian\'s erasure charges', cat='textual', refs=['6:35'], text=(
  "Tertullian, Marc. 4.17.6, on 6:35b: \"Well done, Marcion: you have cleverly taken the rain and the sun away from him, so that "
  "he would not look like the Creator.\" The rain and sun stand in Matthew 5:45, not in any text of Luke. In the same way "
  "Tertullian charges three times (4.7.4, 4.9.15, 4.12.14) that Marcion erased \"I came not to destroy the law but to fulfil it\", "
  "which is Matthew 5:17 and stands in no manuscript of Luke. These charges measure Marcion's text against Matthew. They are "
  "evidence of what Tertullian expected a gospel to contain, not of what Luke contained, and they are not used as reports of "
  "content (METHOD §2).")),
 dict(term='Blind guides, the beam, the two trees, the two treasures (6:39–45)', cat='textual', refs=['6:39', '6:40', '6:41', '6:42', '6:43', '6:44', '6:45'], text=(
  "Tertullian, Marc. 4.17.11 cites these in sequence and turns them against Marcion, Cerdo and Apelles: \"the blind leads the "
  "blind into a pit… a learner is not above his master… let the heretic take the beam from his own eye… a good tree does not "
  "bear bad fruit… Marcion brought nothing good out of the evil treasure of Cerdo.\" 6:44 is not cited and is printed in grey. "
  "At 6:45 NA27 has no \"his\" after \"heart\" (SBLGNT adds αὐτοῦ).")),
 dict(term='The two trees in Marcion\'s church', cat='theological', refs=['6:43', '6:45'], text=(
  "Reception. Marcion's followers used 6:43 as their proof text for two gods, a good one and a just one (Origen, Princ. 2.5.4; "
  "Hippolytus, Haer. 10.19.3; cited via Roth; the library: Dancing with Fire). In the text the saying is applied to persons: "
  "6:45 explains the fruit as what a person brings out of the treasure of the heart. Tertullian makes the same point (\"which "
  "Christ applied figuratively to people, not to two gods\", Marc. 4.17.12). The two-gods reading belongs to the community that "
  "kept the text, not to its wording.")),
 dict(term='Hearing and doing (6:46–49)', cat='theological', refs=['6:46', '6:47', '6:48', '6:49'], text=(
  "Tertullian, Marc. 4.17.12–13 quotes 6:46: \"Why do you call me 'lord, lord'… and do not do what I say?\" 6:47–49 (the two "
  "houses) are not cited and are printed in grey. Interpretation: the sermon ends on doing, not on confessing. The Epistle of "
  "James makes the same demand (\"be doers of the word, and not hearers only\", Jas 1:22), and the library sets the two side by "
  "side (Carriers of Living Water §3.4). Of the three parallels the library draws inside this sermon (6:24 / Jas 5:1; 6:37 / Jas 5:9; "
  "6:46 / Jas 1:22), all three are attested for this text.")),
 dict(term='τῇ προσευχῇ τοῦ θεοῦ, "the prayer of God"', cat='translation', refs=['6:12'], text='The genitive is usually taken as "prayer to God". The Greek says "the prayer of God", and it is kept.'),
 dict(term='εἰς τὸ ὄρος, "into the mountain"', cat='translation', refs=['6:12'], text='With the article: "the mountain". As at 4:29, ὄρος covers hill and mountain.'),
 dict(term='διανυκτερεύων, "spending the whole night"', cat='translation', refs=['6:12'], text='One word: to pass the night through.'),
 dict(term='ἀποστόλους, "emissaries"', cat='translation', refs=['6:13'], text='ἀπόστολος is one sent out, from ἀποστέλλω, "send" (4:43). "Apostle" is the Greek word left untranslated, which later became a church title.'),
 dict(term='ζηλωτήν, "zealot"', cat='translation', refs=['6:15'], text='Literally "one who is zealous". It can mean zealous for the law, or a member of the later Zealot party. Lower case, as a description.'),
 dict(term='Ἰούδαν Ἰακώβου, "Judas of Jacob"', cat='translation', refs=['6:16'], text='The Greek gives only the genitive, "of Jacob": son or brother is not said. Ἰούδας is the name Judah.'),
 dict(term='Ἰσκαριώθ, "Iscarioth"', cat='translation', refs=['6:16'], text='The spelling of this text. The meaning of the name is not known; "man of Kerioth" is one proposal.'),
 dict(term='προδότης, "traitor"', cat='translation', refs=['6:16'], text='One who betrays, hands over.'),
 dict(term='καταβάς, "coming down"', cat='translation', refs=['6:17'], text='From the mountain of 6:12.'),
 dict(term='λαός, "people"', cat='translation', refs=['6:17'], text='The people as a nation, often Israel, as distinct from ὄχλος, "crowd".'),
 dict(term='ἰάομαι, "cure", and θεραπεύω, "heal"', cat='translation', refs=['6:18', '6:19'], text='Both verbs stand side by side here. They are kept apart as everywhere.'),
 dict(term='ἐζήτει, "was seeking"', cat='translation', refs=['6:19'], text='Singular with "the whole crowd": the reading of this text.'),
 dict(term='μακάριοι, "fortunate"', cat='translation', refs=['6:20'], text='μακάριος describes a state of good fortune, of being well off. "Blessed" is the usual rendering, but it is the English for a different Greek word, εὐλογέω (6:28), and merges the two.'),
 dict(term='οἱ πτωχοί, "the destitute"', cat='translation', refs=['6:20'], text='πτωχός is a beggar, someone with nothing, as distinct from πένης, someone poor who works. Tertullian insists that the word requires mendici, "beggars" (Marc. 4.14.1). "The poor" is too mild.'),
 dict(term='αὐτῶν, "theirs"', cat='translation', refs=['6:20'], text='Third person in this text; canonical Luke has "yours".'),
 dict(term='"those who hunger… you will be fed"', cat='translation', refs=['6:21'], text='The Greek moves from "those who" to "you" inside the sentence. The participle with the article can also be read as an address, "you who hunger".'),
 dict(term='χορτασθήσεσθε, "you will be fed"', cat='translation', refs=['6:21'], text='χορτάζω, to feed to the full; it is used of feeding animals until they are full.'),
 dict(term='ἀφορίσωσιν, "set you apart"', cat='translation', refs=['6:22'], text='To mark off, separate, exclude.'),
 dict(term='ἐκβάλωσιν τὸ ὄνομα, "throw out your name"', cat='translation', refs=['6:22'], text='The verb of 4:29 ("threw him out").'),
 dict(term='σκιρτήσατε, "leap"', cat='translation', refs=['6:23'], text='To leap, spring about.'),
 dict(term='μισθός, "wage"', cat='translation', refs=['6:23'], text='Pay for work, wages. "Reward" softens it. Again at 6:35.'),
 dict(term='ἐποίουν, "were doing"', cat='translation', refs=['6:23', '6:26'], text='The imperfect: what they used to do.'),
 dict(term='ἀπέχετε, "you are holding… in full"', cat='translation', refs=['6:24'], text='A word of commerce: to have received payment in full and give a receipt.'),
 dict(term='παράκλησιν, "comfort"', cat='translation', refs=['6:24'], text='Consolation, encouragement, comfort.'),
 dict(term='ἐμπεπλησμένοι, "who have been filled up"', cat='translation', refs=['6:25'], text='A perfect participle: filled full and staying full.'),
 dict(term='καλῶς εἴπωσιν, "speak well of"', cat='translation', refs=['6:26'], text='Literally "say finely of you".'),
 dict(term='ἀγαπᾶτε, "love"', cat='translation', refs=['6:27'], text='ἀγαπάω is the ordinary Greek verb for loving. The idea that it names a special, divine kind of love is a later theological reading, not a feature of the word.'),
 dict(term='τοῖς ἀκούουσιν, "to those who are hearing"', cat='translation', refs=['6:27'], text='The present participle: those who are listening now.'),
 dict(term='εὐλογεῖτε, "bless"', cat='translation', refs=['6:28'], text='To speak well of, to bless. A different word from μακάριος, "fortunate" (6:20).'),
 dict(term='ἐπηρεαζόντων, "mistreat"', cat='translation', refs=['6:28'], text='To abuse, insult, treat spitefully.'),
 dict(term='σιαγόνα, "jaw"', cat='translation', refs=['6:29'], text='The jaw or cheek.'),
 dict(term='ἱμάτιον, χιτών, "cloak", "tunic"', cat='translation', refs=['6:29'], text='The outer garment and the one worn next to the skin.'),
 dict(term='δίδου, "keep giving"', cat='translation', refs=['6:30'], text='A present imperative: give, and go on giving.'),
 dict(term='χάρις, "favour"', cat='translation', refs=['6:32'], text='Goodwill, a gift given freely, and the thanks or credit that answers it. Here: what credit is there in it for you?'),
 dict(term='μηδὲν ἀπελπίζοντες, "despairing of nothing"', cat='translation', refs=['6:35'], text='The usual sense of ἀπελπίζω is "to give up hope, despair". The common rendering "expecting nothing in return" reads it from ἐλπίζω in 6:34, "hope to receive". Both senses are possible. The ordinary one is kept.'),
 dict(term='υἱοί, "sons"', cat='translation', refs=['6:35'], text='A male plural, used of a whole group. The Greek word is kept.'),
 dict(term='Ὑψίστου, "the Highest"', cat='translation', refs=['6:35'], text='A name for God, "the Most High". Capitalised as a name.'),
 dict(term='χρηστός, "kind"', cat='translation', refs=['6:35'], text='Good, useful, kind. In speech it sounded almost the same as χριστός, "anointed".'),
 dict(term='ἀχαρίστους, "the ungrateful"', cat='translation', refs=['6:35'], text='Literally "without favour" (χάρις, 6:32–34): those who give no thanks.'),
 dict(term='γίνεσθε, "become"', cat='translation', refs=['6:36'], text='To come to be. The present imperative: keep becoming.'),
 dict(term='οἰκτίρμονες, "compassionate"', cat='translation', refs=['6:36'], text='Feeling pity. It is not ἐλεήμων, "merciful", which the English often uses here.'),
 dict(term='ἵνα μή, "so that… not"', cat='translation', refs=['6:37'], text='The reading of this text: a purpose clause ("so that you may not be judged"). Canonical Luke has a promise ("and you will not be judged").'),
 dict(term='ἀπολύετε, "release"', cat='translation', refs=['6:37'], text='To set free, to discharge: a prisoner, a debtor. "Forgive" or "pardon" narrows it to one case.'),
 dict(term='μέτρον καλόν, "a fine measure"', cat='translation', refs=['6:38'], text='καλός, fine, good to look at. It is kept apart from ἀγαθός, "good" (6:45).'),
 dict(term='δώσουσιν, "they will give"', cat='translation', refs=['6:38'], text='An impersonal plural, "people will give". The Semitic way of speaking often uses it to avoid naming God.'),
 dict(term='κόλπον, "fold"', cat='translation', refs=['6:38'], text='The fold of the garment at the chest, used as a pocket. The same word is the "bosom" of Abraham (16:22).'),
 dict(term='ὑπερεκχυννόμενον, "pouring over"', cat='translation', refs=['6:38'], text='Running over the brim.'),
 dict(term='Μήτι, "can…?"', cat='translation', refs=['6:39'], text='A question that expects "no".'),
 dict(term='κατηρτισμένος, "fully trained"', cat='translation', refs=['6:40'], text='To put in order, make complete, mend. It is the verb used for mending nets.'),
 dict(term='κάρφος, δοκός, "splinter", "beam"', cat='translation', refs=['6:41'], text='A dry stalk or splinter, and a roof beam.'),
 dict(term='ἄφες, "let"', cat='translation', refs=['6:42'], text='ἀφίημι, "let go, let": the verb of "let sins go" (5:20).'),
 dict(term='ἐκβάλω, "throw out"', cat='translation', refs=['6:42'], text='The verb of 4:29 and of driving out daimons.'),
 dict(term='ὑποκριτά, "play-actor"', cat='translation', refs=['6:42'], text='ὑποκριτής is a stage actor, one who plays a part. "Hypocrite" is the Greek word left untranslated.'),
 dict(term='ἀδελφός, "brother"', cat='translation', refs=['6:42'], text='Kept as the Greek word, though it is used of fellow members of a community.'),
 dict(term='καλόν, σαπρόν, "fine", "rotten"', cat='translation', refs=['6:43'], text='καλός is fine, sound. σαπρός is rotten, decayed.'),
 dict(term='ἀγαθός, πονηρός, "good", "evil"', cat='translation', refs=['6:45'], text='ἀγαθός is good in itself. πονηρός is evil, malicious, worthless.'),
 dict(term='περισσεύματος, "overflow"', cat='translation', refs=['6:45'], text='What is more than enough, the surplus.'),
 dict(term='Κύριε κύριε, "lord, lord"', cat='translation', refs=['6:46'], text='The ordinary address to a master. In lower case, because it is not the divine name.'),
 dict(term='λόγων, "words"', cat='translation', refs=['6:47'], text='λόγος, as at 4:32.'),
 dict(term='ἐβάθυνεν, "went deep"', cat='translation', refs=['6:48'], text='From βάθος, "the deep" (5:4).'),
 dict(term='πέτραν, "the rock"', cat='translation', refs=['6:48'], text='πέτρα is bedrock, a rock mass. Πέτρος (Peter, 6:14) is the masculine form, "a stone".'),
 dict(term='προσέρηξεν, "broke against"', cat='translation', refs=['6:48'], text='To dash against, break upon.'),
 dict(term='ῥῆγμα, "breaking"', cat='translation', refs=['6:49'], text='A breaking, a rupture. It is from ῥήγνυμι, "burst" (5:37).'),
]
