"""Batch 1, chapter 1 of the reconstruction: Luke 3:1 and Luke 4 (attested order)."""
from buildlib import greek

W_EP_INC = {'source': 'Epiphanius, Pan. 42.11.4–5 (Holl 107–108)',
            'evidence': 'The text began »ἐν τῷ πεντεκαιδεκάτῳ ἔτει Τιβερίου Καίσαρος« καὶ τὰ ἑξῆς; 1:1–2:52, the baptism (3:21–22) and the genealogy (3:23–38) were not in it.'}
W_TE_471 = {'source': 'Tertullian, Marc. 4.7.1',
            'evidence': '"Anno quintodecimo principatus Tiberiani proponit eum descendisse in civitatem Galilaeae Capharnaum" — the date and the descent to Capernaum stated as one sentence.'}

ENTRIES = [
 dict(ref='3:1', cls='A+',
      gr=greek('3:1', [('Ἐν ἔτει δὲ', 'Ἐν ἔτει')]),
      en='In the fifteenth year of the rule of Tiberius Caesar, while Pontius Pilate was governing Judea, and Herod was ruling Galilee as tetrarch, and Philip his brother was ruling as tetrarch the region of Ituraea and Trachonitis, and Lysanias was ruling Abilene as tetrarch,',
      app=dict(roth='present (Marc. 4.7.1; Pan. 42.11.5; Adam. 64,14–15; Irenaeus, Haer. 1.27.2)',
               witnesses=[W_EP_INC, W_TE_471,
                          {'source': 'Irenaeus, Haer. 1.27.2 (via Roth loci)', 'evidence': 'Marcion\'s Jesus came "temporibus Pontii Pilati praesidis, qui fuit procurator Tiberii Caesaris".'}],
               wording='NA27 without δέ. The opening δέ is absent from both witnesses (Epiphanius quotes the incipit without it; Tertullian "Anno quintodecimo"), and a book cannot open with a connective. The clauses naming Herod, Philip and Lysanias are unattested; NA27 is printed for them. The Pilate clause is attested in sense (Irenaeus); Roth reconstructs it as ἐπὶ τῶν χρόνων Ποντίου Πιλάτου (probable only), so NA27 is printed.',
               decision='printed')),
 dict(ref='4:31', cls='A+',
      gr=greek('4:31', [('Καὶ κατῆλθεν', 'κατῆλθεν')]),
      en='he came down to Capernaum, a city of Galilee. And he was teaching them on the sabbaths.',
      app=dict(roth='present (Marc. 4.7.1–7; Adam. 102,22–23; Irenaeus, Haer. 1.27.2; Hippolytus, Haer. 7.31.6)',
               witnesses=[W_TE_471,
                          {'source': 'Tertullian, Marc. 4.7.7', 'evidence': 'Asks how he could be admitted to teach in the assembly: attests the teaching in the assembly.'}],
               wording='NA27 without the opening Καί, which is canonical Luke\'s link to 4:30; the witnesses join κατῆλθεν directly to 3:1 (editorial junction). Spelling Καφαρναούμ (NA27).',
               decision='printed')),
 dict(ref='4:32', cls='A+', gr=greek('4:32'),
      en='And they were astounded at his teaching, because his word was with authority.',
      app=dict(roth='present (Marc. 4.7.7–8)',
               witnesses=[{'source': 'Tertullian, Marc. 4.7.7', 'evidence': '"Stupebant autem omnes ad doctrinam eius… Quoniam, inquit, in potestate erat sermo eius."'}],
               wording='NA27.', decision='printed')),
 dict(ref='4:33', cls='A+', gr=greek('4:33'),
      en='And in the assembly there was a person having a spirit of an unclean daimon, and he cried out with a loud voice,',
      app=dict(roth='unattested',
               witnesses=[{'source': 'Tertullian, Marc. 4.7.9', 'evidence': '"Exclamat ibidem spiritus daemonis" — the spirit of a daimon cries out in that place (the assembly).'}],
               wording='NA27.', decision='printed',
               reason='Tertullian paraphrases the content of the verse (spirit of a daimon, crying out, in the assembly) before quoting 4:34. Roth lists 4:33 as unattested; the paraphrase is sufficient for A+.')),
 dict(ref='4:34', cls='A+', gr=greek('4:34'),
      en='"Ah! What is there between us and you, Jesus, Nazarene? Did you come to destroy us? I know you, who you are: the holy one of God."',
      app=dict(roth='present (Marc. 4.7.9, 10, 12)',
               witnesses=[{'source': 'Tertullian, Marc. 4.7.9', 'evidence': '"Quid nobis et tibi est Iesu? venisti perdere nos: scio qui sis, sanctus dei." No Ἔα, no Ναζαρηνέ.'}],
               wording='NA27. Tertullian\'s quotation lacks Ἔα and Ναζαρηνέ; one witness, and Roth rates the absence of Ναζαρηνέ only "may not have been present", so NA27 is kept and the omission noted. Tertullian opens 4.8.1 with the name Nazaraeus.',
               decision='printed')),
 dict(ref='4:35', cls='A+', gr=greek('4:35'),
      en='And Jesus rebuked it, saying, "Be muzzled, and go out from him." And the daimon, having thrown him into the middle, went out from him, having harmed him in nothing.',
      app=dict(roth='present (Marc. 4.7.13)',
               witnesses=[{'source': 'Tertullian, Marc. 4.7.13', 'evidence': '"Atquin, inquis, increpuit illum Iesus."'}],
               wording='NA27.', decision='printed')),
 dict(ref='4:36', cls='U?', flag=True, gr=greek('4:36'),
      en='And astonishment came upon all, and they were talking with one another, saying, "What is this word, that with authority and power he gives orders to the unclean spirits, and they go out?"',
      app=dict(roth='unattested', witnesses=[], wording='NA27.', decision='printed, flagged unattested',
               reason='Inside the attested pericope 4:31–37.')),
 dict(ref='4:37', cls='U?', flag=True, gr=greek('4:37'),
      en='And the sound of him was going out into every place of the surrounding region.',
      app=dict(roth='unattested', witnesses=[], wording='NA27.', decision='printed, flagged unattested',
               reason='Inside the attested pericope 4:31–37.')),
 dict(ref='4:16', cls='A+', gr=greek('4:16'),
      en='And he came to Nazara, where he had been brought up, and he went in, according to his custom, on the day of the sabbaths into the assembly, and stood up to read.',
      app=dict(roth='present (Marc. 4.8.2; Ephrem, Comm. Diat. 11.23)',
               witnesses=[{'source': 'Tertullian, Marc. 4.8.2', 'evidence': '"apud Nazareth quoque nihil novi notatur praedicasse, dum alio, merito unius proverbii, eiectus refertur" — the visit to Nazareth, his preaching there, and his ejection.'}],
               wording='NA27 (Ναζαρά). The visit and preaching are attested; the details "as was his custom", "sabbath", "stood up to read" are not.',
               position='After 4:37: Tertullian treats the Capernaum episode (4.7) before Nazareth (4.8.2), and 4:23 refers back to deeds already done at Capernaum.',
               decision='printed')),
 dict(ref='4:23', cls='A+', gr=greek('4:23'),
      en='And he said to them, "Surely you will say this parable to me: \'Physician, heal yourself! Whatever we heard happened at Capernaum, do here too, in your fatherland.\'"',
      app=dict(roth='present (Marc. 4.8.2; Ephrem, Comm. Diat. 11.23)',
               witnesses=[{'source': 'Tertullian, Marc. 4.8.2', 'evidence': '"merito unius proverbii eiectus" — thrown out because of a single proverb.'}],
               wording='NA27.', decision='printed')),
 dict(ref='4:24', cls='U?', flag=True, gr=greek('4:24'),
      en='And he said, "Amen, I tell you: no prophet is acceptable in his fatherland."',
      app=dict(roth='unattested', witnesses=[], wording='NA27.', decision='printed, flagged unattested',
               reason='Inside the attested Nazareth pericope. Tertullian\'s "unius proverbii" may refer to this saying rather than to 4:23; it cannot be decided.')),
 dict(ref='4:28', cls='U?', flag=True, gr=greek('4:28'),
      en='And all in the assembly were filled with rage as they heard these things,',
      app=dict(roth='unattested', witnesses=[], wording='NA27.', decision='printed, flagged unattested',
               reason='Inside the attested Nazareth pericope; Tertullian reports the ejection but not the rage.')),
 dict(ref='4:29', cls='A+', gr=greek('4:29'),
      en='and rising up they threw him out, outside the city, and led him to the brow of the mountain on which their city had been built, so as to throw him down the cliff.',
      app=dict(roth='present (Marc. 4.8.2; Ephrem, Comm. Diat. 11.23; Jerome)',
               witnesses=[{'source': 'Tertullian, Marc. 4.8.2', 'evidence': '"manus ei iniectas… detentus et captus et ad praecipitium usque protractus".'}],
               wording='NA27.', decision='printed')),
 dict(ref='4:30', cls='A+', gr=greek('4:30'),
      en='But he, passing through the middle of them, went on his way.',
      app=dict(roth='present (Marc. 4.8.3; Jerome)',
               witnesses=[{'source': 'Tertullian, Marc. 4.8.3', 'evidence': '"Nam etsi per medios evasit…"'}],
               wording='NA27.', decision='printed')),
 dict(ref='4:40', cls='A+', gr=greek('4:40'),
      en='As the sun was setting, all who had people sick with various diseases brought them to him; and he, laying his hands on each one of them, was healing them.',
      app=dict(roth='present (Marc. 4.8.4)',
               witnesses=[{'source': 'Tertullian, Marc. 4.8.4', 'evidence': '"ipse mox tetigit alios, quibus manus imponens… beneficia medicinarum conferebat".'}],
               wording='NA27 (εἶχον, ἐθεράπευεν; checked on the page image).', decision='printed')),
 dict(ref='4:41', cls='A+', gr=greek('4:41'),
      en='And daimons too were going out from many, crying out and saying, "You are the son of God!" And rebuking them, he would not let them speak, because they knew him to be the Anointed One.',
      app=dict(roth='present (Marc. 4.8.5)',
               witnesses=[{'source': 'Tertullian, Marc. 4.8.5', 'evidence': '"spiritus nequam… excedebant vociferantes, Tu es filius dei… increpabantur et iubebantur tacere."'}],
               wording='NA27. NA27 cites McionT for its text against the addition ὁ χριστός after εἶ (A Q Θ Ψ 0102 f1.13 𝔐). κραυγάζοντα is NA27 text (κράζοντα ℵ B C …).',
               decision='printed')),
 dict(ref='4:42', cls='A+', gr=greek('4:42'),
      en='When day came, going out, he journeyed to a desert place; and the crowds were searching for him, and they came up to him and were holding him back from journeying away from them.',
      app=dict(roth='present (Marc. 4.8.9–10)',
               witnesses=[{'source': 'Tertullian, Marc. 4.8.9', 'evidence': '"In solitudinem procedit… Detentus a turbis".'}],
               wording='NA27.', decision='printed')),
 dict(ref='4:43', cls='A+', gr=greek('4:43'),
      en='But he said to them, "To the other cities also I must announce the good news of the kingdom of God, because for this I was sent."',
      app=dict(roth='present (Marc. 4.8.10)',
               witnesses=[{'source': 'Tertullian, Marc. 4.8.9', 'evidence': '"Oportet me, inquit, et aliis civitatibus annuntiare regnum dei."'}],
               wording='NA27. Tertullian\'s order "oportet me… et aliis civitatibus" is rated very likely by Roth for δεῖ με only; word order in a Latin citation is not evidence for Greek order, so NA27 is kept.',
               decision='printed')),
 dict(ref='4:44', cls='U?', flag=True, gr=greek('4:44'),
      en='And he was proclaiming in the assemblies of Judea.',
      app=dict(roth='unattested', witnesses=[], wording='NA27 (Ἰουδαίας; Γαλιλαίας A D Θ Ψ f13 𝔐).',
               decision='printed, flagged unattested', reason='Inside the attested pericope 4:42–44.')),
]

