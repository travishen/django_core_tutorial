from django.conf.urls import url

from .views import (
    PostModelCreateAPIView,
    PostModelListAPIView,
    PostModelRetrieveAPIView,
    PostModelDestroyAPIView
)

urlpatterns = [
    url(r'^$', PostModelListAPIView.as_view(), name='list'),
    url(r'^create/$', PostModelCreateAPIView.as_view(), name='create'),
    url(r'^retrieve/(?P<primary_key>\d+)/$', PostModelRetrieveAPIView.as_view(), name='retrieve'),
    url(r'^destroy/(?P<primary_key>\d+)/$', PostModelDestroyAPIView.as_view(), name='destroy')
]