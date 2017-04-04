from apps.patients.models import RelationshipType
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
    RelationshipTypeSerializer
)


class RelationshipTypeView(ListCreateAPIView):
    permission_classes = (isStaffOrReadOnly,)
    queryset = RelationshipType.objects.all()
    serializer_class = RelationshipTypeSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('name', 'order')

class RelationshipTypeDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (isStaffOrReadOnly,)
    queryset = RelationshipType.objects.all()
    serializer_class = RelationshipTypeSerializer
