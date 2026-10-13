"""Batch 5, chapter 19 of the reconstruction: Luke 21:1–38 (21:7–38 printed; 21:5–6 restored by method, METHOD §11)."""
from buildlib import greek, R
from batch1_ch2 import U, A
from batch5_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}

T393 = T('4.39.3', '"Videamus et quae signa temporibus imponat. Bella, opinor, et regnum super regnum, et gentem super gentem, et pestem, et fames terraeque motus, et formidines, et prodigia de caelo… Haec cum adicit etiam oportere fieri…"')
T399 = T('4.39.9', '"signa iam ultimi finis enarrat, solis et lunae siderumque prodigia, et in terra angustias nationum obstupescentium velut a sonitu maris fluctuantis, pro expectatione imminentium orbi malorum. Quod et ipsae vires caelorum concuti habeant…"')

CR_21_5 = ('The temple\'s stones that will be thrown down: a separate NA27 paragraph with no attested verse. Tertullian\'s survey of the discourse begins '
           '"from the disciples\' question" (21:7; 4.39.13).')
GR_21_5 = ('by its words, the printed 21:7, "Teacher, when then (οὖν) will these things (ταῦτα) be?", has its "then" and its "these things" only in 21:6; '
           'without it the disciples ask about nothing (21:7 would follow 20:44). By its mechanics: the discourse of 21:8–36 answers when "these things" will be, '
           'and what is thrown down is the adorned house, the outside of 11:39–40; without it the printed 21:20 ("its desolation has come near") has no beginning. '
           'Reading: docs/research/correspondence/word_by_word.md, chapter 18, test of 21:5–6.')

