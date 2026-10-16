"""Batch 5, chapter 19 of the reconstruction: Luke 21:1–38 (21:7–38 printed)."""
from buildlib import greek
from batch1_ch2 import U, A
from batch5_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}

T393 = T('4.39.3', '"Videamus et quae signa temporibus imponat. Bella, opinor, et regnum super regnum, et gentem super gentem, et pestem, et fames terraeque motus, et formidines, et prodigia de caelo… Haec cum adicit etiam oportere fieri…"')
T399 = T('4.39.9', '"signa iam ultimi finis enarrat, solis et lunae siderumque prodigia, et in terra angustias nationum obstupescentium velut a sonitu maris fluctuantis, pro expectatione imminentium orbi malorum. Quod et ipsae vires caelorum concuti habeant…"')

ENTRIES = [
 A('21:7', G('21:7'), 'And they asked him, saying, "Teacher, when then will these things be, and what is the sign when these things are about to happen?"',
   'present (Marc. 4.39.13)', [T('4.39.13', '"Ipsum decursum scripturae evangelicae ab interrogatione discipulorum usque ad parabolam fici…"')],
   wording='NA27. Tertullian attests the learners\' question, not its wording; Roth rates "the learners" as subject possible only (NA27: οἱ μαθηταί added by D). In this text "these things" has no antecedent, since 21:5–6, the prediction about the temple stones, are not printed.'),
 A('21:8', G('21:8'), 'And he said, "Look out that you are not led astray; for many will come upon my name, saying, \'I am,\' and, \'The time has come near.\' Do not journey after them.',
   'present (Marc. 4.39.1–2)', [T('4.39.1', '"…qui multos dicat venturos in nomine ipsius… amplius et prohibeat eos recipi…"'), T('4.39.2', '"Venient denique illi dicentes, Ego sum Christus."')],
   wording='NA27. Tertullian\'s "I am the Christ" is Matthew\'s wording (Matt 24:5); Roth: possible only.'),
 A('21:9', G('21:9'), 'And when you hear of wars and upheavals, do not be terrified; for these things must happen first, but the end is not at once."',
   'present (Marc. 4.39.3)', [T393]),
 A('21:10', G('21:10'), 'Then he was saying to them, "Nation will rise against nation, and kingdom against kingdom,',
   'present (Marc. 4.39.3)', [T393]),
 A('21:11', G('21:11'), 'and there will be great earthquakes, and in place after place famines and plagues, and there will be terrors and great signs from heaven.',
   'present (Marc. 4.39.3)', [T393], wording='NA27 (ἀπ\' οὐρανοῦ σημεῖα; SBLGNT σημεῖα ἀπ\' οὐρανοῦ — checked on the page image).'),
 A('21:12', G('21:12'), 'But before all these things they will lay their hands on you and pursue you, handing you over to the assemblies and prisons, you being led away before kings and governors for the sake of my name.',
   'present (Marc. 4.39.4)', [T('4.39.4', '"Ante haec autem persecutiones eis praedicat et passiones venturas, in martyrium utique et in salutem."')]),
 A('21:13', G('21:13'), 'It will turn out for you as a testimony.',
   'present (Marc. 4.39.4)', [T('4.39.4', '"in martyrium".')]),
 A('21:14', G('21:14'), 'So set it in your hearts not to rehearse beforehand how to answer in defence;',
   'present (Marc. 4.39.6–7)', [T('4.39.6', '"Et hic igitur ipse vetat cogitari quid responderi oporteat apud tribunalia".')]),
 A('21:15', G('21:15'), 'for I will give you a mouth and wisdom, which all who oppose you will not be able to withstand or speak against.',
   'present (Marc. 4.39.6–7)', [T('4.39.6', '"Et sapientiam ipsam, cui nemo resisteret…"')]),
 A('21:16', G('21:16'), 'And you will be handed over even by parents and brothers and relatives and friends, and they will put some of you to death,',
   'present (Marc. 4.39.8)', [T('4.39.8', '"A proximis quoque persecutiones…"')]),
 A('21:17', G('21:17'), 'and you will be hated by all because of my name.',
   'present (Marc. 4.39.8)', [T('4.39.8', '"et nominis ex odio utique blasphemiam praedicatam".')]),
 A('21:19', G('21:19'), 'By your endurance gain your souls.',
   'present (Marc. 4.39.8)', [T('4.39.8', '"Sed per tolerantiam, inquit, salvos facietis vosmetipsos".')],
   wording='NA27. Tertullian\'s "you will save yourselves" (NA27 apparatus: σώσετε McionT) is rated possible only by Roth; not adopted.'),
 A('21:20', G('21:20'), 'But when you see Jerusalem surrounded by armies, then know that its desolation has come near.',
   'present (Marc. 4.39.9)', [T('4.39.9', '"Sed monstrato dehinc tempore excidii, cum coepisset vallari exercitibus Hierusalem…"')]),
 U('21:23', G('21:23'), 'Woe to those who are with child and to those who are nursing in those days; for there will be great distress upon the land and wrath upon this people,', 'Inside the attested paragraph 21:20–24.'),
 U('21:24', G('21:24'), 'and they will fall by the mouth of the sword and be led captive into all the nations, and Jerusalem will be trampled by nations until the times of nations are fulfilled.', 'Inside the attested paragraph 21:20–24.'),
 A('21:25', G('21:25'), 'And there will be signs in sun and moon and stars, and upon the earth anguish of nations in perplexity at the roar of the sea and the surge,',
   'present (Marc. 4.39.9)', [T399]),
 A('21:26', G('21:26'), 'humans fainting from fear and expectation of what is coming upon the inhabited world; for the powers of the heavens will be shaken.',
   'present (Marc. 4.39.9)', [T399]),
 A('21:27', G('21:27', [('ἐρχόμενον ἐν νεφέλῃ μετὰ δυνάμεως καὶ δόξης πολλῆς.', 'ἐρχόμενον ἀπὸ τῶν οὐρανῶν μετὰ δυνάμεως πολλῆς.')]),
   'And then they will see the son of the human coming from the heavens with much power.',
   'present (Marc. 4.39.10–11)',
   [T('4.39.10', '"Post haec quid dominus? Et tunc videbunt filium hominis venientem de caelis cum plurima virtute."'),
    T('4.39.11', '"Hic erit dies magnus domini et illustris, venientis de caelis filii hominis, secundum Danielem: Ecce cum caeli nubibus tanquam filius hominis adveniens…"')],
   wording=('Marcionite reading adopted (retroversion): "coming from the heavens with much power" for NA27 "coming in a cloud with power and great glory". Tertullian quotes the verse as the Lord\'s words ("Post haec quid dominus?", 4.39.10) and repeats "coming from the heavens" (4.39.11); Roth: "from the heavens" very likely, "with power… great" secure, "and glory likely not present". '
            'His Latin "cum plurima virtute" cannot render NA27\'s two nouns. The cloud he brings in himself, from Daniel 7:13, as a separate text. NA27 apparatus: καὶ δυνάμει πολλῇ καὶ δόξῃ D e (sys.c).')),
 A('21:28', G('21:28'), 'But when these things begin to happen, straighten up and lift up your heads, because your release is drawing near."',
   'present (Marc. 4.39.10, 12)', [T('4.39.10', '"Cum autem haec fient, erigetis vos, et levabitis capita, quoniam appropinquavit redemptio vestra".')],
   wording='NA27. Tertullian lacks "your" with "heads"; Roth: likely not present, because Tertullian has "capita vestra" when he cites the verse in Res. 22.6, and D d omit the pronoun (Roth n. 434; not in the NA27 apparatus). Latin can leave the possessive unexpressed, so his "capita" can render NA27 (METHOD §5.4). Printed.'),
 A('21:29', G('21:29'), 'And he told them a parable: "See the fig tree and all the trees;',
   'present (Marc. 4.39.10, 13, 16)', [T('4.39.16', '"In summa ipsius parabolae considera exemplum. Aspice ficum et arbores omnes".')]),
 A('21:30', G('21:30'), 'when they already put out their leaves, seeing it you know from yourselves that summer is already near.',
   'present (Marc. 4.39.16)', [T('4.39.16', '"cum fructum protulerint, intellegunt homines aestatem appropinquasse".')],
   wording='NA27. Tertullian\'s "when they bear fruit, people know" is rated possible only.'),
 A('21:31', G('21:31'), 'So you also, when you see these things happening, know that the kingdom of God is near.',
   'present (Marc. 4.39.10, 16)', [T('4.39.11', '"Sic et vos cum videritis omnia haec fieri, scitote appropinquasse regnum dei."'), T('4.39.16', '"sic et vos cum videritis haec fieri, scitote in proximo esse regnum dei".')],
   wording='NA27. Tertullian cites the verse twice; 4.39.16 renders NA27 exactly, while 4.39.11 has Matthew\'s "all" (Matt 24:33). Roth: secure, as NA27.'),
 A('21:32', G('21:32'), 'Amen, I tell you that this generation will not pass away at all until all things happen.',
   'present (Marc. 4.39.18)', [T('4.39.18', '"Adhuc ingerit non transiturum caelum ac terram, nisi omnia peragantur."')],
   wording='NA27. Tertullian has "heaven and earth will not pass away until all is accomplished" (cf. Matt 5:18); Roth: possible only. Not adopted.'),
 A('21:33', G('21:33'), 'The sky and the earth will pass away, but my words will not pass away at all.',
   'present (Marc. 4.39.18)', [T('4.39.18', '"Transeat age nunc terra et caelum… dum verbum eius maneat in aevum; sic enim et Esaias praenuntiavit."')],
   wording='NA27. Tertullian joins Isa 40:8 ("the word… abides for ever"); Roth rates "my word abides" possible only.'),
 A('21:34', G('21:34'), 'But watch yourselves, so that your hearts are not weighed down with the after-effects of drinking and drunkenness and the anxieties of daily life, and that day comes upon you suddenly',
   'present (Marc. 4.39.18)', [T('4.39.18', '"Admoneantur et discipuli, ne quando graventur corda eorum crapula et ebrietate et saecularibus curis, et insistat eis repentinus dies ille velut laqueus".')]),
 A('21:35', G('21:35'), 'like a snare; for it will come in upon all who sit upon the face of the whole earth.',
   'present for 21:35a (Marc. 4.39.18); 21:35b unattested', [T('4.39.18', '"velut laqueus".')]),
 U('21:36', G('21:36'), 'But keep awake at every time, begging that you may be strong enough to escape all these things that are about to happen, and to stand before the son of the human."', 'Inside the attested paragraph 21:34–36.'),
 A('21:37', G('21:37'), 'And during the days he was teaching in the temple, but during the nights he would go out and spend the night on the mountain called of Olives;',
   'present (Marc. 4.39.19)', [T('4.39.19', '"Sed enim per diem in templo docebat… Ad noctem vero in elaeonem secedebat."')]),
 A('21:38', G('21:38'), 'and all the people would rise early to come to him in the temple to hear him.',
   'present (Marc. 4.39.19)', [T('4.39.19', '"Diluculo conveniendum erat…"')]),
]

