# Create your views here.
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import simplejson

from models import StoredRequest
from forms import PriorityChangeForm


def show_request_info(request):
    return render(request, 'request-info.html')


def set_request_priority(request, id):
    form = PriorityChangeForm(id, request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        #return HttpResponseRedirect(reverse('last-requests'))
    return render(request, 'priority_form.html', {'form': form})


def get_ips(request):
    ips = StoredRequest.objects.values('remote_ip', 'priority').order_by().distinct()
    data = simplejson.dumps(list(ips))
    return HttpResponse(data, mimetype='application/json')

def get_paths(request):
    paths = StoredRequest.objects.values('path', 'priority').order_by().distinct()
    data = data = simplejson.dumps(list(paths))
    return HttpResponse(data, mimetype='application/json')
