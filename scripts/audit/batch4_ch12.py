"""Batch 4, chapter 12 of the reconstruction: Luke 14:1–35 (14:12–24 printed)."""
from buildlib import greek, R
from batch1_ch2 import U, A
from batch4_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}

CR_14 = ('The man with dropsy healed on the sabbath (14:1–6) and the places at table (14:7–11): two NA27 paragraphs with no attested verse (METHOD §4.3). '
         'Tertullian passes from 13:28 (4.30.6) to 14:12 (4.31.1); his "rursus" at 4.30.1 introduces 13:15 (the ox or donkey watered), not 14:5 (the son or ox in a well).')
GR_14 = ('by its words, the printed text needs the passage. 14:12 "he said also to the one who had invited him (τῷ κεκληκότι αὐτόν)" takes up 14:10 '
         '"the one who invited you (ὁ κεκληκώς σε)"; the printed text has no host and no meal since 11:37. 14:15 "those reclining with him (συνανακειμένων)" '
         'takes up 14:10, and "eat bread" takes up 14:1. By its mechanics: 14:7–14 is one teaching about the meal; the printed text has the host\'s half '
         '(call those who cannot repay) without the guest\'s half (take the last place and be called up higher, to glory). '
         'Reading: docs/research/correspondence/word_by_word.md, chapter 11, test of 14:1–11.')
W14 = lambda ref, en: R(ref, G(ref), en, 'U?', 'unattested', CR_14, GR_14, wording='NA27 (checked on the page image, p. 208).')

ENTRIES = [
 W14('14:1', 'One sabbath, when he went into the house of one of the rulers of the Pharisees to eat bread, they were watching him closely.'),
 W14('14:2', 'And there in front of him was a man who had dropsy.'),
 W14('14:3', 'And Jesus answered and said to the lawyers and Pharisees, "Is it lawful to heal on the sabbath, or not?"'),
 W14('14:4', 'But they were silent. And taking hold of him, he healed him and let him go.'),
 W14('14:5', 'And he said to them, "Which of you, if a son or an ox falls into a well, will not at once draw him up on the sabbath day?"'),
 W14('14:6', 'And they could not reply to this.'),
 W14('14:7', 'He told a parable to those who were invited, noticing how they chose the first places, saying to them,'),
 W14('14:8', '"When you are invited by someone to a wedding feast, do not recline in the first place, in case someone more honoured than you has been invited by him,'),
 W14('14:9', 'and the one who invited you both comes and says to you, \'Give this man your place,\' and then with shame you begin to take the last place.'),
 W14('14:10', 'But when you are invited, go and recline in the last place, so that when the one who invited you comes, he will say to you, \'Friend, go up higher.\' Then you will have glory before all who are at table with you.'),
 W14('14:11', 'For everyone who exalts himself will be humbled, and the one who humbles himself will be exalted."'),
 A('14:12', G('14:12'), 'He said also to the man who had invited him, "When you give a dinner or a banquet, do not invite your friends or your brothers or your relatives or rich neighbours, in case they invite you in return and you are repaid.',
   'present (Marc. 4.31.1)', [T('4.31.1', '"Ad prandium vel ad coenam quales vocari iubet? Quales ostenderat per Esaiam…"')]),
 U('14:13', G('14:13'), 'But when you give a feast, invite the poor, the crippled, the lame, the blind;', 'Inside the attested paragraph 14:12–14.'),
 A('14:14', G('14:14'), 'and you will be blessed, because they cannot repay you; for you will be repaid at the resurrection of the righteous."',
   'present (Marc. 4.31.1)', [T('4.31.1', '"qui scilicet humanitatis istius vicem retribuere non possint. Hanc si Christus captari vetat, in resurrectione eam repromittens…"')],
   wording='NA27. Tertullian has "in the resurrection" without "of the righteous"; the words are not quoted, and no omission is attested (Roth). Printed.'),
 U('14:15', G('14:15'), 'When one of those at table with him heard this, he said to him, "Blessed is anyone who will eat bread in the kingdom of God!"',
   'A one-verse NA27 paragraph, but part of the attested pericope: the parable 14:16–24 is the answer to it ("But he said to him").'),
 A('14:16', G('14:16'), 'But he said to him, "A man once gave a great banquet and invited many.',
   'present (Marc. 4.31.1–2)', [T('4.31.1', '"Etiam invitatoris parabola cui magis parti occurrat expende. Homo quidam fecit coenam et vocavit multos."')],
   wording='NA27. Tertullian does not have "great"; Roth: "μέγα may have been present". Printed.'),
 A('14:17', G('14:17'), 'At the hour of the banquet he sent his servant to say to those who had been invited, \'Come, for everything is now ready.\'',
   'present (Marc. 4.31.3)', [T('4.31.3', '"Dehinc si is mittit ad convivas qui coenam paravit…"')]),
 A('14:18', G('14:18'), 'But they all alike began to make excuses. The first said to him, \'I have bought a field, and I must go out and see it; please have me excused.\'',
   'present (Marc. 4.31.3–4)', [T('4.31.3', '"Excusant se invitati."'), T('4.31.4', '"Agrum emi, et boves mercatus sum, et uxorem duxi."')]),
 A('14:19', G('14:19'), 'Another said, \'I have bought five yoke of oxen, and I am going to try them out; please have me excused.\'',
   'present (Marc. 4.31.4)', [T('4.31.4', '"et boves mercatus sum".')]),
 A('14:20', G('14:20'), 'Another said, \'I have married a wife, and therefore I cannot come.\'',
   'present (Marc. 4.31.4)', [T('4.31.4', '"et uxorem duxi".')]),
 A('14:21', G('14:21'), 'So the servant came and reported this to his master. Then the master of the house, in anger, said to his servant, \'Go out quickly into the streets and lanes of the town, and bring in here the poor and the crippled and the blind and the lame.\'',
   'present (Marc. 4.31.5–6)', [T('4.31.5', '"Hoc ut patrifamiliae renuntiatum est, motus tunc (bene quod et motus, negat enim Marcion moveri deum suum…) mandat de plateis et vicis civitatis facere sublectionem."')],
   wording='NA27. Tertullian\'s "motus" ("moved") is rated possible only as a rendering of a different verb (Roth: ἐπαρθείς?); NA27 ὀργισθείς is printed.'),
 A('14:22', G('14:22'), 'And the servant said, \'Master, what you commanded has been done, and there is still room.\'',
   'present (Marc. 4.31.6)', [T('4.31.6', '"Dehinc loco abundante…"')]),
 A('14:23', G('14:23'), 'Then the master said to the servant, \'Go out into the roads and hedgerows, and compel people to come in, so that my house may be filled.',
   'present (Marc. 4.31.6)', [T('4.31.6', '"praecepit etiam de viis et sepibus colligi, id est nos iam de extraneis gentibus".')]),
 A('14:24', G('14:24'), 'For I tell you, none of those men who were invited will taste my banquet.\'"',
   'present (Marc. 4.31.6)', [T('4.31.6', '"de qua illos gustaturos negat dominus".')]),
]

