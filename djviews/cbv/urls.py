from django.conf.urls import url

from .views import home

from django.views.generic.base import TemplateView
from dashboard.views import TempView, AnotherTempView
from dashboard.views import BookDetail, BookList
from dashboard.views import BookCreate, BookUpdate, BookDelete

urlpatterns = [
    url(r'^$', home, name='home'),
    # url(r'^about/$', TemplateView.as_view(template_name='cbv/about.html'), name='about'),
    url(r'^temp1/$', TempView.as_view(), name='temp1'),
    url(r'^temp2/$', AnotherTempView.as_view(), name='temp2'),
url(r'^book/$', BookList.as_view(), name='book_list'),
url(r'^book/create/$', BookCreate.as_view(), name='book_create'),
    url(r'^book/(?P<slug>[-\w]+)/$', BookDetail.as_view(), name='book_detail'),
    url(r'^book/update/(?P<slug>[-\w]+)$', BookUpdate.as_view(), name='book_update'),
    url(r'^book/delete/(?P<slug>[-\w]+)$', BookDelete.as_view(), name='book_delete')

]