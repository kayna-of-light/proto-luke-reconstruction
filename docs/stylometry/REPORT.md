# Stylometric baseline: report

**Run:** 2026-10-12.

**Pre-registration:** `PREREGISTRATION.md` (commit 1459729, before any counts). Its §9 lists every change made after the first run.

**Code:** `scripts/stylometry/`. **Results:** `docs/stylometry/results/`.

**Reproduce:**
- Put the sources in `AUDIT_SRC`; see `scripts/audit/README.md`.
- Run `python3 scripts/stylometry/baseline.py --strata roth`, and likewise for `harnack`, `klinghardt`, `nicolotti`, `beduhn`, `hahn` and `zahn`.
- Then run `exploratory.py` (with `RUN_E3=1` for E3), `recon_matrix.py` and `summarize.py`.

## 1. What was tested

Canonical Luke was divided verse by verse into three groups:
- **P:** what the witnesses to Marcion's text attest as present.
- **A:** what they attest as absent.
- **U:** the rest.

N stands for A together with U. Every count is made on canonical Luke's own Greek (SBLGNT/MorphGNT).

**The question.** Is canonical Luke's idiom concentrated in N, beyond what deleting the same blocks of verses at random would produce?
- If yes, the material missing from Marcion's text is written in a recognisably different hand (the expansion hypothesis in its stylometric form, as Bilby argues it).
- If no, the missing material cannot be told apart stylistically from what Marcion's text keeps.

**The feature families:**

| Family | What it is | How it was defined |
|---|---|---|
| F1 | 62 of Bilby's published "Lk2 signature" features, re-implemented from his definitions | from his table |
| F2 | Vocabulary characteristic of Luke | Hawkins' criterion, defined against Matthew and Mark |
| F3 | Vocabulary characteristic of Acts | defined against Matthew and Mark, using no Luke data |

