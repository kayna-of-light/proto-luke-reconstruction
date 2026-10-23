# Proto-Luke Reconstruction — Working Document

**Status:** Groundwork only. Nothing in `data/` has been changed. This document records the position the project is in, everything already established with its sources, and the plan of work. Every later phase starts from here.
**Opened:** 2026-10-12
**Branch:** `claude/kind-pasteur-gbzgpx` (PR against `main`; there is no `develop` branch on the remote)
**Companion repo:** `kayna-of-light/literary-compilation`. Its `data/` library repeats several of the claims audited here (§9).

---

## 0. How to use this document (read first in a new session)

1. Read §1 (position), §3 (rules of method), and §5 (Luke 24 evidence table) before touching anything.
2. The reconstruction in `data/proto_luke.json` was generated in December 2025 through NotebookLM ("The Bible Notebook"). Its numbered references ("1, 2, 5–7") point to NotebookLM sources that are not recoverable from the repository. **Treat every claim in the JSON notes as unverified until it is traced to a primary source listed in §7.**
3. Facts in this document carry page or section references to sources that were actually read. Where something was *not* read, it says so. Do not upgrade an unread source to a read one.
4. Section §7 says where each source physically lives: URL, DOI or Google Drive file ID. Use it to extend your context, not your memory.
5. Do not start the computational work (§8, Phase B) or edit `data/` until the owner approves the phase. The owner explicitly asked that this PR contain only the groundwork.

---

## 1. Where we stand (summary)

### 1.1 The governing premise: Marcion did not cut

The reconstruction rests on the premise that Marcion's *Evangelion* is not an abridgement of canonical Luke. Either it preserves an earlier form of the text that canonical Luke expanded, or it shares a common original with Luke. The owner holds that this is established. Section §2 lists the evidence as read.

The consequence for method matters most. If Marcion did not cut, then a verse missing from his text is not a "Marcionite excision". The question becomes **what canonical Luke added to an earlier text, and why.** It is a redaction question about Luke versus Proto-Luke. It is not a question about late scribes or orthodox copyists.

### 1.2 The owner's argument has been inflated in two ways

The owner's argument is about **what canonical Luke did to Proto-Luke**. Earlier agent-written material (the JSON notes, README and preface, and several literary-compilation documents) replaced it with something different:

- **"Later scribes added anti-Docetic proofs in the second century", tied to the Western Non-Interpolations.** That is a claim about the manuscript tradition *after* canonical Luke existed. It is a different argument from the owner's, and it is applied inconsistently (§5).
- **"Marcion lacked X"** asserted for passages where Marcion's text actually *had* X, or where the evidence is only silence (§5).

### 1.3 What the evidence shows for Luke 24:36–43, the core case

**Present in Marcion's text (attested):**
- 24:37: the disciples think they see a **φάντασμα** ("phantom"). Codex D agrees; canonical Luke has πνεῦμα.
- 24:38.
- 24:39: "See my hands and my feet, that it is I myself, for a spirit does not have bones as you see me having."
- 24:41: he asks for food.
- 24:42–43: he eats the fish.

**Absent from Marcion's text** (all three witnesses quote continuously and agree):
- "handle me and see" (ψηλαφήσατέ με καὶ ἴδετε)
- "flesh and" (σάρκα καί)

**Unattested:**
- 24:36b "Peace to you" (a Western Non-Interpolation)
- 24:40 "he showed them his hands and feet" (a Western Non-Interpolation)

**How the Marcionite community read the verse.** They took 24:39 as Jesus saying he had no bones, like a spirit (Tertullian, *Marc.* 4.43.7). They grounded their own teaching on eating fish in 24:42–43 (Eznik, *De Deo* 407). So they kept the eating scene and still read Jesus as spirit.

**What canonical Luke adds:** touch, flesh, probably 24:40, the Peter tradition (24:12, 24:34), and the scripture-opening and commissioning of the Eleven (24:44–49). Daniel A. Smith (2017) and Shelly Matthews (2017) read this layer as restricting apostolic authority to the Twelve, who touched the risen Jesus in the flesh, and rejecting Paul's pneumatic resurrection. They read it as *not* specifically anti-Docetic. This is the owner's "Luke versus Proto-Luke" argument, with a scholarly basis.

**What the current reconstruction does instead** (v2, the JSON and the compiled PDF):
- It cuts 24:39b–43 wholesale as "late anti-Docetic additions" and gives the reason that Marcion lacked them. The eating was in Marcion's text, so that reason fails.
- It keeps "Peace to you" (a Western Non-Interpolation), contradicting its own stated method.
- It prints πνεῦμα where Marcion's text and Codex D read φάντασμα.

### 1.4 The "editorial fatigue / computer-aided analysis" claim is misattributed

- **The claim:** the README, the JSON `description`, `docs/research_questions.md` Q6, and several literary-compilation documents say "computer-aided analysis of editorial fatigue" shows canonical Luke expanding Marcion's text. They attribute it to Klinghardt, BeDuhn and Vinzent.
- **The trail:** the only footnote (in the literary-compilation *Jamesian Protograph* documents) points to a Google Drive document, *"Reconstructing Proto-Luke: A Guide"* (`1gvijydXnEUUz5zDAS10mFKNJd6s-Nk-cdm0nMoSLX8k`). That document returns "not found". A Drive full-text search found no replacement.
- **The term itself:** "editorial fatigue" occurs 0 times in BeDuhn 2013, in Smith 2017 and in Bilby's study (searched in full text). The only fatigue-type example in the project's own material is the Capernaum reference at Luke 4:23 (§2.5).
- **The research that does exist** is **computational stylometry** by **Mark G. Bilby** (§2.4). It uses binomial tests on morphologically tagged Greek to show that canonical Luke's distinctive features are concentrated in the material absent from Marcion's text. The project has never cited it.

### 1.5 Verse-level problems in chapter 22 beyond 24:36–43

Some verses that are **attested** for Marcion's text are **missing** from the reconstruction:
- 24:17–18
- 24:21a
- 24:25–26

Some verses that are **unattested**, and judged probably absent by BeDuhn, Smith, Klinghardt and Bilby, are **kept**:
- 24:32
- 24:44–45
- 24:52–53, partly

Details are in §5.

### 1.6 The working mistake this document corrects

Earlier in the 2026-10-12 session the assisting agent weighted scholarly status (majority view, peer-review standing, big names) above data. It also recruited a counter-argument it had not checked: Wolter's "Lukan vocabulary in Marcion's text", taken from a footnote in Roth. And it searched only established names, which is how it missed Bilby. The rules in §3 exist to stop this happening again.

---

## 2. Did Marcion cut? The evidence as read

The question is answered from the evidence. Head-counts of scholars are not evidence and are not used here. Each item says what was measured, on what material, and where it was read.

### 2.1 The omissions follow no consistent doctrine

Source: BeDuhn, *The First New Testament* (2013), 82–84 and 87–88; summary at 77.

- Every Marcionite motive proposed for an omission has a counter-example: material with the same "offending" content that stayed in the text. BeDuhn's examples:
  - scripture quoted as authority;
  - God's care for creation (12:24, 12:28);
  - Torah commandments affirmed (10:26–28; 18:20–22);
  - judgement (6:24–25; 12:5; 13:27–28 and others);
  - a "very conventional account of Jesus' death and resurrection".
- BeDuhn (p. 77): "The 'missing' material relative to Luke does not contain any concept contrary to Marcionism not found also in other passages retained in the Evangelion."
- Tertullian himself, *Marc.* 4.43.7, says that Marcion "on purpose… has abstained from crossing out… certain matters opposed to him". He can explain it only as a ruse.
- D. S. Williams, "Reconsidering Marcion's Gospel," *JBL* 108 (1989): 477–496, finds no consistent editorial principle in the 23 passages that can be reconstructed. *Not read directly; reported by BeDuhn, n. 78.*
- BeDuhn, n. 83: Marcion referred to Jesus' baptism by John and did not deny it happened (Epiphanius, *Pan.* 42.3.10). So the absence of the baptism scene is not explained by Marcionite doctrine either.

