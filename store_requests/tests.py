import datetime

from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import Client
from django.core.handlers.wsgi import WSGIRequest

from tddspry.django import HttpTestCase, DatabaseTestCase
from tddspry import NoseTestCase

from models import StoredRequest


class RequestFactory(Client):
    """
    Class that lets you create mock Request objects for use in testing.
    
    Usage:
    
    rf = RequestFactory()
    get_request = rf.get('/hello/')
    post_request = rf.post('/submit/', {'foo': 'bar'})
    
    This class re-uses the django.test.client.Client interface, docs here:
    http://www.djangoproject.com/documentation/testing/#the-test-client
    
    Once you have a request object you can pass it to any view function, 
    just as if that view had been hooked up using a URLconf.
    
    """
    def request(self, **request):
        """
        Similar to parent class, but returns the request object as soon as it
        has created it.
        """
        environ = {
            'HTTP_COOKIE': self.cookies,
            'PATH_INFO': '/',
            'QUERY_STRING': '',
            'REQUEST_METHOD': 'GET',
            'SCRIPT_NAME': '',
            'SERVER_NAME': 'testserver',
            'SERVER_PORT': 80,
            'SERVER_PROTOCOL': 'HTTP/1.1',
        }
        environ.update(self.defaults)
        environ.update(request)
        return WSGIRequest(environ)


class TestStoredRequestCRUD(DatabaseTestCase):

    def create_test_request(self, path="/request"):
        request = RequestFactory().get(path)
        return request

    def test_create(self):
        request = self.create_test_request()
        self.assert_create(StoredRequest,
                           **StoredRequest.parse_request(request))

    def test_read(self):
        request = self.create_test_request()
        parsed_request = StoredRequest.parse_request(request)
        stored_request = StoredRequest.objects.create(**parsed_request)
        self.assert_read(StoredRequest, pk=stored_request.pk)

    def test_update(self):
        request = self.create_test_request()
        parsed_request = StoredRequest.parse_request(request)
        stored_request = StoredRequest.objects.create(**parsed_request)

        upd_request = self.create_test_request('/someurl')
        parsed_request = StoredRequest.parse_request(upd_request)
        self.assert_update(stored_request, **parsed_request)

    def test_delete(self):
        request = self.create_test_request()
        parsed_request = StoredRequest.parse_request(request)
        stored_request = StoredRequest.objects.create(**parsed_request)
        self.assert_delete(stored_request)

