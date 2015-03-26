from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('apps.users.views',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url('^', include('django.contrib.auth.urls'))
)
