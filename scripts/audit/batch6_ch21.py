"""Batch 6, chapter 21 of the reconstruction: Luke 23:1–56 (23:13–16 and 23:39–43 restored by method, METHOD §11)."""
from buildlib import R
from batch1_ch2 import U, A
from batch6_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}

T421 = T('4.42.1', '"Perductum enim illum ad Pilatum onerare coeperunt quod se regem diceret Christum… Pilato quoque interroganti, Tu es Christus? proinde, Tu dicis…"')
T423 = T('4.42.3', '"Nam et Herodi velut munus a Pilato missus… Delectatus est denique Herodes viso Iesu, nec vocem ullam ab eo audivit."')
T424 = T('4.42.4', '"Et Barrabas quidem nocentissimus vita ut bonus donatur, Christus vero iustissimus ut homicida morti expostulatur. Sed et duo scelesti circumfiguntur illi, ut inter iniquos scilicet deputaretur."')
T427 = T('4.42.7', '"nihil de Pilato postulatum, nihil de patibulo detractum, nihil sindone involutum, nihil sepulcro novo conditum."')

CR_23_13 = 'Pilate tells the chief priests and rulers that neither he nor Herod found him guilty: a paragraph with no attested verse (METHOD §4.3).'
GR_23_13 = ('by its words, three printed verses point to it: 23:18 "release (ἀπόλυσον) to us Barabbas" answers an offer of release that only 23:16 makes; 23:20 "again (πάλιν), wishing to release Jesus" has no earlier wish without it; '
            'the attested 23:22 "a third time" repeats 23:14–16 almost word for word ("I found nothing deserving death in him; having disciplined him, I will release him"), and the second finding, between 23:4 and 23:22, is 23:14–15. '
            'By its mechanics: release offered three times answers the denial spoken three times (22:34; 22:57–60). Reading: docs/research/correspondence/word_by_word.md, chapter 21, test of 23:13–16; second_pass.md §2.')
CR_23_39 = 'The two criminals; "Jesus, remember me when you come into your kingdom". A paragraph with no attested verse; its answer (23:43) is attested absent.'
CR_23_43 = 'Epiphanius states that the text lacked "Today you will be with me in paradise" (sch. 72). Tertullian passes from 23:34 to 23:44 (4.42.4–5).'
GR_23_39 = ('by its mechanics, the printed text states the law of the two, "one taken along, the other left" (17:34–35), and brings two evil-doers to the cross, "one on the right and one on the left" (23:32–33), without bringing them back. '
            'Here one demands that he save himself, and the other fears God, accepts his measure, asks to be remembered, and is taken "today, with me". It completes three strands of the final text: faith\'s "with you… to death" (22:33) denied (22:54–62) and here kept by the evil-doer; '
            'remembering (22:61 → 23:42 → 24:6–8); and "today" (4:21; 19:9). Reading: docs/research/correspondence/word_by_word.md, chapter 21, test of 23:39–43; second_pass.md §2.')
W13 = lambda ref, en: R(ref, G(ref), en, 'U?', 'unattested', CR_23_13, GR_23_13, wording='NA27 (checked on the page image, p. 238).')
W39 = lambda ref, en, note='': R(ref, G(ref), en, 'U?', 'unattested', CR_23_39, GR_23_39, wording='NA27 (checked on the page image, p. 240).' + note)

