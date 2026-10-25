"""Batch 6, chapter 21 of the reconstruction: Luke 23:1–56."""
from batch1_ch2 import U, A
from batch6_patches import G

T = lambda loc, ev: {'source': f'Tertullian, Marc. {loc}', 'evidence': ev}
E = lambda n, ev: {'source': f'Epiphanius, Pan. 42.11.6, sch. {n}', 'evidence': ev}

T421 = T('4.42.1', '"Perductum enim illum ad Pilatum onerare coeperunt quod se regem diceret Christum… Pilato quoque interroganti, Tu es Christus? proinde, Tu dicis…"')
T423 = T('4.42.3', '"Nam et Herodi velut munus a Pilato missus… Delectatus est denique Herodes viso Iesu, nec vocem ullam ab eo audivit."')
T424 = T('4.42.4', '"Et Barrabas quidem nocentissimus vita ut bonus donatur, Christus vero iustissimus ut homicida morti expostulatur. Sed et duo scelesti circumfiguntur illi, ut inter iniquos scilicet deputaretur."')
T427 = T('4.42.7', '"nihil de Pilato postulatum, nihil de patibulo detractum, nihil sindone involutum, nihil sepulcro novo conditum."')

ENTRIES = [
 A('23:1', G('23:1'), 'And the whole multitude of them, standing up, led him before Pilate.',
   'present (Marc. 4.42.1)', [T421]),
 A('23:2', G('23:2', [('διαστρέφοντα τὸ ἔθνος ἡμῶν καὶ κωλύοντα φόρους Καίσαρι διδόναι καὶ λέγοντα',
                      'διαστρέφοντα τὸ ἔθνος ἡμῶν καὶ καταλύοντα τὸν νόμον καὶ τοὺς προφήτας καὶ κωλύοντα φόρους Καίσαρι διδόναι καὶ ἀποστρέφοντα τὰς γυναῖκας καὶ τὰ τέκνα καὶ λέγοντα')]),
   'And they began to accuse him, saying, "We found this man perverting our nation, and abolishing the law and the prophets, and forbidding to give tributes to Caesar, and turning away the women and the children, and saying that he himself is the Anointed One, a king."',
   'present (Marc. 4.42.1; Pan. 42.11.6, sch. 69–70)',
   [T421,
    E(69, 'προσέθετο μετὰ τὸ »τοῦτον εὕρομεν διαστρέφοντα τὸ ἔθνος« »καὶ καταλύοντα τὸν νόμον καὶ τοὺς προφήτας«. Elenchus 69: "the text did not read so, but: we found this man misleading the people, saying that he is Christ a king".'),
    E(70, 'προσθήκη μετὰ τὸ »κελεύοντα φόρους μὴ δοῦναι« »καὶ ἀποστρέφοντα τὰς γυναῖκας καὶ τὰ τέκνα«.')],
   wording=('Marcionite readings adopted: "and abolishing the law and the prophets" after "perverting our nation", and "and turning away the women and the children" after the tribute. Epiphanius states twice, in two scholia, that the text had these words in addition to canonical Luke\'s; NA27 cites both for Marcion (McionE); Roth: very likely. '
            'The rest of the verse is NA27. Epiphanius\' own wording of it is a summary (Roth); NA27 cites McionE also for the omission of "our", which Roth leaves open, and it is printed.'),
   western='"And abolishing the law and the prophets" also stands in Old Latin manuscripts (e b c ff2 gat i) and a few Vulgate manuscripts; c and e have "and he turned away our sons and wives from us" at 23:5.'),
 A('23:3', G('23:3'), 'And Pilate asked him, saying, "Are you the king of the Judeans?" And answering him, he said, "You say it."',
   'present (Marc. 4.42.1)', [T421],
   wording='NA27. Tertullian has Pilate ask "Are you the Christ?"; Roth: possible only, since Tertullian has just spoken of the charge "Christ a king" and goes on to Ps 2 ("against his Christ"). Not adopted.'),
 U('23:4', G('23:4'), 'And Pilate said to the high priests and the crowds, "I find no cause in this man."', 'Inside the attested paragraph 23:2–5.'),
 U('23:5', G('23:5'), 'But they were insisting, saying, "He stirs up the people, teaching throughout all Judea, beginning from Galilee to here."', 'Inside the attested paragraph 23:2–5.'),
 U('23:6', G('23:6'), 'And Pilate, hearing it, asked whether the man was a Galilean;', 'Inside the attested paragraph 23:6–7.'),
 A('23:7', G('23:7'), "and learning that he was from Herod's jurisdiction, he sent him up to Herod, who was himself also in Jerusalem in these days.",
   'present (Marc. 4.42.3)', [T423]),
 A('23:8', G('23:8'), 'And Herod, seeing Jesus, rejoiced greatly, for he had been wanting to see him for a long time, because of hearing about him, and he was hoping to see some sign done by him.',
   'present (Marc. 4.42.3)', [T423]),
 A('23:9', G('23:9'), 'And he was questioning him with many words; but he answered him nothing.',
   'present (Marc. 4.42.3)', [T423], wording='NA27. Tertullian ("he heard no word from him") attests the silence, not the wording.'),
 U('23:10', G('23:10'), 'And the high priests and the scribes had been standing by, accusing him vehemently.', 'Inside the attested paragraph 23:8–12.'),
 U('23:11', G('23:11'), 'And Herod too, with his soldiers, treated him as nothing, and having mocked him, putting a bright garment around him, he sent him back to Pilate.', 'Inside the attested paragraph 23:8–12. NA27 [καί].'),
 U('23:12', G('23:12'), 'And Herod and Pilate became friends with one another on that very day; for before they had been in enmity toward each other.', 'Inside the attested paragraph 23:8–12.'),
 A('23:18', G('23:18'), 'And they cried out all together, saying, "Take this man away, and release Barabbas to us";',
   'present (Marc. 4.42.4)', [T424]),
 A('23:19', G('23:19'), 'who had been thrown into prison for a certain uprising that had happened in the city, and for murder.',
   'present (Marc. 4.42.4)', [T424], wording='NA27. Tertullian\'s "most guilty in life" and "as a murderer" refer to the crimes (Roth: possible).'),
 U('23:20', G('23:20'), 'And again Pilate called out to them, wanting to release Jesus.', 'Inside the attested paragraph 23:18–23. NA27 αὐτοῖς (SBLGNT without it).'),
 U('23:21', G('23:21'), 'But they kept shouting, saying, "Crucify, crucify him!"', 'Inside the attested paragraph 23:18–23.'),
 A('23:22', G('23:22'), 'And a third time he said to them, "Why, what evil has this man done? I have found no cause of death in him; so I will discipline him and release him."',
   'present (Marc. 4.42.4)', [T424], wording='NA27. Tertullian\'s "most just" refers to Pilate\'s finding (Roth); no insight into the wording.'),
 A('23:23', G('23:23'), 'But they were pressing with loud voices, asking for him to be crucified; and their voices were prevailing.',
   'present (Marc. 4.42.4)', [T424], wording='NA27. Tertullian\'s "his death is demanded" refers to the cries (Roth); no insight into the wording.'),
 U('23:24', G('23:24'), 'And Pilate decided that their request should be done;', 'Inside the attested paragraph 23:24–25.'),
 A('23:25', G('23:25'), 'and he released the one who had been thrown into prison for uprising and murder, whom they were asking for; but Jesus he handed over to their will.',
   'present (Marc. 4.42.4)', [T424], wording='NA27. Tertullian attests the release ("donatur"; Roth: ἀπέλυσεν).'),
 A('23:32', G('23:32'), 'And two others also, evil-doers, were being led with him to be done away with.',
   'present (Marc. 4.42.4)', [T424]),
 A('23:33', G('23:33'), 'And when they came to the place called Skull, there they crucified him and the evil-doers, one on the right and one on the left.',
   'present (Marc. 4.42.4; Pan. 42.11.6, sch. 71)',
   [T424, E(71, '»καὶ ἐλθόντες εἰς τόπον λεγόμενον Κρανίου τόπος ἐσταύρωσαν αὐτὸν καὶ διεμερίσαντο τὰ ἱμάτια αὐτοῦ καὶ ἐσκοτίσθη ὁ ἥλιος«.')],
   wording='NA27. Epiphanius\' wording follows Matt 27:33 and runs 23:33, 34b and 45 together; Roth: a summary, possible only.'),
 A('23:44', G('23:44'), 'And it was already about the sixth hour, and darkness came over the whole land until the ninth hour,',
   'present (Marc. 4.42.5)',
   [T('4.42.5', '"Ecce autem et elementa concutiuntur… Hic erit dies de quo et Amos: Et erit illa die, dicit dominus, occidet sol meridie (habes et horae sextae significationem), et contenebrabit super terram."')],
   wording='NA27. Tertullian\'s gloss on Amos 8:9 attests the sixth hour and the darkness over the land (Roth: very likely).'),
 A('23:45', G('23:45'), 'the sun having failed; and the curtain of the sanctuary was torn in the middle.',
   'present (Marc. 4.42.5; Pan. 42.11.6, sch. 71)',
   [T('4.42.5', '"Scissum est et templi velum…"'), E(71, '»… καὶ ἐσκοτίσθη ὁ ἥλιος«.')],
   wording=('NA27. For "the sun\'s light failed" (τοῦ ἡλίου ἐκλιπόντος) Epiphanius has "and the sun was darkened" (καὶ ἐσκοτίσθη ὁ ἥλιος), the reading of A C3 W Θ Ψ f1.13 𝔐 lat sy; NA27 cites McionEvid. '
            'Roth: probable only, because the scholion is a summary in Matthew\'s wording; Ephrem and Eznik, who speak of the sun darkened in Marcionite contexts, were not checked here. Not adopted. Tertullian attests the curtain (Roth: secure).')),
 A('23:46', G('23:46'), 'And calling out with a loud voice, Jesus said, "Father, into your hands I set my spirit." And having said this, he breathed out.',
   'present (Marc. 4.42.6; Pan. 42.11.6, sch. 73)',
   [T('4.42.6', '"Vociferatur ad patrem, ut et moriens ultima voce prophetas adimpleret. Hoc dicto expiravit."'),
    E(73, '»καὶ φωνήσας φωνῇ μεγάλῃ ἐξέπνευσεν«.')],
   wording=('NA27. Both witnesses attest the loud cry and "he breathed out"; Tertullian\'s "having said this" renders τοῦτο δὲ εἰπών. Neither quotes the words of the cry. Tertullian\'s "to the Father… to fulfil the prophets" (Ps 31:5) points to them (Roth: possible). '
            'Adamantius quotes the verse (198,8–12), but as the orthodox speaker; it is not counted.')),
 A('23:50', G('23:50'), 'And look, a man named Joseph, being a member of the council, and a good and just man—',
   'present (Marc. 4.42.8; Pan. 42.11.6, sch. 74)',
   [T('4.42.8', '"Sed si et Ioseph corpus fuisse noverat quod tota pietate tractavit, ille Ioseph qui non consenserat in scelere Iudaeis…"'),
    E(74, '»καὶ ἰδοὺ ἀνὴρ ὀνόματι Ἰωσήφ, καθελὼν τὸ σῶμα ἐνετύλιξε σινδόνι καὶ ἔθηκεν ἐν μνήματι λαξευτῷ«.')],
   wording='NA27 (with NA27\'s bracketed καί). Epiphanius quotes "and behold, a man named Joseph"; the rest is unattested.'),
 A('23:51', G('23:51'), 'this one had not agreed with their counsel and action—from Arimathea, a city of the Judeans, who was waiting for the kingdom of God,',
   'present (Marc. 4.42.8)', [T('4.42.8', '"ille Ioseph qui non consenserat in scelere Iudaeis".')]),
 A('23:52', G('23:52'), 'this one, coming to Pilate, asked for the body of Jesus,',
   'present (Marc. 4.42.7)', [T427]),
 A('23:53', G('23:53'), 'and taking it down, he wrapped it in linen, and laid him in a tomb cut in stone, where no one had yet been laid.',
   'present (Marc. 4.42.7; Pan. 42.11.6, sch. 74)', [T427, E(74, '»… καθελὼν τὸ σῶμα ἐνετύλιξε σινδόνι καὶ ἔθηκεν ἐν μνήματι λαξευτῷ«.')],
   wording='NA27. Both witnesses attest the taking down, the linen and the tomb; Tertullian\'s "new" may come from "where no one had been laid" or from Matt 27:60 (Roth).'),
 U('23:54', G('23:54'), 'And it was the day of preparation, and the sabbath was dawning.', 'Inside the attested paragraph 23:50–54.'),
 A('23:55', G('23:55'), 'And the women who had come with him out of Galilee, following after, looked at the tomb and how his body was laid,',
   'present (Marc. 4.43.1)', [T('4.43.1', '"si nec mulierum illarum officium praeterit prophetia quae ante lucem convenerunt ad sepulcrum cum odorum paratura".')],
   wording='NA27. Tertullian attests the women (Roth: very likely).'),
 A('23:56', G('23:56'), 'and returning, they made ready spices and perfumed oils. And on the sabbath they rested, according to the commandment.',
   'present (Pan. 42.11.6, sch. 75; Marc. 4.43.1)',
   [E(75, '»καὶ ὑποστρέψασαι αἱ γυναῖκες ἡσύχασαν τὸ σάββατον κατὰ τὸν νόμον«.')],
   wording='NA27. Epiphanius has "according to the law" for "according to the commandment"; Roth: "the law" possible only. Not adopted. Tertullian\'s "with the preparation of spices" (4.43.1) refers to 23:56a or 24:1.'),
]