OMITTED = [
 dict(ref='14:25–35', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='Hating one\'s family and carrying the cross (14:25–27), the tower and the king at war (14:28–33), and salt (14:34–35): three NA27 paragraphs with no attested verse. Epiphanius refers to 14:26 in a refutation (Pan. 42.11.17, ἔλ. 70), but not as a reading of Marcion\'s text (Roth). Tertullian passes from 14:24 (4.31.8) to 15:4 (4.32.1).')),
]

PREAMBLE = (
 "Whom to invite. Jesus tells his host not to invite those who can repay, but the poor, the crippled, the lame and the blind, "
 "for he will be repaid at the resurrection. He tells the parable of a man who gave a great banquet: the invited guests "
 "excuse themselves with a field, five yoke of oxen and a marriage, and the master, angry, has his servant bring in the poor "
 "from the streets and then from the roads and hedges. Tertullian reads the parable as the Creator's long history of "
 "inviting Israel through the prophets and then calling the nations (Marc. 4.31). The sayings on the cost of discipleship "
 "(14:25–35) are not cited by any witness and are not printed. The chapter opens with the healing on the sabbath and the "
 "places at table (14:1–11), which no witness cites either; they are printed as restored by method, because the printed text "
 "needs them (METHOD §11; see the notes)."
)

NOTES = [
 dict(term='Restored by method: 14:1–11', cat='textual', refs=['14:1', '14:10', '14:11', '14:12', '14:15'], text=(
  "The healing of a man with dropsy on the sabbath (14:1–6) and the advice to take the last place at table (14:7–11) are not "
  "cited by Tertullian or Epiphanius. They form two NA27 paragraphs with no attested verse, and their absence is undetermined "
  "(U?). Tertullian had just argued the sabbath question at 13:15 (4.30.1), and a second sabbath healing would have added nothing "
  "new to his case. The passage is printed as restored by method (METHOD §11). By its words, the printed text needs it: 14:12, "
  "\"he said also to the one who had invited him (τῷ κεκληκότι αὐτόν)\", takes up 14:10, \"the one who invited you (ὁ κεκληκώς σε)\", "
  "and without 14:1–11 the printed text has no host and no meal since 11:37; 14:15, \"those at table with him (συνανακειμένων)\", "
  "takes up 14:10, and its \"eat bread\" takes up 14:1. By its mechanics: 14:7–14 is one teaching about the meal in two halves, "
  "the guest's (take the last place, and be called up higher, to glory) and the host's (invite those who cannot repay). Without "
  "14:1–11 the printed text has the second without the first. 14:11 is the same saying as the attested 18:14. The reading is in "
  "docs/research/correspondence/word_by_word.md (chapter 11, test of 14:1–11). The Greek is NA27, checked on the page image (p. 208).")),
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
]
