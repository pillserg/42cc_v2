from django.conf.urls.defaults import patterns, include, url

from views import show_request_info
from models import StoredRequest

urlpatterns = patterns('',
     url(r'^$', 'django.views.generic.list_detail.object_list',
         dict(queryset=StoredRequest.objects.all(),
              template_name='last_requests.html',
              paginate_by=10,),
         name='last-requests')
                       )