OMITTED = [
 dict(ref='21:1–4', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='The widow\'s two coins: a separate NA27 paragraph with no attested verse (METHOD §4.3). Tertullian passes from 20:44 (4.38.10) to 21:8 (4.39.1).')),
 dict(ref='21:5–6', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='The temple\'s stones that will be thrown down: a separate NA27 paragraph with no attested verse. Tertullian\'s survey of the discourse begins "from the learners\' question" (21:7; 4.39.13).')),
 dict(ref='21:18', cls='A−', app=dict(roth='absent', witnesses=[
      E(58, 'πάλιν παρέκοψε τὸ »θρὶξ ἐκ τῆς κεφαλῆς ὑμῶν οὐ μὴ ἀπόληται«.')],
      decision='not printed', reason='Epiphanius states that the text lacked "not a hair of your head will perish"; NA27 cites the omission for Marcion (McionE), with syc. Tertullian goes from 21:17 to 21:19 (4.39.8).')),
 dict(ref='21:21–22', cls='A−', app=dict(roth='absent', witnesses=[
      E(59, 'πάλιν παρέκοψε ταῦτα »τότε οἱ ἐν τῇ Ἰουδαίᾳ φευγέτωσαν εἰς τὰ ὄρη« καὶ τὰ ἑξῆς, διὰ τὰ ἐπιφερόμενα ἐν τῷ ῥητῷ »ἕως πληρωθῇ πάντα τὰ γεγραμμένα«.')],
      decision='not printed', reason='Epiphanius states that the text lacked "then those in Judea must flee to the mountains" and what follows, including "that all that is written may be fulfilled". Tertullian passes from 21:20 to 21:25 (4.39.9).')),
]

