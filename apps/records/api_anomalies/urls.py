from django.conf.urls import url
from django.contrib import admin


from .views import (
    AnomalyView,
    AnomalyDetailView
)

urlpatterns = [
    url(r'^$', AnomalyView.as_view()),
    url(r'^(?P<pk>[\w-]+)/$', AnomalyDetailView.as_view())
]