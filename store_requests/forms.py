from django import forms

from models import StoredRequest


class PriorityChangeForm(forms.Form):
    """Simple form for changing StoredRequests prioriy"""
    priority = forms.IntegerField()
    for_all_by_ip = forms.BooleanField(required=False)
    _and = forms.BooleanField(required=False)
    for_all_by_path = forms.BooleanField(required=False)

    def __init__(self, id, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        req = StoredRequest.objects.get_or_none(pk=id)
        if not req:
            raise forms.ValidationError('wrong id')
        self.request = req
        self.id = id
        self.fields['priority'].initial = req.priority


    def save(self):
        self.request.priority = self.cleaned_data['priority']
        self.request.save()
        if self.cleaned_data['for_all_by_ip']:
            qs = StoredRequest.objects.filter(remote_ip=self.request.remote_ip)
            qs.update(priority=self.cleaned_data['priority'])
        if self.cleaned_data['for_all_by_path']:
            qs = StoredRequest.objects.filter(path=self.request.path)
            qs.update(priority=self.cleaned_data['priority'])