# Verses of Luke 3–4 that are not printed (records only).
OMITTED = [
 dict(ref='3:2–20', cls='A−', app=dict(roth='unattested', witnesses=[W_EP_INC, W_TE_471],
      decision='not printed',
      reason='The witnesses join the date of 3:1 directly to the descent to Capernaum (4:31): Tertullian 4.7.1 in one sentence; Irenaeus, Haer. 1.27.2 and Hippolytus, Haer. 7.31 likewise open with the descent. The sequence leaves no room for John\'s preaching. Roth classes 3:2–20 as unattested; the difference is recorded.')),
 dict(ref='3:21–22', cls='A−', app=dict(roth='absent', witnesses=[W_EP_INC], decision='not printed',
      reason='Epiphanius, Pan. 42.11.4: τὰ τῆς τοῦ βαπτίσματος ὑποθέσεως not in the text.')),
 dict(ref='3:23–38', cls='A−', app=dict(roth='absent', witnesses=[W_EP_INC], decision='not printed',
      reason='Epiphanius, Pan. 42.11.4: the genealogy not in the text.')),
 dict(ref='4:1–13', cls='A−', app=dict(roth='absent', witnesses=[W_TE_471,
      {'source': 'Tertullian, Marc. 5.6.7 (via Roth loci)', 'evidence': 'cited by Roth for the absence of the temptation.'}],
      decision='not printed', reason='Excluded by the 3:1 → 4:31 junction. The temptation is also listed as absent in the library (Dancing with Fire §5.2).')),
 dict(ref='4:14–15', cls='A−', app=dict(roth='unattested', witnesses=[W_TE_471], decision='not printed',
      reason='Excluded by the 3:1 → 4:31 junction (Roth: unattested; difference recorded).')),
 dict(ref='4:17–21', cls='U−', app=dict(roth='unattested ("possibly not present")', witnesses=[
      {'source': 'Tertullian, Marc. 4.8.2', 'evidence': '"nihil novi notatur praedicasse".'}], decision='not printed',
      reason='Tertullian works through the Nazareth visit (4.8.2–3) and his whole case in book IV is that Jesus fulfils the Creator\'s prophets. A reading of Isaiah 61 announced as fulfilled "today" would have been his strongest proof; he says only that Jesus preached "nothing new". Silence where the passage would have served him (METHOD §3, U−).')),
 dict(ref='4:22', cls='U−', app=dict(roth='unattested ("possibly not present")', witnesses=[
      {'source': 'Tertullian, Marc. 4.7.7', 'evidence': '"cuius nemo adhuc certus de tribu, de populo, de domo" — no one yet knew his tribe, people or house.'}], decision='not printed',
      reason='Tertullian argues that Jesus\' descent was unknown to his hearers; "Is not this Joseph\'s son?" would have contradicted the Marcionite reading and served Tertullian in 4.7–4.8 and in his arguments on the birth. He does not cite it. The previous text printed 4:22a; it is removed.')),
 dict(ref='4:25–26', cls='U−', app=dict(roth='unattested', witnesses=[
      {'source': 'Tertullian, Marc. 4.8.2', 'evidence': '"merito unius proverbii eiectus" — thrown out because of a single proverb.'}], decision='not printed',
      reason='Tertullian gives one proverb as the cause of the ejection; in canonical Luke the Elijah and Elisha sayings are what provoke the rage. Elijah sent to a Sidonian widow would also have served Tertullian\'s argument for the Creator\'s concern for the nations; it is not cited.')),
 dict(ref='4:27', cls='A+', app=dict(roth='present (Marc. 4.35.6; Pan. 42.11.6 sch. 48)', witnesses=[
      {'source': 'Epiphanius, Pan. 42.11.6, sch. 48', 'evidence': 'The saying about Naaman stood inside the healing of the ten lepers (17:14).'}],
      decision='printed in chapter 15, between 17:12 and 17:14 (batch 4 replaces this record)', reason='Attested in a different position.')),
 dict(ref='4:38–39', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='Whole pericope (Simon\'s mother-in-law) without an attested verse (METHOD §4.3).')),
]

