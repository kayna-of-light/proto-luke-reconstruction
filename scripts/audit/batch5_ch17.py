"""Batch 5, chapter 17 of the reconstruction: Luke 19:1–48 (19:1–26 printed; 19:27–46 restored by method, METHOD §11)."""
from buildlib import greek, R
from batch1_ch2 import U, A
from batch5_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}

E53 = E(53, 'παρέκοψεν τὸ κεφάλαιον τὸ περὶ τῆς ὄνου καὶ Βηθφαγὴ καὶ τὸ περὶ τῆς πόλεως καὶ τοῦ ἱεροῦ, ὅτι γεγραμμένον ἦν »ὁ οἶκός μου οἶκος προσευχῆς κληθήσεται, καὶ ποιεῖτε αὐτὸν σπήλαιον λῃστῶν«.')
CR_19_28 = '"After he had said this, he went on ahead, going up to Jerusalem." A one-verse NA27 paragraph with no attested verse; it introduces the entry (19:29–46).'
CR_19_29 = ('Epiphanius (sch. 53) states that the text lacked the section on the colt and Bethphage, the lament over the city, and the cleansing of the temple with its quotation '
            '"my house shall be called a house of prayer". Tertullian passes from 19:26 (4.37.4) to 20:1–8 (4.38.1); Roth counts his silence as confirmation (tacitus).')
GR_19 = ('by its mechanics, the road set at 9:51 ("he set his face to go to Jerusalem") is named again at 17:11 and 19:11 ("because he was near Jerusalem"), and without '
         '19:28–46 it never arrives: from "near Jerusalem" the text goes to "in the temple" (20:1), with no going up, no descent of the mountain with "peace in heaven, '
         'and glory in the highest", no weeping over the city whose peace is hidden from its eyes, and no entering the house of prayer. By its words, 20:2 "by what authority '
         'do you do these things?" has its first object in 19:45–46. Reading: docs/research/correspondence/word_by_word.md, chapter 17, tests of 19:28 and 19:29–46.')
W28 = lambda ref, en: R(ref, G(ref), en, 'U?', 'unattested', CR_19_28, GR_19, wording='NA27 (checked on the page image, p. 223).')
AGAINST = (' Printed against Marcion\'s text: the witnesses state that the passage was not in it.')
WA = lambda ref, en, page='224', note='': R(ref, G(ref), en, 'A−', 'absent', CR_19_29, GR_19 + AGAINST, witnesses=[E53],
                                         wording=f'NA27 (checked on the page image, p. {page}).{note}')

T371 = T('4.37.1', '"Consequitur et Zachaei domus salutem… exceptum domo sua pascens dominum… in omnia misericordiae opera dimidium substantiae offerens… dicendo, Et si cui quid per calumniam eripui, quadruplum reddo. Itaque dominus, Hodie, inquit, salus huic domui."')
T374 = T('4.37.4', '"Servorum quoque parabola, qui secundum rationem feneratae pecuniae dominicae diiudicantur, iudicem ostendit deum, etiam ex parte severitatis, non tantum honorantem verum et auferentem quod quis videatur habuisse. Aut si et hic creatorem finxerit austerum, tollentem quod non posuerit et metentem quod non severit…"')

CR_19_27 = ('"But as for these enemies of mine, who did not want me to reign over them, bring them here and slaughter them before me." Tertullian\'s point in 4.37.4 is that the parable shows God as a judge "even on the side of severity", and he finds that severity in the master taking away what the servant seemed to have (19:26). '
            'The command to slaughter the master\'s enemies would have been his strongest evidence, and he does not cite it.')
