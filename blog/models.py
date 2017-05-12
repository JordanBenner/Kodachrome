from django.db import models
from django.conf import settings
# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=140,
                                blank=True, null=True)
    slug = models.SlugField(max_length=50, unique=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    tag = models.ManyToManyField(Tag)
    # tags = models.TextField()
    #
    # def tag_list (self):
    #     return self.tags.split(', ')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Poll(models.Model):
    question = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.question


class Choice(models.Model):
    answer = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    poll = models.ForeignKey(Poll)

    def __str__(self):
        return self.answer
