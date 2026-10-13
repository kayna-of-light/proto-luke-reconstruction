"""Batch 1, chapter 1 of the reconstruction: Luke 3:1 and Luke 4 (attested order)."""
from buildlib import greek

W_EP_INC = {'source': 'Epiphanius, Pan. 42.11.4–5 (Holl 107–108)',
            'evidence': 'The text began »ἐν τῷ πεντεκαιδεκάτῳ ἔτει Τιβερίου Καίσαρος« καὶ τὰ ἑξῆς; 1:1–2:52, the baptism (3:21–22) and the genealogy (3:23–38) were not in it.'}
W_TE_471 = {'source': 'Tertullian, Marc. 4.7.1',
            'evidence': '"Anno quintodecimo principatus Tiberiani proponit eum descendisse in civitatem Galilaeae Capharnaum" — the date and the descent to Capernaum stated as one sentence.'}

REST_4_17 = ('Class U−: Tertullian works through the Nazareth visit (4.8.2–3), and his case in book IV is that Jesus fulfils the Creator\'s prophets; '
             'a reading of Isaiah 61 announced as fulfilled "today" would have been his strongest proof, and he says only that Jesus preached "nothing new". '
             'Restored by method (METHOD §11). By its words, the printed text needs the passage: 4:16 ends "stood up to read" and nothing is read; '
             '4:23 "surely you will say this parable to me" answers something he said; 4:24 "accepted" (δεκτός) answers 4:19 "the acceptable (δεκτόν) year". '
             'By its mechanics: the first rising in the text is rising to read the Word, and the proclamation of release (4:18) is the first of which 24:47 is the last. '
             'Reading: docs/research/correspondence/word_by_word.md, chapter 1, test of 4:17–22. Printed against the class U− (the silence of Tertullian), not against an attested absence.')
W_TE_482_SILENT = {'source': 'Tertullian, Marc. 4.8.2', 'evidence': '"nihil novi notatur praedicasse" (the class U− rests on this silence; see the reason).'}

