from django.conf.urls import url
from django.contrib import admin


from .views import HabitsView

urlpatterns = [
    url(r'^$', HabitsView.as_view()),
]