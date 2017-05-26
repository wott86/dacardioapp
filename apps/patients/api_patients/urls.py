from django.conf.urls import url, include
from rest_framework_nested import routers

from .views import (
    DiagnosisViewSet,
    PatientViewSet,
    PictureView
)

router = routers.SimpleRouter()
router.register(r'patients', PatientViewSet)

diagnosis_router = routers.NestedSimpleRouter(router, r'patients', lookup='patient')
diagnosis_router.register(r'diagnosis', DiagnosisViewSet, base_name='patient-diagnosis')

urlpatterns = (
    url(r'^', include(router.urls)),
    url(r'^', include(diagnosis_router.urls)),
    url(r'^patients/(?P<pk>[\w-]+)/picture/$', PictureView.as_view())
)