from apps.patients.models import (
    Habit,
    Patient
    )

from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from .serializers import (
    HabitSerializer,
    PatientSerializer
)


class PatientsView(ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientView(RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class HabitsView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

