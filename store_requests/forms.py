from django import forms

from models import StoredRequest


class PriorityChangeForm(forms.Form):
    """Simple form for changing StoredRequests prioriy"""
    priority = forms.IntegerField()
    for_all_by_ip = forms.BooleanField(required=False)
    bool_and = forms.BooleanField(required=False)
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
        if all((self.cleaned_data['for_all_by_ip'],
                self.cleaned_data['bool_and'],
                self.cleaned_data['for_all_by_path'],)):
            qs = StoredRequest.objects.filter(remote_ip=self.request.remote_ip,
                                              path=self.request.path)

        elif self.cleaned_data['for_all_by_ip']:
            qs = StoredRequest.objects.filter(remote_ip=self.request.remote_ip)

        elif self.cleaned_data['for_all_by_path']:
            qs = StoredRequest.objects.filter(path=self.request.path)

        else:
            self.request.priority = self.cleaned_data['priority']
            self.request.save()

            return

        qs.update(priority=self.cleaned_data['priority'])

