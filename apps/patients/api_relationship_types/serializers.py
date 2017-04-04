from rest_framework.serializers import ModelSerializer
from apps.patients.models import RelationshipType


class RelationshipTypeSerializer(ModelSerializer):

    class Meta:
        model = RelationshipType
        fields = '__all__'
        read_only_fields = ('id',)
