"""Batch 2, chapter 5 of the reconstruction: Luke 8:1–25."""
from buildlib import greek
from batch1_ch2 import U, A
from batch2_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}

ENTRIES = [
 U('8:1', G('8:1'), 'Soon afterwards he went on through towns and villages, proclaiming and bringing the good news of the kingdom of God; and the twelve were with him,',
   'Opens the attested passage 8:1–3.'),
 A('8:2', G('8:2'), 'and also some women who had been cured of evil spirits and illnesses: Mary, called Magdalene, from whom seven daimons had gone out,',
   'present (Marc. 4.19.1)', [T('4.19.1', '"Quod divites Christo mulieres adhaerebant…"')],
   wording='NA27. Only the women are attested; the names in 8:2–3 are not cited, apart from the wife of Herod\'s steward.'),
 A('8:3', G('8:3'), 'and Joanna, the wife of Chuza, Herod\'s steward, and Susanna, and many others, who provided for them out of their own means.',
   'present (Marc. 4.19.1)', [T('4.19.1', '"mulieres… quae et de facultatibus suis ministrabant ei, inter quas et uxor regis procuratoris".')],
   wording='NA27 (αὐτοῖς). Tertullian has "ministrabant ei" (αὐτῷ, the reading of ℵ A L Ψ and others); Roth rates it possible. Noted, not adopted.'),
 A('8:4', G('8:4'), 'When a great crowd was gathering and people from town after town were coming to him, he spoke in a parable:',
   'present (Marc. 4.19.2)', [T('4.19.2', '"Aeque de parabolis…"')]),
 U('8:5', G('8:5'), '"A sower went out to sow his seed. As he sowed, some fell along the path and was trampled on, and the birds of the sky ate it up.',
   'Inside the attested pericope 8:4–8.'),
 U('8:6', G('8:6'), 'Some fell on the rock, and when it grew up it withered, because it had no moisture.', 'Inside the attested pericope 8:4–8.'),
 U('8:7', G('8:7'), 'Some fell among the thorns, and the thorns grew up with it and choked it.', 'Inside the attested pericope 8:4–8.'),
 A('8:8', G('8:8'), 'And some fell into the good soil, and when it grew it produced a hundredfold." As he said this he called out, "Whoever has ears to hear, let him hear."',
   'present (Marc. 4.19.2)', [T('4.19.2', '"dedit Christo frequenter inculcare, Qui habet aures audiat".')]),
 A('8:16', G('8:16'), 'No one lights a lamp and hides it under a jar or puts it under a bed; but he puts it on a lampstand, so that those who come in may see the light.',
   'present (Marc. 4.19.5)', [T('4.19.5', '"cum lucernam negat abscondi solere".')]),
 A('8:17', G('8:17'), 'For nothing is hidden that will not be made manifest, nor anything secret that will not be known and come to light.',
   'present (Marc. 4.19.5)', [T('4.19.5', '"qui de occulto in apertum repromittit".')]),
 A('8:18', G('8:18'), 'So take care how you hear; for to whoever has, more will be given, and from whoever does not have, even what he thinks he has will be taken away."',
   'present (Marc. 4.19.3–4)', [T('4.19.3–4', '"Videte quomodo audiatis… Ei qui habet dabitur, ab eo autem qui non habet etiam quod habere se putat auferetur ei."')]),
 A('8:20', G('8:20'), 'And it was reported to him, "Your mother and your brothers are standing outside, wanting to see you."',
   'present (Marc. 4.19.7; Pan. 42.11.6, sch. 12; Ephrem)',
   [E(12, 'οὐκ εἶχεν »ἡ μήτηρ αὐτοῦ καὶ οἱ ἀδελφοὶ αὐτοῦ«, ἀλλὰ μόνον »ἡ μήτηρ σου καὶ οἱ ἀδελφοί σου«.'),
    T('4.19.7', '"non potuisse illi annuntiari quod mater et fratres eius foris starent quaerentes videre eum".')]),
 A('8:21', greek('8:21', text='ὁ δὲ ἀποκριθεὶς εἶπεν πρὸς αὐτούς· Τίς μοι μήτηρ καὶ τίνες μοι ἀδελφοί, εἰ μὴ οἱ τοὺς λόγους μου ἀκούοντες καὶ ποιοῦντες αὐτούς;'),
   'But he answered them, "Who is my mother, and who are my brothers, except those who hear my words and do them?"',
   'present (Marc. 4.19.6, 10, 11)',
   [T('4.19.6', '"Quae mihi mater, et qui mihi fratres?"'),
    T('4.19.11', '"cum praemisisset, Quae mihi mater et qui mihi fratres? subiungens, Nisi qui audiunt verba mea et faciunt ea".')],
   wording='Marcionite form printed (retroversion; Roth\'s Greek): a question, and "my words" for "the word of God". Tertullian quotes it twice, and his Latin cannot render NA27\'s statement "My mother and my brothers are those who hear the word of God and do it". Roth rates the question and "my words" very likely and the participles secure; the dative μοι (for "mihi") and εἰ μή are probable or possible only. The NA27 opening (ὁ δὲ ἀποκριθεὶς εἶπεν πρὸς αὐτούς) is kept.'),
 A('8:22', G('8:22'), 'One day he got into a boat with his disciples, and he said to them, "Let us go across to the other side of the lake." So they set out,',
   'present (Marc. 4.20.2–3)', [T('4.20.3', '"Nam cum transfretat…"')]),
 A('8:23', G('8:23'), 'and as they sailed he fell asleep. A windstorm came down on the lake, and the boat was filling with water, and they were in danger.',
   'present (Marc. 4.20.3; Pan. 42.11.6, sch. 13)', [E(13, '»πλεόντων αὐτῶν ἀφύπνωσεν…«')]),
 A('8:24', G('8:24'), 'They came and woke him, saying, "Master, Master, we are perishing!" And he woke up and rebuked the wind and the raging of the water; they ceased, and there was a calm.',
   'present (Marc. 4.20.3; Pan. 42.11.6, sch. 13)',
   [E(13, '»ὁ δὲ ἐγερθεὶς ἐπετίμησε τῷ ἀνέμῳ καὶ τῇ θαλάσσῃ«.'),
    T('4.20.3', '"Cum ad minas eius eliditur mare… Comminans, inquit, mari".')],
   wording='NA27. Epiphanius has ἐγερθείς and "the sea" (τῇ θαλάσσῃ) for "the raging of the water"; Tertullian too speaks of the sea, but in the words of Nahum 1:4, which he is quoting. Roth rates both possible only. Noted, not adopted.'),
 A('8:25', G('8:25'), 'He said to them, "Where is your faith?" They were afraid and amazed, and said to one another, "Who then is this, that he commands even the winds and the water, and they obey him?"',
   'present (Marc. 4.20.1)', [T('4.20.1', '"Quis autem iste est qui et ventis et mari imperat?"')],
   wording='NA27. Tertullian has "the sea" (mari) for "the water"; Roth: possible. Noted, not adopted.'),
]

