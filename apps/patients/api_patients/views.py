from django.shortcuts import get_object_or_404
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import (
    GenericViewSet,
    ModelViewSet
)
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin
)

from rest_framework.generics import (
    RetrieveUpdateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)

from apps.patients.models import (
    History,
    Diagnosis,
    Patient
)

from .serializers import (
    DiagnosisSerializer,
    DiagnosisCreateSerializer,
    PatientSerializer,
    PatientCreateSerializer,
    PictureSerializer
)

class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('first_name', 'last_name', 'id_card_number', 'chart_number')
    ordering_fields = ('first_name', 'last_name', 'id_card_number', 'chart_number')

    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PUT' or self.request.method == 'PATCH':
            return PatientCreateSerializer
        return PatientSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save(created_by=self.request.user, updated_by=self.request.user)
        return_serializer = PatientSerializer(obj)
        headers = self.get_success_headers(return_serializer.data)
        return Response(return_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save(updated_by=self.request.user)
        return_serializer = PatientSerializer(obj)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return Response(return_serializer.data)

class PictureView(RetrieveUpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PictureSerializer

class DiagnosisViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin):
    serializer_class = DiagnosisCreateSerializer
    queryset = Diagnosis.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PUT' or self.request.method == 'PATCH':
            return DiagnosisCreateSerializer
        return DiagnosisSerializer

    def create(self, request, patient_pk=None):
        queryset = Diagnosis.objects.filter(patient=patient_pk)
        patient = Patient.objects.get(pk=patient_pk)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save(patient=patient, made_by=self.request.user)
        return_serializer = DiagnosisSerializer(obj)
        return Response(return_serializer.data)

    def list(self, request, patient_pk=None):
        patient = get_object_or_404(Patient, pk=patient_pk)
        queryset = patient.diagnosis.all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer =  self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, patient_pk=None):
        queryset = Diagnosis.objects.filter(pk=pk, patient=patient_pk)
        diagnosis = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(diagnosis)
        return Response(serializer.data)
