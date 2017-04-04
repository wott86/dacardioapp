from django.conf.urls import url
from django.contrib import admin

from .views import (
    PatientView,
    PatientDetailView,
    PictureView
)

urlpatterns = [
    url(r'^$', PatientView.as_view()),
    url(r'^(?P<pk>[\w-]+)/$', PatientDetailView.as_view()),
    url(r'^(?P<pk>[\w-]+)/picture/$', PictureView.as_view())
]