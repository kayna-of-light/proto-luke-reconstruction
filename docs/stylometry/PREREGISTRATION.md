# Stylometric baseline: pre-registration

Written and committed before any feature in the material had been counted (working document §3, rule 8). The commit that adds this file comes before the commit that adds the analysis code and results; the history shows the order. Changes after the first run are listed at the end, with reasons, and nothing above that list is altered.

## 1. Question

Canonical Luke contains material that the witnesses to Marcion's text do not show. Does that material carry the idiom of the hand that produced canonical Luke and Acts *more* than the material the witnesses show, beyond what removing passages at random would produce?

- **Expansion** (canonical Luke expanded the earlier text: the Schwegler model, or the Semler model on Luke's side) predicts yes. The added material is written in the expander's own idiom.
- **Abridgement** (Marcion shortened canonical Luke for doctrinal reasons) predicts no. Cuts made for doctrinal reasons do not select for style, so the idiom is spread proportionally.

What a positive result can and cannot show is set out in §8.

## 2. Data

| Item | Source | Use |
|---|---|---|
| Canonical Luke | SBLGNT with MorphGNT lemmas and parsing (github.com/morphgnt/sblgnt, CC-BY-SA) | All counts are made on the canonical wording. |
| Matthew, Mark, Acts, rest of the NT | same | Reference corpora (§4: F2, F3, F4; NT hapax). |
| Attested present (P) | Roth 2015, as normalized by Bilby: *JOHD* 7 (2021) art. 27, Dataverse doi:10.7910/DVN/BYPOOR, file "Roth GMarc normalized.txt" (CC-BY-NC-ND; downloaded at run time, not committed) | Every verse with an entry is P, including verses attested only in part (6:30a etc.). Entries whose content is only empty brackets (23:34a, 23:34b) are not P. |
| Attested absent (A) | Roth 2015, ch. 3, list of passages attested as not present (as extracted for the audit) | Whole verses only: 1:1–2:52; 3:2–20; 3:21–38; 4:1–13; 8:19; 11:30–32; 11:49–51; 12:6; 13:1–9; 13:29–35; 15:11–32; 18:31–33; 19:29–46; 20:9–17; 20:37; 21:18; 21:21–22; 22:16; 22:35–38; 22:50–51; 23:43. Partly absent verses (9:31, 12:28, 17:10, 20:38, 23:34) are not A. Where a verse is both on this list and in the P file, it is P. |
| Unattested (U) | the rest | — |

**Why Roth and not the audit's own classes.** The baseline has to be independent of the audit's decisions. Roth's classification was made without reference to stylometry and without the project's premise, so the baseline cannot be circular. The audit's classes are used in a later rerun (§7).

The unit is the verse, with SBLGNT versification. Verses SBLGNT does not print (e.g. 17:36, 23:17) do not exist for the analysis.

The **not-present stratum** is N = A ∪ U.
- **Primary contrast:** P against N.
- **Secondary:** P against A, where A is the stricter set.

U contains verses that were in Marcion's text but are not cited. That dilutes any difference between P and N, so the primary contrast is conservative.

## 3. Units of count

- Rates are occurrences per 1,000 words, where a word is a MorphGNT token.
- For a verse-level score, a verse's count is the sum of its feature occurrences.

## 4. Feature families (fixed here)

### F1: Bilby's published signature features, re-implemented

These are re-implemented from the definitions in Bilby's table 3.1 (*First Gospel* v5.01, vol. 3, pp. 2–4). His results are not copied. They are mapped onto MorphGNT as follows.

- "Lemma X" means the MorphGNT lemma.
- "Participle", "infinitive" etc. mean MorphGNT mood P, N, D, S, O.
- "Followed by" means the next token.
- "Within k" means within the next k tokens.

| # | Feature | Implementation |
|---|---|---|
| 1 | πρός + accusative | Lemma πρός whose next nominal or article token is accusative. |
| 2 | Participle + δέ | A participle immediately followed by δέ. |
| 3 | λέγω participle | Lemma λέγω, mood P. |
| 4 | Passive participle | Mood P, voice P. |
| 5 | ἀρχ- root | Lemma begins with ἀρχ or ἄρχ. |
| 6 | Speaking + πρός | Lemma λέγω, πρός within 2. |
| 7 | Aorist middle participle | Tense A, voice M, mood P. |
| 8 | Periphrastic | Lemma εἰμί immediately followed by a participle. |
| 9 | ἄγγελος | Lemma. This is a lexical proxy for Bilby's "angels as characters". |
| 10 | Lukan NT hapax | A lemma that occurs in Luke and in no other NT book. |
| 11 | ἄρχω verb | Lemma ἄρχω, POS V. |
| 12 | γάρ | — |
| 13 | συ-verbs | POS V, lemma begins with συ. |
| 14 | ἰδού | — |
| 15 | καὶ ἐγένετο | καί immediately followed by γίνομαι in the aorist indicative 3rd singular. |
| 16 | πόλις | — |
| 17 | λαός | — |
| 18 | γίνομαι participle | — |
| 19 | ὄχλος | — |
| 20 | ἄρχω + infinitive | An infinitive within 4 of a finite or participial form of ἄρχω. |
| 21 | ἀποκρίνομαι participle | — |
| 22 | ἡμέρα | — |
| 23 | ἕτερος | — |
| 24 | ἐνώπιον | — |
| 25 | Genitive articular infinitive | Genitive article immediately followed by an infinitive. |
| 26 | λέγω … δέ … πρός | λέγω, then δέ within 1, then πρός within 2 of δέ. |
| 27 | κατά + accusative article | — |
| 28 | λέγω infinitive | — |
| 29 | ῥῆμα | — |
| 30 | ἀρχι- compounds | Lemma begins with ἀρχι. |
| 31 | ὁράω participle | — |
| 32 | Article + δέ + participle | Article, δέ, participle, adjacent. |
| 33 | ἐπερωτάω | — |
| 34 | ἑαυτοῦ | — |
| 35 | ἐν τῷ + infinitive | ἐν, dative article, infinitive within 2. |
| 36 | πλήν | — |
| 37 | οὐ μή + subjunctive | οὐ, μή, then a subjunctive within 3. |
| 38 | ἔτος | — |
| 39 | Article + καλέω participle | — |
| 40 | θέλω | — |
| 41 | καλέω participle | — |
| 42 | θαυμάζω | — |
| 43 | πίμπλημι | — |
| 44 | Present passive infinitive | — |
| 45 | ἅπτω | — |
| 46 | ἕως | — |
| 47 | ὅστις | — |
| 48 | καλέω | — |
| 49 | οὖν | — |
| 50 | μέλλω | — |
| 51 | δεῖ | — |
| 52 | ἅπας | — |
| 53 | ἀλλήλων | — |
| 54 | πληρ- lemmas | — |
| 55 | Article + γίνομαι participle | — |
| 56 | Superlative | Degree S. |
| 57 | ὄνομα nominative | — |
| 58 | ἀνίστημι participle | — |
| 59 | Gospel hapax | A lemma in Luke that is absent from Matthew, Mark and John. |
| 60 | Perfect participle | — |
| 61 | αὐτός | — |
| 62 | κατα- verbs | POS V, lemma begins with κατ or καθ. |

The other rows of Bilby's list cannot be implemented mechanically and are not used: oracular-poetic speech, deep-layered sentences, preposed genitive, "cratic" καί, cataphoric expressions, and the thematic clusters. Bilby presents the F1 features as Lk2 signatures, so the predicted direction is a higher rate in N than in P.

### F2: Hawkins-type "characteristic of Luke" vocabulary (blind to Marcion)

These are lemmas that occur at least 4 times in Luke and either:
- do not occur in Matthew or Mark at all; or
- occur in Luke at least twice as often as in Matthew and Mark together (raw counts).

This is the criterion of J. C. Hawkins, *Horae Synopticae* (1899/1909). It is computed from SBLGNT before any reference to Marcion. The family score is the sum of these lemmas' occurrences.

**Predicted:** higher rate in N.

### F3: Acts-characteristic vocabulary (blind to Marcion and to Luke)

These are lemmas that occur at least 4 times in Acts, with a rate in Acts (per 1,000 words) at least twice their rate in Matthew and Mark together. Lemmas occurring 0 times in Matthew and Mark qualify if they occur at least 4 times in Acts.

The definition uses no Luke data. Acts is the work of the hand that produced canonical Luke. So F3 measures that hand's idiom from outside the gospel.

**Predicted:** higher rate in N.

### F4: Function-word profile and distance

- **Function words:** the 100 most frequent lemmas in Luke (all of Luke, computed once).
- **Burrows' Delta.** Relative frequencies are z-scored across these segments: P, N, A, Acts, Mark, Matthew.
- **Predicted:** Delta(N, Acts) < Delta(P, Acts), and Delta(P, Mark) < Delta(N, Mark).
- **Check:** the same comparison with the 50 and the 200 most frequent lemmas.

### F5: Neutral morphological categories (no direction predicted)

Every value of MorphGNT POS, tense, voice and mood, counted as a rate. Tests are two-sided, Holm-corrected within F5. This family exists so that the report shows the whole morphological profile, not only features chosen to show a difference.

## 5. Tests

For every feature in F1, F2 (single lemmas and the family sum), F3 (likewise) and F5:

- **Counts.** k_P, k_N and word totals W_P, W_N.
- **Rate ratio.** RR = (k_N / W_N) / (k_P / W_P), with a 95% confidence interval (log method; 0.5 added to zero cells).
- **Test.** Conditional binomial: given k = k_P + k_N, k_N ~ Bin(k, W_N / (W_P + W_N)). It is one-sided in the predicted direction for F1–F3 and two-sided for F5.
- **Multiple comparisons.** Holm correction within each family at α = 0.05.

### 5.1 The abridgement null (block-preserving)

The family statistic for F1, F2 and F3 is **S = log RR** of the family sum. For F1 this is the sum of all 62 features' occurrences.

- **N1, circular shift.** The P/N mask over the verse sequence of Luke (1:1–24:53) is shifted by every possible offset. That keeps every block of omitted verses intact and moves it elsewhere. The p-value is the share of offsets with S ≥ observed S.
- **N2, block permutation.** The sequence is cut into its maximal runs of P and of N. The N-runs and the P-runs are each permuted at random and interleaved again. There are 10,000 draws, with seed 20261012. The p-value is the share of draws with S ≥ observed S.

The null therefore keeps the number and length of the omissions and moves them through the text without regard to style.

### 5.2 Controls

- **Genre.**
  - A verse is *speech* if it contains:
    - a finite or imperative verb in the 1st or 2nd person; or
    - a 1st- or 2nd-person personal pronoun (lemmas ἐγώ, σύ, ἡμεῖς, ὑμεῖς as MorphGNT lemmatizes them).
  - Otherwise the verse is *narrative*.
  - The RR and the N1 and N2 nulls are computed within each genre separately. A pooled Mantel–Haenszel log RR is also computed across the two.
- **Infancy narrative and genealogy.** Every test is repeated without 1:1–2:52 and 3:23–38.
- **Tradition.** A Luke verse is *Markan* if it shares at least 2 distinct lemma bigrams with any single verse of Mark, after removing the article, καί, δέ, αὐτός and εἰμί. Every test is repeated within Markan and non-Markan verses.
  - The detector is accepted only if it flags between 250 and 550 verses of Luke. Otherwise the tradition control is reported as failed and not run.
- **Strict contrast.** P against A (U left out), for F1–F3 family sums, with the same nulls.

## 6. Predictions and what counts against them

| Hypothesis | Predicts | Counts against it |
|---|---|---|
| Expansion | F2 and F3 family RR > 1, beyond the 95th percentile of N1 and N2, in the full text **and** with genre controlled **and** without Luke 1–2 and the genealogy; Delta(N, Acts) < Delta(P, Acts) | RR at or below the null's 95th percentile once genre is controlled and Luke 1–2 is removed |
| Abridgement | F2 and F3 RR within the null distribution once genre and Luke 1–2 are controlled | RR beyond the 95th percentile under all controls |

Result labels (working document §8):
- **supported:** the prediction holds under all three conditions (full text, genre-controlled, without Luke 1–2 and the genealogy);
- **not observed:** it fails under the controlled conditions;
- **underdetermined:** the results differ between controls, or the Markan and non-Markan strata disagree.

F1 is reported as a replication of Bilby. Its features were chosen by contrasting strata in his own data, so F1 counts as evidence only where F2 and F3 agree with it.

## 7. Use in the audit

**Verse score.** The F2 + F3 occurrences of a verse, per word, are combined with the F4 function-word profile in a regularized logistic regression (L2, C = 1.0). The model is trained to separate P from A verses, without 1:1–2:52 and 3:23–38. It is evaluated by 10-fold cross-validation, stratified, with seed 20261012.

**Threshold for use.**
- If the cross-validated AUC ≥ 0.70, each U verse's score is recorded in the apparatus as a supporting line of evidence. Its weight is stated, it never overrides a witness, and it decides nothing by itself.
- If the AUC < 0.70, the score is not used, and the apparatus says so.

**Rerun.** After the audit, the whole analysis is rerun with the audit's own classes (A+, A−, U−, U?) and the two runs are compared. This is a check on the audit, not a new test.

## 8. What a positive result can and cannot show

**It can show** that the material missing from Marcion's text is written, more than chance placement allows, in the idiom of the hand of canonical Luke and Acts.

**It cannot by itself exclude** an abridger whose reasons for cutting happened to correlate with that idiom. For example, a redactor's idiom concentrated in narrative framing or temple scenes, and an abridger who cut such scenes for doctrinal reasons. The genre, infancy and tradition controls reduce that possibility; they do not remove it. The report states how far each control narrows it.

**A negative result** does not show abridgement either. U dilutes the contrast, and the Roth text is a minimal text.

## 9. Changes after the first run

1. **Parser correction, made before any result was read.** In Bilby's file "()" marks a verse attested with no recoverable wording (e.g. 5:17, 5:20, 6:39), while "([])" marks an attested omission (23:34a, 23:34b). The first run's parser treated both as not present, which dropped 38 attested verses from P. §2 already says that only the two 23:34 entries are excluded, so the parser was corrected to match §2. The first run's output was discarded unread, apart from the stratum counts printed to the console.
2. **Correction to the enumeration of A, found after the first results.** §2 defines A as Roth's list of passages attested as not present (Roth 2015, §3.2.2), but the enumeration given there includes 3:2–20. Roth puts 3:2–20 in his list of *unattested* verses instead (§3.2.3: "though indirectly attested as not present"). The audit's extraction had appended it to the wrong list. The analysis now follows Roth's actual list.
   - **Affected:** only the strict P-against-A contrast. 3:2–20 is in N either way.
   - **Record:** the run on the enumeration as registered is kept in `results/roth_registered_A_list/`, and the report gives both.
3. **Exploratory analyses, not pre-registered** (`scripts/stylometry/exploratory.py`). They were added after the first results and are labelled as exploratory wherever they are reported:
   - **E1:** F1 without its two hapax counts, and F2 and F3 without proper names.
   - **E2:** the share of each feature that survives in Roth's attested wording, compared with canonical Luke's wording of the same verses.
4. **Sensitivity runs on other editions.** These were listed in the working document (§8, Phase B) but not in this file: P is taken from the Harnack, Klinghardt, Nicolotti, BeDuhn, Hahn and Zahn datasets (Bilby's normalized datasets on Dataverse), with A as in item 2 and U the rest. The tests are unchanged.

