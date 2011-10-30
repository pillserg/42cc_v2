from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from contacts.models import UserDetail
from contacts.forms import UserDetailForm


def show_main_page(request):
    user_detail = UserDetail.objects.get_first_or_none()
    assert user_detail
    return render(request, 'index.html', {'user_detail': user_detail})


@login_required
def edit_contacts(request, template_name='edit-contacts.html'):
    if request.is_ajax():
        template_name = 'ajax-edit-contacts.html'

    user_detail = UserDetail.objects.get_first_or_none()
    form = UserDetailForm(request.POST or None, instance=user_detail)

    if form.is_valid():
        form.save()

    return render(request, template_name, locals())
