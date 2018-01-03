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
    url(r'^retrieve/(?P<id>\d+)/$', PostModelRetrieveAPIView.as_view(), name='retrieve'),
    url(r'^destroy/(?P<id>\d+)/$', PostModelDestroyAPIView.as_view(), name='destroy')
]