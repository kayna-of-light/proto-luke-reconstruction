"""Batch 4, chapter 12 of the reconstruction: Luke 14:1–35 (14:12–24 printed)."""
from buildlib import greek
from batch1_ch2 import U, A
from batch4_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}

ENTRIES = [
 A('14:12', G('14:12'), 'And he was saying also to the one who had invited him, "When you make a midday meal or a dinner, do not call your friends nor your brothers nor your relatives nor rich neighbours, so that they too do not invite you in return and it becomes a repayment to you.',
   'present (Marc. 4.31.1)', [T('4.31.1', '"Ad prandium vel ad coenam quales vocari iubet? Quales ostenderat per Esaiam…"')]),
 U('14:13', G('14:13'), 'But when you make a reception, call the destitute, the crippled, the lame, the blind;', 'Inside the attested paragraph 14:12–14.'),
 A('14:14', G('14:14'), 'and you will be fortunate, because they have nothing to repay you with; for it will be repaid to you at the rising of the just."',
   'present (Marc. 4.31.1)', [T('4.31.1', '"qui scilicet humanitatis istius vicem retribuere non possint. Hanc si Christus captari vetat, in resurrectione eam repromittens…"')],
   wording='NA27. Tertullian has "in the resurrection" without "of the righteous"; the words are not quoted, and no omission is attested (Roth). Printed.'),
 U('14:15', G('14:15'), 'And one of those reclining at table with him, hearing these things, said to him, "Fortunate is whoever will eat bread in the kingdom of God."',
   'A one-verse NA27 paragraph, but part of the attested pericope: the parable 14:16–24 is the answer to it ("But he said to him").'),
 A('14:16', G('14:16'), 'But he said to him, "A certain person was making a great dinner, and he invited many,',
   'present (Marc. 4.31.1–2)', [T('4.31.1', '"Etiam invitatoris parabola cui magis parti occurrat expende. Homo quidam fecit coenam et vocavit multos."')],
   wording='NA27. Tertullian does not have "great"; Roth: "μέγα may have been present". Printed.'),
 A('14:17', G('14:17'), "and he sent his slave at the hour of the dinner to say to those who had been invited, 'Come, because it is already ready.'",
   'present (Marc. 4.31.3)', [T('4.31.3', '"Dehinc si is mittit ad convivas qui coenam paravit…"')]),
 A('14:18', G('14:18'), "And they all alike began to excuse themselves. The first said to him, 'I have bought a field, and I have need to go out and see it; I ask you, have me excused.'",
   'present (Marc. 4.31.3–4)', [T('4.31.3', '"Excusant se invitati."'), T('4.31.4', '"Agrum emi, et boves mercatus sum, et uxorem duxi."')]),
 A('14:19', G('14:19'), "And another said, 'I have bought five yoke of oxen, and I am journeying to test them; I ask you, have me excused.'",
   'present (Marc. 4.31.4)', [T('4.31.4', '"et boves mercatus sum".')]),
 A('14:20', G('14:20'), "And another said, 'I have married a wife, and because of this I cannot come.'",
   'present (Marc. 4.31.4)', [T('4.31.4', '"et uxorem duxi".')]),
 A('14:21', G('14:21'), "And the slave arrived and reported these things to his lord. Then the master of the house, angered, said to his slave, 'Go out quickly into the streets and lanes of the city, and bring in here the destitute and crippled and blind and lame.'",
   'present (Marc. 4.31.5–6)', [T('4.31.5', '"Hoc ut patrifamiliae renuntiatum est, motus tunc (bene quod et motus, negat enim Marcion moveri deum suum…) mandat de plateis et vicis civitatis facere sublectionem."')],
   wording='NA27. Tertullian\'s "motus" ("moved") is rated possible only as a rendering of a different verb (Roth: ἐπαρθείς?); NA27 ὀργισθείς is printed.'),
 A('14:22', G('14:22'), "And the slave said, 'Lord, what you ordered has been done, and there is still room.'",
   'present (Marc. 4.31.6)', [T('4.31.6', '"Dehinc loco abundante…"')]),
 A('14:23', G('14:23'), "And the lord said to the slave, 'Go out into the roads and hedges and compel them to come in, so that my house may be filled.",
   'present (Marc. 4.31.6)', [T('4.31.6', '"praecepit etiam de viis et sepibus colligi, id est nos iam de extraneis gentibus".')]),
 A('14:24', G('14:24'), 'For I tell you that none of those men who were invited will taste my dinner.\'"',
   'present (Marc. 4.31.6)', [T('4.31.6', '"de qua illos gustaturos negat dominus".')]),
]

