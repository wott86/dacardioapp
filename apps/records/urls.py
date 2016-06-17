from apps.records.views import GraphicView, RegisterViewDetail, \
    RegisterViewList, GraphicStatFormView, ReportView
from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'apps.records.views',
    url(r'^$', login_required(RegisterViewList.as_view()),
        name='record_list'),
    url(r'^(\d+)/channel/(\d+)/$',
        login_required(RegisterViewDetail.as_view()),
        name='view_channel'),
    url(r'^(\d+)/channel/(\d+)/form/$',
        login_required(GraphicStatFormView.as_view()),
        name='view_channel_form'),
    url(r'^(\d+)/channel/(\d+)/image/$',
        login_required(GraphicView.as_view()),
        name='record_image'),
    url(r'^(\d+)/channel/(\d+)/report/(\w+)/$',
        login_required(ReportView.as_view()),
        name='report'),
)
