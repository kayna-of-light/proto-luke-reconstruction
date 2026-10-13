"""Batch 4, chapter 13 of the reconstruction: Luke 15:1–32 (15:1–10 printed; 15:11–32 restored by method, METHOD §11)."""
from buildlib import greek, R
from batch1_ch2 import U, A
from batch4_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}

CR_15 = ('Epiphanius (sch. 42) states that the whole parable of the two sons was not in the text. Tertullian passes from the coin (4.32.2) to the two masters (16:13, 4.33.1); '
         'Roth counts his silence as confirmation (tacitus).')
GR_15 = ('by its words, the printed 15:1–2 sets two movements going: the sinners received, and the Pharisees and scribes grumbling "this man welcomes sinners and eats with them". '
         'The sheep and the coin answer the welcoming; only the parable of the two sons answers the eating ("let us eat and celebrate", 15:23) and the grumblers, in the elder son who will not go in and is pleaded with (15:28). '
         'The printed 15:7 and 15:10 name "a sinner who repents", but the sheep and the coin are found, they do not repent; the turn itself is shown only here: "coming to himself… rising, I will go to my father" (15:17–20). '
         'By its mechanics it is the text\'s fullest statement of the rising (ἀναστάς) that goes to the father, and of "was dead and is alive again" (cf. 24:5). '
         'Reading: docs/research/correspondence/word_by_word.md, chapter 13, test of 15:11–32; third_pass.md.')
W15 = lambda ref, en, page='211', note='': R(ref, G(ref), en, 'A−', 'absent', CR_15, GR_15 + ' Printed against Marcion\'s text: the witness states that the passage was not in it.',
                                         witnesses=[E(42, 'πάλιν παρέκοψε πᾶσαν τὴν παραβολὴν τῶν δύο υἱῶν, τοῦ εἰληφότος τὸ μέρος τῶν ὑπαρχόντων καὶ ἀσώτως δαπανήσαντος καὶ τοῦ ἄλλου.')],
                                         wording=f'NA27 (checked on the page image, p. {page}).' + note)

