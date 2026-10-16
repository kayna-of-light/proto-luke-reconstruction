#!/usr/bin/env python3
"""
JSON to PDF Converter for Proto-Luke Gospel
Generates a professional PDF with Greek/English parallel columns using ReportLab
"""

import json
import re
import unicodedata
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, NextPageTemplate, PageTemplate, Frame, BaseDocTemplate, CondPageBreak
)
from reportlab.platypus.flowables import BalancedColumns, HRFlowable, Flowable
import reportlab.platypus.paragraph as _rlpara
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
import os

# Custom page size (7x10 inches - common for academic books)
BOOK_SIZE = (7*inch, 10*inch)

# The one grid: every block spans the frame; two-column blocks share this centre gutter
GUTTER = 14
MARGIN_REF_GAP = 8

# Color definitions
CHAPTER_COLOR = colors.Color(139/255, 69/255, 19/255)  # Saddle brown
VERSE_NUM_COLOR = colors.Color(128/255, 0, 0)  # Dark red
NOTE_COLOR = colors.Color(40/255, 40/255, 40/255)  # Near black

# Code points Palatino can draw; anything else goes to the fallback font
FALLBACK = {'glyphs': None}

try:
    import pyphen
    _ENGLISH = pyphen.Pyphen(lang='en_US')
except ImportError:
    _ENGLISH = None

_GREEK_LETTERS = set('αβγδεζηθικλμνξοπρσςτυφχψω')
_GREEK_VOWELS = set('αεηιουω')
_DIPHTHONGS = {'αι', 'ει', 'οι', 'υι', 'αυ', 'ευ', 'ηυ', 'ου', 'ωυ'}
# Consonant groups that can begin a word go with the following vowel (Smyth §140)
_ONSETS = set(('βδ βλ βρ γδ γλ γμ γν γρ δμ δν δρ θλ θμ θν θρ κλ κμ κν κρ κτ μν '
               'πλ πν πρ πτ σβ σγ σθ σκ σμ σπ στ σφ σχ τλ τμ τρ φθ φλ φν φρ χθ χλ χμ χν '
               'χρ σκλ σκρ σπλ σπρ στρ σφρ σχρ').split())


def _greek_breaks(word):
    """Positions where a polytonic Greek word may be divided between syllables."""
    base, diaeresis, subscript = [], [], []
    for c in word:
        d = unicodedata.normalize('NFD', c)
        base.append(d[0].lower())
        diaeresis.append('\u0308' in d)
        subscript.append('\u0345' in d)
    nuclei, i = [], 0
    while i < len(word):
        if base[i] in _GREEK_VOWELS:
            pair = base[i] + base[i + 1] if i + 1 < len(word) else ''
            if pair in _DIPHTHONGS and not diaeresis[i + 1] and not subscript[i]:
                nuclei.append((i, i + 2))
                i += 2
                continue
            nuclei.append((i, i + 1))
        i += 1
    breaks = []
    for (_, s), (e, _) in zip(nuclei, nuclei[1:]):
        cluster = ''.join(base[s:e])
        if any(c not in _GREEK_LETTERS for c in cluster):
            continue
        k = next((k for k in range(len(cluster)) if len(cluster) - k == 1 or cluster[k:] in _ONSETS),
                 len(cluster))
        breaks.append(s + k)
    return [b for b in breaks if b >= 2 and len(word) - b >= 2]


def hyphenate(word):
    """(head, tail) pairs, longest head first: classical syllables for Greek, a dictionary for English."""
    if any(unicodedata.normalize('NFD', c)[0].lower() in _GREEK_LETTERS for c in word):
        return [(word[:b], word[b:]) for b in reversed(_greek_breaks(word))]
    return list(_ENGLISH.iterate(word)) if _ENGLISH else []


# ReportLab only offers Latin and Cyrillic words to a hyphenator; admit Greek and the raised dot too
_rlpara._hy_letters += '\u0370-\u03ff\u1f00-\u1fff'
_rlpara._hy_letters_pat = re.compile(f'^[{_rlpara._hy_letters}]+$')
_rlpara._hy_shy_letters_pat = re.compile(f'^[{_rlpara._hy_shy}{_rlpara._hy_letters}]+$')
_rlpara._hy_sfx_pat = re.compile(_rlpara._hy_sfx_pat.pattern.replace(']+$', '\u00b7\u0387]+$'))
TERM_COLOR = colors.Color(0, 51/255, 102/255)  # Dark blue
UNATTESTED_COLOR = "#808080"  # Grey: verse not cited by any witness (attestation: unattested)


