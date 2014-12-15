from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^github/(?P<acme>\d+)/$', views.index),
    #ajax
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
