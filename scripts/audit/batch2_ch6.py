"""Batch 2, chapter 6 of the reconstruction: Luke 8:26–9:17."""
from buildlib import greek
from batch1_ch2 import U, A
from batch2_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}
AD = lambda loc, ev: {'source': f'Dialogue of Adamantius {loc} (Bakhuyzen; via Roth)', 'evidence': ev}

ENTRIES = [
 U('8:26', G('8:26'), 'And they sailed down to the country of the Gerasenes, which is opposite Galilee.',
   'Opens the attested pericope 8:26–39.'),
 A('8:27', G('8:27'), 'And as he went out onto the land, a certain man from the city met him, having daimons; and for a long time he had not put on a garment, and he did not stay in a house but among the tombs.',
   'present (Marc. 4.20.4)', [T('4.20.4', '"cum invenis in uno homine multitudinem daemonum".')]),
 A('8:28', G('8:28'), 'And seeing Jesus, crying out, he fell down before him and said with a loud voice, "What is there between me and you, Jesus, son of the Highest God? I beg you, do not torture me."',
   'present (Marc. 4.20.5)', [T('4.20.5', '"Cuius autem dei filium Iesum legio testata est? Sine dubio cuius tormenta et abyssum noverant et timebant."')]),
 U('8:29', G('8:29'), 'For he was ordering the unclean spirit to go out from the person. For many times it had seized him, and he was bound with chains and fetters and kept under guard, and tearing the bonds apart he was driven by the daimon into the deserts.',
   'Inside the attested pericope 8:26–39.'),
 A('8:30', G('8:30'), 'And Jesus asked him, "What is your name?" And he said, "Legion," because many daimons had gone into him.',
   'present (Marc. 4.20.4; Adam. 36,20)', [T('4.20.4', '"legionem se professam".')]),
 A('8:31', G('8:31'), 'And they were urging him not to order them to go away into the abyss.',
   'present (Marc. 4.20.6)', [T('4.20.6', '"veniam scilicet abyssi creatoris".')]),
 A('8:32', G('8:32'), 'Now there was a sizeable herd of pigs there, feeding on the mountain; and they urged him to allow them to go into those; and he allowed them.',
   'present (Marc. 4.20.6–7)', [T('4.20.6', '"Denique impetraverunt."')]),
 U('8:33', G('8:33'), 'And the daimons, going out from the person, went into the pigs, and the herd rushed down the cliff into the lake and was choked.',
   'Inside the attested pericope 8:26–39.'),
 U('8:34', G('8:34'), 'And those feeding them, seeing what had happened, fled and reported it in the city and in the fields.', 'Inside the attested pericope 8:26–39.'),
 U('8:35', G('8:35'), 'And they went out to see what had happened, and came to Jesus, and found the person from whom the daimons had gone out sitting, clothed and of sound mind, at the feet of Jesus; and they were afraid.', 'Inside the attested pericope 8:26–39.'),
 U('8:36', G('8:36'), 'And those who had seen it reported to them how the one who had been daimonised was saved.', 'Inside the attested pericope 8:26–39.'),
 U('8:37', G('8:37'), 'And the whole multitude of the surrounding region of the Gerasenes asked him to go away from them, because they were held by a great fear; and he got into a boat and returned.', 'Inside the attested pericope 8:26–39.'),
 U('8:38', G('8:38'), 'And the man from whom the daimons had gone out was begging him to be with him; but he released him, saying,', 'Inside the attested pericope 8:26–39.'),
 U('8:39', G('8:39'), '"Return to your house, and tell in full what God has done for you." And he went away through the whole city, proclaiming what Jesus had done for him.', 'Inside the attested pericope 8:26–39.'),
 U('8:40', G('8:40'), 'And as Jesus returned, the crowd received him, for they were all waiting for him.',
   'Opens the NA27 paragraph 8:40–56, whose central part (8:42b–48) is attested; Epiphanius\' "as they were going" presupposes the journey to Jairus\' house.'),
 U('8:41', G('8:41'), 'And look, a man came whose name was Jairus, and he was a ruler of the assembly; and falling at the feet of Jesus he was urging him to come into his house,', 'Inside the attested paragraph 8:40–56.'),
 A('8:42', G('8:42'), 'because he had an only-born daughter, about twelve years old, and she was dying. And as he went, the crowds were choking him.',
   'present for 8:42b (Pan. 42.11.6, sch. 14); 8:42a unattested',
   [E(14, '»ἐγένετο δὲ ἐν τῷ ὑπάγειν αὐτούς, συνέπνιγον αὐτὸν οἱ ὄχλοι«.')],
   wording='NA27. 8:42a (the daughter) is unattested; printed within the attested verse.'),
 A('8:43', G('8:43'), 'And a woman who had been in a flow of blood for twelve years, who had spent her whole living on physicians and could not be healed by anyone,',
   'present (Marc. 4.20.7–8; Pan. 42.11.6, sch. 14)',
   [E(14, '»καὶ γυνὴ ἁψαμένη αὐτοῦ ἰάθη τοῦ αἵματος«.'), T('4.20.7', '"Tangitur a femina quae sanguine fluitabat".')],
   wording='NA27, including its bracketed clause [ἰατροῖς προσαναλώσασα ὅλον τὸν βίον] (no witness lacks it).'),
 A('8:44', G('8:44'), 'coming up behind, touched the fringe of his garment, and at once the flow of her blood stood still.',
   'present (Marc. 4.20.8, 13; Pan. 42.11.6, sch. 14)', [T('4.20.13', '"dum tangitur vestimentum eius".')]),
 A('8:45', G('8:45', [('Τίς ὁ ἁψάμενός μου;', 'Τίς μου ἥψατο;')]),
   'And Jesus said, "Who touched me?" And when all were denying it, Peter said, "Overseer, the crowds are hemming you in and pressing against you."',
   'present (Marc. 4.20.8; Pan. 42.11.6, sch. 14)',
   [E(14, '»καὶ εἶπεν ὁ κύριος· τίς μου ἥψατο;«'), T('4.20.8', '"Quis me, inquit, tetigit? Etiam excusantibus discipulis…"')],
   wording='Marcionite reading adopted: τίς μου ἥψατο; for τίς ὁ ἁψάμενός μου; (Epiphanius\' Greek, with Tertullian "Quis me tetigit?"; Roth: secure). Epiphanius\' ὁ κύριος for ὁ Ἰησοῦς is rated possible; not adopted. Tertullian\'s "excusantibus discipulis" (the learners, not Peter alone) is rated possible; noted.'),
 A('8:46', G('8:46'), 'But Jesus said, "Someone touched me, for I knew power had gone out from me."',
   'present (Marc. 4.20.8; Pan. 42.11.6, sch. 14)',
   [E(14, '»ἥψατό μού τις. καὶ γὰρ ἔγνων δύναμιν ἐξελθοῦσαν ἀπ\' ἐμοῦ«.'), T('4.20.8', '"Tetigit me aliquis… Sensi enim virtutem ex me profectam."')],
   wording='NA27. Epiphanius\' καὶ γάρ and ἐξελθοῦσαν are rated possible and probable by Roth; not adopted.'),
 U('8:47', G('8:47'), 'And the woman, seeing that she had not escaped notice, came trembling, and falling down before him, she reported before all the people for what reason she had touched him and how she had been cured at once.',
   'Inside the attested paragraph 8:40–56.'),
 A('8:48', G('8:48'), 'And he said to her, "Daughter, your trust has saved you; journey into peace."',
   'present (Marc. 4.20.9)', [T('4.20.9', '"cum dicit, Fides tua te salvam fecit".')]),
 U('8:49', G('8:49'), 'While he was still speaking, someone comes from the ruler of the assembly, saying, "Your daughter has died; trouble the teacher no longer."', 'Inside the attested paragraph 8:40–56 (NA27 continues the paragraph at 8:49).'),
 U('8:50', G('8:50'), 'But Jesus, hearing it, answered him, "Do not be afraid; only trust, and she will be saved."', 'Inside the attested paragraph 8:40–56.'),
 U('8:51', G('8:51'), 'And coming into the house, he did not let anyone go in with him except Peter and John and Jacob, and the father of the child and the mother.', 'Inside the attested paragraph 8:40–56.'),
 U('8:52', G('8:52'), 'And all were weeping and beating their breasts for her. But he said, "Do not weep, for she did not die, but is sleeping."', 'Inside the attested paragraph 8:40–56.'),
 U('8:53', G('8:53'), 'And they were laughing him down, knowing that she had died.', 'Inside the attested paragraph 8:40–56.'),
 U('8:54', G('8:54'), 'But he, taking hold of her hand, called out, saying, "Child, get up!"', 'Inside the attested paragraph 8:40–56.'),
 U('8:55', G('8:55'), 'And her spirit returned, and she stood up at once, and he directed that something be given to her to eat.', 'Inside the attested paragraph 8:40–56.'),
 U('8:56', G('8:56'), 'And her parents were beside themselves; but he ordered them to tell no one what had happened.', 'Inside the attested paragraph 8:40–56.'),
 A('9:1', G('9:1'), 'And calling the twelve together, he gave them power and authority over all the daimons, and to heal diseases,',
   'present (Adam. 82,2–4)',
   [AD('82,2–4 (2.12)', 'The orthodox speaker Adamantius reads 9:1–2 "from the gospel" as an argument against the Marcionite Marcus, which presupposes that Marcus accepts the passage. A weaker attestation than a Marcionite speaker\'s.')]),
 A('9:2', G('9:2', [('καὶ ἰᾶσθαι τοὺς ἀσθενεῖς,', 'καὶ ἰᾶσθαι,')]), 'and he sent them out to proclaim the kingdom of God and to cure,',
   'present (Marc. 4.21.1; Adam. 82,4–5)', [T('4.21.1', '"Dimittit discipulos ad praedicandum dei regnum."'),
    AD('82,4–5 (2.12)', '»καὶ ἀπέστειλεν αὐτοὺς κηρύσσειν τὴν βασιλείαν τοῦ θεοῦ καὶ ἰᾶσθαι.«')],
   wording='NA27 without its bracketed [τοὺς ἀσθενεῖς] (METHOD §5: bracketed words are printed unless a witness lacks them; Adamantius\' reading of the verse ends at ἰᾶσθαι).'),
 A('9:3', G('9:3'), 'and he said to them, "Take nothing for the road, neither staff nor bag nor bread nor silver, nor are you to have two tunics each.',
   'present (Marc. 4.21.1)', [T('4.21.1', '"Prohibet eos victui aut vestitui quid in viam ferre."')]),
 U('9:4', G('9:4'), 'And whatever house you go into, stay there, and go out from there.', 'Inside the attested pericope 9:1–6.'),
 A('9:5', G('9:5'), 'And as many as do not receive you, when you go out from that city, shake off the dust from your feet as a testimony against them."',
   'present (Marc. 4.21.1)', [T('4.21.1', '"At cum iubet pulverem excutere de pedibus in eos a quibus excepti non fuissent, et hoc in testimonium mandat fieri."')]),
 A('9:6', G('9:6'), 'And going out, they were going through the villages, announcing the good news and healing everywhere.',
   'present (Adam. 82,6–7)', [AD('82,6–7 (2.12)', 'Read by Adamantius in the same argument as 9:1–2 (see 9:1): »ἐξερχόμενοι δὲ διήρχοντο κατὰ πόλεις καὶ κώμας…«.')],
   wording='NA27. Adamantius\' "through towns and villages" is rated possible by Roth; not adopted.'),
 A('9:7', G('9:7'), 'And Herod the tetrarch heard of all the things that were happening, and he was at a loss, because it was said by some that John had been raised from the dead,',
   'present (Marc. 4.21.2)', [T('4.21.2', '"Christum Iesum alii Ioannem, alii Heliam, alii unum aliquem ex veteribus prophetis Herodi adseverabant".')]),
 A('9:8', G('9:8'), 'and by some that Elijah had appeared, and by others that one of the prophets of old had stood up.',
   'present (Marc. 4.21.2)', [T('4.21.2', 'see 9:7.')]),
 U('9:9', G('9:9'), 'And Herod said, "John I beheaded; but who is this about whom I hear such things?" And he was seeking to see him.', 'Inside the attested pericope 9:7–9.'),
 U('9:10', G('9:10'), 'And returning, the emissaries described to him all that they had done. And taking them along, he withdrew privately to a city called Bethsaida.', 'Inside the attested pericope 9:10–17.'),
 U('9:11', G('9:11'), 'But the crowds, knowing it, followed him; and receiving them, he was speaking to them about the kingdom of God, and those who had need of healing he was curing.', 'Inside the attested pericope 9:10–17.'),
 A('9:12', G('9:12'), 'And the day began to decline; and coming up, the twelve said to him, "Release the crowd, so that going into the villages and fields around they may lodge and find provisions, because here we are in a desert place."',
   'present (Marc. 4.21.2–3)', [T('4.21.2', '"Pascit populum in solitudine".')]),
 A('9:13', G('9:13'), 'But he said to them, "You give them something to eat." But they said, "We have no more than five loaves and two fish, unless we are to go and buy food for all this people."',
   'present (Marc. 4.21.3)', [T('4.21.3', '"nec de inferioribus materiis panis et piscis".')]),
 A('9:14', G('9:14'), 'For there were about five thousand men. And he said to his learners, "Make them recline in table groups of about fifty each."',
   'present (Marc. 4.21.3)', [T('4.21.3', '"nec quinque circiter sed sexcenta milia hominum".')]),
 U('9:15', G('9:15'), 'And they did so, and made them all recline.', 'Inside the attested pericope 9:10–17.'),
 A('9:16', G('9:16', [('εὐλόγησεν αὐτοὺς', 'εὐλόγησεν ἐπ’ αὐτοὺς')]),
   'And taking the five loaves and the two fish, looking up to the sky, he blessed over them and broke them in pieces, and he was giving them to the learners to set before the crowd.',
   'present (Pan. 42.11.6, sch. 15; [Adam. 108,25])',
   [E(15, '»ἀναβλέψας εἰς τὸν οὐρανὸν εὐλόγησεν ἐπ\' αὐτούς«.')],
   wording='Marcionite reading adopted: εὐλόγησεν ἐπ\' αὐτούς (Epiphanius\' Greek; Roth: very likely). NA27 apparatus: ἐπ\' αὐτ. D it sy(s).c; McionE.',
   western='Agrees with D and the Old Latin and Old Syriac.'),
 A('9:17', G('9:17'), 'And they ate and were fed, all of them; and what was left over to them was taken up: twelve baskets of broken pieces.',
   'present (Marc. 4.21.4)', [T('4.21.4', '"ut et pabuli exiguitatem non tantum sufficere, verum etiam exuberare… voluerit".')]),
]

