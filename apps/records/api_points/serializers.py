from rest_framework.serializers import ModelSerializer
from ..models import Point

class PointSerializer(ModelSerializer):
    class Meta:
        model = Point
        exclude = ('channel',)