"""Batch 4, chapter 14 of the reconstruction: Luke 16:1–31."""
from buildlib import greek
from batch1_ch2 import U, A
from batch4_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}
AD = lambda loc, ev: {'source': f'Dialogue of Adamantius {loc} (via Roth)', 'evidence': ev}
ADAM = 'present (Adam. 76,16–78,6; Roth: wording probable only)'

ENTRIES = [
 U('16:1', G('16:1'), 'He also said to the disciples, "There was a rich man who had a steward, and charges were brought to him that this man was squandering his property.', 'Opens the attested parable 16:1–9.'),
 A('16:2', G('16:2'), 'So he called him and said to him, \'What is this I hear about you? Give an account of your stewardship, for you can no longer be steward.\'',
   'present (Marc. 4.33.1)', [T('4.33.1', '"secundum servi illius exemplum, qui ab actu summotus…"')], wording='NA27. Roth: attested, but no insight into the wording.'),
 U('16:3', G('16:3'), 'And the steward said to himself, \'What shall I do, since my master is taking the stewardship away from me? I am not strong enough to dig, and I am ashamed to beg.', 'Inside the attested parable 16:1–9.'),
 A('16:4', G('16:4'), 'I have decided what to do, so that when I am removed from the stewardship, people will receive me into their houses.\'',
   'present (Marc. 4.33.1)', [T('4.33.1', '"in subsidium sibi" — the steward providing for himself.')], wording='NA27. Roth: attested, but no insight into the wording.'),
 A('16:5', G('16:5'), 'So, summoning his master\'s debtors one by one, he said to the first, \'How much do you owe my master?\'',
   'present (Marc. 4.33.1)', [T('4.33.1', '"dominicos debitores deminutis cautionibus relevat".')], wording='NA27. Roth: attested, but no insight into the wording.'),
 A('16:6', G('16:6'), 'He said, \'A hundred measures of oil.\' He said to him, \'Take your bill, sit down quickly and write fifty.\'',
   'present (Marc. 4.33.1)', [T('4.33.1', '"deminutis cautionibus" — reducing the written bonds.')], wording='NA27. Roth: attested, but no insight into the wording.'),
 A('16:7', G('16:7'), 'Then he said to another, \'And how much do you owe?\' He said, \'A hundred measures of wheat.\' He said to him, \'Take your bill and write eighty.\'',
   'present (Marc. 4.33.1)', [T('4.33.1', '"deminutis cautionibus".')], wording='NA27. Roth: attested, but no insight into the wording.'),
 U('16:8', G('16:8'), 'And the master praised the dishonest steward for acting shrewdly; for the sons of this age are shrewder in dealing with their own generation than the sons of light.', 'Inside the attested parable 16:1–9.'),
 A('16:9', G('16:9'), 'And I tell you, make friends for yourselves by means of the mammon of injustice, so that when it fails they may receive you into the eternal dwellings.',
   'present for 16:9a (Marc. 4.33.1); 16:9b unattested', [T('4.33.1', '"Et ego, inquit, dico vobis, facite vobis amicos de mammona iniustitiae, de nummo scilicet de quo et servus ille."')]),
 U('16:10', G('16:10'), 'Whoever is faithful in a very little is faithful also in much, and whoever is dishonest in a very little is dishonest also in much.', 'Inside the attested paragraph 16:10–12.'),
 A('16:11', G('16:11'), 'If then you have not been faithful in the unjust mammon, who will entrust to you the true riches?',
   'present (Marc. 4.33.4)', [T('4.33.4', '"Si in mammona iniusto fideles non extitistis, quod verum est quis vobis credet?"')]),
 A('16:12', G('16:12', [('τὸ ὑμέτερον', 'τὸ ἐμὸν')]),
   'And if you have not been faithful in what belongs to another, who will give you what is mine?',
   'present (Marc. 4.33.4)', [T('4.33.4', '"Et si in alieno fideles inventi non estis, meum quis dabit vobis?… Quis vobis dabit quod meum est?"')],
   wording='Marcionite reading adopted: τὸ ἐμόν ("what is mine") for τὸ ὑμέτερον ("what is your own"). Tertullian quotes it twice; Roth: very likely. NA27 apparatus: ἐμόν 157 e i l; McionT. NA27 has τίς ὑμῖν δώσει (SBLGNT τίς δώσει ὑμῖν — checked on the page image).',
   western='"Mine" is also the reading of the Old Latin e i l.'),
 A('16:13', G('16:13'), 'No servant can serve two masters; for either he will hate the one and love the other, or he will be devoted to the one and despise the other. You cannot serve God and mammon."',
   'present (Marc. 4.33.1–3; Adam. 56,11–12)', [T('4.33.2', '"Non potestis deo servire et mammonae."'),
                                                 T('4.33.1', '"Quibus duobus dominis neget posse serviri quia alterum offendi sit necesse alterum defendi, ipse declarat deum proponens et mammonam."')]),
 A('16:14', G('16:14'), 'The Pharisees, who were lovers of money, heard all this, and they ridiculed him.',
   'present (Marc. 4.33.2)', [T('4.33.2', '"Irridebant denique pharisaei pecuniae cupidi".')]),
 A('16:15', G('16:15'), 'And he said to them, "You are those who justify yourselves before people, but God knows your hearts; for what is exalted among people is an abomination before God.',
   'present (Marc. 4.33.6)', [T('4.33.6', '"Si autem et iustificantes se coram hominibus pharisaei… Si et adicit, Scit autem deus corda vestra… Quod elatum est apud homines perosum est deo".')]),
 A('16:16', G('16:16'), 'The law and the prophets were until John; since then the kingdom of God is proclaimed as good news, and everyone forces his way into it.',
   'present (Marc. 4.33.7; Pan. 42.11.6, sch. 43)',
   [E(43, '»ὁ νόμος καὶ οἱ προφῆται ἕως Ἰωάννου καὶ πᾶς εἰς αὐτὴν βιάζεται«.'),
    T('4.33.7', '"Lex et prophetae usque ad Ioannem, ex quo regnum dei annuntiatur."')],
   wording='NA27. Epiphanius has ἕως for μέχρι, the reading of A D W Θ Ψ and the Byzantine text; Roth: probable only.'),
 A('16:17', G('16:17', [('ἢ τοῦ νόμου μίαν κεραίαν πεσεῖν', 'ἢ τῶν λόγων μου μίαν κεραίαν πεσεῖν')]),
   'But it is easier for heaven and earth to pass away than for one stroke of my words to fall.',
   'present (Marc. 4.33.9)',
   [T('4.33.9', '"Transeat igitur caelum et terra citius, sicut et lex et prophetae, quam unus apex verborum domini… ideo subtexuit facilius elementa transitura quam verba sua".')],
   wording=('Marcionite reading adopted, against Roth\'s grade (probable): "of my words" (τῶν λόγων μου) for "of the law" (τοῦ νόμου). NA27 apparatus: τῶν λόγων μου McionT. '
            'Tertullian twice says that the saying concerns Christ\'s own words ("verborum domini", "verba sua"), and treats the law and the prophets as what passes. His thesis in 4.33.7–9 is that Christ fulfilled the law and did not destroy it. Canonical Luke\'s "easier for heaven and earth to pass than for one stroke of the law to fall" would have been his strongest proof, and he does not use it; instead he has to reconcile the saying with the law by way of Isaiah 40:8. '
            'Roth allows that Tertullian may be echoing Luke 21:33 and Isa 40:8; that would not explain why he passes over the wording that best served him. Departure from Roth recorded in the audit log. The Greek printed keeps NA27\'s construction (πεσεῖν) and replaces only the genitive.')),
 A('16:18', G('16:18'), 'Everyone who divorces his wife and marries another commits adultery, and he who marries a woman divorced from her husband commits adultery.',
   'present (Marc. 4.34.1, 4, 9)', [T('4.34.1', '"Sed Christus divortium prohibet dicens, Qui dimiserit uxorem suam et aliam duxerit, adulterium committit; qui dimissam a viro duxerit, aeque adulter est."')],
   wording='NA27, without the second πᾶς (NA27 cites McionT with 𝔓75 B D L for the shorter text). Tertullian\'s "likewise is an adulterer" is rated possible only.'),
 A('16:19', G('16:19'), 'There was a rich man who was clothed in purple and fine linen and feasted splendidly every day.',
   'present (Pan. 42.11.6, sch. 44; Adam. 76,16–17)', [E(44, 'περὶ τοῦ πλουσίου καὶ Λαζάρου τοῦ πτωχοῦ…'),
                                                     AD('76,16–17 (2.10)', 'ἄνθρωπός τις ἦν πλούσιος καὶ ἐνεδιδύσκετο πορφύραν καὶ βύσσον, εὐφραινόμενος καθ᾿ ἡμέραν λαμπρῶς.')]),
 A('16:20', G('16:20'), 'And at his gate lay a poor man named Lazarus, covered with sores,',
   'present (Pan. 42.11.6, sch. 44; Adam. 76,17–18)', [E(44, '…Λαζάρου τοῦ πτωχοῦ'), AD('76,17–18 (2.10)', 'πτωχὸς δέ τις ὀνόματι Λάζαρος ἐβέβλητο…')]),
 A('16:21', G('16:21'), 'longing to be fed with what fell from the rich man\'s table; and even the dogs came and licked his sores.',
   ADAM, [AD('76,19–21 (2.10)', 'καὶ ἐπιθυμῶν χορτασθῆναι ἀπὸ τῶν πιπτόντων ἀπὸ τῆς τραπέζης τοῦ πλουσίου· ἀλλὰ καὶ οἱ κύνες ἐρχόμενοι ἔλειχον τὰ τραύματα αὐτοῦ.')]),
 A('16:22', G('16:22'), 'The poor man died and was carried by the angels to Abraham\'s bosom. The rich man also died and was buried.',
   'present (Marc. 4.34.10–11; Pan. 42.11.6, sch. 44; Adam. 76,21–23)',
   [E(44, 'περὶ τοῦ πλουσίου καὶ Λαζάρου τοῦ πτωχοῦ, ὅτι ἀπηνέχθη ὑπὸ τῶν ἀγγέλων εἰς τὸν κόλπον τοῦ Ἀβραάμ.'),
    T('4.34.10', '"divitis apud inferos dolentis et pauperis in sinu Abrahae requiescentis".')]),
 A('16:23', G('16:23', [('ἐν τοῖς κόλποις αὐτοῦ', 'ἐν τῷ κόλπῳ αὐτοῦ')]),
   'And in Hades, being in torment, he lifted up his eyes and saw Abraham far off and Lazarus in his bosom.',
   'present (Marc. 4.34.10–12; Adam. 76,23–25)',
   [T('4.34.12', '"Sed nec allevasset dives oculos, et quidem de longinquo…"; 4.34.11 "quae ab inferis discernit Abrahae sinum pauperi".'),
    AD('76,23–25 (2.10)', '…ἐν τῷ ᾅδῃ ἐπάρας τοὺς ὀφθαλμοὺς αὐτοῦ… ὁρᾷ Ἀβραὰμ ἀπὸ μακρόθεν καὶ Λάζαρον ἐν τῷ κόλπῳ αὐτοῦ.')],
   wording='Marcionite reading adopted: the singular ἐν τῷ κόλπῳ ("in his bosom") for NA27\'s plural ἐν τοῖς κόλποις. Tertullian ("sinus") and the Adamantius Dialogue; Roth: secure. The singular is also the reading of D and every Old Latin manuscript except d and e.',
   western='The singular is the reading of D and the Old Latin.'),
 A('16:24', G('16:24'), 'And he called out, \'Father Abraham, have mercy on me, and send Lazarus to dip the tip of his finger in water and cool my tongue, for I am in anguish in this flame.\'',
   ADAM, [AD('76,26–29 (2.10)', 'καὶ αὐτὸς φωνήσας εἶπεν· πάτερ Ἀβραάμ, ἐλέησόν με καὶ πέμψον Λάζαρον…')]),
 A('16:25', G('16:25'), 'But Abraham said, \'Child, remember that you received your good things in your lifetime, and Lazarus likewise bad things; but now he is comforted here, and you are in anguish.',
   'present (Pan. 42.11.6, sch. 45; Adam. 76,29–31)', [E(45, '»νῦν δὲ ὧδε παρακαλεῖται« ὁ αὐτὸς Λάζαρος.')],
   wording='NA27. NA27 cites McionA,E for ὅδε ("this one") for ὧδε ("here"); the difference is one of breathing and accent, which the manuscripts of Epiphanius do not settle. Roth: possible only.'),
 A('16:26', G('16:26'), 'And besides all this, between us and you a great chasm has been fixed, so that those who would pass from here to you cannot, and none may cross from there to us.\'',
   'present (Marc. 4.34.11; Adam. 76,31–34)', [T('4.34.11', '"Nam et magnum ait intercidere regiones istas profundum et transitum utrinque prohibere."')]),
 A('16:27', G('16:27'), 'And he said, \'Then I beg you, father, to send him to my father\'s house,',
   ADAM, [AD('76,34–35 (2.10)', 'ἐρωτῶ οὖν σε, πάτερ, ἵνα πέμψῃς αὐτὸν εἰς τὴν οἰκίαν τοῦ πατρός μου·')]),
 A('16:28', G('16:28'), 'for I have five brothers, so that he may warn them, lest they also come into this place of torment.\'',
   ADAM, [AD('76,35–78,2 (2.10)', 'ἔχω γὰρ ἐκεῖ πέντε ἀδελφούς· ὅπως διαμαρτύρηται αὐτοῖς…')]),
 A('16:29', G('16:29'), 'But Abraham said, \'They have Moses and the prophets; let them listen to them.\'',
   'present (Marc. 4.34.10, 17; Pan. 42.11.6, sch. 46; Adam. 78,2–3)',
   [E(46, 'εἶπεν Ἀβραάμ »ἔχουσι Μωυσέα καὶ τοὺς προφήτας, ἀκουσάτωσαν αὐτῶν«.'),
    T('4.34.17', '"Habent illic Moysen et prophetas, audiant illos."')]),
 A('16:30', G('16:30'), 'And he said, \'No, father Abraham; but if someone goes to them from the dead, they will repent.\'',
   ADAM, [AD('78,3–5 (2.10)', 'ὁ δὲ εἶπεν· οὐχί, πάτερ… ἀλλ᾿ ἐάν τις ἐκ νεκρῶν πορευθῇ πρὸς αὐτούς, μετανοήσουσιν.')]),
 A('16:31', G('16:31'), 'He said to him, \'If they do not listen to Moses and the prophets, neither will they be convinced if someone rises from the dead.\'"',
   'present (Pan. 42.11.6, sch. 46; Adam. 78,5–6)',
   [E(46, '»…ἐπεὶ οὐδὲ τοῦ ἐγειρομένου ἐκ νεκρῶν ἀκούσουσιν«.'),
    AD('78,5–6 (2.10)', 'εἰ Μωϋσέως καὶ τῶν προφητῶν οὐκ ἤκουσαν, οὐδ᾿ ἄν τις ἐκ νεκρῶν ἀπέλθῃ ἀκούσουσιν αὐτοῦ.')],
   wording='NA27. Epiphanius gives a short form ("for they will not listen even to one raised from the dead") and the Dialogue a longer one with ἀπέλθῃ ("goes", NA27: McionA with W it sys.c); both rated probable at best. Not adopted.'),
]

