from apps.records.models import Anomaly
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
    AnomalySerializer
)


class AnomalyView(ListCreateAPIView):
    permission_classes = (isStaffOrReadOnly,)
    queryset = Anomaly.objects.all()
    serializer_class = AnomalySerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('name', 'order')

class AnomalyDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (isStaffOrReadOnly,)
    queryset = Anomaly.objects.all()
    serializer_class = AnomalySerializer
