from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import (
    ModelViewSet,
    ViewSet
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
        obj = serializer.save()
        return_serializer = PatientSerializer(obj)
        headers = self.get_success_headers(return_serializer.data)
        return Response(return_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        return_serializer = PatientSerializer(obj)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return Response(return_serializer.data)

class PictureView(RetrieveUpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PictureSerializer

class DiagnosisViewSet(ViewSet):
    serializer_class = DiagnosisCreateSerializer

    def create(self, request, patients_pk=None):
        queryset = Diagnosis.objects.filter(patient=patients_pk)
        patient = Patient.objects.get(pk=patients_pk)
        serializer = DiagnosisSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save(patient=patient, made_by=self.request.user)
        return_serializer = DiagnosisSerializer(obj)
        return Response(return_serializer.data)

    def list(self, request, patients_pk=None):
        queryset = Diagnosis.objects.filter(patient=patients_pk)
        serializer = DiagnosisSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, patients_pk=None):
        queryset = Diagnosis.objects.filter(pk=pk, patient=patients_pk)
        serializer = DiagnosisSerializer(queryset, many=True)
        return Response(serializer.data)
