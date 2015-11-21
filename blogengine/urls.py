from django.conf.urls import patterns
from django.conf.urls import url
from blogengine.views import PostListView, PostCreate

__author__ = 'juanwolf'

urlpatterns = patterns('',
    url(r'^$', PostListView.as_view(), name='homepage'),
    url(r'^post/create', PostCreate.as_view(), name='create-post')
)
