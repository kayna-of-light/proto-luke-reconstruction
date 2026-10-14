"""Batch 5, chapter 16 of the reconstruction: Luke 18:1–43."""
from buildlib import greek
from batch1_ch2 import U, A
from batch5_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}
AD = lambda loc, ev: {'source': f'Dialogue of Adamantius {loc} (via Roth)', 'evidence': ev}

T361 = T('4.36.1', '"Nam et orandi perseverantiam et instantiam mandans parabolam iudicis ponit coacti audire viduam instantia et perseverantia interpellationum eius… Sed subiunxit facturum deum vindictam electorum suorum."')
T3612 = T('4.36.1–2', '"et duos adorantes diversa mente describit, pharisaeum in superbia, publicanum in humilitate, ideoque alterum reprobatum, alterum iustificatum descendisse".')
AD200 = lambda loc, gr: AD(f'{loc} (5.14)', gr)

ENTRIES = [
 A('18:1', G('18:1'), 'And he was telling them a parable about their need to pray always and not lose heart,',
   'present (Marc. 4.36.1)', [T361]),
 A('18:2', G('18:2'), 'saying, "There was a certain judge in a certain city who did not fear God and had no regard for any human.',
   'present (Marc. 4.36.1)', [T361]),
 A('18:3', G('18:3'), "And there was a widow in that city, and she kept coming to him, saying, 'Give me justice against my opponent at law.'",
   'present (Marc. 4.36.1)', [T361]),
 U('18:4', G('18:4'), "And for a time he would not; but after these things he said within himself, 'Even if I do not fear God nor have regard for any human,", 'Inside the attested parable 18:1–8.'),
 A('18:5', G('18:5'), 'yet because this widow is giving me trouble, I will give her justice, so that she does not keep coming and in the end strike me under the eye.\'"',
   'present (Marc. 4.36.1)', [T361], wording='NA27. Roth: attested, but no insight into the wording.'),
 U('18:6', G('18:6'), 'And the lord said, "Hear what the judge of injustice says.', 'Inside the attested parable 18:1–8.'),
 A('18:7', G('18:7'), 'And will God not do justice for his chosen ones, who cry to him day and night, and is he slow to anger over them?',
   'present (Marc. 4.36.1)', [T('4.36.1', '"Sed subiunxit facturum deum vindictam electorum suorum… quem electorum suorum clamantium ad eum die et nocte vindicem ostendit."')]),
 U('18:8', G('18:8'), 'I tell you that he will do justice for them quickly. But when the son of the human comes, will he find the trust on the earth?"', 'Inside the attested parable 18:1–8.'),
 U('18:9', G('18:9'), 'And he also told this parable to some who relied on themselves that they were just, and treated the rest as nothing:', 'Opens the attested parable 18:9–14.'),
 A('18:10', G('18:10'), '"Two humans went up into the temple to pray, the one a Pharisee and the other a tax collector.',
   'present (Marc. 4.36.1–2)', [T3612, T('4.36.2', '"Alterius dei nec templum nec oratores nec iudicium invenio penes Christum, nisi creatoris."')]),
 A('18:11', G('18:11'), "The Pharisee, standing, was praying these things toward himself: 'God, I give you thanks that I am not like the rest of the humans, plunderers, unjust, adulterers, or even like this tax collector.",
   'present (Marc. 4.36.1–2)', [T3612], wording='NA27. Roth: an arrogant prayer is attested, but no insight into its wording.'),
 A('18:12', G('18:12'), "I fast twice in the week; I give a tenth of all that I acquire.'",
   'present (Marc. 4.36.1–2)', [T3612], wording='NA27. Roth: attested, but no insight into the wording.'),
 A('18:13', G('18:13'), "But the tax collector, standing far off, would not even lift up his eyes to heaven, but was beating his chest, saying, 'God, be merciful to me, the sinner.'",
   'present (Marc. 4.36.1–2)', [T3612], wording='NA27 (ἔτυπτεν; SBLGNT ἔτυπτε — checked on the page image). Roth: a humble prayer is attested, but no insight into its wording.'),
 A('18:14', G('18:14'), 'I tell you, this one went down to his house declared just, rather than that one; because everyone who lifts himself up will be brought low, but the one who brings himself low will be lifted up."',
   'present (Marc. 4.36.1–2)', [T3612]),
 U('18:15', G('18:15'), 'And they were bringing to him even their babies, so that he might touch them; but seeing it, the learners were rebuking them.', 'Inside the attested paragraph 18:15–17.'),
 A('18:16', G('18:16'), 'But Jesus called them to him, saying, "Let the little children come to me, and do not hinder them, for of such is the kingdom of God.',
   'present (Adam. 32,26–27; Roth: wording possible only)',
   [AD('32,26–27 (1.16)', '[Megethius, the Marcionite speaker] ὁ δὲ ἀγαθὸς κύριος ἄφετε φησίν τὰ παιδία ἔρχεσθαι πρός με· τῶν γὰρ τοιούτων ἐστὶν ἡ βασιλεία τῶν οὐρανῶν.')],
   wording='NA27. The Marcionite speaker in the Dialogue sets the saying against Elisha and the bears (2 Kgs 2:23–24) in an antithesis. His "kingdom of the heavens" is Matthew\'s; "come to me" is Luke\'s wording. Tertullian knows a similar antithesis but sets it against Matt 18:3–4 (4.23.4). The attestation is weak, and Roth rates the wording possible only.'),
 U('18:17', G('18:17'), 'Amen, I tell you, whoever does not receive the kingdom of God like a little child will not go into it at all."', 'Inside the attested paragraph 18:15–17.'),
 A('18:18', G('18:18'), 'And a certain ruler asked him, saying, "Good teacher, by doing what shall I inherit life of the age?"',
   'present (Marc. 4.36.4, 6; Pan. 42.11.6, sch. 50; Adam. 92,25–26)',
   [E(50, '»εἶπέ τις πρὸς αὐτόν· διδάσκαλε ἀγαθέ, τί ποιήσας ζωὴν αἰώνιον κληρονομήσω;«'),
    T('4.36.4', '"Denique interrogatus ab illo quodam, Praeceptor optime, quid faciens vitam aeternam possidebo?"')]),
 A('18:19', G('18:19'),
   'And Jesus said to him, "Why do you call me good? No one is good except one, God.',
   'present (Marc. 4.36.3, 6; Pan. 42.11.6, sch. 50; Adam. 2,18–19; 92,26–27; Origen, Princ. 2.5.1, 4; Hippolytus, Haer. 7.31.6)',
   [E(50, '»ὁ δέ· μή με λέγε ἀγαθόν. εἷς ἐστιν ἀγαθός ὁ θεός«· προσέθετο ἐκεῖνος »ὁ πατήρ«.'),
    T('4.36.3', '"Sed quis optimus, nisi unus, inquit, deus?"'),
    AD('2,18–19 (1.1)', '[Megethius] …οὐδεὶς ἀγαθὸς εἰ μὴ εἷς, ὁ πατήρ.')],
   wording=('NA27 (εἰ μὴ εἷς ὁ θεός), the text before Marcion (METHOD §11). Marcion\'s text in its later copies read "God the Father" (ὁ θεὸς ὁ πατήρ): Epiphanius says that Marcion "added \'the Father\'", and the Dialogue and Origen\'s report of the heretics\' use have it (Roth: very likely). Tertullian, the earliest witness, has only "God" ("nisi unus deus"), and Roth allows that the copies differed. '
            'In the correspondential reading "Father" is everywhere relational (in address, "your Father", "my Father", the Father who gives); only this reading fixes it as a title (docs/research/correspondence/decisions.md, T2). '
            'Epiphanius\' "do not call me good" and "one is good" are rated probable only; NA27 is printed for the rest.')),
 A('18:20', G('18:20', [('Μὴ μοιχεύσῃς, Μὴ φονεύσῃς, Μὴ κλέψῃς, Μὴ ψευδομαρτυρήσῃς', 'Μὴ φονεύσῃς, Μὴ μοιχεύσῃς, Μὴ κλέψῃς, Μηδὲ ψευδομαρτυρήσῃς')]),
   'You know the commandments: Do not murder, Do not commit adultery, Do not steal, Do not bear false witness, Honour your father and mother."',
   'present (Marc. 4.36.4–5, 7; Pan. 42.11.6, sch. 50; Adam. 92,27–29)',
   [T('4.36.5', '"Resciditne Christus priora praecepta, non occidendi, non adulterandi, non furandi, non falsum testandi, diligendi patrem et matrem?"'),
    E(50, '…καὶ ἀντὶ τοῦ »τὰς ἐντολὰς οἶδας« λέγει »τὰς ἐντολὰς οἶδα«.')],
   wording=('Marcionite reading adopted: the order "do not murder, do not commit adultery" (Tertullian; the Dialogue), with μηδέ before the last prohibition (the Dialogue); Roth: very likely. It is the order of the Hebrew Decalogue, Matthew 19:18 and almost every Old Latin manuscript of Luke. '
            'Epiphanius has "I know the commandments" (spoken by the man); Tertullian and the Dialogue have "you know". Roth: the copies may have differed. NA27 "you know" is printed.'),
   western='The order kill–adultery is that of the Old Latin.'),
 A('18:21', G('18:21'), 'And he said, "All these I have kept from youth."',
   'present (Marc. 4.36.4; Adam. 92,29–30)', [T('4.36.4', '"cumque ille principaliora quaeque affirmasset observasse se ab adulescentia".')],
   wording='NA27 (without μου; SBLGNT has it — checked on the page image).'),
 A('18:22', G('18:22', [('Ἔτι ἕν σοι λείπει', 'Ἕν σοι λείπει'), ('καὶ διάδος πτωχοῖς', 'καὶ δὸς πτωχοῖς'), ('ἐν οὐρανοῖς', 'ἐν οὐρανῷ')]),
   'And hearing it, Jesus said to him, "One thing you lack: sell all that you have and give to the destitute, and you will have treasure in heaven; and come, follow me."',
   'present (Marc. 4.36.4, 6, 7; Adam. 92,30–32)',
   [T('4.36.4', '"Unum, inquit, tibi deest: omnia, quaecunque habes, vende et da pauperibus, et habebis thesaurum in caelo, et veni, sequere me."'),
    T('4.36.7', '"Vende, inquit, quae habes… Et da, inquit, egenis… Et veni, inquit, sequere me."')],
   wording=('Marcionite readings adopted: no "still" (ἔτι) before "one thing you lack", δός ("give") for διάδος ("distribute"), and ἐν οὐρανῷ ("in heaven", singular) for NA27\'s ἐν [τοῖς] οὐρανοῖς. Tertullian quotes the verse and repeats its parts; the Dialogue agrees. Roth: secure. '
            'δός is the reading of ℵ A D L and others, ἐν οὐρανῷ of W Θ Ψ f1.13 and the Byzantine text (NA27 apparatus).')),
 A('18:23', G('18:23'), 'But hearing these things, he became deeply grieved, for he was very rich.',
   'present (Marc. 4.36.5)', [T('4.36.5', '"uti gloriosissimus ille observator praeceptorum pecuniam multo cariorem habiturus traduceretur".')],
   wording='NA27. Roth: attested, but no insight into the wording.'),
 A('18:35', G('18:35'), 'And it happened, as he was drawing near to Jericho, that a certain blind man was sitting beside the road, begging.',
   'present (Marc. 4.36.9; Pan. 42.11.6, sch. 51; Adam. 200,22–24)',
   [E(51, '»ἐγένετο δὲ ἐν τῷ ἐγγίζειν αὐτὸν τῇ Ἱεριχὼ τυφλὸς ἐβόα…«'),
    T('4.36.9', '"Cum igitur praetereuntem illum caecus audisset…"')]),
 A('18:36', G('18:36'), 'And hearing a crowd journeying through, he was asking what this might be.',
   'present (Adam. 200,24–25)', [AD200('200,24–25', 'ἀκούσας δὲ ὄχλου διαπορευομένου ἐπυνθάνετο τί ἂν εἴη τοῦτο.')]),
 A('18:37', G('18:37'), 'And they reported to him, "Jesus the Nazoraean is passing by."',
   'present (Marc. 4.36.9; Adam. 200,25–26)', [T('4.36.9', '"praetereuntem illum".'), AD200('200,25–26', 'ἀπηγγέλθη δὲ αὐτῷ ὅτι Ἰησοῦς παρέρχεται.')],
   wording='NA27. The Dialogue has no "of Nazareth"; Roth: "may have been missing". Not adopted (one witness).'),
 A('18:38', G('18:38'), 'And he shouted, saying, "Jesus, son of David, have mercy on me!"',
   'present (Marc. 4.36.9, 11; 4.37.1; 4.38.10; Pan. 42.11.6, sch. 51; Adam. 200,26)',
   [E(51, '»…τυφλὸς ἐβόα· Ἰησοῦ υἱὲ Δαυίδ, ἐλέησόν με«.'),
    T('4.36.9', '"cur exclamavit, Iesu, fili David, miserere mei!"')]),
 A('18:39', G('18:39'), 'And those going in front were rebuking him, so that he would be silent; but he was crying out all the more, "Son of David, have mercy on me!"',
   'present (Marc. 4.36.9)', [T('4.36.9', '"Sed antecedentes increpabant caecum, uti taceret."')]),
 A('18:40', G('18:40'), 'And Jesus, standing still, ordered him to be led to him. And when he had drawn near, he asked him,',
   'present (Adam. 200,26–28)', [AD200('200,26–28', 'σταθεὶς δὲ… ἐκέλευσεν αὐτὸν ἀχθῆναι… ἐγγίσαντος δὲ αὐτοῦ ἐπηρώτησεν αὐτόν·')]),
 A('18:41', G('18:41'), '"What do you want me to do for you?" And he said, "Lord, that I may see again."',
   'present (Adam. 200,28–29)', [AD200('200,28–29', 'τί σοι θέλεις ποιήσω; ὁ δὲ εἶπεν· κύριε, ἵνα ἀναβλέψω.')]),
 A('18:42', G('18:42'), 'And Jesus said to him, "See again; your trust has saved you."',
   'present (Marc. 4.36.10, 12; Pan. 42.11.6, sch. 51; Adam. 200,29–30)',
   [E(51, '»καὶ ὅτε ἰάθη, φησίν· ἡ πίστις σου σέσωκέν σε«.'), T('4.36.10', '"Fides, inquit, tua te salvum fecit."')]),
 A('18:43', G('18:43'), 'And at once he saw again, and he was following him, giving glory to God. And all the people, seeing it, gave praise to God.',
   'present (Marc. 4.36.12; 4.37.1; Pan. 42.11.6, sch. 51; Adam. 200,30)',
   [T('4.37.1', '"et omnis populus laudes referebat deo, non Marcionis, sed David".')]),
]

