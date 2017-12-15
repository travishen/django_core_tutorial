from django.conf.urls import url

from .views import home

from django.views.generic.base import TemplateView
from dashboard.views import TempView, AnotherTempView

urlpatterns = [
    url(r'^$', home, name='home'),
    # url(r'^about/$', TemplateView.as_view(template_name='cbv/about.html'), name='about'),
    url(r'^temp1/$', TempView.as_view(), name='temp1'),
    url(r'^temp2/$', AnotherTempView.as_view(), name='temp2')
]