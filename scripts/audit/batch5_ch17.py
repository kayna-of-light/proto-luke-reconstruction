"""Batch 5, chapter 17 of the reconstruction: Luke 19:1–48 (19:1–26 printed)."""
from buildlib import greek
from batch1_ch2 import U, A
from batch5_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}

T371 = T('4.37.1', '"Consequitur et Zachaei domus salutem… exceptum domo sua pascens dominum… in omnia misericordiae opera dimidium substantiae offerens… dicendo, Et si cui quid per calumniam eripui, quadruplum reddo. Itaque dominus, Hodie, inquit, salus huic domui."')
T374 = T('4.37.4', '"Servorum quoque parabola, qui secundum rationem feneratae pecuniae dominicae diiudicantur, iudicem ostendit deum, etiam ex parte severitatis, non tantum honorantem verum et auferentem quod quis videatur habuisse. Aut si et hic creatorem finxerit austerum, tollentem quod non posuerit et metentem quod non severit…"')

ENTRIES = [
 U('19:1', G('19:1'), 'And going in, he was passing through Jericho.', 'Inside the attested pericope 19:1–10.'),
 A('19:2', G('19:2'), 'And look, a man called by name Zacchaeus; and he was a chief tax collector, and he was rich.',
   'present (Marc. 4.37.1)', [T371]),
 U('19:3', G('19:3'), 'And he was seeking to see Jesus, who he is, and he could not because of the crowd, for he was small in stature.', 'Inside the attested pericope 19:1–10.'),
 U('19:4', G('19:4'), 'And running ahead to the front, he went up into a sycomore-fig tree, so that he might see him, because he was about to pass through that way.', 'Inside the attested pericope 19:1–10.'),
 U('19:5', G('19:5'), 'And when he came to the place, looking up, Jesus said to him, "Zacchaeus, hurry and come down, for today I must stay in your house."', 'Inside the attested pericope 19:1–10.'),
 A('19:6', G('19:6'), 'And he hurried and came down, and received him as a guest, rejoicing.',
   'present (Marc. 4.37.1)', [T('4.37.1', '"exceptum domo sua pascens dominum".')]),
 U('19:7', G('19:7'), 'And seeing it, all were grumbling, saying, "He has gone in to lodge with a sinful man."', 'Inside the attested pericope 19:1–10.'),
 A('19:8', G('19:8'), 'But Zacchaeus, standing, said to the lord, "Look, half of my possessions, lord, I give to the destitute; and if I have extorted anything from anyone, I give it back fourfold."',
   'present (Marc. 4.37.1)', [T371], wording='NA27. Tertullian\'s order of the elements varies; Roth: order uncertain.'),
 A('19:9', G('19:9'), 'And Jesus said to him, "Today salvation has come to this house, because he too is a son of Abraham;',
   'present (Marc. 4.37.1)', [T371]),
 A('19:10', G('19:10'), 'for the son of the human came to seek and to save what was lost."',
   'present (Marc. 4.37.2)', [T('4.37.2', '"Cum vero dicit, Venit enim filius hominis salvum facere quod periit…"')],
   wording='NA27. Tertullian does not have "to seek"; Roth: it "may not have been present". Printed.'),
 A('19:11', G('19:11'), 'And as they were hearing these things, he went on and told a parable, because he was near Jerusalem and they thought that the kingdom of God was about to be shown at once.',
   'present (Marc. 4.37.4)', [T374]),
 U('19:12', G('19:12'), 'So he said, "A certain well-born man journeyed into a far country, to receive a kingdom for himself and return.', 'Inside the attested parable 19:11–27.'),
 A('19:13', G('19:13'), "And calling ten slaves of his, he gave them ten minas and said to them, 'Do business with this while I am coming.'",
   'present (Marc. 4.37.4; 4.39.11)', [T374, T('4.39.11', '"relicta pecunia servis qua feneraretur".')]),
 U('19:14', G('19:14'), "But his citizens hated him, and sent an embassy after him, saying, 'We do not want this man to reign over us.'", 'Inside the attested parable 19:11–27.'),
 U('19:15', G('19:15'), 'And it happened, when he returned having received the kingdom, that he said that these slaves to whom he had given the silver should be called to him, so that he might know what they had gained by doing business.', 'Inside the attested parable 19:11–27.'),
 U('19:16', G('19:16'), "And the first arrived, saying, 'Lord, your mina has earned ten minas more.'", 'Inside the attested parable 19:11–27.'),
 U('19:17', G('19:17'), "And he said to him, 'Well done, good slave! Because you have been trustworthy in a very little, have authority over ten cities.'", 'Inside the attested parable 19:11–27.'),
 U('19:18', G('19:18'), "And the second came, saying, 'Your mina, lord, has made five minas.'", 'Inside the attested parable 19:11–27.'),
 U('19:19', G('19:19'), "And he said to this one also, 'And you, be over five cities.'", 'Inside the attested parable 19:11–27.'),
 U('19:20', G('19:20'), "And the other came, saying, 'Lord, look, your mina, which I kept laid away in a cloth;", 'Inside the attested parable 19:11–27.'),
 U('19:21', G('19:21'), "for I was afraid of you, because you are a harsh man: you take up what you did not lay down, and reap what you did not sow.'", 'Inside the attested parable 19:11–27.'),
 A('19:22', G('19:22'), "He says to him, 'Out of your own mouth I judge you, evil slave. You knew that I am a harsh man, taking up what I did not lay down and reaping what I did not sow?",
   'present (Marc. 4.37.4)', [T374]),
 A('19:23', G('19:23'), "And why did you not put my silver on a bank table? And I, coming, would have collected it with interest.'",
   'present (Marc. 4.37.4)', [T('4.37.4', '"hic quoque me ille instruit cuius pecuniam ut fenerem edocet".')]),
 U('19:24', G('19:24'), "And to those standing by he said, 'Take the mina from him and give it to the one who has the ten minas'—", 'Inside the attested parable 19:11–27.'),
 U('19:25', G('19:25'), "and they said to him, 'Lord, he has ten minas'—", 'Inside the attested parable 19:11–27.'),
 A('19:26', G('19:26'), '\'I tell you that to everyone who has, it will be given; but from the one who does not have, even what he has will be taken away.\'"',
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
 "\"from the one who does not have, even what he has will be taken away\". The slaughter of the master's enemies (19:27) is not "
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
 dict(term='διήρχετο, "was passing through"', cat='translation', refs=['19:1'], text='The imperfect: he was on his way through.'),
 dict(term='ἀρχιτελώνης, "a chief tax collector"', cat='translation', refs=['19:2'], text='Head of the tax and toll collectors of a district.'),
 dict(term='τίς ἐστιν, "who he is"', cat='translation', refs=['19:3'], text='The present tense inside the sentence, as the Greek has it.'),
 dict(term='τῇ ἡλικίᾳ μικρός, "small in stature"', cat='translation', refs=['19:3'], text='ἡλικία, as at 12:25.'),
 dict(term='προδραμών, "running ahead"', cat='translation', refs=['19:4'], text='To run on before.'),
 dict(term='συκομορέαν, "a sycomore-fig tree"', cat='translation', refs=['19:4'], text='A fig tree with mulberry-like leaves, not the European sycamore.'),
 dict(term='ἀναβλέψας, "looking up"', cat='translation', refs=['19:5'], text='ἀναβλέπω, the verb of "see again" (18:41–43), here in its plain sense.'),
 dict(term='σήμερον… δεῖ με μεῖναι, "today I must stay"', cat='translation', refs=['19:5'], text='δεῖ, as at 4:43.'),
 dict(term='ὑπεδέξατο, "received him as a guest"', cat='translation', refs=['19:6'], text="To receive under one's roof."),
 dict(term='διεγόγγυζον, "were grumbling"', cat='translation', refs=['19:7'], text='As at 15:2.'),
 dict(term='καταλῦσαι, "to lodge"', cat='translation', refs=['19:7'], text='As at 9:12.'),
 dict(term='σταθείς, "standing"', cat='translation', refs=['19:8'], text="To stand still, take one's stand."),
 dict(term='τὸν κύριον… κύριε, "the lord… lord"', cat='translation', refs=['19:8'], text="The narrator's word and Zacchaeus' address, both κύριος."),
 dict(term='δίδωμι… ἀποδίδωμι, "I give… I give back"', cat='translation', refs=['19:8'], text='Present tense. It can mean what he now resolves to do, or what he already does. The Greek does not decide.'),
 dict(term='ἐσυκοφάντησα, "I have extorted"', cat='translation', refs=['19:8'], text='To extort by false accusation.'),
 dict(term='τετραπλοῦν, "fourfold"', cat='translation', refs=['19:8'], text='Four times the amount, as the law required for a stolen sheep (Ex 22:1).'),
 dict(term='σωτηρία, "salvation"', cat='translation', refs=['19:9'], text='From σῴζω (7:50): rescue, being made whole.'),
 dict(term='ζητῆσαι καὶ σῶσαι τὸ ἀπολωλός, "to seek and to save what was lost"', cat='translation', refs=['19:10'], text='ἀπόλλυμι, as at 15:4–6. The Greek is neuter: "the lost thing".'),
 dict(term='ἀναφαίνεσθαι, "to be shown"', cat='translation', refs=['19:11'], text='To be brought into view, appear.'),
 dict(term='εὐγενής, "well-born"', cat='translation', refs=['19:12'], text='Of noble birth.'),
 dict(term='λαβεῖν ἑαυτῷ βασιλείαν, "to receive a kingdom for himself"', cat='translation', refs=['19:12'], text='βασιλεία here is royal rule, kingship, as client kings received it from Rome.'),
 dict(term='δέκα μνᾶς, "ten minas"', cat='translation', refs=['19:13'], text="A mina was about a hundred days' wages."),
 dict(term='Πραγματεύσασθε, "do business"', cat='translation', refs=['19:13'], text='To trade.'),
 dict(term='ἐν ᾧ ἔρχομαι, "while I am coming"', cat='translation', refs=['19:13'], text='Literally "in which I come": until I come back.'),
 dict(term='πολῖται, "citizens"', cat='translation', refs=['19:14'], text='The people of his city.'),
 dict(term='πρεσβείαν, "an embassy"', cat='translation', refs=['19:14'], text='A delegation of elders.'),
 dict(term='βασιλεῦσαι, "to reign"', cat='translation', refs=['19:14'], text='The verb of βασιλεία.'),
 dict(term='τὸ ἀργύριον, "the silver"', cat='translation', refs=['19:15'], text='Money, as at 9:3.'),
 dict(term='προσηργάσατο, "has earned… more"', cat='translation', refs=['19:16'], text='To gain by working in addition.'),
 dict(term='Εὖγε, "well done"', cat='translation', refs=['19:17'], text='An exclamation of approval.'),
 dict(term='ἀγαθὲ δοῦλε, "good slave"', cat='translation', refs=['19:17'], text='As at 7:2.'),
 dict(term='ἐν ἐλαχίστῳ πιστός, "trustworthy in a very little"', cat='translation', refs=['19:17'], text='As at 16:10.'),
 dict(term='ἐν σουδαρίῳ, "in a cloth"', cat='translation', refs=['19:20'], text='A Latin word (sudarium), a cloth for wiping sweat.'),
 dict(term='αὐστηρός, "harsh"', cat='translation', refs=['19:21'], text='Severe, strict, hard.'),
 dict(term='λέγει, "he says"', cat='translation', refs=['19:22'], text='The present tense, kept.'),
 dict(term='πονηρὲ δοῦλε, "evil slave"', cat='translation', refs=['19:22'], text='πονηρός, as at 6:45.'),
 dict(term='ἐπὶ τράπεζαν, "on a bank table"', cat='translation', refs=['19:23'], text="τράπεζα, a table, the moneychanger's table: a bank."),
 dict(term='σὺν τόκῳ, "with interest"', cat='translation', refs=['19:23'], text='τόκος, literally "offspring": what money breeds.'),
 dict(term='τοῖς παρεστῶσιν, "to those standing by"', cat='translation', refs=['19:24'], text='His attendants.'),
 dict(term='λέγω ὑμῖν, "I tell you"', cat='translation', refs=['19:26'], text='Whether the master or Jesus speaks this sentence, the Greek does not mark. In this text the parable ends here; 19:27 is not printed.'),
]
