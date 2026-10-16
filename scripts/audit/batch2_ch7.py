"""Batch 2, chapter 7 of the reconstruction: Luke 9:18–62."""
from buildlib import greek
from batch1_ch2 import U, A
from batch2_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}
AD = lambda loc, ev: {'source': f'Dialogue of Adamantius {loc} (via Roth)', 'evidence': ev}

ENTRIES = [
 A('9:18', G('9:18'), 'And it happened, while he was praying alone, that the learners were with him, and he asked them, saying, "Who do the crowds say that I am?"',
   'present (Adam. 84,1–2)', [AD('84,1–2 (2.13)', 'Quoted in the dialogue; Roth counts it as attested (wording possible only).')],
   wording='NA27 (order λέγουσιν οἱ ὄχλοι; SBLGNT differs — checked on the page image).'),
 A('9:19', G('9:19'), 'And they answered and said, "John the baptiser; but others, Elijah; and others, that one of the prophets of old has stood up."',
   'present (Adam. 84,2–4)', [AD('84,2–4 (2.13)', 'Quoted in the dialogue.')]),
 A('9:20', G('9:20'), 'And he said to them, "But you, who do you say that I am?" And Peter answered and said, "The Anointed One of God."',
   'present (Marc. 4.21.6; Adam. 84,4–5)', [T('4.21.6', '"interroganti domino quisnam illis videretur… Tu es Christus".')],
   wording='NA27. Tertullian\'s answer is "Tu es Christus", without "of God"; Roth notes that "of God" may have been missing. One witness, in paraphrase; not adopted.'),
 A('9:21', G('9:21'), 'But he, rebuking them, ordered them to tell this to no one,',
   'present (Marc. 4.21.6)', [T('4.21.6', '"immo et silentium indicens… praecepit ne cui hoc dicerent".')]),
 A('9:22', G('9:22', [('καὶ τῇ τρίτῃ ἡμέρᾳ ἐγερθῆναι.', 'καὶ μετὰ τρεῖς ἡμέρας ἐγερθῆναι.')]),
   'saying, "The son of the human must suffer many things and be rejected by the elders and high priests and scribes, and be killed, and after three days be raised."',
   'present (Marc. 4.21.7; Pan. 42.11.6, sch. 16; [Adam. 198,1–4])',
   [E(16, '»λέγων, δεῖ τὸν υἱὸν τοῦ ἀνθρώπου πολλὰ παθεῖν καὶ ἀποκτανθῆναι καὶ μετὰ τρεῖς ἡμέρας ἐγερθῆναι«.'),
    T('4.21.7', '"quia oporteret filium hominis multa pati, et reprobari a presbyteris et scribis et sacerdotibus, et interfici, et post tertium diem resurgere".')],
   wording='Marcionite reading adopted: μετὰ τρεῖς ἡμέρας for τῇ τρίτῃ ἡμέρᾳ. Epiphanius\' Greek, confirmed by Tertullian\'s "post tertium diem"; NA27 apparatus: μεθ\' ἡμέρας τρεῖς D it; McionA,(E) (Mark 8:31 has μετὰ τρεῖς ἡμέρας). NA27 ἐγερθῆναι is kept (Epiphanius; Adamantius has ἀναστῆναι). The order of the three groups differs in Tertullian; not adopted.',
   western='Agrees in sense with D and the Old Latin.'),
 U('9:23', G('9:23'), 'And he was saying to all, "If anyone wants to come after me, let him disown himself, and take up his cross day by day, and follow me.',
   'Inside the attested passage 9:23–27.'),
 A('9:24', G('9:24'), 'For whoever wants to save his soul will destroy it; but whoever destroys his soul for my sake, he will save it.',
   'present (Marc. 4.21.8–9)', [T('4.21.8', '"Qui voluerit, inquit, animam suam salvam facere, perdet illam, et qui perdiderit eam propter me, salvam faciet eam."')]),
 U('9:25', G('9:25'), 'For what does a person gain, having won the whole world, but having destroyed himself or suffered the loss of himself?', 'Inside the attested passage 9:23–27.'),
 A('9:26', G('9:26'), 'For whoever is ashamed of me and of my words, of him the son of the human will be ashamed, when he comes in his glory and that of the Father and of the holy messengers.',
   'present for 9:26a (Marc. 4.21.10, 12); 9:26b unattested',
   [T('4.21.10', '"Qui confusus, inquit, mei fuerit, et ego confundar eius."')],
   wording='NA27. Tertullian quotes only "Whoever is ashamed of me, I will be ashamed of him": without "and of my words" (λόγους is lacking in D a e l syc, NA27) and without 9:26b ("when he comes in his glory…"). Roth: 9:26b "may not have been present but technically it is unattested". One witness; NA27 printed and the evidence noted.'),
 U('9:27', G('9:27'), 'But I tell you truly, there are some of those standing here who will not taste death until they see the kingdom of God."', 'Inside the attested passage 9:23–27.'),
 A('9:28', G('9:28'), 'And it happened about eight days after these words that, taking along Peter and John and Jacob, he went up into the mountain to pray.',
   'present (Marc. 4.22.1, 7; Pan. 42.11.17, refutation 63; Ephrem)',
   [T('4.22.7', '"Tres de discentibus arbitros futurae visionis et vocis assumit… In montem secedit."')]),
 A('9:29', G('9:29'), 'And it happened, as he was praying, that the look of his face became other, and his clothing white, flashing like lightning.',
   'present (Marc. 4.22.13)', [T('4.22.13', '"splendor eius ut lux erit, utique qua etiam vestitus eius refulsit".')]),
 A('9:30', G('9:30'), 'And look, two men were talking with him, who were Moses and Elijah,',
   'present (Marc. 4.22.1–3, 12; Pan. 42.11.6, sch. 17; Ephrem)',
   [E(17, '»καὶ ἰδοὺ δύο ἄνδρες συνελάλουν αὐτῷ, Ἠλίας καὶ Μωυσῆς ἐν δόξῃ«.'),
    T('4.22.1', '"quod illum cum Moyse et Helia in secessu montis conspici pateris".')],
   wording='NA27. Epiphanius has the names in the order Elijah, Moses and joins "in glory" to them; Tertullian has Moses first (= NA27). Not changed.'),
 A('9:31', greek('9:31', text='οἳ ὀφθέντες ἐν δόξῃ.'),
   'who were seen in glory.',
   'present for 9:31a (Marc. 4.22.12; Pan. 42.11.6, sch. 17); 9:31b absent (Marc. 4.22.16)',
   [E(17, '»…ἐν δόξῃ«.'),
    T('4.22.16', '"Nam et si Marcion noluit eum colloquentem domino ostensum, sed stantem…" — in Marcion\'s text Moses is not shown speaking with the Lord.')],
   wording='9:31a printed (NA27). 9:31b (ἔλεγον τὴν ἔξοδον αὐτοῦ ἣν ἤμελλεν πληροῦν ἐν Ἰερουσαλήμ, "they spoke of his departure, which he was about to fulfil at Jerusalem") is not printed: Roth classes it as attested not present on Tertullian 4.22.16. Epiphanius\' copy had συνελάλουν at 9:30, so the two copies may have differed here.'),
 A('9:32', G('9:32'), 'But Peter and those with him were weighed down with sleep; but becoming fully awake, they saw his glory and the two men standing with him.',
   'present (Marc. 4.22.16; Ephrem)', [T('4.22.16', '"sed stantem" — the two men standing with him (συνεστῶτας).')]),
 A('9:33', G('9:33'), 'And it happened, as they were parting from him, that Peter said to Jesus, "Overseer, it is fine for us to be here; and let us make three tents, one for you and one for Moses and one for Elijah," not knowing what he was saying.',
   'present (Marc. 4.22.4, 16)', [T('4.22.4', '"Bonum est nos hic esse… et faciamus hic tria tabernacula, unum tibi, et Moysi unum, et Heliae unum; sed nesciens quid diceret."')]),
 A('9:34', G('9:34'), 'And as he was saying these things, a cloud came and was overshadowing them; and they were afraid as they went into the cloud.',
   'present (Marc. 4.22.7, 13)', [T('4.22.7', '"sub eodem etiam ambitu nubis".')]),
 A('9:35', G('9:35', [('ὁ ἐκλελεγμένος', 'ὁ ἀγαπητός')]),
   'And a voice came out of the cloud, saying, "This is my son, the beloved; hear him."',
   'present (Marc. 4.22.1, 8, 10, 12; Pan. 42.11.6, sch. 18; Ephrem)',
   [E(18, '»ἐκ τῆς νεφέλης φωνή· οὗτός ἐστιν ὁ υἱός μου ὁ ἀγαπητός«.'),
    T('4.22.1', '"vox illa de caelo: Hic est filius meus dilectus, hunc audite!" (quoted four times in 4.22).')],
   wording='Marcionite reading adopted: ὁ ἀγαπητός for ὁ ἐκλελεγμένος (both witnesses; Roth: secure). NA27 apparatus: ἀγαπητός A C* W f13 33 𝔐 it vgcl.ww sy(c).p.h; McionT,E.',
   western='Agrees with the Old Latin and with A C* W and the Byzantine text.'),
 U('9:36', G('9:36'), 'And when the voice had come, Jesus was found alone. And they were silent and reported to no one in those days anything of what they had seen.',
   'Inside the attested pericope 9:28–36.'),
 U('9:37', G('9:37'), 'And it happened on the next day, when they had come down from the mountain, that a large crowd met him.', 'Inside the attested pericope 9:37–43a.'),
 U('9:38', G('9:38'), 'And look, a man from the crowd shouted, saying, "Teacher, I beg you to look upon my son, because he is my only-born,', 'Inside the attested pericope 9:37–43a.'),
 U('9:39', G('9:39'), 'and look, a spirit takes him, and suddenly he cries out, and it convulses him with foam, and it hardly goes away from him, crushing him.', 'Inside the attested pericope 9:37–43a.'),
 A('9:40', G('9:40'), 'And I begged your learners to throw it out, and they were not able."',
   'present (Pan. 42.11.6, sch. 19)', [E(19, '»ἐδεήθην τῶν μαθητῶν σου«. εἶχε δὲ παρὰ τὸ »οὐκ ἠδυνήθησαν ἐκβαλεῖν αὐτό«…')]),
 A('9:41', G('9:41', [('Ὦ γενεὰ ἄπιστος καὶ διεστραμμένη,', 'Ὦ γενεὰ ἄπιστος,')]),
   'And Jesus answered and said, "O untrusting generation, how long shall I be with you and bear with you? Bring your son here."',
   'present (Marc. 4.23.1–2; Pan. 42.11.6, sch. 19)',
   [E(19, '»καὶ πρὸς αὐτούς· ὦ γενεὰ ἄπιστος, ἕως πότε ἀνέξομαι ὑμῶν;«'),
    T('4.23.1–2', '"O genitura incredula, quousque ero apud vos? quousque sustinebo vos?"; "O natio incredula, quamdiu ero vobiscum, quamdiu vos sustinebo?"')],
   wording='Attested omission: καὶ διεστραμμένη ("and perverse") is absent from both witnesses\' quotations (METHOD §5.3); the shorter address is Mark\'s (Mark 9:19). The witnesses otherwise differ: Tertullian has two "how long" clauses, Epiphanius one, and Epiphanius addresses the words "to them" (the learners). NA27\'s two clauses are kept.'),
 U('9:42', G('9:42'), 'And while he was still coming up, the daimon tore at him and convulsed him violently. But Jesus rebuked the unclean spirit, and cured the boy, and gave him back to his father.', 'Inside the attested pericope 9:37–43a.'),
 U('9:43', G('9:43'), 'And all were astounded at the majesty of God. And while all were marvelling at all the things he was doing, he said to his learners,',
   'Closes the attested pericope 9:37–43a and opens 9:43b–45, whose central saying (9:44) is attested.'),
 A('9:44', G('9:44'), '"You, put these words into your ears: for the son of the human is about to be handed over into the hands of humans."',
   'present (Pan. 42.11.6, sch. 20)', [E(20, '»ὁ γὰρ υἱὸς τοῦ ἀνθρώπου μέλλει παραδίδοσθαι εἰς χεῖρας ἀνθρώπων«.')]),
 U('9:45', G('9:45'), 'But they did not understand this saying, and it was veiled from them so that they should not perceive it; and they were afraid to ask him about this saying.', 'Inside the attested passage 9:43b–45.'),
 A('9:46', G('9:46'), 'And a reasoning came in among them, which of them might be greater.',
   'present (Marc. 4.23.4)', [T('4.23.4', '"tales esse docens debere qui semper maiores velint esse".')]),
 A('9:47', G('9:47'), 'But Jesus, knowing the reasoning of their heart, took hold of a little child and stood it beside himself,',
   'present (Marc. 4.23.4)', [T('4.23.4', '"Sed ecce Christus diligit parvulos".')]),
 A('9:48', G('9:48'), 'and said to them, "Whoever receives this little child in my name receives me; and whoever receives me receives the one who sent me. For the one who is lesser among you all, this one is great."',
   'present (Marc. 4.23.4)', [T('4.23.4', 'see 9:46–47.')],
   wording='NA27 (ὃς ἐὰν δέξηται; SBLGNT ὃς ἂν — checked on the page image).'),
 U('9:51', G('9:51'), 'And it happened, as the days of his taking up were being filled, that he set his face firmly to journey to Jerusalem,', 'Opens the attested pericope 9:51–56.'),
 A('9:52', G('9:52'), 'and he sent messengers before his face. And journeying, they went into a village of Samaritans, to make ready for him;',
   'unattested', [T('4.23.8', '"discipulos super illum viculum Samaritarum" — the village of the Samaritans.')],
   reason='Tertullian names the Samaritan village of 9:52 when he discusses 9:54–55. Roth lists 9:49–53 as unattested; the allusion is sufficient for A+.'),
 U('9:53', G('9:53'), 'and they did not receive him, because his face was journeying to Jerusalem.', 'Inside the attested pericope 9:51–56.'),
 A('9:54', G('9:54'), 'And seeing it, the learners Jacob and John said, "Lord, do you want us to tell fire to come down from the sky and consume them?"',
   'present (Marc. 4.23.8)', [T('4.23.8', '"Repraesentat creator ignium plagam Helia postulante… e contrario Christi lenitatem, increpantis eandem animadversionem destinantes discipulos".')],
   wording='NA27. The addition "as Elijah did" (A C D W Θ Ψ 𝔐 it) is not in NA27\'s text; Tertullian brings Elijah in himself, as Marcion\'s Antitheses did, so his reference does not show that the text had the words.'),
 A('9:55', G('9:55'), 'But turning, he rebuked them.',
   'present (Marc. 4.23.8–9)', [T('4.23.9', '"Nam et tunc ad Heliam, Non in igni, inquit, dominus sed in spiritu miti."')],
   wording='NA27. The longer text ("You do not know of what spirit you are; for the son of the human came not to destroy lives but to save them", K Θ f1.13 700 it and others; D and Epiphanius have only the first part) is not attested for Marcion\'s text. Tertullian\'s "not in fire but in a gentle spirit" quotes 1 Kings 19:12.'),
 U('9:56', G('9:56'), 'And they journeyed to another village.', 'Inside the attested pericope 9:51–56.'),
 A('9:57', G('9:57'), 'And as they were journeying on the road, someone said to him, "I will follow you wherever you go away to."',
   'present (Marc. 4.23.9)', [T('4.23.9', '"Sequar te quocunque ieris".')]),
 A('9:58', G('9:58'), 'And Jesus said to him, "The foxes have dens, and the birds of the sky have places to settle, but the son of the human has nowhere to lay his head."',
   'present (Marc. 4.23.9)', [T('4.23.9', '"cur recusat eum qui se tam individuum illi comitem offert?"')]),
 A('9:59', G('9:59'), 'And he said to another, "Follow me." But he said, "Lord, allow me first to go away and bury my father."',
   'present (Marc. 4.23.10)', [T('4.23.10', '"Illi autem causato patris sepulturam…"')],
   wording='NA27, with its bracketed [κύριε] (Tertullian paraphrases the request and does not quote the address).'),
 A('9:60', G('9:60'), 'But he said to him, "Let the dead bury their own dead; but you, go away and announce the kingdom of God far and wide."',
   'present (Marc. 4.23.10; Clement, Strom. 3.4.25)', [T('4.23.10', '"Sine mortui sepeliant mortuos suos, tu autem vade et annuntia regnum dei".')]),
 A('9:61', G('9:61'), 'And another also said, "I will follow you, lord; but first allow me to take leave of those in my house."',
   'present (Marc. 4.23.11)', [T('4.23.11', '"et tertium illum prius suis valedicere parantem".')]),
 A('9:62', G('9:62'), 'But Jesus said to him, "No one who has put his hand to a plough and is looking at the things behind is well placed for the kingdom of God."',
   'present (Marc. 4.23.11)', [T('4.23.11', '"prohibet retro respectare".')],
   wording='NA27 with its bracketed [πρὸς αὐτόν] (SBLGNT omits it — checked on the page image).'),
]

