from django.conf.urls import url
from django.contrib import admin


from .views import (
    SesView,
    SesDetailView
)

urlpatterns = [
    url(r'^$', SesView.as_view()),
    url(r'^(?P<pk>[\w-]+)/$', SesDetailView.as_view())
]