### 2.2 Harmonization: the text-critical test

Source: BeDuhn 2013, 88–90 and nn. 71–78.

- In some passages Marcion's text and Luke are harmonized toward Matthew; in others they are not. Each has independent harmonizations the other lacks. Harnack counted 34 harmonizations in Marcion's text that are not found in witnesses to Luke; Wilshire counts 32 (n. 71).
- The copies Tertullian used (third century) and Epiphanius used (fourth century) carry *different* harmonizations. Examples (n. 76, after Williams): 12:31 (*primum* = Matt 6:33); 18:19 (εἷς ἐστιν = Matt 19:17 against *sed quis*); 9:41 (a second "how long" = Matt 17:17 and Mark 9:19).
- **The logic.** A separate community that used only this one gospel could not have harmonized it toward Matthew. So the variation must already have existed before Marcion. He adopted a text that was circulating in several copies; he did not produce an edition from one manuscript of Luke.
- Knox (*Marcion and the New Testament*, 1942, 156) concludes that direct derivation in *either* direction is ruled out on text-critical grounds. *Knox not read directly; reported by BeDuhn n. 74.*
- **The minor agreements.** Of McLoughlin's 52 "significant" minor agreements of Matthew and Luke against Mark, 31 can be checked against Marcion's text: 20 are absent and 11 present (BeDuhn n. 88). Marcion's text has about a third of the minor agreements found in the critical text of Luke (p. 93).

### 2.3 What the patristic witnesses could know

Source: BeDuhn 2013, 67–69.

- Marcion never compared his text with Luke's. Tertullian has to *suppose* that the "falsified (*interpolatum*) gospel" Marcion speaks of means Luke (*Marc.* 4.4).
- Tertullian concedes that rival claims about whose text was falsified could not be settled objectively (*Marc.* 4.4).
- No citation of material unique to Luke can be securely dated before Marcion (p. 79, p. 81).

### 2.4 Computational stylometry (Bilby)

Source: Mark G. Bilby, *The First Gospel, the Gospel of the Poor: A New Reconstruction of Q and Resolution of the Synoptic Problem based on Marcion's Early Luke*, LODLIB v4.03 (2024-02-18), Zenodo record 10676806, base DOI 10.5281/zenodo.3927056. **There is a newer v5.01 (2025-03-15, five volumes), Zenodo record 15033575, not yet read.**

**Method**
- Morphologically tagged Greek, using the BibleWorks Greek Morphology schema.
- The text is divided into strata:
  - Qn: Bilby's proposed earliest source, his "new Q";
  - Lk1 = Marcion's text;
  - Lk2 = canonical Luke's additional material.
- For each feature he counts the verses in which it occurs, compares the counts with the expected counts, and gives binomial probabilities (book pp. 133–136, PDF pp. 134–137).
- Word bases: Qn-sourced passages 4,550 words; Mark-sourced passages 1,350; Lk1 originals 100; remaining Lk2 about 13,482.

**Selected results (pp. 134–135)**

| Feature | Qn expected / found | binomial p | Lk1 expected / found | binomial p | Lk2 found |
|---|---|---|---|---|---|
| πρός + accusative ("unto") | 37 / 6 | 3.53e-10 | 12 / 1 | 9.58e-05 | 151 |
| Participle + δέ | 21 / 1 | 1.57e-08 | 7 / 0 | 1.21e-03 | 89 |
| Oracular-poetic speech | 15 / 0 | 3.98e-07 | 5 / 0 | 9.13e-03 | 63 |
| λέγω + πρός ("say unto") | 11 / 0 | 1.33e-05 | 4 / 0 | 2.80e-02 | 48 |
| Lukan words found nowhere else in the NT | 66 / 41 | 7.00e-04 | 21 / 5 | 3.25e-05 | 235 |
| Angels as characters | 10 / 1 | 7.02e-04 | 3 / 0 | 4.65e-02 | 40 |

About 70 lexical and grammatical features are listed, plus thematic clusters: Temple piety, salvation-history fulfilment, haste, dramatization, aristocratic patronage, LXX quotation, and others.

**His argument (p. 133)**
- The null hypothesis is that Marcion's text is an abridgement of canonical Luke by the same author.
- Canonical Luke's signature features are disproportionately absent from Marcion's text.
- An abridger would have had to remove "several hundred clusters… with extraordinary consistency". He calls these "statistical analyses proving the Schwegler hypothesis", i.e. that canonical Luke expanded an earlier text.

**Mark coverage (p. 103)**
- Marcion's text lacks 35.7% of Mark's passages (40/112).
- Matthew lacks 5.4% and canonical Luke 10.7%.
- Marcion's text follows Mark 1:16–3:19a *more* faithfully than Matthew does (92.9% against 85.7%).

**Luke 24 (pp. 708–716)**
- 24:12 absent: "a dense cluster of characteristic LkR2 features" (θαυμάζω, πρός + accusative, the reflexive pronoun, τὸ γεγονός, haste, focus on Peter).
- 24:36 absent: "characteristic of Lk2".
- 24:39 without ψηλαφήσατέ με καὶ ἴδετε and without σάρκα: "LkR2 added that phrase under the influence of the Jn2 Thomas narrative".
- 24:40 absent: it continues the same redaction.
- 24:41–43 **present** in Lk1 (food request, fish, eating). Only ἀπὸ τῆς χαρᾶς καὶ θαυμαζόντων ("from joy and wondering") and ἐνώπιον αὐτῶν ("before them") mark canonical Luke.
- 24:44–46 absent.

