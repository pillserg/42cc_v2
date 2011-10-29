# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def show_request_info(request):
    return render(request, 'request-info.html')
