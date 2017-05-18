from rest_framework.serializers import ModelSerializer
from apps.patients.models import Education


class EducationSerializer(ModelSerializer):

    class Meta:
        model = Education
        fields = '__all__'
        read_only_fields = ('id',)
        