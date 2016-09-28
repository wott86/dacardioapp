from django.conf.urls import include, url

urlpatterns = [
               # Examples:
               # url(r'^blog/', include('blog.urls')),
               url('^', include('django.contrib.auth.urls'))
               ]
