import datetime

from django.conf import settings
from django.core.urlresolvers import reverse

from tddspry.django import HttpTestCase, DatabaseTestCase
from tddspry import NoseTestCase

from contacts.models import UserDetail

ORIG_CONTACTS_DICT = dict(name=u'Sergey',
                     last_name=u'Pilyavskiy',
                     email=u'pill.sv0@gmail.com',
                     jabber=u'pillserg@jabber.com',
                     skype=u'pillserg',
                     other_contacts=(u'pill.sv0@gmail.com',
                                     'ICQ:289861503'),
                     bio=(u'Born in Kiev (1987)'
                          u'Graduated from NAU (2010)'
                          u'Currently looking for work.'),
                     birthdate=datetime.datetime(1987, 9, 3))


CONTACTS_DICT = dict(name=u'Sergey',
                     last_name=u'Pilyavskiy',
                     email=u'pill.sv0test@gmail.com',
                     jabber=u'pillsergtest@jabber.com',
                     skype=u'pillserg',
                     other_contacts=(u'pill.sv0@gmail.com',
                                     u'ICQ:289861503'),
                     bio=(u'Born in Kiev (1987)'
                          u'Graduated from NAU (2010)'
                          u'Currently looking for work.'),
                     birthdate=datetime.datetime(1987, 9, 3))


JD_CONTACTS_DICT = dict(name=u'John',
                        last_name=u'Dow',
                        email=u'someone0@gmail.com',
                        jabber=u'somejab@jabber.com',
                        skype=u'someskypeid',
                        other_contacts=u'blah2',
                        bio=u'Unknown\n',
                        birthdate=datetime.date(1987, 9, 3))


class TestUserDetailCRUD(DatabaseTestCase):
    """
    CRUD test for UserDetail model
    fields: name, last_name, email, jabber, skype,
            other_contacts, bio, birthdate
    """

    def create_test_user_detail(self):
        user_detail = UserDetail.objects.create(**CONTACTS_DICT)
        return user_detail

    def test_create(self):
        self.assert_create(UserDetail, **CONTACTS_DICT)

    def test_read(self):
        user_detail = self.create_test_user_detail()
        self.assert_read(UserDetail, pk=user_detail.pk)

    def test_update(self):
        user_detail = self.create_test_user_detail()
        self.assert_update(user_detail, **JD_CONTACTS_DICT)

    def test_delete(self):
        user_detail = self.create_test_user_detail()
        self.assert_delete(user_detail)


class TestContactsPage(HttpTestCase):
    """
    Contacts data must be present on main page
    """

    def test_ContactPage(self):
        self.go(reverse('main_page'))
        for value in ORIG_CONTACTS_DICT.values():
            if type(value) == type(''):
                value = value.replace('(', '\(').replace(')', '\)')
            elif type(value) == type(datetime.datetime.now()):
                value = value.strftime('%Y-%m-%d')
            else:
                continue
            self.find(value)
