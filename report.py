from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def create_report():
    pdf_filename = "TP_Search_Algorithms_Report.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter,
                            rightMargin=40, leftMargin=40,
                            topMargin=40, bottomMargin=40)
    
    story = []
    styles = getSampleStyleSheet()
    
    # Custom Styles
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        textColor=colors.HexColor('#1a365d'),
        spaceAfter=15,
        alignment=1 # Center
    )
    
    heading_style = ParagraphStyle(
        'HeadingStyle',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=13,
        textColor=colors.HexColor('#2b6cb0'),
        spaceBefore=12,
        spaceAfter=6
    )
    
    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        textColor=colors.HexColor('#2d3748'),
        spaceAfter=8,
        leading=14
    )

    # Title
    story.append(Paragraph("Practical Work Report (TP)", title_style))
    story.append(Paragraph("Evaluation and Comparison of Search Algorithms", ParagraphStyle('Sub', parent=title_style, fontSize=14, textColor=colors.HexColor('#4a5568'))))
    story.append(Spacer(1, 10))

    # Section 1
    story.append(Paragraph("1. Introduction & Objectives", heading_style))
    intro_text = (
        "The objective of this practical work is to evaluate and compare the performance of four fundamental "
        "search algorithms: Simple Sequential Search, Optimised Sequential Search (for sorted tables), "
        "Iterative Binary Search, and Recursive Binary Search. The comparison relies on two core criteria: "
        "(a) Number of Comparisons and (b) Execution Time."
    )
    story.append(Paragraph(intro_text, body_style))

    # Section 2
    story.append(Paragraph("2. Experimental Methodology", heading_style))
    meth_text = (
        "Following the lab guidelines, large arrays of random elements were generated with sizes of "
        "N = 10³, 10⁴, and 10⁶. To ensure statistical accuracy and eliminate anomalies, 30 independent "
        "tests were conducted for each case, and the average values were recorded using high-precision timers."
    )
    story.append(Paragraph(meth_text, body_style))

    # Section 3
    story.append(Paragraph("3. Summary of Findings & Analysis", heading_style))
    findings_text = (
        "• <b>Sequential Search:</b> Exhibits linear time complexity O(N), making performance degrade rapidly for large arrays (10⁶).<br/>"
        "• <b>Optimised Sequential Search:</b> Improves performance on sorted arrays by terminating early, but remains bounded by O(N).<br/>"
        "• <b>Binary Search (Iterative & Recursive):</b> Demonstrates logarithmic time complexity O(log N), maintaining extreme speed and minimal comparison counts even for massive datasets."
    )
    story.append(Paragraph(findings_text, body_style))

    # Section 4
    story.append(Paragraph("4. Conclusion", heading_style))
    concl_text = (
        "The experiments confirm that algorithm selection is critical for application performance. While sequential searches "
        "are sufficient for small datasets, binary search is vastly superior and essential for large-scale searching operations."
    )
    story.append(Paragraph(concl_text, body_style))
    
    story.append(Spacer(1, 15))
    story.append(Paragraph("<b>Submitted to:</b> eboubakkar@gmail.com", ParagraphStyle('SubTo', parent=body_style, fontName='Helvetica-Oblique', textColor=colors.HexColor('#718096'))))

    doc.build(story)
    print(f"Report generated successfully as '{pdf_filename}'")

if __name__ == '__main__':
    create_report()