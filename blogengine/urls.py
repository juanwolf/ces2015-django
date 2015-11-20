from django.conf.urls import patterns
from django.conf.urls import url
from blogengine.views import PostListView

__author__ = 'juanwolf'

urlpatterns = patterns('',
   url(r'^$', PostListView.as_view(), name='homepage')
)
