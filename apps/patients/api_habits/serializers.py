from rest_framework.serializers import ModelSerializer
from apps.patients.models import Habit


class HabitSerializer(ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'
        read_only_fields = ('id',)
