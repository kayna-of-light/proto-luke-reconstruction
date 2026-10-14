"""Batch 2, chapter 4 of the reconstruction: Luke 7."""
from buildlib import greek
from batch1_ch2 import U, A
from batch2_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}

ENTRIES = [
 U('7:1', G('7:1'), 'When he had completed all his sayings in the ears of the people, he went into Capernaum.',
   'Opens the attested pericope 7:1–10.'),
 A('7:2', G('7:2'), "And a certain centurion's slave, who was in a bad way, was about to come to his end; and he was valued by him.",
   'present (Marc. 4.18.1)', [T('4.18.1', '"Proinde extollenda fide centurionis…" — the centurion.')],
   wording='NA27. Only the centurion is attested; the details of the verse are not.'),
 U('7:3', G('7:3'), 'Hearing about Jesus, he sent to him elders of the Judeans, asking him to come and bring his slave safely through.'),
 U('7:4', G('7:4'), 'And when they came to Jesus, they were urging him earnestly, saying, "He is worthy that you should grant him this,'),
 U('7:5', G('7:5'), 'for he loves our nation, and he himself built the assembly for us."'),
 U('7:6', G('7:6'), 'And Jesus was going with them. And when he was already not far from the house, the centurion sent friends, saying to him, "Lord, do not trouble yourself, for I am not fit for you to come in under my roof;'),
 U('7:7', G('7:7'), 'that is why I did not count myself worthy to come to you either. But say it with a word, and let my boy be cured.'),
 U('7:8', G('7:8'), 'For I too am a person set under authority, having soldiers under myself; and I say to this one, \'Go!\' and he goes, and to another, \'Come!\' and he comes, and to my slave, \'Do this!\' and he does it."'),
 A('7:9', G('7:9', [('Λέγω ὑμῖν, οὐδὲ ἐν τῷ Ἰσραὴλ τοσαύτην πίστιν εὗρον.', 'Λέγω ὑμῖν, τοσαύτην πίστιν οὐδὲ ἐν τῷ Ἰσραὴλ εὗρον.')]), 'Hearing these things, Jesus marvelled at him, and turning to the crowd that was following him he said, "I tell you, not even in Israel have I found such trust."',
   'present (Marc. 4.18.1; Pan. 42.11.6, sch. 7)',
   [E(7, '»λέγω δὲ ὑμῖν, τοσαύτην πίστιν οὐδὲ ἐν τῷ Ἰσραὴλ εὗρον«.'),
    T('4.18.1', '"si is professus est talem se fidem nec in Israele invenisse".')],
   wording='NA27 words in the order of Epiphanius\' quotation (τοσαύτην πίστιν before οὐδὲ ἐν τῷ Ἰσραήλ; Roth: secure). Epiphanius\' δέ after λέγω is rated "likely not present" by Roth and is not printed.'),
 U('7:10', G('7:10'), 'And returning to the house, those who had been sent found the slave in health.'),
 U('7:11', G('7:11'), 'And it happened on the next day that he journeyed to a city called Nain, and his learners and a large crowd were journeying with him.',
   'Opens the attested pericope 7:11–17.'),
 A('7:12', G('7:12'), 'And as he drew near to the gate of the city, look, a dead man was being carried out, the only-born son of his mother, and she was a widow; and a sizeable crowd of the city was with her.',
   'present (Marc. 4.18.2)', [T('4.18.2', '"Resuscitavit et mortuum filium viduae."')]),
 U('7:13', G('7:13'), 'And seeing her, the lord was moved with compassion over her and said to her, "Do not weep."'),
 A('7:14', G('7:14'), 'And coming up, he touched the bier, and those carrying it stood still, and he said, "Young man, I say to you, get up!"',
   'present (Marc. 4.18.2)', [T('4.18.2', '"Resuscitavit et mortuum filium viduae."')]),
 A('7:15', G('7:15'), 'And the dead man sat up and began to speak, and he gave him to his mother.',
   'present (Marc. 4.18.2)', [T('4.18.2', '"Resuscitavit et mortuum filium viduae."')]),
 A('7:16', G('7:16'), 'And fear took hold of all, and they were giving glory to God, saying, "A great prophet has been raised among us," and, "God has visited his people."',
   'present (Marc. 4.18.2–3)',
   [T('4.18.3', '"omnes illic creatori gloriam retulerint dicentes, Magnus prophetes prodiit in nobis, et Respexit deus populum suum."')],
   wording='NA27. Tertullian\'s "prodiit" is read by Roth as ἐγήγερται (possible only); not adopted.'),
 U('7:17', G('7:17'), 'And this word about him went out in all Judea and all the surrounding region.'),
 A('7:18', G('7:18'), 'And his learners reported to John about all these things. And calling two of his learners to him, John',
   'present (Marc. 4.18.4)', [T('4.18.4', '"Sed scandalizatur Ioannes auditis virtutibus Christi".')]),
 A('7:19', G('7:19'), 'sent them to the lord, saying, "Are you the one who is coming, or are we to wait for another?"',
   'present (Marc. 4.18.5–7; Adam. 50,12–14)', [T('4.18.6', '"Tu es, inquit, qui venis, an alium expectamus?"')]),
 A('7:20', G('7:20'), 'And when the men had come to him, they said, "John the baptiser sent us to you, saying, \'Are you the one who is coming, or are we to wait for another?\'"',
   'present (Marc. 4.18.6)', [T('4.18.6', 'The question repeated and explained.')]),
 U('7:21', G('7:21'), 'In that hour he healed many of diseases and scourges and evil spirits, and to many blind people he granted sight.',
   'Inside the attested pericope 7:18–23.'),
 A('7:22', G('7:22'), 'And answering, he said to them, "Go and report to John what you have seen and heard: blind people see again, lame people walk about, the leprous are being cleansed and deaf people hear, dead people are being raised, the destitute are being given the good news.',
   'present (Marc. 4.18.6; Eznik, De Deo 358)', [T('4.18.6', '"ut dominus per easdem operationes agnoscendum se nuntiaverit Ioanni".')]),
 A('7:23', G('7:23'), 'And fortunate is whoever is not tripped up by me."',
   'present (Marc. 4.18.8; Pan. 42.11.6, sch. 8; Ephrem)',
   [E(8, 'παρηλλαγμένον τὸ »μακάριος ὃς οὐ μὴ σκανδαλισθῇ ἐν ἐμοί«· εἶχε γὰρ ὡς πρὸς Ἰωάννην.'),
    T('4.18.8', '"qui non fuerit scandalizatus in Christum, quod tunc Ioannem minuit".')],
   wording='NA27. Epiphanius says the saying was "altered" in that it was taken as aimed at John (Holl: an application, not a different wording). Recorded as the Marcionite reading of the verse (reception).'),
 A('7:24', G('7:24'), 'When John\'s messengers had gone away, he began to say to the crowds about John, "What did you go out into the desert to gaze at? A reed shaken by wind?',
   'present (Marc. 4.18.7–8)', [T('4.18.8', '"Quid existis videre in solitudinem?"')]),
 U('7:25', G('7:25'), 'But what did you go out to see? A person dressed in soft garments? Look, those in splendid clothing and luxury are in royal houses.',
   'Inside the attested passage 7:24–28.'),
 A('7:26', G('7:26'), 'But what did you go out to see? A prophet? Yes, I tell you, and more than a prophet.',
   'present (Marc. 4.18.7)', [T('4.18.7', '"propheten eum confirmans, immo et supra".')]),
 A('7:27', G('7:27'), "This is the one about whom it is written, 'Look, I send my messenger before your face, who will make ready your way before you.'",
   'present (Marc. 4.18.4, 7, 8; Pan. 42.11.6, sch. 9; Adam. 98,11–13)',
   [E(9, '»αὐτός ἐστι περὶ οὗ γέγραπται· ἰδού, ἀποστέλλω τὸν ἄγγελόν μου πρὸ προσώπου σου«.'),
    T('4.18.7', '"Ecce ego mitto angelum meum ante faciem tuam, qui praeparabit viam tuam".')],
   wording='NA27. Epiphanius\' αὐτός for οὗτος is rated possible by Roth; ἔμπροσθέν σου is not in Tertullian\'s quotation (Roth: attested in Adamantius).'),
 A('7:28', G('7:28'), 'I tell you, among those born of women no one is greater than John; but the lesser one in the kingdom of God is greater than he."',
   'present (Marc. 4.18.8)', [T('4.18.8', '"maior quidem omnibus natis mulierum… qui minor fuerit in regno dei".')]),
 A('7:36', G('7:36'), 'And one of the Pharisees was asking him to eat with him; and going into the house of the Pharisee, he reclined at table.',
   'present (Pan. 42.11.6, sch. 10)', [E(10, '»καὶ εἰσελθὼν εἰς τὸν οἶκον τοῦ Φαρισαίου κατεκλίθη«.')]),
 A('7:37', G('7:37'), 'And look, a woman who was a sinner in the city, learning that he was reclining at table in the house of the Pharisee, brought an alabaster flask of perfumed oil,',
   'present (Marc. 4.18.9; Pan. 42.11.6, sch. 10)',
   [E(10, '»ἡ δὲ γυνὴ… ἡ ἁμαρτωλός«.'), T('4.18.9', '"Illius autem peccatricis feminae argumentum…"')]),
 A('7:38', G('7:38'), 'and standing behind at his feet, weeping, she began to wet his feet with her tears, and she was wiping them with the hairs of her head, and kissing his feet again and again, and anointing them with the perfumed oil.',
   'present (Marc. 4.18.9; Pan. 42.11.6, sch. 10)',
   [E(10, '»ἡ δὲ γυνὴ στᾶσα ὀπίσω ἡ ἁμαρτωλὸς παρὰ τοὺς πόδας ἔβρεξε τοῖς δάκρυσι τοὺς πόδας καὶ ἤλειψεν καὶ κατεφίλει«.'),
    T('4.18.9', '"cum pedes domini osculis figeret, lacrimis inundaret, crinibus detergeret, unguento perduceret".')],
   wording='NA27. The order of the actions differs between the two witnesses and from NA27; Roth leaves it open.'),
 U('7:39', G('7:39'), 'But seeing it, the Pharisee who had invited him said within himself, "This man, if he were a prophet, would know who and what sort of woman it is who is touching him, that she is a sinner."',
   'Inside the attested pericope 7:36–50.'),
 U('7:40', G('7:40'), 'And answering, Jesus said to him, "Simon, I have something to say to you." And he says, "Teacher, say it."', 'Inside the attested pericope 7:36–50.'),
 U('7:41', G('7:41'), '"There were two debtors to a certain moneylender. The one owed five hundred denarii, and the other fifty.', 'Inside the attested pericope 7:36–50.'),
 U('7:42', G('7:42'), 'When they had nothing to pay back, he freely granted it to both. Which of them, then, will love him more?"', 'Inside the attested pericope 7:36–50.'),
 U('7:43', G('7:43'), 'Simon answered and said, "I suppose the one to whom he freely granted the more." And he said to him, "You have judged rightly."', 'Inside the attested pericope 7:36–50.'),
 A('7:44', G('7:44'), 'And turning to the woman, he said to Simon, "Do you see this woman? I came into your house; you gave me no water for my feet, but she has wet my feet with her tears and wiped them with her hairs.',
   'present (Pan. 42.11.6, sch. 11)', [E(11, 'καὶ πάλιν »αὕτη τοῖς δάκρυσιν ἔβρεξέν τοὺς πόδας μου καὶ ἤλειψεν καὶ κατεφίλει«.')]),
 A('7:45', G('7:45'), 'You gave me no kiss; but she, from the time I came in, has not stopped kissing my feet.',
   'present (Pan. 42.11.6, sch. 11)', [E(11, '…καὶ κατεφίλει.')]),
 A('7:46', G('7:46'), 'You did not anoint my head with olive oil; but she has anointed my feet with perfumed oil.',
   'present (Pan. 42.11.6, sch. 11)', [E(11, '…καὶ ἤλειψεν…')]),
 A('7:47', G('7:47'), 'For this reason, I tell you, her sins, which are many, have been let go, because she loved much; but the one to whom little is let go loves little."',
   'present (Marc. 4.18.9)', [T('4.18.9', '"ut peccatricis paenitentia secundum creatorem meruerit veniam".')]),
 A('7:48', G('7:48'), 'And he said to her, "Your sins have been let go."',
   'present (Marc. 4.18.9)', [T('4.18.9', '"meruerit veniam".')]),
 U('7:49', G('7:49'), 'And those reclining at table with him began to say within themselves, "Who is this, who even lets sins go?"', 'Inside the attested pericope 7:36–50.'),
 A('7:50', G('7:50'), 'And he said to the woman, "Your trust has saved you; journey into peace."',
   'present (Marc. 4.18.9)', [T('4.18.9', '"ab eo audiit, Fides tua te salvam fecit".')]),
]

