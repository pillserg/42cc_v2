from django import forms
from django.conf import settings

from models import UserDetail


class CalendarWidget(forms.TextInput):
    """date widget using datepicker from jQueryUI"""
    class Media:
        js = (settings.MEDIA_URL + "js/jquery.form.js",
              settings.MEDIA_URL + "js/csrftoken.js",
              settings.MEDIA_URL + "js/init_ajax_form.js",
              settings.MEDIA_URL + 'js/jquery-ui-1.8.16.custom.min.js',
        )
        css = {
            'all': (settings.MEDIA_URL +
                    "css/ui-lightness/jquery-ui-1.8.16.custom.css",)}

    def __init__(self, attrs={}):
        """init super widget"""
        super(CalendarWidget, self).__init__(
            attrs={'class': 'vDateField', 'size': '10'})


class UserDetailForm(forms.ModelForm):
    """ModelForm for editing user details"""
    class Meta:
        model = UserDetail
        widgets = {'birthdate': CalendarWidget()}

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
            'other_contacts', ]
