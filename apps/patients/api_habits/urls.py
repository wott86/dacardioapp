from django.conf.urls import url
from django.contrib import admin


from rest_framework.authtoken import views

urlpatterns = [
    url(r'^api-token-auth/', views.obtain_auth_token),
]