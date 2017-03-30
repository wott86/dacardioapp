from rest_framework.serializers import ModelSerializer

from apps.patients.models import (
    Patient,
    Habit
)

from apps.patients.api_habits.serializers import HabitSerializer


class PatientSerializer(ModelSerializer):
    habits = HabitSerializer(many=True)

    class Meta:
        model = Patient
        exclude = ('picture',)
