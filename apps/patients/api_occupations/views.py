from apps.patients.models import Occupation
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
    OccupationSerializer
)


class OccupationView(ListCreateAPIView):
    permission_classes = (isStaffOrReadOnly,)
    queryset = Occupation.objects.all()
    serializer_class = OccupationSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('name', 'order')

class OccupationDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (isStaffOrReadOnly,)
    queryset = Occupation.objects.all()
    serializer_class = OccupationSerializer