OMITTED = [
 dict(ref='14:1–11', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='The man with dropsy healed on the sabbath (14:1–6) and the places at table (14:7–11): two NA27 paragraphs with no attested verse (METHOD §4.3). Tertullian passes from 13:28 (4.30.6) to 14:12 (4.31.1); his "rursus" at 4.30.1 introduces 13:15 (the ox or donkey watered), not 14:5 (the son or ox in a well).')),
 dict(ref='14:25–35', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='Hating one\'s family and carrying the cross (14:25–27), the tower and the king at war (14:28–33), and salt (14:34–35): three NA27 paragraphs with no attested verse. Epiphanius refers to 14:26 in a refutation (Pan. 42.11.17, ἔλ. 70), but not as a reading of Marcion\'s text (Roth). Tertullian passes from 14:24 (4.31.8) to 15:4 (4.32.1).')),
]

PREAMBLE = (
 "Whom to invite. Jesus tells his host not to invite those who can repay, but the poor, the crippled, the lame and the blind, "
 "for he will be repaid at the resurrection. He tells the parable of a man who gave a great banquet: the invited guests "
 "excuse themselves with a field, five yoke of oxen and a marriage, and the master, angry, has his servant bring in the poor "
 "from the streets and then from the roads and hedges. Tertullian reads the parable as the Creator's long history of "
 "inviting Israel through the prophets and then calling the nations (Marc. 4.31). The healing on the sabbath and the "
 "places at table (14:1–11), and the sayings on the cost of discipleship (14:25–35), are not cited by any witness and are "
 "not printed."
)