OMITTED = []

PREAMBLE = (
 "On the far side of ourselves something lives among the tombs and has worn nothing for years. Ask its name and "
 "it answers with a crowd. It begs not to be sent into the deep, and is allowed to go elsewhere.\n\n"
 "Closer to home, something young is dying just as it should be coming into its fullness, and something else has"
 " been bleeding away for just as long, spending all it has on cures from outside. In the crush it touches only "
 "the very hem, and that is enough. Power goes out, and truth feels it go.\n\n"
 "What we send out after that carries nothing in its hands. What rules us at the edges hears of it and cannot "
 "make sense of what it hears.\n\n"
 "And as the light declines, somewhere bare, we look at what we have to give, and it does not look like enough. "
 "There is more left over than we began with."
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
  "out, and the woman's trust. The legal questions belong to the readers.")),
 dict(term='Jairus\' daughter (8:40–42a, 8:49–56)', cat='textual', refs=['8:40', '8:41', '8:49', '8:56'], text=(
  "No witness cites the request of Jairus or the raising of his daughter. Epiphanius' quotation begins \"as they were going\", "
  "which presupposes the journey to Jairus' house, and NA27 prints 8:40–56 as one paragraph. The frame is therefore printed in "
  "grey, as part of an attested passage. Tertullian had already used the raising of the widow's son (7:11–17) to argue that "
  "raising the dead was the Creator's sign (4.18.2), so a second raising would add nothing to his case. That is why his "
  "silence here is not counted as evidence of absence.")),
 dict(term='The mission of the twelve (9:1–6)', cat='textual', refs=['9:1', '9:2', '9:3', '9:5', '9:6'], text=(
  "Tertullian, Marc. 4.21.1: the learners are sent to preach the kingdom of God, are forbidden to take food or clothing for "
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
 dict(term='ἀνήρ, "man"', cat='translation', refs=['8:27'], text='ἀνήρ, a male. In 8:29, 8:33 and 8:35 the text calls him ἄνθρωπος, "the person".'),
 dict(term='ἐν τοῖς μνήμασιν, "among the tombs"', cat='translation', refs=['8:27'], text='μνῆμα, a memorial, a tomb.'),
 dict(term='Τί ἐμοὶ καὶ σοί, "what is there between me and you"', cat='translation', refs=['8:28'], text='The idiom of 4:34, here in the singular.'),
 dict(term='υἱὲ τοῦ θεοῦ τοῦ ὑψίστου, "son of the Highest God"', cat='translation', refs=['8:28'], text='Lower case for "son", as at 4:41. "The Highest" as at 6:35.'),
 dict(term='βασανίσῃς, "torture"', cat='translation', refs=['8:28'], text='βασανίζω, to examine by torture, torment.'),
 dict(term='παρήγγελλεν, "was ordering"', cat='translation', refs=['8:29'], text='The imperfect: he had been ordering it, or he was in the course of ordering it.'),
 dict(term='συνηρπάκει, "had seized"', cat='translation', refs=['8:29'], text='To seize and carry off.'),
 dict(term='Λεγιών, "Legion"', cat='translation', refs=['8:30'], text='The Latin word for a Roman army unit of several thousand soldiers, taken into Greek.'),
 dict(term='τὴν ἄβυσσον, "the abyss"', cat='translation', refs=['8:31'], text='"The bottomless", the deep below the earth.'),
 dict(term='χοίρων, "pigs"', cat='translation', refs=['8:32'], text='Unclean animals under the law.'),
 dict(term='ἐν τῷ ὄρει, "on the mountain"', cat='translation', refs=['8:32'], text='ὄρος, as at 4:29 and 6:12.'),
 dict(term='ἐπιτρέψῃ, "allow"', cat='translation', refs=['8:32'], text='To give leave, permit.'),
 dict(term='ἀπεπνίγη, "was choked"', cat='translation', refs=['8:33'], text='The verb of the thorns that choked the seed (8:7). It means drowned here.'),
 dict(term='ἱματισμένον, "clothed"', cat='translation', refs=['8:35'], text='Answers 8:27, "had not put on a garment".'),
 dict(term='σωφρονοῦντα, "of sound mind"', cat='translation', refs=['8:35'], text='Sensible, in control of himself.'),
 dict(term='ὁ δαιμονισθείς, "the one who had been daimonised"', cat='translation', refs=['8:36'], text='One acted on by daimons. "Possessed" is an interpretation of what that means.'),
 dict(term='ἐσώθη, "was saved"', cat='translation', refs=['8:36'], text='σῴζω: here, made well.'),
 dict(term='συνείχοντο, "were held"', cat='translation', refs=['8:37'], text='Gripped, held fast.'),
 dict(term='ἀπέλυσεν, "released"', cat='translation', refs=['8:38'], text='ἀπολύω, to release, send away, dismiss.'),
 dict(term='διηγοῦ, "tell in full"', cat='translation', refs=['8:39'], text='To tell through, recount in detail.'),
 dict(term='"what God has done… what Jesus had done"', cat='translation', refs=['8:39'], text='The Greek has God in the command and Jesus in what the man proclaims. The English keeps both.'),
 dict(term='ἀπεδέξατο, "received"', cat='translation', refs=['8:40'], text='To welcome, receive gladly.'),
 dict(term='ἄρχων τῆς συναγωγῆς, "a ruler of the assembly"', cat='translation', refs=['8:41'], text='The leader of the local assembly. In 8:49 one word, ἀρχισυνάγωγος, says the same.'),
 dict(term='μονογενής, "only-born"', cat='translation', refs=['8:42'], text='As at 7:12.'),
 dict(term='συνέπνιγον, "were choking"', cat='translation', refs=['8:42'], text='The verb of 8:7, choking: the crowd crushing him.'),
 dict(term='ἐν ῥύσει αἵματος, "in a flow of blood"', cat='translation', refs=['8:43'], text='A continuous flow of blood, which made her unclean under the law.'),
 dict(term='βίον, "living"', cat='translation', refs=['8:43'], text='βίος is livelihood, the means one lives on.'),
 dict(term='κρασπέδου, "fringe"', cat='translation', refs=['8:44'], text='The edge or tassel of a garment, as the law required (Num 15:38).'),
 dict(term='ἔστη, "stood still"', cat='translation', refs=['8:44'], text='The ordinary verb "stood", used of the flow stopping.'),
 dict(term='Ἐπιστάτα, "overseer"', cat='translation', refs=['8:45'], text='As at 5:5.'),
 dict(term='δύναμιν ἐξεληλυθυῖαν, "power had gone out"', cat='translation', refs=['8:46'], text='As at 6:19.'),
 dict(term='οὐκ ἔλαθεν, "had not escaped notice"', cat='translation', refs=['8:47'], text='λανθάνω, to be hidden, unnoticed.'),
 dict(term='ἰάθη, "had been cured"', cat='translation', refs=['8:47'], text='ἰάομαι, cure.'),
 dict(term='Θυγάτηρ, "Daughter"', cat='translation', refs=['8:48'], text='The address is "daughter", as the Greek has it.'),
 dict(term='ἔρχεται, "comes"', cat='translation', refs=['8:49'], text='The present tense in the middle of past narration, kept.'),
 dict(term='πίστευσον, "trust"', cat='translation', refs=['8:50'], text='πιστεύω, here without an object: trust.'),
 dict(term='τῆς παιδός, "of the child"', cat='translation', refs=['8:51'], text='παῖς, here feminine: the girl.'),
 dict(term='ἐκόπτοντο, "beating their breasts"', cat='translation', refs=['8:52'], text='κόπτομαι, to strike oneself in mourning, lament.'),
 dict(term='κατεγέλων, "were laughing him down"', cat='translation', refs=['8:53'], text='To laugh at, deride.'),
 dict(term='Ἡ παῖς, ἔγειρε, "child, get up"', cat='translation', refs=['8:54'], text='ἐγείρω, as at 7:14.'),
 dict(term='ἐπέστρεψεν τὸ πνεῦμα αὐτῆς, "her spirit returned"', cat='translation', refs=['8:55'], text='πνεῦμα, spirit, also breath.'),
 dict(term='ἀνέστη, "stood up"', cat='translation', refs=['8:55'], text='ἀνίστημι.'),
 dict(term='ἐξέστησαν, "were beside themselves"', cat='translation', refs=['8:56'], text='From the same root as ἔκστασις (5:26), standing out of oneself.'),
 dict(term='δύναμιν καὶ ἐξουσίαν, "power and authority"', cat='translation', refs=['9:1'], text='δύναμις, the ability to act; ἐξουσία, the right to act.'),
 dict(term='θεραπεύειν… ἰᾶσθαι, "heal… cure"', cat='translation', refs=['9:1', '9:2'], text='Both verbs, kept apart.'),
 dict(term='ἀργύριον, "silver"', cat='translation', refs=['9:3'], text='Silver, money.'),
 dict(term='ἀνὰ δύο χιτῶνας, "two tunics each"', cat='translation', refs=['9:3'], text='The tunic worn next to the skin, as at 6:29.'),
 dict(term='εἰς μαρτύριον ἐπ\' αὐτούς, "as a testimony against them"', cat='translation', refs=['9:5'], text='ἐπί with the accusative, "upon, against".'),
 dict(term='διηπόρει, "was at a loss"', cat='translation', refs=['9:7'], text='To be perplexed, not to know which way to go.'),
 dict(term='ἠγέρθη ἐκ νεκρῶν, "had been raised from the dead"', cat='translation', refs=['9:7'], text='ἐγείρω, passive.'),
 dict(term='ἀνέστη, "had stood up"', cat='translation', refs=['9:8'], text='ἀνίστημι. A different verb from "raised" (9:7) in the same sentence. Both are kept.'),
 dict(term='ἀπόστολοι, "emissaries"', cat='translation', refs=['9:10'], text='As at 6:13.'),
 dict(term='διηγήσαντο, "described"', cat='translation', refs=['9:10'], text='To tell in full, as at 8:39.'),
 dict(term='ἀποδεξάμενος, "receiving"', cat='translation', refs=['9:11'], text='As at 8:40.'),
 dict(term='Ἀπόλυσον, "release"', cat='translation', refs=['9:12'], text='ἀπολύω, to send away, dismiss, release.'),
 dict(term='καταλύσωσιν, "lodge"', cat='translation', refs=['9:12'], text='To unharness and put up for the night.'),
 dict(term='ἄνδρες, "men"', cat='translation', refs=['9:14'], text='ἀνήρ: males.'),
 dict(term='Κατακλίνατε… κλισίας, "make them recline in table groups"', cat='translation', refs=['9:14'], text='κλισία, a company reclining together at a meal.'),
 dict(term='ἀναβλέψας εἰς τὸν οὐρανόν, "looking up to the sky"', cat='translation', refs=['9:16'], text='οὐρανός, "sky" and "heaven".'),
 dict(term='εὐλόγησεν ἐπ\' αὐτούς, "he blessed over them"', cat='translation', refs=['9:16'], text='The reading of this text, "upon them". Canonical Luke has "blessed them".'),
 dict(term='ἐδίδου, "he was giving"', cat='translation', refs=['9:16'], text='The imperfect: he kept giving.'),
 dict(term='ἐχορτάσθησαν, "were fed"', cat='translation', refs=['9:17'], text='χορτάζω, fed full, as at 6:21.'),
 dict(term='κόφινοι, "baskets"', cat='translation', refs=['9:17'], text='Large wicker baskets.'),
]
