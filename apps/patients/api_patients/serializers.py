from rest_framework.serializers import ModelSerializer

from apps.patients.models import (
    Patient,
    Habit
)

from apps.patients.api_habits.serializers import HabitSerializer
from apps.patients.api_ses.serializers import SesSerializer
from apps.patients.api_occupations.serializers import OccupationSerializer
from apps.patients.api_educations.serializers import EducationSerializer


class PatientSerializer(ModelSerializer):
    habits = HabitSerializer(many=True)
    ses = SesSerializer()
    occupation = OccupationSerializer()
    education = EducationSerializer()

    class Meta:
        model = Patient
        read_only_fields = ('picture',)
        fields = '__all__'

class PatientCreateSerializer(ModelSerializer):
    class Meta:
        model = Patient
        exclude = ('picture',)


class PictureSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = ('picture',)
