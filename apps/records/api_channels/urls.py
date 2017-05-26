from django.conf.urls import url, include
from rest_framework_nested import routers

from .views import ChannelViewSet
from apps.records.api_records import urls

channel_router = routers.NestedSimpleRouter(urls.records_router, r'records', lookup='record')
channel_router.register(r'channels', ChannelViewSet, base_name='record-channels')

urlpatterns = (
    url(r'^', include(channel_router.urls)),
)