OMITTED = [
 dict(ref='23:13–16', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='Pilate tells the chief priests and rulers that neither he nor Herod found him guilty: a paragraph with no attested verse (METHOD §4.3).')),
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
 dict(ref='23:39–42', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='The two criminals; "Jesus, remember me when you come into your kingdom". Unattested; the answer (23:43) is absent, and the paragraph has no attested verse.')),
 dict(ref='23:43', cls='A−', app=dict(roth='absent', witnesses=[
      E(72, 'παρέκοψε τὸ »σήμερον μετ\' ἐμοῦ ἔσῃ ἐν τῷ παραδείσῳ«.')],
      decision='not printed', reason='Epiphanius states that the text lacked "Today you will be with me in paradise". Tertullian passes from 23:34 to 23:44 (4.42.4–5).')),
 dict(ref='23:47–48', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='The centurion ("certainly this man was righteous") and the crowds beating their breasts: a paragraph with no attested verse.')),
 dict(ref='23:49', cls='U?', app=dict(roth='unattested', witnesses=[], decision='not printed',
      reason='His acquaintances and the women standing at a distance: a one-verse paragraph with no attested verse.')),
]

PREAMBLE = (
 "Every power in us that rules from outside now has truth in its hands. The one from the edges has wanted to see"
 " it for a long time and hopes for a sign. It gets silence. The one at the centre asks again what wrong it has "
 "done, and finds none. But the voices are louder, and the voices win.\n\n"
 "What was locked up for uprising and murder is set free instead.\n\n"
 "At the place of the skull, among those who did evil, truth is put to death. In the middle of the day the sun "
 "fails, and the curtain at the very centre tears down the middle. The last words are not a cry of defeat. They "
 "are a handing over.\n\n"
 "Then someone from the very council that condemned it, who never agreed, asks for the body and lays it in stone"
 " where nothing has lain before. Those who came from the edge watch where it is laid, make ready the spices, "
 "and rest."
)

