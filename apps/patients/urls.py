__author__ = 'alvaro'
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'apps.patients.views',
    url(r'^$', 'patient_list', name='patient_list'),
    url(r'^(\d+)/$', 'patient_detail', name='patient_detail')
)