from django.db import models
from django.utils.translation import ugettext as _

class UserDetail(models.Model):
    """
    Model representing basic persons contacts 
    """

    name = models.CharField(max_length=30, verbose_name=_('first name'))
    last_name = models.CharField(max_length=100, verbose_name=_('last name'))
    email = models.EmailField(unique=True, verbose_name='email')
    jabber = models.EmailField(unique=True, verbose_name=_('jabber'))
    skype = models.CharField(max_length=30, verbose_name=_('skype id'))
    other_contacts = models.TextField(verbose_name=_('additional contacts'))
    bio = models.TextField(verbose_name=_('biography'))
    birthdate = models.DateField(verbose_name=_('birthdate'))

    def __unicode__(self):
        return ' '.join((self.name, self.last_name))


