from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'spreadsheet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^resources/(?P<path>.*)$','django.views.static.serve',{'document_root':setting.MEDIA_ROOT}),
    url(r'^spreadsheet_app/',views.index,name="index"),
)
