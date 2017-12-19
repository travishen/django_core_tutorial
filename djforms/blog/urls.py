from django.conf.urls import url

from .views import search, test, post

urlpatterns = [
    url(r'^$', test, name='test'),
    url(r'^search/$', search, name='search'),
    url(r'^post/$', post, name='post')
]