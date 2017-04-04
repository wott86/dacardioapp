from rest_framework.serializers import ModelSerializer
from apps.patients.models import Ses


class SesSerializer(ModelSerializer):

    class Meta:
        model = Ses
        fields = '__all__'
        read_only_fields = ('id',)
