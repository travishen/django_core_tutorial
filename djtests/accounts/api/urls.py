from django.conf.urls import url
from django.contrib import admin

from .views import (
    PostCrea,
    UserLoginAPIView
    )

urlpatterns = [
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
]
