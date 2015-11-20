# Create your views here.
from django.views.generic import ListView
from blogengine import models


class PostListView(ListView):
    model = models.Post
    template_name = 'blogengine/home.html'
    context_object_name = 'posts'