ENTRIES = [
 R('21:5', G('21:5'), 'And when some were speaking about the temple, how it was adorned with beautiful stones and offerings, he said,',
   'U?', 'unattested', CR_21_5, GR_21_5, wording='NA27 (checked on the page image, p. 229).'),
 R('21:6', G('21:6'), '"As for these things that you see, the days will come when not one stone will be left upon another that will not be thrown down."',
   'U?', 'unattested', CR_21_5, GR_21_5, wording='NA27 (checked on the page image, p. 229).'),
 A('21:7', G('21:7'), 'And they asked him, "Teacher, when then will these things be, and what will be the sign when these things are about to take place?"',
   'present (Marc. 4.39.13)', [T('4.39.13', '"Ipsum decursum scripturae evangelicae ab interrogatione discipulorum usque ad parabolam fici…"')],
   wording='NA27. Tertullian attests the disciples\' question, not its wording; Roth rates "the disciples" as subject possible only (NA27: οἱ μαθηταί added by D). In this text "these things" has no antecedent, since 21:5–6, the prediction about the temple stones, are not printed.'),
 A('21:8', G('21:8'), 'And he said, "See that you are not led astray. For many will come in my name, saying, \'I am he!\' and, \'The time is at hand!\' Do not go after them.',
   'present (Marc. 4.39.1–2)', [T('4.39.1', '"…qui multos dicat venturos in nomine ipsius… amplius et prohibeat eos recipi…"'), T('4.39.2', '"Venient denique illi dicentes, Ego sum Christus."')],
   wording='NA27. Tertullian\'s "I am the Christ" is Matthew\'s wording (Matt 24:5); Roth: possible only.'),
 A('21:9', G('21:9'), 'And when you hear of wars and tumults, do not be terrified, for these things must first take place, but the end will not be at once."',
   'present (Marc. 4.39.3)', [T393]),
 A('21:10', G('21:10'), 'Then he said to them, "Nation will rise against nation, and kingdom against kingdom.',
   'present (Marc. 4.39.3)', [T393]),
 A('21:11', G('21:11'), 'There will be great earthquakes, and in various places famines and pestilences; and there will be terrors and great signs from heaven.',
   'present (Marc. 4.39.3)', [T393], wording='NA27 (ἀπ\' οὐρανοῦ σημεῖα; SBLGNT σημεῖα ἀπ\' οὐρανοῦ — checked on the page image).'),
 A('21:12', G('21:12'), 'But before all this they will lay their hands on you and persecute you, delivering you up to the synagogues and prisons, and you will be brought before kings and governors for my name\'s sake.',
   'present (Marc. 4.39.4)', [T('4.39.4', '"Ante haec autem persecutiones eis praedicat et passiones venturas, in martyrium utique et in salutem."')]),
 A('21:13', G('21:13'), 'This will be your opportunity to bear witness.',
   'present (Marc. 4.39.4)', [T('4.39.4', '"in martyrium".')]),
 A('21:14', G('21:14'), 'Settle it therefore in your minds not to prepare your defence beforehand,',
   'present (Marc. 4.39.6–7)', [T('4.39.6', '"Et hic igitur ipse vetat cogitari quid responderi oporteat apud tribunalia".')]),
 A('21:15', G('21:15'), 'for I will give you a mouth and wisdom, which none of your adversaries will be able to withstand or contradict.',
   'present (Marc. 4.39.6–7)', [T('4.39.6', '"Et sapientiam ipsam, cui nemo resisteret…"')]),
 A('21:16', G('21:16'), 'You will be delivered up even by parents and brothers and relatives and friends, and some of you they will put to death.',
   'present (Marc. 4.39.8)', [T('4.39.8', '"A proximis quoque persecutiones…"')]),
 A('21:17', G('21:17'), 'You will be hated by all for my name\'s sake.',
   'present (Marc. 4.39.8)', [T('4.39.8', '"et nominis ex odio utique blasphemiam praedicatam".')]),
 A('21:19', G('21:19'), 'By your endurance you will gain your lives.',
   'present (Marc. 4.39.8)', [T('4.39.8', '"Sed per tolerantiam, inquit, salvos facietis vosmetipsos".')],
   wording='NA27. Tertullian\'s "you will save yourselves" (NA27 apparatus: σώσετε McionT) is rated possible only by Roth; not adopted.'),
 A('21:20', G('21:20'), 'But when you see Jerusalem surrounded by armies, then know that its desolation has come near.',
   'present (Marc. 4.39.9)', [T('4.39.9', '"Sed monstrato dehinc tempore excidii, cum coepisset vallari exercitibus Hierusalem…"')]),
 U('21:23', G('21:23'), 'Alas for women who are pregnant and for those who are nursing infants in those days! For there will be great distress upon the earth and wrath against this people.', 'Inside the attested paragraph 21:20–24.'),
 U('21:24', G('21:24'), 'They will fall by the edge of the sword and be led captive among all nations, and Jerusalem will be trampled underfoot by the Gentiles, until the times of the Gentiles are fulfilled.', 'Inside the attested paragraph 21:20–24.'),
 A('21:25', G('21:25'), 'And there will be signs in sun and moon and stars, and on the earth distress of nations in perplexity because of the roaring of the sea and the waves,',
   'present (Marc. 4.39.9)', [T399]),
 A('21:26', G('21:26'), 'people fainting with fear and with foreboding of what is coming on the world. For the powers of the heavens will be shaken.',
   'present (Marc. 4.39.9)', [T399]),
 A('21:27', G('21:27'),
   'And then they will see the son of man coming in a cloud with power and great glory.',
   'present (Marc. 4.39.10–11)',
   [T('4.39.10', '"Post haec quid dominus? Et tunc videbunt filium hominis venientem de caelis cum plurima virtute."'),
    T('4.39.11', '"Hic erit dies magnus domini et illustris, venientis de caelis filii hominis, secundum Danielem: Ecce cum caeli nubibus tanquam filius hominis adveniens…"')],
   wording=('NA27 "coming in a cloud with power and great glory" printed by method (METHOD §11) against the attested Marcionite reading "coming from the heavens with great power" (a retroversion). '
            'The correspondential reading marks the attested wording as a strain: it drops the glory that 9:26 announces for the coming of the son of man and 24:26 names as where he enters, and the cloud from which the voice said "hear him" (9:34–35); NA27 continues the line (docs/research/correspondence/word_by_word.md, chapter 19; second_pass.md §3). The evidence for the Marcionite reading: Tertullian quotes the verse as the Lord\'s words ("Post haec quid dominus?", 4.39.10) and repeats "coming from the heavens" (4.39.11); Roth: "from the heavens" very likely, "with power… great" secure, "and glory likely not present". '
            'His Latin "cum plurima virtute" cannot render NA27\'s two nouns. The cloud he brings in himself, from Daniel 7:13, as a separate text. NA27 apparatus: καὶ δυνάμει πολλῇ καὶ δόξῃ D e (sys.c).')),
 A('21:28', G('21:28'), 'Now when these things begin to take place, straighten up and raise your heads, because your redemption is drawing near."',
   'present (Marc. 4.39.10, 12)', [T('4.39.10', '"Cum autem haec fient, erigetis vos, et levabitis capita, quoniam appropinquavit redemptio vestra".')],
   wording='NA27. Tertullian lacks "your" with "heads"; Roth: likely not present, because Tertullian has "capita vestra" when he cites the verse in Res. 22.6, and D d omit the pronoun (Roth n. 434; not in the NA27 apparatus). Latin can leave the possessive unexpressed, so his "capita" can render NA27 (METHOD §5.4). Printed.'),
 A('21:29', G('21:29'), 'And he told them a parable: "Look at the fig tree, and all the trees.',
   'present (Marc. 4.39.10, 13, 16)', [T('4.39.16', '"In summa ipsius parabolae considera exemplum. Aspice ficum et arbores omnes".')]),
 A('21:30', G('21:30'), 'As soon as they come into leaf, you see for yourselves and know that the summer is already near.',
   'present (Marc. 4.39.16)', [T('4.39.16', '"cum fructum protulerint, intellegunt homines aestatem appropinquasse".')],
   wording='NA27. Tertullian\'s "when they bear fruit, people know" is rated possible only.'),
 A('21:31', G('21:31'), 'So also, when you see these things taking place, you know that the kingdom of God is near.',
   'present (Marc. 4.39.10, 16)', [T('4.39.11', '"Sic et vos cum videritis omnia haec fieri, scitote appropinquasse regnum dei."'), T('4.39.16', '"sic et vos cum videritis haec fieri, scitote in proximo esse regnum dei".')],
   wording='NA27. Tertullian cites the verse twice; 4.39.16 renders NA27 exactly, while 4.39.11 has Matthew\'s "all" (Matt 24:33). Roth: secure, as NA27.'),
 A('21:32', G('21:32'), 'Truly I tell you, this generation will not pass away until all has taken place.',
   'present (Marc. 4.39.18)', [T('4.39.18', '"Adhuc ingerit non transiturum caelum ac terram, nisi omnia peragantur."')],
   wording='NA27. Tertullian has "heaven and earth will not pass away until all is accomplished" (cf. Matt 5:18); Roth: possible only. Not adopted.'),
 A('21:33', G('21:33'), 'Heaven and earth will pass away, but my words will not pass away.',
   'present (Marc. 4.39.18)', [T('4.39.18', '"Transeat age nunc terra et caelum… dum verbum eius maneat in aevum; sic enim et Esaias praenuntiavit."')],
   wording='NA27. Tertullian joins Isa 40:8 ("the word… abides for ever"); Roth rates "my word abides" possible only.'),
 A('21:34', G('21:34'), 'But watch yourselves lest your hearts be weighed down with dissipation and drunkenness and cares of this life, and that day come upon you suddenly',
   'present (Marc. 4.39.18)', [T('4.39.18', '"Admoneantur et discipuli, ne quando graventur corda eorum crapula et ebrietate et saecularibus curis, et insistat eis repentinus dies ille velut laqueus".')]),
 A('21:35', G('21:35'), 'like a trap. For it will come upon all who dwell on the face of the whole earth.',
   'present for 21:35a (Marc. 4.39.18); 21:35b unattested', [T('4.39.18', '"velut laqueus".')]),
 U('21:36', G('21:36'), 'But stay awake at all times, praying that you may have strength to escape all these things that are going to take place, and to stand before the son of man."', 'Inside the attested paragraph 21:34–36.'),
 A('21:37', G('21:37'), 'Every day he was teaching in the temple, but at night he went out and lodged on the mount called Olivet.',
   'present (Marc. 4.39.19)', [T('4.39.19', '"Sed enim per diem in templo docebat… Ad noctem vero in elaeonem secedebat."')]),
 A('21:38', G('21:38'), 'And all the people came early in the morning to hear him in the temple.',
   'present (Marc. 4.39.19)', [T('4.39.19', '"Diluculo conveniendum erat…"')]),
]

