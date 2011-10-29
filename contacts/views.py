from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from contacts.models import UserDetail


def show_main_page(request):
    user_detail = UserDetail.objects.get_first_or_none()
    assert user_detail
    return render(request, 'index.html', {'user_detail': user_detail})

@login_required
def edit_contacts(request):
    return render(request, 'base.html')
