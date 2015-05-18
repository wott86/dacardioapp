from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'cardio.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^$', RedirectView.as_view(url='patients/')),
                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^users/', include('apps.users.urls')),
                       url(r'^patients/', include('apps.patients.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns("",
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True }))