from django.conf.urls import url
from django.contrib import admin


from .views import (
    OccupationView,
    OccupationDetailView
)

urlpatterns = [
    url(r'^$', OccupationView.as_view()),
    url(r'^(?P<pk>[\w-]+)/$', OccupationDetailView.as_view())
]
