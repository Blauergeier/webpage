from django.conf.urls import url

from . import views

app_name = 'blogg'
urlpatterns = [
    #url: /blogg/
    url(r'^$', views.index, name='index'),

    #url: /blogg/5/
    url(r'^(?P<entry_id>[0-9]+)/$', views.detail, name='detail'),

    #url: /blogg/{blog_name}/
    url(r'^(?P<blog_name>[A-Za-z]+)/$', views.index, name='blog'),
]