def register_fonts():
    """Register fonts for the document."""
    # Try to register Palatino Linotype or fall back to Times
    font_paths = [
        ("C:/Windows/Fonts/pala.ttf", "Palatino"),
        ("C:/Windows/Fonts/palab.ttf", "Palatino-Bold"),
        ("C:/Windows/Fonts/palai.ttf", "Palatino-Italic"),
        ("C:/Windows/Fonts/palabi.ttf", "Palatino-BoldItalic"),
    ]
    
    # Elsewhere, GNU FreeSerif (full polytonic Greek) is registered under the same names
    free_dir = "/usr/share/fonts/truetype/freefont"
    fallback_paths = [
        (f"{free_dir}/FreeSerif.ttf", "Palatino"),
        (f"{free_dir}/FreeSerifBold.ttf", "Palatino-Bold"),
        (f"{free_dir}/FreeSerifItalic.ttf", "Palatino-Italic"),
        (f"{free_dir}/FreeSerifBoldItalic.ttf", "Palatino-BoldItalic"),
    ]
    if not all(os.path.exists(path) for path, _ in font_paths):
        font_paths = fallback_paths
    
    fonts_registered = False
    for path, name in font_paths:
        if os.path.exists(path):
            try:
                pdfmetrics.registerFont(TTFont(name, path))
                fonts_registered = True
            except Exception as e:
                print(f"Could not register {name}: {e}")
    
    if fonts_registered:
        # Map <b> and <i> inside paragraphs to the matching faces
        pdfmetrics.registerFontFamily('Palatino', normal='Palatino', bold='Palatino-Bold',
                                      italic='Palatino-Italic', boldItalic='Palatino-BoldItalic')
        # Characters Palatino lacks (ℵ, 𝔓, →, ḥ) are drawn from Cambria
        cambria = "C:/Windows/Fonts/cambria.ttc"
        if os.path.exists(cambria):
            try:
                pdfmetrics.registerFont(TTFont('Fallback', cambria, subfontIndex=0))
                FALLBACK['glyphs'] = set(pdfmetrics.getFont('Palatino').face.charToGlyph)
            except Exception as e:
                print(f"Could not register fallback font: {e}")
    
    if not fonts_registered:
        # Fall back to Times which is built-in
        print("Using built-in Times font")
    
    return fonts_registered


