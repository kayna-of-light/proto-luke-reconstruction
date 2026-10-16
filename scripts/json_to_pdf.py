#!/usr/bin/env python3
"""
JSON to PDF Converter for Proto-Luke Gospel
Generates a professional PDF with Greek/English parallel columns using ReportLab
"""

import json
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, NextPageTemplate, PageTemplate, Frame, BaseDocTemplate
)
from reportlab.platypus.flowables import BalancedColumns, HRFlowable
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
import os

# Custom page size (7x10 inches - common for academic books)
BOOK_SIZE = (7*inch, 10*inch)

# Color definitions
CHAPTER_COLOR = colors.Color(139/255, 69/255, 19/255)  # Saddle brown
VERSE_NUM_COLOR = colors.Color(128/255, 0, 0)  # Dark red
NOTE_COLOR = colors.Color(70/255, 70/255, 70/255)  # Dark gray
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
        leftIndent=24,
        rightIndent=24,
        spaceAfter=22
    ))
    
    # Greek text style
    styles.add(ParagraphStyle(
        name='GreekText',
        fontName=base_font,
        fontSize=10,
        leading=14,
        alignment=TA_LEFT,
    ))
    
    # English text style
    styles.add(ParagraphStyle(
        name='EnglishText',
        fontName=base_font,
        fontSize=10,
        leading=14,
        alignment=TA_LEFT,
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
    
    # Heading of a notes set
    styles.add(ParagraphStyle(
        name='NotesHeading',
        fontName=italic_font,
        fontSize=9.5,
        leading=12,
        alignment=TA_CENTER,
        spaceBefore=6,
        spaceAfter=8,
        textColor=CHAPTER_COLOR
    ))
    
    # A single note: run-in heading, small type
    styles.add(ParagraphStyle(
        name='Note',
        fontName=base_font,
        fontSize=7.5,
        leading=9.6,
        alignment=TA_LEFT,
        spaceAfter=4,
        textColor=NOTE_COLOR
    ))
    
    # Description/preface style
    styles.add(ParagraphStyle(
        name='Preface',
        fontName=base_font,
        fontSize=10,
        leading=15,
        alignment=TA_JUSTIFY,
        leftIndent=30,
        rightIndent=30,
        spaceBefore=20,
        spaceAfter=20
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
            id='normal'
        )
        
        template = PageTemplate(id='normal', frames=frame, onPage=self.add_page_elements)
        self.addPageTemplates([template])
    
    def add_page_elements(self, canvas, doc):
        """Add header and footer to each page."""
        canvas.saveState()
        
        page_num = doc.page
        
        # Skip headers on first few pages (title, preface, TOC)
        if page_num > 3:
            # Header
            canvas.setFont('Times-Italic', 9)
            canvas.setFillColor(colors.gray)
            
            if page_num % 2 == 0:  # Even pages - left header
                canvas.drawString(0.7*inch, self.pagesize[1] - 0.5*inch, 
                                  "The Gospel (Proto-Luke)")
            else:  # Odd pages - right header
                canvas.drawRightString(self.pagesize[0] - 0.7*inch, 
                                       self.pagesize[1] - 0.5*inch,
                                       self.title)
            
            # Header line
            canvas.setStrokeColor(colors.lightgrey)
            canvas.line(0.7*inch, self.pagesize[1] - 0.6*inch,
                        self.pagesize[0] - 0.7*inch, self.pagesize[1] - 0.6*inch)
        
        # Page number (centered at bottom)
        canvas.setFont('Times-Roman', 10)
        canvas.setFillColor(colors.black)
        canvas.drawCentredString(self.pagesize[0]/2, 0.4*inch, str(page_num))
        
        canvas.restoreState()


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
    
    elements.append(Paragraph(
        "<i>A Reconstruction of the</i>",
        ParagraphStyle('centered', parent=styles['Normal'], alignment=TA_CENTER, fontSize=12)
    ))
    elements.append(Paragraph(
        "<i>Jamesian Protograph</i>",
        ParagraphStyle('centered', parent=styles['Normal'], alignment=TA_CENTER, fontSize=12)
    ))
    
    elements.append(Spacer(1, 2*inch))
    
    elements.append(Paragraph(
        "With Greek and English Parallel Text",
        ParagraphStyle('small_center', parent=styles['Normal'], alignment=TA_CENTER, fontSize=10)
    ))
    elements.append(Paragraph(
        "and Scholarly Commentary",
        ParagraphStyle('small_center', parent=styles['Normal'], alignment=TA_CENTER, fontSize=10)
    ))
    
    elements.append(PageBreak())
    
    return elements


def create_preface_page(description, styles):
    """Create the preface/description page."""
    elements = []
    
    elements.append(Spacer(1, 1*inch))
    
    elements.append(Paragraph("PREFACE", styles['ChapterTitle']))
    
    elements.append(Spacer(1, 0.3*inch))
    
    for para in description.split('\n\n'):
        if para.strip():
            elements.append(Paragraph(escape_xml(para.strip()), styles['Preface']))
            elements.append(Spacer(1, 0.12*inch))
    
    elements.append(PageBreak())
    
    return elements


def create_verse_table(verses, styles):
    """Greek and English side by side, the Luke reference small in the margin."""
    elements = []
    
    col_widths = [2.45*inch, 2.7*inch, 0.45*inch]
    
    for verse in verses:
        verse_num = verse.get('verse', '')
        greek = escape_xml(verse.get('greek', ''))
        english = escape_xml(verse.get('english', ''))
        canon_ref = verse.get('canonical_ref', '').replace('Luke ', '')
        if verse.get('attestation') == 'unattested':
            greek = f'<font color="{UNATTESTED_COLOR}">{greek}</font>'
            english = f'<font color="{UNATTESTED_COLOR}">{english}</font>'
        
        verse_marker = f'<font color="#800000" size="7"><super>{verse_num}</super></font> '
        
        data = [[Paragraph(verse_marker + greek, styles['GreekText']),
                 Paragraph(verse_marker + english, styles['EnglishText']),
                 Paragraph(escape_xml(canon_ref), styles['MarginRef'])]]
        
        t = Table(data, colWidths=col_widths)
        t.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 3),
            ('RIGHTPADDING', (0, 0), (-1, -1), 5),
            ('TOPPADDING', (0, 0), (-1, -1), 2),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ]))
        
        elements.append(t)
    
    return elements