GR_19_27 = ('by its mechanics, the parable sets two groups going at the departure: the servants given money (19:13) and the citizens who refuse his reign (19:14). He returns "having received the kingdom" (19:15) and reckons with the servants (19:15–26); '
            'the citizens are reckoned with only here. Read inwardly, the enemies who refuse his reign are what in the person refuses it, and their death "before him" is that refusal ended in his presence: the enemy\'s power trodden (10:19), the enemies a footstool (20:43). '
            'In the final text the parable frames the going up and the king hailed (19:28, 19:38). Reading: docs/research/correspondence/word_by_word.md, chapter 17, test of 19:27; second_pass.md §2.')

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
 R('19:27', G('19:27'), 'But as for these enemies of mine, who did not want me to reign over them, bring them here and slaughter them before me.\'"',
   'U−', 'unattested', CR_19_27, GR_19_27, wording='NA27 (checked on the page image, p. 223).'),
 W28('19:28', 'After he had said this, he went on ahead, going up to Jerusalem.'),
 WA('19:29', 'When he drew near to Bethphage and Bethany, at the mountain called the Mount of Olives, he sent two of the disciples,', page='223', note=' NA27 prints Βηθανία[ν]; printed without the brackets (METHOD §5.7).'),
 WA('19:30', 'saying, "Go into the village opposite, where as you enter you will find a colt tied, on which no one has ever sat; untie it and bring it.', page='223–224'),
 WA('19:31', 'If anyone asks you, \'Why are you untying it?\' you shall say this: \'The Lord has need of it.\'"'),
 WA('19:32', 'Those who were sent went away and found it as he had told them.'),
 WA('19:33', 'As they were untying the colt, its owners said to them, "Why are you untying the colt?"'),
 WA('19:34', 'They said, "The Lord has need of it."'),
 WA('19:35', 'And they brought it to Jesus, and throwing their cloaks on the colt they set Jesus on it.'),
 WA('19:36', 'As he went along, they spread their cloaks on the road.', note=' αὐτῶν (SBLGNT ἑαυτῶν).'),
 WA('19:37', 'As he was now drawing near, at the descent of the Mount of Olives, the whole multitude of the disciples began to praise God joyfully with a loud voice for all the deeds of power they had seen,'),
 WA('19:38', 'saying, "Blessed is the one who comes, the king, in the name of the Lord! Peace in heaven, and glory in the highest!"', note=' ὁ ἐρχόμενος ὁ βασιλεύς (SBLGNT ὁ ἐρχόμενος βασιλεύς).'),
 WA('19:39', 'And some of the Pharisees in the crowd said to him, "Teacher, rebuke your disciples."'),
 WA('19:40', 'He answered, "I tell you, if these are silent, the stones will cry out."', note=' Without ὅτι (SBLGNT has it).'),
 WA('19:41', 'And as he drew near and saw the city, he wept over it,'),
 WA('19:42', 'saying, "If you, even you, had known on this day the things that make for peace! But now they are hidden from your eyes.'),
 WA('19:43', 'For days will come upon you when your enemies will set up a palisade against you and surround you and hem you in on every side,', page='225'),
 WA('19:44', 'and they will dash you to the ground, you and your children within you, and they will not leave within you one stone upon another, because you did not know the time of your visitation."', page='225'),
 WA('19:45', 'And he entered the temple and began to drive out those who were selling,', page='225'),
 WA('19:46', 'saying to them, "It is written, \'And my house shall be a house of prayer,\' but you have made it a den of robbers."', page='225'),
]

OMITTED = [
 dict(ref='19:47–48', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='"He was teaching daily in the temple…" A separate NA27 paragraph with no attested verse (METHOD §4.3). Tertullian refers to his teaching by day in the temple only at 21:37 (4.39.19).')),
]