def create_styles(use_palatino=True):
    """Create paragraph styles for the document."""
    styles = getSampleStyleSheet()
    
    # Base font
    base_font = "Palatino" if use_palatino else "Times-Roman"
    bold_font = "Palatino-Bold" if use_palatino else "Times-Bold"
    italic_font = "Palatino-Italic" if use_palatino else "Times-Italic"
    
    # Title style
    styles.add(ParagraphStyle(
        name='BookTitle',
        fontName=bold_font,
        fontSize=28,
        leading=34,
        alignment=TA_CENTER,
        spaceAfter=12,
        textColor=CHAPTER_COLOR
    ))
    
    # Subtitle style
    styles.add(ParagraphStyle(
        name='Subtitle',
        fontName=italic_font,
        fontSize=16,
        leading=20,
        alignment=TA_CENTER,
        spaceAfter=30,
    ))
    
    # Chapter title style
    styles.add(ParagraphStyle(
        name='ChapterTitle',
        fontName=bold_font,
        fontSize=18,
        leading=24,
        alignment=TA_CENTER,
        spaceBefore=30,
        spaceAfter=4,
        textColor=CHAPTER_COLOR
    ))

    # Luke span under the chapter title
    styles.add(ParagraphStyle(
        name='ChapterSpan',
        fontName=italic_font,
        fontSize=9,
        leading=12,
        alignment=TA_CENTER,
        spaceAfter=18,
        textColor=colors.gray
    ))
    
    # Section title style
    styles.add(ParagraphStyle(
        name='SectionTitle',
        fontName=bold_font,
        fontSize=12,
        leading=16,
        spaceBefore=15,
        spaceAfter=8,
        textColor=CHAPTER_COLOR
    ))
    
    # Preamble style
    styles.add(ParagraphStyle(
        name='Preamble',
        fontName=italic_font,
        fontSize=10.5,
        leading=15,
        alignment=TA_JUSTIFY,
        hyphenationLang=hyphenate,
        spaceAfter=22
    ))
    
    # Greek text style
    styles.add(ParagraphStyle(
        name='GreekText',
        fontName=base_font,
        fontSize=10,
        leading=14,
        alignment=TA_JUSTIFY,
        hyphenationLang=hyphenate,
    ))
    
    # English text style
    styles.add(ParagraphStyle(
        name='EnglishText',
        fontName=base_font,
        fontSize=10,
        leading=14,
        alignment=TA_JUSTIFY,
        hyphenationLang=hyphenate,
    ))

    # Luke reference in the margin column
    styles.add(ParagraphStyle(
        name='MarginRef',
        fontName=base_font,
        fontSize=6.5,
        leading=14,
        alignment=TA_RIGHT,
        textColor=colors.Color(0.6, 0.6, 0.6)
    ))
    
    # Heading of a notes set, in the voice of the chapter title
    styles.add(ParagraphStyle(
        name='NotesHeading',
        fontName=italic_font,
        fontSize=12,
        leading=15,
        alignment=TA_CENTER,
        spaceAfter=12,
        textColor=CHAPTER_COLOR
    ))
    
    # A restoration note: full text width, run-in heading
    styles.add(ParagraphStyle(
        name='RestorationNote',
        fontName=base_font,
        fontSize=9,
        leading=13,
        alignment=TA_JUSTIFY,
        hyphenationLang=hyphenate,
        spaceAfter=8,
        textColor=NOTE_COLOR
    ))
    
    # A translation note: two columns
    styles.add(ParagraphStyle(
        name='Note',
        fontName=base_font,
        fontSize=8.5,
        leading=11.5,
        alignment=TA_JUSTIFY,
        hyphenationLang=hyphenate,
        spaceAfter=5,
        textColor=NOTE_COLOR
    ))
    
    # Description/preface style: the measure and rhythm of the text
    styles.add(ParagraphStyle(
        name='Preface',
        fontName=base_font,
        fontSize=10,
        leading=14,
        alignment=TA_JUSTIFY,
        hyphenationLang=hyphenate,
        spaceAfter=9
    ))
    
    # Small centred lines of the title page
    styles.add(ParagraphStyle(
        name='TitleLine',
        fontName=italic_font,
        fontSize=12,
        leading=16,
        alignment=TA_CENTER
    ))
    styles.add(ParagraphStyle(
        name='TitleFoot',
        fontName=base_font,
        fontSize=10,
        leading=14,
        alignment=TA_CENTER
    ))
    
    return styles


def escape_xml(text):
    """Escape special XML characters for ReportLab paragraphs."""
    if not text:
        return ""
    text = str(text)
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    glyphs = FALLBACK['glyphs']
    if glyphs:
        text = ''.join(c if ord(c) < 128 or ord(c) in glyphs else f'<font name="Fallback">{c}</font>'
                       for c in text)
    return text


class ProtoLukeDoc(BaseDocTemplate):
    """Custom document template with headers and footers."""
    
    def __init__(self, filename, **kwargs):
        self.title = kwargs.pop('doc_title', 'The Gospel (Proto-Luke)')
        super().__init__(filename, **kwargs)
        
        # Define frames for content
        frame = Frame(
            0.7*inch, 0.7*inch,
            self.pagesize[0] - 1.4*inch,
            self.pagesize[1] - 1.4*inch,
            id='normal',
            leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0
        )
        
        template = PageTemplate(id='normal', frames=frame, onPageEnd=self.add_page_elements)
        self.addPageTemplates([template])
    
    def add_page_elements(self, canvas, doc):
        """Running head and folio; opening pages carry the folio only."""
        canvas.saveState()
        
        page_num = doc.page
        font = 'Palatino' if FALLBACK['glyphs'] else 'Times-Roman'
        italic = 'Palatino-Italic' if FALLBACK['glyphs'] else 'Times-Italic'
        
        if not RUNNING['opener'] and RUNNING['head']:
            canvas.setFont(italic, 9)
            canvas.setFillColor(colors.gray)
            y = self.pagesize[1] - 0.5*inch
            if page_num % 2 == 0:
                canvas.drawString(0.7*inch, y, 'The Gospel (Proto-Luke)')
            else:
                canvas.drawRightString(self.pagesize[0] - 0.7*inch, y, RUNNING['head'])
            canvas.setStrokeColor(colors.lightgrey)
            canvas.setLineWidth(0.5)
            canvas.line(0.7*inch, y - 0.1*inch, self.pagesize[0] - 0.7*inch, y - 0.1*inch)
        RUNNING['opener'] = False
        
        if page_num > 1:
            canvas.setFont(font, 9)
            canvas.setFillColor(colors.black)
            canvas.drawCentredString(self.pagesize[0]/2, 0.4*inch, str(page_num))
        
        canvas.restoreState()