ENTRIES = [
 U('15:1', G('15:1'), 'Now all the tax collectors and sinners were coming near to listen to him.',
   'A separate NA27 paragraph, but part of the attested pericope: 15:3 ("he told them this parable") answers the complaint of 15:2.'),
 U('15:2', G('15:2'), 'And the Pharisees and the scribes were grumbling, saying, "This man welcomes sinners and eats with them."',
   'Part of the attested pericope 15:1–10 (see 15:1).'),
 A('15:3', G('15:3'), 'So he told them this parable:',
   'present (Marc. 4.32.2)', [T('4.32.2', '"Ita utriusque parabolae argumentum…"')]),
 A('15:4', G('15:4'), '"Which of you, having a hundred sheep and losing one of them, does not leave the ninety-nine in the wilderness and go after the one that is lost until he finds it?',
   'present (Marc. 4.32.1)', [T('4.32.1', '"Ovem et dragmam perditam quis requirit? nonne qui perdidit? Quis autem perdidit? nonne qui habuit?"')]),
 A('15:5', G('15:5'), 'And when he has found it, he lays it on his shoulders, rejoicing.',
   'present (Marc. 4.32.1)', [T('4.32.1', '"is invenit qui quaesivit".')]),
 A('15:6', G('15:6'), 'And when he comes home, he calls together his friends and his neighbours, saying to them, \'Rejoice with me, for I have found my sheep that was lost.\'',
   'present (Marc. 4.32.1)', [T('4.32.1', '"is exultavit qui invenit".')]),
 A('15:7', G('15:7'), 'I tell you, just so there will be more joy in heaven over one sinner who repents than over ninety-nine righteous people who need no repentance.',
   'present (Marc. 4.32.2)', [T('4.32.2', '"Atque adeo exultare illius est de paenitentia peccatoris, id est de perditi recuperatione, qui se professus est olim malle peccatoris paenitentiam quam mortem."')],
   wording='NA27. Tertullian\'s "joy over the repentance of a sinner" may come from 15:7 or 15:10 (Roth).'),
 A('15:8', G('15:8'), 'Or what woman, having ten silver coins, if she loses one coin, does not light a lamp and sweep the house and search carefully until she finds it?',
   'present (Marc. 4.32.1)', [T('4.32.1', '"Ovem et dragmam perditam quis requirit?"')]),
 A('15:9', G('15:9'), 'And when she has found it, she calls together her friends and neighbours, saying, \'Rejoice with me, for I have found the coin that I had lost.\'',
   'present (Marc. 4.32.1)', [T('4.32.1', '"is invenit qui quaesivit, is exultavit qui invenit".')]),
 A('15:10', G('15:10'), 'Just so, I tell you, there is joy before the angels of God over one sinner who repents.',
   'present (Marc. 4.32.2)', [T('4.32.2', '"exultare illius est de paenitentia peccatoris".')],
   wording='NA27. Roth notes that "the angels of" may not have been present; no witness states it. Printed.'),
 W15('15:11', 'Then he said, "There was a man who had two sons.'),
 W15('15:12', 'The younger of them said to his father, \'Father, give me the share of the property that falls to me.\' So he divided his living between them.'),
 W15('15:13', 'Not many days later the younger son gathered everything together and travelled to a far country, and there he scattered his property in reckless living.'),
 W15('15:14', 'When he had spent everything, a severe famine came over that country, and he began to be in need.'),
 W15('15:15', 'So he went and joined himself to one of the citizens of that country, who sent him into his fields to feed pigs.'),
 W15('15:16', 'And he longed to be filled with the pods that the pigs were eating, and no one gave him anything.', page='211–212', note=' χορτασθῆναι ἐκ (SBLGNT γεμίσαι τὴν κοιλίαν αὐτοῦ ἀπό).'),
 W15('15:17', 'But coming to himself he said, \'How many of my father\'s hired workers have bread in abundance, and I am perishing here with hunger!', page='212'),
 W15('15:18', 'Rising, I will go to my father and say to him, "Father, I have sinned against heaven and before you;', page='212'),
 W15('15:19', 'I am no longer worthy to be called your son; make me as one of your hired workers."\'', page='212'),
 W15('15:20', 'And rising he went to his father. But while he was still far off, his father saw him and was moved with compassion; he ran and fell on his neck and kissed him.', page='212'),
 W15('15:21', 'And the son said to him, \'Father, I have sinned against heaven and before you; I am no longer worthy to be called your son.\'', page='212'),
 W15('15:22', 'But the father said to his servants, \'Quickly, bring out the first robe and clothe him with it, and put a ring on his hand and sandals on his feet;', page='212'),
 W15('15:23', 'and bring the fattened calf and kill it, and let us eat and celebrate;', page='212'),
 W15('15:24', 'for this son of mine was dead and is alive again; he was lost and is found.\' And they began to celebrate.', page='212'),
 W15('15:25', 'Now his elder son was in the field; and as he came and drew near to the house, he heard music and dancing.', page='212'),
 W15('15:26', 'He called one of the servants and asked what these things might be.', page='212'),
 W15('15:27', 'He said to him, \'Your brother has come, and your father has killed the fattened calf, because he has received him back safe and sound.\'', page='212'),
 W15('15:28', 'But he was angry and would not go in. His father came out and began to plead with him.', page='212'),
 W15('15:29', 'But he answered his father, \'Look, all these years I have been serving you, and I have never disobeyed your command; yet you have never given me a young goat so that I might celebrate with my friends.', page='212–213'),
 W15('15:30', 'But when this son of yours came, who has devoured your living with prostitutes, you killed the fattened calf for him!\'', page='213'),
 W15('15:31', 'And he said to him, \'Child, you are always with me, and all that is mine is yours.', page='213'),
 W15('15:32', 'But it was right to celebrate and rejoice, because this brother of yours was dead and has come to life; he was lost and is found.\'"', page='213'),
]

