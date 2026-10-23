"""Batch 2, chapter 4 of the reconstruction: Luke 7."""
from buildlib import greek
from batch1_ch2 import U, A
from batch2_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}

ENTRIES = [
 U('7:1', G('7:1'), 'When he had finished all his sayings in the hearing of the people, he entered Capernaum.',
   'Opens the attested pericope 7:1–10.'),
 A('7:2', G('7:2'), 'A centurion had a slave who was ill and close to death, a slave he valued highly.',
   'present (Marc. 4.18.1)', [T('4.18.1', '"Proinde extollenda fide centurionis…" — the centurion.')],
   wording='NA27. Only the centurion is attested; the details of the verse are not.'),
 U('7:3', G('7:3'), 'When he heard about Jesus, he sent elders of the Jews to him, asking him to come and save his slave.'),
 U('7:4', G('7:4'), 'They came to Jesus and pleaded with him earnestly, saying, "He deserves to have you do this for him,'),
 U('7:5', G('7:5'), 'for he loves our nation, and he built our synagogue for us."'),
 U('7:6', G('7:6'), 'So Jesus went with them. When he was not far from the house, the centurion sent friends to say to him, "Lord, do not trouble yourself, for I am not worthy to have you come under my roof;'),
 U('7:7', G('7:7'), 'that is why I did not presume to come to you. But say the word, and let my servant be healed.'),
 U('7:8', G('7:8'), 'For I too am a man set under authority, with soldiers under me; I say to one, \'Go\', and he goes, and to another, \'Come\', and he comes, and to my slave, \'Do this\', and he does it."'),
 A('7:9', G('7:9', [('Λέγω ὑμῖν, οὐδὲ ἐν τῷ Ἰσραὴλ τοσαύτην πίστιν εὗρον.', 'Λέγω ὑμῖν, τοσαύτην πίστιν οὐδὲ ἐν τῷ Ἰσραὴλ εὗρον.')]), 'When Jesus heard this he was amazed at him, and turning to the crowd that followed him he said, "I tell you, such faith I have not found even in Israel."',
   'present (Marc. 4.18.1; Pan. 42.11.6, sch. 7)',
   [E(7, '»λέγω δὲ ὑμῖν, τοσαύτην πίστιν οὐδὲ ἐν τῷ Ἰσραὴλ εὗρον«.'),
    T('4.18.1', '"si is professus est talem se fidem nec in Israele invenisse".')],
   wording='NA27 words in the order of Epiphanius\' quotation (τοσαύτην πίστιν before οὐδὲ ἐν τῷ Ἰσραήλ; Roth: secure). Epiphanius\' δέ after λέγω is rated "likely not present" by Roth and is not printed.'),
 U('7:10', G('7:10'), 'And when those who had been sent returned to the house, they found the slave in good health.'),
 U('7:11', G('7:11'), 'Soon afterwards he went to a town called Nain, and his disciples and a large crowd went with him.',
   'Opens the attested pericope 7:11–17.'),
 A('7:12', G('7:12'), 'As he drew near to the gate of the town, a dead man was being carried out, his mother\'s only son, and she was a widow; and a considerable crowd from the town was with her.',
   'present (Marc. 4.18.2)', [T('4.18.2', '"Resuscitavit et mortuum filium viduae."')]),
 U('7:13', G('7:13'), 'When the Lord saw her, he had compassion for her and said to her, "Do not weep."'),
 A('7:14', G('7:14'), 'Then he came forward and touched the bier, and the bearers stood still. And he said, "Young man, I say to you, rise."',
   'present (Marc. 4.18.2)', [T('4.18.2', '"Resuscitavit et mortuum filium viduae."')]),
 A('7:15', G('7:15'), 'The dead man sat up and began to speak, and he gave him to his mother.',
   'present (Marc. 4.18.2)', [T('4.18.2', '"Resuscitavit et mortuum filium viduae."')]),
 A('7:16', G('7:16'), 'Fear seized them all, and they glorified God, saying, "A great prophet has arisen among us", and "God has visited his people."',
   'present (Marc. 4.18.2–3)',
   [T('4.18.3', '"omnes illic creatori gloriam retulerint dicentes, Magnus prophetes prodiit in nobis, et Respexit deus populum suum."')],
   wording='NA27. Tertullian\'s "prodiit" is read by Roth as ἐγήγερται (possible only); not adopted.'),
 U('7:17', G('7:17'), 'This word about him spread through all Judea and all the surrounding region.'),
 A('7:18', G('7:18'), 'The disciples of John reported all these things to him. And John called two of his disciples',
   'present (Marc. 4.18.4)', [T('4.18.4', '"Sed scandalizatur Ioannes auditis virtutibus Christi".')]),
 A('7:19', G('7:19'), 'and sent them to the Lord, saying, "Are you the one who is to come, or are we to wait for another?"',
   'present (Marc. 4.18.5–7; Adam. 50,12–14)', [T('4.18.6', '"Tu es, inquit, qui venis, an alium expectamus?"')]),
 A('7:20', G('7:20'), 'When the men came to him they said, "John the Baptist has sent us to you, saying, \'Are you the one who is to come, or are we to wait for another?\'"',
   'present (Marc. 4.18.6)', [T('4.18.6', 'The question repeated and explained.')]),
 U('7:21', G('7:21'), 'In that hour he cured many of diseases and afflictions and evil spirits, and to many who were blind he gave sight.',
   'Inside the attested pericope 7:18–23.'),
 A('7:22', G('7:22'), 'And he answered them, "Go and tell John what you have seen and heard: the blind see again, the lame walk, lepers are cleansed, the deaf hear, the dead are raised, the poor are given the good news.',
   'present (Marc. 4.18.6; Eznik, De Deo 358)', [T('4.18.6', '"ut dominus per easdem operationes agnoscendum se nuntiaverit Ioanni".')]),
 A('7:23', G('7:23'), 'And blessed is anyone who does not take offence at me."',
   'present (Marc. 4.18.8; Pan. 42.11.6, sch. 8; Ephrem)',
   [E(8, 'παρηλλαγμένον τὸ »μακάριος ὃς οὐ μὴ σκανδαλισθῇ ἐν ἐμοί«· εἶχε γὰρ ὡς πρὸς Ἰωάννην.'),
    T('4.18.8', '"qui non fuerit scandalizatus in Christum, quod tunc Ioannem minuit".')],
   wording='NA27. Epiphanius says the saying was "altered" in that it was taken as aimed at John (Holl: an application, not a different wording). Recorded as the Marcionite reading of the verse (reception).'),
 A('7:24', G('7:24'), 'When John\'s messengers had gone, he began to speak to the crowds about John: "What did you go out into the wilderness to look at? A reed shaken by the wind?',
   'present (Marc. 4.18.7–8)', [T('4.18.8', '"Quid existis videre in solitudinem?"')]),
 U('7:25', G('7:25'), 'What then did you go out to see? A man dressed in soft clothing? Those who wear splendid clothing and live in luxury are in royal palaces.',
   'Inside the attested passage 7:24–28.'),
 A('7:26', G('7:26'), 'What then did you go out to see? A prophet? Yes, I tell you, and more than a prophet.',
   'present (Marc. 4.18.7)', [T('4.18.7', '"propheten eum confirmans, immo et supra".')]),
 A('7:27', G('7:27'), 'This is the one of whom it is written, \'Behold, I send my messenger before your face, who will prepare your way before you.\'',
   'present (Marc. 4.18.4, 7, 8; Pan. 42.11.6, sch. 9; Adam. 98,11–13)',
   [E(9, '»αὐτός ἐστι περὶ οὗ γέγραπται· ἰδού, ἀποστέλλω τὸν ἄγγελόν μου πρὸ προσώπου σου«.'),
    T('4.18.7', '"Ecce ego mitto angelum meum ante faciem tuam, qui praeparabit viam tuam".')],
   wording='NA27. Epiphanius\' αὐτός for οὗτος is rated possible by Roth; ἔμπροσθέν σου is not in Tertullian\'s quotation (Roth: attested in Adamantius).'),
 A('7:28', G('7:28'), 'I tell you, among those born of women no one is greater than John; yet the least in the kingdom of God is greater than he."',
   'present (Marc. 4.18.8)', [T('4.18.8', '"maior quidem omnibus natis mulierum… qui minor fuerit in regno dei".')]),
 A('7:36', G('7:36'), 'One of the Pharisees asked him to eat with him, and he went into the Pharisee\'s house and reclined at table.',
   'present (Pan. 42.11.6, sch. 10)', [E(10, '»καὶ εἰσελθὼν εἰς τὸν οἶκον τοῦ Φαρισαίου κατεκλίθη«.')]),
 A('7:37', G('7:37'), 'And a woman of the town, who was a sinner, learned that he was reclining at table in the Pharisee\'s house, and she brought an alabaster jar of ointment.',
   'present (Marc. 4.18.9; Pan. 42.11.6, sch. 10)',
   [E(10, '»ἡ δὲ γυνὴ… ἡ ἁμαρτωλός«.'), T('4.18.9', '"Illius autem peccatricis feminae argumentum…"')]),
 A('7:38', G('7:38'), 'She stood behind him at his feet, weeping, and began to wet his feet with her tears and to wipe them with the hair of her head; and she kissed his feet and anointed them with the ointment.',
   'present (Marc. 4.18.9; Pan. 42.11.6, sch. 10)',
   [E(10, '»ἡ δὲ γυνὴ στᾶσα ὀπίσω ἡ ἁμαρτωλὸς παρὰ τοὺς πόδας ἔβρεξε τοῖς δάκρυσι τοὺς πόδας καὶ ἤλειψεν καὶ κατεφίλει«.'),
    T('4.18.9', '"cum pedes domini osculis figeret, lacrimis inundaret, crinibus detergeret, unguento perduceret".')],
   wording='NA27. The order of the actions differs between the two witnesses and from NA27; Roth leaves it open.'),
 U('7:39', G('7:39'), 'When the Pharisee who had invited him saw it, he said to himself, "If this man were a prophet, he would know who and what kind of woman this is who is touching him, that she is a sinner."',
   'Inside the attested pericope 7:36–50.'),
 U('7:40', G('7:40'), 'Jesus answered him, "Simon, I have something to say to you." "Say it, Teacher," he replied.', 'Inside the attested pericope 7:36–50.'),
 U('7:41', G('7:41'), '"A certain creditor had two debtors; one owed five hundred denarii, and the other fifty.', 'Inside the attested pericope 7:36–50.'),
 U('7:42', G('7:42'), 'When they could not pay, he cancelled the debts of both. Which of them, then, will love him more?"', 'Inside the attested pericope 7:36–50.'),
 U('7:43', G('7:43'), 'Simon answered, "I suppose the one for whom he cancelled the larger debt." And he said to him, "You have judged rightly."', 'Inside the attested pericope 7:36–50.'),
 A('7:44', G('7:44'), 'Then turning towards the woman, he said to Simon, "Do you see this woman? I entered your house; you gave me no water for my feet, but she has wet my feet with her tears and wiped them with her hair.',
   'present (Pan. 42.11.6, sch. 11)', [E(11, 'καὶ πάλιν »αὕτη τοῖς δάκρυσιν ἔβρεξέν τοὺς πόδας μου καὶ ἤλειψεν καὶ κατεφίλει«.')]),
 A('7:45', G('7:45'), 'You gave me no kiss, but from the time I came in she has not stopped kissing my feet.',
   'present (Pan. 42.11.6, sch. 11)', [E(11, '…καὶ κατεφίλει.')]),
 A('7:46', G('7:46'), 'You did not anoint my head with oil, but she has anointed my feet with ointment.',
   'present (Pan. 42.11.6, sch. 11)', [E(11, '…καὶ ἤλειψεν…')]),
 A('7:47', G('7:47'), 'Therefore, I tell you, her sins, which were many, have been forgiven, because she loved much; but the one to whom little is forgiven loves little."',
   'present (Marc. 4.18.9)', [T('4.18.9', '"ut peccatricis paenitentia secundum creatorem meruerit veniam".')]),
 A('7:48', G('7:48'), 'And he said to her, "Your sins are forgiven."',
   'present (Marc. 4.18.9)', [T('4.18.9', '"meruerit veniam".')]),
 U('7:49', G('7:49'), 'Those who were at table with him began to say among themselves, "Who is this who even forgives sins?"', 'Inside the attested pericope 7:36–50.'),
 A('7:50', G('7:50'), 'And he said to the woman, "Your faith has saved you; go in peace."',
   'present (Marc. 4.18.9)', [T('4.18.9', '"ab eo audiit, Fides tua te salvam fecit".')]),
]

