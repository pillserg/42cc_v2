from django.conf.urls.defaults import patterns, include, url

from views import show_main_page

urlpatterns = patterns('',
     url(r'^$', show_main_page, name='main_page'),
                       )
