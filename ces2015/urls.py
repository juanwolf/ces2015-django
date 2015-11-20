from django.conf.urls import patterns, url, include
from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # To allow admin section
    url('', include('blogengine.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
