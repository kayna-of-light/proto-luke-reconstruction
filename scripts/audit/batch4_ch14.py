"""Batch 4, chapter 14 of the reconstruction: Luke 16:1–31."""
from buildlib import greek
from batch1_ch2 import U, A
from batch4_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}
AD = lambda loc, ev: {'source': f'Dialogue of Adamantius {loc} (via Roth)', 'evidence': ev}
ADAM = 'present (Adam. 76,16–78,6; Roth: wording probable only)'

ENTRIES = [
 U('16:1', G('16:1'), 'And he was saying also to the learners, "There was a certain rich man who had a steward, and this one was accused to him of scattering his possessions.', 'Opens the attested parable 16:1–9.'),
 A('16:2', G('16:2'), "And calling him, he said to him, 'What is this I hear about you? Give back the account of your stewardship, for you can no longer be steward.'",
   'present (Marc. 4.33.1)', [T('4.33.1', '"secundum servi illius exemplum, qui ab actu summotus…"')], wording='NA27. Roth: attested, but no insight into the wording.'),
 U('16:3', G('16:3'), "And the steward said within himself, 'What shall I do, since my lord is taking the stewardship away from me? To dig I am not strong enough; to beg I am ashamed.", 'Inside the attested parable 16:1–9.'),
 A('16:4', G('16:4'), "I know what I will do, so that when I am removed from the stewardship they will receive me into their own houses.'",
   'present (Marc. 4.33.1)', [T('4.33.1', '"in subsidium sibi" — the steward providing for himself.')], wording='NA27. Roth: attested, but no insight into the wording.'),
 A('16:5', G('16:5'), "And calling to him each one of his lord's debtors, he was saying to the first, 'How much do you owe my lord?'",
   'present (Marc. 4.33.1)', [T('4.33.1', '"dominicos debitores deminutis cautionibus relevat".')], wording='NA27. Roth: attested, but no insight into the wording.'),
 A('16:6', G('16:6'), "And he said, 'A hundred baths of olive oil.' And he said to him, 'Take your writings, and sitting down quickly, write fifty.'",
   'present (Marc. 4.33.1)', [T('4.33.1', '"deminutis cautionibus" — reducing the written bonds.')], wording='NA27. Roth: attested, but no insight into the wording.'),
 A('16:7', G('16:7'), "Then he said to another, 'And you, how much do you owe?' And he said, 'A hundred kors of wheat.' He says to him, 'Take your writings, and write eighty.'",
   'present (Marc. 4.33.1)', [T('4.33.1', '"deminutis cautionibus".')], wording='NA27. Roth: attested, but no insight into the wording.'),
 U('16:8', G('16:8'), 'And the lord praised the steward of injustice, because he had acted sensibly; for the sons of this age are more sensible than the sons of the light toward their own generation.', 'Inside the attested parable 16:1–9.'),
 A('16:9', G('16:9'), 'And I say to you, make friends for yourselves out of the Mammon of injustice, so that when it gives out they may receive you into the tents of the age.',
   'present for 16:9a (Marc. 4.33.1); 16:9b unattested', [T('4.33.1', '"Et ego, inquit, dico vobis, facite vobis amicos de mammona iniustitiae, de nummo scilicet de quo et servus ille."')]),
 U('16:10', G('16:10'), 'The one who is trustworthy in the least is trustworthy also in much, and the one who is unjust in the least is unjust also in much.', 'Inside the attested paragraph 16:10–12.'),
 A('16:11', G('16:11'), 'If then you have not been trustworthy with the unjust Mammon, who will entrust the true to you?',
   'present (Marc. 4.33.4)', [T('4.33.4', '"Si in mammona iniusto fideles non extitistis, quod verum est quis vobis credet?"')]),
 A('16:12', G('16:12', [('τὸ ὑμέτερον', 'τὸ ἐμὸν')]),
   'And if you have not been trustworthy with what belongs to another, who will give you what is mine?',
   'present (Marc. 4.33.4)', [T('4.33.4', '"Et si in alieno fideles inventi non estis, meum quis dabit vobis?… Quis vobis dabit quod meum est?"')],
   wording='Marcionite reading adopted: τὸ ἐμόν ("what is mine") for τὸ ὑμέτερον ("what is your own"). Tertullian quotes it twice; Roth: very likely. NA27 apparatus: ἐμόν 157 e i l; McionT. NA27 has τίς ὑμῖν δώσει (SBLGNT τίς δώσει ὑμῖν — checked on the page image).',
   western='"Mine" is also the reading of the Old Latin e i l.'),
 A('16:13', G('16:13'), 'No household slave can be a slave to two lords; for either he will hate the one and love the other, or he will hold to one and despise the other. You cannot be a slave to God and to Mammon."',
   'present (Marc. 4.33.1–3; Adam. 56,11–12)', [T('4.33.2', '"Non potestis deo servire et mammonae."'),
                                                 T('4.33.1', '"Quibus duobus dominis neget posse serviri quia alterum offendi sit necesse alterum defendi, ipse declarat deum proponens et mammonam."')]),
 A('16:14', G('16:14'), 'And the Pharisees, being lovers of silver, were hearing all these things, and they were turning up their noses at him.',
   'present (Marc. 4.33.2)', [T('4.33.2', '"Irridebant denique pharisaei pecuniae cupidi".')]),
 A('16:15', G('16:15'), 'And he said to them, "You are the ones who declare yourselves just before the humans, but God knows your hearts; because what is high among humans is an abomination before God.',
   'present (Marc. 4.33.6)', [T('4.33.6', '"Si autem et iustificantes se coram hominibus pharisaei… Si et adicit, Scit autem deus corda vestra… Quod elatum est apud homines perosum est deo".')]),
 A('16:16', G('16:16'), 'The law and the prophets were until John; from then the kingdom of God is announced as good news, and everyone forces his way into it.',
   'present (Marc. 4.33.7; Pan. 42.11.6, sch. 43)',
   [E(43, '»ὁ νόμος καὶ οἱ προφῆται ἕως Ἰωάννου καὶ πᾶς εἰς αὐτὴν βιάζεται«.'),
    T('4.33.7', '"Lex et prophetae usque ad Ioannem, ex quo regnum dei annuntiatur."')],
   wording='NA27. Epiphanius has ἕως for μέχρι, the reading of A D W Θ Ψ and the Byzantine text; Roth: probable only.'),
 A('16:17', G('16:17', [('ἢ τοῦ νόμου μίαν κεραίαν πεσεῖν', 'ἢ τῶν λόγων μου μίαν κεραίαν πεσεῖν')]),
   'But it is easier for the sky and the earth to pass away than for one stroke of a letter of my words to fall.',
   'present (Marc. 4.33.9)',
   [T('4.33.9', '"Transeat igitur caelum et terra citius, sicut et lex et prophetae, quam unus apex verborum domini… ideo subtexuit facilius elementa transitura quam verba sua".')],
   wording=('Marcionite reading adopted, against Roth\'s grade (probable): "of my words" (τῶν λόγων μου) for "of the law" (τοῦ νόμου). NA27 apparatus: τῶν λόγων μου McionT. '
            'Tertullian twice says that the saying concerns Christ\'s own words ("verborum domini", "verba sua"), and treats the law and the prophets as what passes. His thesis in 4.33.7–9 is that Christ fulfilled the law and did not destroy it. Canonical Luke\'s "easier for heaven and earth to pass than for one stroke of the law to fall" would have been his strongest proof, and he does not use it; instead he has to reconcile the saying with the law by way of Isaiah 40:8. '
            'Roth allows that Tertullian may be echoing Luke 21:33 and Isa 40:8; that would not explain why he passes over the wording that best served him. Departure from Roth recorded in the audit log. The Greek printed keeps NA27\'s construction (πεσεῖν) and replaces only the genitive.')),
 A('16:18', G('16:18'), 'Everyone who releases his wife and marries another commits adultery, and the one who marries a woman released from a husband commits adultery.',
   'present (Marc. 4.34.1, 4, 9)', [T('4.34.1', '"Sed Christus divortium prohibet dicens, Qui dimiserit uxorem suam et aliam duxerit, adulterium committit; qui dimissam a viro duxerit, aeque adulter est."')],
   wording='NA27, without the second πᾶς (NA27 cites McionT with 𝔓75 B D L for the shorter text). Tertullian\'s "likewise is an adulterer" is rated possible only.'),
 A('16:19', G('16:19'), 'There was a certain rich man, and he dressed in purple and fine linen, making merry every day splendidly.',
   'present (Pan. 42.11.6, sch. 44; Adam. 76,16–17)', [E(44, 'περὶ τοῦ πλουσίου καὶ Λαζάρου τοῦ πτωχοῦ…'),
                                                     AD('76,16–17 (2.10)', 'ἄνθρωπός τις ἦν πλούσιος καὶ ἐνεδιδύσκετο πορφύραν καὶ βύσσον, εὐφραινόμενος καθ᾿ ἡμέραν λαμπρῶς.')]),
 A('16:20', G('16:20'), 'And a certain destitute man, named Lazarus, had been thrown down at his gateway, covered with sores,',
   'present (Pan. 42.11.6, sch. 44; Adam. 76,17–18)', [E(44, '…Λαζάρου τοῦ πτωχοῦ'), AD('76,17–18 (2.10)', 'πτωχὸς δέ τις ὀνόματι Λάζαρος ἐβέβλητο…')]),
 A('16:21', G('16:21'), "and longing to be fed from what fell from the rich man's table; but even the dogs would come and lick his sores.",
   ADAM, [AD('76,19–21 (2.10)', 'καὶ ἐπιθυμῶν χορτασθῆναι ἀπὸ τῶν πιπτόντων ἀπὸ τῆς τραπέζης τοῦ πλουσίου· ἀλλὰ καὶ οἱ κύνες ἐρχόμενοι ἔλειχον τὰ τραύματα αὐτοῦ.')]),
 A('16:22', G('16:22'), 'And it happened that the destitute man died and was carried away by the messengers into the bosom of Abraham. And the rich man also died and was buried.',
   'present (Marc. 4.34.10–11; Pan. 42.11.6, sch. 44; Adam. 76,21–23)',
   [E(44, 'περὶ τοῦ πλουσίου καὶ Λαζάρου τοῦ πτωχοῦ, ὅτι ἀπηνέχθη ὑπὸ τῶν ἀγγέλων εἰς τὸν κόλπον τοῦ Ἀβραάμ.'),
    T('4.34.10', '"divitis apud inferos dolentis et pauperis in sinu Abrahae requiescentis".')]),
 A('16:23', G('16:23', [('ἐν τοῖς κόλποις αὐτοῦ', 'ἐν τῷ κόλπῳ αὐτοῦ')]),
   'And in Hades, lifting up his eyes, being in torments, he sees Abraham from far off, and Lazarus in his bosom.',
   'present (Marc. 4.34.10–12; Adam. 76,23–25)',
   [T('4.34.12', '"Sed nec allevasset dives oculos, et quidem de longinquo…"; 4.34.11 "quae ab inferis discernit Abrahae sinum pauperi".'),
    AD('76,23–25 (2.10)', '…ἐν τῷ ᾅδῃ ἐπάρας τοὺς ὀφθαλμοὺς αὐτοῦ… ὁρᾷ Ἀβραὰμ ἀπὸ μακρόθεν καὶ Λάζαρον ἐν τῷ κόλπῳ αὐτοῦ.')],
   wording='Marcionite reading adopted: the singular ἐν τῷ κόλπῳ ("in his bosom") for NA27\'s plural ἐν τοῖς κόλποις. Tertullian ("sinus") and the Adamantius Dialogue; Roth: secure. The singular is also the reading of D and every Old Latin manuscript except d and e.',
   western='The singular is the reading of D and the Old Latin.'),
 A('16:24', G('16:24'), "And he called out and said, 'Father Abraham, have mercy on me, and send Lazarus to dip the tip of his finger in water and cool my tongue, because I am in anguish in this flame.'",
   ADAM, [AD('76,26–29 (2.10)', 'καὶ αὐτὸς φωνήσας εἶπεν· πάτερ Ἀβραάμ, ἐλέησόν με καὶ πέμψον Λάζαρον…')]),
 A('16:25', G('16:25'), "But Abraham said, 'Child, remember that you received your good things in full in your life, and Lazarus in the same way the bad things; but now here he is comforted, and you are in anguish.",
   'present (Pan. 42.11.6, sch. 45; Adam. 76,29–31)', [E(45, '»νῦν δὲ ὧδε παρακαλεῖται« ὁ αὐτὸς Λάζαρος.')],
   wording='NA27. NA27 cites McionA,E for ὅδε ("this one") for ὧδε ("here"); the difference is one of breathing and accent, which the manuscripts of Epiphanius do not settle. Roth: possible only.'),
 A('16:26', G('16:26'), "And in all these things, between us and you a great chasm has been fixed, so that those who want to cross from here to you cannot, nor may anyone pass over from there to us.'",
   'present (Marc. 4.34.11; Adam. 76,31–34)', [T('4.34.11', '"Nam et magnum ait intercidere regiones istas profundum et transitum utrinque prohibere."')]),
 A('16:27', G('16:27'), "And he said, 'Then I ask you, father, to send him to the house of my father,",
   ADAM, [AD('76,34–35 (2.10)', 'ἐρωτῶ οὖν σε, πάτερ, ἵνα πέμψῃς αὐτὸν εἰς τὴν οἰκίαν τοῦ πατρός μου·')]),
 A('16:28', G('16:28'), "for I have five brothers, so that he may bear full witness to them, so that they too may not come into this place of torment.'",
   ADAM, [AD('76,35–78,2 (2.10)', 'ἔχω γὰρ ἐκεῖ πέντε ἀδελφούς· ὅπως διαμαρτύρηται αὐτοῖς…')]),
 A('16:29', G('16:29'), "But Abraham says, 'They have Moses and the prophets; let them hear them.'",
   'present (Marc. 4.34.10, 17; Pan. 42.11.6, sch. 46; Adam. 78,2–3)',
   [E(46, 'εἶπεν Ἀβραάμ »ἔχουσι Μωυσέα καὶ τοὺς προφήτας, ἀκουσάτωσαν αὐτῶν«.'),
    T('4.34.17', '"Habent illic Moysen et prophetas, audiant illos."')]),
 A('16:30', G('16:30'), "But he said, 'No, father Abraham, but if someone from the dead goes to them, they will change their minds.'",
   ADAM, [AD('78,3–5 (2.10)', 'ὁ δὲ εἶπεν· οὐχί, πάτερ… ἀλλ᾿ ἐάν τις ἐκ νεκρῶν πορευθῇ πρὸς αὐτούς, μετανοήσουσιν.')]),
 A('16:31', G('16:31'), 'But he said to him, \'If they do not hear Moses and the prophets, neither will they be persuaded if someone stands up from the dead.\'"',
   'present (Pan. 42.11.6, sch. 46; Adam. 78,5–6)',
   [E(46, '»…ἐπεὶ οὐδὲ τοῦ ἐγειρομένου ἐκ νεκρῶν ἀκούσουσιν«.'),
    AD('78,5–6 (2.10)', 'εἰ Μωϋσέως καὶ τῶν προφητῶν οὐκ ἤκουσαν, οὐδ᾿ ἄν τις ἐκ νεκρῶν ἀπέλθῃ ἀκούσουσιν αὐτοῦ.')],
   wording='NA27. Epiphanius gives a short form ("for they will not listen even to one raised from the dead") and the Dialogue a longer one with ἀπέλθῃ ("goes", NA27: McionA with W it sys.c); both rated probable at best. Not adopted.'),
]

