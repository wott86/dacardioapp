from rest_framework.serializers import ModelSerializer

from apps.patients.models import (
    Patient,
    Diagnosis
)

from apps.patients.api_habits.serializers import HabitSerializer
from apps.patients.api_ses.serializers import SesSerializer
from apps.patients.api_occupations.serializers import OccupationSerializer
from apps.patients.api_educations.serializers import EducationSerializer
from apps.records.api_anomalies.serializers import AnomalySerializer
from apps.users.api_users.serializers import UserSerializer

class DiagnosisSerializer(ModelSerializer):
    anomalies = AnomalySerializer(many=True)
    made_by = UserSerializer()

    class Meta:
        model = Diagnosis
        exclude = ('patient',)

class DiagnosisCreateSerializer(ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = '__all__'
        read_only_fields = ('made_by', 'patient')


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
