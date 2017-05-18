from rest_framework.serializers import ModelSerializer
from apps.records.models import Anomaly


class AnomalySerializer(ModelSerializer):

    class Meta:
        model = Anomaly
        fields = '__all__'
        read_only_fields = ('id',)