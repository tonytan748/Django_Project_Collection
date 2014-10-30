from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'km_system.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^supplier/',include('supplier.urls',namespace='supplier')),
    url(r'^subcon/',include('subcon.urls',namespace='subcon')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^',include('login.urls')),
)
