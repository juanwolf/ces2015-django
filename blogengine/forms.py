from django import forms
from blogengine.models import Post
from django.utils import six
from django.utils.translation import ugettext as _


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']

    def __init__(self, * args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for key, field in six.iteritems(self.fields):
            self.fields[key].widget.attrs['class'] = 'form-control'

        self.fields['title'].widget.attrs['placeholder'] = _("Titre")
        self.fields['content'].widget.attrs['placeholder'] = _("Message")
        self.fields['author'].widget.attrs['placeholder'] = _("Auteur (twitter, email, etc..)")