NOTES = [
 dict(term='Not printed: 14:1–11', cat='excision', refs=['14:12'], text=(
  "The healing of a man with dropsy on the sabbath and the advice to take the lowest place at table are not cited by "
  "Tertullian or Epiphanius. They form two NA27 paragraphs with no attested verse, and their absence is undetermined. "
  "Tertullian had just argued the sabbath question at 13:15 (4.30.1), and a second sabbath healing would have added nothing "
  "new to his case.")),
 dict(term='The poor at the table (14:12–14)', cat='textual', refs=['14:12', '14:13', '14:14'], text=(
  "Tertullian, Marc. 4.31.1 sets the command to invite those who cannot repay beside Isaiah 58:7 (\"break your bread with the "
  "hungry, and bring the homeless poor into your house\"). He notes that Christ promises the repayment \"in the "
  "resurrection\". 14:13 is not cited and is printed in grey.")),
 dict(term='The great banquet (14:15–24)', cat='textual', refs=['14:15', '14:16', '14:18', '14:21', '14:23', '14:24'], text=(
  "Tertullian, Marc. 4.31.1–8 follows the parable step by step: a man made a dinner and invited many, sent to those invited, "
  "they excused themselves (\"I have bought a field, I have bought oxen, I have married a wife\"), the householder was moved "
  "and sent into the streets and lanes, then, with room to spare, into the roads and hedges. He remarks that Marcion denies "
  "that his God is ever moved to anger. He reads the excuses as Israel refusing the prophets (Jer 7:23–26) and the second "
  "gathering as the call of the nations (Deut 32:20–21). 14:15 is not cited; it is printed in grey because the parable answers "
  "it.")),
 dict(term='Not printed: 14:25–35', cat='excision', refs=['14:24'], text=(
  "Hating father and mother, carrying one's cross, counting the cost of a tower or a war, and the salt that loses its "
  "taste. No witness cites any of these verses as part of the text, and they are not printed. The previous version printed "
  "14:26 and 14:33.")),
 dict(term='Invitation and refusal', cat='theological', refs=['14:14', '14:21', '14:23'], text=(
  "Interpretation. In the attested text the host's duty is to invite those who cannot repay, and the parable ends with the "
  "poor, the crippled, the blind and the lame brought in, and then strangers from the roads. Tertullian reads this as the "
  "Creator's own pattern (Isaiah 58). The same preference for the poor over the rich appears in the Epistle of James "
  "(Jas 2:1–7, the rich man and the poor man in the assembly).")),
 dict(term='τῷ κεκληκότι αὐτόν, "the one who had invited him"', cat='translation', refs=['14:12'], text='καλέω, to call, invite. The same verb runs through the passage: "call" (14:12–13), "invited" (14:16–17, 14:24).'),
 dict(term='ἄριστον ἢ δεῖπνον, "a midday meal or a dinner"', cat='translation', refs=['14:12'], text='ἄριστον, as at 11:37; δεῖπνον, the main meal of the day, in the evening.'),
 dict(term='μὴ φώνει, "do not call"', cat='translation', refs=['14:12'], text='φωνέω, to call out, invite. It is a different verb from καλέω.'),
 dict(term='ἀνταπόδομα, "a repayment"', cat='translation', refs=['14:12'], text='What is given back in return.'),
 dict(term='δοχήν, "a reception"', cat='translation', refs=['14:13'], text='As at 5:29.'),
 dict(term='πτωχούς, "the destitute"', cat='translation', refs=['14:13'], text='As at 6:20.'),
 dict(term='ἀναπείρους, "the crippled"', cat='translation', refs=['14:13'], text='Maimed, disabled.'),
 dict(term='μακάριος ἔσῃ, "you will be fortunate"', cat='translation', refs=['14:14'], text='μακάριος, as at 6:20.'),
 dict(term='ἐν τῇ ἀναστάσει τῶν δικαίων, "at the rising of the just"', cat='translation', refs=['14:14'], text='ἀνάστασις, a standing up, rising. "Resurrection" is the Latin technical term (resurrectio) for the same word.'),
 dict(term='Μακάριος ὅστις φάγεται ἄρτον, "fortunate is whoever will eat bread"', cat='translation', refs=['14:15'], text='ἄρτος, bread, a loaf.'),
 dict(term='ἐκάλεσεν, "invited"', cat='translation', refs=['14:16'], text='καλέω, as in 14:12.'),
 dict(term='τὸν δοῦλον αὐτοῦ, "his slave"', cat='translation', refs=['14:17'], text='As at 7:2.'),
 dict(term='ἕτοιμά ἐστιν, "it is ready"', cat='translation', refs=['14:17'], text='Plural in the Greek: "things are ready".'),
 dict(term='ἀπὸ μιᾶς, "all alike"', cat='translation', refs=['14:18'], text='Literally "from one": with one accord, all at once.'),
 dict(term='παραιτεῖσθαι… ἔχε με παρῃτημένον, "excuse themselves… have me excused"', cat='translation', refs=['14:18'], text='παραιτέομαι, to beg off, decline.'),
 dict(term='ἔχω ἀνάγκην, "I have need"', cat='translation', refs=['14:18'], text='Literally "I have necessity": I must.'),
 dict(term='δοκιμάσαι, "to test"', cat='translation', refs=['14:19'], text='As at 12:56.'),
 dict(term='Γυναῖκα ἔγημα, "I have married a wife"', cat='translation', refs=['14:20'], text='γυνή is both "woman" and "wife".'),
 dict(term='τῷ κυρίῳ αὐτοῦ… ὁ οἰκοδεσπότης, "his lord… the master of the house"', cat='translation', refs=['14:21'], text='Two words for the same man: κύριος, lord, owner; οἰκοδεσπότης, master of the house (12:39).'),
 dict(term='ὀργισθείς, "angered"', cat='translation', refs=['14:21'], text='Made angry.'),
 dict(term='πλατείας καὶ ῥύμας, "streets and lanes"', cat='translation', refs=['14:21'], text='The broad streets and the narrow alleys.'),
 dict(term='Κύριε, "Lord"', cat='translation', refs=['14:22'], text="The slave's address to his owner."),
 dict(term='ἐπέταξας, "you ordered"', cat='translation', refs=['14:22'], text='ἐπιτάσσω, as at 4:36.'),
 dict(term='φραγμούς, "hedges"', cat='translation', refs=['14:23'], text='Fences, hedges along the fields.'),
 dict(term='ἀνάγκασον, "compel"', cat='translation', refs=['14:23'], text='To force, constrain. The Greek says "compel".'),
 dict(term='γεμισθῇ, "may be filled"', cat='translation', refs=['14:23'], text='Filled full.'),
 dict(term='τῶν ἀνδρῶν, "men"', cat='translation', refs=['14:24'], text='ἀνήρ, males.'),
 dict(term='γεύσεται, "will taste"', cat='translation', refs=['14:24'], text='γεύομαι, to taste, as at 9:27.'),
]
