from apps.patients.models import Patient
from apps.records.helpers.time import convert_time_to_milli, TIME_MULTIPLIER
from dateutil import parser
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View
from django.conf import settings
from apps.records.helpers import plot
from apps.records.models import Record, Channel
from apps.records.helpers.pdf import create_pdf


class GraphicStatFormView(View):
    """
    GraphicStatFormView
    """
    form_class = None

    @staticmethod
    def validate_objects(record_id, channel_id, patient_id):
        patient = get_object_or_404(Patient, id=patient_id)
        record = get_object_or_404(Record, id=record_id, patient=patient)
        channel = get_object_or_404(Channel, id=channel_id, record=record)
        return patient, record, channel

    def get(self, request, record_id, channel_id, patient_id):
        patient, record, channel = self.validate_objects(
                record_id,
                channel_id,
                patient_id
        )
        data = {
            'record': record,
            'patient': patient,
            'channel': channel
        }
        return HttpResponse(render(
            request,
            'stats_form.html',
            data
        ))

    def post(self, request, record_id, channel_id, patient_id):
        patient, record, channel = self.validate_objects(
                record_id,
                channel_id,
                patient_id
        )
        segment_size = TIME_MULTIPLIER[
                request.POST.get('segment_unit', 'minutes')]\
            * int(request.POST.get('segment_size', 1))

        graphic_type = request.POST.get('stat_type',
                                        GraphicView.GRAPHIC_TYPE_NORMAL)

        data = {
            'record': record,
            'patient': patient,
            'channel': channel,
            'type': graphic_type,
            'interval_start': int(convert_time_to_milli(
                channel,
                parser.parse(request.POST.get('interval_start', 0)))),
            'interval_end': int(convert_time_to_milli(
                channel,
                parser.parse(request.POST.get('interval_end', 0)))),
            'segment_size': segment_size,
            'request_data': request.POST.copy()
        }

        # In case graphic type is a pdf
        if graphic_type == GraphicView.GRAPHIC_TYPE_PDF:
            response = HttpResponse(content_type='application/pdf')
            create_pdf(channel, data, response)
            return response

        return HttpResponse(render(
            request,
            'graphic_result.html',
            data
        ))


class GraphicView(View):
    GRAPHIC_TYPE_NORMAL = 'normal'
    GRAPHIC_TYPE_MEDIA = 'media'
    GRAPHIC_TYPE_STANDARD_DEVIATION = 'std_dev'
    GRAPHIC_TYPE_RETURN_MAP = 'return'
    GRAPHIC_TYPE_SDSD = 'sdsd'
    GRAPHIC_TYPE_PNN50 = 'pnn50'
    GRAPHIC_TYPE_HIST = 'histogram'
    GRAPHIC_TYPE_LFHF = 'lfhf'
    GRAPHIC_TYPE_PDF = 'pdf'
    GRAPHIC_TYPE_ALL = 'all'

    GRAPHIC_TYPE_PARAM_NAME = 'type'

    def get(self, request, record_id, channel_id, patient_id):
        patient = get_object_or_404(Patient, id=patient_id)
        record = get_object_or_404(Record, id=record_id, patient=patient)
        channel = get_object_or_404(Channel, id=channel_id, record=record)
        response = HttpResponse(content_type='image/png')

        graphic_type = request.GET.get(
                self.GRAPHIC_TYPE_PARAM_NAME, self.GRAPHIC_TYPE_NORMAL)

        interval_start = int(request.GET.get('interval_start', 0))
        interval_end = int(request.GET.get('interval_end', None))
        segment_size = int(request.GET.get(
            'segment_size', TIME_MULTIPLIER['minutes']))

        if graphic_type == self.GRAPHIC_TYPE_NORMAL:
            plot.get_channel_image(
                    channel,
                    response,
                    interval_start=interval_start,
                    interval_end=interval_end
            )
        elif graphic_type == self.GRAPHIC_TYPE_MEDIA:
            plot.get_media_image(
                    channel,
                    response,
                    interval_start,
                    interval_end,
                    segment_size
            )
        elif graphic_type == self.GRAPHIC_TYPE_STANDARD_DEVIATION:
            plot.get_standard_deviation_image(
                    channel,
                    response,
                    interval_start,
                    interval_end,
                    segment_size
            )
        elif graphic_type == self.GRAPHIC_TYPE_SDSD:
            plot.get_SDSD_image(
                    channel,
                    response,
                    interval_start,
                    interval_end,
                    segment_size
            )
        elif graphic_type == self.GRAPHIC_TYPE_RETURN_MAP:
            plot.get_return_map_image(
                    channel,
                    response,
                    interval_start,
                    interval_end
            )
        elif graphic_type == self.GRAPHIC_TYPE_PNN50:
            plot.get_PNN50_image(channel,
                                 response,
                                 interval_start,
                                 interval_end,
                                 segment_size)
        elif graphic_type == self.GRAPHIC_TYPE_HIST:
            plot.get_histogram(channel,
                               interval_start,
                               interval_end,
                               file_like=response,
                               bins=int(request.GET.get('bins', 10)))
        elif graphic_type == self.GRAPHIC_TYPE_LFHF:
            plot.get_fft_image(channel,
                               response,
                               interval_start,
                               interval_end,
                               segment_size)

        elif graphic_type == self.GRAPHIC_TYPE_ALL:
            plot.get_all_images(
                channel,
                response,
                interval_start,
                interval_end,
                segment_size
            )

        return response


class RegisterViewList(View):
    paginator_class = Paginator

    def get(self, request, patient_id):
        patient = get_object_or_404(Patient, id=patient_id)
        order = request.GET.get('order', '-id')
        paginator = self.paginator_class(
                patient.records.all(),
                getattr(settings, 'MAX_ELEMENTS_PER_PAGE', 25)
        )
        try:
            page = paginator.page(request.GET.get('page', 1))
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        data = {
            'page': page,
            'order': order,
            'patient': patient
        }

        return HttpResponse(render(request,
                                   'record_list.html',
                                   data))


class RegisterViewDetail(View):

    def get(self, request, record_id, channel_id, patient_id):
        patient = get_object_or_404(Patient, id=patient_id)
        record = get_object_or_404(Record, id=record_id, patient=patient)
        channel = get_object_or_404(Channel, id=channel_id, record=record)
        data = {
            'record': record,
            'patient': patient,
            'channel': channel,
            'type': request.GET.get('type', GraphicView.GRAPHIC_TYPE_NORMAL),
            'constants': GraphicView
        }

        return HttpResponse(render(request,
                                   'graphic.html',
                                   data))


class ReportView(View):

    def get(self, request, record_id, channel_id, _format, patient_id):
        patient = get_object_or_404(Patient, id=patient_id)
        record = get_object_or_404(Record, id=record_id, patient=patient)
        channel = get_object_or_404(Channel, id=channel_id, record=record)
        if _format == 'pdf':
            response = HttpResponse(content_type='application/pdf')
            # response.write(create_pdf(request, channel))
            create_pdf(request, channel, response)
        else:
            response = HttpResponse(status=400)

        return response
