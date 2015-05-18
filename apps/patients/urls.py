from apps.patients.views import PatientList, PatientDetail, PatientEdit, PatientNew
from django.contrib.auth.decorators import login_required

__author__ = 'alvaro'
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'apps.patients.views',
    url(r'^$', login_required(PatientList.as_view()), name='patient_list'),
    url(r'^new/$', login_required(PatientNew.as_view()), name='patient_create'),
    url(r'^(\d+)/$', login_required(PatientDetail.as_view()), name='patient_detail'),
    url(r'^(\d+)/edit/$', login_required(PatientEdit.as_view()), name='patient_edit')
)