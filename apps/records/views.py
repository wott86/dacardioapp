from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic.base import View
from apps.records.helpers import plot
from apps.records.models import Record


class GraphicView(View):

    def get(self, request, record_id):
        record = get_object_or_404(Record, id=record_id)
        channel = record.channels.filter(pk=5)[0]
        response = HttpResponse(content_type='image/png')
        plot.get_image(channel, response, limit=request.GET.get('samples', None))
        return response
