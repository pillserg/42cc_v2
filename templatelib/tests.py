from tddspry.django import HttpTestCase
from contacts.models import UserDetail


class TestObjToAdminLinkTag(HttpTestCase):
    def test_tag(self):
        self.go('/')
        self.login_to_admin('admin', 'admin')
        pk = UserDetail.objects.get_first_or_none().pk
        self.follow200(reverse('admin:contacts_userdetail_change', args=(pk,)))
