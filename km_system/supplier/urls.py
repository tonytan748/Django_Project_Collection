from django.conf.urls import patterns,url

#from supplier.views import SupplierList,SupplierDetail,SupplierDelete

from views import *

urlpatterns=patterns('',
	url(r'^$',SupplierList,name="list"),
	url(r'^detail/(?P<pk>\d+)/$',SupplierDetail,name='detail'),
	url(r'^delete/(?P<pk>\d+)/$',SupplierDelete,name='delete'),
	url(r'^add/$',SupplierAdd,name='add'),
	url(r'^search/$',SupplierSearch,name='search'),
)