ENTRIES = [
 A('23:1', G('23:1'), 'Then the whole company of them arose and brought him before Pilate.',
   'present (Marc. 4.42.1)', [T421]),
 A('23:2', G('23:2', [('διαστρέφοντα τὸ ἔθνος ἡμῶν καὶ κωλύοντα φόρους Καίσαρι διδόναι καὶ λέγοντα',
                      'διαστρέφοντα τὸ ἔθνος ἡμῶν καὶ καταλύοντα τὸν νόμον καὶ τοὺς προφήτας καὶ κωλύοντα φόρους Καίσαρι διδόναι καὶ ἀποστρέφοντα τὰς γυναῖκας καὶ τὰ τέκνα καὶ λέγοντα')]),
   'And they began to accuse him, saying, "We found this man misleading our nation and destroying the law and the prophets, forbidding us to give tribute to Caesar and turning away the women and the children, and saying that he himself is the Anointed One, a king."',
   'present (Marc. 4.42.1; Pan. 42.11.6, sch. 69–70)',
   [T421,
    E(69, 'προσέθετο μετὰ τὸ »τοῦτον εὕρομεν διαστρέφοντα τὸ ἔθνος« »καὶ καταλύοντα τὸν νόμον καὶ τοὺς προφήτας«. Elenchus 69: "the text did not read so, but: we found this man misleading the people, saying that he is Christ a king".'),
    E(70, 'προσθήκη μετὰ τὸ »κελεύοντα φόρους μὴ δοῦναι« »καὶ ἀποστρέφοντα τὰς γυναῖκας καὶ τὰ τέκνα«.')],
   wording=('Marcionite readings adopted: "and destroying the law and the prophets" after "misleading our nation", and "and turning away the women and the children" after the tribute. Epiphanius states twice, in two scholia, that the text had these words in addition to canonical Luke\'s; NA27 cites both for Marcion (McionE); Roth: very likely. '
            'The rest of the verse is NA27. Epiphanius\' own wording of it is a summary (Roth); NA27 cites McionE also for the omission of "our", which Roth leaves open, and it is printed.'),
   western='"And destroying the law and the prophets" also stands in Old Latin manuscripts (e b c ff2 gat i) and a few Vulgate manuscripts; c and e have "and he turned away our sons and wives from us" at 23:5.'),
 A('23:3', G('23:3'), 'And Pilate asked him, "Are you the King of the Jews?" And he answered him, "You say so."',
   'present (Marc. 4.42.1)', [T421],
   wording='NA27. Tertullian has Pilate ask "Are you the Christ?"; Roth: possible only, since Tertullian has just spoken of the charge "Christ a king" and goes on to Ps 2 ("against his Christ"). Not adopted.'),
 U('23:4', G('23:4'), 'Then Pilate said to the chief priests and the crowds, "I find no guilt in this man."', 'Inside the attested paragraph 23:2–5.'),
 U('23:5', G('23:5'), 'But they were urgent, saying, "He stirs up the people, teaching throughout all Judea, from Galilee where he began even to this place."', 'Inside the attested paragraph 23:2–5.'),
 U('23:6', G('23:6'), 'When Pilate heard this, he asked whether the man was a Galilean.', 'Inside the attested paragraph 23:6–7.'),
 A('23:7', G('23:7'), 'And when he learned that he belonged to Herod\'s jurisdiction, he sent him over to Herod, who was himself in Jerusalem at that time.',
   'present (Marc. 4.42.3)', [T423]),
 A('23:8', G('23:8'), 'When Herod saw Jesus, he was very glad, for he had long desired to see him, because he had heard about him, and he was hoping to see some sign done by him.',
   'present (Marc. 4.42.3)', [T423]),
 A('23:9', G('23:9'), 'So he questioned him at some length, but he made no answer.',
   'present (Marc. 4.42.3)', [T423], wording='NA27. Tertullian ("he heard no word from him") attests the silence, not the wording.'),
 U('23:10', G('23:10'), 'The chief priests and the scribes stood by, vehemently accusing him.', 'Inside the attested paragraph 23:8–12.'),
 U('23:11', G('23:11'), 'And Herod with his soldiers treated him with contempt and mocked him. Then, arraying him in splendid clothing, he sent him back to Pilate.', 'Inside the attested paragraph 23:8–12. NA27 [καί].'),
 U('23:12', G('23:12'), 'And Herod and Pilate became friends with each other that very day, for before this they had been at enmity with each other.', 'Inside the attested paragraph 23:8–12.'),
 W13('23:13', 'Pilate then called together the chief priests and the rulers and the people,'),
 W13('23:14', 'and said to them, "You brought me this man as one who was turning the people away; and look, having examined him before you, I have found in this man no guilt in the things you accuse him of.'),
 W13('23:15', 'Neither has Herod, for he sent him back to us; and look, nothing deserving death has been done by him.'),
 W13('23:16', 'I will therefore punish and release him."'),
 A('23:18', G('23:18'), 'But they all cried out together, "Away with this man, and release to us Barabbas"—',
   'present (Marc. 4.42.4)', [T424]),
 A('23:19', G('23:19'), 'a man who had been thrown into prison for an insurrection started in the city and for murder.',
   'present (Marc. 4.42.4)', [T424], wording='NA27. Tertullian\'s "most guilty in life" and "as a murderer" refer to the crimes (Roth: possible).'),
 U('23:20', G('23:20'), 'Pilate addressed them once more, desiring to release Jesus,', 'Inside the attested paragraph 23:18–23. NA27 αὐτοῖς (SBLGNT without it).'),
 U('23:21', G('23:21'), 'but they kept shouting, "Crucify, crucify him!"', 'Inside the attested paragraph 23:18–23.'),
 A('23:22', G('23:22'), 'A third time he said to them, "Why? What evil has he done? I have found in him no guilt deserving death. I will therefore punish and release him."',
   'present (Marc. 4.42.4)', [T424], wording='NA27. Tertullian\'s "most just" refers to Pilate\'s finding (Roth); no insight into the wording.'),
 A('23:23', G('23:23'), 'But they were urgent, demanding with loud cries that he should be crucified. And their voices prevailed.',
   'present (Marc. 4.42.4)', [T424], wording='NA27. Tertullian\'s "his death is demanded" refers to the cries (Roth); no insight into the wording.'),
 U('23:24', G('23:24'), 'So Pilate decided that their demand should be granted.', 'Inside the attested paragraph 23:24–25.'),
 A('23:25', G('23:25'), 'He released the man who had been thrown into prison for insurrection and murder, for whom they asked, but he delivered Jesus over to their will.',
   'present (Marc. 4.42.4)', [T424], wording='NA27. Tertullian attests the release ("donatur"; Roth: ἀπέλυσεν).'),
 A('23:32', G('23:32'), 'Two others, who were criminals, were led away to be put to death with him.',
   'present (Marc. 4.42.4)', [T424]),
 A('23:33', G('23:33'), 'And when they came to the place that is called The Skull, there they crucified him, and the criminals, one on his right and one on his left.',
   'present (Marc. 4.42.4; Pan. 42.11.6, sch. 71)',
   [T424, E(71, '»καὶ ἐλθόντες εἰς τόπον λεγόμενον Κρανίου τόπος ἐσταύρωσαν αὐτὸν καὶ διεμερίσαντο τὰ ἱμάτια αὐτοῦ καὶ ἐσκοτίσθη ὁ ἥλιος«.')],
   wording='NA27. Epiphanius\' wording follows Matt 27:33 and runs 23:33, 34b and 45 together; Roth: a summary, possible only.'),
 W39('23:39', 'One of the criminals who were hanged there blasphemed him, saying, "Are you not the Anointed One? Save yourself and us!"'),
 W39('23:40', 'But the other answered and rebuked him, saying, "Do you not fear God, since you are under the same sentence?'),
 W39('23:41', 'And we indeed justly, for we are receiving back what our deeds deserve; but this man has done nothing wrong."'),
 W39('23:42', 'And he said, "Jesus, remember me when you come into your kingdom."', note=' εἰς τὴν βασιλείαν (SBLGNT ἐν τῇ βασιλείᾳ).'),
 R('23:43', G('23:43'), 'And he said to him, "Truly I tell you, today you will be with me in paradise."', 'A−', 'absent', CR_23_43,
   GR_23_39 + ' Printed against Marcion\'s text: the witness states that the verse was not in it.',
   witnesses=[E(72, 'παρέκοψε τὸ »σήμερον μετ\' ἐμοῦ ἔσῃ ἐν τῷ παραδείσῳ«.')], wording='NA27 (checked on the page image, p. 240).'),
 A('23:44', G('23:44'), 'It was now about the sixth hour, and there was darkness over the whole land until the ninth hour,',
   'present (Marc. 4.42.5)',
   [T('4.42.5', '"Ecce autem et elementa concutiuntur… Hic erit dies de quo et Amos: Et erit illa die, dicit dominus, occidet sol meridie (habes et horae sextae significationem), et contenebrabit super terram."')],
   wording='NA27. Tertullian\'s gloss on Amos 8:9 attests the sixth hour and the darkness over the land (Roth: very likely).'),
 A('23:45', G('23:45'), 'while the sun\'s light failed. And the curtain of the temple was torn in two.',
   'present (Marc. 4.42.5; Pan. 42.11.6, sch. 71)',
   [T('4.42.5', '"Scissum est et templi velum…"'), E(71, '»… καὶ ἐσκοτίσθη ὁ ἥλιος«.')],
   wording=('NA27. For "the sun\'s light failed" (τοῦ ἡλίου ἐκλιπόντος) Epiphanius has "and the sun was darkened" (καὶ ἐσκοτίσθη ὁ ἥλιος), the reading of A C3 W Θ Ψ f1.13 𝔐 lat sy; NA27 cites McionEvid. '
            'Roth: probable only, because the scholion is a summary in Matthew\'s wording; Ephrem and Eznik, who speak of the sun darkened in Marcionite contexts, were not checked here. Not adopted. Tertullian attests the curtain (Roth: secure).')),
 A('23:46', G('23:46'), 'Then Jesus, calling out with a loud voice, said, "Father, into your hands I commit my spirit!" And having said this he breathed his last.',
   'present (Marc. 4.42.6; Pan. 42.11.6, sch. 73)',
   [T('4.42.6', '"Vociferatur ad patrem, ut et moriens ultima voce prophetas adimpleret. Hoc dicto expiravit."'),
    E(73, '»καὶ φωνήσας φωνῇ μεγάλῃ ἐξέπνευσεν«.')],
   wording=('NA27. Both witnesses attest the loud cry and "he breathed his last"; Tertullian\'s "having said this" renders τοῦτο δὲ εἰπών. Neither quotes the words of the cry. Tertullian\'s "to the Father… to fulfil the prophets" (Ps 31:5) points to them (Roth: possible). '
            'Adamantius quotes the verse (198,8–12), but as the orthodox speaker; it is not counted.')),
 A('23:50', G('23:50'), 'Now there was a man named Joseph, a member of the council, a good and righteous man,',
   'present (Marc. 4.42.8; Pan. 42.11.6, sch. 74)',
   [T('4.42.8', '"Sed si et Ioseph corpus fuisse noverat quod tota pietate tractavit, ille Ioseph qui non consenserat in scelere Iudaeis…"'),
    E(74, '»καὶ ἰδοὺ ἀνὴρ ὀνόματι Ἰωσήφ, καθελὼν τὸ σῶμα ἐνετύλιξε σινδόνι καὶ ἔθηκεν ἐν μνήματι λαξευτῷ«.')],
   wording='NA27 (with NA27\'s bracketed καί). Epiphanius quotes "and behold, a man named Joseph"; the rest is unattested.'),
 A('23:51', G('23:51'), 'who had not consented to their decision and action; he was from Arimathea, a Jewish town, and he was looking for the kingdom of God.',
   'present (Marc. 4.42.8)', [T('4.42.8', '"ille Ioseph qui non consenserat in scelere Iudaeis".')]),
 A('23:52', G('23:52'), 'This man went to Pilate and asked for the body of Jesus.',
   'present (Marc. 4.42.7)', [T427]),
 A('23:53', G('23:53'), 'Then he took it down and wrapped it in a linen shroud and laid him in a tomb cut in stone, where no one had ever yet been laid.',
   'present (Marc. 4.42.7; Pan. 42.11.6, sch. 74)', [T427, E(74, '»… καθελὼν τὸ σῶμα ἐνετύλιξε σινδόνι καὶ ἔθηκεν ἐν μνήματι λαξευτῷ«.')],
   wording='NA27. Both witnesses attest the taking down, the linen and the tomb; Tertullian\'s "new" may come from "where no one had been laid" or from Matt 27:60 (Roth).'),
 U('23:54', G('23:54'), 'It was the day of Preparation, and the Sabbath was beginning.', 'Inside the attested paragraph 23:50–54.'),
 A('23:55', G('23:55'), 'The women who had come with him from Galilee followed and saw the tomb and how his body was laid.',
   'present (Marc. 4.43.1)', [T('4.43.1', '"si nec mulierum illarum officium praeterit prophetia quae ante lucem convenerunt ad sepulcrum cum odorum paratura".')],
   wording='NA27. Tertullian attests the women (Roth: very likely).'),
 A('23:56', G('23:56'), 'Then they returned and prepared spices and ointments. On the Sabbath they rested according to the commandment.',
   'present (Pan. 42.11.6, sch. 75; Marc. 4.43.1)',
   [E(75, '»καὶ ὑποστρέψασαι αἱ γυναῖκες ἡσύχασαν τὸ σάββατον κατὰ τὸν νόμον«.')],
   wording='NA27. Epiphanius has "according to the law" for "according to the commandment"; Roth: "the law" possible only. Not adopted. Tertullian\'s "with the preparation of spices" (4.43.1) refers to 23:56a or 24:1.'),
]

