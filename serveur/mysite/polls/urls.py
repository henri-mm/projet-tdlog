from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^index$', views.index, name='index'),
    url(r'^date$', views.date_actuelle),
    url(r'^addition/(?P<nombre2>\d+)/(?P<nombre2>\d+)/$', views.addition),
)
