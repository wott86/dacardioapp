from rest_framework.serializers import ModelSerializer

from apps.patients.models import (
    Habit
)


class HabitSerializer(ModelSerializer):

    class Meta:
        model = Habit
        exclude = ('order',)
