from django.conf.urls import url

from .views import (
    PostModelCreateAPIView,
    PostModelListAPIView
)

urlpatterns = [
    url(r'^$', PostModelListAPIView.as_view(), name='list'),
    url(r'^create/$', PostModelCreateAPIView.as_view(), name='create')
]