# Create your views here.
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView
from blogengine import models
from blogengine.forms import PostForm


class PostListView(ListView):
    model = models.Post
    template_name = 'blogengine/home.html'
    context_object_name = 'posts'


class PostCreate(CreateView):
    model = models.Post
    form_class = PostForm
    success_url = reverse_lazy('homepage')
    template_name = "blogengine/create-post.html"

    def get_context_data(self, **kwargs):
        context = super(PostCreate, self).get_context_data(**kwargs)
        context['posts'] = models.Post.objects.all()
        return context