PREAMBLE = (
 "The chapter opens on a question that seems to have lost its beginning: teacher, when then will these things "
 "be? What follows is not a timetable. Do not be led astray; many will come using his name. Wars and upheavals, "
 "earthquakes and famines, terrors and signs from heaven. Before all of it, you will be handed over, even by "
 "parents and friends, and need not prepare a word of your defence. By your endurance gain your souls. Jerusalem"
 " will be surrounded; the sea will roar; people will faint with fear; the powers of the heavens will be shaken."
 " Then the son of the human comes from the heavens with much power, and the instruction is to straighten up and"
 " lift your heads. Look at the fig tree when it puts out its leaves. The sky and the earth will pass away; his "
 "words will not. By day he teaches in the temple, by night he lodges on the mountain, and the people rise at "
 "dawn to hear him."
)

NOTES = [
 dict(term='Not printed: 21:1–6', cat='excision', refs=['21:7'], text=(
  "The widow's two coins (21:1–4) and the prediction that not one stone of the temple will be left on another (21:5–6) are not "
  "cited by any witness. Each is a separate NA27 paragraph, and they are not printed. Tertullian describes the discourse as "
  "running \"from the learners' question to the parable of the fig tree\" (4.39.13), so his account begins at 21:7.")),
 dict(term='Signs and persecutions (21:7–19)', cat='textual', refs=['21:8', '21:9', '21:10', '21:11', '21:12', '21:14', '21:15', '21:17', '21:19'], text=(
  "Tertullian, Marc. 4.39.1–8 goes through the discourse in order. Those who \"come upon my name\" use a name that belongs to "
  "the Creator's Christ. The wars, famines, earthquakes and portents \"must take place\". The persecutions come \"before these "
  "things\". The learners are not to think beforehand what to answer before tribunals: "
  "for Tertullian, the one who forbids it is the one who gave Balaam words he had not thought of and promised Moses a mouth. "
  "\"By endurance you will save yourselves.\" Epiphanius states that the text lacked 21:18, \"not a hair of your head will "
  "perish\" (sch. 58).")),
 dict(term='Jerusalem and the end (21:20–28)', cat='textual', refs=['21:20', '21:23', '21:25', '21:26', '21:27', '21:28'], text=(
  "Tertullian (4.39.9–12): when Jerusalem begins to be surrounded by armies (\"vallari exercitibus Hierusalem\"), the signs of the end follow, in sun, moon and "
  "stars, nations in anguish \"as at the roar of the sea\", the powers of heaven shaken. \"And then they will see the son of the human "
  "coming from the heavens with much power\". Then come \"lift up your heads, for your release is drawing near\". The "
  "reading \"from the heavens with much power\" is printed for canonical Luke's \"in a cloud with power and great glory\". "
  "Epiphanius states that the text lacked the flight of those in Judea to the mountains and \"until all that is written is "
  "fulfilled\" (21:21–22; sch. 59). No witness to this text has the \"abomination of desolation\" of Mark 13:14 and Matthew 24:15. "
  "21:23–24 are not cited and are printed in grey.")),
 dict(term='The fig tree and watchfulness (21:29–38)', cat='textual', refs=['21:29', '21:31', '21:32', '21:33', '21:34', '21:35', '21:37'], text=(
  "Tertullian, Marc. 4.39.16–19: the fig tree that bears fruit is a sign of summer, as the troubles of the world are a sign of "
  "the kingdom. \"The sky and the earth will pass away\" and the Lord's word remains (he cites Isa 40:8). The learners are warned "
  "against heaviness of heart \"with dissipation, drunkenness and worldly cares\", lest the day come on them \"like a snare\". "
  "Jesus taught by day in the temple and withdrew at night to the Mount of Olives. 21:36 is not cited and is printed in grey.")),
 dict(term='The coming from the heavens', cat='theological', refs=['21:27', '21:28', '21:31'], text=(
  "Interpretation. In this text the son of the human comes \"from the heavens with much power\", without the cloud and the "
  "\"glory\" of canonical Luke. The redemption drawing near is set beside \"the kingdom of God is near\" (21:31), and the "
  "warning is against the heaviness of a heart taken up with drink and worldly cares. Tertullian's argument is that the "
  "terrors and the promises belong to one son of the human and cannot be separated (4.39.13–15). The text keeps the coming and the "
  "call to watchfulness in one discourse.")),
 dict(term='οὖν, "then"', cat='translation', refs=['21:7'], text='The word joins the question to what came before.'),
 dict(term='Βλέπετε μὴ πλανηθῆτε, "look out that you are not led astray"', cat='translation', refs=['21:8'], text='πλανάω, to lead astray, cause to wander.'),
 dict(term='ἐπὶ τῷ ὀνόματί μου, "upon my name"', cat='translation', refs=['21:8'], text='Using my name, claiming it.'),
 dict(term='Ἐγώ εἰμι, "I am"', cat='translation', refs=['21:8'], text='Word for word, without a predicate. It can mean "I am he" or echo the divine name of Ex 3:14.'),
 dict(term='Ὁ καιρὸς ἤγγικεν, "the time has come near"', cat='translation', refs=['21:8'], text='καιρός, as at 12:56.'),
 dict(term='ἀκαταστασίας, "upheavals"', cat='translation', refs=['21:9'], text='Disorders, revolts.'),
 dict(term='μὴ πτοηθῆτε, "do not be terrified"', cat='translation', refs=['21:9'], text='To be scared, panic.'),
 dict(term='δεῖ, "must"', cat='translation', refs=['21:9'], text='As at 4:43.'),
 dict(term='Ἐγερθήσεται, "will rise"', cat='translation', refs=['21:10'], text='ἐγείρω, passive: "will be raised up".'),
 dict(term='λιμοὶ καὶ λοιμοί, "famines and plagues"', cat='translation', refs=['21:11'], text='The Greek words sound almost alike.'),
 dict(term='φόβητρα, "terrors"', cat='translation', refs=['21:11'], text='Fearful sights. The order "terrors and great signs from heaven" is NA27\'s.'),
 dict(term='διώξουσιν, "pursue"', cat='translation', refs=['21:12'], text='To chase, persecute.'),
 dict(term='ἀπαγομένους, "you being led away"', cat='translation', refs=['21:12'], text='A participle in the accusative: "you" as those led away.'),
 dict(term='ἀποβήσεται ὑμῖν εἰς μαρτύριον, "it will turn out for you as a testimony"', cat='translation', refs=['21:13'], text='To result, come to be.'),
 dict(term='προμελετᾶν, "rehearse beforehand"', cat='translation', refs=['21:14'], text='To practise a speech in advance.'),
 dict(term='ἀπολογηθῆναι, "answer in defence"', cat='translation', refs=['21:14'], text='As at 12:11.'),
 dict(term='στόμα καὶ σοφίαν, "a mouth and wisdom"', cat='translation', refs=['21:15'], text='A mouth: speech.'),
 dict(term='παραδοθήσεσθε, "you will be handed over"', cat='translation', refs=['21:16'], text='παραδίδωμι, as at 9:44.'),
 dict(term='θανατώσουσιν ἐξ ὑμῶν, "they will put some of you to death"', cat='translation', refs=['21:16'], text='Literally "they will put to death from among you".'),
 dict(term='ἐν τῇ ὑπομονῇ… κτήσασθε τὰς ψυχὰς ὑμῶν, "by your endurance gain your souls"', cat='translation', refs=['21:19'], text='ὑπομονή, staying under a load, endurance. κτάομαι, to acquire, gain. ψυχή, as at 9:24.'),
 dict(term='στρατοπέδων, "armies"', cat='translation', refs=['21:20'], text='Military camps, armies encamped.'),
 dict(term='ἡ ἐρήμωσις αὐτῆς, "its desolation"', cat='translation', refs=['21:20'], text='Its being made a desert (ἔρημος).'),
 dict(term='ταῖς ἐν γαστρὶ ἐχούσαις, "those who are with child"', cat='translation', refs=['21:23'], text='Literally "those having in the belly".'),
 dict(term='ἀνάγκη, "distress"', cat='translation', refs=['21:23'], text='Necessity, constraint, distress.'),
 dict(term='ἐπὶ τῆς γῆς, "upon the land"', cat='translation', refs=['21:23'], text='γῆ, land and earth, as at 5:24.'),
 dict(term='στόματι μαχαίρης, "by the mouth of the sword"', cat='translation', refs=['21:24'], text='A Hebrew idiom: the edge of the sword.'),
 dict(term='αἰχμαλωτισθήσονται, "be led captive"', cat='translation', refs=['21:24'], text='Taken as prisoners of war.'),
 dict(term='καιροὶ ἐθνῶν, "the times of nations"', cat='translation', refs=['21:24'], text='Without the article in the Greek.'),
 dict(term='συνοχή, "anguish"', cat='translation', refs=['21:25'], text='Being held together, pressed: distress.'),
 dict(term='ἐν ἀπορίᾳ, "in perplexity"', cat='translation', refs=['21:25'], text='Not knowing which way to go.'),
 dict(term='σάλου, "the surge"', cat='translation', refs=['21:25'], text='The rolling swell.'),
 dict(term='ἀποψυχόντων, "fainting"', cat='translation', refs=['21:26'], text='Literally "breathing out the soul": fainting, dying.'),
 dict(term='τῇ οἰκουμένῃ, "the inhabited world"', cat='translation', refs=['21:26'], text='The world where people live.'),
 dict(term='σαλευθήσονται, "will be shaken"', cat='translation', refs=['21:26'], text='σαλεύω, as at 6:38 and 6:48.'),
 dict(term='ἀπὸ τῶν οὐρανῶν μετὰ δυνάμεως πολλῆς, "from the heavens with much power"', cat='translation', refs=['21:27'], text='The reading of this text, from Tertullian\'s Latin. Canonical Luke has "in a cloud with power and much glory".'),
 dict(term='ἀνακύψατε, "straighten up"', cat='translation', refs=['21:28'], text='The verb of the bent woman (13:11).'),
 dict(term='ἡ ἀπολύτρωσις ὑμῶν, "your release"', cat='translation', refs=['21:28'], text='ἀπολύτρωσις, release by ransom, the buying back of a captive or slave. "Redemption" is the Latin term for the same thing.'),
 dict(term='προβάλωσιν, "put out their leaves"', cat='translation', refs=['21:30'], text='To put forth; the Greek has no word for "leaves".'),
 dict(term='τὸ θέρος, "summer"', cat='translation', refs=['21:30'], text='The summer, the time of harvest.'),
 dict(term='οὐ μὴ παρέλθῃ, "will not pass away at all"', cat='translation', refs=['21:32'], text='The double negative, as at 10:19.'),
 dict(term='οἱ λόγοι μου, "my words"', cat='translation', refs=['21:33'], text='λόγος, as at 6:47.'),
 dict(term='βαρηθῶσιν, "weighed down"', cat='translation', refs=['21:34'], text='As at 9:32.'),
 dict(term='κραιπάλῃ, "the after-effects of drinking"', cat='translation', refs=['21:34'], text='The headache and nausea after a bout of drinking.'),
 dict(term='μερίμναις βιωτικαῖς, "the anxieties of daily life"', cat='translation', refs=['21:34'], text='μέριμνα, as at 12:11; βιωτικός, belonging to βίος, livelihood (8:43).'),
 dict(term='αἰφνίδιος, "suddenly"', cat='translation', refs=['21:34'], text='Unexpected.'),
 dict(term='παγίς, "a snare"', cat='translation', refs=['21:35'], text='A trap, a noose.'),
 dict(term='ἀγρυπνεῖτε, "keep awake"', cat='translation', refs=['21:36'], text='To be sleepless, watchful.'),
 dict(term='δεόμενοι, "begging"', cat='translation', refs=['21:36'], text='δέομαι, as at 10:2.'),
 dict(term='κατισχύσητε, "be strong enough"', cat='translation', refs=['21:36'], text='To have full strength.'),
 dict(term='ηὐλίζετο, "spend the night"', cat='translation', refs=['21:37'], text='To lodge in the open, camp.'),
 dict(term='τὸ ὄρος τὸ καλούμενον Ἐλαιῶν, "the mountain called of Olives"', cat='translation', refs=['21:37'], text='The Greek is a genitive, "of Olives": the mountain of the olive groves.'),
 dict(term='ὤρθριζεν, "would rise early"', cat='translation', refs=['21:38'], text='From ὄρθρος, the dawn.'),
]
