"""Batch 4, chapter 15 of the reconstruction: Luke 17:1–37, with 4:27 inside 17:12–14."""
from buildlib import greek
from batch1_ch2 import U, A
from batch4_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}

E48 = E(48, 'ὅτε συνήντησαν οἱ δέκα λεπροί. ἀπέκοψε δὲ πολλὰ καὶ ἐποίησεν »ἀπέστειλεν αὐτοὺς λέγων, δείξατε ἑαυτοὺς τοῖς ἱερεῦσι« καὶ ἄλλα ἀντὶ ἄλλων ἐποίησε, λέγων ὅτι »πολλοὶ λεπροὶ ἦσαν ἐν ἡμέραις Ἐλισσαίου τοῦ προφήτου καὶ οὐκ ἐκαθαρίσθη εἰ μὴ Νεεμὰν ὁ Σύρος«.')

ENTRIES = [
 A('17:1', G('17:1'), 'And he said to his learners, "It is impossible for the trip-traps not to come, but woe to the one through whom they come.',
   'present (Marc. 4.35.1; Adam. 88,4–5)', [T('4.35.1', '"Conversus ibidem ad discipulos Vae dicit auctori scandalorum…"')]),
 A('17:2', G('17:2'), 'It would be better for him if a millstone were hung around his neck and he were thrown into the sea, than that he should trip up one of these little ones.',
   'present (Marc. 4.35.1)', [T('4.35.1', '"expedisse ei si natus non fuisset, aut si molino saxo ad collum deligato praecipitatus esset in profundum, quam unum ex illis modicis utique discipulis eius scandalizasset".')],
   wording='NA27. Tertullian\'s "if he had not been born" (cf. Mark 14:21) is rated possible only by Roth; not adopted.'),
 A('17:3', G('17:3'), 'Watch yourselves. If your brother sins, rebuke him, and if he changes his mind, let it go for him.',
   'present (Marc. 4.35.2)', [T('4.35.2', '"Peccantem fratrem iubet corripi".')]),
 A('17:4', G('17:4'), 'And if seven times a day he sins against you and seven times turns back to you, saying, \'I change my mind,\' you shall let it go for him."',
   'present (Marc. 4.35.3)', [T('4.35.3', '"Sed et veniam des fratri in te delinquenti iubet, etiam septies."')]),
 A('17:11', G('17:11'), 'And it happened, while journeying to Jerusalem, that he was passing through the middle of Samaria and Galilee.',
   'present (Marc. 4.35.9)', [T('4.35.9', '"In Samariae regionibus res agebatur, unde erat et unus interim ex leprosis."')]),
 A('17:12', G('17:12', [('δέκα λεπροὶ ἄνδρες, οἳ ἔστησαν πόρρωθεν,', 'δέκα λεπροὶ ἄνδρες.')]),
   'And as he was going into a certain village, ten leprous men met him.',
   'present for 17:12a (Marc. 4.35.4, 6; Pan. 42.11.6, sch. 48); 17:12b absent',
   [E48, T('4.35.4', '"in curatione decem leprosorum".')],
   wording=('NA27, including its bracketed [αὐτῷ] (SBLGNT omits it — checked on the page image), without the clause "who stood at a distance" (οἳ ἔστησαν πόρρωθεν). '
            'Epiphanius says that after "when the ten lepers met him" Marcion "cut out much" and put "other things in place of others", quoting 4:27. Roth takes the omitted "much" to be 17:12b–13, the lepers standing at a distance and crying "Jesus, master, have mercy on us", and 4:27 as what stood in its place. Tertullian\'s account of the healing has neither.')),
 A('4:27', greek('4:27', text='πολλοὶ λεπροὶ ἦσαν ἐν τῷ Ἰσραὴλ ἐν ἡμέραις Ἐλισαίου τοῦ προφήτου, καὶ οὐδεὶς αὐτῶν ἐκαθαρίσθη εἰ μὴ Νεεμὰν ὁ Σύρος.'),
   '"And many leprous were in Israel in the days of Elisha the prophet, and none of them was cleansed except Neeman the Syrian."',
   'present, in this position (Marc. 4.35.6; Pan. 42.11.6, sch. 48)',
   [E48, T('4.35.6', '"Nunc etsi praefatus est multos tunc fuisse leprosos apud Israelem in diebus Helisaei prophetae et neminem eorum purgatum nisi Naaman Syrum…"')],
   wording=('Printed here, between 17:12 and 17:14, as both witnesses place it: Epiphanius within the account of the ten lepers, Tertullian as said "beforehand" (praefatus est) in the same episode (Roth, Harnack). The verse is not printed at Luke 4 (batch 1). '
            'Marcionite readings adopted: ἐν ἡμέραις ("in the days of"; Tertullian "in diebus", Epiphanius) for NA27 ἐπί, and the spelling Νεεμάν (Epiphanius). Roth: secure for both. The opening καί of Luke 4:27 belongs to its canonical context and is not printed. No witness gives the words that introduced the saying here.')),
 A('17:14', G('17:14'), 'And seeing them, he said to them, "Journey and show yourselves to the priests." And it happened, as they were going away, that they were cleansed.',
   'present (Marc. 4.35.4, 7, 8, 10; Pan. 42.11.6, sch. 48)',
   [E48, T('4.35.7', '"Sed et quod in manifesto fuit legis praecepit, Ite, ostendite vos sacerdotibus."'),
    T('4.35.4', '"quos tantummodo ire iussos ut se ostenderent sacerdotibus, in itinere purgavit, sine tactu iam et sine verbo".')],
   wording='NA27. Epiphanius\' "he sent them away saying" is probably his own introduction (Roth). His δείξατε for ἐπιδείξατε is rated possible only.'),
 A('17:15', G('17:15'), 'And one of them, seeing that he was cured, turned back, with a loud voice giving glory to God,',
   'present (Marc. 4.35.11)', [T('4.35.11', '"unum illum solutum ex decem memorem divinae gratiae".')]),
 A('17:16', G('17:16'), 'and he fell on his face at his feet, giving him thanks; and he was a Samaritan.',
   'present (Marc. 4.35.9, 11)', [T('4.35.11', '"Samariten miratus".'), T('4.35.9', '"unde erat et unus interim ex leprosis".')]),
 A('17:17', G('17:17'), 'And Jesus answered and said, "Were not the ten cleansed? But the nine, where are they?',
   'present (Marc. 4.35.11)', [T('4.35.11', 'The question about the others is presupposed by "unum illum… ex decem".')], wording='NA27. Roth: attested, but no insight into the wording.'),
 A('17:18', G('17:18'), 'Were none found turning back to give glory to God except this foreigner?"',
   'present (Marc. 4.35.11)', [T('4.35.11', '"quia satis iam obtulerat gloriam deo reddens".')]),
 A('17:19', G('17:19'), 'And he said to him, "Stand up and journey; your trust has saved you."',
   'present (Marc. 4.35.11)', [T('4.35.11', '"Et ideo, Fides tua te salvum fecit, audiit".')]),
 A('17:20', G('17:20'), 'And being asked by the Pharisees when the kingdom of God is coming, he answered them and said, "The kingdom of God does not come with close watching,',
   'present (Marc. 4.35.12)', [T('4.35.12', '"Sed nec pharisaei possunt videri de alterius dei regno consuluisse dominum quando venturum sit… Non venit, inquit, regnum dei cum observatione".')]),
 A('17:21', G('17:21', [('Ἰδοὺ ὧδε ἤ· Ἐκεῖ·', 'Ἰδοὺ ὧδε ἤ· Ἰδοὺ ἐκεῖ·')]),
   'nor will they say, \'Look, here,\' or, \'Look, there\'; for look, the kingdom of God is inside you."',
   'present (Marc. 4.35.12–13)', [T('4.35.12', '"nec dicunt, Ecce hic, ecce illic: ecce enim regnum dei intra vos est."')],
   wording='Marcionite reading adopted: the second "Look" (ἰδού) before "there" (Tertullian\'s "ecce… ecce"; Roth: very likely). The Greek printed is that of A D W Θ Ψ and the Byzantine text (NA27 apparatus: ἢ ἰδοὺ ἐκεῖ); NA27 prints "Look, here!" or "There!".'),
 A('17:22', G('17:22'), 'And he said to the learners, "Days will come when you will long to see one of the days of the son of the human, and you will not see it.',
   'present (Pan. 42.11.6, sch. 49)', [E(49, '»ἐλεύσονται ἡμέραι, ὅταν ἐπιθυμήσητε ἰδεῖν μίαν τῶν ἡμερῶν τοῦ υἱοῦ τοῦ ἀνθρώπου«.')],
   wording='NA27. Epiphanius has ὅταν and the verb ἰδεῖν before "one of the days"; Roth: order uncertain.'),
 U('17:23', G('17:23'), "And they will say to you, 'Look, there,' or, 'Look, here'; do not go away, nor pursue them.", 'Inside the attested paragraph 17:22–37. NA27 prints [ἤ] (SBLGNT omits it).'),
 U('17:24', G('17:24'), 'For as the lightning, flashing out of the one part under the sky, shines to the other part under the sky, so will the son of the human be in his day.', 'Inside the attested paragraph 17:22–37.'),
 A('17:25', G('17:25'), 'But first he must suffer many things and be rejected by this generation.',
   'present (Marc. 4.35.14)', [T('4.35.14', '"Dicens enim filium hominis ante multa pati et reprobari oportere, ante adventum suum…"')]),
 A('17:26', G('17:26'), 'And just as it happened in the days of Noah, so it will be also in the days of the son of the human:',
   'present (Marc. 4.35.15)', [T('4.35.15', '"cur eum diebus Noe et Loth comparat tetris et atrocibus, deus et lenis et mitis?"')]),
 U('17:27', G('17:27'), 'they were eating, drinking, marrying, being given in marriage, until the day Noah went into the ark, and the flood came and destroyed them all.', 'Inside the attested paragraph 17:22–37.'),
 A('17:28', G('17:28'), 'Likewise, just as it happened in the days of Lot: they were eating, drinking, buying, selling, planting, building;',
   'present (Marc. 4.35.15)', [T('4.35.15', '"diebus Noe et Loth".')]),
 U('17:29', G('17:29'), 'but on the day Lot went out from Sodom, it rained fire and sulphur from the sky and destroyed them all.', 'Inside the attested paragraph 17:22–37.'),
 U('17:30', G('17:30'), 'It will be the same on the day the son of the human is uncovered.', 'Inside the attested paragraph 17:22–37.'),
 U('17:31', G('17:31'), 'On that day, whoever is on the roof, and his things in the house, let him not go down to take them away; and likewise the one in the field, let him not turn back to the things behind.', 'Inside the attested paragraph 17:22–37.'),
 A('17:32', G('17:32'), 'Remember the wife of Lot.',
   'present (Marc. 4.35.15)', [T('4.35.15', '"Cur admonet meminisse uxoris Loth, quae praeceptum creatoris non impune contempsit…?"')]),
 U('17:33', G('17:33'), 'Whoever seeks to keep his soul safe will destroy it, but whoever destroys it will keep it alive.', 'Inside the attested paragraph 17:22–37.'),
 U('17:34', G('17:34'), 'I tell you, on this night there will be two on one bed; the one will be taken along, and the other will be let go.', 'Inside the attested paragraph 17:22–37.'),
 U('17:35', G('17:35'), 'There will be two women grinding at the same place; the one will be taken along, but the other will be let go."', 'Inside the attested paragraph 17:22–37.'),
 U('17:37', G('17:37'), 'And answering, they say to him, "Where, lord?" And he said to them, "Where the body is, there the eagles too will be gathered together."', 'Inside the attested paragraph 17:22–37.'),
]