PREAMBLE = (
 "Zacchaeus and the money entrusted to the servants. In Jericho, Zacchaeus, a rich chief tax collector, receives Jesus into "
 "his house, gives half his goods to the poor and restores fourfold what he has taken by fraud. \"Today salvation has come to "
 "this house… for the son of man came to seek and to save the lost.\" Jesus then tells of a nobleman who gives his servants "
 "money to trade with and, on his return, judges them by what they have done with it. In this text the parable ends with "
 "\"from the one who has not, even what he has will be taken away\", and the citizens who refused his reign are brought before "
 "him (19:27, not cited by any witness; printed as restored by method). Then Jesus goes up to Jerusalem: the colt, the descent of the Mount of Olives with \"peace in heaven, and glory in the "
 "highest\", the weeping over the city, and the entry into the temple (19:28–46). Epiphanius states that Marcion's text lacked "
 "19:29–46. The passage is printed here as restored by method, against Marcion's text, because the reading of the printed "
 "text shows that it needs the arrival (METHOD §11; see the notes)."
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
 dict(term='Restored by method, against Marcion\'s text: 19:28–46', cat='textual', refs=['19:28', '19:29', '19:37', '19:38', '19:41', '19:45', '19:46'], text=(
  "Epiphanius, Pan. 42.11.6, sch. 53: παρέκοψεν τὸ κεφάλαιον τὸ περὶ τῆς ὄνου καὶ Βηθφαγὴ καὶ τὸ περὶ τῆς πόλεως καὶ τοῦ "
  "ἱεροῦ — the section on the colt and Bethphage, the city, and the temple with \"my house shall be called a house of prayer\" "
  "were not in Marcion's text. Tertullian passes from 19:26 (4.37.4) to 20:1–8 (4.38.1), and Roth counts his silence as "
  "confirmation. 19:28 (\"he went on ahead, going up to Jerusalem\") is not cited by any witness (U?). The whole of 19:28–46 is "
  "printed as restored by method (METHOD §11), and 19:29–46 is printed against Marcion's text as the witnesses report it. "
  "The grounds are in the printed text. By its mechanics: the road set at 9:51 (\"he set his face to go to Jerusalem\") is "
  "named again at 17:11 and 19:11 (\"because he was near Jerusalem\"), and without this passage it never arrives. From \"near "
  "Jerusalem\" the text would go straight to \"in the temple\" (20:1): no going up, no descent of the mountain with \"peace in "
  "heaven, and glory in the highest\", no weeping over the city whose peace is hidden from its eyes, no entering the house of "
  "prayer. By its words: 20:2, \"by what authority do you do these things?\", has its first object in 19:45–46. The reading is in "
  "docs/research/correspondence/word_by_word.md (chapter 17, tests of 19:28 and 19:29–46). The Greek is NA27, checked on the page "
  "images (pp. 223–225); it differs from SBLGNT at 19:36 (αὐτῶν), 19:38 (ὁ ἐρχόμενος ὁ βασιλεύς) and 19:40 (without ὅτι).")),
 dict(term='Restored by method: the citizens who refused (19:27)', cat='textual', refs=['19:14', '19:15', '19:26', '19:27'], text=(
  "19:27, the slaughter of the enemies who did not want the nobleman to reign, is not cited by Tertullian, though his point "
  "was the master's severity (4.37.4); it is classed probably absent (U−). It is printed as restored by method (METHOD §11), "
  "against that class. By its mechanics: the parable sets two groups going at the departure, the servants (19:13) and the "
  "citizens who say \"we do not want this man to reign over us\" (19:14); the master returns \"having received the kingdom\" "
  "(19:15) and reckons with the servants, and only 19:27 reckons with the citizens. Read inwardly, as the text's persons are "
  "read throughout, the enemies who refuse his reign are what in the person refuses it, and their death \"before him\" is that "
  "refusal ended in his presence: the enemy's power trodden (10:19), the enemies made a footstool (20:43). The enemy as person "
  "is loved (6:27). Reading: docs/research/correspondence/word_by_word.md (chapter 17, test of 19:27); second_pass.md §2.")),
 dict(term='Not printed: 19:47–48', cat='excision', refs=['19:46'], text=(
  "19:47–48 (\"he was teaching daily in the temple…\") forms a paragraph with no attested verse. The correspondential reading "
  "tested it at its place: it continues the line, and nothing printed needs it; 20:1 opens \"as he was teaching the people in "
  "the temple\".")),
 dict(term='The entry in this text', cat='theological', refs=['19:28', '19:38', '19:46'], text=(
  "Interpretation. In Marcion's text as the witnesses report it there is no entry on a colt and no action in the temple: "
  "Epiphanius' charge is that Marcion cut these scenes out, and on the Marcionite-priority view canonical Luke added them. "
  "The witnesses establish only that they were absent from Marcion's copy. This edition prints them on another ground, the "
  "reading of its own printed text (METHOD §11): the road to Jerusalem is the line the whole text runs on, and the passage is "
  "its arrival. Read so, the entry is not a royal claim. He goes up; he comes down the mountain to the praise of \"peace in "
  "heaven\"; he weeps over the city because its peace is hidden from its eyes; and he enters the house that is to be a house of "
  "prayer.")),
]
