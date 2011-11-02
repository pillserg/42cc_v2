from django.conf.urls.defaults import patterns, url

from models import StoredRequest


urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.list_detail.object_list',
        dict(queryset=StoredRequest.objects.all(),
             template_name='last_requests.html',
             paginate_by=10,),
        name='last-requests'),

    url(r'^priority$', 'django.views.generic.list_detail.object_list',
        dict(queryset=StoredRequest.objects.all().order_by('-priority'),
             template_name='last_requests.html',
             paginate_by=10,
             extra_context={'sort_by_priority': True}),
        name='last-requests-by-priority'),

    url(r'^set_priority/(\d+)$', 'store_requests.views.set_request_priority',
        name='set-request-priority'),

)
