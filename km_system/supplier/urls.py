from django.conf.urls import patterns,url

#from supplier.views import SupplierList,SupplierDetail,SupplierDelete

from views import *

urlpatterns=patterns('',
	url(r'^$',SupplierList,name="list"),
	url(r'^detail/(?P<pk>\d+)/$',SupplierDetail,name='detail'),
	url(r'^delete/(?P<pk>\d+)/$',SupplierDelete,name='delete'),
#	url(r'^$',SupplierListView.as_view(),name='list'),
#	url(r'^detail/(?P<pk>\d+)/$',SupplierDetailView.as_view(),name="detail"),
#	url(r'^delete/(?P<pk>\d+)/$',SupplierDelete,name="delete"),
)
