# coding=utf-8
import StringIO
from fpdf import FPDF
from django.conf import settings
from django.utils.translation import ugettext as _
from reportlab.pdfgen import canvas
from . import plot
from apps.records.helpers.time import TIME_MULTIPLIER


class MyPDF(FPDF):

    def separator_line(self):
        """
        separator_line
        """
        self.set_draw_color(10, 10, 10)
        self.line(
            self.get_x(),
            self.get_y(),
            self.get_x() + 195,
            self.get_y())
        # self.set_draw_color(255)


def create_pdf_old(request, channel):
    # Setup
    pdf = MyPDF('P', 'mm', settings.REPORT_PAGE_FORMAT)
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)

    # content
    pdf.multi_cell(
        0,
        10,
        _(u'ELECTROCARDIOGRAFÍA AMBULATORIA'),
        align='C'
    )
    pdf.separator_line()
    pdf.cell(0, 5, ln=1)
    pdf.set_font_size(12)
    pdf.multi_cell(
        80,
        5,
        _(u'Nombre del paciente: %(patient_name)s') % {
            'patient_name': channel.record.patient.full_name
        },
        border='R',
        align='L'
    )
    pdf.cell(
        0,
        5,
        _(u'Médico tratante: %(physician_name)s') % {
            'physician_name': channel.record.patient.added_by.full_name
        },
        align='L'
    )
    return pdf.output(dest='S')


def create_pdf(request, channel, file_like=None):

    interval_start = int(request.GET.get('interval_start', 0))
    interval_end = int(request.GET.get('interval_end', None))
    segment_size = int(request.GET.get(
        'segment_size', TIME_MULTIPLIER['minutes']))
    if file_like is None:
        file_like = StringIO.StringIO()

    # pdf creation
    c = canvas.Canvas(file_like, pagesize=settings.REPORT_PAGE_FORMAT)
    c.drawString(100, 750, 'Hello world')
    c.save()

    return file_like
