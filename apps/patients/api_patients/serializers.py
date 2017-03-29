from rest_framework.serializers import ModelSerializer

from apps.patients.models import (
    Patient,
    Habit
)


class HabitSerializer(ModelSerializer):

    class Meta:
        model = Habit
        exclude = ('order',)


class PatientSerializer(ModelSerializer):
    habits = HabitSerializer(many=True)

    class Meta:
        model = Patient
        exclude = ('picture',)