OMITTED = [
 dict(ref='23:26', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='Simon of Cyrene: a one-verse NA27 paragraph with no attested verse.')),
 dict(ref='23:27–31', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='"Daughters of Jerusalem, do not weep for me…": a paragraph with no attested verse.')),
 dict(ref='23:34', cls='A−', app=dict(roth='34a unattested (Ephrem possibly); 34b absent (Marc. 4.42.4)', witnesses=[
      T('4.42.4', '"Vestitum plane eius a militibus divisum, partim sorte concessum, Marcion abstulit, respiciens psalmi prophetiam: Dispertiti sibi sunt vestimenta mea…"'),
      E(71, '»… ἐσταύρωσαν αὐτὸν καὶ διεμερίσαντο τὰ ἱμάτια αὐτοῦ καὶ ἐσκοτίσθη ὁ ἥλιος«.')],
      decision='not printed',
      reason=('23:34b, the dividing of the garments by lot: Tertullian states that Marcion removed it, because of Ps 22:18, and builds his argument on its absence. Epiphanius\' scholion 71 mentions the dividing, but it runs 23:33, 34b and 45 together in Matthew\'s wording and is a summary (Volckmar, Zahn, Roth). Tertullian\'s explicit statement is followed. '
              '23:34a, "Father, forgive them, for they know not what they do", is printed by NA27 in double brackets as not part of its text (absent from 𝔓75 ℵ1 B D* W Θ 070 579 1241 a sys sa). Neither Tertullian nor Epiphanius cites it; Ephrem mentions the saying in an argument against the Marcionites (Comm. Diat. 21.3), which Roth rates as a possible attestation only. It is not printed.'))),
 dict(ref='23:35–38', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='The rulers and soldiers mock him; the inscription. A paragraph with no attested verse. Ps 22:7, 16 in Tertullian 4.42.4 is not clearly a reference to it (Roth).')),
 dict(ref='23:47–48', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='The centurion ("certainly this man was righteous") and the crowds beating their breasts: a paragraph with no attested verse.')),
 dict(ref='23:49', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='His acquaintances and the women standing at a distance: a one-verse paragraph with no attested verse.')),
]

