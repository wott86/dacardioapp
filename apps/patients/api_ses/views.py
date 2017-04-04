from apps.patients.models import Ses
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
    SesSerializer
)


class SesView(ListCreateAPIView):
    permission_classes = (isStaffOrReadOnly,)
    queryset = Ses.objects.all()
    serializer_class = SesSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('name', 'order')

class SesDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (isStaffOrReadOnly,)
    queryset = Ses.objects.all()
    serializer_class = SesSerializer
