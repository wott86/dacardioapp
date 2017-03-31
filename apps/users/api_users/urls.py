from django.conf.urls import url
from django.contrib import admin

from .views import (
    UserView,
    UserDetailView,
    UserUpdatePasswordView
)

urlpatterns = [
    url(r'^$', UserView.as_view()),
    url(r'^(?P<pk>[\w-]+)/$', UserDetailView.as_view()),
    url(r'^(?P<pk>[\w-]+)/change-password/$', UserUpdatePasswordView.as_view())
]
