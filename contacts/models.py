from django.db import models
from django.utils.translation import ugettext as _


class CustomManager(models.Manager):
    """
    Adds get_or_none and get_firs_or_none method to objects,
    raises Exception if multiple objects returned
    """

    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None

    def get_first_or_none(self, **kwargs):
        qset = self.filter(**kwargs)

        try:
            return qset[0]
        except IndexError:
            return None


class UserDetail(models.Model):
    """
    Model representing basic persons contacts
    """

    name = models.CharField(max_length=30, verbose_name=_('first name'))
    last_name = models.CharField(max_length=100, verbose_name=_('last name'))
    birthdate = models.DateField(verbose_name=_('birthdate'))
    bio = models.TextField(verbose_name=_('biography'))

    email = models.EmailField(unique=True, verbose_name='email')
    jabber = models.EmailField(unique=True, verbose_name=_('jabber'),
                               blank=True, null=True)
    skype = models.CharField(max_length=30, verbose_name=_('skype id'),
                             blank=True, null=True)
    other_contacts = models.TextField(verbose_name=_('additional contacts'),
                                      blank=True, null=True)

    objects = CustomManager()

    def __unicode__(self):
        return ' '.join((self.name, self.last_name))
