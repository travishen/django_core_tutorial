from django.conf.urls import url, include

urlpatterns = [
    url(r'^api/', include('blog.api.urls', namespace='api'))
]