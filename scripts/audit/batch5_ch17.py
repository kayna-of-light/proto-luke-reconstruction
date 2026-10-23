"""Batch 5, chapter 17 of the reconstruction: Luke 19:1–48 (19:1–26 printed)."""
from buildlib import greek
from batch1_ch2 import U, A
from batch5_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}

T371 = T('4.37.1', '"Consequitur et Zachaei domus salutem… exceptum domo sua pascens dominum… in omnia misericordiae opera dimidium substantiae offerens… dicendo, Et si cui quid per calumniam eripui, quadruplum reddo. Itaque dominus, Hodie, inquit, salus huic domui."')
T374 = T('4.37.4', '"Servorum quoque parabola, qui secundum rationem feneratae pecuniae dominicae diiudicantur, iudicem ostendit deum, etiam ex parte severitatis, non tantum honorantem verum et auferentem quod quis videatur habuisse. Aut si et hic creatorem finxerit austerum, tollentem quod non posuerit et metentem quod non severit…"')

ENTRIES = [
 U('19:1', G('19:1'), 'He entered Jericho and was passing through.', 'Inside the attested pericope 19:1–10.'),
 A('19:2', G('19:2'), 'And there was a man named Zacchaeus; he was a chief tax collector and was rich.',
   'present (Marc. 4.37.1)', [T371]),
 U('19:3', G('19:3'), 'He was trying to see who Jesus was, but on account of the crowd he could not, because he was small in stature.', 'Inside the attested pericope 19:1–10.'),
 U('19:4', G('19:4'), 'So he ran ahead and climbed up into a sycamore tree to see him, for he was about to pass that way.', 'Inside the attested pericope 19:1–10.'),
 U('19:5', G('19:5'), 'And when Jesus came to the place, he looked up and said to him, "Zacchaeus, hurry and come down, for I must stay at your house today."', 'Inside the attested pericope 19:1–10.'),
 A('19:6', G('19:6'), 'So he hurried and came down and received him joyfully.',
   'present (Marc. 4.37.1)', [T('4.37.1', '"exceptum domo sua pascens dominum".')]),
 U('19:7', G('19:7'), 'And when they saw it, they all grumbled, "He has gone in to be the guest of a man who is a sinner."', 'Inside the attested pericope 19:1–10.'),
 A('19:8', G('19:8'), 'Zacchaeus stood and said to the Lord, "Look, Lord, half of my possessions I give to the poor, and if I have defrauded anyone of anything, I restore it fourfold."',
   'present (Marc. 4.37.1)', [T371], wording='NA27. Tertullian\'s order of the elements varies; Roth: order uncertain.'),
 A('19:9', G('19:9'), 'And Jesus said to him, "Today salvation has come to this house, since he also is a son of Abraham.',
   'present (Marc. 4.37.1)', [T371]),
 A('19:10', G('19:10'), 'For the son of man came to seek and to save the lost."',
   'present (Marc. 4.37.2)', [T('4.37.2', '"Cum vero dicit, Venit enim filius hominis salvum facere quod periit…"')],
   wording='NA27. Tertullian does not have "to seek"; Roth: it "may not have been present". Printed.'),
 A('19:11', G('19:11'), 'As they heard these things, he went on to tell a parable, because he was near Jerusalem and because they supposed that the kingdom of God was to appear immediately.',
   'present (Marc. 4.37.4)', [T374]),
 U('19:12', G('19:12'), 'He said therefore, "A nobleman went into a far country to receive for himself a kingdom and then return.', 'Inside the attested parable 19:11–27.'),
 A('19:13', G('19:13'), 'Calling ten of his servants, he gave them ten minas, and said to them, \'Engage in business until I come.\'',
   'present (Marc. 4.37.4; 4.39.11)', [T374, T('4.39.11', '"relicta pecunia servis qua feneraretur".')]),
 U('19:14', G('19:14'), 'But his citizens hated him and sent a delegation after him, saying, \'We do not want this man to reign over us.\'', 'Inside the attested parable 19:11–27.'),
 U('19:15', G('19:15'), 'When he returned, having received the kingdom, he ordered these servants to whom he had given the money to be called to him, that he might know what they had gained by doing business.', 'Inside the attested parable 19:11–27.'),
 U('19:16', G('19:16'), 'The first came before him, saying, \'Lord, your mina has made ten minas more.\'', 'Inside the attested parable 19:11–27.'),
 U('19:17', G('19:17'), 'And he said to him, \'Well done, good servant! Because you have been faithful in a very little, you shall have authority over ten cities.\'', 'Inside the attested parable 19:11–27.'),
 U('19:18', G('19:18'), 'And the second came, saying, \'Lord, your mina has made five minas.\'', 'Inside the attested parable 19:11–27.'),
 U('19:19', G('19:19'), 'And he said to him, \'And you are to be over five cities.\'', 'Inside the attested parable 19:11–27.'),
 U('19:20', G('19:20'), 'Then another came, saying, \'Lord, here is your mina, which I kept laid away in a handkerchief;', 'Inside the attested parable 19:11–27.'),
 U('19:21', G('19:21'), 'for I was afraid of you, because you are a severe man. You take what you did not deposit, and reap what you did not sow.\'', 'Inside the attested parable 19:11–27.'),
 A('19:22', G('19:22'), 'He said to him, \'I will condemn you with your own words, you wicked servant! You knew that I was a severe man, taking what I did not deposit and reaping what I did not sow?',
   'present (Marc. 4.37.4)', [T374]),
 A('19:23', G('19:23'), 'Why then did you not put my money in the bank, and at my coming I might have collected it with interest?\'',
   'present (Marc. 4.37.4)', [T('4.37.4', '"hic quoque me ille instruit cuius pecuniam ut fenerem edocet".')]),
 U('19:24', G('19:24'), 'And he said to those who stood by, \'Take the mina from him, and give it to the one who has the ten minas.\'', 'Inside the attested parable 19:11–27.'),
 U('19:25', G('19:25'), 'And they said to him, \'Lord, he has ten minas!\'', 'Inside the attested parable 19:11–27.'),
 A('19:26', G('19:26'), '\'I tell you that to everyone who has, more will be given; but from the one who has not, even what he has will be taken away.',
   'present (Marc. 4.37.4)', [T374],
   wording='NA27. Tertullian\'s "what he seems to have" (quod quis videatur habuisse) is cited by NA27 for Marcion (ὃ δοκεῖ ἔχειν, with Θ 69 syc.h**); Roth: possible only (cf. 8:18). Not adopted.'),
]

