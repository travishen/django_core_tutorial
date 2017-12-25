from django.conf.urls import url, include
from django.contrib import admin

from .views import register, user_login, home, user_logout, user_activate

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^register/', register, name='register'),
    url(r'^login/', user_login, name='login'),
    url(r'^logout/', user_logout, name='logout'),
    url(r'^activate/(?P<code>[a-z0-9].*)/$', user_activate, name='activate')
]
