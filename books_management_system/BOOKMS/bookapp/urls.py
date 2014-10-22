
from django.conf.urls import patterns,url
from bookapp import views,models

urlpatterns = patterns('',

    url(r'book/create/$', views.create_book),
    url(r'book/list/$', views.list_book),
    url(r'book/edit/(?P<id>[^/]+)/$', views.edit_book),
    url(r'book/view/(?P<id>[^/]+)/$', views.view_book),
    
)
