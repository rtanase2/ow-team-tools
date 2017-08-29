from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^heroprefs/', include('heroprefs.urls')),
    url(r'^admin/', admin.site.urls),
]