OMITTED = [
 dict(ref='7:29–35', cls='U−', app=dict(roth='unattested', witnesses=[
      T('4.18.4–8', 'Argues throughout that John belongs to the Creator and that Christ confirms him.')],
      decision='not printed',
      reason='Tertullian works through 7:18–28 continuously (4.18.4–8) and passes to 7:36–50 (4.18.9). His whole argument there is that John is the Creator\'s prophet and that Christ endorses him. 7:29–30 (the people "justified God, having been baptized with John\'s baptism"; the Pharisees "rejected the counsel of God") and 7:33–35 (John and the son of man as wisdom\'s children) would have made that case directly; he does not cite them. The previous text also omitted 7:24–35 apart from 7:27–28.')),
]

PREAMBLE = (
 "Four scenes from the Galilean ministry. A centurion's faith is measured against Israel: \"such faith I have not found even in "
 "Israel.\" A widow's only son is raised at Nain, and the crowd acclaims Jesus in the language of Israel's scripture: \"A great "
 "prophet has arisen among us\" and \"God has visited his people.\" John the Baptist sends to ask whether Jesus is the one to "
 "come, and Jesus answers with the works of the prophets and calls John more than a prophet. In a Pharisee's house a woman of "
 "the town anoints his feet, and her sins are forgiven \"because she loved much.\" Tertullian works through the chapter in "
 "order (Marc. 4.18) and Epiphanius quotes from four of the scenes. Not printed: the passage on John's baptism and \"this "
 "generation\" (7:29–35), which no witness cites although Tertullian's argument needed it."
)

