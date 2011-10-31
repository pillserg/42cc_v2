# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import simplejson

from models import StoredRequest

def show_request_info(request):
    return render(request, 'request-info.html')


def get_ips(request):
    ips = StoredRequest.objects.values('remote_ip', 'priority').order_by().distinct()
    data = simplejson.dumps(list(ips))
    return HttpResponse(data, mimetype='application/json')

def get_paths(request):
    paths = StoredRequest.objects.values('path', 'priority').order_by().distinct()
    data = data = simplejson.dumps(list(paths))
    return HttpResponse(data, mimetype='application/json')
