from apps.patients.models import Habit

from rest_framework.generics import ListAPIView

from .serializers import (
    HabitSerializer
)


class HabitsView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
