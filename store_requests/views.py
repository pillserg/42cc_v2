from django.shortcuts import render

from forms import PriorityChangeForm


def set_request_priority(request, id):
    form = PriorityChangeForm(id, request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    return render(request, 'priority_form.html', {'form': form})
