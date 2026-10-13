# Audit Method — Proto-Luke Reconstruction

**Status:** binding for the audit that began on 2026-10-12. It extends `docs/WORKING_DOCUMENT.md` §3 and supersedes it where the two differ. The owner may override any default marked **(default)**.

## 1. What is being reconstructed

The object is the gospel text read in Marcion's church (the *Evangelion*). Under the project's premise, that text is the earlier form that canonical Luke expanded: Proto-Luke. The reconstruction recovers what the witnesses show that text contained, in the wording they show.

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

English translates the reconstructed Greek. Terminology follows CLAUDE.md:
- "Jesus", not "the Messenger";
- lowercase "messenger(s)" for ἄγγελος only when the context means human or angelic messengers;
- "the Living One" for ὁ ζῶν;
- no Pauline "spiritual body" language.

The translation does not import the commentary: no interpretive glosses inside the text.

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
- **(default)** The ending follows the attestation. 24:47 is the last attested verse. 24:48–53 is unattested and not printed as text unless the owner decides otherwise (working document §10.5). **Overridden 2026-10-13:** 24:47b–53 is printed as restored by method (§11).

## 11. Restoration by method (added 2026-10-13)

The witnesses decide what is attested. They cannot show a passage they never quote, and a hostile witness's silence (`U−`) or a whole unattested pericope (`U?`) leaves a gap that §4 does not fill. §11 is a second method for that gap. It applies only where no witness and nothing else decides the question.

**The method.** The printed text is read by correspondence, from beginning to end, word by word and sentence by sentence, as Swedenborg reads the letter: every element is taken as the spiritual function it names, with no structure decided in advance. The reading is in `docs/research/correspondence/word_by_word.md`. Each unprinted passage is read at its place by its own words.

**When a passage is restored.** Only when the reading shows the printed text needs it. That means one of the following:
- the printed words point to the missing passage (a reference, a pronoun, or a reply that has nothing to answer); or
- the printed text sets a movement going and does not complete it without the passage.

A passage that only continues the line is not restored. Neither is one the printed text only leans on. These are listed for the owner in `docs/research/correspondence/restorations.md`.

**What restoration does not change.**
- The witnesses' evidence and the class (`A+`, `A−`, `U−`, `U?`) stay in the apparatus as they are.
- The decision reads "printed, restored by method (correspondential reading)", and the `reason` gives the reading's grounds.
- Where the class is `A−`, the note says that the passage is printed against Marcion's text as the witnesses report it.
- The Greek is NA27 checked on the page image (§5). No Marcionite reading is adopted inside a restored passage.

**How it is shown.** In the JSON, a restored verse has `attestation: "restored"`. In the PDF it is printed in a distinct colour, and the chapter notes give the grounds. The batch scripts check that every restored verse carries the §11 decision.

**Part of a verse.** Where the restored words are part of an attested verse (12:28a; 24:47b), the verse keeps its class. Its decision reads "printed; … restored by method", and its wording field and the chapter notes name the restored words. The colour marks whole verses only.

**Wording.** The same reading also tests the adopted Marcionite readings (§5.2–5.3). Where it shows that an attested wording breaks the inner line and the NA27 wording continues it, NA27 is printed. The attested reading stays in the apparatus and the notes, with the reading's grounds. The textual ground on the owner's premise is this: the Fathers report that Marcion's church went on altering its copies (§2), so a wording that turns an inner relation into an outward title or separation is taken to belong to that transmission, not to the original. Where the reading finds an adopted wording neutral or continuing, §5 stands.

**Applications.**
- The first (eight passages: 4:17–21, 14:1–11, 19:28–46, 21:5–6, 22:54–62, 24:33–35, 24:44–46, 24:47b–53) was approved by the owner on 2026-10-13.
- The second follows from the reading run again on the final text (`docs/research/correspondence/second_pass.md`), on the owner's instruction that this reading decides.
  - "Leans on" is dropped as a category.
  - Printed: 12:28a, 18:31–34, 19:27, 23:13–16 and 23:39–43.
  - NA27 wording printed at 10:21 ("and of the earth"), 18:19 ("God") and 21:27 ("in a cloud with power and great glory").
