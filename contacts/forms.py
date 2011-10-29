from django import forms

from models import UserDetail


class UserDetailForm(forms.ModelForm):
    """ModelForm for editing user details"""
    class Meta:
        model = UserDetail

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields.keyOrder = [
            'name',
            'email',
            'last_name',
            'jabber',
            'birthdate',
            'skype',
            'bio',
            'other_contacts',
            ]
