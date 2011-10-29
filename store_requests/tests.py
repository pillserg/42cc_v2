import datetime

from django.conf import settings
from django.core.urlresolvers import reverse

from tddspry.django import HttpTestCase, DatabaseTestCase
from tddspry import NoseTestCase

from models import StoredRequest


REQUEST = dict(path='/',
               method='GET',
               is_ajax=False,
               is_secure=False,
               user_agent='Gecco',
               http_host='192.168.0.1',
               time=datetime.datetime.now(),
               language='ru',
               referer='',
               user=None,)


class TestStoredRequestCRUD(DatabaseTestCase):

    def create_test_request(self):
        stored_request = StoredRequest.objects.create(**REQUEST)
        return stored_request

    def test_create(self):
        self.assert_create(StoredRequest, **REQUEST)

    def test_read(self):
        stored_request = self.create_test_request()
        self.assert_read(StoredRequest, pk=stored_request.pk)

    def test_update(self):
        stored_request = self.create_test_request()
        self.assert_update(stored_request, **REQUEST)

    def test_delete(self):
        stored_request = self.create_test_request()
        self.assert_delete(stored_request)

