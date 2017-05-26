from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin
)
from serializers import RecordSerializer
from apps.records.models import Record
from apps.patients.models import Patient

class RecordViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = RecordSerializer
    queryset = Record.objects.all()

    def list(self, request, patient_pk=None):
        patient = get_object_or_404(Patient, pk=patient_pk)
        queryset = patient.records.all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer =  self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, patient_pk=None):
        queryset = Record.objects.filter(pk=pk, patient=patient_pk)
        record = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(record)
        return Response(serializer.data)