NOTES = [
 dict(term='The centurion (7:1–10)', cat='textual', refs=['7:2', '7:9'], text=(
  "Tertullian, Marc. 4.18.1, discusses only the centurion and the saying about faith in Israel; Epiphanius, sch. 7 quotes the "
  "saying: »λέγω δὲ ὑμῖν, τοσαύτην πίστιν οὐδὲ ἐν τῷ Ἰσραὴλ εὗρον«. Its word order (\"such faith\" first) is printed with "
  "NA27's words; Roth rates the words secure. The embassy of the Jewish elders, the friends and the centurion's speech (7:3–8) "
  "and the return of the messengers (7:10) are not cited and are printed in grey.")),
 dict(term='"A great prophet has arisen among us" (7:16)', cat='theological', refs=['7:16'], text=(
  "Tertullian, Marc. 4.18.3 quotes the acclamation, \"Magnus prophetes prodiit in nobis, et Respexit deus populum suum\", and "
  "argues that the crowd glorified the Creator and Jesus did not correct them. Interpretation: in the attested text the people of "
  "Israel name Jesus a prophet and see in the raising a visitation of their God. This is the attested place for the prophet "
  "Christology the library builds on; the phrase \"a prophet mighty in deed and word\" (24:19), used as a title in the library, is "
  "itself unattested for this text (working document §5).")),
 dict(term='John\'s question (7:18–23)', cat='textual', refs=['7:18', '7:19', '7:20', '7:22', '7:23'], text=(
  "Tertullian, Marc. 4.18.4–8 attests John hearing of Jesus' works, the question \"Are you the one who is to come, or are we to "
  "wait for another?\" (quoted twice) and the answer by works. Epiphanius, sch. 8 says the beatitude of 7:23 was \"altered\" "
  "because Marcion's text had it \"as if addressed to John\"; Holl explains this as Marcion's application of the saying, not a "
  "different wording. That is how the Marcionite community read the verse (reception). 7:21 is not cited and is printed in "
  "grey.")),
 dict(term='ἄγγελος as "messenger" (7:24, 7:27)', cat='translation', refs=['7:24', '7:27'], text=(
  "ἄγγελος is rendered \"messenger\" (lower case): John's messengers at 7:24, and the messenger of Malachi 3:1 at 7:27. "
  "Tertullian's Latin has \"angelum\" in the quotation of 7:27 and he plays on the sense \"angel\" (4.18.7, \"ut angelum\").")),
 dict(term='John and the kingdom (7:24–28)', cat='textual', refs=['7:24', '7:26', '7:27', '7:28'], text=(
  "Tertullian, Marc. 4.18.7–8 and Epiphanius, sch. 9 attest the testimony to John: the question \"What did you go out into the "
  "wilderness to see?\", \"a prophet, and more\", the quotation of Malachi 3:1, and \"the least in the kingdom of God is greater "
  "than he\". 7:25 is not cited and is printed in grey. Tertullian reports the Marcionite reading that the kingdom of 7:28 "
  "belongs to a different god from John's; he answers that both belong to the same God (reception).")),
 dict(term='Not printed: 7:29–35', cat='excision', refs=['7:28', '7:36'], text=(
  "7:29–30 (the people and the tax collectors \"justified God\" by John's baptism; the Pharisees rejected \"the counsel of God\") "
  "and 7:31–35 (\"this generation\" and the children in the market-place; \"wisdom is justified by all her children\") are not "
  "cited. Tertullian works through 7:18–28 and then 7:36–50 without a gap in his argument, and these verses would have been his "
  "best evidence that John's baptism was God's own plan. They are classed \"unattested, probably absent\" (METHOD §3).")),
 dict(term='The woman who loved much (7:36–50)', cat='textual', refs=['7:36', '7:37', '7:38', '7:44', '7:45', '7:46', '7:47', '7:48', '7:50'], text=(
  "Epiphanius, sch. 10–11 quotes 7:36, 7:38 and 7:44–46; Tertullian, Marc. 4.18.9 attests the woman, her tears, kisses and "
  "ointment, the forgiveness and \"Your faith has saved you\". The Pharisee's thought and the parable of the two debtors "
  "(7:39–43) and the guests' question (7:49) are not cited and are printed in grey. Tertullian uses the woman's touch as proof "
  "that Jesus had a real body (4.18.9), his own argument against Marcion's Christology.")),
 dict(term='Faith shown in deeds', cat='theological', refs=['7:47', '7:50'], text=(
  "Interpretation. In the attested scene the woman's faith (7:50) is visible in what she does: the tears, the kisses, the "
  "ointment. Her forgiveness is tied to her love (\"because she loved much\", 7:47). The pairing of faith with acts matches the "
  "Epistle of James (\"faith was active along with his works\", Jas 2:22), which the library takes as the closest written "
  "witness to the community behind this text (Carriers of Living Water §3.4).")),
]
