from django.http import HttpResponse
from django.shortcuts import render

from contacts.models import UserDetail


def show_main_page(request):
    user_detail = UserDetail.get_
    return HttpResponse('OK 200')
