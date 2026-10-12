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
 A('18:1', G('18:1'), 'He told them a parable to show that they ought always to pray and not lose heart.',
   'present (Marc. 4.36.1)', [T361]),
 A('18:2', G('18:2'), 'He said, "In a certain town there was a judge who neither feared God nor respected people.',
   'present (Marc. 4.36.1)', [T361]),
 A('18:3', G('18:3'), 'And there was a widow in that town who kept coming to him and saying, \'Give me justice against my adversary.\'',
   'present (Marc. 4.36.1)', [T361]),
 U('18:4', G('18:4'), 'For a while he refused, but afterwards he said to himself, \'Though I neither fear God nor respect people,', 'Inside the attested parable 18:1–8.'),
 A('18:5', G('18:5'), 'yet because this widow keeps bothering me, I will give her justice, so that she does not wear me out by her continual coming.\'"',
   'present (Marc. 4.36.1)', [T361], wording='NA27. Roth: attested, but no insight into the wording.'),
 U('18:6', G('18:6'), 'And the Lord said, "Hear what the unjust judge says.', 'Inside the attested parable 18:1–8.'),
 A('18:7', G('18:7'), 'And will not God give justice to his chosen ones, who cry to him day and night? Will he delay long over them?',
   'present (Marc. 4.36.1)', [T('4.36.1', '"Sed subiunxit facturum deum vindictam electorum suorum… quem electorum suorum clamantium ad eum die et nocte vindicem ostendit."')]),
 U('18:8', G('18:8'), 'I tell you, he will give them justice quickly. Nevertheless, when the son of man comes, will he find faith on earth?"', 'Inside the attested parable 18:1–8.'),
 U('18:9', G('18:9'), 'He also told this parable to some who trusted in themselves that they were righteous, and treated others with contempt:', 'Opens the attested parable 18:9–14.'),
 A('18:10', G('18:10'), '"Two men went up into the temple to pray, one a Pharisee and the other a tax collector.',
   'present (Marc. 4.36.1–2)', [T3612, T('4.36.2', '"Alterius dei nec templum nec oratores nec iudicium invenio penes Christum, nisi creatoris."')]),
 A('18:11', G('18:11'), 'The Pharisee, standing by himself, prayed thus: \'God, I thank you that I am not like other people, robbers, unjust, adulterers, or even like this tax collector.',
   'present (Marc. 4.36.1–2)', [T3612], wording='NA27. Roth: an arrogant prayer is attested, but no insight into its wording.'),
 A('18:12', G('18:12'), 'I fast twice a week; I give tithes of all that I get.\'',
   'present (Marc. 4.36.1–2)', [T3612], wording='NA27. Roth: attested, but no insight into the wording.'),
 A('18:13', G('18:13'), 'But the tax collector, standing far off, would not even lift up his eyes to heaven, but beat his breast, saying, \'God, be merciful to me, a sinner!\'',
   'present (Marc. 4.36.1–2)', [T3612], wording='NA27 (ἔτυπτεν; SBLGNT ἔτυπτε — checked on the page image). Roth: a humble prayer is attested, but no insight into its wording.'),
 A('18:14', G('18:14'), 'I tell you, this man went down to his house justified rather than the other; for everyone who exalts himself will be humbled, but the one who humbles himself will be exalted."',
   'present (Marc. 4.36.1–2)', [T3612]),
 U('18:15', G('18:15'), 'Now they were bringing even infants to him that he might touch them; and when the disciples saw it, they rebuked them.', 'Inside the attested paragraph 18:15–17.'),
 A('18:16', G('18:16'), 'But Jesus called them to him, saying, "Let the children come to me, and do not hinder them; for to such belongs the kingdom of God.',
   'present (Adam. 32,26–27; Roth: wording possible only)',
   [AD('32,26–27 (1.16)', '[Megethius, the Marcionite speaker] ὁ δὲ ἀγαθὸς κύριος ἄφετε φησίν τὰ παιδία ἔρχεσθαι πρός με· τῶν γὰρ τοιούτων ἐστὶν ἡ βασιλεία τῶν οὐρανῶν.')],
   wording='NA27. The Marcionite speaker in the Dialogue sets the saying against Elisha and the bears (2 Kgs 2:23–24) in an antithesis. His "kingdom of the heavens" is Matthew\'s; "come to me" is Luke\'s wording. Tertullian knows a similar antithesis but sets it against Matt 18:3–4 (4.23.4). The attestation is weak, and Roth rates the wording possible only.'),
 U('18:17', G('18:17'), 'Truly I tell you, whoever does not receive the kingdom of God like a child will never enter it."', 'Inside the attested paragraph 18:15–17.'),
 A('18:18', G('18:18'), 'And a ruler asked him, "Good teacher, what must I do to inherit eternal life?"',
   'present (Marc. 4.36.4, 6; Pan. 42.11.6, sch. 50; Adam. 92,25–26)',
   [E(50, '»εἶπέ τις πρὸς αὐτόν· διδάσκαλε ἀγαθέ, τί ποιήσας ζωὴν αἰώνιον κληρονομήσω;«'),
    T('4.36.4', '"Denique interrogatus ab illo quodam, Praeceptor optime, quid faciens vitam aeternam possidebo?"')]),
 A('18:19', G('18:19', [('εἰ μὴ εἷς ὁ θεός.', 'εἰ μὴ εἷς ὁ θεὸς ὁ πατήρ.')]),
   'And Jesus said to him, "Why do you call me good? No one is good except one, God the Father.',
   'present (Marc. 4.36.3, 6; Pan. 42.11.6, sch. 50; Adam. 2,18–19; 92,26–27; Origen, Princ. 2.5.1, 4; Hippolytus, Haer. 7.31.6)',
   [E(50, '»ὁ δέ· μή με λέγε ἀγαθόν. εἷς ἐστιν ἀγαθός ὁ θεός«· προσέθετο ἐκεῖνος »ὁ πατήρ«.'),
    T('4.36.3', '"Sed quis optimus, nisi unus, inquit, deus?"'),
    AD('2,18–19 (1.1)', '[Megethius] …οὐδεὶς ἀγαθὸς εἰ μὴ εἷς, ὁ πατήρ.')],
   wording=('Marcionite reading adopted: "God the Father" (ὁ θεὸς ὁ πατήρ) for "God". Epiphanius says that Marcion "added \'the Father\'"; the Dialogue and Origen\'s report of the heretics\' use also have "the Father"; Roth: very likely. Tertullian has only "God", and Roth allows that the copies differed. '
            'Epiphanius\' "do not call me good" and "one is good" are rated probable only; NA27 is printed for the rest.')),
 A('18:20', G('18:20', [('Μὴ μοιχεύσῃς, Μὴ φονεύσῃς, Μὴ κλέψῃς, Μὴ ψευδομαρτυρήσῃς', 'Μὴ φονεύσῃς, Μὴ μοιχεύσῃς, Μὴ κλέψῃς, Μηδὲ ψευδομαρτυρήσῃς')]),
   'You know the commandments: Do not kill, do not commit adultery, do not steal, do not bear false witness, honour your father and mother."',
   'present (Marc. 4.36.4–5, 7; Pan. 42.11.6, sch. 50; Adam. 92,27–29)',
   [T('4.36.5', '"Resciditne Christus priora praecepta, non occidendi, non adulterandi, non furandi, non falsum testandi, diligendi patrem et matrem?"'),
    E(50, '…καὶ ἀντὶ τοῦ »τὰς ἐντολὰς οἶδας« λέγει »τὰς ἐντολὰς οἶδα«.')],
   wording=('Marcionite reading adopted: the order "do not kill, do not commit adultery" (Tertullian; the Dialogue), with μηδέ before the last prohibition (the Dialogue); Roth: very likely. It is the order of the Hebrew Decalogue, Matthew 19:18 and almost every Old Latin manuscript of Luke. '
            'Epiphanius has "I know the commandments" (spoken by the man); Tertullian and the Dialogue have "you know". Roth: the copies may have differed. NA27 "you know" is printed.'),
   western='The order kill–adultery is that of the Old Latin.'),
 A('18:21', G('18:21'), 'And he said, "All these I have kept from my youth."',
   'present (Marc. 4.36.4; Adam. 92,29–30)', [T('4.36.4', '"cumque ille principaliora quaeque affirmasset observasse se ab adulescentia".')],
   wording='NA27 (without μου; SBLGNT has it — checked on the page image).'),
 A('18:22', G('18:22', [('Ἔτι ἕν σοι λείπει', 'Ἕν σοι λείπει'), ('καὶ διάδος πτωχοῖς', 'καὶ δὸς πτωχοῖς'), ('ἐν οὐρανοῖς', 'ἐν οὐρανῷ')]),
   'When Jesus heard this, he said to him, "One thing you lack: sell all that you have and give to the poor, and you will have treasure in heaven; and come, follow me."',
   'present (Marc. 4.36.4, 6, 7; Adam. 92,30–32)',
   [T('4.36.4', '"Unum, inquit, tibi deest: omnia, quaecunque habes, vende et da pauperibus, et habebis thesaurum in caelo, et veni, sequere me."'),
    T('4.36.7', '"Vende, inquit, quae habes… Et da, inquit, egenis… Et veni, inquit, sequere me."')],
   wording=('Marcionite readings adopted: no "still" (ἔτι) before "one thing you lack", δός ("give") for διάδος ("distribute"), and ἐν οὐρανῷ ("in heaven", singular) for NA27\'s ἐν [τοῖς] οὐρανοῖς. Tertullian quotes the verse and repeats its parts; the Dialogue agrees. Roth: secure. '
            'δός is the reading of ℵ A D L and others, ἐν οὐρανῷ of W Θ Ψ f1.13 and the Byzantine text (NA27 apparatus).')),
 A('18:23', G('18:23'), 'But when he heard these things, he became very sad, for he was very rich.',
   'present (Marc. 4.36.5)', [T('4.36.5', '"uti gloriosissimus ille observator praeceptorum pecuniam multo cariorem habiturus traduceretur".')],
   wording='NA27. Roth: attested, but no insight into the wording.'),
 A('18:35', G('18:35'), 'As he drew near to Jericho, a blind man was sitting by the roadside begging.',
   'present (Marc. 4.36.9; Pan. 42.11.6, sch. 51; Adam. 200,22–24)',
   [E(51, '»ἐγένετο δὲ ἐν τῷ ἐγγίζειν αὐτὸν τῇ Ἱεριχὼ τυφλὸς ἐβόα…«'),
    T('4.36.9', '"Cum igitur praetereuntem illum caecus audisset…"')]),
 A('18:36', G('18:36'), 'Hearing a crowd going by, he asked what this meant.',
   'present (Adam. 200,24–25)', [AD200('200,24–25', 'ἀκούσας δὲ ὄχλου διαπορευομένου ἐπυνθάνετο τί ἂν εἴη τοῦτο.')]),
 A('18:37', G('18:37'), 'They told him, "Jesus of Nazareth is passing by."',
   'present (Marc. 4.36.9; Adam. 200,25–26)', [T('4.36.9', '"praetereuntem illum".'), AD200('200,25–26', 'ἀπηγγέλθη δὲ αὐτῷ ὅτι Ἰησοῦς παρέρχεται.')],
   wording='NA27. The Dialogue has no "of Nazareth"; Roth: "may have been missing". Not adopted (one witness).'),
 A('18:38', G('18:38'), 'And he cried out, "Jesus, son of David, have mercy on me!"',
   'present (Marc. 4.36.9, 11; 4.37.1; 4.38.10; Pan. 42.11.6, sch. 51; Adam. 200,26)',
   [E(51, '»…τυφλὸς ἐβόα· Ἰησοῦ υἱὲ Δαυίδ, ἐλέησόν με«.'),
    T('4.36.9', '"cur exclamavit, Iesu, fili David, miserere mei!"')]),
 A('18:39', G('18:39'), 'And those who were in front rebuked him, telling him to be silent; but he cried out all the more, "Son of David, have mercy on me!"',
   'present (Marc. 4.36.9)', [T('4.36.9', '"Sed antecedentes increpabant caecum, uti taceret."')]),
 A('18:40', G('18:40'), 'Jesus stopped and commanded him to be brought to him. When he came near, he asked him,',
   'present (Adam. 200,26–28)', [AD200('200,26–28', 'σταθεὶς δὲ… ἐκέλευσεν αὐτὸν ἀχθῆναι… ἐγγίσαντος δὲ αὐτοῦ ἐπηρώτησεν αὐτόν·')]),
 A('18:41', G('18:41'), '"What do you want me to do for you?" He said, "Lord, let me see again."',
   'present (Adam. 200,28–29)', [AD200('200,28–29', 'τί σοι θέλεις ποιήσω; ὁ δὲ εἶπεν· κύριε, ἵνα ἀναβλέψω.')]),
 A('18:42', G('18:42'), 'And Jesus said to him, "See again; your faith has saved you."',
   'present (Marc. 4.36.10, 12; Pan. 42.11.6, sch. 51; Adam. 200,29–30)',
   [E(51, '»καὶ ὅτε ἰάθη, φησίν· ἡ πίστις σου σέσωκέν σε«.'), T('4.36.10', '"Fides, inquit, tua te salvum fecit."')]),
 A('18:43', G('18:43'), 'And immediately he saw again and followed him, glorifying God. And all the people, when they saw it, gave praise to God.',
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
 "the temple, and of the one who went home justified. A ruler asks what he must do to inherit eternal life. In this text "
 "Jesus answers, \"No one is good except one, God the Father,\" and lists the commandments in the order \"do not kill, do not "
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
 dict(term='"God the Father" and the commandments (18:18–23)', cat='textual', refs=['18:18', '18:19', '18:20', '18:22', '18:23'], text=(
  "Epiphanius, sch. 50 quotes the exchange: \"Good teacher, what must I do to inherit eternal life?\" \"Do not call me good; "
  "one is good, God\", to which, he says, Marcion \"added 'the Father'\". The Marcionite speaker in the Dialogue of Adamantius "
  "has the same \"except one, the Father\", and Origen reports the heretics' use of it. Tertullian (4.36.3–7) has \"one God\" "
  "and lists the commandments in the order \"not to kill, not to commit adultery, not to steal, not to bear false witness, to "
  "love father and mother\". He quotes the command to sell all and give to the poor, \"and you will have treasure in heaven, "
  "and come, follow me\", and says Christ \"kept the earlier commandments and added what was lacking\", as in Micah 6:8. The "
  "readings \"God the Father\", the order of the commandments, and \"give… treasure in heaven\" are printed.")),
 dict(term='Not printed: 18:24–34', cat='excision', refs=['18:23', '18:35'], text=(
  "18:24–30 (the camel and the needle; the reward for leaving home and family) are not cited by any witness and form a "
  "paragraph without an attested verse. 18:31–33, the third prediction of the passion with \"everything written by the "
  "prophets about the son of man will be fulfilled\", is stated by Epiphanius to have been absent (sch. 52). 18:34, the "
  "disciples not understanding \"these things\", depends on it.")),
 dict(term='The blind man at Jericho (18:35–43)', cat='textual', refs=['18:35', '18:37', '18:38', '18:39', '18:42', '18:43'], text=(
  "Three witnesses attest the healing. Epiphanius, sch. 51: \"as he drew near to Jericho a blind man cried, Jesus, son of "
  "David, have mercy on me… your faith has saved you\". Tertullian (4.36.8–14) dwells on the title: the blind man called him "
  "\"son of David\", and Jesus, far from correcting him, healed him and praised his faith. Tertullian takes this as proof that "
  "Jesus was known to be of David's family. The Dialogue (200) quotes the whole story; 18:36 and 18:40–41 rest on it alone.")),
 dict(term='Son of David', cat='theological', refs=['18:38', '18:42'], text=(
  "Interpretation. The attested text has a blind man twice call Jesus \"son of David\", and Jesus answer with healing and "
  "\"your faith has saved you\". Tertullian's argument from this is that a Christ with no birth could not have been publicly "
  "known as David's descendant (4.36.8). The text does not say how the title was known. The library connects the Davidic "
  "descent of Jesus' family with the desposyni, the relatives who led the Jerusalem community (Carriers of Living Water). "
  "The verse shows only that the title was used of him and accepted.")),
]
