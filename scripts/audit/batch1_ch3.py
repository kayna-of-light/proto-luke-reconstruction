"""Batch 1, chapter 3 of the reconstruction: Luke 6:12–49."""
from buildlib import greek
from batch1_ch2 import U, A

T4171 = {'source': 'Tertullian, Marc. 4.17.11', 'evidence': '"Sed caecus caecum ducit in foveam… Sed non est discipulus super magistrum… Eximat et de oculo suo trabem haereticus, tunc in oculo Christiani si quam putat stipulam revincat. Proinde et arbor bona non proferat malum fructum… nec mala bonum… Sic nec Marcion aliquid boni de thesauro Cerdonis malo protulit".'}

ENTRIES = [
 A('6:12', greek('6:12'), 'In those days he went out to the mountain to pray, and he spent the night in the prayer of God.',
   'present (Marc. 4.13.1)', [{'source': 'Tertullian, Marc. 4.13.1', 'evidence': '"ascendit in montem et illic pernoctat in oratione".'}]),
 A('6:13', greek('6:13'), 'When day came, he called his disciples and chose twelve of them, whom he also designated emissaries:',
   'present (Marc. 4.13.4)', [{'source': 'Tertullian, Marc. 4.13.4', 'evidence': 'The number twelve and its figures; "Totidem enim apostoli portendebantur".'}]),
 A('6:14', greek('6:14'), 'Simon, whom he also named Peter, and Andrew his brother, and James and John, and Philip and Bartholomew,',
   'present (Marc. 4.13.6)', [{'source': 'Tertullian, Marc. 4.13.6', 'evidence': 'Why Simon was given the name Peter ("petra et lapis Christus").'}],
   wording='NA27. Only the naming of Simon as Peter is cited; the other names are printed in the NA27 wording within the attested verse.'),
 U('6:15', greek('6:15', [('Ζηλωτὴν', 'ζηλωτὴν')]), 'and Matthew and Thomas, and James son of Alphaeus, and Simon who was called the zealot,',
   'Inside the attested list 6:13–16. The previous text printed ellipses here (research question Q3c); the verse is now printed and flagged.'),
 A('6:16', greek('6:16'), 'and Judas son of James, and Judas Iscariot, who became a traitor.',
   'present (Marc. 2.28.2; Pan. 42.11.6, sch. 4)',
   [{'source': 'Epiphanius, Pan. 42.11.6, sch. 4', 'evidence': '»Ἰούδαν Ἰσκαριώτην, ὃς ἐγένετο προδότης« (Holl\'s text; manuscripts V and M read -ώθ).'},
    {'source': 'Tertullian, Marc. 2.28.2 (via Roth loci)', 'evidence': 'Judas the traitor.'}],
   wording='NA27 (Ἰσκαριώθ). NA27 cites McionE for Ἰσκαριώτην on the basis of Holl\'s emended text; the Epiphanius manuscripts V and M have -ώθ. Roth leaves the form open. Not changed.'),
 A('6:17', greek('6:17'), 'He came down with them and stood on a level place, with a great crowd of his disciples and a great multitude of people from all Judea and Jerusalem and the coast of Tyre and Sidon,',
   'present (Marc. 4.13.7; Pan. 42.11.6, sch. 4)',
   [{'source': 'Epiphanius, Pan. 42.11.6, sch. 4', 'evidence': 'ἀντὶ δὲ τοῦ »κατέβη μετ\' αὐτῶν« ἔχει »κατέβη ἐν αὐτοῖς«.'},
    {'source': 'Tertullian, Marc. 4.13.6', 'evidence': '"Conveniunt a Tyro et ex aliis regionibus multitudo etiam transmarina."'}],
   wording='NA27. Epiphanius reports ἐν αὐτοῖς for μετ\' αὐτῶν (Roth: probable only). Tertullian\'s "transmarina" agrees in sense with καὶ τῆς περαίας (ℵ* W ff2; "et trans fretum" it vgmss; Roth: possible). Both noted, not adopted.'),
 U('6:18', greek('6:18'), 'who had come to hear him and to be healed of their diseases; and those who were troubled by unclean spirits were healed.',
   'Inside the attested passage 6:17–19.'),
 A('6:19', greek('6:19', [('ἐζήτουν', 'ἐζήτει')]), 'And the whole crowd was trying to touch him, for power was going out from him and healing them all.',
   'present (Pan. 42.11.6, sch. 5)',
   [{'source': 'Epiphanius, Pan. 42.11.6, sch. 5', 'evidence': '»καὶ πᾶς ὁ ὄχλος ἐζήτει ἅπτεσθαι αὐτοῦ. καὶ αὐτὸς ἐπάρας τοὺς ὀφθαλμοὺς αὐτοῦ« καὶ τὰ ἑξῆς.'}],
   wording='Marcionite reading adopted: ἐζήτει (Epiphanius\' Greek; Roth: very likely). NA27 ἐζήτουν; the singular is also the Byzantine reading. A singular verb with a collective subject could be Epiphanius\' own correction; noted.'),
 A('6:20', greek('6:20', [('ὅτι ὑμετέρα ἐστὶν', 'ὅτι αὐτῶν ἐστιν')]),
   'Then he lifted up his eyes to his disciples and said: "Blessed are the poor, for theirs is the kingdom of God.',
   'present (Marc. 4.14.1, 9, 13; Pan. 42.11.6, sch. 5; Eznik, De Deo 405)',
   [{'source': 'Tertullian, Marc. 4.14.1', 'evidence': '"Beati mendici (sic enim exigit interpretatio vocabuli quod in Graeco est), quoniam illorum est regnum dei."'},
    {'source': 'Tertullian, Marc. 4.14.13', 'evidence': '"Beati mendici, quoniam illorum est regnum caelorum."'},
    {'source': 'Epiphanius, Pan. 42.11.6, sch. 5', 'evidence': '»καὶ αὐτὸς ἐπάρας τοὺς ὀφθαλμοὺς αὐτοῦ« (6:20a).'}],
   wording='Marcionite reading adopted: αὐτῶν for ὑμετέρα. Latin "illorum" cannot render ὑμετέρα. NA27 apparatus: αὐτῶν W ff2 sys sa bomss; McionT. Roth: very likely. No "in spirit" (τῷ πνεύματι is added in ℵ2 Q Θ f1.13 33 al).',
   western='Agrees with W, Old Latin ff2 and the Old Syriac (sys).'),
 A('6:21', greek('6:21'), 'Blessed are you who hunger now, for you will be filled. Blessed are you who weep now, for you will laugh.',
   'present (Marc. 4.14.9, 11, 13)',
   [{'source': 'Tertullian, Marc. 4.14.9, 13', 'evidence': '"Beati esurientes, quoniam ipsi saturabuntur"; "Beati qui esuriunt, quoniam saturabuntur… Beati qui plorant, quoniam ridebunt."'}],
   wording='NA27. Tertullian has the third person and no "now" twice. NA27 apparatus: νῦν om. bis McionT (Eus); -σονται ℵ*.c pc it sys samss; McionT Or; -σουσιν W e sys samss; McionT. Roth: possible only. Noted, not adopted.'),
 A('6:22', greek('6:22'), 'Blessed are you when people hate you, and when they exclude you and revile you and cast out your name as evil on account of the son of man.',
   'present (Marc. 4.14.14)',
   [{'source': 'Tertullian, Marc. 4.14.14', 'evidence': '"Beati eritis cum vos odio habebunt homines et exprobrabunt et eicient nomen vestrum velut nequam propter filium hominis."'}],
   wording='NA27. Tertullian lacks "and when they exclude you" (NA27: om. 2542 McionT) and has future verbs (Roth: possible). Noted, not adopted.'),
 A('6:23', greek('6:23'), 'Rejoice in that day and leap for joy, for your reward is great in heaven; for that is what their fathers did to the prophets.',
   'present (Marc. 4.15.1; Pan. 42.11.6, sch. 6)',
   [{'source': 'Epiphanius, Pan. 42.11.6, sch. 6', 'evidence': '»κατὰ τὰ αὐτὰ ἐποίουν τοῖς προφήταις οἱ πατέρες ὑμῶν«.'},
    {'source': 'Tertullian, Marc. 4.15.1', 'evidence': '"Secundum haec, inquit, faciebant prophetis patres eorum."'}],
   wording='NA27. The witnesses disagree: Epiphanius "your fathers", Tertullian "their fathers" (= NA27). Neither has γάρ, but both quote from the start of the clause. Not changed.'),
 A('6:24', greek('6:24'), 'But woe to you who are rich, for you have received your consolation.',
   'present (Marc. 4.15.3, 9; Eznik, De Deo 405)',
   [{'source': 'Tertullian, Marc. 4.15.8–9', 'evidence': '"a Christo dirigitur in divites… Vae divitibus… Quoniam, inquit, recepistis advocationem vestram".'}]),
 A('6:25', greek('6:25'), 'Woe to you who are full now, for you will hunger. Woe, you who laugh now, for you will mourn and weep.',
   'present (Marc. 4.15.13)',
   [{'source': 'Tertullian, Marc. 4.15.13', 'evidence': '"Ingerit Vae etiam saturatis, quia esurient, etiam ridentibus nunc, quia lugebunt."'}],
   wording='NA27. Tertullian has no "now" with "full" (NA27: om. A D K P Γ Ψ 565 2542* 𝔐 lat syp; McionT Irlat). Roth rates the absence "likely"; one witness. Noted, not adopted.'),
 A('6:26', greek('6:26', [('καλῶς ὑμᾶς εἴπωσιν', 'ὑμᾶς καλῶς εἴπωσιν')]),
   'Woe when all people speak well of you, for that is what their fathers did to the false prophets."',
   'present (Marc. 4.15.14)',
   [{'source': 'Tertullian, Marc. 4.15.14', 'evidence': '"Vae, cum vobis benedixerint homines. Secundum haec faciebant et pseudoprophetis patres illorum."'}],
   wording='NA27 (ὑμᾶς καλῶς; SBLGNT καλῶς ὑμᾶς — checked on the page image). Tertullian lacks "all" (NA27: οἱ ἄνθρωποι without πάντες D L Γ Δ 892* pm vgcl sys.p bomss; McionT; Roth: "may not have been present"). Noted, not adopted.'),
 A('6:27', greek('6:27'), 'But I say to you who are listening: Love your enemies, do good to those who hate you,',
   'present (Marc. 4.16.1; Adam. 26,20–21; 88,26)',
   [{'source': 'Tertullian, Marc. 4.16.1', 'evidence': '"Sed vobis dico, inquit, qui auditis… diligite inimicos vestros, et benedicite eos qui vos oderunt, et orate pro eis qui vos calumniantur."'}],
   wording='NA27. Tertullian compresses 6:27b–28a into "bless those who hate you" (Roth: possible). The previous text printed that compressed form; NA27 is restored.'),
 A('6:28', greek('6:28'), 'bless those who curse you, pray for those who mistreat you.',
   'present (Marc. 4.16.1; Adam. 26,20–21)', [{'source': 'Tertullian, Marc. 4.16.1', 'evidence': 'see 6:27.'}]),
 A('6:29', greek('6:29'), 'To the one who strikes you on the cheek, offer the other also; and from the one who takes your cloak, do not withhold your tunic either.',
   'present (Marc. 4.16.2, 6; Adam. 32,5–6; 38,2–3)',
   [{'source': 'Tertullian, Marc. 4.16.2, 6', 'evidence': '"alteram amplius maxillam offerri iubens, et super tunicam pallio quoque cedi"; "non modo non retinendi tunicam sed et amplius et pallium concedendi".'}],
   wording='NA27. Tertullian has the garments in Matthew\'s order, tunic then cloak (Roth: possible). Noted, not adopted.'),
 A('6:30', greek('6:30'), 'Give to everyone who asks of you; and from the one who takes what is yours, do not demand it back.',
   'present for 6:30a (Marc. 4.16.8); 6:30b unattested',
   [{'source': 'Tertullian, Marc. 4.16.8', 'evidence': '"Omni petenti te dato".'}],
   wording='NA27. 6:30b is not cited; printed within the attested verse.'),
 A('6:31', greek('6:31'), 'And as you wish that people would do to you, do the same to them.',
   'present (Marc. 4.16.13, 16)',
   [{'source': 'Tertullian, Marc. 4.16.13', 'evidence': '"Et sicut vobis fieri vultis ab hominibus, ita et vos facite illis."'}],
   wording='NA27. Tertullian\'s form is passive ("as you wish it to be done to you by people") and has "you also" (καὶ ὑμεῖς: ℵ A D L W Θ Ξ Ψ f1.13 33 𝔐; (McionT) in NA27). Roth rates ὑμῖν γίνεσθαι θέλετε παρὰ ἀνθρώπων very likely. Only Tertullian attests it, and a Latin writer can recast the voice of a clause; the NA27 Greek can stand behind his Latin (METHOD §5.4). Noted, not adopted.'),
 U('6:32', greek('6:32'), 'If you love those who love you, what credit is that to you? For even sinners love those who love them.',
   'Inside the attested passage 6:27–36.'),
 U('6:33', greek('6:33', [('καὶ ἐὰν ἀγαθοποιῆτε', 'καὶ γὰρ ἐὰν ἀγαθοποιῆτε')]), 'And if you do good to those who do good to you, what credit is that to you? Even sinners do the same.',
   'Inside the attested passage 6:27–36. NA27 brackets [γάρ]; printed.'),
 A('6:34', greek('6:34'), 'And if you lend to those from whom you hope to receive, what credit is that to you? Even sinners lend to sinners, to receive as much again.',
   'present for 6:34a (Marc. 4.17.1); 6:34b unattested',
   [{'source': 'Tertullian, Marc. 4.17.1', 'evidence': '"Et si feneraveritis a quibus speratis vos recepturos, quae gratia est vobis?"'}],
   wording='NA27, with the bracketed [ἐστίν]. Tertullian\'s "recepturos" is read by Roth as ἀπολαβεῖν (very likely), but "recipere" is also the Latin for λαβεῖν here (so the Vulgate), and no Greek manuscript in NA27 reads ἀπολαβεῖν. Noted, not adopted. 6:34b is not cited.'),
 A('6:35', greek('6:35'), 'But love your enemies, do good, and lend, expecting nothing in return; and your reward will be great, and you will be sons of the Most High, for he is kind to the ungrateful and the wicked.',
   'present for 6:35b (Marc. 4.17.5–6); 6:35a unattested',
   [{'source': 'Tertullian, Marc. 4.17.5–6', 'evidence': '"Ille me nunc rursus filium nuncupat… Quia ipse, inquit, suavis est adversus ingratos et malos."'}],
   wording='NA27. 6:35a is not cited; printed within the attested verse. Roth reads υἱοὶ θεοῦ for υἱοὶ ὑψίστου (possible only); not adopted.'),
 A('6:36', greek('6:36'), 'Be merciful, as your Father is merciful.',
   'present (Marc. 4.17.8)',
   [{'source': 'Tertullian, Marc. 4.17.8', 'evidence': '"Estote, inquit, misericordes, sicut pater vester misertus est vestri."'}],
   wording='NA27 without its bracketed [καί]: Tertullian has "sicut", not "sicut et", and NA27 cites McionT with ℵ B L W Ξ Ψ for the omission. Tertullian\'s "misertus est vestri" (ᾤκτειρεν ὑμᾶς) is rated possible by Roth; noted, not adopted.'),
 A('6:37', greek('6:37', [('καὶ οὐ μὴ κριθῆτε', 'ἵνα μὴ κριθῆτε'), ('καὶ οὐ μὴ καταδικασθῆτε', 'ἵνα μὴ καταδικασθῆτε')]),
   'Do not judge, so that you may not be judged; do not condemn, so that you may not be condemned. Pardon, and you will be pardoned.',
   'present (Marc. 4.17.9)',
   [{'source': 'Tertullian, Marc. 4.17.9', 'evidence': '"Nolite iudicare, ne iudicemini. Nolite condemnare, ne condemnemini. Dimittite, et dimittemini."'}],
   wording='Marcionite reading adopted: ἵνα μή twice. Latin "ne" with the subjunctive renders ἵνα μή, not καὶ οὐ μή. NA27 apparatus: ἵνα A D W Ψ pc a c e f sys sa bopt; McionT (first clause); ἵνα D W* it sys sa; McionT (second). Roth: very likely. Tertullian has no "and" before either prohibition (Roth: καί "likely not present"); one witness, not adopted.',
   western='Agrees with D, W and the Old Latin and Old Syriac.'),
 A('6:38', greek('6:38', [('ᾧ γὰρ μέτρῳ μετρεῖτε', 'τῷ γὰρ αὐτῷ μέτρῳ ᾧ μετρεῖτε')]),
   'Give, and it will be given to you: a good measure, pressed down, shaken together, running over, will be put into your lap. For with the same measure with which you measure, it will be measured back to you."',
   'present (Marc. 4.17.9; Adam. 32,17–18; 66,32–33)',
   [{'source': 'Tertullian, Marc. 4.17.9', 'evidence': '"Date, et dabitur vobis, mensuram bonam, pressam ac fluentem, dabunt in sinum vestrum. Eadem qua mensi eritis mensura, remetietur vobis."'}],
   wording='Marcionite reading adopted: τῷ γὰρ αὐτῷ μέτρῳ ᾧ. Latin "eadem" requires αὐτῷ. NA27 apparatus: 𝔓45vid A C Θ Ψ f13 𝔐 lat syh; McionT. Roth: very likely. Tertullian lacks "shaken together" (Roth: "may have been present"); not adopted.'),
 A('6:39', greek('6:39'), 'He also told them a parable: "Can a blind man lead a blind man? Will they not both fall into a pit?',
   'present (Marc. 4.17.11)', [T4171]),
 A('6:40', greek('6:40'), 'A disciple is not above the teacher; but everyone who is fully trained will be like his teacher.',
   'present (Marc. 4.17.11)', [T4171],
   wording='NA27 (no αὐτοῦ after the first διδάσκαλον, which A C Ψ 𝔐 add; Tertullian "magistrum" without "suum").'),
 A('6:41', greek('6:41'), 'Why do you see the speck in your brother\'s eye, but do not notice the beam in your own eye?',
   'present (Marc. 4.17.11)', [T4171]),
 A('6:42', greek('6:42', [('ὀφθαλμῷ σοῦ δοκὸν', 'ὀφθαλμῷ σου δοκὸν'), ('ὀφθαλμοῦ σοῦ, καὶ', 'ὀφθαλμοῦ σου, καὶ')]),
   'How can you say to your brother, "Brother, let me take out the speck in your eye," when you yourself do not see the beam in your own eye? Hypocrite, first take the beam out of your own eye, and then you will see clearly to take out the speck in your brother\'s eye.',
   'present (Marc. 4.17.11)', [T4171]),
 A('6:43', greek('6:43'), 'For no good tree bears bad fruit, nor again does a bad tree bear good fruit.',
   'present (Marc. 4.17.11; Adam. 56,14–16; 58,11–13; Origen, Princ. 2.5.4; Hippolytus, Haer. 10.19.3; Ps.-Tertullian 6.2; Philastrius 45.2)', [T4171],
   wording='NA27. Roth: the wording is obscured by the many citations; good tree before bad tree, and the verb ποιέω, are clear. NA27 agrees.'),
 U('6:44', greek('6:44'), 'For each tree is known by its own fruit. Figs are not gathered from thorns, nor are grapes picked from a bramble.',
   'Inside the attested passage 6:43–45; Tertullian passes from the trees to the treasure.'),
 A('6:45', greek('6:45', [('τῆς καρδίας αὐτοῦ προφέρει', 'τῆς καρδίας προφέρει')]),
   'The good person brings forth good out of the good treasure of the heart, and the evil person brings forth evil out of the evil; for the mouth speaks out of the abundance of the heart.',
   'present (Marc. 4.17.11; [Adam. 58,18–20]; Origen, Princ. 2.5.4)', [T4171],
   wording='NA27 (no αὐτοῦ after καρδίας; SBLGNT has it — checked on the page image).'),
 A('6:46', greek('6:46'), 'Why do you call me "Lord, Lord", and do not do what I say?',
   'present (Marc. 4.17.12–13)',
   [{'source': 'Tertullian, Marc. 4.17.12–13', 'evidence': '"quis videbitur dixisse, Quid vocas, Domine, domine?… Quis item adiecisse potuisset, Et non facitis quae dico?"'}]),
 U('6:47', greek('6:47'), 'Everyone who comes to me and hears my words and does them, I will show you what he is like:',
   'Inside the passage opened by the attested 6:46.'),
 U('6:48', greek('6:48'), 'he is like a man building a house, who dug deep and laid the foundation on the rock. When a flood came, the river burst against that house and could not shake it, because it had been well built.',
   'Inside the passage opened by the attested 6:46.'),
 U('6:49', greek('6:49'), 'But the one who hears and does not do is like a man who built a house on the ground without a foundation. The river burst against it, and at once it collapsed, and the ruin of that house was great."',
   'Inside the passage opened by the attested 6:46.'),
]

