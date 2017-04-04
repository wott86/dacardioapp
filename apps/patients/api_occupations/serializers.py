from rest_framework.serializers import ModelSerializer
from apps.patients.models import Occupation


class OccupationSerializer(ModelSerializer):

    class Meta:
        model = Occupation
        fields = '__all__'
        read_only_fields = ('id',)
