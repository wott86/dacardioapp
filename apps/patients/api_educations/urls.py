from django.conf.urls import url
from django.contrib import admin


from .views import (
    EducationView,
    EducationDetailView
)

urlpatterns = [
    url(r'^$', EducationView.as_view()),
    url(r'^(?P<pk>[\w-]+)/$', EducationDetailView.as_view())
]