RUNNING = {'head': '', 'opener': True}


class RunningHead(Flowable):
    """Marks where a section opens: that page has no running head, the next pages carry its name."""
    def __init__(self, head):
        super().__init__()
        self.head = head
    
    def wrap(self, availWidth, availHeight):
        return 0, 0
    
    def draw(self):
        RUNNING['head'] = self.head
        RUNNING['opener'] = True


def create_title_page(styles):
    """Create the title page elements."""
    elements = []
    
    elements.append(Spacer(1, 2*inch))
    
    elements.append(Paragraph("THE GOSPEL", styles['BookTitle']))
    elements.append(Paragraph("(Proto-Luke)", styles['Subtitle']))
    
    elements.append(Spacer(1, 0.5*inch))
    
    # Decorative line
    line_data = [['']]
    line_table = Table(line_data, colWidths=[3*inch])
    line_table.setStyle(TableStyle([
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, CHAPTER_COLOR),
    ]))
    elements.append(line_table)
    
    elements.append(Spacer(1, 0.5*inch))
    
    elements.append(Paragraph("A Reconstruction of the", styles['TitleLine']))
    elements.append(Paragraph("Jamesian Protograph", styles['TitleLine']))
    
    elements.append(Spacer(1, 2*inch))
    
    elements.append(Paragraph("With Greek and English Parallel Text", styles['TitleFoot']))
    elements.append(Paragraph("and Scholarly Commentary", styles['TitleFoot']))
    
    elements.append(PageBreak())
    
    return elements


def create_preface_page(description, styles):
    """Create the preface/description page."""
    elements = []
    
    elements.append(RunningHead('Preface'))
    
    elements.append(Paragraph("Preface", styles['ChapterTitle']))
    
    elements.append(Spacer(1, 0.3*inch))
    
    for para in description.split('\n\n'):
        para = escape_xml(para.strip())
        if not para:
            continue
        # A short opening sentence is the paragraph's run-in heading, as in the notes
        m = re.match(r'([A-Z][^.]{0,40}\.)\s', para)
        if m and len(m.group(1).split()) <= 5:
            para = f'<b>{m.group(1)}</b>{para[m.end(1):]}'
        elements.append(Paragraph(para, styles['Preface']))
    
    elements.append(PageBreak())
    
    return elements


class VerseRow(Flowable):
    """Greek and English filling the text block either side of the centre gutter; the Luke
    reference sits outside the block, in the margin, on the first line's baseline."""
    SPACE_AFTER = 5
    
    def __init__(self, greek, english, ref, ref_style):
        super().__init__()
        self.greek, self.english, self.ref, self.ref_style = greek, english, ref, ref_style
    
    def wrap(self, availWidth, availHeight):
        self.col = (availWidth - GUTTER) / 2
        self.width = availWidth
        hg = self.greek.wrap(self.col, availHeight)[1]
        he = self.english.wrap(self.col, availHeight)[1]
        self.body = max(hg, he)
        self.height = self.body + self.SPACE_AFTER
        return self.width, self.height
    
    def split(self, availWidth, availHeight):
        return []
    
    def draw(self):
        top = self.height
        self.greek.drawOn(self.canv, 0, top - self.greek.height)
        self.english.drawOn(self.canv, self.col + GUTTER, top - self.english.height)
        st = self.ref_style
        self.canv.setFont(st.fontName, st.fontSize)
        self.canv.setFillColor(st.textColor)
        self.canv.drawString(self.width + MARGIN_REF_GAP, top - self.english.style.fontSize, self.ref)


