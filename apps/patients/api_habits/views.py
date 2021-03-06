from apps.patients.models import Habit
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
    HabitSerializer
)


class HabitView(ListCreateAPIView):
    permission_classes = (isStaffOrReadOnly,)
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('name', 'order')

class HabitDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (isStaffOrReadOnly,)
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
