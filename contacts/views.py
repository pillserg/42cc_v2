from django.http import HttpResponse
from django.shortcuts import render

from contacts.models import UserDetail


def show_main_page(request):
    user_detail = UserDetail.objects.get_first_or_none()
    assert user_detail
    print user_detail
    return render(request, 'index.html', {'user_detail': user_detail})
