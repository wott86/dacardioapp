from django.conf.urls import url
from django.contrib import admin

from .views import (
    PatientView
)

urlpatterns = [
    url(r'^$', PatientView.as_view()),
    url(r'^(?P<pk>[\w-]+)/$', PatientView.as_view(), name='detail')
]