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