OMITTED = [
]

PREAMBLE = (
 "The lost found. Tax collectors and sinners come to listen to Jesus, and the Pharisees complain that he eats with them. He "
 "answers with two parables: a man who leaves the ninety-nine sheep to look for the one that is lost, and a woman who sweeps "
 "the house for a lost coin. Each rejoices with friends at finding it, and so there is joy over one sinner who repents. "
 "Tertullian's point is that only the one who owned what was lost could look for it (Marc. 4.32). Then the parable of the two "
 "sons: the younger takes his share, scatters it in a far country, comes to himself, rises and goes to his father, who runs to "
 "meet him, clothes him and holds a feast; the elder will not go in, and the father comes out and pleads with him (15:11–32). "
 "Epiphanius states that \"the whole parable of the two sons\" was absent from Marcion's text; it is printed as restored by "
 "method (METHOD §11; see the notes)."
)

NOTES = [
 dict(term='The sheep and the coin (15:1–10)', cat='textual', refs=['15:1', '15:3', '15:4', '15:8', '15:10'], text=(
  "Tertullian, Marc. 4.32.1–2: \"Who looks for the lost sheep and the lost coin? Surely the one who lost them. And who lost "
  "them? The one who had them. And who had them? The one whose they were.\" Since man belongs to the Creator, he concludes, "
  "the joy over the sinner's repentance is the Creator's, \"who said long ago that he prefers the repentance of a sinner to his "
  "death\" (Ezek 18:23). 15:1–2 are not cited. They are printed in grey because the parables answer them.")),
 dict(term='Restored by method, against Marcion\'s text: the two sons (15:11–32)', cat='textual', refs=['15:2', '15:7', '15:10', '15:17', '15:18', '15:20', '15:23', '15:24', '15:28'], text=(
  "Epiphanius, sch. 42: \"again he cut out the whole parable of the two sons, the one who took his share of the property and "
  "spent it wastefully, and the other\". Tertullian, after the coin, goes to the two masters (16:13); the parable would have "
  "served him. The witnesses agree that it was not in Marcion's text. It is printed as restored by method (METHOD §11), against "
  "Marcion's text. By its words: 15:1–2 sets two movements going, the sinners received and the Pharisees and scribes grumbling "
  "\"this man welcomes sinners and eats with them\". The sheep and the coin answer the welcoming. Only this parable answers the "
  "eating (\"let us eat and celebrate\", 15:23) and the grumblers, in the elder son who \"would not go in\" and is pleaded with "
  "(15:28). 15:7 and 15:10 name \"a sinner who repents\", but the sheep and the coin are found and do not repent; the turn itself "
  "is shown only here: \"coming to himself… rising, I will go to my father\" (15:17–20). By its mechanics: it is the text's "
  "fullest statement of the rising (ἀναστάς) that goes to the father, of the son clothed by the father (ἐνδύσατε, 15:22; cf. "
  "12:22, 12:28, 24:49), and of \"was dead and is alive again\" (cf. \"the Living One\", 24:5). Reading: "
  "docs/research/correspondence/word_by_word.md (chapter 13); third_pass.md. The Greek is NA27, checked on the page images "
  "(pp. 211–213); at 15:16 NA27 reads χορτασθῆναι ἐκ, \"to be filled with\".")),
 dict(term='Owner and lost', cat='theological', refs=['15:4', '15:6', '15:7'], text=(
  "Interpretation. Tertullian's argument, \"no one looks for what he never had\", is aimed at the Marcionite claim that a "
  "stranger God redeems humans who were not his. The attested parables themselves say only that the one who lost the sheep "
  "or coin is the one who looks for it and rejoices. The two sons, absent from Marcion's copy and printed here by method, "
  "carries the theme of return from the side of the one who returns: the own asks for its share, scatters it, comes to "
  "itself, rises and goes to the father, and is met while still far off.")),
]
