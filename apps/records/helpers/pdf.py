# coding=utf-8
import StringIO
from fpdf import FPDF
from django.conf import settings
from django.utils.translation import ugettext as _
from reportlab.pdfgen import canvas
from reportlab.lib import colors
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


def create_pdf(channel, data=None, file_like=None):

    if data is None:
        data = {}
    interval_start = int(data.get('interval_start', 0))
    interval_end = int(data.get('interval_end', None))
    segment_size = int(data.get(
        'segment_size', TIME_MULTIPLIER['minutes']))
    if file_like is None:
        file_like = StringIO.StringIO()

    # creating canvas and pdf properties
    width, height = settings.REPORT_PAGE_FORMAT
    margin = 50, 50, 50, 50  # clockwise beginning by top
    y_offset = margin[0]  # this must be incremented
    y_inc = 15
    c = canvas.Canvas(file_like, pagesize=settings.REPORT_PAGE_FORMAT)
    c.setTitle(_('Reporte para el paciente %(patient_name)s') %
               {'patient_name': channel.record.patient.full_name})

    c.drawCentredString(width/2, height-y_offset,
                        _(u'Electrocardiografía ambulatoria continua'))
    y_offset += y_inc
    c.drawCentredString(width/2, height-y_offset,
                        _(u'(Holter 24 Hrs)'))
    y_offset += y_inc
    c.setStrokeColor(colors.grey)
    c.setLineWidth(4)
    c.line(margin[3], height - y_offset, width - margin[1], height - y_offset)
    y_offset += (y_inc * 2)
    c.setStrokeColor(colors.black)

    # patient data
    c.drawString(margin[3], height - y_offset,
                 _('Nombre del paciente: %(patient_name)s') % {
                     'patient_name': channel.record.patient.full_name
                 })
    c.drawString(width - margin[1]-250, height - y_offset,
                 _(u'Médico tratante:'))
    c.drawRightString(width - margin[1], height - y_offset,
                      channel.record.patient.added_by.full_name)

    y_offset += 6
    c.setLineWidth(0.5)
    c.line(margin[3], height - y_offset, width - margin[1], height - y_offset)

    y_offset += y_inc

    c.drawString(margin[3], height - y_offset,
                 _(u'CI: %(id_card_prefix)s-%(id_card_number)s') % {
                     'id_card_prefix': channel.record.patient.id_card_prefix,
                     'id_card_number': channel.record.patient.id_card_number
                 })

    c.drawString(width - margin[1]-250, height - y_offset,
                 _(u'Registro:'))
    c.drawRightString(width - margin[1], height - y_offset,
                      str(channel.record.id))

    y_offset += y_inc

    c.drawString(margin[3], height - y_offset,
                 _(u'Fecha de nacimiento: %(dob)s') % {
                     'dob': channel.record.patient.birth_date
                 })

    c.drawString(width - margin[1]-250, height - y_offset,
                 _(u'Fecha de grabación:'))
    c.drawRightString(width - margin[1], height - y_offset,
                      str(channel.record.created.date()))

    y_offset += y_inc

    c.drawString(margin[3], height - y_offset,
                 _(u'Edad: %(age)s') % {
                     'age': channel.record.patient.age
                 })

    c.drawString(width - margin[1]-250, height - y_offset,
                 _(u'Hora de grabación:'))
    c.drawRightString(width - margin[1], height - y_offset,
                      channel.record.created.strftime('%H:%M:%S %z'))

    y_offset += y_inc

    c.drawString(margin[3], height - y_offset,
                 _(u'Sexo: %(gender)s') % {
                     'gender': channel.record.patient.get_gender_display()
                 })

    c.drawString(width - margin[1]-250, height - y_offset,
                 _(u'Duración:'))
    c.drawRightString(width - margin[1], height - y_offset,
                      channel.duration_str)
    y_offset += 6
    c.line(margin[3], height - y_offset, width - margin[1], height - y_offset)
    y_offset += y_inc
    y_offset += y_inc

    c.drawCentredString(width/2, height-y_offset,
                        _(u'Análisis'))

    # ########
    c.showPage()
    c.save()

    return file_like