OMITTED = [
 dict(ref='7:29–35', cls='U−', app=dict(roth='unattested', witnesses=[
      T('4.18.4–8', 'Argues throughout that John belongs to the Creator and that Christ confirms him.')],
      decision='not printed',
      reason='Tertullian works through 7:18–28 continuously (4.18.4–8) and passes to 7:36–50 (4.18.9). His whole argument there is that John is the Creator\'s prophet and that Christ endorses him. 7:29–30 (the people "justified God, having been baptized with John\'s baptism"; the Pharisees "rejected the counsel of God") and 7:33–35 (John and the son of the human as wisdom\'s children) would have made that case directly; he does not cite them. The previous text also omitted 7:24–35 apart from 7:27–28.')),
]

PREAMBLE = (
 "Four scenes from the Galilean ministry. A centurion's trust is measured against Israel: \"not even in Israel have I found such "
 "trust.\" A widow's only son is raised at Nain, and the crowd acclaims Jesus in the language of Israel's scripture: \"A great "
 "prophet has been raised among us\" and \"God has visited his people.\" John the baptiser sends to ask whether Jesus is the one to "
 "come, and Jesus answers with the works of the prophets and calls John more than a prophet. In a Pharisee's house a woman of "
 "the town anoints his feet, and her sins are let go \"because she loved much.\" Tertullian works through the chapter in "
 "order (Marc. 4.18) and Epiphanius quotes from four of the scenes. Not printed: the passage on John's baptism and \"this "
 "generation\" (7:29–35), which no witness cites although Tertullian's argument needed it."
)