NOTES = [
 dict(term='The charges before Pilate (23:1–5)', cat='textual', refs=['23:1', '23:2', '23:3'], text=(
  "Tertullian (4.42.1) has the council accuse Jesus of calling himself \"Christ, a king\", and Pilate ask \"Are you the Christ?\". "
  "Epiphanius reports two additions in the charges of 23:2: \"and abolishing the law and the prophets\" (sch. 69) and \"and turning "
  "away the women and the children\" (sch. 70). He answers the first from Matt 5:17 (\"I came not to destroy the law and the "
  "prophets\"), and says that the canonical text reads only \"misleading the people\". Old Latin manuscripts have the first "
  "addition at the same place, and c and e have the second at 23:5, so both readings were known outside Marcion's text. They "
  "are printed. 23:4–5 are not cited and are printed in grey.")),
 dict(term='Herod and the sentence (23:6–25)', cat='textual', refs=['23:7', '23:8', '23:9', '23:18', '23:19', '23:22', '23:23', '23:25'], text=(
  "Tertullian (4.42.2–4) reads the trial through Ps 2 and Isaiah: Herod receives Jesus \"as a gift\" from Pilate (Hos 10:6), is "
  "glad to see him and hears no word from him, as the lamb is silent before the shearer (Isa 53:7). Barabbas, \"most guilty in "
  "life\", is released as if good, and Christ, \"most just\", is demanded for death as a murderer. 23:13–16 form a paragraph that "
  "no witness cites and is not printed; NA27 has no 23:17.")),
 dict(term='The crucifixion (23:26–46)', cat='textual', refs=['23:32', '23:33', '23:44', '23:45', '23:46'], text=(
  "Tertullian (4.42.4) attests the two criminals crucified with Jesus \"so that he was counted among the lawless\", and states "
  "that Marcion removed the dividing of his garments because of Ps 22:18; he answers that the whole psalm is Christ's garment. "
  "Epiphanius' scholion 71 mentions the dividing, but in a summary of the scene in Matthew's wording; Tertullian's statement is "
  "followed. Epiphanius states that \"Today you will be with me in paradise\" (23:43) was not in the text (sch. 72). Tertullian "
  "(4.42.5) attests the darkness at the sixth hour and the torn curtain, and (4.42.6) the loud cry to the Father and \"having said "
  "this, he breathed out\", from which he argues that what breathes out a spirit is flesh. \"Father, forgive them\" (23:34a) "
  "is not in the NA27 text and is not cited by either witness. Simon of Cyrene, the daughters of Jerusalem, the mockery at the "
  "cross, the criminals' exchange, the centurion and the onlookers (23:26–31, 35–42, 47–49) are in paragraphs that no witness "
  "cites.")),
 dict(term='The burial (23:50–56)', cat='textual', refs=['23:50', '23:51', '23:52', '23:53', '23:55', '23:56'], text=(
  "Tertullian (4.42.7–8) argues from the burial: if the body were a phantom, nothing would have been asked of Pilate, taken down "
  "from the cross, wrapped in linen or laid in a new tomb; Joseph, \"who had not consented to the crime\", knew it was a body. "
  "Epiphanius quotes Joseph taking down the body, wrapping it in linen and laying it in a rock-cut tomb (sch. 74), and the women "
  "returning and resting on the Sabbath \"according to the law\" (sch. 75). Tertullian (4.43.1) attests the women who came to the "
  "tomb with spices.")),
 dict(term='"Abolishing the law and the prophets"', cat='theological', refs=['23:2'], text=(
  "Interpretation. In this text the charge that Jesus destroys the law and the prophets is made by his accusers before Pilate, "
  "beside the charges about tribute and about turning away women and children; the narrative does not endorse it. Irenaeus "
  "(Haer. 1.27.2, as cited by Roth, 337 n. 230) reports that Marcion taught that Christ abolished the law and the prophets; that belongs to the reception of "
  "the text, not to its wording. The reading itself is old and not confined to Marcion's text, since the Old Latin has it. "
  "Epiphanius' charge that Marcion added the words assumes that canonical Luke is the earlier text.")),
 dict(term='ἀναστάν, "standing up"', cat='translation', refs=['23:1'], text='ἀνίστημι, used of the whole assembly rising.'),
 dict(term='διαστρέφοντα, "perverting"', cat='translation', refs=['23:2'], text='To turn aside, twist, mislead.'),
 dict(term='καταλύοντα τὸν νόμον καὶ τοὺς προφήτας, "abolishing the law and the prophets"', cat='translation', refs=['23:2'], text='Present in this text, and in the Old Latin. καταλύω, to loosen down, dissolve, abolish. Kept apart from ἀπόλλυμι, "destroy" (4:34).'),
 dict(term='ἀποστρέφοντα τὰς γυναῖκας καὶ τὰ τέκνα, "turning away the women and the children"', cat='translation', refs=['23:2'], text='Present in this text, and in the Old Latin. ἀποστρέφω, to turn away, lead astray.'),
 dict(term='φόρους, "tributes"', cat='translation', refs=['23:2'], text='Plural, as at 20:22.'),
 dict(term='χριστὸν βασιλέα, "the Anointed One, a king"', cat='translation', refs=['23:2'], text='Without articles in the Greek: "an anointed one, a king". The second word explains the first for a Roman.'),
 dict(term='τῶν Ἰουδαίων, "of the Judeans"', cat='translation', refs=['23:3'], text='As at 7:3.'),
 dict(term='Σὺ λέγεις, "you say it"', cat='translation', refs=['23:3'], text='As at 22:70: neither a plain yes nor a plain no.'),
 dict(term='αἴτιον, "cause"', cat='translation', refs=['23:4'], text='A ground for a charge.'),
 dict(term='ἐπίσχυον, "were insisting"', cat='translation', refs=['23:5'], text='To grow stronger, press harder.'),
 dict(term='Ἀνασείει, "stirs up"', cat='translation', refs=['23:5'], text='To shake up, incite.'),
 dict(term='ἐκ τῆς ἐξουσίας Ἡρῴδου, "from Herod\'s jurisdiction"', cat='translation', refs=['23:7'], text="ἐξουσία, here the area under Herod's authority."),
 dict(term='ἀνέπεμψεν, "sent him up"', cat='translation', refs=['23:7'], text='To send up to a higher authority, or send back.'),
 dict(term='ἐξ ἱκανῶν χρόνων, "for a long time"', cat='translation', refs=['23:8'], text='As at 8:27.'),
 dict(term='σημεῖον, "sign"', cat='translation', refs=['23:8'], text='As at 11:16 and 11:29.'),
 dict(term='εὐτόνως, "vehemently"', cat='translation', refs=['23:10'], text='With all their strength.'),
 dict(term='ἐξουθενήσας, "treated him as nothing"', cat='translation', refs=['23:11'], text='As at 18:9.'),
 dict(term='ἐμπαίξας, "having mocked"', cat='translation', refs=['23:11'], text='As at 22:63.'),
 dict(term='ἐσθῆτα λαμπράν, "a bright garment"', cat='translation', refs=['23:11'], text='Shining, splendid clothing.'),
 dict(term='Αἶρε τοῦτον, "take this man away"', cat='translation', refs=['23:18'], text='αἴρω, to lift, take away.'),
 dict(term='ἀπόλυσον, "release"', cat='translation', refs=['23:18'], text='ἀπολύω, as at 6:37.'),
 dict(term='Βαραββᾶν, "Barabbas"', cat='translation', refs=['23:18'], text='An Aramaic name, "son of the father".'),
 dict(term='στάσιν, "uprising"', cat='translation', refs=['23:19'], text='A rebellion, revolt.'),
 dict(term='φόνον, "murder"', cat='translation', refs=['23:19'], text='φόνος, as at 18:20.'),
 dict(term='ἐπεφώνουν, "kept shouting"', cat='translation', refs=['23:21'], text='The imperfect.'),
 dict(term='Σταύρου, "crucify"', cat='translation', refs=['23:21'], text='σταυρόω, to put on a stake or cross.'),
 dict(term='παιδεύσας, "discipline"', cat='translation', refs=['23:22'], text='παιδεύω, to train a child, to punish, here to flog.'),
 dict(term='ἐπέκειντο, "were pressing"', cat='translation', refs=['23:23'], text='To lie upon, press hard.'),
 dict(term='κατίσχυον, "were prevailing"', cat='translation', refs=['23:23'], text='To have the upper hand.'),
 dict(term='ἐπέκρινεν, "decided"', cat='translation', refs=['23:24'], text='To give a judgement, decree.'),
 dict(term='παρέδωκεν τῷ θελήματι αὐτῶν, "handed over to their will"', cat='translation', refs=['23:25'], text='παραδίδωμι, as at 9:44; θέλημα, as at 22:42.'),
 dict(term='κακοῦργοι, "evil-doers"', cat='translation', refs=['23:32'], text='Literally "those who do evil": criminals.'),
 dict(term='ἀναιρεθῆναι, "to be done away with"', cat='translation', refs=['23:32'], text='As at 22:2.'),
 dict(term='Κρανίον, "Skull"', cat='translation', refs=['23:33'], text='κρανίον, a skull: the Greek for the Aramaic Golgotha.'),
 dict(term='ἐφ\' ὅλην τὴν γῆν, "over the whole land"', cat='translation', refs=['23:44'], text='γῆ, land and earth, as at 5:24.'),
 dict(term='ὥρα ἕκτη… ἐνάτης, "the sixth hour… the ninth"', cat='translation', refs=['23:44'], text='Counted from sunrise: about noon to three in the afternoon.'),
 dict(term='τοῦ ἡλίου ἐκλιπόντος, "the sun having failed"', cat='translation', refs=['23:45'], text='ἐκλείπω, to fail, give out, as at 16:9 and 22:32; used of an eclipse.'),
 dict(term='τὸ καταπέτασμα τοῦ ναοῦ, "the curtain of the sanctuary"', cat='translation', refs=['23:45'], text='ναός, the inner sanctuary, as distinct from ἱερόν, the whole temple precinct.'),
 dict(term='μέσον, "in the middle"', cat='translation', refs=['23:45'], text='Down the middle, as at 4:30.'),
 dict(term='παρατίθεμαι, "I set"', cat='translation', refs=['23:46'], text='To place beside, entrust, deposit. Ps 31:5.'),
 dict(term='ἐξέπνευσεν, "he breathed out"', cat='translation', refs=['23:46'], text="To breathe one's last: the breath (πνεῦμα) goes out."),
 dict(term='βουλευτής, "a member of the council"', cat='translation', refs=['23:50'], text='A councillor.'),
 dict(term='ἀγαθὸς καὶ δίκαιος, "good and just"', cat='translation', refs=['23:50'], text='ἀγαθός, as at 6:45; δίκαιος, as at 5:32.'),
 dict(term='συγκατατεθειμένος, "agreed"', cat='translation', refs=['23:51'], text='To vote with, consent to.'),
 dict(term='τῇ βουλῇ καὶ τῇ πράξει αὐτῶν, "their counsel and action"', cat='translation', refs=['23:51'], text='βουλή, plan, decision; πρᾶξις, deed.'),
 dict(term='προσεδέχετο, "was waiting for"', cat='translation', refs=['23:51'], text='To wait for, expect, receive.'),
 dict(term='σινδόνι, "linen"', cat='translation', refs=['23:53'], text='A linen cloth.'),
 dict(term='ἐν μνήματι λαξευτῷ, "in a tomb cut in stone"', cat='translation', refs=['23:53'], text='Hewn out of rock.'),
 dict(term='ἡμέρα… παρασκευῆς, "the day of preparation"', cat='translation', refs=['23:54'], text='The day before the sabbath.'),
 dict(term='ἐπέφωσκεν, "was dawning"', cat='translation', refs=['23:54'], text='Was beginning to shine: the sabbath began at sunset.'),
 dict(term='κατακολουθήσασαι, "following after"', cat='translation', refs=['23:55'], text='To follow behind closely.'),
 dict(term='ἐθεάσαντο, "looked at"', cat='translation', refs=['23:55'], text='As at 7:24.'),
 dict(term='ἀρώματα καὶ μύρα, "spices and perfumed oils"', cat='translation', refs=['23:56'], text='μύρον, as at 7:37.'),
 dict(term='ἡσύχασαν, "they rested"', cat='translation', refs=['23:56'], text='To be quiet, keep still.'),
]
