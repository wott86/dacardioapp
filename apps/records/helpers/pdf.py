from fpdf import FPDF


def create_pdf(request):
    pdf = FPDF('P', 'mm', 'Letter')
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, 'Hello world')
    return pdf.output(dest='S')