NOTES = [
 dict(term='The centurion (7:1–10)', cat='textual', refs=['7:2', '7:9'], text=(
  "Tertullian, Marc. 4.18.1, discusses only the centurion and the saying about trust in Israel; Epiphanius, sch. 7 quotes the "
  "saying: »λέγω δὲ ὑμῖν, τοσαύτην πίστιν οὐδὲ ἐν τῷ Ἰσραὴλ εὗρον«. Its word order (\"such trust\" first) is printed with "
  "NA27's words; Roth rates the words secure. The embassy of the Jewish elders, the friends and the centurion's speech (7:3–8) "
  "and the return of the messengers (7:10) are not cited and are printed in grey.")),
 dict(term='"A great prophet has been raised among us" (7:16)', cat='theological', refs=['7:16'], text=(
  "Tertullian, Marc. 4.18.3 quotes the acclamation, \"Magnus prophetes prodiit in nobis, et Respexit deus populum suum\", and "
  "argues that the crowd glorified the Creator and Jesus did not correct them. Interpretation: in the attested text the people of "
  "Israel name Jesus a prophet and see in the raising a visitation of their God. This is the attested place for the prophet "
  "Christology the library builds on; the phrase \"a prophet mighty in deed and word\" (24:19), used as a title in the library, is "
  "itself unattested for this text (working document §5).")),
 dict(term='John\'s question (7:18–23)', cat='textual', refs=['7:18', '7:19', '7:20', '7:22', '7:23'], text=(
  "Tertullian, Marc. 4.18.4–8 attests John hearing of Jesus' works, the question \"Are you the one who is coming, or are we to "
  "wait for another?\" (quoted twice) and the answer by works. Epiphanius, sch. 8 says the beatitude of 7:23 was \"altered\" "
  "because Marcion's text had it \"as if addressed to John\"; Holl explains this as Marcion's application of the saying, not a "
  "different wording. That is how the Marcionite community read the verse (reception). 7:21 is not cited and is printed in "
  "grey.")),
 dict(term='John and the kingdom (7:24–28)', cat='textual', refs=['7:24', '7:26', '7:27', '7:28'], text=(
  "Tertullian, Marc. 4.18.7–8 and Epiphanius, sch. 9 attest the testimony to John: the question \"What did you go out into the "
  "wilderness to see?\", \"a prophet, and more\", the quotation of Malachi 3:1, and \"the lesser one in the kingdom of God is greater "
  "than he\". 7:25 is not cited and is printed in grey. Tertullian reports the Marcionite reading that the kingdom of 7:28 "
  "belongs to a different god from John's; he answers that both belong to the same God (reception).")),
 dict(term='Not printed: 7:29–35', cat='excision', refs=['7:28', '7:36'], text=(
  "7:29–30 (the people and the tax collectors \"justified God\" by John's baptism; the Pharisees rejected \"the counsel of God\") "
  "and 7:31–35 (\"this generation\" and the children in the market-place; \"wisdom is justified by all her children\") are not "
  "cited. Tertullian works through 7:18–28 and then 7:36–50 without a gap in his argument, and these verses would have been his "
  "best evidence that John's baptism was God's own plan. They are classed \"unattested, probably absent\" (METHOD §3).")),
 dict(term='The woman who loved much (7:36–50)', cat='textual', refs=['7:36', '7:37', '7:38', '7:44', '7:45', '7:46', '7:47', '7:48', '7:50'], text=(
  "Epiphanius, sch. 10–11 quotes 7:36, 7:38 and 7:44–46; Tertullian, Marc. 4.18.9 attests the woman, her tears, kisses and "
  "ointment, the letting go of her sins and \"Your trust has saved you\". The Pharisee's thought and the parable of the two debtors "
  "(7:39–43) and the guests' question (7:49) are not cited and are printed in grey. Tertullian uses the woman's touch as proof "
  "that Jesus had a real body (4.18.9), his own argument against Marcion's Christology.")),
 dict(term='Trust shown in deeds', cat='theological', refs=['7:47', '7:50'], text=(
  "Interpretation. In the attested scene the woman's trust (7:50) is visible in what she does: the tears, the kisses, the "
  "ointment. The letting go of her sins is tied to her love (\"because she loved much\", 7:47). The pairing of trust with acts matches the "
  "Epistle of James (\"faith was active along with his works\", Jas 2:22, where \"faith\" is the same Greek word, πίστις), which the library takes as the closest written "
  "witness to the community behind this text (Carriers of Living Water §3.4).")),
 dict(term='ἐπλήρωσεν… εἰς τὰς ἀκοάς, "completed… in the ears"', cat='translation', refs=['7:1'], text='Literally "filled up… into the hearing". ῥήματα are "sayings", things spoken.'),
 dict(term='ἑκατοντάρχου, "centurion"', cat='translation', refs=['7:2'], text='A Roman officer commanding about a hundred soldiers.'),
 dict(term='δοῦλος, "slave"', cat='translation', refs=['7:2'], text='A person owned by another. "Servant" softens what the word says. The centurion calls the same person παῖς, "boy" (7:7).'),
 dict(term='ἤμελλεν τελευτᾶν, "was about to come to his end"', cat='translation', refs=['7:2'], text='To reach the end, to die.'),
 dict(term='ἔντιμος, "valued"', cat='translation', refs=['7:2'], text='Held in honour, precious. It can mean dear to him or of high value.'),
 dict(term='πρεσβυτέρους, "elders"', cat='translation', refs=['7:3'], text='Literally "older men", the leaders of a community.'),
 dict(term='τῶν Ἰουδαίων, "of the Judeans"', cat='translation', refs=['7:3'], text='Ἰουδαῖος is a person of Judea and its people, defined by land and ancestry as much as by religion. "Jews" is the later, wider category.'),
 dict(term='διασώσῃ, "bring safely through"', cat='translation', refs=['7:3'], text='δια-σῴζω, to save through, bring through danger.'),
 dict(term='Ἄξιος, "worthy", and 7:6 ἱκανός, "fit"', cat='translation', refs=['7:4'], text='Two different words. ἄξιος is deserving, of weight; ἱκανός is sufficient, adequate. 7:7 ἠξίωσα, "count worthy", returns to the first.'),
 dict(term='τὴν συναγωγήν, "the assembly"', cat='translation', refs=['7:5'], text='Here the building where the assembly meets.'),
 dict(term='Κύριε, "Lord"', cat='translation', refs=['7:6'], text='"Lord, sir": the capital is only the start of the address. Not the divine name.'),
 dict(term='σκύλλου, "trouble yourself"', cat='translation', refs=['7:6'], text='Literally "be harassed, be put to bother".'),
 dict(term='εἰπὲ λόγῳ, "say it with a word"', cat='translation', refs=['7:7'], text='λόγος, word, as at 4:32.'),
 dict(term='ὁ παῖς μου, "my boy"', cat='translation', refs=['7:7'], text='παῖς means a child, a boy, and is used of a young slave. Here it is the slave of 7:2.'),
 dict(term='τασσόμενος, "set"', cat='translation', refs=['7:8'], text='Put in place, ranked: a military word.'),
 dict(term='Πορεύθητι, "Go!"', cat='translation', refs=['7:8'], text='The road verb, πορεύομαι.'),
 dict(term='πίστιν, "trust"', cat='translation', refs=['7:9'], text='As at 5:20.'),
 dict(term='ἐν τῷ ἑξῆς, "on the next day"', cat='translation', refs=['7:11'], text='Literally "in the next", in sequence. It can also mean "soon afterwards".'),
 dict(term='μονογενής, "only-born"', cat='translation', refs=['7:12'], text='The only child born to her.'),
 dict(term='ὁ κύριος, "the lord"', cat='translation', refs=['7:13'], text='The narrator calls Jesus "the lord", the ordinary word for a master. Lower case: it is not the divine name, and capitals would make it a doctrine.'),
 dict(term='ἐσπλαγχνίσθη, "was moved with compassion"', cat='translation', refs=['7:13'], text='From σπλάγχνα, the inner organs, felt as the seat of feeling: "his inward parts were moved".'),
 dict(term='σοροῦ, "bier"', cat='translation', refs=['7:14'], text='An open coffin or bier.'),
 dict(term='ἐγέρθητι, "get up!"', cat='translation', refs=['7:14'], text='The aorist passive of ἐγείρω, "be raised, rise". The people\'s "has been raised" (7:16) is the same verb.'),
 dict(term='Προφήτης μέγας ἠγέρθη, "a great prophet has been raised"', cat='translation', refs=['7:16'], text='The passive leaves unnamed who raised him.'),
 dict(term='Ἐπεσκέψατο, "has visited"', cat='translation', refs=['7:16'], text='To look upon, look after, go to see. The word for an overseer comes from it.'),
 dict(term='ὁ βαπτιστής, "the baptiser"', cat='translation', refs=['7:20'], text='One who dips, immerses (βαπτίζω). "The Baptist" makes it a title and hides the verb.'),
 dict(term='μαστίγων, "scourges"', cat='translation', refs=['7:21'], text='Literally "whips", afflictions felt as blows.'),
 dict(term='ἐχαρίσατο, "granted"', cat='translation', refs=['7:21'], text='χαρίζομαι, to give as a favour (χάρις). The same verb is "freely granted" at 7:42–43.'),
 dict(term='ἀναβλέπουσιν, "see again"', cat='translation', refs=['7:22'], text='Literally "look up". It means to regain one\'s sight.'),
 dict(term='λεπροί, "the leprous"', cat='translation', refs=['7:22'], text='As at 5:12.'),
 dict(term='πτωχοὶ εὐαγγελίζονται, "the destitute are being given the good news"', cat='translation', refs=['7:22'], text='A passive: good news is announced to them.'),
 dict(term='μακάριος, "fortunate"', cat='translation', refs=['7:23'], text='As at 6:20.'),
 dict(term='σκανδαλισθῇ, "tripped up"', cat='translation', refs=['7:23'], text='σκάνδαλον is the trigger of a trap, a stumbling block. "Take offence" is the meaning in use; the image is of tripping.'),
 dict(term='τῶν ἀγγέλων Ἰωάννου, "John\'s messengers"', cat='translation', refs=['7:24'], text='ἄγγελος, messenger: here two men. The same word as in 7:27.'),
 dict(term='θεάσασθαι, "gaze at"', cat='translation', refs=['7:24'], text='To look at as at a spectacle.'),
 dict(term='ἐν τοῖς βασιλείοις, "in royal houses"', cat='translation', refs=['7:25'], text='Palaces.'),
 dict(term='τὸν ἄγγελόν μου, "my messenger"', cat='translation', refs=['7:27'], text='A quotation (Mal 3:1; Ex 23:20). ἄγγελος is the word for messenger, here a human one.'),
 dict(term='κατασκευάσει, "will make ready"', cat='translation', refs=['7:27'], text='To prepare, equip.'),
 dict(term='ὁ μικρότερος, "the lesser one"', cat='translation', refs=['7:28'], text='A comparative, "the smaller, the lesser". It is often read as a superlative, "the least".'),
 dict(term='κατεκλίθη, "reclined at table"', cat='translation', refs=['7:36'], text='Formal meals were eaten lying on couches.'),
 dict(term='ἁμαρτωλός, "a sinner"', cat='translation', refs=['7:37'], text='The text does not say what her sin was. The common idea that she was a prostitute is not in the Greek.'),
 dict(term='ἀλάβαστρον μύρου, "an alabaster flask of perfumed oil"', cat='translation', refs=['7:37'], text='μύρον is scented oil, perfume. It is kept apart from ἔλαιον, plain olive oil (7:46).'),
 dict(term='κατεφίλει, "kissing again and again"', cat='translation', refs=['7:38'], text='The imperfect of a strengthened verb: she kept kissing.'),
 dict(term='φησίν, "he says"', cat='translation', refs=['7:40'], text='The present tense, in the middle of past narration. The Greek has it, and so does the English.'),
 dict(term='δηνάρια, "denarii"', cat='translation', refs=['7:41'], text="The denarius was a day's wage for a labourer. δανιστής is a moneylender."),
 dict(term='ἐχαρίσατο, "freely granted"', cat='translation', refs=['7:42'], text='χαρίζομαι, to give as a favour. The debt is not "cancelled" in so many words; it is given as a gift.'),
 dict(term='ὅτι ἠγάπησεν πολύ, "because she loved much"', cat='translation', refs=['7:47'], text='ὅτι can give the cause ("because she loved") or the evidence ("as is shown by her love"). The sentence that follows ("the one to whom little is let go loves little") points to the second. The Greek allows both.'),
 dict(term='ἀφέωνται, "have been let go"', cat='translation', refs=['7:47'], text='As at 5:20.'),
 dict(term='συνανακείμενοι, "those reclining at table with him"', cat='translation', refs=['7:49'], text='The other guests.'),
 dict(term='σέσωκεν, "has saved"', cat='translation', refs=['7:50'], text='σῴζω, to save, rescue, make well.'),
 dict(term='πορεύου εἰς εἰρήνην, "journey into peace"', cat='translation', refs=['7:50'], text='εἰς, "into". Behind it lies the Hebrew greeting lekhi le-shalom, "go to peace".'),
]
