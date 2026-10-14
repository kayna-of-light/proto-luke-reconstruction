"""Front matter of the reconstruction: writes the preface (`description`) into data/proto_luke.json.
Paragraphs are separated by blank lines; scripts/json_to_pdf.py prints each as a paragraph.
Usage: AUDIT_SRC=<dir with local source copies> python3 -I scripts/audit/frontmatter.py"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from buildlib import REPO, dump_json

PREFACE = """\
This edition presents the gospel read in Marcion's church in the second century, the text its opponents called his Evangelion, reconstructed verse by verse from the writers who quote it. The working premise of the project is that this text is not an abridgement of canonical Luke but an earlier form of it, here called Proto-Luke. A second premise, that it comes from the Jewish-Christian circle of James the Just, is treated as a hypothesis: the chapter notes describe what the attested text contains and say where it supports that identification and where it does not.

The witnesses. Marcion's gospel survives only in quotation. The principal witnesses are Tertullian, Against Marcion, book 4 (c. 207), who works through the text in order, in Latin; and Epiphanius, Panarion 42 (c. 375), whose 78 scholia quote it in Greek and state where it lacked passages of canonical Luke. The Dialogue of Adamantius is used only where its Marcionite speaker quotes the gospel. Other Fathers (Origen, Hippolytus, Ephrem, Eznik) are cited where they bear on a verse. All of them were hostile. What they report the text to have contained is treated as evidence; what they say about why it was so ("Marcion cut it") is polemic and is not used.

How each verse is decided. Every verse of Luke 3–24 has a record in the apparatus (data/apparatus/luke_03.json to luke_24.json), with the witnesses quoted from their primary texts and a class: attested present; attested absent; unattested but probably absent (where a witness who works through that stretch of text would have used the verse against Marcion and does not cite it); or unattested and undetermined. Of the 1,017 verses of Luke 3–24, 485 are attested present, 143 attested absent, 44 probably absent and 345 undetermined. Attested verses are printed. Undetermined verses are printed only inside a paragraph that contains an attested verse, and are set in grey: they are the canonical text where the witnesses are silent, not attested text. Of the 708 verses printed, 223 are grey. Passages attested absent or probably absent are not printed, and each chapter's notes say what is missing and on whose evidence.

The wording. The Greek is that of Nestle–Aland, 27th edition, checked against the printed page. A reading of Marcion's text replaces it only where a witness attests it in its own words and the evidence makes it very likely: a Greek quotation, agreement of two witnesses, or a witness's habit of citation that rules out its own paraphrase. Where only Tertullian's Latin attests a reading and the Latin cannot render the Nestle–Aland Greek, the Greek is a retroversion, and the note says so. Weaker readings are recorded in the notes and do not change the text. Roth's graded reconstruction (2015) is the second judgement for every reading; where this edition departs from it, the reason is given.

The text before Marcion. The witnesses attest the text of Marcion's church; the edition aims at the text he received. On the premise that Marcion did not cut, the two differ at most in wording. The readings of Marcion's text that no independent manuscript of Luke shares were therefore tested against a reading of the whole attested text in its inner, correspondential sense (docs/research/correspondence; METHOD §11). A reading gives way only where it breaks that inner story and the witnesses to Marcion's text are themselves divided, with the earliest supporting canonical Luke. One reading met both conditions: at 18:19 the later copies read "God the Father", Tertullian only "God", and "except God alone" is printed. The same reading found no gap in the attested text that would require any passage it lacks.

What the witnesses show. The text began with the fifteenth year of Tiberius and Jesus' coming down to Capernaum (3:1; 4:31), and had no birth narratives (Luke 1–2). Passages the witnesses state were absent include the parable of the two sons (15:11–32), the entry into Jerusalem and the cleansing of the temple (19:29–46), the tenants of the vineyard (20:9–17), and "Today you will be with me in paradise" (23:43). Some readings are not those of canonical Luke: in the Lord's prayer a petition for the holy spirit stands in place of "hallowed be your name" (11:2); before Pilate the accusers add that Jesus is "destroying the law and the prophets" and "turning away the women and the children" (23:2); on the road to Emmaus the disciples are rebuked for not believing "all that he spoke to you", not "all that the prophets spoke" (24:25). Other passages that have been thought foreign to this text are attested in it: the cup of the covenant in Jesus' blood (22:20); and, after the resurrection, "See my hands and my feet, that it is I myself; for a spirit does not have bones as you see that I have" (24:39), followed by a request for food (24:41). The words "handle me and see" and "flesh and" were not in that verse.

Priority. The witnesses give no sign that the absences follow a single doctrine, and canonical Luke contains a seam where the shorter text does not (the Capernaum reference of 4:23, which in Marcion's order follows the visit to Capernaum). A stylometric test of the published editions of Marcion's gospel (docs/stylometry) finds Luke 1–2 and the genealogy distinct in style from the rest of Luke. Outside them it finds no measurable stylistic difference between the passages Marcion's text lacked and those it kept, so style alone does not decide the direction of change. Whether canonical Luke expanded this text, or both derive from a common original, is left open; the notes say what canonical Luke "has" or "lacks" rather than what it "added".

Terminology. Jesus is named as in the Greek; ὁ χριστός is rendered "the Anointed One"; ὁ ζῶν at 24:5 is "the Living One". The text is printed to 24:47, the last verse any witness cites.

Sources. Tertullian, Adversus Marcionem, ed. and trans. E. Evans (Oxford, 1972). Epiphanius, Panarion, ed. K. Holl, GCS 31 (Leipzig, 1922). Der Dialog des Adamantius, ed. W. H. van de Sande Bakhuyzen, GCS 4 (Leipzig, 1901). Novum Testamentum Graece, 27th ed. (Stuttgart, 1993). The SBL Greek New Testament (2010), as a machine-readable control. D. T. Roth, The Text of Marcion's Gospel (Leiden: Brill, 2015). A. von Harnack, Marcion: Das Evangelium vom fremden Gott, 2nd ed. (Leipzig, 1924). The method, the record of every decision and the corrections made to the previous edition are in docs/audit (METHOD.md, AUDIT_LOG.md)."""


def main():
    path = f'{REPO}/data/proto_luke.json'
    data = json.load(open(path, encoding='utf-8'))
    data['description'] = PREFACE
    dump_json(data, path)
    print('preface:', len(PREFACE.split()), 'words,', PREFACE.count('\n\n') + 1, 'paragraphs')


if __name__ == '__main__':
    main()
