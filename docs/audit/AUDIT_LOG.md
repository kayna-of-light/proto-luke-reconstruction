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
