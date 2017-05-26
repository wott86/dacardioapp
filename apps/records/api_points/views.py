from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin
)
from serializers import PointSerializer
from apps.patients.models import (
    Patient
)
from apps.records.models import (
    Point,
    Record,
    Point
)

class PointViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = PointSerializer
    queryset = Point.objects.all()

    def list(self, request, record_pk=None, patient_pk=None, channel_pk=None):
        patient = get_object_or_404(Patient, pk=patient_pk)
        record = get_object_or_404(patient.records.all(), pk=record_pk)
        channel = get_object_or_404(record.channels.all(), pk=channel_pk)
        queryset = channel.points.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, record_pk=None, patient_pk=None, channel_pk=None):
        queryset = Point.objects.filter(pk=pk, channel=channel_pk, channel__record=record_pk, channel__record__patient=patient_pk)
        point = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(point)
        return Response(serializer.data)