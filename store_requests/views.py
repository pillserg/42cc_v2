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
    return render(request, 'priority_form.html', {'form': form})
