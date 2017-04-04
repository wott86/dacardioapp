from rest_framework.response import Response
from rest_framework import status
from apps.patients.models import Patient

from rest_framework.generics import (
    RetrieveUpdateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from .serializers import (
    PatientSerializer,
    PatientCreateSerializer,
    PictureSerializer
)


class PatientView(ListCreateAPIView):
    queryset = Patient.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PatientCreateSerializer
        return PatientSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        return_serializer = PatientSerializer(obj)
        headers = self.get_success_headers(return_serializer.data)
        return Response(return_serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PatientDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return PatientCreateSerializer
        return PatientSerializer

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