OMITTED = []

PREAMBLE = (
 "The choosing of the twelve and the teaching given on the level place. Tertullian works through the sermon almost line by line "
 "(Marc. 4.13–4.17), so for this chapter the evidence is dense, and in several places the witnesses show the wording of "
 "Marcion's text where it differs from the canonical one. The blessing is spoken of the poor in the third person: \"Blessed are "
 "the poor, for theirs is the kingdom of God.\" Tertullian notes that the Greek word means beggars. Blessings on the poor, the "
 "hungry and those who weep are matched by woes on the rich, the full and those who laugh. Then come the love of enemies, mercy, "
 "not judging, the measure that is returned, the two trees and the two treasures, and the question \"Why do you call me Lord, "
 "Lord, and do not do what I say?\". The emphasis throughout falls on what a person does. Three of the sayings the library pairs "
 "with the Epistle of James (6:24, 6:37, 6:46) are attested by the witnesses."
)

NOTES = [
 dict(term='The twelve (6:12–16)', cat='textual', refs=['6:12', '6:13', '6:14', '6:15', '6:16'], text=(
  "Tertullian, Marc. 4.13.1–6: he went up the mountain and spent the night in prayer, chose twelve (with figures of the number "
  "from the Creator's scriptures), and named Simon Peter. Epiphanius, sch. 4: »Ἰούδαν Ἰσκαριώτην, ὃς ἐγένετο προδότης«. The "
  "other names are not cited. 6:14 is printed whole because the verse is attested; 6:15 is printed in grey. The previous text "
  "replaced 6:15 with ellipses (research question Q3c); that is superseded. On the form of Judas' surname: NA27 prints "
  "Ἰσκαριώθ and cites Marcion (McionE) for Ἰσκαριώτην, but that rests on Holl's emendation of Epiphanius; his manuscripts V and "
  "M read -ώθ. The NA27 form is kept. The previous note presented Ἰσκαριώθ as a Marcionite reading; it is withdrawn.")),
 dict(term='Emissaries (ἀποστόλους)', cat='translation', refs=['6:13'], text=(
  "ἀπόστολος is rendered \"emissary\", its ordinary sense (one sent out), rather than with the later title \"apostle\".")),
 dict(term='The descent and the crowd (6:17–19)', cat='textual', refs=['6:17', '6:18', '6:19'], text=(
  "Epiphanius, sch. 4: instead of \"he came down with them\" the text had \"he came down among them\" (κατέβη ἐν αὐτοῖς). "
  "Tertullian, Marc. 4.13.6: \"they gather from Tyre and other regions, a multitude even from across the sea\", which agrees in "
  "sense with the reading καὶ τῆς περαίας of ℵ* W and ff2. Roth rates both as probable or possible; they are noted, not printed. "
  "Epiphanius, sch. 5 quotes 6:19a with the singular ἐζήτει, printed here (Roth: very likely; NA27 ἐζήτουν). 6:18 is not cited "
  "and is printed in grey.")),
 dict(term='"Blessed are the poor, for theirs is the kingdom of God" (6:20)', cat='textual', refs=['6:20'], text=(
  "Tertullian, Marc. 4.14.1: \"Beati mendici (sic enim exigit interpretatio vocabuli quod in Graeco est), quoniam illorum est "
  "regnum dei\", repeated at 4.14.13. \"Illorum\" (theirs) cannot translate ὑμετέρα (yours). NA27 records αὐτῶν in W, the Old "
  "Latin ff2, the Old Syriac (sys) and the Sahidic, and cites Marcion (McionT). Roth: very likely. It is printed. Tertullian's "
  "blessing has no \"in spirit\". Epiphanius, sch. 5 attests 6:20a.")),
 dict(term='The poor (πτωχοί)', cat='translation', refs=['6:20'], text=(
  "πτωχός means the destitute, someone who has to beg, not merely a person of small means. Tertullian insists on the point: the "
  "Greek word \"requires\" mendici, beggars (Marc. 4.14.1). The translation keeps \"the poor\" because that is the form in which "
  "the word became a community's name (next note), but it means the destitute.")),
 dict(term='The poor as a named group', cat='theological', refs=['6:20', '6:24'], text=(
  "Interpretation. In the third person the blessing describes a class of people, the poor, and assigns the kingdom to them; it "
  "is not only an address to the listeners. Paul's letters use \"the poor\" for the Jerusalem community (Gal 2:10; Rom 15:26), "
  "and the Epistle of James says that God chose the poor of the world to be heirs of the kingdom (Jas 2:5) and pronounces woe on "
  "the rich (Jas 5:1; cf. Lk 6:24). Later writers name a Jewish-Christian group the Ebionites (from Hebrew ebyonim, \"the "
  "poor\"). The library identifies the community behind the text with that group (Carriers of Living Water §1). The attested "
  "wording of 6:20 is consistent with that identification. It does not prove it: the third person also stands in W, the Old "
  "Syriac and the Old Latin ff2.")),
 dict(term='The other blessings (6:21–23)', cat='textual', refs=['6:21', '6:22', '6:23'], text=(
  "Tertullian, Marc. 4.14.9–14 and 4.15.1; Epiphanius, sch. 6. Tertullian twice gives 6:21 in the third person and without "
  "\"now\" (\"Beati esurientes, quoniam ipsi saturabuntur\"; \"Beati qui plorant, quoniam ridebunt\"), and NA27 cites him for "
  "both. Roth rates these possible only, and the NA27 wording is printed. At 6:22 Tertullian lacks \"and when they exclude you\". "
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
  "blind into a pit… a disciple is not above his master… let the heretic take the beam from his own eye… a good tree does not "
  "bear bad fruit… Marcion brought nothing good out of the evil treasure of Cerdo.\" 6:44 is not cited and is printed in grey. "
  "At 6:45 NA27 has no \"his\" after \"heart\" (SBLGNT adds αὐτοῦ).")),
 dict(term='The two trees in Marcion\'s church', cat='theological', refs=['6:43', '6:45'], text=(
  "Reception. Marcion's followers used 6:43 as their proof text for two gods, a good one and a just one (Origen, Princ. 2.5.4; "
  "Hippolytus, Haer. 10.19.3; cited via Roth; the library: Dancing with Fire). In the text the saying is applied to persons: "
  "6:45 explains the fruit as what a person brings out of the treasure of the heart. Tertullian makes the same point (\"which "
  "Christ applied figuratively to people, not to two gods\", Marc. 4.17.12). The two-gods reading belongs to the community that "
  "kept the text, not to its wording.")),
 dict(term='Hearing and doing (6:46–49)', cat='theological', refs=['6:46', '6:47', '6:48', '6:49'], text=(
  "Tertullian, Marc. 4.17.12–13 quotes 6:46: \"Why do you call me Lord, Lord… and do not do what I say?\" 6:47–49 (the two "
  "houses) are not cited and are printed in grey. Interpretation: the sermon ends on doing, not on confessing. The Epistle of "
  "James makes the same demand (\"be doers of the word, and not hearers only\", Jas 1:22), and the library sets the two side by "
  "side (Carriers of Living Water §3.4). Of the three parallels the library draws inside this sermon (6:24 / Jas 5:1; 6:37 / Jas 5:9; "
  "6:46 / Jas 1:22), all three are attested for this text.")),
]
