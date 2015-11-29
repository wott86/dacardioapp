from apps.records.views import GraphicView, RegisterViewDetail, RegisterViewList
from django.contrib.auth.decorators import login_required

__author__ = 'alvaro'
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'apps.records.views',
    url(r'^$', RegisterViewList.as_view(), name='record_list'),
    url(r'^(\d+)/channel/(\d+)/$', RegisterViewDetail.as_view(), name='view_channel'),
    url(r'^(\d+)/channel/(\d+)/image/$', GraphicView.as_view(), name='record_image'),
)