OMITTED = [
 dict(ref='18:24–30', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='The camel and the needle, and the reward of those who left everything: a separate NA27 paragraph with no attested verse (METHOD §4.3). Tertullian passes from 18:23 (4.36.5) to 18:35 (4.36.8–9). The Dialogue of Adamantius refers to 18:24–30, but not from Marcion\'s text (Harnack, Roth).')),
 dict(ref='18:31–33', cls='A−', app=dict(roth='absent', witnesses=[
      E(52, 'παρέκοψε τὸ »παραλαβὼν τοὺς δώδεκα ἔλεγεν· ἰδού, ἀναβαίνομεν εἰς Ἱεροσόλυμα καὶ τελεσθήσεται πάντα τὰ γεγραμμένα ἐν τοῖς προφήταις περὶ τοῦ υἱοῦ τοῦ ἀνθρώπου. παραδοθήσεται γὰρ καὶ ἀποκτανθήσεται καὶ τῇ τρίτῃ ἡμέρᾳ ἀναστήσεται«· ὅλα ταῦτα παρέκοψε.')],
      decision='not printed', reason='Epiphanius states that the whole third prediction of the passion, with "everything written by the prophets about the son of man will be fulfilled", was not in the text. Tertullian passes from 18:23 to 18:35; Roth counts his silence as confirmation (tacitus). The prediction "by the prophets" would have been Tertullian\'s proof that Christ fulfilled the Creator\'s prophecies.')),
 dict(ref='18:34', cls='U−', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='"But they understood none of these things; this saying was hidden from them." It refers to the prediction in 18:31–33, which Epiphanius says the text lacked, and closes the same NA27 paragraph.')),
]

