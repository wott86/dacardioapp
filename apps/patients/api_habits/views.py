from apps.patients.models import Habit

from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
)

from .serializers import (
    HabitSerializer
)


class HabitsView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
