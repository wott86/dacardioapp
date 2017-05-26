from django.conf.urls import url, include
from rest_framework_nested import routers

from .views import PointViewSet
from apps.records.api_channels import urls

point_router = routers.NestedSimpleRouter(urls.channel_router, r'channels', lookup='channel')
point_router.register(r'points', PointViewSet, base_name='channel-points')

urlpatterns = (
    url(r'^', include(point_router.urls)),
)