OMITTED = [
 dict(ref='17:5–10', cls='U?', app=dict(roth='unattested (17:5–10a); absent (17:10b)', witnesses=[
      E(47, 'παρέκοψε τὸ »λέγετε ὅτι ἀχρεῖοι δοῦλοί ἐσμεν· ὃ ὠφείλομεν ποιῆσαι πεποιήκαμεν«.')],
      decision='not printed',
      reason=('Trust like a mustard seed (17:5–6) and the slave who does what he is told (17:7–10): two NA27 paragraphs with no attested present verse (METHOD §4.3). '
              'Epiphanius states that the text lacked 17:10b ("say, we are unworthy slaves; we have done what we ought to have done"), which is A− (NA27: □ McionE). Tertullian passes from 17:4 (4.35.3) to 17:14 (4.35.4).'))),
 dict(ref='17:13', cls='A−', app=dict(roth='absent', witnesses=[E48], decision='not printed',
      reason='"And they raised their voices, saying, Jesus, master, have mercy on us." Part of what Epiphanius says Marcion "cut out" between the meeting with the ten lepers and the command to the priests; Roth: not present (with 17:12b). Tertullian stresses that they were healed "without touch and without a word" from Jesus, and does not mention their plea.')),
]

PREAMBLE = (
 "Ten parts of us are unclean, and all ten are sent to show themselves, and on the way all ten are made clean. "
 "Only one turns back to give thanks, and it is the one we would least expect: the stranger, the one from the "
 "border country. Where are the nine?\n\n"
 "Then the question comes, as it always does: when will the kingdom come? Where should we be looking? Not here, "
 "not there. Not by watching closely. It is already inside.\n\n"
 "And yet there will be days of longing, days when it cannot be seen. Life will go on as it always has. We will "
 "eat and drink, buy and sell, plant and build, and none of it will be wrong, and none of it will be what "
 "matters when that day comes.\n\n"
 "Remember the woman who looked back."
)

