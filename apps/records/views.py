from apps.patients.models import Patient
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View
from django.conf import settings
from apps.records.helpers import plot
from apps.records.models import Record, Channel
from django.template.context import RequestContext


class GraphicView(View):
    GRAPHIC_TYPE_NORMAL = 'normal'
    GRAPHIC_TYPE_MEDIA = 'media'
    GRAPHIC_TYPE_STANDARD_DEVIATION = 'std_dev'
    GRAPHIC_TYPE_RETURN_MAP = 'return'

    GRAPHIC_TYPE_PARAM_NAME = 'type'

    def get(self, request, record_id, channel_id, patient_id):
        patient = get_object_or_404(Patient, id=patient_id)
        record = get_object_or_404(Record, id=record_id, patient=patient)
        channel = get_object_or_404(Channel, id=channel_id, record=record)
        response = HttpResponse(content_type='image/png')

        graphic_type = request.GET.get(self.GRAPHIC_TYPE_PARAM_NAME, self.GRAPHIC_TYPE_NORMAL)

        if graphic_type == self.GRAPHIC_TYPE_NORMAL:
            plot.get_channel_image(channel, response, limit=request.GET.get('samples', None))
        elif graphic_type == self.GRAPHIC_TYPE_MEDIA:
            plot.get_media_image(channel, response, 0, 5000, 40)
        elif graphic_type == self.GRAPHIC_TYPE_STANDARD_DEVIATION:
            plot.get_standard_deviation_image(channel, response, 0, 5000, 40)
        elif graphic_type == self.GRAPHIC_TYPE_RETURN_MAP:
            plot.get_return_map_image(channel, response, 0, 5000)
        return response


class RegisterViewList(View):
    paginator_class = Paginator

    def get(self, request, patient_id):

        patient = get_object_or_404(Patient, id=patient_id)

        order = request.GET.get('order', '-id')
        paginator = self.paginator_class(patient.records.all(), getattr(settings, 'MAX_ELEMENTS_PER_PAGE', 25))
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

        return HttpResponse(render(request, 'record_list.html', context=RequestContext(request, data)))


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

        return HttpResponse(render(request, 'test.html', context=RequestContext(request, data)))
