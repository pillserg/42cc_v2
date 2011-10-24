from django.conf import settings
from django.core.urlresolvers import reverse

from tddspry.django import HttpTestCase, DatabaseTestCase
from tddspry import NoseTestCase

from cc42_v2.contacts import UserDetail

CONTACTS_DICT = dict(name='Sergey',
                     last_name='Pilyavskiy',
                     email='pill.sv0@gmail.com',
                     jabber='pillserg@jabber.com',
                     skype='pillserg',
                     other_contacts=('pill.sv0@gmail.com',
                                     'ICQ:289861503'),
                     bio=('Born in Kiev (1987)',
                          'Graduated from NAU (2010)',
                          'Currently looking for work.'),
                     birthdate=datetime.datetime(1987, 9, 3))


JD_CONTACTS_DICT = dict(name='John',
                        last_name='Dow',
                        email='someone0@gmail.com',
                        jabber='somejab@jabber.com',
                        skype='someskypeid',
                        other_contacts=('blah\n',
                                        'blah2'),
                        bio=('Unknown\n'),
                        birthdate=datetime.datetime(1988, 9, 3))

class TestUserDetailCRUD(DatabaseTestCase):    
    """
    CRUD test for UserDetail model
    fields: name, last_name, email, jabber, skype,
            other_contacts, bio, birthdate
    """
    
    def create_test_user_detail(self):
        user_detail = UserDetail.create(**CONTACTS_DICT)
        return user_detail
    
    def test_create(self):
        self.assert_create(UserDetail, **CONTACTS_DICT)
    
    def test_read(self):
        user_detail = self.create_test_user_detail()
        self.assert_read(UserDetail, user_detail.pk)
    
    def test_update(self):
        user_detail = self.create_test_user_detail()
        self.assert_update(user_detail, **JD_CONTACTS_DICT)
    
    def test_delete(self):
        user_detail = self.create_test_user_detail()
        self.assert_delete(user_detail)
    
    

class TestContactsPage(HttpTestCase):
    
    def test_ContactPage(self):
        self.go200(reverse('main_page'))
        for value in CONTACTS_DICT.values():
            self.find(value)
        