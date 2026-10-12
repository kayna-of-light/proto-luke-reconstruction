# Audit tools

These are the scripts used for the text audit described in `docs/audit/METHOD.md`.

The source editions are not in the repository. Copyright and licence terms rule some of them out (Roth's book and Bilby's work among them). The scripts read local copies from the directory named by `AUDIT_SRC`, which defaults to `/tmp/audit-src`:

| Path under `AUDIT_SRC` | Content | Where it comes from |
|---|---|---|
| `sbl/63-Lk-morphgnt.txt` | SBLGNT Luke, MorphGNT format | github.com/morphgnt/sblgnt |
| `tert/evans_marc_09book4.txt` | Tertullian, *Adv. Marc.* IV (Evans' Latin) | tertullian.org |
| `roth/roth.txt`, `roth/roth.pdf` | Roth, *The Text of Marcion's Gospel* (2015) | owner's library (not to be committed) |
| `data/*.json` | indexes built by `tert_index.py`, `roth_tables.py` and `roth_ch9.py` | generated |

The Epiphanius scholia are read from the transcription committed at `docs/audit/sources/epiphanius_pan42_scholia.md`.

| Script | Purpose |
|---|---|
| `tert_index.py`, `roth_tables.py`, `roth_ch9.py` | Build the indexes of Tertullian's sections and Roth's loci and graded readings. |
| `worksheet.py <luke-chapter> <out.md>` | Per-verse worksheet: SBLGNT, the current JSON, Roth's class and graded line, the Epiphanius scholia, and the Tertullian sections. |
| `overview.py` | Lists the JSON verses against Roth's classes. |
| `buildlib.py` | Shared build helpers. Each verse is NA27 Greek, made from SBLGNT plus patches that were checked against the NA27 page images. |
| `batchN.py`, `batchN_chK.py` | One batch of the audit: the decisions verse by verse (Greek, English, apparatus record, notes). Running the script writes `data/apparatus/luke_NN.json`, replaces the batch's chapters in `data/proto_luke.json`, and runs the checks in METHOD §9. |

The apparatus files and the JSON are the record. Each batch script states the decisions that produced them.