OMITTED = [
 dict(ref='19:27', cls='U−', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason=('"But as for these enemies of mine, who did not want me to reign over them, bring them here and slaughter them before me." Tertullian\'s point in 4.37.4 is that the parable shows God as a judge "even on the side of severity", and he finds that severity in the master taking away what the servant seemed to have (19:26). '
              'The command to slaughter the master\'s enemies would have been his strongest evidence, and he does not cite it. The verse ends the NA27 paragraph 19:11–27.'))),
 dict(ref='19:28', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='"After he had said this, he went on ahead, going up to Jerusalem." A one-verse NA27 paragraph with no attested verse; it introduces the entry (19:29–46), which Epiphanius says was absent.')),
 dict(ref='19:29–46', cls='A−', app=dict(roth='absent', witnesses=[
      E(53, 'παρέκοψεν τὸ κεφάλαιον τὸ περὶ τῆς ὄνου καὶ Βηθφαγὴ καὶ τὸ περὶ τῆς πόλεως καὶ τοῦ ἱεροῦ, ὅτι γεγραμμένον ἦν »ὁ οἶκός μου οἶκος προσευχῆς κληθήσεται, καὶ ποιεῖτε αὐτὸν σπήλαιον λῃστῶν«.')],
      decision='not printed', reason='Epiphanius states that the text lacked the section on the colt and Bethphage, the lament over the city, and the cleansing of the temple with its quotation "my house shall be called a house of prayer". Tertullian passes from 19:26 (4.37.4) to 20:1–8 (4.38.1); Roth counts his silence as confirmation (tacitus).')),
 dict(ref='19:47–48', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='"He was teaching daily in the temple…" A separate NA27 paragraph with no attested verse (METHOD §4.3). Tertullian refers to his teaching by day in the temple only at 21:37 (4.39.19).')),
]