OMITTED = [
 dict(ref='21:1–4', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='The widow\'s two coins: a separate NA27 paragraph with no attested verse (METHOD §4.3). Tertullian passes from 20:44 (4.38.10) to 21:8 (4.39.1).')),
 dict(ref='21:18', cls='A−', app=dict(roth='absent', witnesses=[
      E(58, 'πάλιν παρέκοψε τὸ »θρὶξ ἐκ τῆς κεφαλῆς ὑμῶν οὐ μὴ ἀπόληται«.')],
      decision='not printed', reason='Epiphanius states that the text lacked "not a hair of your head will perish"; NA27 cites the omission for Marcion (McionE), with syc. Tertullian goes from 21:17 to 21:19 (4.39.8).')),
 dict(ref='21:21–22', cls='A−', app=dict(roth='absent', witnesses=[
      E(59, 'πάλιν παρέκοψε ταῦτα »τότε οἱ ἐν τῇ Ἰουδαίᾳ φευγέτωσαν εἰς τὰ ὄρη« καὶ τὰ ἑξῆς, διὰ τὰ ἐπιφερόμενα ἐν τῷ ῥητῷ »ἕως πληρωθῇ πάντα τὰ γεγραμμένα«.')],
      decision='not printed', reason='Epiphanius states that the text lacked "then those in Judea must flee to the mountains" and what follows, including "that all that is written may be fulfilled". Tertullian passes from 21:20 to 21:25 (4.39.9).')),
]

