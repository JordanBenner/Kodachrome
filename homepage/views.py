from django.template.response import TemplateResponse
from django import http
from django.templatetags.static import static


def homepage(request):
    context = {}
    return TemplateResponse(request, 'base.html', context)


def favicon(request):
    return http.HttpResponseRedirect(static('img/favicon.ico'))
