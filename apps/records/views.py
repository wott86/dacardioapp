from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View
from apps.records.helpers import plot
from apps.records.models import Record, Channel
from django.template.context import RequestContext


class GraphicView(View):
    GRAPHIC_TYPE_NORMAL = 'normal'
    GRAPHIC_TYPE_MEDIA = 'media'
    GRAPHIC_TYPE_STANDARD_DEVIATION = 'std_dev'
    GRAPHIC_TYPE_RETURN_MAP = 'return'

    GRAPHIC_TYPE_PARAM_NAME = 'type'

    def get(self, request, record_id, channel_id):
        record = get_object_or_404(Record, id=record_id)
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


class RegisterView(View):

    def get(self, request, record_id, channel_id):
        record = get_object_or_404(Record, id=record_id)
        channel = get_object_or_404(Channel, id=channel_id, record=record)
        data = {
            'record': record,
            'channel': channel,
            'type': request.GET.get('type', GraphicView.GRAPHIC_TYPE_NORMAL),
            'constants': GraphicView
        }

        return HttpResponse(render(request, 'record_list.html', context=RequestContext(request, data)))
