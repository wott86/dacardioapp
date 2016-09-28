from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import logout_then_login
# from django.core.urlresolvers import reverse
from django.views.generic.base import RedirectView
from django.views.static import serve

urlpatterns = [
               # Examples:
               # url(r'^$', 'cardio.views.home', name='home'),
               # url(r'^blog/', include('blog.urls')),
               url(r'^auth/logout/$',
                   logout_then_login, name='logout_then_login'),
               url(r'^$',
                   RedirectView.as_view(url='patients/', permanent=True)),
               url(r'^admin/', include(admin.site.urls)),

               url(r'^users/', include('apps.users.urls')),
               url(r'^patients/', include('apps.patients.urls')),
               url(r'^records/', include('apps.records.urls')),
               ]

if settings.DEBUG:
    urlpatterns += [url(r'^media/(?P<path>.*)$', serve,
                        {'document_root': settings.MEDIA_ROOT,
                         'show_indexes': True})]