**Method points to test, not to dismiss**
- Bilby builds his own earlier-Luke text and removes what he calls "Lk2 contaminations" from the other reconstructions (p. 134 n. 89). A replication on an *independently* reconstructed text (Roth's, without his cleaning) will show whether the result depends on that step. This is Phase B, §8.
- The book is a living edition deposited on Zenodo. The datasets were reviewed by the *Journal of Open Humanities Data* (§7.3). The only published review found is Litwa's (2024). Litwa states that he is not competent to assess the statistics and addresses only readability and peer-review form. That says nothing either way about the data.
- **Licence:** the book is CC-BY-NC-ND 4.0. Its front matter also says no part may be used as training data for any large language model. Analysis and citation are permitted; do not commit its text into this repository.

### 2.5 Narrative seam at Luke 4:23

The closest case to an editorial-fatigue argument the project has.

- **The seam:** canonical Luke puts Nazareth (4:16–30) before Capernaum (4:31–37). Yet at Nazareth the crowd says "what we heard happened in Capernaum, do here". Nothing has happened at Capernaum yet in Luke's order.
- **Marcion's text** has Capernaum first, so the line fits.
- **Who argues it:** Couchoud ("Is Marcion's Gospel One of the Synoptics?", p. 269, quoted in BeDuhn n. 66) and Klinghardt (as summarized by Litwa 2025).
- BeDuhn n. 66 shows that Loisy's alternative fails: the Capernaum reference is not in Mark; it is peculiar to Luke's version.
- The current reconstruction already uses this argument (`docs/research_questions.md` Q1). **It is the one place where the "editorial fatigue" label applies in the Goulder/Goodacre sense.** Cite it as that, not as "computer-aided analysis".

### 2.6 Arguments on the other side, with their actual reach

- **Lukan redactional vocabulary inside Marcion's text.** Wolter, *Lukasevangelium* 3, cited in Roth 2015, ch. 2 n. 367: βασιλείαν τοῦ θεοῦ κηρύσσειν/εὐαγγελίζεσθαι at 4:43 and 16:16.
  - *Reach:* two phrases. They show that Marcion's text shares some Lukan idiom. That fits the common-original and same-milieu models as well as the abridgement model.
  - Roth (n. 366) shows that Klinghardt's attempt to remove εὐαγγελίζεται at 16:16 fails, because Tertullian prefers *adnuntiare* (95 against 28 uses).
  - Bilby's counts (§2.4) test exactly this question across the whole text. **This argument has to be weighed against those counts, not used on its own.**
- **Hays,** "Marcion vs. Luke: A Response to the Plädoyer of Matthias Klinghardt," *ZNW* 99 (2008). **Not read.**
- **Knox and Tyson's mixed model:** Marcion shortened, Luke expanded. BeDuhn 90–91 discusses it. Tyson makes a strong case that Luke 1–2 is a late addition, which removes much of what had been attributed to Marcion's cutting (BeDuhn 91).
- **Smith 2017** allows that Marcion "probably did adapt this text to his own needs" (p. 52). He also rates the case for Marcion's priority in Luke 24 "suggestive, though admittedly not conclusive" (pp. 41, 61). These are statements of how far his evidence reaches; record them as such.

### 2.7 Which model? (Open — affects how absences are read)

| Model | Who holds it | What an absence in Marcion's text means |
|---|---|---|
| Schwegler: canonical Luke expanded Marcion's text | Klinghardt 2015/2021; Bilby; Vinzent; Couchoud; Townsend | A Lukan addition |
| Semler: both developed independently from a common original | BeDuhn 2013; Smith 2017 leans this way | Addition on Luke's side, *or* a difference on Marcion's side; decided passage by passage |
| Mixed: Marcion and a predecessor shortened, Luke expanded | Knox 1942; Tyson 2006 | Either |
| Patristic: Marcion abridged Luke | Harnack; Roth's framing is cautious | A Marcionite cut |

The owner's premise excludes the patristic model. Between Schwegler and Semler, the reconstruction should state which it adopts. The Luke 24 results in §5 come out the same under both.

**Terminology warning.** "Proto-Luke" means different things in the literature:
- Streeter and Taylor: Luke minus its Markan blocks.
- BeDuhn: a possible common original.
- This project: the text Marcion had, read as the Jamesian Protograph.

BeDuhn (p. 93) points out that Marcion's text is *not* the Streeter Proto-Luke, because it already integrates Markan material. The preface and README must define the term.

---

## 3. Rules of method (binding for all phases)

1. **Evidence before status.** Never use "the majority holds" or "not peer-reviewed" as an argument. State what a study measured, on what material, by what method, and how far the result reaches. (This repeats the literary-compilation CLAUDE.md rules "Do Not Recruit Objections" and "Confirmation Is Not a Defect".)
2. **Search beyond the big names.** For every question, search by *method and data*, e.g. "stylometric", "binomial", "morphological tagging", "Marcion Luke dataset". Search by author name only after that. Search Zenodo, Dataverse and Academia as well as journals.
3. **Under the no-cutting premise, a witness's silence is evidence.** Where Tertullian or Epiphanius go through a passage continuously, and a verse would have been ammunition against Marcion, their silence counts toward absence. Record each case as one of:
   - **attested present**: quoted or paraphrased;
   - **attested absent**: a continuous quotation without it, or the fathers say explicitly that it was missing;
   - **unattested, probably absent**: the witnesses run continuously through the passage and would have used it;
   - **unattested, undetermined**: the passage is skipped.

   Roth's rule that "unattested is only unattested" is a reconstruction-editor's convention. It is not this project's evidential rule, but always record Roth's classification beside ours.
4. **Explicit patristic citation outranks the Western witnesses for Marcion's text.** Smith (2017, 45–49) shows that Klinghardt prefers Western readings even against what the fathers explicitly cite (24:6, 24:9). The Western text is a separate witness: record its agreement or disagreement, but don't let it override a citation.
5. **Keep redaction separate from transmission.** "What canonical Luke added to Proto-Luke" is one claim. "What later scribes added to canonical Luke" (the Western Non-Interpolations, in Westcott and Hort's sense) is another. Never merge them in a note.
6. **The earliest attested reader leads.** Where the Marcionite community's own reading of a passage is attested, record it and give it precedence over the heresiologist's gloss. Examples: 24:39 (Tertullian, *Marc.* 4.43.7); the fish (Eznik, *De Deo* 407). Tertullian's "to show that he even had teeth" is his own polemic, not the text.
7. **No untraceable sources.** NotebookLM references and Gemini outputs are not sources. Every note in the JSON must name a primary source (patristic passage, manuscript, edition with page) or a scholarly work with page.
8. **Pre-register computational tests.** Write each prediction, and what would count as a miss, before running the test (Phase B, §8).
9. **Stay within the project's register.** Jamesian terminology applies ("the Living One", not "Soma Pneumatikon"; "Jesus", not "the Messenger"). The JSON note on 24:39 calls the resurrection teaching "Jamesian/Pauline" and quotes 1 Cor 15:50. That leans on Paul to argue for a Jamesian text; revisit it.

---

## 4. The repository as it stands

### 4.1 Files

| Path | What it is |
|---|---|
| `data/proto_luke.json` | Primary data, 391 KB. Keys: `title`, `description`, `chapters[]`. Each chapter has `chapter`, `title`, `preamble`, `verses[]` (`verse`, `canonical_ref`, `english`, `greek`), `notes[]` (`id`, `term`, `explanation`, `verse_refs`, `category`: textual / translation / excision / theological) and `additional_explanation` (`title`, `content`, `points[]`). Note: CLAUDE.md describes an older schema (`chapter_number`, `greek_text`, `english_translation`); the JSON does not use it. |
| `data/reconstructions/THE GOSPEL (PROTO-LUKE)_ CHAPTER N[ (Greek)].md` | v1 NotebookLM outputs, 23 Dec 2025, English and Greek. They use the retired terms "the Messenger" and "Soma Pneumatikon". |
| `data/reconstructions/THE GOSPEL (PROTO-LUKE; v2)_ CHAPTER N (Greek).md` | v2 NotebookLM outputs, 24 Dec 2025 (chapter 22 is English). |
| `docs/research_questions.md` | Questions 1–6, rounds 2–3. Q4, Q5 and Q6 are "PENDING IMPLEMENTATION". Q6 holds the editorial-fatigue claim. |
| `output/Proto-Luke_Jamesian_Protograph.pdf` | Compiled PDF, 106 pp., 25 Dec 2025. It matches the JSON. Drive copy: `10mKfiXA35zcEzNPuZONX3KlJeQuoB5cl`. |
| `scripts/json_to_pdf.py`, `json_to_latex.py`, `generate_text.py` | Output generation (ReportLab; Windows font paths are hard-coded). |

### 4.2 Chapter-to-Luke mapping (from `canonical_ref`)

| Ch | Luke passages included |
|---|---|
| 1 | 3:1, 4:31, 4:32, 4:16, 4:22, 4:23 |
| 2 | 4:33–35, 40–41, 43; 5:1–6, 8, 10–14 |
| 3 | 6:12–49 (selection) |
| 4 | 7:1–50 (selection) |
| 5 | 8:1–3, 16–18, 20–22, 24–25 |
| 6 | 8:26–55; 9:1–17 (selection) |
| 7 | 9:18–62 (selection) |
| 8 | 10:1–4, 9–11, 16, 21–22, 25–28 |
| 9 | 11:1–52 (selection) |
| 10 | 12:2–56 (selection) |
| 11 | 13:10–29 (selection) |
| 12 | 14:12–33 (selection) |
| 13 | 15:1–10 |
| 14 | 16:9–31 |
| 15 | 17:1–32 (selection), with 4:27 placed between 17:13 and 17:14 |
| 16 | 18:1–43 (selection) |
| 17 | 19:1–46 (selection) |
| 18 | 20:1–46 (selection) |
| 19 | 21:1–38 (selection) |
| 20 | 22:1–70 (selection; 22:19a only, without 19b–20) |
| 21 | 23:1–53 (selection) |
| 22 | 24:1–3, 4–5, 6–8, 9–11, 13–16, 19, 30–31, 32, 36–39, 44–45, 47–48, 51, 52–53 |

**Open question for Phase C:** the selection criterion was never written down. Some omissions follow Marcion's attestation (e.g. 4:27 placed inside 17:14 follows Tertullian, as BeDuhn also has it). Others look like abridgement. Phase C rebuilds the inclusion of every verse from evidence.

### 4.3 How the reconstruction came to be (Drive)

All are Google Docs in the Drive folder `1Jv3PqlFCzi2iBFYNzXnL9Ui6aRVgNUqy` unless noted.

- **v1 chapter 22 "(includes tomb)",** `1L2lTw7dh_GXml5QyKnyKmmFXcw9R1fa14F4eXJTJVnU`.
  - Framed as an "Excision Protocol to remove the second-century 'Anti-Docetic' additions".
  - *Keeps* 24:6a ("He is not here, but has been raised"), with a note on the passive ἠγέρθη.
  - Omits 24:12 as "a Western Non-Interpolation… added later to harmonize Luke with John".
  - Includes 24:33 and 24:35.
  - Omits **all** of 24:39–43, including 39a, as "2nd-century anti-Docetic interpolations… to 'lock down' a physicalist theology".
  - Uses "Messenger" and "Soma Pneumatikon".
- **v2 chapter 22,** `1etelpf-LwrIzOkIqA-w6mWzb3O5Zu3CkwOZhRutawpY`. The basis of the JSON and PDF.
  - Omits 24:6a ("absent in the Western text (Codex Bezae) and the Marcionite witnesses").
  - Keeps 24:36 "Peace to you" and 24:39a; omits 24:39b–43.
- **The v1 → v2 changes** (24:6a dropped, 24:39a restored) are recorded nowhere. Smith 2017, 47, shows that **Klinghardt** omits the whole line of 24:6 against Epiphanius. That is the probable source of v2's 24:6a omission. *Not verified: Klinghardt not read.*
- **Other chapter drafts** in the same folder: e.g. chapter 1 `1zxhLdvmm0gyYsWR1svX-4zDNzdiaZi2EeOuCXLwRr1M`, chapter 8 `1geLgwZ-afNYiBFJraLhIqOtBIZSeulrVnsbzmDNiLdo`, chapter 14 `1-f46lTYs81ogMOtpLKQLnKDBAWjGA2um_CjYbgSXAp8`, chapter 16 `1YmiiQPNasl2ABSgbznWjPM7V9iwLwsKeKAEf1gzGpkw`. Several say "this revision acknowledges the lack of 'editorial fatigue' in the Marcionite witnesses". That is the origin of the fatigue language.
- **NotebookLM: "The Bible Notebook"** (link in CLAUDE.md). Its source list has not been exported. **Action for Phase A:** ask the owner for the notebook's source list, so the numbered references can be mapped.

---

## 5. Luke 24 — evidence table and the current reconstruction

**Abbreviations**
- T = Tertullian, *Adversus Marcionem* book 4.
- E sch. = Epiphanius, *Panarion* 42 scholia (GCS 31, Holl).
- Ad = Adamantius, *Dialogue* 5.12.
- Ez = Eznik, *De Deo* 407.
- R = Roth 2015 (page).
- B = BeDuhn 2013 (page).
- K = Klinghardt 2015 (page, via Smith 2017).
- Bi = Bilby v4.03 (page).
- WNI = Westcott–Hort "Western non-interpolation". The list, from WH 1882 vol. 2, Introduction §240 (pp. 175–177) and §383 (pp. 294–295), and Appendix pp. 71–72: Matt 27:49; Luke 22:19b–20; 24:3, 6, 12, 36, 40, 51, 52.
- D = Codex Bezae; it = Old Latin; sy^s,c = Sinaitic and Curetonian Syriac.
- JSON = current `data/proto_luke.json`, chapter 22.

| Luke | Element | Marcion's text | Western / WNI | Scholars | JSON now | Assessment |
|---|---|---|---|---|---|---|
| 24:1–3 | Women at tomb; "did not find the body" | Present, T 4.43.1–2. "Of the Lord Jesus" unattested (R 266 n. 423: silence cannot establish its absence) | 24:3 WNI ("of the Lord Jesus" lacking in D, it) | B 193–194: Marcion's text had "the body" without the phrase, "certainly more original". Tyson: κύριος Ἰησοῦς is Acts vocabulary, not Luke's | Kept without the phrase | **Holds** |
| 24:1b | "They were saying among themselves, who will roll away the stone" | Unattested | Longer reading in D 070 c | K treats it as "probable" for Marcion against the silence of the witnesses (Smith 46) | Not included | Correctly not included |
| 24:4 | "In shining/dazzling clothing" | E sch. 76: ἐν ἐσθῆτι **λαμπρᾷ** | ἀστραπτούσῃ is a minor agreement with Matthew | B 194 and Smith 47: λαμπρᾷ, without the minor agreement. R and K give ἀστραπτούσῃ as "possible" | ἀστραπτούσῃ; note 2 builds a "pneumatic radiance" reading on it | **Fix:** follow the attested λαμπρᾷ; rewrite note 2 |
| 24:5 | "Why do you seek the living among the dead" | Present, E sch. 76 | — | — | Kept | Holds |
| 24:6a | "He is not here, but was raised" | **ἠγέρθη present**: E sch. 76 (*Pan.* 42.11.17); T 4.43.5. R 342, 435 holds ἠγέρθη secure. οὐκ ἔστιν ὧδε, ἀλλά unattested; B 194: Marcion's text read "he was raised" alone, as Mark 16:6 has ἠγέρθη | WNI (D and it lack both clauses) | K omits the whole line against Epiphanius (Smith 47) | The whole of 6a omitted. Note 3/8: "absent in… the Marcionite witnesses" | **Note is false** for ἠγέρθη. **Fix:** restore ἠγέρθη; omit "he is not here, but"; give the evidence |
| 24:6b–7 | "Remember how he spoke to you…" | Present. E: "remember how he spoke while he was still with you"; T: "in Galilee". Both lack "into the hands of sinful men"; E also lacks "and be crucified" (B 194) | — | Smith 60: the command to *remember* replaces Mark 16:7's commission to the women, an early restriction | Kept, *with* "into the hands of sinful men" | **Fix:** drop "into the hands of sinful men" (attested absent in both witnesses) |
| 24:8 | "And they remembered his words" | Unattested; lacking in a couple of Greek MSS (B 194) | — | — | Kept | Mark it as unattested |
| 24:9–11 | Report to the disciples; disbelief | Present, T 4.43.2–3, 5: "from the tomb", reported to "**the pupils**" (not "the eleven and all the rest"). Start of v. 11 not cited (B 194). 24:10 unattested | D, it omit "from the tomb" | K follows D against T (Smith 49) | Kept as "the eleven and to all the rest" | **Fix:** "to the disciples"; keep "from the tomb" |
| 24:12 | Peter runs to the tomb | Unattested, and **probably absent**: neither father knows it; no writer before Ambrose cites it (Smith 49–50). R 26 n. 112, 78: "unattested" | WNI | B 195; Lieu 218; K 1130; Smith (who argues for Lukan style) agrees with K that it is Lukan redaction inserted into the earlier text (Smith 53). Bi 708: a dense cluster of Lk2 features | Omitted. Note 6: "secondary interpolation found in the Alexandrian tradition" | **Omission holds; reason wrong.** Rewrite as Lukan redaction (Luke versus Proto-Luke), tied to 24:24 and 24:34 |
| 24:13–16 | Emmaus: two travel; Jesus joins; eyes held | Present, T 4.43.3; E sch. 77. 24:14 unattested | — | — | Kept including 24:14 | Mark 24:14 as unattested |
| 24:17–19a | "What are these matters…?"; Kleopas; "What sort of things?" | **Present**, T 4.43.3 ("He even pretended not to be aware"); E sch. 77 names Kleopas (B 195) | — | — | **24:17–18 missing**; only 19 kept | **Fix:** restore 24:17–18 |
| 24:19b–20 | "Jesus the Nazarene… a prophet mighty in deed and word…" | **Unattested** (B 195) | — | — | Kept as verse 6 | **Flag.** "Prophet mighty in deed and word" is unattested for Marcion's text. Under rule 3, classify as undetermined or probably absent. A literary-compilation framework document takes its title from this phrase (§9). Decision needed |
| 24:21a | "We supposed him to be the ransomer of Israel" | **Present**, T 4.43.3: *putabamus*, *redemptorem Israelis* (B 195) | — | Smith 59 | **Missing** | **Fix:** restore with the attested wording |
| 24:21b–24 | Recap; "some of those with us went to the tomb" | Unattested; B 195: "appears to be a summary of John 20.1–10". 24:24 presupposes 24:12 | — | B; K and B "probably absent" (Smith 51 n. 52) | Omitted | Holds |
| 24:25–26 | "O senseless… slow of heart to trust **all the things he spoke** to you"; "necessary for the Christ to suffer" | **Present**: E sch. 77; T 4.43.4; Ad 5.12. All have "to you"; T has "all the things he spoke", E and Ad "that I spoke", against Luke's "that **the prophets** said" (B 195–196) | — | — | **Missing** | **Fix:** restore. The reading differs from canonical Luke in a way that bears on scripture-authority redaction (Smith 59) |
| 24:27 | Interprets Moses and the prophets | Unattested; "would surely have been commented upon" (B 196) | — | Probably absent (B, K, Smith 59) | Omitted | Holds |
| 24:28–29 | Arrival; "stay with us" | Unattested; some content needed for the narrative (B 196) | — | — | Omitted | Mark narrative bridge as needed |
| 24:30–31 | Breaking of bread; eyes opened; "vanished" | Present, E sch. 77 (the last clause of v. 31 not quoted, B 196) | — | — | Kept including ἄφαντος | Mark ἄφαντος as unattested; note 13 builds on it |
| 24:32 | "Was not our heart burning… as he opened the scriptures" | **Unattested**; "would certainly have been cited" (B 196) | — | Probably absent (B 196; Smith 59 n. 99) | **Kept** (verse 8), with notes 12 and 14 on "opening the scriptures" | **Fix:** remove or mark probably absent; rewrite notes 12 and 14 |
| 24:33–35 | Return; "appeared to Simon" | Unattested; 24:34 "almost certainly absent" (B 196) | — | Smith 51: 24:34 depends on 1 Cor 15:5; with 24:12 it restricts the witnesses to Peter and the Eleven | Omitted | Holds; record the reason |
| 24:36 | "He stood among them" + "Peace to you" | Unattested (B 196) | "Peace to you" = WNI | Bi 713: absent, characteristic of Lk2 | **Kept including "Peace to you"** | **Fix:** remove "Peace to you"; contradicts the reconstruction's own stated rule |
| 24:37 | They think they see a **phantom** | **φάντασμα**, T 4.43.6; Ad 5.12 (B 196) | D, d: φάντασμα | Smith 54: only Marcion's text and D use the correct word for a ghost; canonical Luke's double πνεῦμα looks redactional (K 1151) | πνεῦμα; note 15 builds on it | **Fix:** φάντασμα; rewrite note 15 |
| 24:38 | "Why are you troubled…" | Present: T, Ad; E abbreviates (B 197; Bi 713) | — | — | Kept | Holds |
| 24:39 | "See my hands and my feet, that it is I myself, for a spirit does not have bones as you see me having" | **Present** in this form: E sch. 78 (ἴδετε τὰς χεῖράς μου καὶ τοὺς πόδας μου, ὅτι πνεῦμα ὀστᾶ οὐκ ἔχει, καθὼς ἐμὲ θεωρεῖτε ἔχοντα); T 4.43.6 (*Videte manus meas et pedes, quia ipse ego sum, quoniam spiritus ossa non habet, sicut me habentem videtis*); Ad. **Attested absent:** "handle me and see" (all three) and "flesh and" (T, E). R 345–346, 435 | Tertullian (*Carn. Chr.* 5) and Ephrem (*Against Bardaisan*) also quote it without "flesh and", outside an anti-Marcionite context (B 197) | Marcionite reading: no bones, as a spirit has none (T 4.43.7). Smith 54–58: touch and flesh are canonical-Luke redaction restricting authority to the Twelve, paralleled in Ignatius, *Smyrn.* 3.1–2; not specifically anti-Docetic. Bi 714: "touch me" added under the influence of John's Thomas story | **Only 39a kept**; 39b omitted as "late anti-Docetic" | **Fix:** restore 39b in the attested form, without "flesh" and "handle me"; record the Marcionite reading; rewrite the rationale as Lukan redaction |
| 24:40 | "He showed them his hands and feet" | Unattested (R 26, 78) | WNI (D, it, sy^s,c) | Probably absent (Bi 714) | Not included | Holds; record why |
| 24:41–43 | Asks for food; they give broiled fish; he eats | **Present**: T 4.43.8 (*cibum desideravit*); Ez 407 (Marcionites base their teaching on eating fish on this). R 268, 409, 436. "From joy and wondering" unattested, "evidently a gloss" (B 197) | No WNI. The honeycomb is a later addition (NA28 p. 290; text without it in 𝔓75 ℵ A B D L W) | Bi 715: present in Lk1 except ἀπὸ τῆς χαρᾶς καὶ θαυμαζόντων and ἐνώπιον αὐτῶν. B 72: Marcion's text's resurrection "has a physical character (24.39, 41–42)" | **Omitted** as "late anti-Docetic additions" (note 16) | **Fix:** restore 24:41–43 (without "from joy", "before them" or the honeycomb); rewrite note 16. How the eating is to be *read* is a separate, open interpretive question (§10) |
| 24:44a | "And he said to them…" | Present, T 4.43.9 (B 198) | — | — | Kept as part of 44–45 | Keep 44a only |
| 24:44b–46 | Law, prophets, psalms; "opened their mind" | **Unattested**; "likely to have been cited… if present" (B 198) | — | K: a post-Marcionite creation (Smith 59 n. 94); Bi 716: absent; Smith 59: Tertullian and Epiphanius pass over in silence what would be the clearest anti-Marcionite passage | **Kept** (verse 10), with note 18 calling it "the climax of the Protograph" | **Fix:** remove or mark probably absent; the climax claim has to go |
| 24:47 | Preach to all the nations | Present, T 4.43.9, as direct speech (B 198); "beginning from Jerusalem" unattested | — | K shows 44–49 as unattested (Smith 59 n. 94) | Kept with 24:48 | Keep 47; mark 48 as unattested |
| 24:48–53 | Witnesses; Bethany; parting; return; Temple | Unattested; the ending is not cited by T or E (B 198 excursus) | 24:51b "carried up" and 24:52 "worshipping him" = WNI | B: 24:50–51a could serve as an ending; Acts 1:8b–11 may preserve the earlier ending; the longer ending of Mark parallels it | Keeps 51 ("parted") and 52–53 | Mark all as unattested; decide on the ending explicitly (§10) |

### 5.1 Consequences for the chapter as a whole

- **The preamble and `additional_explanation`** describe a stratum "defined by the Western Non-Interpolations" whose "physicalist proofs (flesh, bones, and eating)" were "added in the second century to combat Gnosticism". Rewrite this as:
  - **attested Proto-Luke:** the phantom fear; "a spirit has no bones as you see me having"; the meal of fish;
  - **canonical-Luke redaction:** touch, flesh, the Peter tradition, scripture-opening, commissioning of the Eleven;
  - **later transmission:** the WNIs.
- **"Faith comes through the opening of the scriptures, not inspection"** (notes 12, 14, 18) rests on 24:32 and 24:44–45. Those are exactly the verses the evidence makes probably *absent*, and Smith and Klinghardt read them as canonical redaction. The attested Proto-Luke climax is different: recognition at the breaking of bread (24:30–31), the phantom fear answered in Jesus' own terms (24:37–39), the meal (24:41–43), and the sending to all the nations (24:47).

---

## 6. Problems outside Luke 24 already identified (to be verified in Phase C)

1. **The JSON `description`, the README "Methodology" and the "Key Scholarly Sources" section**:
   - claim "editorial fatigue analysis" as method (vector 1), which is untraced (§1.4);
   - list Vinzent's *Christ's Resurrection in Early Christianity* (2011), while the library documents cite *Marcion and the Dating of the Synoptic Gospels* (2014);
   - omit Bilby, Roth, Smith, Lieu, Tyson and Knox.
2. **The README and description "Excised Material" list** includes "baptism, temptation". `docs/research_questions.md` Q2 justifies the cut with Marcionite-ideology reasoning ("subordinate the Messenger to John the Baptist or test him against the 'Creator'"). Under the no-cutting premise that reasoning is upside down. The cut has to rest on Marcion's attested text, not on a motive. Note also BeDuhn n. 83 (§2.1).
3. **Q4 and Q5 terminology** ("the Messenger" → "Jesus"; "Soma Pneumatikon" → Jamesian terms). Marked as resolved but pending implementation. v1 markdown files still contain the old terms. Check the JSON.
4. **CLAUDE.md describes a JSON schema the file doesn't use** (§4.1). Update CLAUDE.md in Phase E.
5. **22:19b–20 (the second cup):** omitted, which agrees with the WNI and the short text. Smith 2017, 49, citing Roth 2012, 311, notes that **part of v. 20 is attested** for Marcion's text (T 4.40.4). A 2020 *Novum Testamentum* article (author not yet identified) argues that Marcion's gospel is a witness for the short text. Re-examine in Phase C.
6. **The chapter 1 incipit** (3:1 + 4:31 + 4:32 + 4:16 + 4:22 + 4:23) follows the attested order. Keep the 4:23 seam argument and cite it properly (§2.5).

---

## 7. Source inventory — where everything lives

Status:
- **R** = read in full or in the relevant part, in the 2026-10-12 session.
- **P** = partly read.
- **N** = not read.
- **Lost** = the session copy is gone; re-download from the location given.

### 7.1 Primary sources

| Source | Location | Status |
|---|---|---|
| Tertullian, *Adversus Marcionem* 4 (Latin) | tertullian.org Latin text (`adv_marc_4` pages); Evans edition, Oxford 1972, English with Latin at tertullian.org/articles/evans_marc | R (4.43; 4.4) |
| Epiphanius, *Panarion* 42, scholia 76–78 (Greek) | Holl, GCS 31. Quoted via Roth and BeDuhn. **Obtain a direct text** (archive.org: Holl, *Epiphanius II*) | P (via secondary sources) |
| Adamantius, *Dialogue* 5.12 | GCS 4 (van de Sande Bakhuyzen); quoted via BeDuhn and Bilby | N directly |
| Eznik of Kolb, *De Deo* 407 | Armenian; quoted in Bilby 715 n. 824, B 197, R 409 | P (via secondary sources) |
| Ignatius, *Smyrnaeans* 3.1–3 | Any edition; Smith 2017, 55, 57 quotes it | R (via Smith) |
| NA28 (Luke 24 apparatus, p. 290) | Drive `1BgywaOKTYeB6IHbSO_W4F3AJDStBS1-U` (full); parts `1gfqLvRbym5XgQwdLHvZxHZ0Ra6caYkpS`, `1zOEtS-j2uUukuZ1HlU2hHetl0uJP2sIM` | R (p. 290) |
| NA27 (CLAUDE.md names NTG 27 as the base) | Drive `1bUoxWJD3aAFNQJVqe0YpEqOmK4dqfVfF` (full, 326 MB); 10–13 parts in folders `1iRPU_sSa44P5k5s0nVRCNayFCjQiVCh2` and `1ItW3DfpQKILLYXXQFiQlH31o43mlUb91` | N |
| BHS (for the LXX/HB side) | Drive `1QLTO8V5JAWhxeyFQHpfLifKE-MzQgsKI` (full) and parts | N |
| Westcott & Hort, *The New Testament in the Original Greek*, vol. 2 (1882) | archive.org identifier `newtestamentino02hortgoog` (Introduction §§240, 383; Appendix, Notes on Select Readings, pp. 71–72) | R (relevant sections) |
| SBLGNT + MorphGNT (morphologically tagged Luke) | github.com/morphgnt/sblgnt (CC-BY-SA). Needed for Phase B | N |

### 7.2 Reconstructions of Marcion's gospel

| Work | Location | Status |
|---|---|---|
| Roth, Dieter T., *The Text of Marcion's Gospel*, NTTSD 49 (Leiden: Brill, 2015) | Drive `1RjQpaB62J1xb9Bx4ngPIkEQnIltqGWlu`; second copy `1sdSmhOucbmufX-0mM-lZIVofSNBcjzSD` | P (Luke 24 entries pp. 26, 78, 266–268, 342, 345–346, 409, 435–436; ch. 2 on the history of research) |
| BeDuhn, Jason D., *The First New Testament: Marcion's Scriptural Canon* (Salem, OR: Polebridge, 2013) | Not in Drive. Read from an online library copy, which was not stored. **Owner to supply a copy for Drive** | R (pp. 65–98, 126–127, 193–199, chapter notes to ch. 3, pp. 350–354) |
| Klinghardt, Matthias, *Das älteste Evangelium und die Entstehung der kanonischen Evangelien*, TANZ 60/1–2 (Tübingen, 2015); English: *The Oldest Gospel and the Formation of the Canonical Gospels* (Leuven: Peeters, 2021) | **Not obtained.** Smith 2017 cites vol. 1, 73–93, 117–141, 165, 171, 351–362; vol. 2, 1116–1158 | N (the essential missing source) |
| Harnack, Adolf von, *Marcion: Das Evangelium vom fremden Gott*, 2nd ed., TU 45 (Leipzig, 1924) | archive.org (public domain). Bilby's normalized dataset: *JOHD* 7 (2021) 24, DOI 10.5334/johd.47 | N |
| Tsutsui, Kenji, "Das Evangelium Marcions," *AJBI* 18 (1992): 67–132 | — | N |
| Nicolotti (2019) reconstruction | Bilby dataset paper on ResearchGate | N |

### 7.3 Studies of priority and redaction

| Work | Location | Status |
|---|---|---|
| Smith, Daniel A., "Marcion's Gospel and the Resurrected Jesus of Canonical Luke 24," *ZAC* 21 (2017): 41–62 | Author's copy, open access: ir.lib.uwo.ca/huron_theologypub/6. PDF: uwo.scholaris.ca/bitstreams/594b5af8-5ee9-45c8-a079-4fed262ed9f8/download | R (complete) |
| Smith, Daniel A., "Seeing a Pneuma(tic Body): The Apologetic Interests of Luke 24:36–43," *CBQ* 72 (2010): 752–772 | — | N |
| Smith, Daniel A., *Revisiting the Empty Tomb* (Minneapolis, 2010), 99–118 | — | N |
| Matthews, Shelly, "Fleshly Resurrection, Authority Claims, and the Scriptural Practices of Lukan Christianity," *JBL* 136 (2017): 163–183 | Project MUSE, muse.jhu.edu/article/652365 (paywalled); author page tcu.academia.edu/ShellyMatthews | N |
| Bilby, Mark G., *The First Gospel, the Gospel of the Poor*, LODLIB | v4.03: Zenodo 10676806 (84.7 MB, one PDF). **v5.01: Zenodo 15033575 (5 volumes: intro, synopsis, tables, attestations, resources)** | R (v4.03 pp. 29–30, 103, 133–136, 708–716); v5.01 N |
| Bilby, "Normalized Datasets of Roth's Reconstruction of Marcion's Gospel," *JOHD* 7 (2021) art. 27, DOI 10.5334/johd.57 | Data: Dataverse DOI 10.7910/DVN/BYPOOR; supplement DOI 10.5334/johd.57.s1; BGM key DOI 10.5281/zenodo.4950243. Two UTF-8 .txt files (readable Greek; lemma + BGM tags). Parentheses = possible or uncertain; omitted readings dropped. Licence CC-BY-NC-ND | Paper P; data N |
| Bilby, Harnack datasets, *JOHD* 7 (2021) 24, DOI 10.5334/johd.47; Klinghardt and Nicolotti datasets (ResearchGate 357441780) | — | N |
| Litwa, M. David, review of Bilby (2024) | mdavidlitwa.com/2024/04/29/review-of-m-bilbys-gospel-of-the-poor/ | R |
| Litwa, summary of Klinghardt 2021 Part III (2025) | mdavidlitwa.com/2025/04/10/how-to-prove-marcions-gospel-came-before-canonical-luke/ | R (secondary) |
| BeDuhn, "The Myth of Marcion as Redactor," *Annali di Storia dell'Esegesi* 29 (2012): 21–48 | academia.edu 107485673 | N |
| BeDuhn, "New Studies of Marcion's Evangelion," *ZAC* 21 (2017): 8–24, DOI 10.1515/zac-2017-0001 | academia.edu 52872815 | N |
| Williams, David S., "Reconsidering Marcion's Gospel," *JBL* 108 (1989): 477–496 | JSTOR | N |
| Knox, John, *Marcion and the New Testament* (Chicago, 1942) | archive.org (check) | N |
| Tyson, Joseph B., *Marcion and Luke-Acts: A Defining Struggle* (Columbia, SC, 2006) | — | N |
| Lieu, Judith M., *Marcion and the Making of a Heretic* (Cambridge, 2015) | — | N |
| Vinzent, Markus, *Marcion and the Dating of the Synoptic Gospels* (Leuven, 2014); *Christ's Resurrection in Early Christianity* (2011) | — | N |
| Klinghardt, "Markion vs. Lukas," *NTS* 52 (2006): 484–513; "The Marcionite Gospel and the Synoptic Problem," *NovT* 50 (2008): 1–27 | Cambridge Core / Brill | N |
| Hays, Christopher M., "Marcion vs. Luke," *ZNW* 99 (2008), esp. 228–230 (cited by BeDuhn n. 69) | researchgate 240753253 | N |
| Gregory, Andrew, *The Reception of Luke and Acts in the Period before Irenaeus*, WUNT II 169 (Tübingen, 2003) | — | N |
| "Das Problem von Kurz- und Langtext in Lk 22,17–20 und das für Marcion bezeugte Evangelium," *NovT* (2020), DOI 10.1163/15685365-12341649 | academia.edu 42349711 | N (author to identify) |
| Goodacre, Mark, "Fatigue in the Synoptics," *NTS* 44 (1998); *The Case against Q* (2002) | markgoodacre.org/Q/fatigue.htm | P (method only) |

### 7.4 Related material in the companion repository (literary-compilation)

- `docs/EVOLVING_CONCEPTUAL_STRAINS.md`, strain #9. Rewritten in literary-compilation PR #33 (still open). It frames the eating as resting on a redaction-critical "anti-Docetic motive". **That framing is contradicted by §5 above and has to be revised before the PR is merged.**
- `docs/audit_ledger.md`: a row about the corpus-wide dependency on the Luke 24 claim.
- The Drive library mirrors, e.g. *The Forensic Stratigraphy of the Resurrection*, *The Jamesian Protograph* (two versions), *No Original Exists* (Drive PDF `19WvlMZKtrPBmeacaXfutJlBNRA24mF1W`).

---

## 8. Plan

The phases are ordered. Each phase ends with a commit and a report to the owner. **Phase B is computational and needs the owner's go-ahead before it starts.**

### Phase A — Sources

1. Ask the owner for:
   - the NotebookLM "Bible Notebook" source list;
   - a copy of BeDuhn 2013 for Drive;
   - Klinghardt 2015/2021, the essential missing work;
   - whether the lost *"Reconstructing Proto-Luke: A Guide"* exists anywhere.
2. Download:
   - Bilby v5.01;
   - the Roth and Harnack datasets (Dataverse);
   - MorphGNT/SBLGNT;
   - Holl's Epiphanius (archive.org);
   - Harnack 1924 (archive.org).

   Record each in §7 with its location.
3. Read Klinghardt vol. 2, 1116–1158 (Luke 24) and vol. 1, 73–93 (method). Add a K column to the §5 table.
4. Read Matthews 2017 and Smith 2010 for the authority-restriction argument.
5. Search by **method**, not by name: "stylometr* Marcion", "Marcion Luke dataset", "Marcion Luke redaction statistics", "Evangelion computational". Record every study found in §7, whoever the author is.

### Phase B — Computational stylometry: replication and extension (needs approval)

**Question:** are features characteristic of canonical Luke's own redaction concentrated in the material absent from Marcion's text, beyond what an abridgement would produce?

**Data**
- Luke: SBLGNT text with MorphGNT tags (lemma, part of speech, morphology).
- Marcion's text: Bilby's normalized Roth dataset, used **unaltered** as the primary test, with Roth's certainty levels as published (parenthesized readings in one run, out in another). Bilby's own Lk1 and the Harnack, Klinghardt and Nicolotti datasets are sensitivity runs.
- Verse alignment: map each Luke verse to one of:
  - **attested present**;
  - **attested absent** (Roth's list of verses attested as not present, pp. 75–76);
  - **unattested**: split into "probably absent" (witnesses run continuously, rule 3) and "undetermined", each split held fixed *before* running.

**Features**, fixed before running:
1. Bilby's published list (§2.4), re-implemented from the definitions in his index, not copied as results.
2. Function-word frequencies (the 100 most frequent lemmas).
3. Part-of-speech and morphology n-grams.
4. A held-out set of features *not* used by Bilby, to guard against features chosen after seeing the data.

**Tests**
- Per feature: binomial and Poisson rate comparison of present against absent material, with Holm correction across each family (as in §4 rule 7 of the companion structured-data-analysis CLAUDE.md).
- Effect sizes: rate ratios with 95% confidence intervals.
- **The abridgement null, simulated.** Delete random sets of Luke pericopes (respecting pericope boundaries and the sayings/narrative mix) until each set matches the length of the absent material. Count how often the observed concentration of features is reached. This turns "an abridger would have to be miraculous" into a measured probability.
- **The genre control.** Run sayings and narrative separately. Lukan narrative idiom (καὶ ἐγένετο, εἶπεν πρός) is genre-sensitive, so a narrative-heavy absent stratum could create a spurious signal.
- **The Markan control.** In passages where Luke follows Mark, compare canonical Luke's departures from Mark where Marcion's text is present against where it is absent.
- Unsupervised check: Burrows' Delta or a bootstrap consensus tree over present, absent and Markan segments.

**Predictions, pre-registered**

| Hypothesis | What it predicts | What would count against it |
|---|---|---|
| Expansion (Schwegler or Semler on Luke's side) | Canonical-Luke-only features are concentrated in the absent material, beyond the random-deletion null | No difference between present and absent material once genre is controlled |
| Abridgement | Features are distributed proportionally, because cuts follow theology, not style | The observed concentration falls outside 95% of random deletions |

**Outputs**
- `scripts/stylometry/` (code)
- `analysis/stylometry.ipynb` (executed top to bottom)
- `docs/stylometry_report.md`: methods, results, labelled **supported / not observed / underdetermined**

**Licences**
- Bilby's datasets are CC-BY-NC-ND: download them at runtime; never commit the dataset or a modified copy.
- SBLGNT/MorphGNT are CC-BY-SA: attribute them.
- Bilby's book text must not be committed (it carries a no-LLM-training clause).

### Phase C — Verse-by-verse evidence apparatus for all 22 chapters

- Build `data/apparatus/` with one record per Luke verse. Fields:
  - Marcion status (§3 rule 3);
  - the witnesses with references;
  - Roth's classification;
  - BeDuhn, Klinghardt and Bilby positions;
  - Western and WNI status;
  - the decision and its reason.
- Re-derive the inclusion of every verse in `proto_luke.json` from this apparatus. Do Luke 24 first (§5 is the draft), then chapters 22–23, then 3–4, then the rest.
- Every JSON note gets a traceable citation. Remove NotebookLM-only reasoning.

### Phase D — Rewrite chapter 22 (Luke 24) — owner decisions first (§10)

- Apply the "Fix" column of §5.
- Rewrite the preamble, notes and `additional_explanation` on the three-layer model in §5.1.
- Regenerate the PDF.

### Phase E — Front matter

- Rewrite the JSON `description` and the README "Methodology", "Excised Material" and "Key Scholarly Sources" from traced sources only:
  - the Bilby stylometry;
  - the harmonization test;
  - the absence of a doctrinal pattern in the omissions;
  - the 4:23 seam;
  - patristic attestation;
  - the Western witnesses, kept distinct.
- Implement research questions Q4, Q5 and Q6.
- Update CLAUDE.md (schema; method; source list).

### Phase F — Propagation to literary-compilation (separate PR in that repository)

- Correct the documents that repeat the inflated claims. Locations as found on 2026-10-12, paths under `data/`:
  - `04_Early_Christian_History/The Jamesian Protograph_ A Forensic Reconstruction of Proto-Luke.md` (§2.2, "computer-aided analysis", footnote 1 → dead Drive guide)
  - `04_Early_Christian_History/The Jamesian Protograph_ A Forensic Reconstruction of the Proto-Lukan Nexus, the Q Source, and the Politics of Resurrection.md` (line ~55, same claim)
  - `03_Biblical_Scholarship/No Original Exists_ … .md` (§4.2 "decisive evidence is editorial fatigue"; §5 table "Luke 24:39–43 excised… Marcionite absent"; line ~523)
  - `02_Swedenborgian_Theology/Asking the Skin to Be the Heart_ … .md` (lines ~116, 238, 506, 544)
  - `00_Master_Theses/The Carriers of Living Water_ … .md` (line ~160; Luke 24 section; tables ~474 and ~1021)
  - `05_The_Self/Dancing with Fire_ … .md` (line ~149)
  - `04_Early_Christian_History/They Killed His Brother and Took His Name_ … .md` (lines ~286, 300)
  - `04_Early_Christian_History/The Mistress Who Became a Sister_ … .md` (lines ~122, 637)
  - `04_Early_Christian_History/The Forensic Stratigraphy of the Resurrection_ … .md` (Luke 24 tomb narrative; premise "where the Western text and Marcion agree")
  - `00_Framework/A Prophet Mighty in Deed and Word_ … .md` (title phrase from 24:19b, unattested for Marcion's text; line ~110)
  - `04_Early_Christian_History/The Lukan Dissonance_ … .md` (line ~184)
  - `03_Biblical_Scholarship/What the Apparatus Cannot See_ … .md` §3.4 (the list of eight WNIs: check it against WH)
  - `02_Swedenborgian_Theology/Anatomy of Ascension…` (reads the fish correspondentially; check consistency once §10 is decided)
- Revise strain #9 in literary-compilation PR #33 (§7.4) before it is merged.

---

## 9. What the literary-compilation library currently claims on these points

So that a later session doesn't have to search for it again:
- "Computer-aided analysis of 'editorial fatigue' suggests the opposite direction of dependence" (both *Jamesian Protograph* documents). Untraced: the footnote leads to a deleted Drive guide.
- "The decisive evidence is editorial fatigue… canonical Luke exhibits editorial fatigue when diverging from Marcion's text" (*No Original Exists* §4.2). No study is named.
- "Luke 24:39–43 excised: Marcionite absent; anti-Docetic motivation; Western Non-Interpolation cluster; High (4 methods converge)" (*No Original Exists* §5 table). Contradicted by §5: 24:39 core and 24:41–43 are attested present; 24:39 and 24:41–43 are not WNIs (only 24:40 is).
- "Critical scholarship (BeDuhn, Vinzent) identifies the entire 'flesh and bones' apology as a later orthodox insertion" (*No Original Exists*). BeDuhn says the opposite: Marcion's text's resurrection "has a physical character (24.39, 41–42)" (p. 72).
- "The Marcionite evidence… consistently supports the shorter readings" (*No Original Exists*). Not consistent: 24:6 (ἠγέρθη) and 24:9 ("from the tomb") show non-Western readings attested for Marcion's text (Smith 49).

---

## 10. Decisions the owner needs to make

1. **Model:** Schwegler (Luke expanded Marcion's text) or Semler (common original)? Or leave it open and mark the passages where the choice matters?
2. **The status of "unattested, probably absent":** do such verses go in the main text in brackets, or only in the apparatus?
3. **24:19b ("a prophet mighty in deed and word")** is unattested. Keep it in brackets, or move it to the apparatus? It matters for the framework document of that name. *Resolved 2026-10-13 by the method, not by preference:* 19b is `U?` (Tertullian passes over it while quoting 24:21 for the same argument it would have served; Epiphanius is silent), and only an attested omission removes words from an attested verse (METHOD §5.3). Printed, with the class and reasoning in the apparatus (24:19).
4. **24:41–43 (the meal):** it is attested for Proto-Luke. How should the reconstruction's commentary read it? Options:
   - the Marcionite community's own reading (Eznik: a basis for their teaching on eating fish);
   - a correspondential reading (cf. *Anatomy of Ascension*);
   - no interpretive note beyond the evidence.
5. **The ending:** stop at 24:47; or add 24:50–51a ("parted from them") as a probable ending (BeDuhn's excursus); or mark the ending as unknown?
6. **Phase B scope:** replication on Roth's data only, or the full sensitivity set (Bilby, Harnack, Klinghardt, Nicolotti)?

---

## 11. Session log

- **2026-10-12** (Claude Code; owner's request after the literary-compilation nightly audit).
  - Read: Tertullian *Marc.* 4.43; Roth 2015 (Luke 24 entries); NA28 p. 290; Westcott–Hort vol. 2 (WNI sections); BeDuhn 2013 (pp. 65–98, 126–127, 193–199, notes); Smith 2017 (complete); Bilby v4.03 (sections cited in §2.4); Litwa 2024 and 2025 (blog).
  - Found that the "computer-aided editorial fatigue" footnote leads to a deleted Drive guide; identified Bilby's computational stylometry as the existing research.
  - Owner's corrections recorded in §1.2 and §1.6.
  - No data changed; this document and the PR are the only output.