OMITTED = []

PREAMBLE = (
 "Mammon, the law and the rich man. A steward about to be dismissed reduces his master's debtors' bills, and Jesus tells "
 "his disciples to make friends by the mammon of injustice: no one can serve God and mammon. The Pharisees, lovers of money, "
 "ridicule him; he answers that God knows their hearts. \"The law and the prophets were until John; since then the kingdom "
 "of God is proclaimed.\" In this text the next saying is about his own words: \"it is easier for heaven and earth to pass away "
 "than for one stroke of my words to fall\" (Tertullian, Marc. 4.33.9). There follow the saying on divorce, which Tertullian "
 "links to John's rebuke of Herod, and the rich man and Lazarus. The rich man asks for a messenger to his brothers and is "
 "told: \"They have Moses and the prophets; let them listen to them.\""
)

NOTES = [
 dict(term='The steward (16:1–9)', cat='textual', refs=['16:1', '16:2', '16:4', '16:5', '16:8', '16:9'], text=(
  "Tertullian, Marc. 4.33.1 summarizes the parable: the servant removed from his post relieves his master's debtors by "
  "reducing their bonds, to provide for himself. He then quotes \"And I tell you, make friends for yourselves of the mammon of "
  "injustice\" and explains mammon as money. The previous version marked 16:1–8 as \"conflicting evidence\"; the "
  "parable is attested. 16:1, 16:3 and 16:8 are not cited and are printed in grey.")),
 dict(term='God and mammon (16:10–15)', cat='textual', refs=['16:10', '16:11', '16:12', '16:13', '16:14', '16:15'], text=(
  "Tertullian, Marc. 4.33.1–6. \"You cannot serve God and mammon\": he argues that the two masters are God and money, not the "
  "Creator and another God, so that one God is named. He quotes 16:11–12 in the form \"who will give you what is mine?\", "
  "which he reads as Christ's own. That reading, \"mine\" for \"your own\", is printed; it is also in three Old Latin "
  "manuscripts. 16:10 is not cited and is printed in grey.")),
 dict(term='"One stroke of my words" (16:16–17)', cat='textual', refs=['16:16', '16:17'], text=(
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
  "Three witnesses attest the parable. Epiphanius, sch. 44–46: Lazarus carried by the angels to Abraham's bosom, \"now he is "
  "comforted here\", \"they have Moses and the prophets, let them listen to them\". Tertullian, Marc. 4.34.10–17: the rich man "
  "in torment in Hades, the great chasm, Lazarus in the bosom of Abraham. The Dialogue of Adamantius (76–78) quotes the whole "
  "parable, but Roth rates its wording probable only. The singular \"in his bosom\" (16:23), with Tertullian, the Dialogue, D "
  "and the Old Latin, is printed. 16:21, 16:24, 16:27–28 and 16:30 rest on the Dialogue alone. They are printed as part of "
  "the attested parable, in the NA27 wording.")),
 dict(term='Hades and Abraham\'s bosom', cat='theological', refs=['16:22', '16:23', '16:26', '16:29'], text=(
  "Reception and interpretation. The Marcionite reading, which Tertullian reports, was that both torment and rest \"in the "
  "underworld\" are the Creator's reward for those who obey the law and the prophets, while Christ's heaven is elsewhere "
  "(4.34.11). Tertullian replies that the text itself distinguishes Abraham's bosom from Hades by a great chasm, and he calls "
  "Abraham's bosom a temporary place of rest for the souls of the righteous until the resurrection (4.34.13). The attested "
  "text describes a state after death that follows at once on the life lived: the poor man is carried to Abraham, the "
  "rich man is in torment, and the two are separated. It does not speak of a later resurrection. To the request for a "
  "messenger from the dead, the parable answers with \"Moses and the prophets\".")),
]
