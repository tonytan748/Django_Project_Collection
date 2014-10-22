from django.conf.urls import url,patterns

from views import *

urlpatterns=patterns('',
	url(r'^/$',mylogin),
	url(r'^/logout/$',mylogout),
)
