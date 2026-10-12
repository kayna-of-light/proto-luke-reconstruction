"""Batch 2, chapter 6 of the reconstruction: Luke 8:26–9:17."""
from buildlib import greek
from batch1_ch2 import U, A
from batch2_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}
AD = lambda loc, ev: {'source': f'Dialogue of Adamantius {loc} (Bakhuyzen; via Roth)', 'evidence': ev}

ENTRIES = [
 U('8:26', G('8:26'), 'Then they sailed to the region of the Gerasenes, which is opposite Galilee.',
   'Opens the attested pericope 8:26–39.'),
 A('8:27', G('8:27'), 'As he stepped out on land, a man from the town who had daimons met him. For a long time he had worn no clothes, and he did not live in a house but among the tombs.',
   'present (Marc. 4.20.4)', [T('4.20.4', '"cum invenis in uno homine multitudinem daemonum".')]),
 A('8:28', G('8:28'), 'When he saw Jesus, he cried out and fell down before him and said with a loud voice, "What have I to do with you, Jesus, son of the Most High God? I beg you, do not torment me."',
   'present (Marc. 4.20.5)', [T('4.20.5', '"Cuius autem dei filium Iesum legio testata est? Sine dubio cuius tormenta et abyssum noverant et timebant."')]),
 U('8:29', G('8:29'), 'For he had commanded the unclean spirit to come out of the man. Many times it had seized him; he was kept under guard and bound with chains and shackles, but he would break the bonds and be driven by the daimon into the wilderness.',
   'Inside the attested pericope 8:26–39.'),
 A('8:30', G('8:30'), 'Jesus asked him, "What is your name?" He said, "Legion", because many daimons had entered him.',
   'present (Marc. 4.20.4; Adam. 36,20)', [T('4.20.4', '"legionem se professam".')]),
 A('8:31', G('8:31'), 'And they begged him not to order them to go away into the abyss.',
   'present (Marc. 4.20.6)', [T('4.20.6', '"veniam scilicet abyssi creatoris".')]),
 A('8:32', G('8:32'), 'A large herd of pigs was feeding there on the hillside, and they begged him to let them enter these; and he gave them permission.',
   'present (Marc. 4.20.6–7)', [T('4.20.6', '"Denique impetraverunt."')]),
 U('8:33', G('8:33'), 'Then the daimons came out of the man and entered the pigs, and the herd rushed down the steep bank into the lake and was drowned.',
   'Inside the attested pericope 8:26–39.'),
 U('8:34', G('8:34'), 'When the herdsmen saw what had happened, they fled and told it in the town and in the countryside.', 'Inside the attested pericope 8:26–39.'),
 U('8:35', G('8:35'), 'People came out to see what had happened. They came to Jesus and found the man from whom the daimons had gone out sitting at the feet of Jesus, clothed and in his right mind; and they were afraid.', 'Inside the attested pericope 8:26–39.'),
 U('8:36', G('8:36'), 'Those who had seen it told them how the man who had been possessed had been saved.', 'Inside the attested pericope 8:26–39.'),
 U('8:37', G('8:37'), 'Then all the people of the surrounding country of the Gerasenes asked him to leave them, for they were seized with great fear. So he got into the boat and returned.', 'Inside the attested pericope 8:26–39.'),
 U('8:38', G('8:38'), 'The man from whom the daimons had gone out begged that he might be with him; but he sent him away, saying,', 'Inside the attested pericope 8:26–39.'),
 U('8:39', G('8:39'), '"Return to your home, and tell how much God has done for you." And he went away, proclaiming throughout the whole town how much Jesus had done for him.', 'Inside the attested pericope 8:26–39.'),
 U('8:40', G('8:40'), 'When Jesus returned, the crowd welcomed him, for they were all waiting for him.',
   'Opens the NA27 paragraph 8:40–56, whose central part (8:42b–48) is attested; Epiphanius\' "as they were going" presupposes the journey to Jairus\' house.'),
 U('8:41', G('8:41'), 'Then a man named Jairus came, a leader of the synagogue. He fell at Jesus\' feet and begged him to come to his house,', 'Inside the attested paragraph 8:40–56.'),
 A('8:42', G('8:42'), 'for he had an only daughter, about twelve years old, and she was dying. As he went, the crowds pressed in on him.',
   'present for 8:42b (Pan. 42.11.6, sch. 14); 8:42a unattested',
   [E(14, '»ἐγένετο δὲ ἐν τῷ ὑπάγειν αὐτούς, συνέπνιγον αὐτὸν οἱ ὄχλοι«.')],
   wording='NA27. 8:42a (the daughter) is unattested; printed within the attested verse.'),
 A('8:43', G('8:43'), 'And a woman who had suffered from a flow of blood for twelve years, and had spent all she had on physicians, and could not be healed by anyone,',
   'present (Marc. 4.20.7–8; Pan. 42.11.6, sch. 14)',
   [E(14, '»καὶ γυνὴ ἁψαμένη αὐτοῦ ἰάθη τοῦ αἵματος«.'), T('4.20.7', '"Tangitur a femina quae sanguine fluitabat".')],
   wording='NA27, including its bracketed clause [ἰατροῖς προσαναλώσασα ὅλον τὸν βίον] (no witness lacks it).'),
 A('8:44', G('8:44'), 'came up behind him and touched the fringe of his cloak, and immediately her flow of blood stopped.',
   'present (Marc. 4.20.8, 13; Pan. 42.11.6, sch. 14)', [T('4.20.13', '"dum tangitur vestimentum eius".')]),
 A('8:45', G('8:45', [('Τίς ὁ ἁψάμενός μου;', 'Τίς μου ἥψατο;')]),
   'Jesus said, "Who touched me?" When all denied it, Peter said, "Master, the crowds are surrounding you and pressing in on you."',
   'present (Marc. 4.20.8; Pan. 42.11.6, sch. 14)',
   [E(14, '»καὶ εἶπεν ὁ κύριος· τίς μου ἥψατο;«'), T('4.20.8', '"Quis me, inquit, tetigit? Etiam excusantibus discipulis…"')],
   wording='Marcionite reading adopted: τίς μου ἥψατο; for τίς ὁ ἁψάμενός μου; (Epiphanius\' Greek, with Tertullian "Quis me tetigit?"; Roth: secure). Epiphanius\' ὁ κύριος for ὁ Ἰησοῦς is rated possible; not adopted. Tertullian\'s "excusantibus discipulis" (the disciples, not Peter alone) is rated possible; noted.'),
 A('8:46', G('8:46'), 'But Jesus said, "Someone touched me; for I know that power has gone out from me."',
   'present (Marc. 4.20.8; Pan. 42.11.6, sch. 14)',
   [E(14, '»ἥψατό μού τις. καὶ γὰρ ἔγνων δύναμιν ἐξελθοῦσαν ἀπ\' ἐμοῦ«.'), T('4.20.8', '"Tetigit me aliquis… Sensi enim virtutem ex me profectam."')],
   wording='NA27. Epiphanius\' καὶ γάρ and ἐξελθοῦσαν are rated possible and probable by Roth; not adopted.'),
 U('8:47', G('8:47'), 'When the woman saw that she could not remain hidden, she came trembling, and falling down before him she declared in the presence of all the people why she had touched him and how she had been healed at once.',
   'Inside the attested paragraph 8:40–56.'),
 A('8:48', G('8:48'), 'He said to her, "Daughter, your faith has saved you; go in peace."',
   'present (Marc. 4.20.9)', [T('4.20.9', '"cum dicit, Fides tua te salvam fecit".')]),
 U('8:49', G('8:49'), 'While he was still speaking, someone came from the house of the leader of the synagogue and said, "Your daughter is dead; do not trouble the teacher any longer."', 'Inside the attested paragraph 8:40–56 (NA27 continues the paragraph at 8:49).'),
 U('8:50', G('8:50'), 'When Jesus heard this, he answered him, "Do not be afraid; only believe, and she will be saved."', 'Inside the attested paragraph 8:40–56.'),
 U('8:51', G('8:51'), 'When he came to the house, he let no one go in with him except Peter, John and James, and the child\'s father and mother.', 'Inside the attested paragraph 8:40–56.'),
 U('8:52', G('8:52'), 'Everyone was weeping and mourning for her; but he said, "Do not weep, for she is not dead but asleep."', 'Inside the attested paragraph 8:40–56.'),
 U('8:53', G('8:53'), 'And they laughed at him, knowing that she was dead.', 'Inside the attested paragraph 8:40–56.'),
 U('8:54', G('8:54'), 'But he took her by the hand and called out, "Child, get up!"', 'Inside the attested paragraph 8:40–56.'),
 U('8:55', G('8:55'), 'Her spirit returned, and she got up at once; and he directed that she be given something to eat.', 'Inside the attested paragraph 8:40–56.'),
 U('8:56', G('8:56'), 'Her parents were amazed; but he ordered them to tell no one what had happened.', 'Inside the attested paragraph 8:40–56.'),
 A('9:1', G('9:1'), 'He called the twelve together and gave them power and authority over all daimons and to cure diseases,',
   'present (Adam. 82,2–4)',
   [AD('82,2–4 (2.12)', 'The orthodox speaker Adamantius reads 9:1–2 "from the gospel" as an argument against the Marcionite Marcus, which presupposes that Marcus accepts the passage. A weaker attestation than a Marcionite speaker\'s.')]),
 A('9:2', G('9:2', [('καὶ ἰᾶσθαι τοὺς ἀσθενεῖς,', 'καὶ ἰᾶσθαι,')]), 'and he sent them out to proclaim the kingdom of God and to heal.',
   'present (Marc. 4.21.1; Adam. 82,4–5)', [T('4.21.1', '"Dimittit discipulos ad praedicandum dei regnum."'),
    AD('82,4–5 (2.12)', '»καὶ ἀπέστειλεν αὐτοὺς κηρύσσειν τὴν βασιλείαν τοῦ θεοῦ καὶ ἰᾶσθαι.«')],
   wording='NA27 without its bracketed [τοὺς ἀσθενεῖς] (METHOD §5: bracketed words are printed unless a witness lacks them; Adamantius\' reading of the verse ends at ἰᾶσθαι).'),
 A('9:3', G('9:3'), 'He said to them, "Take nothing for the journey: no staff, no bag, no bread, no money, and do not have two tunics.',
   'present (Marc. 4.21.1)', [T('4.21.1', '"Prohibet eos victui aut vestitui quid in viam ferre."')]),
 U('9:4', G('9:4'), 'Whatever house you enter, stay there, and leave from there.', 'Inside the attested pericope 9:1–6.'),
 A('9:5', G('9:5'), 'Wherever they do not welcome you, as you leave that town shake the dust off your feet as a testimony against them."',
   'present (Marc. 4.21.1)', [T('4.21.1', '"At cum iubet pulverem excutere de pedibus in eos a quibus excepti non fuissent, et hoc in testimonium mandat fieri."')]),
 A('9:6', G('9:6'), 'They set out and went through the villages, bringing the good news and curing people everywhere.',
   'present (Adam. 82,6–7)', [AD('82,6–7 (2.12)', 'Read by Adamantius in the same argument as 9:1–2 (see 9:1): »ἐξερχόμενοι δὲ διήρχοντο κατὰ πόλεις καὶ κώμας…«.')],
   wording='NA27. Adamantius\' "through towns and villages" is rated possible by Roth; not adopted.'),
 A('9:7', G('9:7'), 'Herod the tetrarch heard about all that was happening, and he was perplexed, because it was said by some that John had been raised from the dead,',
   'present (Marc. 4.21.2)', [T('4.21.2', '"Christum Iesum alii Ioannem, alii Heliam, alii unum aliquem ex veteribus prophetis Herodi adseverabant".')]),
 A('9:8', G('9:8'), 'by some that Elijah had appeared, and by others that one of the ancient prophets had arisen.',
   'present (Marc. 4.21.2)', [T('4.21.2', 'see 9:7.')]),
 U('9:9', G('9:9'), 'Herod said, "John I beheaded; but who is this about whom I hear such things?" And he tried to see him.', 'Inside the attested pericope 9:7–9.'),
 U('9:10', G('9:10'), 'When the emissaries returned, they told him all that they had done. He took them with him and withdrew privately to a town called Bethsaida.', 'Inside the attested pericope 9:10–17.'),
 U('9:11', G('9:11'), 'When the crowds found out, they followed him; and he welcomed them, spoke to them about the kingdom of God, and healed those who needed healing.', 'Inside the attested pericope 9:10–17.'),
 A('9:12', G('9:12'), 'The day began to decline, and the twelve came to him and said, "Send the crowd away, so that they may go into the surrounding villages and countryside to find lodging and provisions; for we are here in a deserted place."',
   'present (Marc. 4.21.2–3)', [T('4.21.2', '"Pascit populum in solitudine".')]),
 A('9:13', G('9:13'), 'But he said to them, "You give them something to eat." They said, "We have no more than five loaves and two fish, unless we are to go and buy food for all these people."',
   'present (Marc. 4.21.3)', [T('4.21.3', '"nec de inferioribus materiis panis et piscis".')]),
 A('9:14', G('9:14'), 'For there were about five thousand men. And he said to his disciples, "Make them sit down in groups of about fifty each."',
   'present (Marc. 4.21.3)', [T('4.21.3', '"nec quinque circiter sed sexcenta milia hominum".')]),
 U('9:15', G('9:15'), 'They did so, and made them all sit down.', 'Inside the attested pericope 9:10–17.'),
 A('9:16', G('9:16', [('εὐλόγησεν αὐτοὺς', 'εὐλόγησεν ἐπ’ αὐτοὺς')]),
   'And taking the five loaves and the two fish, he looked up to heaven and blessed over them, and broke them, and gave them to the disciples to set before the crowd.',
   'present (Pan. 42.11.6, sch. 15; [Adam. 108,25])',
   [E(15, '»ἀναβλέψας εἰς τὸν οὐρανὸν εὐλόγησεν ἐπ\' αὐτούς«.')],
   wording='Marcionite reading adopted: εὐλόγησεν ἐπ\' αὐτούς (Epiphanius\' Greek; Roth: very likely). NA27 apparatus: ἐπ\' αὐτ. D it sy(s).c; McionE.',
   western='Agrees with D and the Old Latin and Old Syriac.'),
 A('9:17', G('9:17'), 'And all ate and were filled; and what was left over was gathered up, twelve baskets of broken pieces.',
   'present (Marc. 4.21.4)', [T('4.21.4', '"ut et pabuli exiguitatem non tantum sufficere, verum etiam exuberare… voluerit".')]),
]

