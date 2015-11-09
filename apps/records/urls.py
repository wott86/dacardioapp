from apps.records.views import GraphicView
from django.contrib.auth.decorators import login_required

__author__ = 'alvaro'
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'apps.records.views',
    url(r'^(\d+)/image/$', GraphicView.as_view(), name='record_image'),
)
