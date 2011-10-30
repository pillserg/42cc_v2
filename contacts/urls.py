from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('contacts.views',
                       url(r'^$', 'show_main_page', name='main-page'),
                       url(r'^edit/$', 'edit_contacts', name='edit-contacts'),
                       url(r'^edit/reverse/$', 'edit_contacts',
                           {'reverse': True}, name='edit-contacts-reverse'),
                       )
