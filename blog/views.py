# rom django.shortcuts import render

from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
from django import http

from blog.models import Blog, Post, Poll, Choice


def blog_index(request, blog_slug):
    blog = get_object_or_404(Blog, slug=blog_slug)
    posts = Post.objects.filter(blog=blog)
    # view substitute
    tag = request.GET.get('tag', '')
    if tag:
        posts = posts.filter(tag__slug=tag)

    context = {
        'blog': blog,
        'posts': posts,
    }
    return TemplateResponse(request, 'blog.html', context)


def blog_post(request, blog_slug, post_slug):

    context = {
        'post': get_object_or_404(Post, slug=post_slug, blog__slug=blog_slug),
    }
    return TemplateResponse(request, 'blog_post.html', context)


def results(request, question_slug):
    question = get_object_or_404(Poll, slug=question_slug)
    choices = Choice.objects.filter(poll=question)
    context = {'question': question, 'choices': choices}

    return TemplateResponse(request, 'poll_results.html', context)


def vote(request, question_slug, choice_id):
    choice = Choice.objects.get(id=choice_id)
    choice.votes += 1
    choice.save()
    return http.HttpResponseRedirect('../../')


def poll_index(request):
    polls = Poll.objects.all()
    category = request.GET.get('category', '')
    if category:
        polls = polls.filter(categories__slug=category)
        print(polls.count())

    context = {
        'polls': polls,
    }
    return TemplateResponse(request, 'poll.html', context)