PREAMBLE = (
 "Pilate, Herod and the cross. The council brings Jesus to Pilate. In this text the accusers say: \"We found this man misleading "
 "our nation and destroying the law and the prophets, forbidding us to give tribute to Caesar and turning away the women and the "
 "children\" (Epiphanius, sch. 69–70). Pilate sends him to Herod, who is glad to see him and hears no word from him. The crowd asks "
 "for Barabbas and demands that Jesus be crucified, though Pilate three times finds no guilt in him and offers to release him "
 "(23:13–16 printed as restored by method). He is crucified at the Skull between two criminals. One of them asks, \"Jesus, "
 "remember me when you come into your kingdom\", and is told, \"Today you will be with me in paradise\" (23:39–43, printed "
 "as restored by method, 23:43 against Marcion's text). There is darkness at the "
 "sixth hour and the curtain of the temple is torn. Jesus cries out with a loud voice to the Father and breathes his last. Joseph, "
 "who had not consented to the council's act, takes down the body, wraps it in linen and lays it in a rock-cut tomb. The women see "
 "the tomb and rest on the Sabbath. By the witnesses' statements Marcion's text lacked the dividing of the garments (Tertullian) "
 "and \"Today you will be with me in paradise\" (Epiphanius); the second is printed by method (see the notes)."
)