PREAMBLE = (
 "Prayer, the commandments and the son of David. Jesus tells of a widow who wore down an unjust judge, and says that God "
 "will give justice to his chosen ones who cry to him day and night. He tells of a Pharisee and a tax collector praying in "
 "temple, and of the one who went home justified. A ruler asks what he must do to inherit life of the age. Jesus answers, "
 "\"No one is good except one, God,\" and lists the commandments in the order \"do not murder, do not "
 "commit adultery\". He then tells the man: \"One thing you lack: sell all that you have and give to the poor… and come, "
 "follow me.\" Near Jericho a blind man calls him \"Jesus, son of David\" and is healed. The third prediction of the passion, "
 "with its appeal to \"everything written by the prophets\" (18:31–33), is not in the text (Epiphanius, sch. 52)."
)

NOTES = [
 dict(term='The widow and the judge (18:1–8)', cat='textual', refs=['18:1', '18:2', '18:3', '18:5', '18:7'], text=(
  "Tertullian, Marc. 4.36.1: Christ \"set the parable of the judge forced to hear the widow by her persistence\" and \"added "
  "that God would avenge his chosen ones who cry to him day and night\". So the God to be prayed to is a judge and avenger, the "
  "Creator. 18:4, 18:6 and 18:8 are not cited and are printed in grey.")),
 dict(term='The Pharisee and the tax collector (18:9–14)', cat='textual', refs=['18:9', '18:10', '18:11', '18:13', '18:14'], text=(
  "Tertullian, Marc. 4.36.1–2: two men praying in the temple \"with different minds\", the Pharisee in pride and the tax "
  "collector in humility, \"one rejected and the other went down justified\". He notes that the temple is the Creator's "
  "temple. 18:9 is not cited and is printed in grey.")),
 dict(term='"Except one, God" and the commandments (18:18–23)', cat='textual', refs=['18:18', '18:19', '18:20', '18:22', '18:23'], text=(
  "Epiphanius, sch. 50 quotes the exchange: \"Good teacher, what must I do to inherit life of the age?\" \"Do not call me good; "
  "one is good, God\", to which, he says, Marcion \"added 'the Father'\". The Marcionite speaker in the Dialogue of Adamantius "
  "has the same \"except one, the Father\", and Origen reports the heretics' use of it. Tertullian (4.36.3–7), the earliest "
  "witness, has \"one God\" without \"the Father\", "
  "and lists the commandments in the order \"not to kill, not to commit adultery, not to steal, not to bear false witness, to "
  "love father and mother\". He quotes the command to sell all and give to the poor, \"and you will have treasure in heaven, "
  "and come, follow me\", and says Christ \"kept the earlier commandments and added what was lacking\", as in Micah 6:8. "
  "\"The Father\" belongs to the later copies of Marcion's text and is not printed: the text before Marcion is decided by the "
  "earliest witness together with the correspondential reading, in which \"Father\" is relational throughout and only this "
  "reading makes it a title (METHOD §11). The order of the commandments and \"give… treasure in heaven\" are printed.")),
 dict(term='Not printed: 18:24–34', cat='excision', refs=['18:23', '18:35'], text=(
  "18:24–30 (the camel and the needle; the reward for leaving home and family) are not cited by any witness and form a "
  "paragraph without an attested verse. 18:31–33, the third prediction of the passion with \"everything written by the "
  "prophets about the son of man will be fulfilled\", is stated by Epiphanius to have been absent (sch. 52). 18:34, the "
  "disciples not understanding \"these things\", depends on it.")),
 dict(term='The blind man at Jericho (18:35–43)', cat='textual', refs=['18:35', '18:37', '18:38', '18:39', '18:42', '18:43'], text=(
  "Three witnesses attest the healing. Epiphanius, sch. 51: \"as he drew near to Jericho a blind man cried, Jesus, son of "
  "David, have mercy on me… your trust has saved you\". Tertullian (4.36.8–14) dwells on the title: the blind man called him "
  "\"son of David\", and Jesus, far from correcting him, healed him and praised his faith. Tertullian takes this as proof that "
  "Jesus was known to be of David's family. The Dialogue (200) quotes the whole story; 18:36 and 18:40–41 rest on it alone.")),
 dict(term='Son of David', cat='theological', refs=['18:38', '18:42'], text=(
  "Interpretation. The attested text has a blind man twice call Jesus \"son of David\", and Jesus answer with healing and "
  "\"your trust has saved you\". Tertullian's argument from this is that a Christ with no birth could not have been publicly "
  "known as David's descendant (4.36.8). The text does not say how the title was known. The library connects the Davidic "
  "descent of Jesus' family with the desposyni, the relatives who led the Jerusalem community (Carriers of Living Water). "
  "The verse shows only that the title was used of him and accepted.")),
 dict(term='πρὸς τὸ δεῖν… προσεύχεσθαι, "about their need to pray"', cat='translation', refs=['18:1'], text='δεῖ, "must", as at 4:43.'),
 dict(term='μὴ ἐγκακεῖν, "not lose heart"', cat='translation', refs=['18:1'], text='To grow weary, give up.'),
 dict(term='μὴ ἐντρεπόμενος, "had no regard for"', cat='translation', refs=['18:2'], text='To turn toward, respect, feel shame before.'),
 dict(term='ἤρχετο, "kept coming"', cat='translation', refs=['18:3'], text='The imperfect: again and again.'),
 dict(term='Ἐκδίκησόν με, "give me justice"', cat='translation', refs=['18:3'], text='ἐκδικέω, to see justice done for someone. "Avenge" is too narrow; "vindicate" is close. The same root returns in 18:5, 18:7 and 18:8.'),
 dict(term='ἀντιδίκου, "opponent at law"', cat='translation', refs=['18:3'], text='As at 12:58.'),
 dict(term='κόπον, "trouble"', cat='translation', refs=['18:5'], text='As at 11:7.'),
 dict(term='ὑπωπιάζῃ με, "strike me under the eye"', cat='translation', refs=['18:5'], text='A boxer\'s word: to hit under the eye, to give a black eye. It is often softened to "wear me out". The Greek is the boxing word, possibly meant as a figure of speech for being worn down or shamed.'),
 dict(term='εἰς τέλος, "in the end"', cat='translation', refs=['18:5'], text='Or "continually", "for good".'),
 dict(term='ὁ κύριος, "the lord"', cat='translation', refs=['18:6'], text='As at 7:13.'),
 dict(term='ὁ κριτὴς τῆς ἀδικίας, "the judge of injustice"', cat='translation', refs=['18:6'], text='A Semitic genitive, as at 16:8.'),
 dict(term='τῶν ἐκλεκτῶν αὐτοῦ, "his chosen ones"', cat='translation', refs=['18:7'], text='Those picked out.'),
 dict(term='μακροθυμεῖ ἐπ\' αὐτοῖς, "is he slow to anger over them"', cat='translation', refs=['18:7'], text='μακροθυμέω, to be long-tempered, patient. Whether it is patience toward the chosen or delay in helping them is not clear in the Greek.'),
 dict(term='τὴν πίστιν, "the trust"', cat='translation', refs=['18:8'], text='With the article: "the" trust, as the widow showed it.'),
 dict(term='τοὺς πεποιθότας ἐφ\' ἑαυτοῖς, "who relied on themselves"', cat='translation', refs=['18:9'], text='πείθω in the perfect, as at 11:22.'),
 dict(term='ἐξουθενοῦντας, "treated as nothing"', cat='translation', refs=['18:9'], text='To make nothing of, despise.'),
 dict(term='ἀνέβησαν, "went up"', cat='translation', refs=['18:10'], text='To go up: the temple stood on a height.'),
 dict(term='εἰς τὸ ἱερόν, "into the temple"', cat='translation', refs=['18:10'], text='ἱερόν, the whole sacred precinct.'),
 dict(term='πρὸς ἑαυτόν, "toward himself"', cat='translation', refs=['18:11'], text='It can go with "standing" (standing by himself) or with "praying" (praying to himself). The Greek allows both.'),
 dict(term='ἅρπαγες, "plunderers"', cat='translation', refs=['18:11'], text='From ἁρπαγή, "plunder" (11:39).'),
 dict(term='δὶς τοῦ σαββάτου, "twice in the week"', cat='translation', refs=['18:12'], text='σάββατον also means the week, the span from sabbath to sabbath.'),
 dict(term='ἔτυπτεν, "was beating"', cat='translation', refs=['18:13'], text='The imperfect: he kept beating. ἔτυπτεν is the form of NA27 here.'),
 dict(term='ἱλάσθητί μοι, "be merciful to me"', cat='translation', refs=['18:13'], text='ἱλάσκομαι, to be propitious, to be appeased. It is the word of the temple\'s atonement. "Be merciful" gives the sense; the Greek is the language of sacrifice.'),
 dict(term='τῷ ἁμαρτωλῷ, "the sinner"', cat='translation', refs=['18:13'], text='With the article: "the" sinner, not "a" sinner.'),
 dict(term='δεδικαιωμένος, "declared just"', cat='translation', refs=['18:14'], text='δικαιόω, as at 16:15.'),
 dict(term='παρ\' ἐκεῖνον, "rather than that one"', cat='translation', refs=['18:14'], text='Literally "beside that one": in comparison with, instead of.'),
 dict(term='ὁ ὑψῶν ἑαυτόν, "who lifts himself up"', cat='translation', refs=['18:14'], text='ὑψόω, to raise high.'),
 dict(term='ταπεινωθήσεται, "will be brought low"', cat='translation', refs=['18:14'], text='ταπεινόω, to lower, humble.'),
 dict(term='τὰ βρέφη, "their babies"', cat='translation', refs=['18:15'], text='βρέφος, an infant. The Greek has the article: "the" babies, their own.'),
 dict(term='Ἄφετε, "let"', cat='translation', refs=['18:16'], text='ἀφίημι, as at 6:42.'),
 dict(term='τὰ παιδία, "the little children"', cat='translation', refs=['18:16'], text='As at 9:47.'),
 dict(term='οὐ μή, "not… at all"', cat='translation', refs=['18:17'], text='A double negative, as at 10:19.'),
 dict(term='ἄρχων, "ruler"', cat='translation', refs=['18:18'], text='As at 8:41.'),
 dict(term='ζωὴν αἰώνιον, "life of the age"', cat='translation', refs=['18:18'], text='αἰώνιος, belonging to the age to come. "Eternal life" makes it endless time.'),
 dict(term='εἰ μὴ εἷς ὁ θεός, "except one, God"', cat='translation', refs=['18:19'], text='The wording of canonical Luke, which this edition prints here in place of the later Marcionite "God the Father" (METHOD §11). εἷς ὁ θεός can be read "one, God", "the one God", or "God alone". The word order is kept.'),
 dict(term='Μὴ φονεύσῃς, "do not murder"', cat='translation', refs=['18:20'], text='φονεύω, to murder, not the general word for killing. This text has the commandments in the order murder, adultery.'),
 dict(term='ἐφύλαξα, "I have kept"', cat='translation', refs=['18:21'], text='φυλάσσω, to guard, keep.'),
 dict(term='Ἕν σοι λείπει, "one thing you lack"', cat='translation', refs=['18:22'], text='The reading of this text, without "still".'),
 dict(term='δὸς πτωχοῖς, "give to the destitute"', cat='translation', refs=['18:22'], text='The reading of this text, δός. πτωχός, as at 6:20.'),
 dict(term='ἐν οὐρανῷ, "in heaven"', cat='translation', refs=['18:22'], text='Singular in this text.'),
 dict(term='δεῦρο, "come"', cat='translation', refs=['18:22'], text='"Here!", "come on!"'),
 dict(term='περίλυπος, "deeply grieved"', cat='translation', refs=['18:23'], text='Grieved all around, very sad.'),
 dict(term='ἐπαιτῶν, "begging"', cat='translation', refs=['18:35'], text='ἐπαιτέω, as at 16:3.'),
 dict(term='ἐπυνθάνετο, "he was asking"', cat='translation', refs=['18:36'], text='To inquire.'),
 dict(term='ὁ Ναζωραῖος, "the Nazoraean"', cat='translation', refs=['18:37'], text='A different form from Ναζαρηνός (4:34). Whether both mean "of Nazara" is debated; the Greek form is kept.'),
 dict(term='υἱὲ Δαυίδ, "son of David"', cat='translation', refs=['18:38'], text="A title of the expected king from David's line."),
 dict(term='ἐλέησόν με, "have mercy on me"', cat='translation', refs=['18:38'], text='As at 16:24.'),
 dict(term='οἱ προάγοντες, "those going in front"', cat='translation', refs=['18:39'], text='Those leading the procession.'),
 dict(term='ἔκραζεν, "was crying out"', cat='translation', refs=['18:39'], text='The imperfect: he kept crying out.'),
 dict(term='ἀναβλέψω, "see again"', cat='translation', refs=['18:41'], text='As at 7:22.'),
 dict(term='αἶνον, "praise"', cat='translation', refs=['18:43'], text='A word of praise.'),
]
