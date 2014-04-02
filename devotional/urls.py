from django.conf.urls import patterns, url
from devotional.views import list_devotionals

urlpatterns = patterns('',
    url(r'list/$', list_devotionals, name='devotionals'),
)
