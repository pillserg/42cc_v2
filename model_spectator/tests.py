
from django.contrib.contenttypes.models import ContentType

from tddspry.django import DatabaseTestCase
from model_spectator.models import ModelChange
from contacts.models import UserDetail

JD_CONTACTS_DICT = dict(name=u'John',
                        last_name=u'Dow',
                        email=u'someone0@gmail.com',
                        jabber=u'somejab@jabber.com',
                        skype=u'someskypeid',
                        other_contacts=u'blah2',
                        bio=u'Unknown\n',
                        birthdate=u'1987-09-03')

ud = UserDetail.objects.get_first_or_none()

model_change_test_obj = dict(
                            content_type=ContentType.objects.get_for_model(ud),
                            model_pk=ud.pk,
                            event=1
                            )

class TestModelChangeCRUD(DatabaseTestCase):

    def make_obj(self):
        return ModelChange.objects.create(**model_change_test_obj)

    def test_create(self):
        self.assert_create(ModelChange, **model_change_test_obj)

    def test_update(self):
        self.assert_update(self.make_obj(), event=2)

    def test_read(self):
        self.assert_read(ModelChange, pk=self.make_obj().pk)

    def test_delete(self):
        self.assert_delete(self.make_obj())

    def test_save_signal_is_saved(self):
        prev_num = ModelChange.objects.all().count()
        self.assert_create(UserDetail, **JD_CONTACTS_DICT)
        self.assert_count(ModelChange, prev_num + 1)
        model_change = ModelChange.objects.latest()
        self.assertEqual(1, model_change.event, 'event type is wrong')

    def test_update_signal_is_saved(self):
        prev_num = ModelChange.objects.all().count()
        ud = UserDetail.objects.get_first_or_none()
        self.assert_update(ud, name='somebody')
        self.assert_count(ModelChange, prev_num + 1)
        model_change = ModelChange.objects.latest()
        self.assertEqual(2, model_change.event, 'event type is wrong')

    def test_delete_signal_is_saved(self):
        prev_num = ModelChange.objects.all().count()
        ud = UserDetail.objects.get_first_or_none()
        self.assert_delete(ud)
        self.assert_count(ModelChange, prev_num + 1)
        model_change = ModelChange.objects.latest()
        self.assertEqual(3, model_change.event, 'event type is wrong')

