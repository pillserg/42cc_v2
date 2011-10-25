from django.http import HttpResponse
from django.shortcuts import render


def show_main_page(request):
    return HttpResponse('OK 200')
