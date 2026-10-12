# Audit Log

One entry per batch. Method: `docs/audit/METHOD.md`. Per-verse evidence: `data/apparatus/luke_NN.json`.

## Batch 1: Luke 3:1–6:49 → chapters 1–3 (2026-10-12)

### What was checked

Every verse of Luke 3:1–6:49 was checked against four things:
- the Tertullian sections (Evans' Latin);
- the Epiphanius scholia (Holl page images);
- Roth's tables and graded reconstruction;
- the NA27 page images, both text and apparatus.

The records are in `data/apparatus/luke_03.json` to `luke_06.json`. All 170 verses are covered, with ranges used for whole absent passages. The Greek of every printed verse was compared with the NA27 page (pp. 164–175), not only with SBLGNT.

### Structure

| Chapter | Contents | Verses printed | Of which unattested (grey) |
|---|---|---|---|
| 1 | 3:1; 4:31–37; 4:16, 23–24, 28–30; 4:40–44 | 19 | 5 |
| 2 | 5:1–38; 6:1–11 | 49 | 19 |
| 3 | 6:12–49 | 38 | 8 |

- **Chapter 1 now holds all of Luke 4.** Before, the chapter boundary fell inside the Capernaum episode, splitting 4:31–32 from 4:33–35.
- **Chapter 2 is new from 5:15 to 6:11.** That stretch was missing from the previous text even though Tertullian attests it (*Marc.* 4.10–4.12).
- **Chapters 4–22 keep their numbers.** They are unchanged in this batch.

### Corrections to the previous text

**Verses restored**
- **Attested but missing from the previous text:** 4:29–30; 4:42; 5:9; 5:17–6:9 (the paralytic, Levi, fasting, the sabbath disputes); 6:30, 6:34, 6:36–45.
- **Unattested verses inside attested passages:** these were missing or merged into neighbouring verses. They are now printed and flagged.

**Verses removed**
- **4:22a.** It is unattested, and Tertullian's silence counts against it (4.7.7).

**Wording**
- **Ναζαρηνέ at 4:34 restored.** The previous text had deleted it. Only one witness lacks it, and Roth rates the omission only "may not have been present".
- **6:15 printed and flagged.** The previous text replaced it with ellipses.
- **6:27–28 back to NA27.** The previous text printed Tertullian's compressed "bless those who hate you".
- **Opening δέ (3:1) and Καί (4:31) dropped.** This is the editorial junction.

**Notes withdrawn as contradicted by the witnesses**
- **6:23c "a later addition".** Both Epiphanius (sch. 6) and Tertullian (4.15.1) quote it.
- **Ἰσκαριώθ "a Marcionite/Western reading".** It is the NA27 text.
- **κατῆλθεν "a vertical descent".** That is Marcion's reception of the text (Tertullian 4.7.1), not its wording.
- **4:22 "excision of biological paternity".** This stated a motive that no witness gives.
- **Statements about direction of change.** For example, "editorial fatigue proves". These are reworded as attested order.

**Removed throughout chapters 1–3**
- NotebookLM numbering.
- The words "forensic" and "clinical".
- `additional_explanation` blocks, which the PDF did not render.

### Marcionite readings printed (each attested in a primary text, at least "very likely")

| Verse | Reading | Witnesses | Agreement |
|---|---|---|---|
| 5:14 | ἵνα ᾖ μαρτύριον τοῦτο ὑμῖν | Epiph. sch. 1 (Greek); Tert. 4.9.10 | D it (with εἰς) |
| 5:24 | ἔγειρε καὶ ἆρον τὸν κράβαττόν σου καὶ πορεύου | Tert. 4.10.1 (retroversion; see below) | ℵ D 1424; κράβαττον D c r1 |
| 6:5 | ὁ υἱὸς τοῦ ἀνθρώπου καὶ τοῦ σαββάτου | Epiph. sch. 3 (Greek) | A D L Θ Ψ 𝔐 |
| 6:19 | ἐζήτει | Epiph. sch. 5 (Greek) | Byzantine |
| 6:20 | αὐτῶν (for ὑμετέρα) | Tert. 4.14.1, 13 | W ff2 sys sa |
| 6:36 | without [καί] | Tert. 4.17.8 | ℵ B L W |
| 6:37 | ἵνα μή (twice) | Tert. 4.17.9 | D W it sys |
| 6:38 | τῷ γὰρ αὐτῷ μέτρῳ ᾧ | Tert. 4.17.9 | 𝔓45vid A C 𝔐 |

### Base-text corrections

The previous text and the worksheets took their Greek from SBLGNT. At these places NA27 differs, and the NA27 wording is now printed (checked on the page images):
- 5:12 ἰδὼν δέ
- 5:13 λέγων
- 5:18 [αὐτόν]
- 5:34 ὁ Ἰησοῦς
- 5:36–37 μή γε
- 6:3 ὅτε and [ὄντες]
- 6:4 [ὡς]
- 6:15 ζηλωτήν
- 6:26 ὑμᾶς καλῶς
- 6:33 [γάρ]
- 6:34 [ἐστίν]
- 6:42 σου
- 6:45 without αὐτοῦ

### Decisions where the audit departs from Roth

| Verse | Roth | Audit | Reason |
|---|---|---|---|
| 3:2–20, 4:14–15 | unattested | attested absent | The 3:1 → 4:31 junction in Tertullian 4.7.1 leaves no room for them. |
| 4:33 | unattested | attested present | Tertullian 4.7.9 paraphrases it. |
| 5:14 εἰς | very likely | left open | Epiphanius' Greek lacks it. |
| 6:8 | present (Adamantius) | flagged unattested | Roth marks the attestation uncertain. |
| 6:31 γίνεσθαι παρὰ ἀνθρώπων | very likely | noted only | Tertullian alone attests it, and his Latin can render the NA27 Greek (METHOD §5.4). |
| 6:34 ἀπολαβεῖν | very likely | noted only | "recipere" renders λαβεῖν, and no Greek manuscript has ἀπολαβεῖν. |

### Source problems found

- **Tertullian, *Marc.* 4.10.1: a line is missing from the tertullian.org Latin.** The transcription of Evans breaks off after "Exsurge, et tolle". Evans' English ("Arise and take up thy bed") and the NA27 citation of McionT for κράβαττον show that the line contained the noun.
- **Tertullian's erasure charges compare Marcion's text with Matthew, not Luke.** The charges at 4.7.4, 4.9.15, 4.12.14 (Mt 5:17) and 4.17.6 (Mt 5:45) concern passages that are not in Luke. They are not used as reports of content.

### Library claims tested in this range

These go to Phase F (`docs/audit/library_corrections.md`).

**Contradicted or unsupported**
- **5:5 ἐπιστάτα as a Marcionite reading** (*No Original Exists*, App. B). 5:5 is unattested, so the claim is unsupported.
- **The "Orthodox Wrapper" including 4:16–30** (research_questions Q2). This is contradicted: the Nazareth visit is attested.

**Consistent with the witnesses**
- **The James parallels inside the sermon.** 6:24 / Jas 5:1, 6:37 / Jas 5:9 and 6:46 / Jas 1:22 (*Carriers* §3.4) are all attested.
- **Torah observance at 5:14.** Both witnesses attest it, with a Marcionite explanation recorded as reception.

### Not yet done

- **PDF regenerated.** The PDF script now renders flagged verses in grey with a legend. It also falls back to GNU FreeSerif for polytonic Greek when the Windows Palatino fonts are absent.
- **Preface not yet rewritten.** The preface (`description`) still describes the old method. It is rewritten at the end of the audit (task 5).

## Stylometric baseline (2026-10-12)

The stylometric baseline was run between batches 1 and 2: pre-registered, then run on seven editions. See `docs/stylometry/REPORT.md`.

**Consequences for the audit:**
- **No verse-level stylometric criterion.** A classifier separating absent from present verses performs at chance (AUC ≈ 0.5). Inclusion decisions therefore continue to rest on the witnesses alone. Batch 1 needed no change.
- **Outside Luke 1–2, no measurable stylistic difference.** Missing and kept material cannot be told apart, so no note cites style for or against a verse.

## Batch 2: Luke 7:1–9:62 → chapters 4–7 (2026-10-12)

### What was checked

- Every verse of Luke 7–9 (168 verses) has a record in `data/apparatus/luke_07.json` to `luke_09.json`.
- **Tertullian, *Marc.* 4.18–4.23:** read in full, as were the Epiphanius scholia 7–20.
- **Roth's classes:** recorded for every verse.
- **NA27 against SBLGNT, new screen.** This batch added a systematic check (`scripts/audit/na27_screen.py`):
  - every NA27 page of Luke was rendered and OCR'd with the Ancient Greek model;
  - the OCR text was aligned with SBLGNT, and every candidate difference listed;
  - each candidate in the batch range was checked on the page image.
- **The screen's recall.** It found all the NA27 differences already identified by eye in batch 1, so batch 1 needs no Greek change.

### Structure

| Chapter | Contents | Printed | Grey (unattested) |
|---|---|---|---|
| 4 | Luke 7 (without 7:29–35) | 43 | 19 |
| 5 | Luke 8:1–25 (without 8:9–15, 8:19) | 17 | 4 |
| 6 | Luke 8:26–9:17 | 48 | 25 |
| 7 | Luke 9:18–62 (without 9:49–50; 9:31b removed) | 43 | 13 |

The chapter boundaries of the previous text are kept.

### Not printed

| Verses | Class | Reason |
|---|---|---|
| 7:29–35 | U− | Tertullian's argument in 4.18 needed John's baptism as "the counsel of God". |
| 8:9–10 | U− | Tertullian cites Isaiah 6:9 himself (4.19.2) instead of Jesus' use of it. |
| 8:11–15 | U? | Its NA27 paragraph has no attested verse. |
| 8:19 | A− | Epiphanius, sch. 12. |
| 9:49–50 | U? | A separate paragraph with no attested verse. |
| 9:31b | A− | Roth, on Tertullian 4.22.16. Epiphanius' copy differs at 9:30. |

### Marcionite readings printed

| Verse | Reading | Witnesses | Agreement |
|---|---|---|---|
| 7:9 | Word order τοσαύτην πίστιν οὐδὲ ἐν τῷ Ἰσραήλ | Epiph. sch. 7 (Greek) | — |
| 8:21 | "Who is my mother and who are my brothers, except those who hear my words and do them?" | Tert. 4.19.6, 11 (retroversion, Roth's Greek) | form of Mark and Matthew |
| 8:45 | τίς μου ἥψατο; | Epiph. sch. 14; Tert. 4.20.8 | — |
| 9:16 | εὐλόγησεν ἐπ' αὐτούς | Epiph. sch. 15 | D it sy(s).c |
| 9:22 | μετὰ τρεῖς ἡμέρας | Epiph. sch. 16; Tert. 4.21.7 | D it; Mark 8:31 |
| 9:35 | ὁ ἀγαπητός | Epiph. sch. 18; Tert. 4.22 (four times) | A C* W f13 𝔐 it |
| 9:41 | without καὶ διεστραμμένη | Epiph. sch. 19; Tert. 4.23.1–2 (attested omission) | Mark 9:19 |
| 9:2 | without NA27's bracketed [τοὺς ἀσθενεῖς] | Adamantius 82,4–5 | — |

### NA27 corrections to SBLGNT (on the page images)

- 7:22 καὶ κωφοί
- 8:20 ἰδεῖν θέλοντές σε
- 9:18 λέγουσιν οἱ ὄχλοι
- 9:48 ὃς ἐάν
- 9:62 [πρὸς αὐτόν]

### Departures from Roth

| Verse | Roth | Audit | Basis |
|---|---|---|---|
| 9:52 | unattested | attested | Tertullian 4.23.8 names "that village of the Samaritans". |
| 7:29–35 | unattested | probably absent | — |
| 8:9–10 | unattested | probably absent | — |

### Weaker attestations, recorded as such

- **9:1 and 9:6.** These are read in the Dialogue of Adamantius by the *orthodox* speaker, as an argument the Marcionite is expected to accept. Roth counts them as attested.
- **9:18–19.** Adamantius 84, via Roth; the Greek OCR of that page could not be read.

### Notes withdrawn from the previous text

- **"Excision of 8:24a".** Epiphanius' quotation is compressed; 8:24 is attested.
- **"Excision of the distribution clause (9:16b)".** No witness supports it.
- **"Omission in 9:54" and "Excision in 9:55".** These rested on readings no witness supports.
- **"The Great Omission".** Mark 6:45–8:26 is missing from canonical Luke as well, so it does not distinguish the two texts (`docs/audit/library_context.md` §5). A note at 9:17 now says so.


## Batch 3: Luke 10:1–13:35 → chapters 8–11 (2026-10-12)

### What was checked

- Every verse of Luke 10–13 (190 verses) has a record in `data/apparatus/luke_10.json` to `luke_13.json`.
- **Tertullian, *Marc.* 4.24–4.30:** read in full, as were the Epiphanius scholia 22–41.
- **Roth's classes:** recorded for every verse, together with his discussion of each graded reading (chs. 4–6, 8).
- **Origen, fragment on Luke 11:3:** read in Rauer's edition (GCS 35, 1930, p. 254, fr. XLVI). It is the only Greek quotation of the Marcionite bread petition.
- **NA27 screen:** every candidate in Luke 10–13 was checked on the page images (pp. 190–207), apparatus included, wherever a reading was at issue.

### Structure

| Chapter | Contents | Printed | Grey (unattested) |
|---|---|---|---|
| 8 | Luke 10 (without 10:12–15, 10:18, 10:29–42) | 23 | 5 |
| 9 | Luke 11 (without 11:24–26, 11:30–32, 11:34–36, 11:49–51, 11:53–54) | 40 | 7 |
| 10 | Luke 12 (without 12:6–7, 12:33–34; 12:28a removed) | 55 | 11 |
| 11 | Luke 13:10–28 (without 13:22) | 18 | 8 |

The chapter boundaries of the previous text are kept: one chapter per chapter of Luke.

### Not printed

| Verses | Class | Reason |
|---|---|---|
| 10:12–15 | U− | Tertullian argues at length (4.24.7–8) that the dust saying implies judgement, and does not cite the verses that state it (Sodom, the woes). |
| 10:18 | U− | Tertullian brings in Ps 91:13 and Isa 27:1 for the fall of the serpent (4.24.10) instead. |
| 10:29–37 | U− | The Samaritan. Both witnesses end the lawyer's exchange at 10:28; the parable expounds the "head of the law" Tertullian was arguing for. |
| 10:38–42 | U? | Martha and Mary. A paragraph with no attested verse; the witnesses' silence is undetermined. |
| 11:24–26 | U? | A paragraph with no attested verse. |
| 11:30–32 | A− | Epiph. sch. 25. |
| 11:34–36 | U? | A paragraph with no attested verse. |
| 11:49–51 | A− | Epiph. sch. 28. |
| 11:53–54 | U? | A paragraph with no attested verse. |
| 12:6 | A− | Epiph. sch. 29. |
| 12:7 | U− | It depends on 12:6 ("many sparrows"); Tertullian argues the Creator's care and goes from 12:5 to 12:8. |
| 12:28a | A− | Epiph. sch. 31 ("God clothes the grass"). |
| 12:33–34 | U? | A paragraph with no attested verse. |
| 13:1–9 | A− | Epiph. sch. 38. |
| 13:22 | U? | A one-verse paragraph with no attested verse. |
| 13:29–35 | A− | Epiph. sch. 41, saying by saying. |

### Marcionite readings printed

| Verse | Reading | Witnesses | Agreement |
|---|---|---|---|
| 10:1 | "seventy", without NA27's bracketed [δύο] | Tert. 4.24.1 (Roth: very likely) | ℵ A C L W 𝔐 |
| 10:21 | εὐχαριστῶ σοι, κύριε τοῦ οὐρανοῦ (no πάτερ, no καὶ τῆς γῆς) | Epiph. sch. 22; Tert. 4.25.1 | 𝔓45 (no "and of the earth") |
| 10:21 | ὅτι ἅτινα ἦν κρυπτὰ σοφοῖς καὶ συνετοῖς ἀπεκάλυψας νηπίοις | Tert. 4.25.1, 6 (retroversion, Roth's Greek) | — |
| 10:22 | "who the Father is… who the son is" (Father first) | Tert. 4.25.10; Adamantius; Eznik | some MSS and fathers |
| 10:25 | ζωήν without αἰώνιον | Tert. 4.25.14, 18 (explicit) | — |
| 11:2 | a petition for the holy spirit in place of "hallowed be your name" (ἐλθέτω τὸ πνεῦμά σου τὸ ἅγιον) | Tert. 4.26.3–5 (content; the Greek wording is that of 700, 162, Gregory of Nyssa, shortened) | NA27: (McionT) |
| 11:3 | τὸν ἄρτον σου | Origen (Greek); Tert. 4.26.4 | NA27: McionOr |
| 11:29 | without εἰ μὴ τὸ σημεῖον Ἰωνᾶ | Epiph. sch. 25; Tert. 4.27.1 | — |
| 11:38 | ἤρξατο διακρινόμενος ἐν ἑαυτῷ λέγειν διὰ τί… (D's Greek) | Tert. 4.27.2 (retroversion) | D lat syc; NA27: (McionT) |
| 11:42 | τὴν κλῆσιν for τὴν κρίσιν | Epiph. sch. 26; Tert. 4.27.4, 6 | — |
| 12:5 | βαλεῖν εἰς γέενναν | Epiph. sch. 29; Tert. 4.28.3 | 𝔓45 (D) W; NA27: McionT,E |
| 12:8, 12:9 | "before God", without τῶν ἀγγέλων | Epiph. sch. 30; Tert. 4.28.4 | ℵ*; NA27: McionT,(E) |
| 12:27 | πῶς οὔτε νήθει οὔτε ὑφαίνει (D's Greek) | Tert. 4.29.1 (retroversion) | D sys.c Cl; NA27: (McionT) |
| 12:28 | without 12:28a | Epiph. sch. 31 (attested omission) | — |
| 12:31 | τὴν βασιλείαν τοῦ θεοῦ | Epiph. sch. 33; Tert. 4.29.5 | 𝔓45 A D1 W 𝔐; NA27: McionE |
| 12:32 | ὁ πατήρ without ὑμῶν | Epiph. sch. 34 (explicit) | — |
| 12:38 | ἐν τῇ ἑσπερινῇ φυλακῇ for "in the second or third watch" | Epiph. sch. 35 (explicit) | D and the Old Latin (with both) |
| 12:53 | διαμερισθήσεται (singular) | Tert. 4.29.14 (retroversion) | Byzantine text |
| 12:56 | "heaven and earth" | Tert. 4.29.15 | 𝔓45 𝔓75 ℵ2 D it |
| 12:58 | παραδώσει σε | Epiph. sch. 37 | 𝔓45 D |
| 13:28 | πάντας τοὺς δικαίους for the patriarchs and prophets; κρατουμένους for ἐκβαλλομένους | Epiph. sch. 40; Tert. 4.30.4–5 | — |

### NA27 corrections to SBLGNT (on the page images)

- 10:1 no καί before ἑτέρους
- 10:6 ἐὰν ἐκεῖ ᾖ; μή γε
- 10:21 [ἐν] τῷ πνεύματι; ναὶ ὁ πατήρ
- 11:14 [καὶ αὐτὸ ἦν]
- 11:20 [ἐγώ]
- 11:33 τὸ φῶς (SBLGNT τὸ φέγγος)
- 12:54 [τὴν] νεφέλην
- 12:56 τὸν καιρὸν δὲ τοῦτον
- 13:21 [ἐν]έκρυψεν
- 13:27 [ὑμᾶς]

METHOD §5.7 now states the rule for NA27's bracketed words, which batch 2 already applied.

### Departures from Roth

| Verse | Roth | Audit | Basis |
|---|---|---|---|
| 10:12–15, 10:18, 10:29–37, 12:7 | unattested | probably absent | Tertullian's continuous argument at these points (see above). |
| 12:24 | "God feeds them" probably not present | printed | No witness states it was lacking. Roth's inference rests on the analogy with 12:28a. |

### Weaker attestations, recorded as such

- **Not adopted (one witness, or Roth "probable"/"possible").** The readings are recorded in the apparatus:
  - 10:24, Tertullian's short form, which lacks "and kings" (NA27: McionT with D it);
  - 10:27, without "and with all your mind" (NA27: McionT with D it);
  - 11:4, μὴ ἄφες ἡμᾶς εἰσενεχθῆναι, Tertullian's own way of glossing the petition;
  - 11:48, D's "you testify that you do not approve", which is in Tertullian's argument, not his quotation;
  - 12:10, "whoever speaks against the holy spirit";
  - 12:51, βαλεῖν and ἀλλά (NA27 cites McionT; Roth: possible).
- **11:2.** The petition for the spirit is attested in content only. Its Greek wording is not attested for this text (see `docs/research_questions.md` Q7).

### Corrections to the previous text

- **13:29 was printed.** Epiphanius states it was absent. It is removed.
- **10:5–8 and 10:23–24 were omitted as "excisions".** Tertullian attests 10:5, 7–11 and 10:23–24. They are printed.
- **"Excision of 11:14–36".** 11:14–22 are attested by Tertullian (4.26.10–12). Only 11:24–26 and 11:34–36 are not printed, and only as paragraphs with no attested verse.
- **11:2 replaced "your kingdom come".** Tertullian attests the kingdom petition and places the spirit before it. The previous text also printed "do not let us be led" as Marcionite; it is printed in the NA27 form, with the reason given.
- **12:4 "kill you only" (no "body") and 12:10 without "blaspheme".** Epiphanius' Greek has "the body"; the 12:10 form is rated probable only. NA27 is printed.
- **Notes withdrawn.** Notes that gave no witness for their claims were withdrawn, among them "Upon you… the Ebionim", "dry forensic correction", and "Little flock = the Ebionim". New notes separate the attested text, its reception and interpretation.

## Batch 4: Luke 14:1–17:37 → chapters 12–15 (2026-10-12)

### What was checked

- Every verse of Luke 14–17 (152 verses; NA27 has no 17:36) has a record in `data/apparatus/luke_14.json` to `luke_17.json`.
- The record for 4:27 in `luke_04.json` was updated, since the verse is printed here.
- **Tertullian, *Marc.* 4.31–4.35:** read in full, as were the Epiphanius scholia 42–49.
- **Roth:** classes, and his discussion of every graded reading used.
- **NA27:** checked on the page images (pp. 208–218), apparatus included.

### Structure

| Chapter | Contents | Printed | Grey (unattested) |
|---|---|---|---|
| 12 | Luke 14:12–24 | 13 | 2 |
| 13 | Luke 15:1–10 | 10 | 2 |
| 14 | Luke 16 | 31 | 4 |
| 15 | Luke 17 (without 17:5–10, 17:13, 17:12b), with 4:27 between 17:12 and 17:14 | 30 | 10 |

### Not printed

| Verses | Class | Reason |
|---|---|---|
| 14:1–11 | U? | Two paragraphs with no attested verse. |
| 14:25–35 | U? | Three paragraphs with no attested verse. |
| 15:11–32 | A− | Epiph. sch. 42 ("the whole parable of the two sons"). |
| 17:5–10 | U? (17:10b A−) | Two paragraphs with no attested present verse; Epiph. sch. 47 for 17:10b. |
| 17:12b–13 | A− | Epiph. sch. 48 ("he cut out much"); Roth. |

**Two one-verse paragraphs are printed in grey: 14:15 and 15:1–2.** The attested parables that follow are answers to them ("But he said to him", "So he told them this parable"). They count as one pericope with what follows (METHOD §4.3).

### Marcionite readings printed

| Verse | Reading | Witnesses | Agreement |
|---|---|---|---|
| 16:12 | τὸ ἐμόν for τὸ ὑμέτερον | Tert. 4.33.4 (twice) | e i l; NA27: McionT |
| 16:17 | τῶν λόγων μου for τοῦ νόμου | Tert. 4.33.9 (twice) | NA27: McionT |
| 16:23 | ἐν τῷ κόλπῳ (singular) | Tert. 4.34.10–12; Adamantius | D and the Old Latin |
| 4:27 (at 17:12–14) | position; ἐν ἡμέραις for ἐπί; Νεεμάν | Epiph. sch. 48; Tert. 4.35.6 | — |
| 17:12 | without οἳ ἔστησαν πόρρωθεν (17:13 also absent) | Epiph. sch. 48 | — |
| 17:21 | ἰδοὺ ὧδε ἤ· ἰδοὺ ἐκεῖ | Tert. 4.35.12 | A D W Θ Ψ 𝔐 |

### NA27 corrections to SBLGNT (on the page images)

- 16:12 τίς ὑμῖν δώσει
- 17:12 [αὐτῷ]
- 17:23 [ἤ]

### Departures from Roth

| Verse | Roth | Audit | Basis |
|---|---|---|---|
| 16:17 | "of my words" probable | printed | Tertullian's thesis in 4.33.7–9 is that Christ fulfilled the law. Canonical "one stroke of the law" would have proved it directly, and he passes it over for Christ's "words" (twice) and has to argue from Isa 40:8 instead. Roth's alternative, that 21:33 influenced Tertullian, does not explain why he would give up the wording that served him best. |
| 14:15, 15:1–2 | unattested | printed in grey | They open the attested pericopes. |

### Weaker attestations, recorded as such

- **16:19–31.** Several verses (16:21, 24, 27–28, 30) rest on the Dialogue of Adamantius alone. They are printed as part of the parable, which Tertullian and Epiphanius attest. Their wording is NA27.
- **Not adopted (one witness, or Roth "probable"/"possible"):**
  - 14:14, Tertullian without "of the righteous";
  - 14:16, without "great";
  - 15:10, without "the angels of";
  - 16:16, ἕως;
  - 16:25, ὅδε (NA27: McionA,E);
  - 16:31, the Dialogue's ἀπέλθῃ;
  - 17:2, "if he had not been born".

### Corrections to the previous text

- **Printed though unattested:** 14:26, 14:33. They are removed. 17:10 is attested in part and absent in part; it is removed.
- **Printed though attested absent:** 17:13. It is removed.
- **Omitted though attested.** These are printed:
  - 16:1–8, the steward. The previous version called it "conflicting evidence"; Tertullian 4.33.1 attests it.
  - 17:11–12, 17:15–18.
  - Most of 16:19–31.
- **Claims the witnesses do not support.** The NA27 wording is printed:
  - 14:14, without "of the righteous";
  - 14:16, without "great";
  - 15:7–10, without "the angels".

## Batch 5: Luke 18:1–21:38 → chapters 16–19 (2026-10-12)

### What was checked

- Every verse of Luke 18–21 (176 verses) has a record in `data/apparatus/luke_18.json` to `luke_21.json`.
- **Tertullian, *Marc.* 4.36–4.39:** read in full, as were the Epiphanius scholia 50–59 and the Dialogue of Adamantius at 32,26–27, 92,26–32 and 200,24–30.
- **Roth:** classes, and his chapter 9 grade (bold, bold italic, regular, italic) for every reading used or rejected.
- **NA27:** checked on the page images (pp. 218–232), apparatus included, and the paragraph breaks used for METHOD §4.3.

### Structure

| Chapter | Contents | Printed | Grey (unattested) |
|---|---|---|---|
| 16 | Luke 18:1–23, 18:35–43 | 32 | 6 |
| 17 | Luke 19:1–26 | 26 | 16 |
| 18 | Luke 20:1–8, 20:19 (without its last clause), 20:20–36, 20:39–44 | 32 | 11 |
| 19 | Luke 21:7–17, 21:19–20, 21:23–38 | 29 | 3 |

### Not printed

| Verses | Class | Reason |
|---|---|---|
| 18:24–30 | U? | A paragraph with no attested verse. The Dialogue's reference is not to Marcion's text. |
| 18:31–33 | A− | Epiph. sch. 52 (the third passion prediction, "all that is written by the prophets"). |
| 18:34 | U− | Refers to 18:31–33 and closes their paragraph. |
| 19:27 | U− | The slaughter of the enemies; Tertullian argues the master's severity from 19:26 and does not cite it. |
| 19:28 | U? | A one-verse paragraph introducing the absent entry. |
| 19:29–46 | A− | Epiph. sch. 53 (colt and Bethphage, the city, the temple and "house of prayer"). |
| 19:47–48 | U? | A paragraph with no attested verse. |
| 20:9–17 | A− | Epiph. sch. 55 (the vineyard; "the stone that the builders rejected"). |
| 20:18 | U− | Refers to the stone of 20:17. |
| 20:19c | probably absent | "For they perceived that he had told this parable against them": refers to the absent parable. Epiphanius quotes the rest of the verse (sch. 54). |
| 20:37–38 | A− (20:38b unattested) | Epiph. sch. 56–57 (Moses at the bush; "God of the living"). 20:38b completes the sentence. |
| 20:45–47 | U? | A paragraph with no attested verse. |
| 21:1–4, 21:5–6 | U? | Two paragraphs with no attested verse. Tertullian's survey runs "from the disciples' question" (21:7). |
| 21:18 | A− | Epiph. sch. 58 ("not a hair of your head"); NA27: McionE. |
| 21:21–22 | A− | Epiph. sch. 59 (the flight from Judea, "that all that is written may be fulfilled"). |

### Marcionite readings printed

| Verse | Reading | Witnesses | Agreement |
|---|---|---|---|
| 18:19 | εἷς ὁ θεὸς ὁ πατήρ | Epiph. sch. 50; Adamantius; Origen, *Princ.* 2.5.1, 4; Hippolytus | — |
| 18:20 | order kill–adultery; μηδὲ ψευδομαρτυρήσῃς | Tert. 4.36.4; Adamantius | Old Latin; Matt 19:18 |
| 18:22 | Ἕν σοι λείπει (no ἔτι); δός; ἐν οὐρανῷ | Tert. 4.36.4–7; Adamantius | δός ℵ A D L; ἐν οὐρανῷ W Θ Ψ f1.13 𝔐 |
| 20:35 | οὓς δὲ κατηξίωσεν ὁ θεός | Tert. 4.38.5, 7–8 (three times) | — |
| 21:27 | ἐρχόμενον ἀπὸ τῶν οὐρανῶν μετὰ δυνάμεως πολλῆς (retroversion) | Tert. 4.39.10–11 | without "glory": cf. D e (δυνάμει πολλῇ κ. δόξῃ) |

### NA27 corrections to SBLGNT (on the page images)

- 18:13 ἔτυπτεν
- 18:21 without μου
- 20:24 οἱ δὲ εἶπαν
- 20:26 αὐτοῦ ῥήματος
- 20:44 κύριον αὐτόν
- 21:11 φόβητρά τε καὶ ἀπ’ οὐρανοῦ σημεῖα μεγάλα

### Departures from Roth

| Verse | Roth | Audit | Basis |
|---|---|---|---|
| 20:35 | "whom God has deemed worthy" probable | printed | Tertullian quotes the clause three times with God as subject (4.38.5, 7–8). He reports the Marcionite punctuation "the God of that age" and argues against the punctuation, not the wording. The Marcionite reading he reports requires ὁ θεός in the text, as Roth himself says. |
| 18:34, 19:27, 20:18 | unattested | U− | Each depends on a passage attested absent (18:31–33, 20:9–17) or, at 19:27, would have been Tertullian's strongest evidence for his argument at that point. |
| 20:19c | present (verse) | clause not printed | The clause refers to the absent parable and is not in Epiphanius' quotation. |

### Weaker attestations, recorded as such

- **18:16, 18:36, 18:40, 18:41** rest on the Dialogue of Adamantius alone; 18:16 is an antithesis by the Marcionite speaker (Roth: possible). They are printed with NA27 wording.
- **Not adopted (Roth "probable"/"possible", or one witness):**
  - 18:19, Epiphanius' "do not call me good";
  - 18:20, Epiphanius' "I know the commandments";
  - 18:37, the Dialogue without "of Nazareth";
  - 19:10, without "to seek";
  - 19:26, ὃ δοκεῖ ἔχειν (NA27: McionT);
  - 20:35, Roth's τῆς κληρονομίας for τυχεῖν;
  - 20:36, μέλλουσιν (NA27: McionT);
  - 21:8, "I am the Christ" (Matthew's wording);
  - 21:19, σώσετε ἑαυτούς (NA27: McionT);
  - 21:28, without ὑμῶν (Roth: likely not present; D d). Tertullian's *capita* can render NA27 (METHOD §5.4);
  - 21:30, "when they bear fruit";
  - 21:32, "heaven and earth will not pass away";
  - 21:33, "my word abides for ever" (Isa 40:8).

### Corrections to the previous text

- **Printed though unattested:** 18:24–25, 20:45–46 and 21:1–4. They are removed.
- **Printed though attested absent:** 19:37–38 and 19:43–46. They are removed.
- **Wording the witnesses contradict.** At 21:20 the previous text printed "the abomination of desolation standing where it ought not" (Mark 13:14), although its own note cited Tertullian's "surrounded by armies" (4.39.9). NA27 is printed.
- **Unattested readings removed:** 19:26 ὃ δοκεῖ ἔχειν, 21:8 ὁ Χριστός, 21:19 σώσετε ἑαυτούς and 21:30 καρπόν, all possible only.
- **Verses cut short without a witness:** 18:5, 18:8, 18:11 and 18:43. They are printed in full.
- **Omitted though attested.** These are printed:
  - 18:7, 18:12, 18:16, 18:36, 18:39–41;
  - 20:7, 20:28–31, 20:33, 20:39;
  - 21:7, 21:14, 21:16, 21:32, 21:35.
- **Unattested verses inside attested pericopes** (METHOD §4.3) are now printed in grey. Most of the parable of the money entrusted (19:12–25) and the question about Caesar (20:20–23, 26) are among them.
- **Library:** `library_corrections.md` items 10 (21:20–22) and 11 (18:19, 18:22).

## Batch 6: Luke 22:1–24:53 → chapters 20–22 (2026-10-12)

### What was checked

- Every verse of Luke 22–24 (179 verses; NA27 has no 23:17) has a record in `data/apparatus/luke_22.json` to `luke_24.json`.
- **Tertullian, *Marc.* 4.40–4.43:** read in full, with 5.6.7 (Satan and Judas). **Epiphanius, scholia 60–78:** read with their elenchi, and checked on Holl's page images (pp. 116–117).
- **Adamantius:** read at 108,27 and 198,5–21. Both are spoken by Adamantius, the orthodox speaker, and are not counted as evidence for Marcion's text.
- **Roth:** classes, chapter 9 grades and his discussion of every reading used or rejected.
- **NA27:** checked on the page images (pp. 232–245), apparatus included. This covers the double brackets at 22:43–44 and 23:34a and the paragraph breaks.
- **Not checked here:** Eznik (De Deo 358, 407) and Ephrem (Comm. Diat. 21.3), known only from Roth's quotations. Verses that rest on them alone are printed as unattested (24:42–43).

### Structure

| Chapter | Contents | Printed | Grey (unattested) |
|---|---|---|---|
| 20 | Luke 22:1–15, 17–23, 31–34, 39–42, 45–48, 63–71 (22:3 without "Satan entered into") | 43 | 21 |
| 21 | Luke 23:1–12, 18–25, 32–33, 44–46, 50–56 | 32 | 10 |
| 22 | Luke 24:1–11, 13–23, 25–26, 28–31, 36–43, 47 | 37 | 14 |

### Not printed

| Verses | Class | Reason |
|---|---|---|
| 22:3a | A− | "Satan entered into": Tertullian 5.6.7, "in my text… but according to Marcion". |
| 22:16 | A− | Epiph. sch. 63. |
| 22:24–30 | U? | A paragraph with no attested verse; Epiphanius' elenchus 63 suggests he did not find 22:30. |
| 22:35–38 | A− | Epiph. sch. 64 (the purse and the swords; "counted among the lawless"). |
| 22:43–44 | U? | NA27 double brackets; not cited. |
| 22:49 | U− | Depends on the absent swords (22:38) and the absent blow (22:50). |
| 22:50–51 | A− | Epiph. sch. 67 and elenchus (the ear and its healing). |
| 22:52–53, 22:54–62 | U? | Paragraphs with no attested verse (including Peter's denial). |
| 23:13–16, 23:26, 23:27–31 | U? | Paragraphs with no attested verse. |
| 23:34 | A− (34b); 34a U? | 34b, the dividing of the garments: Tertullian 4.42.4, "Marcion abstulit". Epiphanius' sch. 71 mentions it, but in a summary in Matthew's wording. 34a ("Father, forgive them"): NA27 double brackets; Ephrem only. |
| 23:35–38, 23:39–42 | U? | Paragraphs with no attested verse. |
| 23:43 | A− | Epiph. sch. 72 ("Today you will be with me in paradise"). |
| 23:47–48, 23:49 | U? | Paragraphs with no attested verse. |
| 24:12, 24:24 | U− | Peter at the tomb, and the report of it. Both witnesses follow the chapter closely, and the linen cloths would have served their argument. 24:12 is also a Western non-interpolation. |
| 24:27, 24:32, 24:44–46 | U− | Moses, the prophets and the psalms; the opening of the scriptures. These are Tertullian's thesis, with which he ends book 4, and Epiphanius' theme in sch. 77; neither cites them. |
| 24:33–35 | U? | A paragraph with no attested verse (including the appearance to Simon). |
| 24:47b, 24:48–53 | U? | Nothing after 24:47 is cited (METHOD §10). "Beginning from Jerusalem" is punctuated with 24:48 in NA27. |

### Marcionite readings printed

| Verse | Reading | Witnesses | Agreement |
|---|---|---|---|
| 22:3 | without "Satan entered into" (rest of the verse put in the nominative, editorially) | Tert. 5.6.7 | — |
| 22:4 | τὸ πῶς αὐτὸν παραδῷ αὐτοῖς | Epiph. sch. 60 (both listings) | many manuscripts (Roth) |
| 23:2 | + "and destroying the law and the prophets"; + "and turning away the women and the children" | Epiph. sch. 69–70 | NA27: McionE (both); Old Latin e b c ff2 gat i (first), c e at 23:5 (second) |
| 24:6 | ἠγέρθη without "he is not here, but"; ὅσα for ὡς | Epiph. sch. 76; Tert. 4.43.5 | NA27: ἠγ. McionE; ὅσα D c sys.c McionT,E |
| 24:21 | ἐνομίζομεν (retroversion of *putabamus*) | Tert. 4.43.3–5 | Arabic and Persian Diatessaron, Ambrosiaster (Roth, citing IGNTP) |
| 24:25 | οἷς ἐλάλησεν πρὸς ὑμᾶς for "that the prophets spoke" (retroversion) | Tert. 4.43.4; Epiph. sch. 77 (ἐλάλησα ὑμῖν) | NA27: ἐλάλησεν πρὸς ὑμᾶς McionT,A |
| 24:39 | without "handle me and see" and "flesh and" | Tert. 4.43.6–7; Epiph. sch. 78 | NA27: McionT,E (flesh) |

### NA27 corrections to SBLGNT (on the page images)

- 22:7 [ἐν]; 22:18 [ὅτι]; 22:19–20 printed without SBLGNT's brackets
- 23:2 ἑαυτόν; 23:12 αὐτούς; 23:20 αὐτοῖς; 23:50 [καί]; 23:56 full stop
- 24:3 τοῦ κυρίου Ἰησοῦ; 24:36 καὶ λέγει αὐτοῖς· Εἰρήνη ὑμῖν; 24:40 without brackets; 24:47 εἰς ἄφεσιν

### Departures from Roth

| Verse | Roth | Audit | Basis |
|---|---|---|---|
| 24:6 | "he is not here" unattested | absent | Epiphanius' citation habit. His own citations read "ἀνέστη, οὐκ ἔστιν ὧδε" (elenchus 76; Pan. 56.2.8). In the scholion he writes Luke's ἠγέρθη alone, a verb he does not otherwise use for it, in an unbroken quotation from 24:5. NA27 also cites McionE for ἠγ. alone. |
| 24:21 | ἐνομίζομεν possible | printed | *Putabamus* cannot render "hoped", and Tertullian builds 4.43.4–5 on what the disciples "thought" (five times). |
| 24:25 | final element uncertain | ἐλάλησεν πρὸς ὑμᾶς | Both witnesses lack "the prophets", so the NA27 wording is attested absent and a reading has to be printed. Tertullian's third person is the earliest. Epiphanius' own elenchus shows that the first person makes the recognition at the breaking of bread incoherent. |
| 24:39 | omissions "may not have been present" | absent | "Flesh": both witnesses lack it, and Epiphanius' own citations of the verse have it. "Handle me": Tertullian quotes continuously while arguing for the reality of the body, and speaks only of hands and feet offered for inspection. |
| 22:49; 24:12, 24, 27, 32, 44–46 | unattested | U− | As in "Not printed". |
| 22:17; 23:46–53 (Adamantius) | possibly attested | not counted | The Dialogue's words are the orthodox speaker's. |

### Readings proposed in the working document's §5 that the evidence did not support

- **24:37 φάντασμα.** *Phantasma* is Tertullian's standing word for the Marcionite Christ (4.40.3; 4.42.7–8; 4.43.8), so his use of it does not show the wording. Roth: possible only; NA27 cites D alone.
- **24:4 λαμπρᾷ.** It occurs only in Epiphanius' summary introduction to sch. 76 (Roth).
- **24:7 without "into the hands of sinful men", and 24:3 without "of the Lord Jesus".** The witnesses are silent, and the words would not have served their arguments. Silence is not attested absence; NA27 is printed.
- **24:9 "to the disciples".** Tertullian does not name the recipients.
- **24:36 "Peace to you" and 24:40.** Western non-interpolations; NA27 prints them. A Western omission does not remove words from this text (METHOD §1, Western witnesses). They are printed in grey.

### Weaker attestations, recorded as such

- **24:42–43 (the fish).** Roth classes them present on Eznik alone. They are printed in grey, since Eznik was not checked here. Tertullian's "he asked for food to show that he had teeth" (24:41) is attested.
- **24:19b ("a prophet mighty in deed and word").** Unattested, inside the attested verse 24:19. The library's *A Prophet Mighty in Deed and Word* takes its title from it (working document §10.3).
- **Not adopted (Roth "probable"/"possible", or one witness):**
  - 22:8, Epiphanius' wording;
  - 22:14, "the twelve apostles" (NA27: McionE);
  - 22:47, καταφιλῆσαι;
  - 22:64, "striking";
  - 22:67, D's question form;
  - 23:3, "Are you the Christ?";
  - 23:45, "the sun was darkened" (NA27: McionEvid);
  - 23:56, "according to the law".

### Corrections to the previous text

- **Printed though attested absent:** 23:43 ("Today… paradise", Epiph. sch. 72). It is removed.
- **Printed though not part of this text.** These are removed:
  - unattested paragraphs: 22:24–30, 22:52–53, 23:13–16, 23:26, 23:35–42;
  - probably absent: 24:32, 24:44–45;
  - after the last attested verse: 24:48, 24:51–53.
- **Omitted though attested.** These are printed:
  - 22:3 (in part), 22:20, 22:71;
  - 23:22–23, 23:55–56;
  - 24:18, 24:21, 24:25–26, 24:41.
  - 22:20 had been omitted as a Western non-interpolation, although Tertullian attests it.
- **24:6.** The previous text lacked "he has been raised", which is attested, and printed "how" for the attested "all that".
- **Wording the witnesses do not support:**
  - 22:7–8, Epiphanius' paraphrase;
  - 22:14, "the twelve" without "apostles";
  - 22:47, καταφιλῆσαι;
  - 23:3, "Christ";
  - 24:19, Ναζωραίου (NA27 Ναζαρηνοῦ);
  - 23:2, only one of the two attested additions.
  - NA27 is printed, or the attested reading where one is adopted.
- **Library:** `library_corrections.md` items 12 (22:19–20 and the Western non-interpolations), 13 (24:39–43) and 14 (24:6).

## Front matter (2026-10-12)

- **Preface rewritten** (`scripts/audit/frontmatter.py`, `description` in the JSON). It describes what the text is and covers:
  - the witnesses and how much each can prove;
  - the four classes and what is printed;
  - the wording rules;
  - the results with their totals (1,017 verses of Luke 3–24: 485 A+, 143 A−, 44 U−, 345 U?; 708 printed, 223 grey);
  - the priority question, left open;
  - terminology and sources.

  The previous preface made three statements the evidence does not support (research questions Q6):
  - "editorial fatigue analysis" as a method;
  - the Western non-interpolations as a criterion;
  - the excision of the resurrection proofs.
- **The PDF prints the preface in paragraphs.** The title page reads "A Reconstruction of the Jamesian Protograph", following batch 1, which withdrew "forensic".
- **Q4 implemented.** ὁ χριστός is "the Anointed One" (4:41; 9:20; 20:41; 22:67; 23:2; 24:26).
- **Q5 checked.** No "spiritual body" language occurs. "The Living One" is used at 24:5.
- **All six batch scripts were rerun in order.** The JSON and apparatus they produce are identical to the committed files except for the Q4 translations.
- **README and CLAUDE.md** now describe the actual schema, the apparatus, the build and the decision rules.
