__author__ = 'alvaro'
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'apps.patients.views',
    url(r'^$', 'patient_list', name='patient_list'),
    url(r'^create/$', 'patient_create', name='patient_create'),
    url(r'^(\d+)/$', 'patient_detail', name='patient_detail'),
    url(r'^(\d+)/edit/$', 'patient_edit', name='patient_edit')
)