from django.conf.urls import patterns,url

from views import SubconListView,SubconUpdateView

urlpatterns=patterns('',
	url(r'^$',SubconListView.as_view(),name="list"),
	url(r'^detail/(?P<pk>\d+)/$',SubconUpdateView.as_view(),name='detail'),
	url(r'^add/$',SubconAddView.as_view(),name='add'),

)