The tests also include:
- a function-word distance (Burrows' Delta);
- the whole morphological profile, F5.

**The null.** Every family-level result is judged against the observed omission blocks, moved through the text by every possible circular shift (N1) and by 10,000 random block permutations (N2).

**The controls:**
- genre (speech against narrative);
- leaving out the infancy narrative and the genealogy (1:1–2:52; 3:23–38);
- tradition (verses with and without a Markan parallel);
- a strict P-against-A contrast.

## 2. Results on Roth's edition (the primary run)

**Group sizes:**

| Group | Verses | Words |
|---|---|---|
| P | 484 | 8,681 |
| A | 251 | — |
| U | 414 | — |

**Rate ratios.** Each figure is the rate in N divided by the rate in P. An asterisk marks a ratio beyond the 95th percentile of both nulls.

| Condition | F1 Bilby | F2 Luke vocabulary | F3 Acts vocabulary |
|---|---|---|---|
| Full text | 1.23* | 1.39* | 1.17 |
| Full, genre controlled (Mantel–Haenszel) | 1.18* | 1.34* | 1.10 |
| Without Luke 1–2 and the genealogy | 1.14* | 1.24* | 1.04 |
| Without them, genre controlled | 1.10* | 1.20* | 0.99 |
| Markan verses only | 1.16* | 1.37* | 1.04 |
| Non-Markan verses, without Luke 1–2 | 1.11 | 1.14 | 1.03 |
| Strict P against A | 1.33* | 1.60* | 1.37 |
| Strict P against A, without Luke 1–2 | 1.03 | 1.12 | 1.00 |

**Pre-registered labels (§6):**
- F1: **supported**.
- F2: **supported**.
- F3: **not observed**.
- Expansion as pre-registered requires F2 *and* F3, so the overall label is **underdetermined**.

## 3. The same tests on the other editions (sensitivity)

The editions print different numbers of verses (P) because each editor judges unattested verses differently.

| Edition | P | F1 label | F2 label | F3 label | F2 RR, full | F2 RR, without Luke 1–2 and genre controlled |
|---|---|---|---|---|---|---|
| Roth 2015 | 484 | supported | supported | not observed | 1.39* | 1.20* |
| Harnack 1924 | 603 | underdetermined | underdetermined | not observed | 1.33* | 1.13 |
| Klinghardt 2021 | 799 | underdetermined | underdetermined | not observed | 1.34* | 1.04 |
| Nicolotti 2019 | 777 | not observed | underdetermined | not observed | 1.35* | 1.07 |
| BeDuhn 2013 | 549 | underdetermined | underdetermined | not observed | 1.33* | 1.13 |
| Hahn | 825 | underdetermined | underdetermined | not observed | 1.38* | 1.08 |
| Zahn 1892 | 630 | underdetermined | underdetermined | not observed | 1.33* | 1.13 |

In every edition, the strict P-against-A contrast without Luke 1–2 gives F1 0.96–1.03, F2 1.02–1.12 and F3 0.97–1.01. None is beyond the null.

**The verse-level score (§7).** A regularized classifier trained to tell A verses from P verses (outside Luke 1–2) by vocabulary and function words reaches a cross-validated AUC of 0.51 on Roth's edition and 0.52–0.56 on the others. That is chance. By the pre-registered threshold (≥ 0.70) the score is **not used** in the audit.

## 4. Exploratory checks (not pre-registered)

### E1: content against style

- Removing proper names from F2 and F3 (Μαριάμ, Ζαχαρίας, Ἐλισάβετ and the like) changes little: F2 1.28 in the full text and 1.20 without Luke 1–2, both beyond the null.
- The single features that drive F2 and F1 are mostly thematic vocabulary, not grammar:
  - ῥῆμα, 17 in N against 1 in P;
  - πίμπλημι ("be filled", of the Spirit);
  - λαός ("the people");
  - πνεῦμα, ἄγγελος, ὑποστρέφω;
  - the genitive articular infinitive.
- Bilby's grammatical "signature" features are **not** concentrated in N at all:

| Feature | RR |
|---|---|
| πρός + accusative | 1.06 |
| participle + δέ | 1.02 |
| "say unto" | 0.90 |
| καὶ ἐγένετο | 0.86 |
| periphrastic | 0.96 |
| ἐν τῷ + infinitive | 0.81 |

In canonical Luke's own wording, the verses Marcion's text contains use these features as often as the verses it lacks.

### E2: where Bilby's p-values come from

Bilby's very small probabilities for Lk1 (e.g. πρός + accusative, 1 found against 12 expected, p = 9.6e-05) are computed on the *reconstructed wording* of Marcion's text. For the verses Roth attests, E2 counts how much of each feature survives in Roth's attested wording, compared with canonical Luke's wording of the same verses:

| | Canonical, same verses | Roth's wording | Share retained |
|---|---|---|---|
| All words | 8,681 | 4,141 | 0.48 |
| Nouns | 1,531 | 879 | 0.57 |
| Finite verbs | 1,378 | 517 | 0.38 |
| καί | 635 | 223 | 0.35 |
| αὐτός | 469 | 150 | 0.32 |
| δέ | 266 | 70 | 0.26 |
| **πρός + accusative** | 71 | 17 | **0.24** |
| **participle + δέ** | 41 | 9 | **0.22** |
| **periphrastic** | 16 | 4 | **0.25** |
| **ἐν τῷ + infinitive** | 14 | 5 | **0.36** |
| **λέγω … πρός** | 33 | 2 | **0.06** |
| **καὶ ἐγένετο** | 14 | 0 | **0.00** |

**Two findings follow:**
- **The "signature" features drop out at the rate of ordinary connectives (δέ, καί, αὐτός).** The Church Fathers quote sayings and key phrases, not the connective tissue.
- **The speech-introduction frames ("he said to them") and the narrative transition καὶ ἐγένετο drop out almost completely.** These are exactly the parts of a verse a quoting author leaves out.

A rate measured on attested wording therefore records how the Fathers quoted. It does not, by itself, record who wrote the verse. Bilby's p-values treat the reconstructed wording as if it were a complete text, so they overstate the evidence. This applies to the inference, not to his data.

### E3: the Delta contrast under the block null

The pre-registered Delta comparison holds descriptively in every edition: N is nearer Acts than P is, and P is nearer Mark than N is. Under the block-shift null:

| Condition | N1 p | N2 p |
|---|---|---|
| Full text | 0.023 | 0.002 |
| Without Luke 1–2 | 0.17 | 0.17 |
| Narrative only, without Luke 1–2 | 0.11 | 0.13 |
| Speech only, without Luke 1–2 | 0.48 | 0.53 |

## 5. What the baseline shows

1. **Luke 1–2 and the genealogy stand apart.** Their vocabulary, their nearness to Acts and their morphology differ from the rest of the gospel, beyond chance, in every edition. They are absent from Marcion's text on explicit testimony (Epiphanius, *Pan.* 42.11.4–5), and the style agrees: a separate block.
2. **Outside Luke 1–2, the material missing from Marcion's text cannot be told apart from the material it keeps, in grammar or function words.** This holds in all seven editions and under the strict contrast. In particular it holds for Bilby's grammatical features and for the idiom of Acts.
3. **What remains is lexical and thematic**, and it appears only against Roth's minimal edition: a modest excess (about 1.2×) of Luke's characteristic vocabulary in the unattested material. The words carrying it are ῥῆμα, πίμπλημι, λαός, πνεῦμα and ἄγγελος: "word", "filled with the Spirit", "the people", angels. Two readings fit:
   - These are subjects canonical Luke added.
   - These are subjects the Fathers had no occasion to quote. Roth counts as present only what the Fathers quote; the more inclusive editions, built on other grounds, show no such excess.

   The data cannot separate the two readings.
4. **No verse-level stylometric criterion exists.** Style cannot tell an absent verse from a present one (AUC ≈ 0.5). In the audit, inclusion decisions rest on the witnesses alone.

## 6. What the baseline does not show

- **It does not show that Marcion abridged Luke.** A text whose added material is in the same idiom as its base fits equally well:
  - a common original revised lightly by both sides (Semler);
  - a second edition by the same hand or school (Gramaglia's position, as Bilby reports it);
  - a careful imitator.

  The witnesses' own evidence on priority is unaffected: §2 of the working document (no doctrinal pattern in the absences; independent harmonizations; the 4:23 seam).
- **It does not show that the stylometric case for Luke's expansion has failed in every form.** Only the forms tested here were tested: verse selection on canonical wording, and quotation-limited wording. The stronger claims in the literature, that a stylometric analysis *proves* two different authors throughout, are not reproduced on independent data once Luke 1–2 is set aside.

## 7. Consequences for the audit and for the library

**For the audit:**
- **No change to the method.** Unattested verses are decided from the witnesses' coverage (METHOD §3–4), not from style.
- **Phrasing in notes.** Notes may say that Luke 1–2 is stylistically distinct (this report, §5.1). They may not cite stylometry for the absence or presence of any other verse.

**For the library (Phase F, `docs/audit/library_corrections.md`):**
- **Claims that a computer-aided or stylometric analysis proves canonical Luke expanded Marcion's text are not supported as stated.** These appear in the *Jamesian Protograph* documents, *No Original Exists* §4.2, and the working document's §2.4 summary of Bilby. They need restating, as follows:
  - the infancy narrative is distinct;
  - outside it, no stylistic difference is measurable;
  - the published p-values rest on quotation-limited wording.
- **The 4:23 seam, the harmonization evidence and the absence of a doctrinal pattern in the omissions are untouched by this result.** They now carry the case for priority without stylometric support.

## 8. Still to run

The pre-registered rerun on the audit's own classes (§7 of the pre-registration), once the audit is complete.
