from django.conf.urls import url

from .views import search, test, post, formset

urlpatterns = [
    url(r'^$', test, name='test'),
    url(r'^search/$', search, name='search'),
    url(r'^post/$', post, name='post'),
    url(r'^formset/$', formset, name='formset'),
]