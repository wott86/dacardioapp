from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import logout_then_login
# from django.core.urlresolvers import reverse
from django.views.generic.base import RedirectView
from django.views.static import serve
from rest_framework.authtoken import views


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

    url(r'^api/docs/', include('rest_framework_docs.urls')),

    url(r'^api/token-auth/', include('apps.users.api_auth.urls')),
    url(r'^api/users/', include("apps.users.api_users.urls")),
    url(r'^api/', include("apps.patients.api_patients.urls")),
    url(r'^api/', include("apps.records.api_records.urls")),
    url(r'^api/', include("apps.records.api_channels.urls")),
    url(r'^api/', include("apps.records.api_points.urls")),
    url(r'^api/habits/', include("apps.patients.api_habits.urls")),
    url(r'^api/educations/', include("apps.patients.api_educations.urls")),
    url(r'^api/occupations/', include("apps.patients.api_occupations.urls")),
    url(r'^api/relationship-types/', include("apps.patients.api_relationship_types.urls")),
    url(r'^api/socio-economic-status/', include("apps.patients.api_ses.urls")),
    url(r'^api/anomalies/', include("apps.records.api_anomalies.urls")),
]


if settings.DEBUG:
    urlpatterns += [url(r'^media/(?P<path>.*)$', serve,
                        {'document_root': settings.MEDIA_ROOT,
                         'show_indexes': True})]