NOTES = [
 dict(term='Stumbling and letting go (17:1–4)', cat='textual', refs=['17:1', '17:2', '17:3', '17:4'], text=(
  "Tertullian, Marc. 4.35.1–3. He takes the woe on the one who causes stumbling as a judge's threat, and compares the command "
  "to rebuke a sinning brother with Lev 19:17. He says the letting go \"seven times\" is \"too little\" compared with the "
  "Creator, who sets no limit. NA27 begins a new paragraph at 17:3b.")),
 dict(term='Not printed: 17:5–10', cat='excision', refs=['17:4', '17:11'], text=(
  "Epiphanius, sch. 47: the text lacked \"say, we are unworthy slaves; we have done what we ought to have done\" (17:10b). "
  "NA27 cites Marcion for the omission. The rest of 17:5–10, trust like a mustard seed and the slave who serves at table "
  "before he eats, is not cited by either witness. Its two paragraphs have no attested verse, and they are not printed.")),
 dict(term='The ten lepers and Naaman (17:11–19; 4:27)', cat='textual', refs=['17:11', '17:12', '4:27', '17:14', '17:16', '17:18', '17:19'], text=(
  "Epiphanius, sch. 48: \"when the ten lepers met him\"; Marcion \"cut out much\", had \"he sent them away saying, Show "
  "yourselves to the priests\", and put in \"other things in place of others\", saying \"there were many lepers in the days of "
  "Elisha the prophet and none was cleansed except Naaman the Syrian\". Tertullian, Marc. 4.35.4–11 says Christ had said this "
  "\"beforehand\" (praefatus est) and goes through the healing: sent to the priests, cleansed on the way \"without touch and "
  "without a word\", one of them a Samaritan who gave glory to God. Luke 4:27 is therefore printed here, after the meeting "
  "and before the command, and the lepers' cry for mercy (17:12b–13) is not printed. In canonical Luke 4:27 belongs to the "
  "Nazareth sermon (4:25–27), whose sayings on Elijah and Elisha this text does not have at that point (batch 1).")),
 dict(term='Priests and Samaritans', cat='theological', refs=['17:14', '17:16', '17:18'], text=(
  "Reception and interpretation. Marcion, Tertullian says, presented the healing on the way as Christ outrunning the "
  "ceremonies of the law (4.35.4). Tertullian replies that the ten were healed because they obeyed the law and went to the "
  "priests (4.35.8), and that the Samaritan was sent to Jerusalem because \"salvation is from the Jews\" (4.35.10). The "
  "attested text has Jesus send all ten to the priests, as the law of Leviticus 14 requires, and praise the Samaritan's return "
  "to give glory to God. Naaman, cleansed by Elisha, is the precedent the text itself cites. It sets the healing within "
  "Israel's prophetic history and not against it.")),
 dict(term='"Inside you" (17:20–21)', cat='textual', refs=['17:20', '17:21'], text=(
  "Tertullian, Marc. 4.35.12–13 quotes \"The kingdom of God does not come with observation, nor do they say, Look here, look "
  "there; for behold, the kingdom of God is within you\" (intra vos, \"inside you\"). He explains \"within you\" as \"in your hand, in your power, if you "
  "hear and do the commandment of God\", and compares Deut 30:11–14 (\"the word is near you, in your mouth and in your heart, "
  "to do it\"). The second \"Look\" (ἰδού) is printed with Tertullian and the Byzantine text.")),
 dict(term='The days of the son of the human (17:22–37)', cat='textual', refs=['17:22', '17:25', '17:26', '17:28', '17:32'], text=(
  "Epiphanius, sch. 49 quotes 17:22. Tertullian, Marc. 4.35.14–16 cites the son of the human who \"must first suffer many things and "
  "be rejected\" (17:25), drawing the word \"rejected\" from Ps 118:22 (\"the stone the builders rejected\"). He asks why a "
  "gentle God would compare his coming to the dark days of Noah and Lot and warn his hearers to remember Lot's wife. The other "
  "verses of the paragraph are not cited and are printed in grey. NA27 has no verse 17:36.")),
 dict(term='Ἀνένδεκτόν ἐστιν, "it is impossible"', cat='translation', refs=['17:1'], text='Literally "it is not admissible", it cannot be.'),
 dict(term='τὰ σκάνδαλα, "the trip-traps"', cat='translation', refs=['17:1'], text='σκάνδαλον, the trigger-stick of a trap, a stumbling block, as at 7:23.'),
 dict(term='λυσιτελεῖ, "it would be better"', cat='translation', refs=['17:2'], text='It pays, it is of more profit.'),
 dict(term='λίθος μυλικός, "a millstone"', cat='translation', refs=['17:2'], text='A stone of a mill.'),
 dict(term='σκανδαλίσῃ, "trip up"', cat='translation', refs=['17:2'], text='As at 7:23.'),
 dict(term='Προσέχετε ἑαυτοῖς, "watch yourselves"', cat='translation', refs=['17:3'], text='As at 12:1.'),
 dict(term='ἐπιτίμησον, "rebuke"', cat='translation', refs=['17:3'], text='ἐπιτιμάω, as at 4:35.'),
 dict(term='μετανοήσῃ… ἄφες αὐτῷ, "changes his mind… let it go for him"', cat='translation', refs=['17:3'], text='μετανοέω, as at 15:7; ἀφίημι, as at 5:20.'),
 dict(term='ἐπιστρέψῃ, "turns back"', cat='translation', refs=['17:4'], text='To turn around, return.'),
 dict(term='Μετανοῶ, "I change my mind"', cat='translation', refs=['17:4'], text='The same verb in the first person.'),
 dict(term='διὰ μέσον Σαμαρείας καὶ Γαλιλαίας, "through the middle of Samaria and Galilee"', cat='translation', refs=['17:11'], text='The Greek says "through the middle". It may mean "between" the two regions.'),
 dict(term='δέκα λεπροὶ ἄνδρες, "ten leprous men"', cat='translation', refs=['17:12'], text='This text lacks "who stood at a distance".'),
 dict(term='Νεεμὰν ὁ Σύρος, "Neeman the Syrian"', cat='translation', refs=['4:27'], text='The spelling of this text, Νεεμάν. Canonical Luke has Ναιμάν (Naaman). This verse stands here in this text, inside the healing of the ten, where both witnesses place it.'),
 dict(term='ἐν ἡμέραις Ἐλισαίου, "in the days of Elisha"', cat='translation', refs=['4:27'], text='The reading of this text, ἐν ἡμέραις. Canonical Luke has ἐπί, "in the time of".'),
 dict(term='ἐκαθαρίσθη, "was cleansed"', cat='translation', refs=['4:27'], text='καθαρίζω, to make clean, as at 5:12–13.'),
 dict(term='ἐπιδείξατε ἑαυτούς, "show yourselves"', cat='translation', refs=['17:14'], text='As in the law for one cleansed of leprosy (Lev 14).'),
 dict(term='ἰάθη, "he was cured"', cat='translation', refs=['17:15'], text='ἰάομαι.'),
 dict(term='ὑπέστρεψεν, "turned back"', cat='translation', refs=['17:15'], text='To return.'),
 dict(term='εὐχαριστῶν, "giving thanks"', cat='translation', refs=['17:16'], text='εὐχαριστέω, as at 10:21.'),
 dict(term='ὁ ἀλλογενής, "this foreigner"', cat='translation', refs=['17:18'], text='One of another race, not of Israel.'),
 dict(term='Ἀναστὰς πορεύου, "stand up and journey"', cat='translation', refs=['17:19'], text='ἀνίστημι and the road verb πορεύομαι.'),
 dict(term='ἡ πίστις σου σέσωκέν σε, "your trust has saved you"', cat='translation', refs=['17:19'], text='As at 7:50.'),
 dict(term='μετὰ παρατηρήσεως, "with close watching"', cat='translation', refs=['17:20'], text='παρατήρησις, close observation. The verb is the one used at 6:7 for the scribes watching him closely.'),
 dict(term='Ἰδοὺ ὧδε ἤ· Ἰδοὺ ἐκεῖ, "\'Look, here,\' or, \'Look, there\'"', cat='translation', refs=['17:21'], text='The reading of this text, with ἤ, "or".'),
 dict(term='ἐντὸς ὑμῶν, "inside you"', cat='translation', refs=['17:21'], text='ἐντός means "within, inside". "Among you" or "in your midst" is a widely held reading, but the Greek would more naturally say that with ἐν μέσῳ. Elsewhere in the New Testament ἐντός means "the inside" (Matt 23:26). The plain sense is kept: "inside you".'),
 dict(term='ἐπιθυμήσετε, "you will long"', cat='translation', refs=['17:22'], text='To desire, long for.'),
 dict(term='διώξητε, "pursue"', cat='translation', refs=['17:23'], text='To run after, chase.'),
 dict(term='ἐκ τῆς ὑπὸ τὸν οὐρανὸν εἰς τὴν ὑπ\' οὐρανόν, "out of the one part under the sky… to the other part under the sky"', cat='translation', refs=['17:24'], text='The Greek says "from the [region] under the sky to the [region] under the sky": from one horizon to the other.'),
 dict(term='δεῖ, "must"', cat='translation', refs=['17:25'], text='As at 9:22.'),
 dict(term='ἐγάμουν, ἐγαμίζοντο, "marrying, being given in marriage"', cat='translation', refs=['17:27'], text='The men married; the women were given in marriage.'),
 dict(term='κιβωτόν, "the ark"', cat='translation', refs=['17:27'], text='κιβωτός, a box, a chest: the ark.'),
 dict(term='ἀπώλεσεν, "destroyed"', cat='translation', refs=['17:27'], text='ἀπόλλυμι.'),
 dict(term='θεῖον, "sulphur"', cat='translation', refs=['17:29'], text='Brimstone.'),
 dict(term='ἀποκαλύπτεται, "is uncovered"', cat='translation', refs=['17:30'], text='As at 12:2: uncovered, revealed.'),
 dict(term='τὰ σκεύη αὐτοῦ, "his things"', cat='translation', refs=['17:31'], text="σκεῦος, a vessel, a utensil, one's goods."),
 dict(term='περιποιήσασθαι, "keep… safe"', cat='translation', refs=['17:33'], text='To preserve for oneself, keep.'),
 dict(term='ζῳογονήσει, "will keep alive"', cat='translation', refs=['17:33'], text='To give life to, keep alive.'),
 dict(term='παραλημφθήσεται… ἀφεθήσεται, "will be taken along… will be let go"', cat='translation', refs=['17:34'], text='παραλαμβάνω, to take along with oneself (as at 9:28). ἀφίημι, to let go, leave: the verb used for sins let go (5:20). Which of the two is the better lot, the Greek does not say.'),
 dict(term='ἀλήθουσαι, "grinding"', cat='translation', refs=['17:35'], text='Feminine: two women at the hand-mill.'),
 dict(term='λέγουσιν, "they say"', cat='translation', refs=['17:37'], text='The present tense, kept.'),
 dict(term='κύριε, "lord"', cat='translation', refs=['17:37'], text='As at 5:8.'),
 dict(term='οἱ ἀετοί, "the eagles"', cat='translation', refs=['17:37'], text='ἀετός is an eagle. It is also used of the vultures that gather at a carcass.'),
]
