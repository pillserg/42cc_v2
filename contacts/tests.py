import datetime
import copy

from django.core.urlresolvers import reverse
from django.test.client import Client

from tddspry.django import HttpTestCase, DatabaseTestCase, TestCase

from contacts.models import UserDetail
from contacts.forms import UserDetailForm

USERNAME = 'admin'
PASSWORD = 'admin'

ORIG_CONTACTS_DICT = dict(name=u'Sergey',
                     last_name=u'Pilyavskiy',
                     email=u'pill.sv0@gmail.com',
                     jabber=u'pillserg@jabber.com',
                     skype=u'pillserg',
                     other_contacts=(u'pill.sv0@gmail.com'
                                     u'ICQ:289861503'),
                     bio=(u'Born in Kiev (1987)'
                          u'Graduated from NAU (2010)'
                          u'Currently looking for work.'),
                     birthdate=u'1987-09-03')


CONTACTS_DICT = dict(name=u'Sergey',
                     last_name=u'Pilyavskiy',
                     email=u'pill.sv0test@gmail.com',
                     jabber=u'pillsergtest@jabber.com',
                     skype=u'pillserg',
                     other_contacts=(u'pill.sv0@gmail.com'
                                     u'ICQ:289861503'),
                     bio=(u'Born in Kiev (1987)'
                          u'Graduated from NAU (2010)'
                          u'Currently looking for work.'),
                     birthdate=u'1987-09-03')


JD_CONTACTS_DICT = dict(name=u'John',
                        last_name=u'Dow',
                        email=u'someone0@gmail.com',
                        jabber=u'somejab@jabber.com',
                        skype=u'someskypeid',
                        other_contacts=u'blah2',
                        bio=u'Unknown\n',
                        birthdate=u'1987-09-03')


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
        # ugly but I couldn't think of anything constructive right now
        local_dict = JD_CONTACTS_DICT
        local_dict['birthdate'] = datetime.date(1987, 9, 4)
        self.assert_update(user_detail, **local_dict)

    def test_delete(self):
        user_detail = self.create_test_user_detail()
        self.assert_delete(user_detail)


class TestContactsPage(HttpTestCase):
    """
    Contacts data must be present on main page
    """

    def test_contact_page(self):
        self.go(reverse('main-page'))
        for value in ORIG_CONTACTS_DICT.values():
            if type(value) == type(''):
                value = value.replace('(', '\(').replace(')', '\)')
            elif type(value) == type(datetime.datetime.now()):
                value = value.strftime('%Y-%m-%d')
            else:
                continue
            self.find(value)


class TestEditPage(TestCase):
    """
    login required
    contacts data must be editable
    """
    def test_edit_page_200(self):
        self.go200(reverse('edit-contacts'))

    def test_edit_form_initial(self):
        self.login(USERNAME, PASSWORD)
        self.go(reverse('edit-contacts'))
        for value in ORIG_CONTACTS_DICT.values():
            if type(value) == type(''):
                value = value.replace('(', '\(').replace(')', '\)')
            elif type(value) == type(datetime.datetime.now()):
                value = value.strftime('%Y-%m-%d')
            else:
                continue
            self.find(value)

    def test_data_is_editable_and_saved_to_db(self):
        self.login(USERNAME, PASSWORD)
        self.go(reverse('edit-contacts'))
        [self.fv('1', k, v) for k, v in JD_CONTACTS_DICT.items()]
        self.submit200()
        self.assert_read(UserDetail, **JD_CONTACTS_DICT)

    def test_login_required_to_access_edit_page(self):
        # Could not find how to get assertRedirects in tddspry
        # thus simple client test
        c = Client()
        response = c.get(reverse('edit-contacts'), follow=True)
        # hardcoded url - it's bad, i know
        self.assertRedirects(response, 'http://testserver/login/?next=/edit/')

    def test_errors(self):
        self.login(USERNAME, PASSWORD)
        self.go(reverse('edit-contacts'))
        self.fv('1', 'name', '')
        self.fv('1', 'birthdate', '19020')
        self.submit()
        self.find('This field is required')
        self.find('Enter a valid date.')

    def test_not_required_fields(self):
        self.login(USERNAME, PASSWORD)
        self.go(reverse('edit-contacts'))
        not_full_data_dict = copy.deepcopy(JD_CONTACTS_DICT)
        del not_full_data_dict['skype']
        del not_full_data_dict['jabber']
        [self.fv('1', k, v) for k, v in not_full_data_dict.items()]

    def test_ajax(self):
        # Just test presence of jquery.forms lib for now
        self.login(USERNAME, PASSWORD)
        self.go(reverse('edit-contacts'))
        self.find('js/jquery.form.js')

    def test_reversed_fields_page(self):
        self.login(USERNAME, PASSWORD)
        self.go(reverse('edit-contacts-reverse'))
        f = UserDetailForm()
        f.fields.keyOrder.reverse()
        fields = f.fields.keys()
        regexp = '.+'.join(['id="id_' + f + '"' for f in fields])
        self.find(regexp, flags="s")