PREAMBLE = (
 "The signs of the end. Some speak of the temple adorned with beautiful stones and offerings, and Jesus says that not one "
 "stone will be left upon another (21:5–6, printed as restored by method; see the notes). The disciples ask when these things will be. Jesus warns them against those who will come in his "
 "name, and speaks of wars, earthquakes, famines, terrors and signs from heaven, and of persecution before kings and "
 "governors, \"for my name's sake\". He tells them not to prepare their defence, for he will give them wisdom, and that by "
 "endurance they will gain their lives. He speaks of Jerusalem surrounded by armies, of signs in sun, moon and stars, and of "
 "the son of man coming \"in a cloud with power and great glory\" (NA27; Tertullian's \"from the heavens with great power\", "
 "Marc. 4.39.10, is recorded in the notes). When these things begin, they are "
 "to lift up their heads, for their redemption is near; the fig tree shows that the kingdom of God is near. He warns them "
 "against dissipation and the cares of life. By day he teaches in the temple and by night he lodges on the Mount of Olives. "
 "Two sayings are absent, by Epiphanius' statement: \"not a hair of your head will perish\" (21:18) and the flight from Judea "
 "\"that all that is written may be fulfilled\" (21:21–22)."
)

NOTES = [
 dict(term='Not printed: 21:1–4', cat='excision', refs=['21:5'], text=(
  "The widow's two coins (21:1–4) is not cited by any witness. It is a separate NA27 paragraph and is not printed (METHOD "
  "§4.3). Tertullian describes the discourse as running \"from the disciples' question to the parable of the fig tree\" "
  "(4.39.13), so his account begins at 21:7.")),
 dict(term='Restored by method: 21:5–6', cat='textual', refs=['21:5', '21:6', '21:7', '21:20'], text=(
  "The prediction that not one stone of the temple will be left on another (21:5–6) is not cited by any witness; it is a "
  "separate NA27 paragraph, and its absence is undetermined (U?). It is printed as restored by method (METHOD §11). By its words, "
  "the printed text needs it: 21:7, \"Teacher, when then (οὖν) will these things (ταῦτα) be?\", has its \"then\" and its \"these "
  "things\" only in 21:6. Without it the question follows 20:44 and asks about nothing. By its mechanics: the discourse of "
  "21:8–36 answers when \"these things\" will be, and what is thrown down is the adorned house, beautiful outside (cf. 11:39–40); "
  "without it the printed 21:20, \"its desolation has come near\", has no beginning. The reading is in "
  "docs/research/correspondence/word_by_word.md (chapter 18, test of 21:5–6). The Greek is NA27, checked on the page image (p. 229).")),
 dict(term='Signs and persecutions (21:7–19)', cat='textual', refs=['21:8', '21:9', '21:10', '21:11', '21:12', '21:14', '21:15', '21:17', '21:19'], text=(
  "Tertullian, Marc. 4.39.1–8 goes through the discourse in order. Those who \"come in my name\" use a name that belongs to "
  "the Creator's Christ. The wars, famines, earthquakes and portents \"must take place\". The persecutions come \"before these "
  "things\". The disciples are not to think beforehand what to answer before tribunals: "
  "for Tertullian, the one who forbids it is the one who gave Balaam words he had not thought of and promised Moses a mouth. "
  "\"By endurance you will save yourselves.\" Epiphanius states that the text lacked 21:18, \"not a hair of your head will "
  "perish\" (sch. 58).")),
 dict(term='Jerusalem and the end (21:20–28)', cat='textual', refs=['21:20', '21:23', '21:25', '21:26', '21:27', '21:28'], text=(
  "Tertullian (4.39.9–12): when Jerusalem begins to be surrounded by armies (\"vallari exercitibus Hierusalem\"), the signs of the end follow, in sun, moon and "
  "stars, nations in anguish \"as at the roar of the sea\", the powers of heaven shaken. \"And then they will see the son of man "
  "coming from the heavens with great power\". Then come \"lift up your heads, for your redemption has drawn near\". "
  "Tertullian's wording \"from the heavens with great power\" is attested (Roth: very likely), but NA27's \"in a cloud with "
  "power and great glory\" is printed, by method (METHOD §11): the correspondential reading marks the attested wording as a "
  "strain that drops the glory announced at 9:26 and the cloud of the mountain (9:34–35). On the premise of a correspondential "
  "original it belongs to the transmission of Marcion's copy. "
  "Epiphanius states that the text lacked the flight of those in Judea to the mountains and \"until all that is written is "
  "fulfilled\" (21:21–22; sch. 59). No witness to this text has the \"abomination of desolation\" of Mark 13:14 and Matthew 24:15. "
  "21:23–24 are not cited and are printed in grey.")),
 dict(term='The fig tree and watchfulness (21:29–38)', cat='textual', refs=['21:29', '21:31', '21:32', '21:33', '21:34', '21:35', '21:37'], text=(
  "Tertullian, Marc. 4.39.16–19: the fig tree that bears fruit is a sign of summer, as the troubles of the world are a sign of "
  "the kingdom. \"Heaven and earth will pass away\" and the Lord's word remains (he cites Isa 40:8). The disciples are warned "
  "against heaviness of heart \"with dissipation, drunkenness and worldly cares\", lest the day come on them \"like a trap\". "
  "Jesus taught by day in the temple and withdrew at night to the Mount of Olives. 21:36 is not cited and is printed in grey.")),
 dict(term='The coming in a cloud', cat='theological', refs=['21:27', '21:28', '21:31'], text=(
  "Interpretation. The son of man comes \"in a cloud with power and great glory\": the glory announced at 9:26 and seen on the "
  "mountain (9:32), and the cloud from which the voice said \"hear him\" (9:34–35). In Swedenborg's exposition of the same "
  "words (Arcana Coelestia 4060, on Matt 24:30) the cloud is the sense of the letter and the glory the inner sense: the coming "
  "is the Lord revealed in the Word. The redemption drawing near is set beside \"the kingdom of God is near\" (21:31), and the "
  "warning is against the heaviness of a heart taken up with drink and worldly cares. Marcion's copy, as Tertullian read it, "
  "had the coming \"from the heavens with great power\", without the cloud and the glory.")),
]
