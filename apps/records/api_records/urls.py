from django.conf.urls import url, include
from rest_framework_nested import routers

from .views import RecordViewSet
from apps.patients.api_patients import urls

records_router = routers.NestedSimpleRouter(urls.router, r'patients', lookup='patient')
records_router.register(r'records', RecordViewSet, base_name='patient-records')

urlpatterns = (
    url(r'^', include(records_router.urls)),
)