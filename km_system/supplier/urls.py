from django.conf.urls import patterns,url

from views import *

urlpatterns=patterns('',
	url(r'^$',SupplierList,name="supplier_list"),
	url(r'^detail/(?P<pk>\d+)/$',SupplierDetail,name='supplier_detail'),
	url(r'^delete/(?P<pk>\d+)/$',SupplierDelete,name='supplier_delete'),
#	url(r'^$',SupplierListView.as_view(),name='list'),
#	url(r'^detail/(?P<pk>\d+)/$',SupplierDetailView.as_view(),name="detail"),
#	url(r'^delete/(?P<pk>\d+)/$',SupplierDelete,name="delete"),
)
