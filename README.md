# Proto-Luke: The Jamesian Protograph

A reconstruction, from its ancient witnesses, of the gospel text read in Marcion's church: on the project's premise, the earlier form of the Third Gospel.

## Overview

This project reconstructs the gospel read in Marcion's church in the second century (the *Evangelion*), verse by verse, from the writers who quote it. Its premise is that this text is an earlier form of the Third Gospel, called here **Proto-Luke**, and not an abridgement of canonical Luke. Its identification with the circle of James the Just is treated as a hypothesis, tested in the chapter notes against what the attested text contains.

## Method

- **Witnesses.** Tertullian, *Against Marcion* IV (Latin, c. 207); Epiphanius, *Panarion* 42, 78 scholia (Greek, c. 375); the *Dialogue of Adamantius*, where its Marcionite speaker quotes the gospel. What these hostile witnesses report the text to have contained is evidence. What they say about why it was so is polemic and is not used.
- **One decision per verse.** Every verse of Luke 3–24 has a record in `data/apparatus/` with the witnesses quoted and a class:
  - attested present;
  - attested absent;
  - unattested but probably absent;
  - unattested and undetermined.
- **What is printed.** Attested verses are printed. Unattested verses inside an attested paragraph are printed in grey. Absent passages are listed in each chapter's notes.
- **Wording.** Nestle–Aland 27, checked on the printed page. A Marcionite reading replaces it only where a witness attests it in its own words and it is at least "very likely" in Roth's grading. Retroversions from Tertullian's Latin are marked.
- **Western non-interpolations** (Westcott–Hort) are recorded. A Western omission does not by itself remove words from this text.
- The full method is in `docs/audit/METHOD.md`, and every decision is in `docs/audit/AUDIT_LOG.md`.

## Results in brief

- **Restoration by method.** The printed text was read by correspondence from beginning to end, word by word (`docs/research/correspondence/word_by_word.md`). Where the printed text's own words point to a passage it does not print, or a movement it sets going is not completed without it, the passage is printed as restored by method, in green, with the grounds in the notes (METHOD §11). Eight passages: 4:17–21, 14:1–11, 19:28–46, 21:5–6, 22:54–62, 24:33–35, 24:44–46, 24:47b–53. Their class in the apparatus does not change.

- **Coverage.** Of the 1,017 verses of Luke 3–24:
  - 485 are attested present;
  - 143 attested absent;
  - 44 probably absent;
  - 345 undetermined.
  The text prints 766 verses: 223 of them in grey, and 58 in green, restored by method (below).
- **Beginning and end.** The text began at 3:1 + 4:31 (the fifteenth year of Tiberius; Jesus comes down to Capernaum) and had no Luke 1–2. The last verse any witness cites is 24:47; the text is printed to 24:53, with the ending restored by method.
- **Absent by the witnesses' statements:**
  - the parable of the two sons (15:11–32);
  - the entry into Jerusalem and the cleansing of the temple (19:29–46; printed here as restored by method, against Marcion's text);
  - the tenants (20:9–17);
  - "Today you will be with me in paradise" (23:43).
- **Attested and printed:**
  - the petition for the holy spirit in the Lord's prayer (11:2);
  - the cup of the covenant (22:20);
  - "a spirit does not have bones as you see that I have" (24:39), without "handle me and see" and "flesh";
  - the request for food (24:41).
- **Priority.** A stylometric baseline (`docs/stylometry/REPORT.md`) finds Luke 1–2 distinct in style. Elsewhere it finds no measurable difference between what Marcion's text lacked and what it kept. Whether canonical Luke expanded this text or both derive from a common original is left open.
- **Library corrections.** Claims in the companion library that the witnesses contradict are listed in `docs/audit/library_corrections.md`.

## Key Sources

- Tertullian, *Adversus Marcionem*, ed. E. Evans (Oxford, 1972)
- Epiphanius, *Panarion*, ed. K. Holl, GCS 31 (1922)
- *Der Dialog des Adamantius*, ed. W. H. van de Sande Bakhuyzen, GCS 4 (1901)
- *Novum Testamentum Graece*, 27th ed.; SBLGNT as a machine-readable control
- Dieter T. Roth, *The Text of Marcion's Gospel* (Brill, 2015)
- Adolf von Harnack, *Marcion: Das Evangelium vom fremden Gott*, 2nd ed. (1924)
- Jason BeDuhn, *The First New Testament* (2013); Matthias Klinghardt, *The Oldest Gospel and the Formation of the Canonical Gospels* (2015/2021); Mark G. Bilby (stylometry). These are compared in the stylometric baseline.

## Project Structure

```
├── data/
│   ├── proto_luke.json              # The reconstruction: Greek, English, preambles, notes (built by scripts/audit)
│   ├── apparatus/luke_NN.json       # Verse-by-verse evidence and decisions, Luke 3–24
│   └── reconstructions/             # Superseded v1 markdown drafts (not maintained)
├── docs/
│   ├── WORKING_DOCUMENT.md          # Background and plan of the audit
│   ├── audit/                       # METHOD.md, AUDIT_LOG.md, library_corrections.md
│   ├── stylometry/                  # Pre-registration and report of the stylometric baseline
│   └── research_questions.md        # Scholarly questions and resolutions
├── output/
│   └── Proto-Luke_Jamesian_Protograph.pdf  # Generated PDF
├── scripts/
│   ├── audit/                       # Build scripts: batch1–6 (chapters), frontmatter (preface)
│   ├── stylometry/                  # Stylometric baseline
│   ├── json_to_pdf.py               # PDF generation
│   ├── json_to_latex.py             # LaTeX generation
│   └── generate_text.py             # Text extraction
└── README.md
```

To rebuild: `AUDIT_SRC=<local source copies> python3 -I scripts/audit/batchN.py` for N = 1…6, then `scripts/audit/frontmatter.py`, then `python3 scripts/json_to_pdf.py`. The source copies (SBLGNT/MorphGNT, Tertullian, Epiphanius, Roth) are not committed.

## Branching Strategy (GitFlow)

- **main** — Stable releases only
- **develop** — Active development and research
- **feature/** — New features or chapters
- **hotfix/** — Urgent fixes to main

## Companion Repositories

This project is part of a multi-repository research framework:

| Repository | Purpose |
|---|---|
| **[literary-compilation](https://github.com/kayna-of-light/literary-compilation)** | The Divine Bricolage — research collection and synthesis across multiple channels, documenting what the data shows and how it connects |
| **[structured-data-analysis](https://github.com/kayna-of-light/structured-data-analysis)** | Empirical data analysis — NDE phenomenology, past-life memory, MallWorld dream data |
| **[nag-hammadi-analysis](https://github.com/kayna-of-light/NagHammadiLibrary)** | Correspondential reading of the complete Nag Hammadi Library |
| **[manichaean-analysis](https://github.com/kayna-of-light/manichaean-analysis)** | Extraction of the correspondential substrate from the Kephalaia and Manichaean corpus — recovering the Ancient Word |

## Output

The reconstruction is available as a formatted PDF: `output/Proto-Luke_Jamesian_Protograph.pdf`

## License

This scholarly reconstruction is provided for academic and research purposes.
