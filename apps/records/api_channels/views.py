from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin
)
from serializers import ChannelSerializer
from apps.patients.models import (
    Patient
)
from apps.records.models import (
    Channel,
    Record
)

class ChannelViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = ChannelSerializer
    queryset = Channel.objects.all()

    def list(self, request, record_pk=None, patient_pk=None):
        patient = get_object_or_404(Patient, pk=patient_pk)
        record = get_object_or_404(patient.records.all(), pk=record_pk)
        queryset = record.channels.all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer =  self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, record_pk=None, patient_pk=None):
        queryset = Channel.objects.filter(pk=pk, record=record_pk, record__patient=patient_pk)
        channel = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(channel)
        return Response(serializer.data)