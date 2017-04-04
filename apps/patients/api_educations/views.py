from apps.patients.models import Education
from rest_framework import permissions
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)

from cardio.permissions import isStaffOrReadOnly

from .serializers import (
    EducationSerializer
)


class EducationView(ListCreateAPIView):
    permission_classes = (isStaffOrReadOnly,)
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('name', 'order')

class EducationDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (isStaffOrReadOnly,)
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
