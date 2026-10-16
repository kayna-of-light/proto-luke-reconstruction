"""Batch 4, chapter 13 of the reconstruction: Luke 15:1–32 (15:1–10 printed)."""
from buildlib import greek
from batch1_ch2 import U, A
from batch4_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}

ENTRIES = [
 U('15:1', G('15:1'), 'And all the tax collectors and the sinners were drawing near to him to hear him.',
   'A separate NA27 paragraph, but part of the attested pericope: 15:3 ("he told them this parable") answers the complaint of 15:2.'),
 U('15:2', G('15:2'), 'And both the Pharisees and the scribes were grumbling, saying, "This man receives sinners and eats with them."',
   'Part of the attested pericope 15:1–10 (see 15:1).'),
 A('15:3', G('15:3'), 'And he spoke this parable to them, saying,',
   'present (Marc. 4.32.2)', [T('4.32.2', '"Ita utriusque parabolae argumentum…"')]),
 A('15:4', G('15:4'), '"What person among you, having a hundred sheep and having lost one of them, does not leave the ninety-nine in the desert and journey after the one that is lost until he finds it?',
   'present (Marc. 4.32.1)', [T('4.32.1', '"Ovem et dragmam perditam quis requirit? nonne qui perdidit? Quis autem perdidit? nonne qui habuit?"')]),
 A('15:5', G('15:5'), 'And having found it, he lays it on his shoulders, rejoicing,',
   'present (Marc. 4.32.1)', [T('4.32.1', '"is invenit qui quaesivit".')]),
 A('15:6', G('15:6'), "and coming into the house, he calls together the friends and the neighbours, saying to them, 'Rejoice with me, because I have found my sheep that was lost.'",
   'present (Marc. 4.32.1)', [T('4.32.1', '"is exultavit qui invenit".')]),
 A('15:7', G('15:7'), 'I tell you that in the same way there will be joy in heaven over one sinner who changes his mind, rather than over ninety-nine just people who have no need of a change of mind.',
   'present (Marc. 4.32.2)', [T('4.32.2', '"Atque adeo exultare illius est de paenitentia peccatoris, id est de perditi recuperatione, qui se professus est olim malle peccatoris paenitentiam quam mortem."')],
   wording='NA27. Tertullian\'s "joy over the repentance of a sinner" may come from 15:7 or 15:10 (Roth).'),
 A('15:8', G('15:8'), 'Or what woman, having ten drachmas, if she loses one drachma, does not light a lamp and sweep the house and seek carefully until she finds it?',
   'present (Marc. 4.32.1)', [T('4.32.1', '"Ovem et dragmam perditam quis requirit?"')]),
 A('15:9', G('15:9'), "And having found it, she calls together the women friends and neighbours, saying, 'Rejoice with me, because I have found the drachma that I lost.'",
   'present (Marc. 4.32.1)', [T('4.32.1', '"is invenit qui quaesivit, is exultavit qui invenit".')]),
 A('15:10', G('15:10'), 'In the same way, I tell you, there comes to be joy before the messengers of God over one sinner who changes his mind."',
   'present (Marc. 4.32.2)', [T('4.32.2', '"exultare illius est de paenitentia peccatoris".')],
   wording='NA27. Roth notes that "the messengers of" may not have been present; no witness states it. Printed.'),
]

OMITTED = [
 dict(ref='15:11–32', cls='A−', app=dict(roth='absent', witnesses=[
      E(42, 'πάλιν παρέκοψε πᾶσαν τὴν παραβολὴν τῶν δύο υἱῶν, τοῦ εἰληφότος τὸ μέρος τῶν ὑπαρχόντων καὶ ἀσώτως δαπανήσαντος καὶ τοῦ ἄλλου.')],
      decision='not printed', reason='Epiphanius states that the whole parable of the two sons was not in the text. Tertullian passes from the coin (4.32.2) to the two masters (16:13, 4.33.1); Roth counts his silence as confirmation (tacitus). A parable of a father who receives a returning son would have served Tertullian\'s argument that the God who rejoices over the repentant is the one who "prefers the repentance of a sinner to his death" (Ezek 18:23).')),
]

PREAMBLE = (
 "Most of what we are has never strayed: ninety-nine parts that stay where they are put and need nothing "
 "changed. One has gone missing, and that is where the whole attention goes.\n\n"
 "The ninety-nine are left in the wilderness. The lost one is followed until it is found, and then it is not "
 "driven home but carried, on the shoulders, with joy. Everyone nearby is called in to rejoice.\n\n"
 "The second loss is not a living thing but silver: one coin out of ten, lost inside the house itself. A lamp is"
 " lit. The whole house is swept and searched, every corner, until it turns up.\n\n"
 "Neither of them is scolded. Neither is asked where it has been.\n\n"
 "There is more joy over one that turns than over all that never needed to."
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
 dict(term='ἦσαν… ἐγγίζοντες, "were drawing near"', cat='translation', refs=['15:1'], text='The imperfect with a participle: they kept coming near.'),
 dict(term='διεγόγγυζον, "were grumbling"', cat='translation', refs=['15:2'], text='γογγύζω as at 5:30, strengthened with δια-.'),
 dict(term='προσδέχεται, "receives"', cat='translation', refs=['15:2'], text='To receive, welcome, admit.'),
 dict(term='συνεσθίει, "eats with"', cat='translation', refs=['15:2'], text='One word: "eats together with".'),
 dict(term='ἀπολέσας… τὸ ἀπολωλός, "having lost… the one that is lost"', cat='translation', refs=['15:4'], text='ἀπόλλυμι, the verb of "destroy" (4:34) and "perish" (8:24). The same verb is "lose" here.'),
 dict(term='ἐν τῇ ἐρήμῳ, "in the desert"', cat='translation', refs=['15:4'], text='As at 4:42.'),
 dict(term='πορεύεται, "journey"', cat='translation', refs=['15:4'], text='The road verb, as at 4:30.'),
 dict(term='ἐπιτίθησιν, "lays"', cat='translation', refs=['15:5'], text='The present tense, kept.'),
 dict(term='συγκαλεῖ, "calls together"', cat='translation', refs=['15:6'], text='καλέω with συν-, as in 14:12.'),
 dict(term='μετανοοῦντι, "who changes his mind"', cat='translation', refs=['15:7'], text="μετανοέω, to change one's mind, as at 5:32."),
 dict(term='ἢ ἐπί, "rather than over"', cat='translation', refs=['15:7'], text='ἤ, "than": the Greek has no word for "more".'),
 dict(term='δικαίοις, "just people"', cat='translation', refs=['15:7'], text='δίκαιος, as at 5:32.'),
 dict(term='δραχμάς, "drachmas"', cat='translation', refs=['15:8'], text="A silver coin, a day's wage."),
 dict(term='σαροῖ, "sweep"', cat='translation', refs=['15:8'], text='To sweep clean.'),
 dict(term='ἐπιμελῶς, "carefully"', cat='translation', refs=['15:8'], text='With care.'),
 dict(term='τὰς φίλας, "the women friends"', cat='translation', refs=['15:9'], text='The Greek is feminine.'),
 dict(term='ἐνώπιον τῶν ἀγγέλων τοῦ θεοῦ, "before the messengers of God"', cat='translation', refs=['15:10'], text='ἄγγελος, messenger, as at 9:26.'),
]
