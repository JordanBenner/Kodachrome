"""kodachrome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import blog.views
import homepage.views
#import portfolio.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/(\S+)/(\S+)/$', blog.views.blog_post),
    url(r'^blog/(\S+)/$', blog.views.blog_index),
    url(r'^poll/(\S+)/vote/(\d+)/$', blog.views.vote, name="vote"),
    url(r'^poll/(\S+)/$', blog.views.results, name="poll"),
    url(r'^poll/$', blog.views.poll_index, name="poll_index"),
    url(r'^$', homepage.views.homepage, name='homepage'),
    url(r'^p$', homepage.views.portfolio, name='portfolio'),
    url(r'^favicon.ico$', homepage.views.favicon),
    # url(r'^pricing/(\S+)/$', prices.views.prices_index),
    #url(r'^portfolio/(\S+)/$', portfolio.views.results, name="portfolio"),

]
