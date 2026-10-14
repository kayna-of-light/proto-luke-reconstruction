# Audit Method — Proto-Luke Reconstruction

**Status:** binding for the audit that began on 2026-10-12. It extends `docs/WORKING_DOCUMENT.md` §3 and supersedes it where the two differ. The owner may override any default marked **(default)**.

## 1. What is being reconstructed

The object is the gospel text read in Marcion's church (the *Evangelion*). Under the project's premise, that text is the earlier form that canonical Luke expanded: Proto-Luke. The reconstruction recovers what the witnesses show that text contained, in the wording they show. Where a wording is Marcion's alone and the correspondential test of §11 shows it to be later than the text he received, the earlier wording is printed.

It does not add, remove or reword anything because of what a theology (Jamesian, Pauline, Marcionite or orthodox) would lead one to expect. Each reading must be shown from the data. The standing of a scholar or a tradition is not evidence.

A second premise is stated so that it can be tested, not assumed: that this text is Jamesian. The profile of the text the witnesses attest is described in the notes and preambles. Where that profile supports the Jamesian identification, the notes say so. Where it does not, they say that too.

## 2. The data and how much each witness can prove

| Rank | Witness | Edition used | What it can establish |
|---|---|---|---|
| 1 | Tertullian, *Adversus Marcionem* IV (with V where relevant) | Evans, Oxford 1972 (Latin with apparatus; tertullian.org) | Presence or absence of a verse, and its sense. It gives wording only in Latin: a Greek wording drawn from it is a retroversion and is marked as one. Section numbers in the evidence follow the tertullian.org division of Evans' text; in the `roth` field they are Roth's (Moreschini's), which sometimes differ by one section. |
| 1 | Epiphanius, *Panarion* 42.11.6 (78 scholia) and 42.11.17 (refutations) | Holl, GCS 31 (1922), archive.org `epiphanius02epip` | Greek wording when quoted. Explicit statements that something is "not there" (οὐκ ἔχει, παρέκοψε, περιέκοψε). |
| 2 | *Dialogue of Adamantius* | van de Sande Bakhuyzen, GCS 4 (1901), archive.org `derdialogdesadam00origuoft` | Greek wording, but only where a Marcionite speaker quotes the gospel or where the context ties the quotation to Marcion's text. Otherwise the passage is not evidence for Marcion's text. |
| 3 | Other Fathers (Irenaeus, Hippolytus, Origen, Ephrem, Eznik, Jerome) | via Roth 2015 loci, read in the cited context where available | Presence of a verse, and the Marcionites' own reading of it. |
| — | Manuscript tradition of Luke | NA27 (Drive, `Books/optimized` parts 4–6; text identical to NA28 in Luke) with its apparatus; SBLGNT/MorphGNT as a machine-readable control | The base wording where Marcion's wording is unattested. It is also the context for judging an attested variant: who else reads it. |
| — | Western witnesses (D, Old Latin, Old Syriac) | NA27 apparatus; Westcott–Hort vol. 2 for the Western non-interpolations | An independent witness. Agreement with Marcion's text is recorded. A Western reading never places a reading in Marcion's text by itself and never overrides an explicit patristic citation. |
| Finding aids | Roth, *The Text of Marcion's Gospel* (2015): tables of loci (ch. 3) and graded reconstruction (ch. 9); Harnack 1924; BeDuhn 2013 (via the working document); Bilby | — | They locate the evidence and give a second judgement. Every reading used is checked against the primary text. Where a finding aid and the primary text disagree, the primary text prevails, and the disagreement is recorded. |

The Fathers are hostile witnesses. Two kinds of statement are distinguished:
- **Statements about what the text contained.** A quotation, or a report that a passage is missing. These are data. They are tested for internal consistency and against each other.
- **Statements about why the text was so.** "Marcion cut it." "He kept it to deceive." These are polemic. They establish nothing about direction of change and are never used.

The Fathers also report that Marcion's followers kept altering their text (Tertullian, *Marc.* 4.5.7; *Adam.* 96,6–8). So the reconstruction recovers the text the witnesses attest. Where Tertullian (c. 207) and Epiphanius (c. 375) disagree, the difference is recorded as a difference between copies, not resolved by preference.

## 3. Attestation classes (one per verse, or per part of a verse)

| Class | Code | Criterion |
|---|---|---|
| Attested present | `A+` | A witness quotes, paraphrases or unambiguously alludes to the content of the verse as part of Marcion's text. |
| Attested absent | `A−` | A witness states the passage was not in the text (Epiphanius' scholia "not there" / "cut"; Tertullian's explicit statements). Or the witnesses quote continuously across the place without it, and the quoted sequence leaves no room for it. |
| Unattested, probably absent | `U−` | No witness mentions it, and both of the following hold. (a) A witness works through that stretch of text continuously; Tertullian's sequence in *Marc.* IV is the test. (b) The passage would have served that witness's argument against Marcion. Under the no-cutting premise, the silence of a witness who would have used the passage counts (working document, rule 3). The reason is given in every case. |
| Unattested, undetermined | `U?` | No witness mentions it, and the conditions for `U−` are not met. |

Roth's classification is recorded beside ours. His "unattested" covers both `U−` and `U?`.

## 4. What goes into the reconstructed text (default)

1. **`A+` verses are in the text.**
2. **`A−` verses are not in the text.** They are listed in the chapter's notes, with the witness that states their absence.
3. **`U?` verses are in the text only if they belong to a pericope of which at least one verse is `A+`, and they carry the flag `attestation: "unattested"`.** The witnesses cite selectively within passages they discuss. Leaving out every uncited verse inside an attested pericope would produce a text no one ever read. A whole pericope with no attested verse is not in the text. It is listed in the notes as an unattested pericope.
4. **`U−` verses are not in the text.** They are listed in the notes with the reason.
5. The canonical order is kept, except where a witness attests a different order (e.g. Capernaum before Nazareth; 4:27 inside 17:14).

## 5. Wording

1. **Base:** the NA27 text of the verse.
2. **A Marcionite reading replaces the NA27 wording only if** both:
   - it is attested in the primary text of a witness (checked by us, not taken from a finding aid);
   - it is at least "very likely" in the sense of Roth ch. 9 levels 1–2. That means either confirmed by the witness's citation habit, or by two witnesses, or by a Greek quotation that the witness's habits do not explain away.

   Weaker readings ("probable", "possible") are recorded in the notes and do not change the text.
3. **Attested omissions within a verse** remove the words. Example: "handle me and see" and "flesh and" at 24:39, both absent in continuous quotation by two witnesses.
4. **Retroversion.** Where only Tertullian attests a reading, the Greek printed is NA27 unless his Latin cannot render the NA27 Greek. Example: *putabamus* at 24:21. A retroversion is marked in the notes.
5. **Spelling** follows NA27 (Ναζαρά at 4:16, Καφαρναούμ), unless a witness attests otherwise.
6. **Differences between NA27 and SBLGNT** are checked against the NA27 page image. NA27 prevails.
7. **Words NA27 prints in square brackets** are printed, without the brackets, unless a witness to this text lacks them (applied from batch 2 on: 9:2, 10:1).

## 6. Translation

The English translates the reconstructed Greek as printed, including the adopted Marcionite readings. It is made from the Greek, not revised from an existing English version.

**Principles**
- **Say what the Greek says.** A word is not softened or exchanged for the familiar church word: δοῦλος is "slave", ἄγγελος is "messenger".
- **Meaning in use, not etymology.** Where the root says more than the word meant at the time, a note can say so; the translation does not build on it.
- **No theology by typography.** Greek has no capitals. "God" and "the Father" are capitalised, as is "the Lord" where κύριος stands for the divine name. Titles are not (the son of God, the holy one of God, lord said to Jesus).
- **Different Greek words are kept apart** as far as English allows. Where it does not, a translation note names the Greek word.
- **Grammar the English would hide is kept** where it can be: plurals (sabbaths, heavens), continuing imperfects, passives that name no agent, shifts of person and number.
- **No interpretation in the text.** It follows no doctrine and not the project's own correspondential reading. Translation notes explain the choice of words, not the meaning of the passage. A fixed rendering is noted where it first occurs; later notes are given only for choices particular to the passage.

**Fixed renderings**

| Greek | English |
|---|---|
| ἄγγελος | messenger |
| δοῦλος; παῖς; οἰκέτης; μίσθιος; ὑπηρέτης; διακονέω | slave; boy (child, young slave); household slave; hired worker; attendant; serve |
| δαιμόνιον; σατανᾶς; διάβολος | daimon; Satan (kept untranslated, as in the Greek); the slanderer |
| ἀμήν | Amen (kept untranslated, as in the Greek) |
| βασιλεία | kingdom (royal rule as much as realm) |
| ἁμαρτία; ἁμαρτωλός | sin; sinner |
| ἀφίημι (sins, debts); ἄφεσις; ἀπολύω | let go; release; release |
| μετάνοια; μετανοέω | change of mind; change one's mind |
| πίστις; πιστεύω; πιστός | trust; trust (believe, where a content follows); trustworthy |
| σῴζω | save (rescue, make well) |
| μαθητής; ἀπόστολος | learner; emissary |
| κύριος | lord, master; "the Lord" for the divine name |
| ὁ χριστός | the Anointed One |
| ὁ υἱὸς τοῦ ἀνθρώπου; ἄνθρωπος; ἀνήρ | the son of the human; human, person; man, husband |
| ψυχή | soul (the living self) |
| αἰών; ζωὴ αἰώνιος | age; life of the age |
| μακάριος; εὐλογέω | fortunate; bless |
| πτωχός | destitute |
| δίκαιος | just |
| χάρις | favour |
| εὐαγγελίζομαι; κηρύσσω | announce good news; proclaim |
| συναγωγή | assembly |
| ὑποκριτής | play-actor |
| πνεῦμα (ἅγιον) | spirit (holy spirit), lower case |
| ἀνίστημι; ἐγείρω; ἀνάστασις | stand up, rise; raise, get up; rising |
| θεραπεύω; ἰάομαι | heal; cure |
| προσκυνέω | bow down before |
| ὁ ζῶν | the Living One |
| Ἰάκωβος | Jacob (the Greek is the patriarch's name; "James" is a later Latin form) |
| γέεννα; ᾅδης | Gehenna; Hades |

The terminology of CLAUDE.md applies: "Jesus", never "the Messenger"; no Pauline "spiritual body" language.

## 7. Notes

Every note names its evidence: witness and locus, manuscript sigla, edition page. Categories:
- `textual`: attestation and wording;
- `translation`;
- `excision`: renamed in sense to "absent from Proto-Luke", and covering `A−` and `U−`;
- `theological`.

A theological note may draw on the library (literary-compilation). It must:
- say that it is interpretation;
- keep apart three things: (a) what canonical Luke added to Proto-Luke (redaction); (b) what later scribes did to canonical Luke (transmission; the Western non-interpolations); (c) what the Marcionite community made of the text (reception);
- not present as data any claim that the witnesses contradict.

NotebookLM numbers and Gemini outputs are not sources and are removed.

## 8. Role of the library (literary-compilation)

The library supplies:
- the hypotheses to test: Jamesian origin, poverty theology, the "Living One" Christology, and the correspondential composition of the parables;
- the frame for theological notes.

It does not supply readings. Where a library document makes a factual claim about Marcion's text, the manuscripts or the Fathers, the claim is checked in the apparatus. If the witnesses contradict it, the apparatus says so, and the document is listed for correction in Phase F (`docs/audit/library_corrections.md`). The working context is in `docs/audit/library_context.md`.

## 9. Workflow per batch

1. Generate the worksheet for the Luke range, from the tools in the auditor's scratchpad:
   - the current JSON verse;
   - Roth class and loci;
   - Roth ch. 9 graded line;
   - the Tertullian section text;
   - the Epiphanius scholion;
   - Adamantius;
   - SBLGNT Greek.
2. Read each locus in the primary text. Assign the class. Decide the wording. Check the base text against NA27:
   - take the screen's candidate list for the range (`scripts/audit/na27_screen.py`: NA27 pages OCR'd and aligned with SBLGNT);
   - confirm each candidate on the page image;
   - look at the page image for every printed verse the screen marks as noisy.
3. Write the apparatus records (`data/apparatus/luke_NN.json`).
4. Rebuild the JSON chapter from the apparatus: verses, Greek, English, notes, preamble.
5. Run the checks:
   - JSON validity;
   - every verse has a class;
   - every `A+` verse of the range is present;
   - no `A−` or `U−` verse is in the text;
   - every note cites a locus;
   - terminology check.
6. Commit, with the batch's findings summarised in `docs/audit/AUDIT_LOG.md`.

## 10. Defaults the owner may override

- **(default)** `U?` verses inside attested pericopes are printed and flagged. Whole unattested pericopes are not printed. *(Working document §10.2.)*
- **(default)** The order of the witnesses is kept. The model question (Schwegler or Semler) is left open, and notes say "canonical Luke has / lacks". They do not say "Luke added" except where both models agree.
- **(default)** Readings at Roth's "probable / possible" level stay in the notes.
- **(default)** The ending follows the attestation. 24:47 is the last attested verse. 24:48–53 is unattested and not printed as text unless the owner decides otherwise (working document §10.5).

## 11. The text before Marcion: the correspondential test

The witnesses attest the text read in Marcion's church. The text he received differs from it at most in wording: what the witnesses attest as present or absent is so in the received text as well (premise: Marcion did not cut, working document §1.1).

1. **What is tested.** Only the Marcionite readings printed under §5 that no independent manuscript of Luke shares. A reading shared with manuscripts outside Marcion's line (P45, D, the Old Latin, the Byzantine text, and others) existed independently of his church, and stands.
2. **How it is tested.** The whole printed text is translated into its inner sense and read as one story (`docs/research/correspondence/`). A Marcion-only reading gives way to the NA27 wording only if both hold:
   - the reading breaks the inner story of the attested text;
   - the witnesses to Marcion's text are themselves divided, and the earliest of them supports the NA27 wording.
3. **Passages are not tested.** Attested absence is absence. An unattested passage would come into question only if the inner mechanics of the attested text failed without it. In the attested text they do not (`docs/research/correspondence/register.md`).
4. **Result.** One reading gives way: 18:19, "God the Father" (later copies) for "God" (Tertullian). The NA27 wording is printed and the Marcionite reading is recorded in the apparatus. Every other Marcion-only reading stands. Seven remain recorded doubts where both forms run in the inner story (`docs/research/correspondence/decisions.md`).
