from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return '%s - %s' % (self.title, self.author)