def _note_flowables(notes, styles, ref_first):
    out = []
    for note in notes:
        term = escape_xml(note.get('term', ''))
        explanation = escape_xml(note.get('explanation', ''))
        refs = ', '.join(str(v) for v in note.get('verse_refs', []))
        ref = f'<font color="#800000">{refs}</font>' if refs else ''
        if ref_first:
            text = f'{ref}&nbsp;&nbsp;<b>{term}</b>: {explanation}'
        else:
            text = f'<b>{term}</b>' + (f'&nbsp;&nbsp;{ref}' if ref else '') + f'. {explanation}'
        out.append(Paragraph(text, styles['Note']))
    return out


def create_notes_section(notes, styles):
    """End-of-chapter notes in two sets: the restoration, then the translation."""
    elements = []
    restoration = [n for n in notes if n.get('category') != 'translation']
    translation = [n for n in notes if n.get('category') == 'translation']
    
    for heading, group, ref_first in (('Notes on the restoration', restoration, False),
                                      ('Notes on the translation', translation, True)):
        if not group:
            continue
        elements.append(Spacer(1, 14))
        elements.append(HRFlowable(width='30%', thickness=0.4, color=colors.lightgrey, spaceAfter=6))
        elements.append(Paragraph(heading, styles['NotesHeading']))
        elements.append(BalancedColumns(_note_flowables(group, styles, ref_first), nCols=2,
                                        innerPadding=10, leftPadding=0, rightPadding=0))
    
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
    note_elements = create_notes_section(notes, styles)
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