OMITTED = [
 dict(ref='8:9–10', cls='U−', app=dict(roth='unattested', witnesses=[
      T('4.19.2', '"illa quoque pronuntiatio eius ad populum, Aure audietis et non audietis, dedit Christo frequenter inculcare, Qui habet aures audiat" — he cites Isaiah 6:9 himself.')],
      decision='not printed',
      reason='In 8:10 Jesus applies Isaiah 6:9 to those outside. Tertullian\'s argument at this point is that the Creator\'s prophet foretold this way of speaking; he quotes Isaiah 6:9 himself and links it only to "whoever has ears, let him hear" (8:8). A saying in which Jesus quotes the Creator\'s prophet would have been his strongest evidence, and he does not cite it. NA27 begins a new paragraph at 8:9.')),
 dict(ref='8:11–15', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='The explanation of the sower forms its own NA27 paragraph (8:9–15) with no attested verse (METHOD §4.3).')),
 dict(ref='8:19', cls='A−', app=dict(roth='absent', witnesses=[
      E(12, 'οὐκ εἶχεν »ἡ μήτηρ αὐτοῦ καὶ οἱ ἀδελφοὶ αὐτοῦ«.')],
      decision='not printed', reason='Epiphanius states that the text did not have the narrative sentence "his mother and his brothers came", only the report to Jesus in 8:20. Tertullian passes over it (Roth: tacitus).')),
]

