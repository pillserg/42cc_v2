from django.conf.urls.defaults import patterns, include, url

from views import show_request_info

urlpatterns = patterns('',
     url(r'^$', show_request_info, name='request_info'),
                       )
