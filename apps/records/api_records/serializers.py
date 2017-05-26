from rest_framework.serializers import ModelSerializer
from ..models import Record
from apps.users.api_users.serializers import UserSerializer


class RecordSerializer(ModelSerializer):
    taken_by = UserSerializer()
    class Meta:
        model = Record
        fields =('id', 'created', 'modified', 'taken_by')