OMITTED = []

PREAMBLE = (
 "Three works of power and the mission of the twelve. On the far shore Jesus frees a man held by a \"legion\" of daimons, who "
 "beg not to be sent into the abyss. Back among the crowds, a woman who has bled for twelve years touches his cloak and is "
 "healed, and the text has him ask, \"Who touched me?\" Tertullian quotes the question and uses it against Marcion's teaching "
 "that Jesus' body was not real (Marc. 4.20.7–14). The twelve are sent to proclaim the kingdom without provisions. Herod hears "
 "that Jesus is taken for John, Elijah or one of the ancient prophets. In a deserted place five thousand are fed from five "
 "loaves and two fish. The witnesses cite the woman's healing but not the raising of Jairus' daughter that frames it; the "
 "frame is printed in grey, because Epiphanius' \"as they were going\" presupposes the journey to Jairus' house."
)

NOTES = [
 dict(term='The legion (8:26–39)', cat='textual', refs=['8:27', '8:28', '8:30', '8:31', '8:32'], text=(
  "Tertullian, Marc. 4.20.4–7: \"a multitude of daimons in one man\", the name \"legion\", the cry that Jesus is \"son of God\", "
  "and the plea not to be sent into the abyss, which he says Jesus granted (\"Denique impetraverunt\"). The binding with chains "
  "(8:29), the drowning of the herd and the reaction of the townspeople (8:33–39) are not cited and are printed in grey.")),
 dict(term='Daimons and the abyss', cat='theological', refs=['8:28', '8:31'], text=(
  "Reception. Tertullian argues that the daimons knew whose son Jesus was because they feared the Creator's abyss, and that "
  "Jesus' granting their request proves he belonged to that God (Marc. 4.20.5–7). The text itself says only that they begged "
  "not to be sent into the abyss (ἄβυσσος, the deep in the Greek Bible).")),
 dict(term='The woman who touched his cloak (8:42b–48)', cat='textual', refs=['8:42', '8:43', '8:44', '8:45', '8:46', '8:48'], text=(
  "Epiphanius, sch. 14: »ἐγένετο δὲ ἐν τῷ ὑπάγειν αὐτούς, συνέπνιγον αὐτὸν οἱ ὄχλοι. καὶ γυνὴ ἁψαμένη αὐτοῦ ἰάθη τοῦ "
  "αἵματος· καὶ εἶπεν ὁ κύριος· τίς μου ἥψατο;« and »ἥψατό μού τις. καὶ γὰρ ἔγνων δύναμιν ἐξελθοῦσαν ἀπ' ἐμοῦ«. Tertullian, "
  "Marc. 4.20.7–13: \"Quis me, inquit, tetigit?… Tetigit me aliquis… Sensi enim virtutem ex me profectam… Fides tua te salvam "
  "fecit.\" Both witnesses give the question as \"Who touched me?\" (τίς μου ἥψατο;) where NA27 has \"Who is the one who touched "
  "me?\"; the attested form is printed. 8:47 is not cited and is printed in grey.")),
 dict(term='The woman and the law of purity', cat='theological', refs=['8:43', '8:48'], text=(
  "Reception and interpretation. The Marcionites read the healing as Jesus setting aside the law that made a woman with a flow "
  "of blood unclean (Lev 15:25–27). Tertullian answers that the law concerns the regular flow, not a disease, and that the "
  "woman did not break it (Marc. 4.20.9–12). The text itself says nothing about the law: it reports the touch, the power going "
  "out, and the woman's faith. The legal questions belong to the readers.")),
 dict(term='Jairus\' daughter (8:40–42a, 8:49–56)', cat='textual', refs=['8:40', '8:41', '8:49', '8:56'], text=(
  "No witness cites the request of Jairus or the raising of his daughter. Epiphanius' quotation begins \"as they were going\", "
  "which presupposes the journey to Jairus' house, and NA27 prints 8:40–56 as one paragraph. The frame is therefore printed in "
  "grey, as part of an attested passage. Tertullian had already used the raising of the widow's son (7:11–17) to argue that "
  "raising the dead was the Creator's sign (4.18.2), so a second raising would add nothing to his case. That is why his "
  "silence here is not counted as evidence of absence.")),
 dict(term='The mission of the twelve (9:1–6)', cat='textual', refs=['9:1', '9:2', '9:3', '9:5', '9:6'], text=(
  "Tertullian, Marc. 4.21.1: the disciples are sent to preach the kingdom of God, are forbidden to take food or clothing for "
  "the road, and are told to shake the dust from their feet \"as a testimony\". 9:1–2 and 9:6 are also read in the Dialogue of "
  "Adamantius (82,2–7) by the orthodox speaker, as an argument the Marcionite is expected to accept; Roth counts this as "
  "attestation. 9:4 is not cited and is printed in grey.")),
 dict(term='Herod and the prophets (9:7–9)', cat='textual', refs=['9:7', '9:8', '9:9'], text=(
  "Tertullian, Marc. 4.21.2: \"some said John, some Elijah, some one of the ancient prophets\". He argues that whichever of "
  "these Jesus was, he was not raised to preach another god. 9:9 is not cited and is printed in grey.")),
 dict(term='The feeding (9:10–17)', cat='textual', refs=['9:12', '9:13', '9:14', '9:16', '9:17'], text=(
  "Tertullian, Marc. 4.21.2–5 compares the feeding with the manna and with Elisha's loaves (2 Kgs 4:42–44); Epiphanius, sch. 15 "
  "quotes 9:16 as »ἀναβλέψας εἰς τὸν οὐρανὸν εὐλόγησεν ἐπ' αὐτούς« (\"he blessed over them\"), printed here (Roth: very "
  "likely). 9:10–11 and 9:15 are not cited and are printed in grey. The previous text treated the distribution clause of 9:16 "
  "as an excision; no witness supports that.")),
 dict(term='After the feeding: Mark 6:45–8:26', cat='textual', refs=['9:17'], text=(
  "Both this text and canonical Luke pass from the feeding (Mark 6:30–44) to Peter's confession (Mark 8:27–30) and lack the "
  "intervening block of Mark (6:45–8:26). The previous note presented this \"Great Omission\" as evidence that Proto-Luke is "
  "independent of Mark; since canonical Luke lacks the same block, it tells nothing about the relation between the two texts "
  "(audit context §5).")),
]
