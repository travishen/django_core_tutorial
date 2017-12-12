from django.conf.urls import url

from .views import post_model_list_view, post_model_detail_view, post_model_create_view, post_model_update_view
from .views import post_model_view

urlpatterns = [
    # url(r'^$', post_model_list_view, name='list'),
    # url(r'^detail/(?P<id>\d+)/$', post_model_detail_view, name='detail'),
    # url(r'^create/$', post_model_create_view, name='create'),
    # url(r'^update/(?P<id>\d+)/$', post_model_update_view, name='update'),
    url(r'^$', post_model_view, name='list'),
    url(r'^detail/(?P<id>\d+)/$', post_model_view, name='detail'),
    url(r'^create/$', post_model_view, name='create'),
    url(r'^update/(?P<id>\d+)/$', post_model_view, name='update'),
]

