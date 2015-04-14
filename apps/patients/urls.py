__author__ = 'alvaro'
from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'apps.patients.views',
    url(r'^$', 'list_patients', name='list_patients')
)