def create_verse_table(verses, styles):
    """Greek and English side by side, the Luke reference small in the margin."""
    elements = []
    
    for verse in verses:
        verse_num = verse.get('verse', '')
        greek = escape_xml(verse.get('greek', ''))
        english = escape_xml(verse.get('english', ''))
        canon_ref = verse.get('canonical_ref', '').replace('Luke ', '')
        if verse.get('attestation') == 'unattested':
            greek = f'<font color="{UNATTESTED_COLOR}">{greek}</font>'
            english = f'<font color="{UNATTESTED_COLOR}">{english}</font>'
        
        verse_marker = f'<font color="#800000" size="7"><super>{verse_num}</super></font> '
        
        elements.append(VerseRow(Paragraph(verse_marker + greek, styles['GreekText']),
                                 Paragraph(verse_marker + english, styles['EnglishText']),
                                 canon_ref, styles['MarginRef']))
    
    return elements


def luke_refs(numbers, luke_of):
    """Edition verse numbers as compact Luke references: 8:28, 31; 8:28–30; 9:1."""
    parsed = []
    for n in numbers:
        m = re.match(r'(?:Luke )?(\d+):(\d+)([a-z]?)$', luke_of.get(n, ''))
        if m:
            parsed.append((int(m.group(1)), int(m.group(2)), m.group(3)))
    runs = []
    for c, v, part in parsed:
        last = runs[-1] if runs else None
        if last and last[0] == c and not part and not last[3] and v == last[2] + 1:
            last[2] = v
        elif not last or last != [c, v, v, part]:
            runs.append([c, v, v, part])
    out, prev = [], None
    for c, a, b, part in runs:
        verses = f'{a}{part}' if a == b else f'{a}–{b}'
        out.append(verses if c == prev else f'{c}:{verses}')
        prev = c
    return ', '.join(out)


REF_COLOR = '#8c8c8c'


class HangingNote(Flowable):
    """A translation note with its reference hung to the left; kept whole within a column."""
    REF_WIDTH = 0.48 * inch
    
    def __init__(self, ref, text, style):
        super().__init__()
        ref_style = ParagraphStyle('NoteRef', parent=style, alignment=TA_LEFT,
                                   textColor=colors.HexColor(REF_COLOR), hyphenationLang='')
        self.cells = [Paragraph(ref, ref_style), Paragraph(text, style)]
        self.gap = style.spaceAfter
    
    def wrap(self, availWidth, availHeight):
        self.table = Table([self.cells], colWidths=[self.REF_WIDTH, availWidth - self.REF_WIDTH])
        self.table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), self.gap),
        ]))
        return self.table.wrap(availWidth, availHeight)
    
    def split(self, availWidth, availHeight):
        return []
    
    def draw(self):
        self.table.drawOn(self.canv, 0, 0)


def _note_flowables(notes, style, luke_of, ref_first):
    out = []
    for note in notes:
        raw_term = note.get('term', '')
        term = escape_xml(raw_term)
        explanation = escape_xml(note.get('explanation', ''))
        refs = luke_refs(note.get('verse_refs', []), luke_of)
        if ref_first:
            # Only the Greek is bold; the English gloss after it stays plain
            m = re.match(r'([^"].*?),\s*(".*)$', raw_term)
            head = (f'<b>{escape_xml(m.group(1))}</b>, {escape_xml(m.group(2))}' if m
                    else f'<b>{term}</b>')
            out.append(HangingNote(refs, f'{head}: {explanation}', style))
            continue
        else:
            # A heading that already names its verses needs no second reference
            ref = '' if not refs or re.search(r'\d+:\d+', raw_term) else f' ({refs})'
            text = f'<b>{term}</b>{ref}. {explanation}'
        out.append(Paragraph(text, style))
    return out


