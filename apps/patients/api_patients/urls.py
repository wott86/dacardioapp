from django.conf.urls import url
from django.contrib import admin

from .views import (
    PatientsView,
    PatientView
)

urlpatterns = [
    url(r'^$', PatientsView.as_view()),
    url(r'^(?P<pk>[\w-]+)/$', PatientView.as_view(), name='detail')
]