PREAMBLE = (
 "Zacchaeus and the money entrusted to the servants. In Jericho, Zacchaeus, a rich chief tax collector, receives Jesus into "
 "his house, gives half his goods to the poor and restores fourfold what he has taken by fraud. \"Today salvation has come to "
 "this house… for the son of man came to seek and to save the lost.\" Jesus then tells of a nobleman who gives his servants "
 "money to trade with and, on his return, judges them by what they have done with it. In this text the parable ends with "
 "\"from the one who has not, even what he has will be taken away\". The slaughter of the master's enemies (19:27) is not "
 "cited. The entry into Jerusalem, the lament over the city and the cleansing of the temple (19:29–46) are absent: "
 "Epiphanius states that the text lacked them."
)

NOTES = [
 dict(term='Zacchaeus (19:1–10)', cat='textual', refs=['19:2', '19:6', '19:8', '19:9', '19:10'], text=(
  "Tertullian, Marc. 4.37.1–3: \"the house of Zacchaeus also attains salvation\". Zacchaeus received the Lord and fed him, "
  "offered half his goods for works of mercy and said \"if I have taken anything from anyone by false accusation, I restore it "
  "fourfold\"; \"Today, he said, salvation to this house.\" Tertullian reads this as Isaiah 58:7 fulfilled, and \"the son of "
  "man came to save what was lost\" as the salvation of the whole person, body and soul. 19:1, 19:3–5 and 19:7 are not cited "
  "and are printed in grey.")),
 dict(term='The money entrusted to the servants (19:11–26)', cat='textual', refs=['19:11', '19:13', '19:22', '19:23', '19:26'], text=(
  "Tertullian, Marc. 4.37.4: \"the parable of the servants who are judged according to the account of their master's money "
  "lent at interest shows God as judge, even on the side of severity\". He has the \"austere\" master \"taking what he did not "
  "deposit and reaping what he did not sow\", and taking away \"what one seemed to have\". He mentions the parable again at "
  "4.39.11 (\"leaving money with his servants to trade with\"). The unattested verses of the parable are printed in grey.")),
 dict(term='Not printed: 19:27–48', cat='excision', refs=['19:26'], text=(
  "19:27, the slaughter of the enemies who did not want the nobleman to reign, is not cited by Tertullian, though his point "
  "was the master's severity; it is classed probably absent. 19:29–46 are absent by Epiphanius' statement (sch. 53): the "
  "colt and Bethphage, the city, and the temple with \"my house shall be called a house of prayer\". 19:28 and 19:47–48, the "
  "verses that frame them, form paragraphs with no attested verse. In this text Jesus goes from the parable to the question "
  "about his authority (20:1–8) without a royal entry into Jerusalem or the cleansing of the temple.")),
 dict(term='No triumphal entry', cat='theological', refs=['19:26'], text=(
  "Interpretation. Without 19:29–46, the text has no royal entry on a colt and no action against the traders in the temple, "
  "the scenes in which canonical Luke presents Jesus as king and judge of the temple. In the attested text Jesus is in the "
  "temple teaching (20:1; 21:37), and the authorities question his authority there. Epiphanius' charge is that Marcion cut "
  "these scenes out. On the Marcionite-priority view, canonical Luke added them. The witnesses establish only that they were "
  "absent from the text.")),
]
