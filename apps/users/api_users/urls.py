from django.conf.urls import url
from django.contrib import admin

from .views import (
    UserView,
    UserDetailView,
)

urlpatterns = [
    url(r'^$', UserView.as_view()),
    url(r'^(?P<pk>[\w-]+)/$', UserDetailView.as_view())
]