def _notes_break(title, styles, rule):
    # A heading never stands alone at the foot of a page; the space above it vanishes at a page top
    out = [CondPageBreak(2 * inch)]
    if rule:
        out.append(HRFlowable(width=0.9 * inch, thickness=0.6, color=CHAPTER_COLOR,
                              spaceBefore=22, spaceAfter=10))
        return out + [Paragraph(title, styles['NotesHeading'])]
    return out + [Paragraph(title, ParagraphStyle('NotesHeadingSpaced', parent=styles['NotesHeading'],
                                                  spaceBefore=22))]


def create_notes_section(notes, verses, styles):
    """End-of-chapter notes: the restoration in one column, then the translation in two."""
    elements = []
    luke_of = {v.get('verse'): v.get('canonical_ref', '') for v in verses}
    restoration = [n for n in notes if n.get('category') != 'translation']
    translation = [n for n in notes if n.get('category') == 'translation']
    
    if restoration:
        elements.extend(_notes_break('Notes on the restoration', styles, True))
        elements.extend(_note_flowables(restoration, styles['RestorationNote'], luke_of, False))
    if translation:
        elements.extend(_notes_break('Notes on the translation', styles, not restoration))
        elements.append(BalancedColumns(_note_flowables(translation, styles['Note'], luke_of, True),
                                        nCols=2, innerPadding=GUTTER, leftPadding=0, rightPadding=0,
                                        endSlack=0))  # any overrun would be shrunk to fit
    
    return elements


def create_chapter(chapter, styles):
    """Create a complete chapter with verses and notes."""
    elements = []
    
    chapter_num = chapter.get('chapter', '')
    title = chapter.get('title', f'Chapter {chapter_num}')
    preamble = chapter.get('preamble', '')
    verses = chapter.get('verses', [])
    notes = chapter.get('notes', [])
    
    # Chapter title, with the span of Luke it covers
    elements.append(RunningHead(f'Chapter {chapter_num}'))
    elements.append(Paragraph(f'Chapter {chapter_num}', styles['ChapterTitle']))
    if verses:
        first = verses[0].get('canonical_ref', '')
        last = verses[-1].get('canonical_ref', '').replace('Luke ', '')
        elements.append(Paragraph(escape_xml(f'{first} – {last}'), styles['ChapterSpan']))
    
    if preamble:
        elements.append(Paragraph(escape_xml(preamble), styles['Preamble']))
    
    # Verses
    verse_elements = create_verse_table(verses, styles)
    elements.extend(verse_elements)
    
    # Notes at end of chapter
    note_elements = create_notes_section(notes, verses, styles)
    elements.extend(note_elements)
    
    # Page break after chapter
    elements.append(PageBreak())
    
    return elements


def generate_pdf(json_data, output_path):
    """Generate the complete PDF document."""
    print("Registering fonts...")
    use_palatino = register_fonts()
    
    print("Creating styles...")
    styles = create_styles(use_palatino)
    
    title = json_data.get('title', 'The Gospel (Proto-Luke)')
    description = json_data.get('description', '')
    chapters = json_data.get('chapters', [])
    
    print(f"Creating PDF document: {output_path}")
    
    # Create document
    doc = ProtoLukeDoc(
        str(output_path),
        pagesize=BOOK_SIZE,
        doc_title=title,
        title=title,
        author='',
        leftMargin=0.7*inch,
        rightMargin=0.7*inch,
        topMargin=0.7*inch,
        bottomMargin=0.7*inch
    )
    
    elements = []
    
    # Title page
    print("Creating title page...")
    elements.extend(create_title_page(styles))
    
    # Preface page
    print("Creating preface...")
    elements.extend(create_preface_page(description, styles))
    
    # Chapters
    for i, chapter in enumerate(chapters):
        print(f"Processing chapter {i+1}/{len(chapters)}...")
        elements.extend(create_chapter(chapter, styles))
    
    # Build PDF
    print("Building PDF...")
    doc.build(elements)
    
    print(f"PDF created: {output_path}")


def main():
    """Main entry point."""
    script_dir = Path(__file__).parent
    project_dir = script_dir.parent
    json_path = project_dir / 'data' / 'proto_luke.json'
    output_path = project_dir / 'output' / 'Proto-Luke_Jamesian_Protograph.pdf'
    
    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    print(f"Loading JSON from: {json_path}")
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"Found {len(data.get('chapters', []))} chapters")
    
    generate_pdf(data, output_path)
    
    print("\nDone!")


if __name__ == '__main__':
    main()