PREAMBLE = (
 "A short section on hearing. Women who had been healed travel with Jesus and the twelve and support them from their own "
 "means. The parable of the sower ends in a call to hear, and the sayings on the lamp and the measure of hearing follow. "
 "When his mother and brothers are reported to be outside, the text has Jesus ask, \"Who is my mother, and who are my "
 "brothers, except those who hear my words and do them?\" (Tertullian, Marc. 4.19.6, 11). The section closes with the calming "
 "of the storm. Two passages of canonical Luke are not printed. The first is the explanation of the sower with its quotation of "
 "Isaiah 6, which no witness cites. The second is the narrative sentence in which his mother and brothers arrive: Epiphanius "
 "says the text had only the report to Jesus."
)

NOTES = [
 dict(term='Women who provided for them (8:1–3)', cat='textual', refs=['8:2', '8:3'], text=(
  "Tertullian, Marc. 4.19.1: \"that rich women adhered to Christ and ministered to him from their means, among them the wife of "
  "the king's procurator\". 8:2–3 are attested in substance; the names (Mary Magdalene, Joanna, Chuza, Susanna) are not cited "
  "and are printed in the NA27 wording within the attested verses. 8:1 is not cited and is printed in grey. Tertullian reads "
  "\"ministered to him\" (αὐτῷ); NA27 has \"to them\" (αὐτοῖς).")),
 dict(term='The sower and the call to hear (8:4–8, 8:16–18)', cat='textual', refs=['8:4', '8:8', '8:16', '8:17', '8:18'], text=(
  "Tertullian, Marc. 4.19.2–5 attests the parable, the call \"whoever has ears, let him hear\", the lamp not hidden, the hidden "
  "made manifest and \"take care how you hear; to whoever has more will be given\". 8:5–7 are not cited and are printed in "
  "grey.")),
 dict(term='Not printed: 8:9–15', cat='excision', refs=['8:8', '8:16'], text=(
  "The disciples' question, Jesus' quotation of Isaiah 6:9 (\"so that seeing they may not see\") and the allegorical explanation "
  "of the sower are not cited by any witness. At 8:8 Tertullian brings in Isaiah 6:9 himself (\"Aure audietis et non audietis\", "
  "Marc. 4.19.2) to show that the Creator foretold this way of speaking. Had the text contained Jesus quoting the same prophet "
  "(8:10), it would have been his best evidence. 8:9–10 are classed \"unattested, probably absent\". 8:11–15 belong to the same "
  "NA27 paragraph, which has no attested verse, and are not printed.")),
 dict(term='"Who is my mother?" (8:19–21)', cat='textual', refs=['8:20', '8:21'], text=(
  "Epiphanius, sch. 12: the text \"did not have 'his mother and his brothers' [8:19], but only 'your mother and your brothers'\" "
  "[8:20]; so the arrival of the family is not narrated, only reported to Jesus. Tertullian, Marc. 4.19.6–13, quotes the reply "
  "twice as a question, \"Quae mihi mater et qui mihi fratres?\", and completes it: \"Nisi qui audiunt verba mea et faciunt ea\". "
  "That differs from canonical Luke in form (a question, as in Mark 3:33 and Matthew 12:48) and in content (\"my words\", not "
  "\"the word of God\"). The Greek printed is Roth's reconstruction from Tertullian's Latin (a retroversion). Tertullian records "
  "the Marcionite argument that the saying denies Jesus' birth; he answers that it transfers the names of kin to those who hear "
  "and do (4.19.11). The Marcionite argument is reception.")),
 dict(term='Hearing and doing', cat='theological', refs=['8:18', '8:21'], text=(
  "Interpretation. The attested form of 8:21 makes kinship with Jesus a matter of hearing his words and doing them, the same "
  "standard as 6:46 (\"why do you call me Lord, Lord, and do not do what I say?\"). The demand is the one the library finds in "
  "the Epistle of James (\"be doers of the word\", Jas 1:22). In this text it is attested twice, in two independent sayings.")),
 dict(term='The storm (8:22–25)', cat='textual', refs=['8:22', '8:23', '8:24', '8:25'], text=(
  "Tertullian, Marc. 4.20.1–3; Epiphanius, sch. 13: \"as they sailed he fell asleep; and he rose and rebuked the wind and the "
  "sea\". Both witnesses speak of \"the sea\" where NA27 has \"the raging of the water\" (8:24) and \"the water\" (8:25), as in "
  "Matthew and Mark. Tertullian's \"mare\" comes in words he is quoting from Nahum 1:4, and Epiphanius may be giving the familiar "
  "Matthean phrase; Roth rates the reading possible. NA27 is printed and the evidence noted. \"Master\" renders ἐπιστάτα.")),
]