ENTRIES = [
 dict(ref='3:1', cls='A+',
      gr=greek('3:1', [('Ἐν ἔτει δὲ', 'Ἐν ἔτει')]),
      en='In the fifteenth year of the rule of Tiberius Caesar, when Pontius Pilate was governing Judea, and Herod was tetrarch of Galilee, and his brother Philip tetrarch of the region of Ituraea and Trachonitis, and Lysanias tetrarch of Abilene,',
      app=dict(roth='present (Marc. 4.7.1; Pan. 42.11.5; Adam. 64,14–15; Irenaeus, Haer. 1.27.2)',
               witnesses=[W_EP_INC, W_TE_471,
                          {'source': 'Irenaeus, Haer. 1.27.2 (via Roth loci)', 'evidence': 'Marcion\'s Jesus came "temporibus Pontii Pilati praesidis, qui fuit procurator Tiberii Caesaris".'}],
               wording='NA27 without δέ. The opening δέ is absent from both witnesses (Epiphanius quotes the incipit without it; Tertullian "Anno quintodecimo"), and a book cannot open with a connective. The clauses naming Herod, Philip and Lysanias are unattested; NA27 is printed for them. The Pilate clause is attested in sense (Irenaeus); Roth reconstructs it as ἐπὶ τῶν χρόνων Ποντίου Πιλάτου (probable only), so NA27 is printed.',
               decision='printed')),
 dict(ref='4:31', cls='A+',
      gr=greek('4:31', [('Καὶ κατῆλθεν', 'κατῆλθεν')]),
      en='he came down to Capernaum, a city of Galilee. And he was teaching them on the sabbaths;',
      app=dict(roth='present (Marc. 4.7.1–7; Adam. 102,22–23; Irenaeus, Haer. 1.27.2; Hippolytus, Haer. 7.31.6)',
               witnesses=[W_TE_471,
                          {'source': 'Tertullian, Marc. 4.7.7', 'evidence': 'Asks how he could be admitted to teach in the synagogue: attests the teaching in the synagogue.'}],
               wording='NA27 without the opening Καί, which is canonical Luke\'s link to 4:30; the witnesses join κατῆλθεν directly to 3:1 (editorial junction). Spelling Καφαρναούμ (NA27).',
               decision='printed')),
 dict(ref='4:32', cls='A+', gr=greek('4:32'),
      en='and they were astounded at his teaching, because his word was with authority.',
      app=dict(roth='present (Marc. 4.7.7–8)',
               witnesses=[{'source': 'Tertullian, Marc. 4.7.7', 'evidence': '"Stupebant autem omnes ad doctrinam eius… Quoniam, inquit, in potestate erat sermo eius."'}],
               wording='NA27.', decision='printed')),
 dict(ref='4:33', cls='A+', gr=greek('4:33'),
      en='And in the assembly there was a man who had the spirit of an unclean daimon, and he cried out with a loud voice:',
      app=dict(roth='unattested',
               witnesses=[{'source': 'Tertullian, Marc. 4.7.9', 'evidence': '"Exclamat ibidem spiritus daemonis" — the spirit of a daimon cries out in that place (the synagogue).'}],
               wording='NA27.', decision='printed',
               reason='Tertullian paraphrases the content of the verse (spirit of a daimon, crying out, in the synagogue) before quoting 4:34. Roth lists 4:33 as unattested; the paraphrase is sufficient for A+.')),
 dict(ref='4:34', cls='A+', gr=greek('4:34'),
      en='"Ha! What have we to do with you, Jesus the Nazarene? Have you come to destroy us? I know who you are: the holy one of God."',
      app=dict(roth='present (Marc. 4.7.9, 10, 12)',
               witnesses=[{'source': 'Tertullian, Marc. 4.7.9', 'evidence': '"Quid nobis et tibi est Iesu? venisti perdere nos: scio qui sis, sanctus dei." No Ἔα, no Ναζαρηνέ.'}],
               wording='NA27. Tertullian\'s quotation lacks Ἔα and Ναζαρηνέ; one witness, and Roth rates the absence of Ναζαρηνέ only "may not have been present", so NA27 is kept and the omission noted. Tertullian opens 4.8.1 with the name Nazaraeus.',
               decision='printed')),
 dict(ref='4:35', cls='A+', gr=greek('4:35'),
      en='And Jesus rebuked it, saying, "Be silent, and come out of him." And when the daimon had thrown him down in their midst, it came out of him without harming him at all.',
      app=dict(roth='present (Marc. 4.7.13)',
               witnesses=[{'source': 'Tertullian, Marc. 4.7.13', 'evidence': '"Atquin, inquis, increpuit illum Iesus."'}],
               wording='NA27.', decision='printed')),
 dict(ref='4:36', cls='U?', flag=True, gr=greek('4:36'),
      en='And amazement came over them all, and they said to one another, "What is this word? With authority and power he commands the unclean spirits, and they come out."',
      app=dict(roth='unattested', witnesses=[], wording='NA27.', decision='printed, flagged unattested',
               reason='Inside the attested pericope 4:31–37.')),
 dict(ref='4:37', cls='U?', flag=True, gr=greek('4:37'),
      en='And a report about him went out into every place in the surrounding region.',
      app=dict(roth='unattested', witnesses=[], wording='NA27.', decision='printed, flagged unattested',
               reason='Inside the attested pericope 4:31–37.')),
 dict(ref='4:16', cls='A+', gr=greek('4:16'),
      en='And he came to Nazara, where he had been brought up; and, as was his custom, he went into the assembly on the sabbath day and stood up to read.',
      app=dict(roth='present (Marc. 4.8.2; Ephrem, Comm. Diat. 11.23)',
               witnesses=[{'source': 'Tertullian, Marc. 4.8.2', 'evidence': '"apud Nazareth quoque nihil novi notatur praedicasse, dum alio, merito unius proverbii, eiectus refertur" — the visit to Nazareth, his preaching there, and his ejection.'}],
               wording='NA27 (Ναζαρά). The visit and preaching are attested; the details "as was his custom", "sabbath", "stood up to read" are not.',
               position='After 4:37: Tertullian treats the Capernaum episode (4.7) before Nazareth (4.8.2), and 4:23 refers back to deeds already done at Capernaum.',
               decision='printed')),
 dict(ref='4:17', cls='U−', restored=True, gr=greek('4:17'),
      en='And the scroll of the prophet Isaiah was handed to him; and unrolling the scroll he found the place where it was written:',
      app=dict(roth='unattested ("possibly not present")', witnesses=[W_TE_482_SILENT],
               wording='NA27 (checked on the page image, p. 164).', decision='printed, restored by method (correspondential reading)', reason=REST_4_17)),
 dict(ref='4:18', cls='U−', restored=True, gr=greek('4:18'),
      en='"The spirit of the Lord is upon me, because he has anointed me to bring good news to the poor; he has sent me to proclaim release to captives and recovery of sight to the blind, to send away the broken in release,',
      app=dict(roth='unattested ("possibly not present")', witnesses=[W_TE_482_SILENT],
               wording='NA27 (p. 164). NA27 prints the quotation of Isaiah 61:1–2 (with 58:6) as verse lines.', decision='printed, restored by method (correspondential reading)', reason=REST_4_17)),
 dict(ref='4:19', cls='U−', restored=True, gr=greek('4:19'),
      en='to proclaim the acceptable year of the Lord."',
      app=dict(roth='unattested ("possibly not present")', witnesses=[W_TE_482_SILENT],
               wording='NA27 (p. 164).', decision='printed, restored by method (correspondential reading)', reason=REST_4_17)),
 dict(ref='4:20', cls='U−', restored=True, gr=greek('4:20'),
      en='And rolling up the scroll, he gave it back to the attendant and sat down; and the eyes of all in the assembly were fixed on him.',
      app=dict(roth='unattested ("possibly not present")', witnesses=[W_TE_482_SILENT],
               wording='NA27 (p. 164).', decision='printed, restored by method (correspondential reading)', reason=REST_4_17)),
 dict(ref='4:21', cls='U−', restored=True, gr=greek('4:21'),
      en='And he began to say to them, "Today this scripture has been fulfilled in your ears."',
      app=dict(roth='unattested ("possibly not present")', witnesses=[W_TE_482_SILENT],
               wording='NA27 (p. 164).', decision='printed, restored by method (correspondential reading)', reason=REST_4_17)),
 dict(ref='4:23', cls='A+', gr=greek('4:23'),
      en='And he said to them, "Doubtless you will quote this proverb to me: \'Physician, heal yourself.\' Whatever we heard was done at Capernaum, do here also in your home town."',
      app=dict(roth='present (Marc. 4.8.2; Ephrem, Comm. Diat. 11.23)',
               witnesses=[{'source': 'Tertullian, Marc. 4.8.2', 'evidence': '"merito unius proverbii eiectus" — thrown out because of a single proverb.'}],
               wording='NA27.', decision='printed')),
 dict(ref='4:24', cls='U?', flag=True, gr=greek('4:24'),
      en='And he said, "Truly I tell you, no prophet is accepted in his home town."',
      app=dict(roth='unattested', witnesses=[], wording='NA27.', decision='printed, flagged unattested',
               reason='Inside the attested Nazareth pericope. Tertullian\'s "unius proverbii" may refer to this saying rather than to 4:23; it cannot be decided.')),
 dict(ref='4:28', cls='U?', flag=True, gr=greek('4:28'),
      en='And all in the assembly were filled with rage when they heard these things,',
      app=dict(roth='unattested', witnesses=[], wording='NA27.', decision='printed, flagged unattested',
               reason='Inside the attested Nazareth pericope; Tertullian reports the ejection but not the rage.')),
 dict(ref='4:29', cls='A+', gr=greek('4:29'),
      en='and they rose up and drove him out of the town, and led him to the brow of the hill on which their town was built, so as to throw him down headlong;',
      app=dict(roth='present (Marc. 4.8.2; Ephrem, Comm. Diat. 11.23; Jerome)',
               witnesses=[{'source': 'Tertullian, Marc. 4.8.2', 'evidence': '"manus ei iniectas… detentus et captus et ad praecipitium usque protractus".'}],
               wording='NA27.', decision='printed')),
 dict(ref='4:30', cls='A+', gr=greek('4:30'),
      en='but he passed through the midst of them and went on his way.',
      app=dict(roth='present (Marc. 4.8.3; Jerome)',
               witnesses=[{'source': 'Tertullian, Marc. 4.8.3', 'evidence': '"Nam etsi per medios evasit…"'}],
               wording='NA27.', decision='printed')),
 dict(ref='4:40', cls='A+', gr=greek('4:40'),
      en='As the sun was setting, all who had people sick with various diseases brought them to him; and he laid his hands on each one of them and healed them.',
      app=dict(roth='present (Marc. 4.8.4)',
               witnesses=[{'source': 'Tertullian, Marc. 4.8.4', 'evidence': '"ipse mox tetigit alios, quibus manus imponens… beneficia medicinarum conferebat".'}],
               wording='NA27 (εἶχον, ἐθεράπευεν; checked on the page image).', decision='printed')),
 dict(ref='4:41', cls='A+', gr=greek('4:41'),
      en='And daimons also came out of many, shouting and saying, "You are the son of God." And he rebuked them and would not allow them to speak, because they knew that he was the Anointed One.',
      app=dict(roth='present (Marc. 4.8.5)',
               witnesses=[{'source': 'Tertullian, Marc. 4.8.5', 'evidence': '"spiritus nequam… excedebant vociferantes, Tu es filius dei… increpabantur et iubebantur tacere."'}],
               wording='NA27. NA27 cites McionT for its text against the addition ὁ χριστός after εἶ (A Q Θ Ψ 0102 f1.13 𝔐). κραυγάζοντα is NA27 text (κράζοντα ℵ B C …).',
               decision='printed')),
 dict(ref='4:42', cls='A+', gr=greek('4:42'),
      en='When day came he went out and made his way to a deserted place. And the crowds were searching for him; they came to him and tried to keep him from leaving them.',
      app=dict(roth='present (Marc. 4.8.9–10)',
               witnesses=[{'source': 'Tertullian, Marc. 4.8.9', 'evidence': '"In solitudinem procedit… Detentus a turbis".'}],
               wording='NA27.', decision='printed')),
 dict(ref='4:43', cls='A+', gr=greek('4:43'),
      en='But he said to them, "I must proclaim the good news of the kingdom of God to the other towns also, because for this I was sent."',
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
 "The text opens with a date and an arrival. Epiphanius quotes its first words, \"In the fifteenth year of Tiberius Caesar\", "
 "and states that the birth narratives, the baptism and the genealogy were not in it (Pan. 42.11.4–5). Tertullian joins the date "
 "directly to the descent to Capernaum (Marc. 4.7.1). There is no preface, no John the Baptist preaching, no baptism, no "
 "genealogy and no temptation. Jesus enters the narrative as an adult teacher in the synagogue of a Galilean town. "
 "The order also differs from canonical Luke. Tertullian treats the exorcism at Capernaum before the visit to Nazareth, and the "
 "Nazareth scene presupposes it (\"whatever we heard was done at Capernaum\", 4:23). As the witnesses report it, the Nazareth "
 "visit is short: they cite no reading from Isaiah, no question about Joseph's son and no Elijah and Elisha sayings, and Jesus is "
 "driven out over a single proverb. The reading from Isaiah (4:17–21) is printed as restored by method: the printed text needs it "
 "(METHOD §11; see the notes). Verses printed in grey are not cited by any witness but stand inside a passage the witnesses "
 "attest; the notes list what is absent and why."
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
  "4:23 (\"whatever we heard was done at Capernaum\") refers back to events already told. In canonical Luke the Nazareth scene "
  "comes first and 4:23 refers to deeds the reader has not yet seen. The order is attested; which direction the change went is "
  "not stated here (METHOD §10).")),
 dict(term='The exorcism at Capernaum (4:33–35)', cat='textual', refs=['4:33', '4:34', '4:35'], text=(
  "Tertullian, Marc. 4.7.9: \"Exclamat ibidem spiritus daemonis, Quid nobis et tibi est Iesu? venisti perdere nos: scio qui sis, "
  "sanctus dei\"; 4.7.13: \"increpuit illum Iesus\". The paraphrase attests 4:33, which Roth lists as unattested. Tertullian's "
  "quotation of 4:34 lacks Ἔα and Ναζαρηνέ. This is one witness, and a Latin quotation can drop an interjection and a title; "
  "Roth rates the absence of Ναζαρηνέ only \"may not have been present\". The NA27 wording is printed. Tertullian begins the next "
  "section with the name \"Nazaraeus\" (4.8.1). The previous text deleted Ναζαρηνέ; that went beyond the evidence and is reversed.")),
 dict(term='Daimon (δαιμόνιον)', cat='translation', refs=['4:33', '4:35', '4:41'], text=(
  "Rendered \"daimon\" to keep the Greek word rather than the later theological category \"demon\". \"The spirit of an unclean "
  "daimon\" translates πνεῦμα δαιμονίου ἀκαθάρτου literally.")),
 dict(term='Not printed in this section: 4:36–39', cat='excision', refs=['4:37', '4:40'], text=(
  "4:36–37 are printed in grey: no witness cites them, but they close the attested exorcism. 4:38–39 (Simon's mother-in-law) "
  "forms its own paragraph and no witness cites it; Tertullian passes from 4:35 (4.7.13) to Nazareth (4.8.2) and returns at 4:40 "
  "(4.8.4). A whole unattested pericope is not printed (METHOD §4.3).")),
 dict(term='The Nazareth visit: what is attested', cat='textual', refs=['4:16', '4:23', '4:24', '4:28', '4:29', '4:30'], text=(
  "Tertullian, Marc. 4.8.2–3: at Nazareth Jesus \"is noted as having preached nothing new\" and was thrown out \"on account of a "
  "single proverb\"; hands were laid on him, he was held, seized and dragged to the precipice, and he escaped \"through their "
  "midst\". This attests 4:16 (the visit and his preaching), a proverb (4:23, or 4:24), 4:29 and 4:30. 4:24 and 4:28 are not "
  "cited and are printed in grey.")),
 dict(term='Restored by method: the reading from Isaiah (4:17–21)', cat='textual', refs=['4:16', '4:17', '4:18', '4:19', '4:20', '4:21', '4:23', '4:24'], text=(
  "No witness cites 4:17–21, and the class is U−: Tertullian works through the Nazareth visit (Marc. 4.8.2–3), his case in "
  "book IV is that Jesus fulfils the Creator's prophets, and he says only that Jesus preached \"nothing new\" there. The passage "
  "is printed as restored by method (METHOD §11), against that class. The grounds are in the printed text. By its words: 4:16 "
  "ends \"he stood up to read\" and nothing is read; 4:23 \"surely you will say this parable to me\" answers something he has said; "
  "4:24 \"no prophet is accepted (δεκτός)\" answers 4:19 \"the acceptable (δεκτόν) year of the Lord\". By its mechanics: the first "
  "rising in the text (ἀνέστη, 4:16) is rising to read, and the proclamation of release (κηρύξαι… ἄφεσιν, 4:18) is the first of "
  "which 24:47 (κηρυχθῆναι… εἰς ἄφεσιν) is the last. The reading is in docs/research/correspondence/word_by_word.md (chapter 1, "
  "test of 4:17–22). The Greek is NA27, checked on the page image (p. 164).")),
 dict(term='Absent from the Nazareth visit: 4:22 and 4:25–26', cat='excision', refs=['4:21', '4:23'], text=(
  "4:22 (\"Is not this Joseph's son?\"): Tertullian argues (4.7.7) that no one knew Jesus' tribe, people or house; the question "
  "would have served him and is not cited. 4:25–26 (Elijah and the widow of Sarepta): Tertullian names one proverb as the cause "
  "of the ejection, whereas in canonical Luke the Elijah and Elisha sayings provoke it. Both are classed \"unattested, probably "
  "absent\" (METHOD §3). The correspondential reading tested both at their places: they continue the line, but the printed text "
  "does not need them, so they are not restored. 4:27 (Naaman) is attested, but inside the healing of the ten lepers "
  "(Epiphanius, sch. 48; Tertullian, Marc. 4.35.6); it is printed there. The previous text printed 4:22a; it is removed. The "
  "previous note headed \"Excision of Biological Paternity\" stated a motive for a change; the witnesses show only that the verse "
  "is absent.")),
 dict(term='4:41: "the son of God"', cat='textual', refs=['4:41'], text=(
  "Tertullian, Marc. 4.8.5: the spirits came out \"vociferantes, Tu es filius dei\" and were ordered to be silent. NA27 cites "
  "Marcion (McionT) with ℵ B C D L W and others against the addition of ὁ χριστός (\"you are the Christ, the son of God\") in "
  "A Q Θ Ψ and the Byzantine text. The closing clause \"because they knew that he was the Anointed One\" is not cited by Tertullian; "
  "it is printed in the NA27 wording within the attested verse.")),
 dict(term='The departure (4:42–44)', cat='textual', refs=['4:42', '4:43', '4:44'], text=(
  "Tertullian, Marc. 4.8.9: \"In solitudinem procedit… Detentus a turbis, Oportet me, inquit, et aliis civitatibus annuntiare "
  "regnum dei.\" 4:44 is not cited and is printed in grey; NA27 reads \"Judea\" (ℵ B C L and others), against \"Galilee\" in "
  "A D Θ Ψ and the Byzantine text.")),
 dict(term='What the opening shows', cat='theological', refs=['3:1', '4:31', '4:16'], text=(
  "Interpretation, drawn from the attested text only. Jesus is introduced without ancestry, birth, prophetic announcement, "
  "baptism or testing. His first acts are teaching in a synagogue on the sabbath and an exorcism, and his hearers are said not "
  "to know where he comes from. The text gives no Davidic descent and no family claim. The library's thesis that the earliest "
  "gospel belongs to the Jerusalem community around James (Carriers of Living Water §1–3) is not contradicted by this: the setting "
  "is wholly Jewish (synagogue, sabbath, the kingdom of God). But the text in this section gives no support to a dynastic "
  "framing either. The reading of κατῆλθεν as a descent from heaven belongs to Marcion's church, not to the wording.")),
]
