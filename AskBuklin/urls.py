"""AskBuklin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from Ask_buk import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),

    url(r'^hot/$', views.hot, name='hot'),
	url(r'^question/(?P<id_quest>[0-9]+)$', views.question, name='question'),
    url(r'^tag/(?P<tag>[a-zA-Z0-9]+)$', views.questions_tag, name='questions_tag'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^ask/$', views.ask, name='ask'),
	url(r'^login/$', views.log_in, name='log_in'),
	url(r'^logout/$', views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^like_q/$', views.like_q, name='like_q'),
    url(r'^like_a/$', views.like_a, name='like_a'),
]
