from django.conf.urls import url
from django.contrib import admin


from .views import (
    HabitView,
    HabitDetailView
)

urlpatterns = [
    url(r'^$', HabitView.as_view()),
    url(r'^(?P<pk>[\w-]+)/$', HabitDetailView.as_view())
]
