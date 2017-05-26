from rest_framework.serializers import ModelSerializer
from ..models import Channel

class ChannelSerializer(ModelSerializer):
    class Meta:
        model = Channel
        exclude = ('record',)