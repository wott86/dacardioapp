from django.conf.urls import url
from django.contrib import admin

from .views import (
    UserView,
    UsersView,
)

urlpatterns = [
    url(r'^$', UsersView.as_view()),
    url(r'^(?P<pk>[\w-]+)/$', UserView.as_view())
]