OMITTED = [
 dict(ref='9:49–50', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='A separate NA27 paragraph (the strange exorcist) with no attested verse (METHOD §4.3). Tertullian passes from 9:48 (4.23.4) to 9:54 (4.23.8).')),
]

PREAMBLE = (
 "Who do the crowds say that I am? The chapter turns on that question, and on Peter's answer: the Anointed One "
 "of God. He is told to tell no one. At once, and for the first time plainly, the cost is named: the son of the "
 "human must suffer, be rejected, be killed, and be raised. To follow him is to take up the same road. Eight "
 "days later three learners go up a mountain with him and see his face become other and his clothing flash like "
 "lightning, with Moses and Elijah beside him in glory. A cloud covers them, and a voice says: hear him. Below, "
 "a father's only son is being torn apart, and the learners cannot help. Then an argument about who is greater, "
 "answered by a little child set beside him. From here the book changes direction. The days of his taking up are"
 " being filled, and he sets his face toward Jerusalem."
)

NOTES = [
 dict(term='Peter\'s confession (9:18–22)', cat='textual', refs=['9:18', '9:19', '9:20', '9:21', '9:22'], text=(
  "Tertullian, Marc. 4.21.6–7: Peter answers \"Tu es Christus\", Jesus imposes silence, and gives as the reason that \"the son "
  "of man must suffer many things, be rejected by the elders and scribes and priests, be killed, and rise after the third "
  "day\". Epiphanius, sch. 16 quotes the prediction in Greek with μετὰ τρεῖς ἡμέρας (\"after three days\") for canonical Luke's "
  "\"on the third day\"; that form is printed (D and the Old Latin have it, as does Mark 8:31). 9:18–19 are read in the Dialogue "
  "of Adamantius (84,1–4); Roth counts them as attested. NA27 reads λέγουσιν οἱ ὄχλοι at 9:18 (SBLGNT has a different order).")),
 dict(term='Cross and shame (9:23–27)', cat='textual', refs=['9:23', '9:24', '9:25', '9:26', '9:27'], text=(
  "Tertullian, Marc. 4.21.8–12 quotes 9:24 (\"whoever wants to save his soul will destroy it…\") and 9:26 (\"whoever is ashamed of "
  "me, I will be ashamed of him\"), and argues at length that only a Christ with a real birth and flesh could be a cause of "
  "shame. His quotation of 9:26 lacks \"and my words\" (also lacking in D and some Old Latin and Old Syriac witnesses) and the "
  "coming \"in his glory\" (9:26b). One witness; NA27 printed and the evidence noted. 9:23, 9:25 and 9:27 are not cited and are "
  "printed in grey.")),
 dict(term='The transfiguration (9:28–36)', cat='textual', refs=['9:28', '9:29', '9:30', '9:31', '9:32', '9:33', '9:34', '9:35'], text=(
  "Tertullian, Marc. 4.22.1–16; Epiphanius, sch. 17–18. Both witnesses give the voice as \"This is my son, the beloved\" "
  "(ἀγαπητός; \"filius meus dilectus\"), and NA27 cites Marcion for it with A C* W, the Byzantine text and the Old Latin; it is "
  "printed for canonical Luke's \"my chosen\". Tertullian says that Marcion did not want Moses shown \"speaking with the Lord, "
  "but standing\" (4.22.16). Roth takes this to mean 9:31b (\"they spoke of his departure, which he was to fulfil at "
  "Jerusalem\") was not in the text, and it is not printed. Epiphanius' copy did have them \"talking with him\" (9:30), so the "
  "copies may have differed on the conversation. 9:36 is not cited and is printed in grey.")),
 dict(term='Moses, Elijah and the son', cat='theological', refs=['9:30', '9:35'], text=(
  "Reception and interpretation. For Tertullian the scene proves that Jesus belongs with the law and the prophets: \"he would "
  "not show them in conversation, a sign of familiarity, nor in a share of his glory\" if he had come to destroy them "
  "(4.22.2). The Marcionite reading took the voice (\"hear him\") as transferring authority away from Moses and Elijah "
  "(4.22.1). The attested text shows Jesus with Moses and Elijah in glory and the voice naming him son. It does not itself say "
  "whether their authority is confirmed or ended.")),
 dict(term='"O untrusting generation" (9:37–43a)', cat='textual', refs=['9:40', '9:41'], text=(
  "Epiphanius, sch. 19 quotes the father's words and the reply \"to them\": »ὦ γενεὰ ἄπιστος, ἕως πότε ἀνέξομαι ὑμῶν;«. "
  "Tertullian quotes the reply twice (4.23.1–2), \"O genitura incredula, quousque ero apud vos? quousque sustinebo vos?\". "
  "Neither has \"and perverse\" (καὶ διεστραμμένη), which canonical Luke shares with Matthew 17:17; the shorter address is "
  "Mark's (9:19). The words are absent from two witnesses' quotations and are not printed (METHOD §5.3). The witnesses differ "
  "on the rest: Tertullian has two \"how long\" clauses, as in Matthew and Mark, and Epiphanius one. Their copies were "
  "harmonized differently, a point made by Williams and BeDuhn (working document §2.2). 9:37–39 and 9:42–43a are not cited and "
  "are printed in grey.")),
 dict(term='Greatness and the child (9:43b–48)', cat='textual', refs=['9:44', '9:46', '9:47', '9:48'], text=(
  "Epiphanius, sch. 20 quotes the second passion prediction (9:44). Tertullian, Marc. 4.23.4 sets Jesus' love of children "
  "against the Antitheses' example of Elisha and the bears (2 Kgs 2:23–24). NA27 reads ὃς ἐὰν δέξηται at 9:48 (SBLGNT ὃς ἄν). "
  "9:43b and 9:45 are not cited and are printed in grey. 9:49–50 (the strange exorcist) form a separate paragraph that no "
  "witness cites, and are not printed.")),
 dict(term='The Samaritan village (9:51–56)', cat='textual', refs=['9:52', '9:54', '9:55'], text=(
  "Tertullian, Marc. 4.23.8–9: against the Creator's fire called down by Elijah (2 Kgs 1:10–12) stands Christ's leniency, "
  "\"rebuking the learners who wanted the same punishment for that village of the Samaritans\". This attests 9:52, which Roth "
  "lists as unattested, and 9:54–55. Two longer readings of canonical manuscripts, \"as Elijah did\" (9:54) and \"you do not "
  "know of what spirit you are…\" (9:55–56), are not attested for this text. Tertullian brings in Elijah himself, as the "
  "Antitheses did. 9:51, 9:53 and 9:56 are not cited and are printed in grey.")),
 dict(term='Would-be followers (9:57–62)', cat='textual', refs=['9:57', '9:58', '9:59', '9:60', '9:61', '9:62'], text=(
  "Tertullian, Marc. 4.23.9–11 attests all three exchanges, quoting \"Let the dead bury their dead, but you go and proclaim "
  "the kingdom of God\". He argues that the reply keeps the law forbidding priests and Nazirites contact with the dead (Lev "
  "21:1; Num 6:6–7). NA27 prints [κύριε] at 9:59 and [πρὸς αὐτόν] at 9:62 in brackets; both are printed.")),
 dict(term='Suffering, rising and the law', cat='theological', refs=['9:22', '9:60'], text=(
  "Interpretation. The attested text predicts suffering, death and being raised \"after three days\", and Tertullian takes "
  "the prediction as the Creator's prophecy fulfilled (4.21.7). In 9:60 he reads the call to leave the dead to bury their dead "
  "as the Nazirite and priestly rule applied to those devoted to the kingdom (4.23.10). Hegesippus' report that James lived as "
  "a Nazirite, which the library uses (Carriers of Living Water §3.2), concerns the same pattern of consecration; whether the "
  "saying was read that way in the community behind the text cannot be shown from the witnesses.")),
 dict(term='κατὰ μόνας, "alone"', cat='translation', refs=['9:18'], text='In private. The learners are with him all the same, as the sentence says.'),
 dict(term='ἀνέστη, "has stood up"', cat='translation', refs=['9:19'], text='ἀνίστημι, as at 9:8.'),
 dict(term='Τὸν χριστὸν τοῦ θεοῦ, "the Anointed One of God"', cat='translation', refs=['9:20'], text='As at 4:41.'),
 dict(term='Δεῖ, "must"', cat='translation', refs=['9:22'], text='Necessity, as at 4:43.'),
 dict(term='ἀποδοκιμασθῆναι, "be rejected"', cat='translation', refs=['9:22'], text='To be tested and found wanting, thrown out after examination.'),
 dict(term='ἀρχιερέων, "high priests"', cat='translation', refs=['9:22'], text='The plural: the high priest and the leading priestly families.'),
 dict(term='μετὰ τρεῖς ἡμέρας ἐγερθῆναι, "after three days be raised"', cat='translation', refs=['9:22'], text='The reading of this text, "after three days". Canonical Luke has "on the third day". ἐγείρω, passive.'),
 dict(term='ἀρνησάσθω ἑαυτόν, "let him disown himself"', cat='translation', refs=['9:23'], text='ἀρνέομαι, to say no to, disown, deny. It is the verb of 8:45, "all were denying it".'),
 dict(term='σταυρόν, "cross"', cat='translation', refs=['9:23'], text='The Roman stake or cross on which the condemned were executed.'),
 dict(term='ψυχήν, "soul"', cat='translation', refs=['9:24'], text='The living self, the life a person has. "Life" is the sense in many translations; "soul" keeps the word.'),
 dict(term='ἀπολέσει, "will destroy"', cat='translation', refs=['9:24'], text='ἀπόλλυμι, to destroy or to lose. "Lose" is often used here. "Destroy" keeps the verb of 4:34, 5:37 and 6:9.'),
 dict(term='ζημιωθείς, "suffered the loss of"', cat='translation', refs=['9:25'], text='To be fined, to forfeit.'),
 dict(term='ἐπαισχυνθῇ, "is ashamed of"', cat='translation', refs=['9:26'], text='To be ashamed of, to disown out of shame.'),
 dict(term='τῶν ἁγίων ἀγγέλων, "the holy messengers"', cat='translation', refs=['9:26'], text='ἄγγελος, messenger, as at 7:24 and 7:27. "Angels" is the Greek word left untranslated, and it brings the later doctrine of a class of beings.'),
 dict(term='ἀληθῶς, "truly"', cat='translation', refs=['9:27'], text='A Greek word here, not ἀμήν.'),
 dict(term='γεύσωνται θανάτου, "taste death"', cat='translation', refs=['9:27'], text='A Semitic way of saying "die".'),
 dict(term='τὸ εἶδος… ἕτερον, "the look… became other"', cat='translation', refs=['9:29'], text='εἶδος is form, appearance; ἕτερος is other, different. The Greek has no verb: "the look of his face, other".'),
 dict(term='ἐξαστράπτων, "flashing like lightning"', cat='translation', refs=['9:29'], text='From ἀστραπή, "lightning".'),
 dict(term='ὀφθέντες, "were seen"', cat='translation', refs=['9:31'], text='The aorist passive of ὁράω, "to see": "having been seen", "appearing".'),
 dict(term='βεβαρημένοι ὕπνῳ, "weighed down with sleep"', cat='translation', refs=['9:32'], text='Heavy with sleep.'),
 dict(term='διαγρηγορήσαντες, "becoming fully awake"', cat='translation', refs=['9:32'], text='To stay awake through, to wake fully.'),
 dict(term='καλόν, "fine"', cat='translation', refs=['9:33'], text='καλός, as at 6:43.'),
 dict(term='σκηνάς, "tents"', cat='translation', refs=['9:33'], text='Booths, as at the feast of Booths.'),
 dict(term='ἐπεσκίαζεν, "was overshadowing"', cat='translation', refs=['9:34'], text='To cast a shadow over.'),
 dict(term='ὁ υἱός μου ὁ ἀγαπητός, "my son, the beloved"', cat='translation', refs=['9:35'], text='The reading of this text. Canonical Luke has "my son, the chosen one". Lower case "son": the voice names a relation, not a title.'),
 dict(term='αὐτοῦ ἀκούετε, "hear him"', cat='translation', refs=['9:35'], text='ἀκούω, to hear, listen, obey.'),
 dict(term='ἐβόησεν, "shouted"', cat='translation', refs=['9:38'], text='To cry aloud.'),
 dict(term='σπαράσσει, "convulses"', cat='translation', refs=['9:39'], text='To tear, rend, throw into convulsions.'),
 dict(term='συντρῖβον, "crushing"', cat='translation', refs=['9:39'], text='To break in pieces, shatter.'),
 dict(term='ἐκβάλωσιν, "throw out"', cat='translation', refs=['9:40'], text='ἐκβάλλω, as at 6:42.'),
 dict(term='γενεὰ ἄπιστος, "untrusting generation"', cat='translation', refs=['9:41'], text='ἄπιστος, without trust (πίστις). This text lacks "and perverse".'),
 dict(term='ἀνέξομαι, "bear with"', cat='translation', refs=['9:41'], text='To hold up under, endure.'),
 dict(term='ἔρρηξεν, "tore at"', cat='translation', refs=['9:42'], text='ῥήγνυμι, to break, tear, throw down.'),
 dict(term='ἰάσατο, "cured"', cat='translation', refs=['9:42'], text='ἰάομαι.'),
 dict(term='μεγαλειότητι, "majesty"', cat='translation', refs=['9:43'], text='Greatness, magnificence.'),
 dict(term='Θέσθε… εἰς τὰ ὦτα, "put… into your ears"', cat='translation', refs=['9:44'], text='Literally "place these words into your ears".'),
 dict(term='παραδίδοσθαι, "be handed over"', cat='translation', refs=['9:44'], text='παραδίδωμι, to hand over, deliver. "Betray" is one use of it, but the word itself says "hand over".'),
 dict(term='παρακεκαλυμμένον, "veiled"', cat='translation', refs=['9:45'], text='Covered over, hidden by a veil.'),
 dict(term='διαλογισμός, "a reasoning"', cat='translation', refs=['9:46'], text='As at 5:22.'),
 dict(term='μείζων… μικρότερος… μέγας, "greater… lesser… great"', cat='translation', refs=['9:46', '9:48'], text='The Greek has comparatives and a positive, not superlatives. "The greatest" and "the least" are usual in English but say more than the Greek.'),
 dict(term='παιδίον, "a little child"', cat='translation', refs=['9:47'], text='The diminutive of παῖς.'),
 dict(term='δέξηται, "receives"', cat='translation', refs=['9:48'], text='δέχομαι, to receive, welcome.'),
 dict(term='ἐν τῷ συμπληροῦσθαι τὰς ἡμέρας, "as the days were being filled"', cat='translation', refs=['9:51'], text='The days are filled up, completed.'),
 dict(term='τῆς ἀναλήμψεως αὐτοῦ, "of his taking up"', cat='translation', refs=['9:51'], text='ἀνάλημψις, a being taken up. It can mean his being taken up into heaven, or his being taken away from this life.'),
 dict(term='τὸ πρόσωπον ἐστήρισεν, "set his face firmly"', cat='translation', refs=['9:51'], text='στηρίζω, to fix, make firm. A Hebrew idiom for resolve.'),
 dict(term='ἀγγέλους, "messengers"', cat='translation', refs=['9:52'], text='ἄγγελος, here human messengers.'),
 dict(term='τὸ πρόσωπον αὐτοῦ ἦν πορευόμενον, "his face was journeying"', cat='translation', refs=['9:53'], text='Word for word. It means that he was on his way to Jerusalem.'),
 dict(term='ἀναλῶσαι, "consume"', cat='translation', refs=['9:54'], text='To use up, destroy.'),
 dict(term='κατασκηνώσεις, "places to settle"', cat='translation', refs=['9:58'], text='Literally "tentings", places to settle or roost.'),
 dict(term='κλίνῃ, "lay"', cat='translation', refs=['9:58'], text='κλίνω, to bend, lay down, incline. It is the same verb as "the day began to decline" (9:12).'),
 dict(term='Ἄφες, "let"', cat='translation', refs=['9:60'], text='ἀφίημι, as at 6:42.'),
 dict(term='διάγγελλε, "announce far and wide"', cat='translation', refs=['9:60'], text='To announce throughout, spread the news.'),
 dict(term='ἀποτάξασθαι, "take leave of"', cat='translation', refs=['9:61'], text='To say goodbye, set oneself apart from.'),
 dict(term='εὔθετος, "well placed"', cat='translation', refs=['9:62'], text='Fit, suitable, rightly set.'),
]
