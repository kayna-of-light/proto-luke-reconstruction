"""Batch 4, chapter 13 of the reconstruction: Luke 15:1–32 (15:1–10 printed)."""
from buildlib import greek
from batch1_ch2 import U, A
from batch4_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}

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
 A('15:10', G('15:10'), 'Just so, I tell you, there is joy before the angels of God over one sinner who repents."',
   'present (Marc. 4.32.2)', [T('4.32.2', '"exultare illius est de paenitentia peccatoris".')],
   wording='NA27. Roth notes that "the angels of" may not have been present; no witness states it. Printed.'),
]

OMITTED = [
 dict(ref='15:11–32', cls='A−', app=dict(roth='absent', witnesses=[
      E(42, 'πάλιν παρέκοψε πᾶσαν τὴν παραβολὴν τῶν δύο υἱῶν, τοῦ εἰληφότος τὸ μέρος τῶν ὑπαρχόντων καὶ ἀσώτως δαπανήσαντος καὶ τοῦ ἄλλου.')],
      decision='not printed', reason='Epiphanius states that the whole parable of the two sons was not in the text. Tertullian passes from the coin (4.32.2) to the two masters (16:13, 4.33.1); Roth counts his silence as confirmation (tacitus). A parable of a father who receives a returning son would have served Tertullian\'s argument that the God who rejoices over the repentant is the one who "prefers the repentance of a sinner to his death" (Ezek 18:23).')),
]

PREAMBLE = (
 "The lost found. Tax collectors and sinners come to listen to Jesus, and the Pharisees complain that he eats with them. He "
 "answers with two parables: a man who leaves the ninety-nine sheep to look for the one that is lost, and a woman who sweeps "
 "the house for a lost coin. Each rejoices with friends at finding it, and so there is joy over one sinner who repents. "
 "Tertullian's point is that only the one who owned what was lost could look for it (Marc. 4.32). The parable of the two sons "
 "(15:11–32) is not in this text: Epiphanius states that \"the whole parable of the two sons\" was absent."
)

NOTES = [
 dict(term='The sheep and the coin (15:1–10)', cat='textual', refs=['15:1', '15:3', '15:4', '15:8', '15:10'], text=(
  "Tertullian, Marc. 4.32.1–2: \"Who looks for the lost sheep and the lost coin? Surely the one who lost them. And who lost "
  "them? The one who had them. And who had them? The one whose they were.\" Since man belongs to the Creator, he concludes, "
  "the joy over the sinner's repentance is the Creator's, \"who said long ago that he prefers the repentance of a sinner to his "
  "death\" (Ezek 18:23). 15:1–2 are not cited. They are printed in grey because the parables answer them.")),
 dict(term='Not printed: 15:11–32', cat='excision', refs=['15:10'], text=(
  "Epiphanius, sch. 42: \"again he cut out the whole parable of the two sons, the one who took his share of the property and "
  "spent it wastefully, and the other\". Tertullian, after the coin, goes to the two masters (16:13). The parable would have "
  "served him: its father receives back a son who left his house, the Creator's own image of repentance. Two witnesses agree "
  "that it was not there. \"Cut out\" is Epiphanius' charge; the content of his statement is that the parable was absent.")),
 dict(term='Owner and lost', cat='theological', refs=['15:4', '15:6', '15:7'], text=(
  "Interpretation. Tertullian's argument, \"no one looks for what he never had\", is aimed at the Marcionite claim that a "
  "stranger God redeems humans who were not his. The attested parables themselves say only that the one who lost the sheep "
  "or coin is the one who looks for it and rejoices. The Prodigal Son, which carries the theme of return most fully in "
  "canonical Luke, is absent here; in this text the theme rests on the two short parables alone.")),
]