NOTES = [
 dict(term='The charges before Pilate (23:1–5)', cat='textual', refs=['23:1', '23:2', '23:3'], text=(
  "Tertullian (4.42.1) has the council accuse Jesus of calling himself \"Christ, a king\", and Pilate ask \"Are you the Christ?\". "
  "Epiphanius reports two additions in the charges of 23:2: \"and destroying the law and the prophets\" (sch. 69) and \"and turning "
  "away the women and the children\" (sch. 70). He answers the first from Matt 5:17 (\"I came not to destroy the law and the "
  "prophets\"), and says that the canonical text reads only \"misleading the people\". Old Latin manuscripts have the first "
  "addition at the same place, and c and e have the second at 23:5, so both readings were known outside Marcion's text. They "
  "are printed. 23:4–5 are not cited and are printed in grey.")),
 dict(term='Herod and the sentence (23:6–25)', cat='textual', refs=['23:7', '23:8', '23:9', '23:18', '23:19', '23:22', '23:23', '23:25'], text=(
  "Tertullian (4.42.2–4) reads the trial through Ps 2 and Isaiah: Herod receives Jesus \"as a gift\" from Pilate (Hos 10:6), is "
  "glad to see him and hears no word from him, as the lamb is silent before the shearer (Isa 53:7). Barabbas, \"most guilty in "
  "life\", is released as if good, and Christ, \"most just\", is demanded for death as a murderer. NA27 has no 23:17.")),
 dict(term='Restored by method: Pilate\'s second finding (23:13–16)', cat='textual', refs=['23:4', '23:14', '23:15', '23:16', '23:18', '23:20', '23:22'], text=(
  "23:13–16 form a paragraph that no witness cites (U?). It is printed as restored by method (METHOD §11). By its words, three "
  "printed verses point to it: 23:18, \"release (ἀπόλυσον) to us Barabbas\", answers an offer of release that only 23:16 makes; "
  "23:20, \"again (πάλιν), wishing to release Jesus\", has no earlier wish without it; and the attested 23:22, \"a third time\", "
  "repeats 23:14–16 almost word for word (\"I found nothing deserving death in him; I will therefore punish and release him\"). "
  "The first finding is 23:4 and the third 23:22; the second is 23:14–15. By its mechanics: release offered three times answers "
  "the denial spoken three times (22:34; 22:57–60). Reading: docs/research/correspondence/second_pass.md §2. The Greek is NA27, "
  "checked on the page image (p. 238).")),
 dict(term='The crucifixion (23:26–46)', cat='textual', refs=['23:32', '23:33', '23:44', '23:45', '23:46'], text=(
  "Tertullian (4.42.4) attests the two criminals crucified with Jesus \"so that he was counted among the lawless\", and states "
  "that Marcion removed the dividing of his garments because of Ps 22:18; he answers that the whole psalm is Christ's garment. "
  "Epiphanius' scholion 71 mentions the dividing, but in a summary of the scene in Matthew's wording; Tertullian's statement is "
  "followed. Epiphanius states that \"Today you will be with me in paradise\" (23:43) was not in the text (sch. 72); it is "
  "printed by method (see the next note). Tertullian "
  "(4.42.5) attests the darkness at the sixth hour and the torn curtain, and (4.42.6) the loud cry to the Father and \"having said "
  "this, he breathed his last\", from which he argues that what breathes out a spirit is flesh. \"Father, forgive them\" (23:34a) "
  "is not in the NA27 text and is not cited by either witness. Simon of Cyrene, the daughters of Jerusalem, the mockery at the "
  "cross, the centurion and the onlookers (23:26–31, 35–38, 47–49) are in paragraphs that no witness cites; the correspondential "
  "reading tested them at their places, and the printed text does not need them.")),
 dict(term='Restored by method: the two beside him (23:39–43)', cat='textual', refs=['23:32', '23:33', '23:39', '23:42', '23:43'], text=(
  "No witness cites 23:39–42 (U?), and Epiphanius states that Marcion's text lacked 23:43, \"Today you will be with me in "
  "paradise\" (sch. 72). The passage is printed as restored by method (METHOD §11), and 23:43 against Marcion's text. By its "
  "mechanics: the printed text states the law of the two, \"one taken along, the other left\" (17:34–35), and brings two "
  "evil-doers to the cross, \"one on the right and one on the left\" (23:32–33; Tertullian 4.42.4: \"duo scelesti circumfiguntur "
  "illi\"), without bringing them back. Here one demands that he save himself, and the other fears God, accepts his measure, "
  "asks to be remembered, and is taken \"today, with me\". It completes three strands: Peter's \"with you… to death\" (22:33), "
  "denied in 22:54–62 and here kept by an evil-doer; remembering (22:61; 23:42; 24:6–8); and \"today\" (4:21; 19:9). Reading: "
  "docs/research/correspondence/word_by_word.md (chapter 21); second_pass.md §2. The Greek is NA27, checked on the page image "
  "(p. 240); at 23:42 NA27 reads εἰς τὴν βασιλείαν. The previous edition printed 23:43 without grounds and the audit removed it "
  "(batch 6); it is now printed on the grounds stated here.")),
 dict(term='The burial (23:50–56)', cat='textual', refs=['23:50', '23:51', '23:52', '23:53', '23:55', '23:56'], text=(
  "Tertullian (4.42.7–8) argues from the burial: if the body were a phantom, nothing would have been asked of Pilate, taken down "
  "from the cross, wrapped in linen or laid in a new tomb; Joseph, \"who had not consented to the crime\", knew it was a body. "
  "Epiphanius quotes Joseph taking down the body, wrapping it in linen and laying it in a rock-cut tomb (sch. 74), and the women "
  "returning and resting on the Sabbath \"according to the law\" (sch. 75). Tertullian (4.43.1) attests the women who came to the "
  "tomb with spices.")),
 dict(term='"Destroying the law and the prophets"', cat='theological', refs=['23:2'], text=(
  "Interpretation. In this text the charge that Jesus destroys the law and the prophets is made by his accusers before Pilate, "
  "beside the charges about tribute and about turning away women and children; the narrative does not endorse it. Irenaeus "
  "(Haer. 1.27.2, as cited by Roth, 337 n. 230) reports that Marcion taught that Christ abolished the law and the prophets; that belongs to the reception of "
  "the text, not to its wording. The reading itself is old and not confined to Marcion's text, since the Old Latin has it. "
  "Epiphanius' charge that Marcion added the words assumes that canonical Luke is the earlier text.")),
]
