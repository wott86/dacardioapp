from django.conf.urls import url
from django.contrib import admin


from .views import (
    RelationshipTypeView,
    RelationshipTypeDetailView
)

urlpatterns = [
    url(r'^$', RelationshipTypeView.as_view()),
    url(r'^(?P<pk>[\w-]+)/$', RelationshipTypeDetailView.as_view())
]