OMITTED = []

PREAMBLE = (
 "Money is the subject, and the chapter refuses to be simple about it. A steward accused of scattering his "
 "master's goods, about to lose his post, cuts down the debts of everyone who owes his master, and is praised "
 "for it. Make friends out of the Mammon of injustice. Whoever is trustworthy in the least is trustworthy in "
 "much. No one can be a slave to two lords. The Pharisees, lovers of silver, turn up their noses. Then a turning"
 " point, stated in a single line: the law and the prophets were until John; from then the kingdom of God is "
 "announced. And here what will not pass away is not a stroke of the law but a stroke of his words. The chapter "
 "ends with two men and a gateway. One dresses in purple and feasts every day; the other lies at the gate "
 "covered with sores, and the dogs lick them. Both die. Watch where each is carried, and what becomes of the "
 "space between them."
)

NOTES = [
 dict(term='The steward (16:1–9)', cat='textual', refs=['16:1', '16:2', '16:4', '16:5', '16:8', '16:9'], text=(
  "Tertullian, Marc. 4.33.1 summarizes the parable: the slave removed from his post relieves his master's debtors by "
  "reducing their bonds, to provide for himself. He then quotes \"And I tell you, make friends for yourselves of the mammon of "
  "injustice\" and explains mammon as money. The previous version marked 16:1–8 as \"conflicting evidence\"; the "
  "parable is attested. 16:1, 16:3 and 16:8 are not cited and are printed in grey.")),
 dict(term='God and mammon (16:10–15)', cat='textual', refs=['16:10', '16:11', '16:12', '16:13', '16:14', '16:15'], text=(
  "Tertullian, Marc. 4.33.1–6. \"You cannot be a slave to God and to Mammon\": he argues that the two masters are God and money, not the "
  "Creator and another God, so that one God is named. He quotes 16:11–12 in the form \"who will give you what is mine?\", "
  "which he reads as Christ's own. That reading, \"mine\" for \"your own\", is printed; it is also in three Old Latin "
  "manuscripts. 16:10 is not cited and is printed in grey.")),
 dict(term='"One stroke of a letter of my words" (16:16–17)', cat='textual', refs=['16:16', '16:17'], text=(
  "Epiphanius, sch. 43 and Tertullian 4.33.7 quote \"The law and the prophets were until John\". On 16:17 Tertullian writes: "
  "\"Let heaven and earth pass away sooner, as the law and the prophets also did, than one stroke of the words of the Lord\", "
  "and \"he added that the elements would pass more easily than his words\". NA27 cites this as Marcion's reading (τῶν λόγων "
  "μου, \"of my words\"). Roth rates it probable only, allowing for the influence of 21:33 (\"my words will not pass away\") and "
  "Isa 40:8. The audit prints it, for a reason in Tertullian's argument. He sets out to show that Christ fulfilled the law and "
  "did not destroy it. Canonical Luke's \"one stroke of the law\" would have proved that directly, and he does not use it. He "
  "had to deal with a text in which what does not pass away is Christ's word, and the law and the prophets are what has come "
  "to an end with John.")),
 dict(term='Divorce and Herod (16:18)', cat='textual', refs=['16:18'], text=(
  "Tertullian, Marc. 4.34.1–9 quotes the saying twice. He argues that it forbids divorce for the purpose of remarriage and so "
  "agrees with Moses, and he connects it with John's rebuke of Herod, who married his brother's wife. He reports that the "
  "Marcionites refused baptism to the married unless they renounced marriage (4.34.5); that is their practice, not the text.")),
 dict(term='The rich man and Lazarus (16:19–31)', cat='textual', refs=['16:19', '16:22', '16:23', '16:25', '16:26', '16:29', '16:31'], text=(
  "Three witnesses attest the parable. Epiphanius, sch. 44–46: Lazarus carried by the messengers to Abraham's bosom, \"now here he is "
  "comforted\", \"they have Moses and the prophets; let them hear them\". Tertullian, Marc. 4.34.10–17: the rich man "
  "in torment in Hades, the great chasm, Lazarus in the bosom of Abraham. The Dialogue of Adamantius (76–78) quotes the whole "
  "parable, but Roth rates its wording probable only. The singular \"in his bosom\" (16:23), with Tertullian, the Dialogue, D "
  "and the Old Latin, is printed. 16:21, 16:24, 16:27–28 and 16:30 rest on the Dialogue alone. They are printed as part of "
  "the attested parable, in the NA27 wording.")),
 dict(term='Hades and Abraham\'s bosom', cat='theological', refs=['16:22', '16:23', '16:26', '16:29'], text=(
  "Reception and interpretation. The Marcionite reading, which Tertullian reports, was that both torment and rest \"in the "
  "underworld\" are the Creator's reward for those who obey the law and the prophets, while Christ's heaven is elsewhere "
  "(4.34.11). Tertullian replies that the text itself distinguishes Abraham's bosom from Hades by a great chasm, and he calls "
  "Abraham's bosom a temporary place of rest for the souls of the righteous until the resurrection (4.34.13). The attested "
  "text describes a state after death that follows at once on the life lived: the destitute man is carried to Abraham, the "
  "rich man is in torment, and the two are separated. It does not speak of a later resurrection. To the request for a "
  "messenger from the dead, the parable answers with \"Moses and the prophets\".")),
 dict(term='οἰκονόμον, "steward"', cat='translation', refs=['16:1'], text='The manager of a household or estate. οἰκονομία, "stewardship" (16:2–4), is his office.'),
 dict(term='διεβλήθη, "was accused"', cat='translation', refs=['16:1'], text='διαβάλλω, to accuse, to slander. It is the verb behind διάβολος, "the slanderer".'),
 dict(term='διασκορπίζων, "scattering"', cat='translation', refs=['16:1'], text='To scatter, squander.'),
 dict(term='ἀπόδος τὸν λόγον, "give back the account"', cat='translation', refs=['16:2'], text='λόγος here is an account, a reckoning.'),
 dict(term='ὁ κύριός μου, "my lord"', cat='translation', refs=['16:3'], text='His owner, as at 12:36.'),
 dict(term='σκάπτειν… ἐπαιτεῖν, "to dig… to beg"', cat='translation', refs=['16:3'], text='ἐπαιτέω, to beg. The destitute (πτωχοί) are those who must beg.'),
 dict(term='μετασταθῶ, "I am removed"', cat='translation', refs=['16:4'], text='To be moved out, deposed.'),
 dict(term='βάτους, "baths"', cat='translation', refs=['16:6'], text='A Hebrew liquid measure (bath), about 22 litres.'),
 dict(term='τὰ γράμματα, "your writings"', cat='translation', refs=['16:6'], text='The written bond, the bill.'),
 dict(term='κόρους, "kors"', cat='translation', refs=['16:7'], text='A Hebrew dry measure (kor), about 220 litres.'),
 dict(term='λέγει, "he says"', cat='translation', refs=['16:7'], text='The present tense, kept.'),
 dict(term='ὁ κύριος, "the lord"', cat='translation', refs=['16:8'], text="Either the steward's lord in the parable, or Jesus (as at 7:13). The Greek does not decide."),
 dict(term='τὸν οἰκονόμον τῆς ἀδικίας, "the steward of injustice"', cat='translation', refs=['16:8'], text='A Semitic genitive, usually rendered "the dishonest steward". ἀδικία, as at 13:27.'),
 dict(term='φρονίμως, "sensibly"', cat='translation', refs=['16:8'], text='φρόνιμος, as at 12:42: shrewd, prudent.'),
 dict(term='οἱ υἱοὶ τοῦ αἰῶνος τούτου, "the sons of this age"', cat='translation', refs=['16:8'], text='αἰών, age. The Semitic "sons of" means those who belong to it.'),
 dict(term='μαμωνᾶ, "Mammon"', cat='translation', refs=['16:9'], text='An Aramaic word for wealth, property, left untranslated in the Greek, and so here.'),
 dict(term='ἐκλίπῃ, "it gives out"', cat='translation', refs=['16:9'], text='To fail, come to an end.'),
 dict(term='τὰς αἰωνίους σκηνάς, "the tents of the age"', cat='translation', refs=['16:9'], text='αἰώνιος, belonging to the age. "Eternal" turns it into endless time.'),
 dict(term='πιστός, "trustworthy"', cat='translation', refs=['16:10'], text='As at 12:42.'),
 dict(term='τὸ ἀληθινόν… πιστεύσει, "the true… will entrust"', cat='translation', refs=['16:11'], text='πιστεύω here is "entrust": the word of trust.'),
 dict(term='τὸ ἐμόν, "what is mine"', cat='translation', refs=['16:12'], text='The reading of this text. Canonical Luke has τὸ ὑμέτερον, "what is yours".'),
 dict(term='οἰκέτης, "household slave"', cat='translation', refs=['16:13'], text='A slave of the house, kept apart from δοῦλος.'),
 dict(term='δουλεύειν, "be a slave to"', cat='translation', refs=['16:13'], text='The verb of δοῦλος. "Serve" softens it.'),
 dict(term='ἀνθέξεται… καταφρονήσει, "hold to… despise"', cat='translation', refs=['16:13'], text='To cling to; to look down on.'),
 dict(term='φιλάργυροι, "lovers of silver"', cat='translation', refs=['16:14'], text='One word: silver-loving.'),
 dict(term='ἐξεμυκτήριζον, "were turning up their noses at"', cat='translation', refs=['16:14'], text='From μυκτήρ, "nose": to sneer at.'),
 dict(term='οἱ δικαιοῦντες ἑαυτούς, "who declare yourselves just"', cat='translation', refs=['16:15'], text='δικαιόω, to declare just, from δίκαιος.'),
 dict(term='βδέλυγμα, "abomination"', cat='translation', refs=['16:15'], text='Something loathsome, detestable.'),
 dict(term='βιάζεται, "forces his way"', cat='translation', refs=['16:16'], text='The verb can be middle ("forces his way in") or passive ("is pressed to enter"). Both readings are old.'),
 dict(term='κεραίαν, "one stroke of a letter"', cat='translation', refs=['16:17'], text='Literally "a little horn", a small stroke of the pen.'),
 dict(term='τῶν λόγων μου, "of my words"', cat='translation', refs=['16:17'], text='The reading of this text. Canonical Luke has "of the law".'),
 dict(term='ἀπολύων τὴν γυναῖκα αὐτοῦ, "who releases his wife"', cat='translation', refs=['16:18'], text='ἀπολύω, to release, set free, dismiss, as at 6:37 and 13:12. "Divorce" is what it means here; the Greek uses the general word of release.'),
 dict(term='μοιχεύει, "commits adultery"', cat='translation', refs=['16:18'], text='To commit adultery.'),
 dict(term='πορφύραν καὶ βύσσον, "purple and fine linen"', cat='translation', refs=['16:19'], text='Purple cloth and fine Egyptian linen: the clothing of the very rich.'),
 dict(term='εὐφραινόμενος, "making merry"', cat='translation', refs=['16:19'], text='εὐφραίνω, as at 12:19.'),
 dict(term='πτωχός, "a destitute man"', cat='translation', refs=['16:20'], text='As at 6:20.'),
 dict(term='ἐβέβλητο, "had been thrown down"', cat='translation', refs=['16:20'], text='βάλλω, a pluperfect passive: he lay where he had been thrown.'),
 dict(term='εἱλκωμένος, "covered with sores"', cat='translation', refs=['16:20'], text='Ulcerated.'),
 dict(term='ἐπιθυμῶν χορτασθῆναι, "longing to be fed"', cat='translation', refs=['16:21'], text='χορτάζω, fed full, as at 6:21.'),
 dict(term='ἐπέλειχον, "would… lick"', cat='translation', refs=['16:21'], text='The imperfect: they kept licking.'),
 dict(term='ἀπενεχθῆναι ὑπὸ τῶν ἀγγέλων, "was carried away by the messengers"', cat='translation', refs=['16:22'], text='ἄγγελος, as at 9:26.'),
 dict(term='εἰς τὸν κόλπον Ἀβραάμ, "into the bosom of Abraham"', cat='translation', refs=['16:22'], text='κόλπος, the chest, the fold of the garment there (6:38): the place of the honoured guest reclining at a meal.'),
 dict(term='ἐν τῷ ᾅδῃ, "in Hades"', cat='translation', refs=['16:23'], text='The Greek name for the realm of the dead (Hebrew sheol). "Hell" imports a later picture.'),
 dict(term='ὁρᾷ, "he sees"', cat='translation', refs=['16:23'], text='The present tense, kept.'),
 dict(term='βασάνοις, "torments"', cat='translation', refs=['16:23'], text='As at 8:28.'),
 dict(term='ἐλέησόν με, "have mercy on me"', cat='translation', refs=['16:24'], text='ἐλεέω, to have pity, show mercy.'),
 dict(term='ὀδυνῶμαι, "I am in anguish"', cat='translation', refs=['16:24'], text='To suffer pain, grief.'),
 dict(term='ἀπέλαβες, "you received… in full"', cat='translation', refs=['16:25'], text='To receive back, receive what is due.'),
 dict(term='παρακαλεῖται, "he is comforted"', cat='translation', refs=['16:25'], text='παρακαλέω, the verb behind παράκλησις, "comfort" (6:24): the rich had their comfort in full.'),
 dict(term='ἐστήρικται, "has been fixed"', cat='translation', refs=['16:26'], text='στηρίζω, as at 9:51.'),
 dict(term='διαμαρτύρηται, "bear full witness"', cat='translation', refs=['16:28'], text='To testify thoroughly, warn.'),
 dict(term='ἀκουσάτωσαν, "let them hear"', cat='translation', refs=['16:29'], text='ἀκούω, to hear, listen to, obey.'),
 dict(term='μετανοήσουσιν, "they will change their minds"', cat='translation', refs=['16:30'], text='μετανοέω, as at 15:7.'),
 dict(term='ἀναστῇ, "stands up"', cat='translation', refs=['16:31'], text='ἀνίστημι, to stand up, rise.'),
 dict(term='πεισθήσονται, "will they be persuaded"', cat='translation', refs=['16:31'], text='πείθω, to persuade.'),
]