PREAMBLE = (
 "We know this feeling. Every day already spoken for, something far away keeping count, and the best of us "
 "somewhere we cannot reach.\n\n"
 "Then one quiet day, at the edge of the water, when we have finally stopped trying, there is a voice. It is not"
 " loud. It asks for nothing. We only notice that everything in us has gone still to listen.\n\n"
 "Something in us that never belonged there knows it at once, and is afraid.\n\n"
 "What we grew up as wants it too, but on its own terms. When it cannot have it so, it carries it up to the "
 "highest place it has and tries to let it fall.\n\n"
 "It does not fall. It walks right through us.\n\n"
 "That evening we bring it everything that hurts. In the morning we beg it to stay where it healed us.\n\n"
 "It will not stay where we want it. It goes on, into every part of us, until all of it is set right."
)

NOTES = [
 dict(term='The opening of the text (3:1 → 4:31)', cat='textual', refs=['3:1', '4:31'], text=(
  "Epiphanius, Pan. 42.11.4–5 (Holl 107–108): the text began »ἐν τῷ πεντεκαιδεκάτῳ ἔτει Τιβερίου Καίσαρος« and lacked Luke "
  "1:1–2:52, the baptism (3:21–22) and the genealogy (3:23–38). Tertullian, Marc. 4.7.1: \"Anno quintodecimo principatus Tiberiani "
  "proponit eum descendisse in civitatem Galilaeae Capharnaum.\" Irenaeus, Haer. 1.27.2 also opens Marcion's account with Jesus "
  "coming \"in the times of Pontius Pilate\". The witnesses join the date to the descent, so 3:2–4:15 is not printed (3:2–20 "
  "John's preaching; 4:1–13 temptation; 4:14–15 return to Galilee). Roth (2015) classes 3:2–20 and 4:14–15 as unattested "
  "rather than absent; the junction is the evidence for absence. The δέ of canonical 3:1 and the Καί of 4:31 are canonical "
  "Luke's connectives and are not printed (editorial junction; neither witness has them). The clauses naming Herod, Philip and "
  "Lysanias are not cited by any witness; they are printed in the NA27 wording within the attested verse.")),
 dict(term='He came down (κατῆλθεν)', cat='theological', refs=['4:31'], text=(
  "Interpretation. In the Greek the verb has its ordinary geographical sense: from the hill country down to Capernaum on the lake. "
  "Tertullian reports that Marcion read it as a descent from heaven (\"utique de caelo\", Marc. 4.7.1). That is the reception of "
  "the text in Marcion's church, not a feature of its wording. Earlier versions of this note presented the heavenly descent as "
  "the meaning of the text; it is withdrawn.")),
 dict(term='Capernaum before Nazareth', cat='textual', refs=['4:31', '4:16', '4:23'], text=(
  "Tertullian works through Marcion's text in order: the Capernaum exorcism in Marc. 4.7 (4:31–35), then Nazareth in 4.8.2–3 "
  "(4:16, 23, 29–30), then the evening healings and departure in 4.8.4–10 (4:40–43). This edition follows that order. Within it "
  "4:23 (\"whatever we heard happened at Capernaum\") refers back to events already told. In canonical Luke the Nazareth scene "
  "comes first and 4:23 refers to deeds the reader has not yet seen. The order is attested; which direction the change went is "
  "not stated here (METHOD §10).")),
 dict(term='The exorcism at Capernaum (4:33–35)', cat='textual', refs=['4:33', '4:34', '4:35'], text=(
  "Tertullian, Marc. 4.7.9: \"Exclamat ibidem spiritus daemonis, Quid nobis et tibi est Iesu? venisti perdere nos: scio qui sis, "
  "sanctus dei\"; 4.7.13: \"increpuit illum Iesus\". The paraphrase attests 4:33, which Roth lists as unattested. Tertullian's "
  "quotation of 4:34 lacks Ἔα and Ναζαρηνέ. This is one witness, and a Latin quotation can drop an interjection and a title; "
  "Roth rates the absence of Ναζαρηνέ only \"may not have been present\". The NA27 wording is printed. Tertullian begins the next "
  "section with the name \"Nazaraeus\" (4.8.1). The previous text deleted Ναζαρηνέ; that went beyond the evidence and is reversed.")),
 dict(term='Not printed in this section: 4:36–39', cat='excision', refs=['4:37', '4:40'], text=(
  "4:36–37 are printed in grey: no witness cites them, but they close the attested exorcism. 4:38–39 (Simon's mother-in-law) "
  "forms its own paragraph and no witness cites it; Tertullian passes from 4:35 (4.7.13) to Nazareth (4.8.2) and returns at 4:40 "
  "(4.8.4). A whole unattested pericope is not printed (METHOD §4.3).")),
 dict(term='The Nazareth visit: what is attested', cat='textual', refs=['4:16', '4:23', '4:24', '4:28', '4:29', '4:30'], text=(
  "Tertullian, Marc. 4.8.2–3: at Nazareth Jesus \"is noted as having preached nothing new\" and was thrown out \"on account of a "
  "single proverb\"; hands were laid on him, he was held, seized and dragged to the precipice, and he escaped \"through their "
  "midst\". This attests 4:16 (the visit and his preaching), a proverb (4:23, or 4:24), 4:29 and 4:30. 4:24 and 4:28 are not "
  "cited and are printed in grey.")),
 dict(term='Absent from the Nazareth visit: 4:17–22 and 4:25–26', cat='excision', refs=['4:16', '4:23'], text=(
  "4:17–21 (the reading of Isaiah 61 and \"today this scripture is fulfilled\"): Tertullian's case in Marc. IV is that Jesus "
  "fulfils the Creator's prophets. A fulfilment of Isaiah announced in the assembly would have been his best proof, and he says "
  "instead that Jesus preached \"nothing new\" there. 4:22 (\"Is not this Joseph's son?\"): Tertullian argues (4.7.7) that no one "
  "knew Jesus' tribe, people or house; the question would have served him and is not cited. 4:25–26 (Elijah and the widow of "
  "Sarepta): Tertullian names one proverb as the cause of the ejection, whereas in canonical Luke the Elijah and Elisha sayings "
  "provoke it. All three are classed \"unattested, probably absent\" (METHOD §3). 4:27 (Naaman) is attested, but inside the "
  "healing of the ten lepers (Epiphanius, sch. 48; Tertullian, Marc. 4.35.6); it is printed there. The previous text printed "
  "4:22a; it is removed. The previous note headed \"Excision of Biological Paternity\" stated a motive for a change; the witnesses "
  "show only that the verse is absent.")),
 dict(term='4:41: "the son of God"', cat='textual', refs=['4:41'], text=(
  "Tertullian, Marc. 4.8.5: the spirits came out \"vociferantes, Tu es filius dei\" and were ordered to be silent. NA27 cites "
  "Marcion (McionT) with ℵ B C D L W and others against the addition of ὁ χριστός (\"you are the Christ, the son of God\") in "
  "A Q Θ Ψ and the Byzantine text. The closing clause \"because they knew him to be the Anointed One\" is not cited by Tertullian; "
  "it is printed in the NA27 wording within the attested verse.")),
 dict(term='The departure (4:42–44)', cat='textual', refs=['4:42', '4:43', '4:44'], text=(
  "Tertullian, Marc. 4.8.9: \"In solitudinem procedit… Detentus a turbis, Oportet me, inquit, et aliis civitatibus annuntiare "
  "regnum dei.\" 4:44 is not cited and is printed in grey; NA27 reads \"Judea\" (ℵ B C L and others), against \"Galilee\" in "
  "A D Θ Ψ and the Byzantine text.")),
 dict(term='What the opening shows', cat='theological', refs=['3:1', '4:31', '4:16'], text=(
  "Interpretation, drawn from the attested text only. Jesus is introduced without ancestry, birth, prophetic announcement, "
  "baptism or testing. His first acts are teaching in a assembly on the sabbath and an exorcism, and his hearers are said not "
  "to know where he comes from. The text gives no Davidic descent and no family claim. The library's thesis that the earliest "
  "gospel belongs to the Jerusalem community around James (Carriers of Living Water §1–3) is not contradicted by this: the setting "
  "is wholly Jewish (assembly, sabbath, the kingdom of God). But the text in this section gives no support to a dynastic "
  "framing either. The reading of κατῆλθεν as a descent from heaven belongs to Marcion's church, not to the wording.")),
 dict(term='ἡγεμονία, ἡγεμονεύοντος, "rule", "governing"', cat='translation', refs=['3:1'], text='the emperor\'s "rule" and Pilate\'s "governing" are the same Greek word (ἡγεμών, one who leads). The English keeps the pair visible.'),
 dict(term='τετρααρχοῦντος, "ruling as tetrarch"', cat='translation', refs=['3:1'], text='a tetrarch is literally "ruler of a fourth", a client ruler under Rome. The verb comes three times.'),
 dict(term='The sentence has no main verb', cat='translation', refs=['3:1'], text='the date runs straight into "he came down" (4:31). The final comma is the Greek\'s.'),
 dict(term='κατῆλθεν, "he came down"', cat='translation', refs=['4:31'], text='the subject is not named until 4:35. Nothing in the Greek says where from.'),
 dict(term='τοῖς σάββασιν, "the sabbaths"', cat='translation', refs=['4:31'], text='plural in the Greek. It can mean "on the sabbath day", but the plural is kept.'),
 dict(term='ἐξεπλήσσοντο, "astounded"', cat='translation', refs=['4:32'], text='the imperfect, "they kept being astounded". The verb means overwhelmed or struck out of one\'s composure.'),
 dict(term='συναγωγή, "assembly"', cat='translation', refs=['4:33'], text='the Greek word means a gathering, both the people gathered and the place. "Synagogue" is the word left untranslated.'),
 dict(term='δαιμόνιον, "daimon"', cat='translation', refs=['4:33'], text='in Greek a spirit-power, a lesser divine being. "Demon" brings in the later idea of a fallen angel. "A spirit of an unclean daimon" translates πνεῦμα δαιμονίου ἀκαθάρτου word for word.'),
 dict(term='ἄνθρωπος, "person"', cat='translation', refs=['4:33'], text='a human being. The word does not say male. ἀνήρ is the word for a man.'),
 dict(term='Ἔα, "Ah!"', cat='translation', refs=['4:34'], text='a cry of displeasure or surprise. It can also be read as the imperative of ἐάω, "let alone!"'),
 dict(term='τί ἡμῖν καὶ σοί, "what is there between us and you"', cat='translation', refs=['4:34'], text='a Hebrew idiom, literally "what to us and to you?" It means "we have nothing in common".'),
 dict(term='"us", "we"', cat='translation', refs=['4:34'], text='plural, although one daimon speaks.'),
 dict(term='Ναζαρηνέ, "Nazarene"', cat='translation', refs=['4:34'], text='an adjective, "the one from Nazara". Other derivations have been proposed (Hebrew nazir, "consecrated"; netser, "shoot"). The translation keeps the Greek word.'),
 dict(term='ὁ ἅγιος τοῦ θεοῦ, "the holy one of God"', cat='translation', refs=['4:34'], text='lower case. The Greek is a description, not a title set apart by capitals.'),
 dict(term='ἐπετίμησεν, "rebuked"', cat='translation', refs=['4:35'], text='to censure, to order sharply. The same verb is used for the daimons (4:41).'),
 dict(term='φιμώθητι, "be muzzled"', cat='translation', refs=['4:35'], text='the verb is used for muzzling an animal. Here it means a harsh "be silent!"'),
 dict(term='ἔξελθε ἀπ\' αὐτοῦ, "go out from him"', cat='translation', refs=['4:35'], text='the same command Simon speaks about himself at 5:8 ("go out from me"). The English keeps them alike.'),
 dict(term='εἰς τὸ μέσον, "into the middle"', cat='translation', refs=['4:35'], text='the same phrase returns at 5:19 and 6:8.'),
 dict(term='θάμβος, "astonishment"', cat='translation', refs=['4:36'], text='a different word from ἐξεπλήσσοντο (4:32) and from ἔκστασις (5:26).'),
 dict(term='λόγος, "word"', cat='translation', refs=['4:36'], text='the same word as in 4:32. Like the Hebrew davar, it can also mean "matter, thing": "what is this thing?"'),
 dict(term='ἐπιτάσσει, "gives orders"', cat='translation', refs=['4:36'], text='a command from one set above.'),
 dict(term='ἦχος, "sound"', cat='translation', refs=['4:37'], text='a noise or echo. It is not the usual word for a report (φήμη).'),
 dict(term='Ναζαρά, "Nazara"', cat='translation', refs=['4:16'], text='the form of the name in this text, as in NA27 here.'),
 dict(term='οὗ ἦν τεθραμμένος, "where he had been brought up"', cat='translation', refs=['4:16'], text='the verb τρέφω means to feed, nourish, rear.'),
 dict(term='τῇ ἡμέρᾳ τῶν σαββάτων, "the day of the sabbaths"', cat='translation', refs=['4:16'], text='plural, as at 4:31.'),
 dict(term='ἀνέστη ἀναγνῶναι, "stood up to read"', cat='translation', refs=['4:16'], text='ἀνίστημι, to stand up, rise. The same verb is used at 4:29 ("rising up").'),
 dict(term='παραβολή, "parable"', cat='translation', refs=['4:23'], text='here a proverb. Luke uses the one word for both a proverb and a story. The English keeps the one word so the reader can see this.'),
 dict(term='πατρίς, "fatherland"', cat='translation', refs=['4:23'], text='one\'s native place, the land of one\'s fathers. "Home town" is correct in sense but loses the link with "father".'),
 dict(term='ἀμήν, "Amen"', cat='translation', refs=['4:24'], text='a Hebrew word ("firmly, truly") that the Greek leaves untranslated, so it is left untranslated here.'),
 dict(term='δεκτός, "acceptable"', cat='translation', refs=['4:24'], text='welcome. It is the word used for a sacrifice that is accepted.'),
 dict(term='θυμός, "rage"', cat='translation', refs=['4:28'], text='hot passion, anger that flares up.'),
 dict(term='ἐξέβαλον, "threw out"', cat='translation', refs=['4:29'], text='ἐκβάλλω, the verb also used for driving out daimons. The Greek says "threw him out outside the city".'),
 dict(term='ὄρος, "mountain"', cat='translation', refs=['4:29'], text='the word covers both hill and mountain. "Mountain" is kept because the same word is used for the mountain of prayer (6:12) and the mountain of 9:28.'),
 dict(term='πόλις, "city"', cat='translation', refs=['4:29'], text='πόλις is kept as "city" throughout, as distinct from κώμη, "village".'),
 dict(term='κατακρημνίσαι, "throw down the cliff"', cat='translation', refs=['4:29'], text='to hurl down a precipice.'),
 dict(term='διὰ μέσου αὐτῶν, "through the middle of them"', cat='translation', refs=['4:30'], text='cf. "into the middle" at 4:35.'),
 dict(term='ἀσθενοῦντας, "sick"', cat='translation', refs=['4:40'], text='literally "without strength, weak".'),
 dict(term='ἐθεράπευεν, "was healing"', cat='translation', refs=['4:40'], text='the imperfect, one after another. θεραπεύω (heal, tend) is kept apart from ἰάομαι (cure, 5:17).'),
 dict(term='ὁ υἱὸς τοῦ θεοῦ, "the son of God"', cat='translation', refs=['4:41'], text='lower case. In Jewish usage it was a title of the king (Ps 2:7) and of the just. A capital "Son" in English assumes a later doctrine the Greek does not mark.'),
 dict(term='τὸν χριστόν, "the Anointed One"', cat='translation', refs=['4:41'], text='χριστός means anointed, the Greek for Hebrew mashiach. "Christ" makes it a name.'),
 dict(term='ἔρημον τόπον, "a desert place"', cat='translation', refs=['4:42'], text='an uninhabited place, not necessarily sand.'),
 dict(term='κατεῖχον, "were holding him back"', cat='translation', refs=['4:42'], text='the imperfect can mean "tried to hold him back". Both readings are open.'),
 dict(term='πορεύομαι, "journey"', cat='translation', refs=['4:42'], text='the same verb as "went on his way" (4:30). It returns throughout the text for the road.'),
 dict(term='εὐαγγελίσασθαι, "announce the good news"', cat='translation', refs=['4:43'], text='a verb, not "preach the gospel".'),
 dict(term='δεῖ, "must"', cat='translation', refs=['4:43'], text='necessity.'),
 dict(term='βασιλεία, "kingdom"', cat='translation', refs=['4:43'], text='first the rule of a king, then the realm he rules. Read "reign" in "kingdom" as much as "realm".'),
 dict(term='ἀπεστάλην, "I was sent"', cat='translation', refs=['4:43'], text='the verb behind ἀπόστολος, "emissary" (6:13).'),
 dict(term='Ἰουδαίας, "Judea"', cat='translation', refs=['4:44'], text='here probably the land of the Judeans as a whole, not only the southern district. The Greek name is kept.'),
]
