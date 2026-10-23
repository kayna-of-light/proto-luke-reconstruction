# Proto-Luke Reconstruction Project - Editorial Instructions

## Project Overview

This repository contains a scholarly reconstruction of **Proto-Luke** (the Jamesian Protograph), a hypothetical source document underlying the canonical Gospel of Luke. The reconstruction is based on the **New Marcionite Paradigm** in biblical scholarship.

### Key Scholarly Sources
- **Matthias Klinghardt** - *The Oldest Gospel and the Formation of the Canonical Gospels*
- **Jason BeDuhn** - *The First New Testament: Marcion's Scriptural Canon*
- **Markus Vinzent** - *Marcion and the Dating of the Synoptic Gospels*
- **Novum Testamentum Graece (NTG 27)** - Greek text base
- **Dieter T. Roth** - *The Text of Marcion's Gospel* (Brill, 2015) - tables of loci and graded reconstruction, the second judgement for every reading
- **Primary witnesses** - Tertullian, *Adversus Marcionem* IV (ed. Evans 1972); Epiphanius, *Panarion* 42 (ed. Holl, GCS 31); *Dialogue of Adamantius* (ed. van de Sande Bakhuyzen, GCS 4)

### Research Assistant

All scholarly questions and editorial decisions requiring in-depth knowledge should be referred to our NotebookLM research assistant: **[The Bible Notebook](https://notebooklm.google.com/notebook/ddf5f7ea-f040-4920-96a4-8e284ee327fe?authuser=1)**

This research assistant has access to all primary sources and scholarly materials needed for the reconstruction. Do NOT make independent editorial decisions on content.

Verse-level decisions (whether a verse is in the text, and its wording) are made from those same primary sources under `docs/audit/METHOD.md` and recorded in the apparatus (`data/apparatus/`), with the witness quoted for every decision. Questions that go beyond the evidence of a verse — interpretation, the wider research framework — go to The Bible Notebook and are logged in `docs/research_questions.md`.

### Core Premise
The reconstruction proceeds from the hypothesis that Marcion's Gospel (*Evangelion*) preserves an earlier form of the Jesus tradition than canonical Luke, and that this earlier form reflects a **Jamesian** (Jewish-Christian) theological perspective rather than a Pauline one.

---

## Terminology Guidelines

### The Protagonist

| ✅ CORRECT | ❌ INCORRECT |
|-----------|-------------|
| **Jesus** | "the Messenger" |
| **he/him** (referring to Jesus) | "the Messenger" as title |

- Always refer to the protagonist as **"Jesus"** in English translations and notes
- The term "the Messenger" was incorrectly used in earlier drafts and has been systematically replaced
- Exception: Lowercase **"messenger(s)"** is correct when translating **ἄγγελος** (angelos) referring to actual angels/messengers
- **ὁ χριστός** is translated **"the Anointed One"** (research question Q4)

### Jamesian vs. Pauline Vocabulary

This is a **Jamesian** reconstruction. Avoid Pauline theological terminology:

| ✅ JAMESIAN (Use These) | ❌ PAULINE (Avoid) |
|------------------------|-------------------|
| "The Living One" (ὁ ζῶν) | "Soma Pneumatikon" |
| "Exaltation" | "Spiritual Body" |
| "Raised/Risen" | "Resurrection body" (when emphasizing physicality) |
| "Vindication" | Pauline atonement language |

### Greek Text Conventions

- Greek text uses the **Novum Testamentum Graece (NTG 27)** edition as base
- Preserve original Greek in `greek` fields
- Use standard scholarly transliteration when discussing Greek in notes
- Mark textual variants explicitly

---

## JSON Structure

The primary data file is `data/proto_luke.json`. It is built by the audit scripts (`scripts/audit/batchN.py`); edit the scripts, not the JSON, and rebuild. Structure:

```json
{
  "title": "THE GOSPEL (PROTO-LUKE)",
  "description": "Preface: paragraphs separated by blank lines (scripts/audit/frontmatter.py)",
  "chapters": [
    {
      "chapter": 1,
      "title": "...",
      "preamble": "Chapter introduction...",
      "verses": [
        {
          "verse": 1,
          "canonical_ref": "Luke 3:1",
          "greek": "NA27 Greek, with adopted Marcionite readings",
          "english": "...",
          "attestation": "unattested"
        }
      ],
      "notes": [
        {"id": 1, "term": "...", "verse_refs": [1, 2], "category": "textual | translation | excision | theological", "explanation": "..."}
      ]
    }
  ]
}
```

`attestation: "unattested"` appears only on verses printed in grey (unattested verses inside an attested paragraph).

### Apparatus

`data/apparatus/luke_NN.json` (Luke 3–24) holds one record per verse or range: `ref`, `class` (`A+`, `A−`, `U−`, `U?`), `roth` (Roth's class and loci), `witnesses` (source and quoted evidence), `wording`, `decision`, `reason`, and, for printed verses, `reconstruction` (chapter and verse in the JSON).

### Field Guidelines

- **description**: The preface: what is reconstructed, the witnesses, the method, the results, sources
- **preamble**: Chapter-level summary of the attested text
- **greek**: NA27 Greek (checked on the page image), with Marcionite readings only where METHOD §5 allows; retroversions are marked in the notes
- **english**: Translation of the printed Greek, following the terminology above
- **notes**: Textual (attestation and wording, with loci), excision (what is not printed and why), translation, theological (marked as interpretation; keeps apart redaction, transmission and reception)

---

## File Organization

```
proto-luke-reconstruction/
├── CLAUDE.md                      # This file
├── data/
│   ├── proto_luke.json            # Reconstruction (built by scripts/audit)
│   └── apparatus/luke_NN.json     # Verse-by-verse evidence, Luke 3–24
├── docs/
│   ├── research_questions.md      # Scholarly decisions log
│   ├── WORKING_DOCUMENT.md        # Background and plan of the audit
│   ├── audit/                     # METHOD.md, AUDIT_LOG.md, library_corrections.md
│   └── stylometry/                # Pre-registration and report
├── output/
│   └── Proto-Luke_Jamesian_Protograph.pdf
├── scripts/
│   ├── json_to_pdf.py             # PDF generation script
│   └── audit/                     # Build scripts (batch1–6, frontmatter) and tools
└── README.md
```

The build scripts read local copies of the sources (SBLGNT/MorphGNT, Tertullian, Epiphanius, Roth) from the directory in `AUDIT_SRC`; these are not committed. Bilby's book and datasets must never be committed (licence).

---

## GitFlow Workflow

- **main**: Release-ready versions only
- **develop**: Active development branch
- Feature work: Create feature branches from `develop`
- Merge to `main` only for releases

---

## Research Questions Protocol

When encountering scholarly decisions, document in `docs/research_questions.md`:

1. State the question clearly
2. Provide relevant evidence
3. Document the decision and rationale
4. Mark as RESOLVED with implementation notes

---

## PDF Generation

Run from project root:

```bash
python scripts/json_to_pdf.py
```

Output: `output/Proto-Luke_Jamesian_Protograph.pdf`

---

## Common Editorial Tasks

### Adding/Editing Verses
1. Read the witnesses for the verse in their primary texts; assign the class (METHOD §3)
2. Ensure Greek text matches NTG 27 on the page image (or note the adopted reading and why)
3. Translation uses the terminology above
4. Notes cite the locus of every claim; do not cite this file or unverified library claims as evidence
5. Record the decision in the apparatus and in `docs/audit/AUDIT_LOG.md`; consult **The Bible Notebook** for questions beyond the verse evidence

### Terminology Checks
Before committing, verify:
- [ ] No instances of "the Messenger" as title for Jesus
- [ ] No Pauline "Soma Pneumatikon" language
- [ ] Greek text properly formatted (NTG 27 base)
- [ ] Citations follow scholarly convention
- [ ] Every printed verse has an apparatus record; no `A−`/`U−` verse is printed (the batch scripts check this)

### Quality Assurance
- Regenerate PDF after JSON changes
- Verify JSON validity (no syntax errors)
- Check cross-references between chapters

---

## Scholarly Context Notes

### Marcionite Parallels
Where Marcion's *Evangelion* (as reconstructed by scholars) differs from canonical Luke, note:
- The Marcionite reading
- Whether it likely represents the earlier form
- Theological implications of variants

### The Passion Narrative
Chapter 22+ represents the Passion narrative. Special attention to:
- Luke 22:43-44 (Agony in Gethsemane) - in NA27 double brackets and not cited for this text; not printed (batch 6)
- Luke 23:34a ("Father, forgive them") - in NA27 double brackets; only Ephrem may allude to it; not printed (batch 6)
- Luke 22:19b-20 and the other Western non-interpolations - a Western omission does not by itself remove words from this text; 22:20 is attested by Tertullian (batch 6)
- Luke 24 resurrection accounts - "the Living One" (24:5); the attested text of 24:39 and 24:41 is printed (see the chapter 22 notes)

---

## Contact & Attribution

Repository: https://github.com/kayna-of-light/proto-luke-reconstruction.git

This reconstruction is a scholarly exercise in textual criticism and should be cited appropriately in academic work.
