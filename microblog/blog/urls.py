from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
#    url(r'^blog/$',include(views.blog_list),name="list"),
    url(r'^blog/$',views.PostListView.as_view(),name="list"),

    url(r'^blog/(<slug>[\w-]+)/$',views.PostDetailView.as_view(),name="detail"),
#    url(r'^blog/(?P<pk>\d+)/$',include(views.blog_detail),name="detail"),
)
