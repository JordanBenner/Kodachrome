from django.contrib import admin
from blog.models import Blog, Post, Poll, Choice


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created', 'blog')


@admin.register(Poll)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('question', 'slug')


@admin.register(Choice)
class PostAdmin(admin.ModelAdmin):
    list_display = ('answer', 'votes', 'poll')
