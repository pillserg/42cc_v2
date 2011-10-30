from tddspry.django import HttpTestCase

from django.core.urlresolvers import reverse

from contacts.models import UserDetail


class TestObjToAdminLinkTag(HttpTestCase):
    def test_tag(self):
        self.go('/')
        self.login('admin', 'admin')
        pk = UserDetail.objects.get_first_or_none().pk
        self.follow200(reverse('admin:contacts_userdetail_change', args=(pk,)))
