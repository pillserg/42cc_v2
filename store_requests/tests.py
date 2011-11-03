from django.core.urlresolvers import reverse
from django.test import Client
from django.core.handlers.wsgi import WSGIRequest

from tddspry.django import HttpTestCase, DatabaseTestCase

from models import StoredRequest


USERNAME = 'admin'
PASSWORD = 'admin'


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


class TestRealRequestsMustBeSaved(HttpTestCase):
    def test_200(self):
        self.go200(reverse('last-requests'))

    def test_twill_request_is_saved_to_db(self):
        self.assert_count(StoredRequest, 0)
        self.go(reverse('main-page'))
        self.assert_count(StoredRequest, 1)

    def test_last_requests_is_present_on_page(self, num_requests=10):
        url = reverse('main-page')
        for i in xrange(num_requests):
            self.go(url)
        self.assert_count(StoredRequest, num_requests)
        self.go(reverse('last-requests'))
        self.find('<div class="request">', count=num_requests)

    def test_priority_page(self):
        self.go200(reverse('last-requests-by-priority'))

    def test_upd_priority_form(self):
        self.go(reverse('main-page'))
        self.login_to_admin(USERNAME, PASSWORD)
        self.go(reverse('edit-contacts'))
        sr = StoredRequest.objects.get_first_or_none()
        self.go(reverse('set-request-priority', args=(sr.pk,)))
        self.fv('1', 'priority', '999')
        self.submit200()
        self.go(reverse('last-requests-by-priority'))
        self.find('999')

    def test_mass_upd_priority(self):
        self.go(reverse('main-page'))
        self.login_to_admin(USERNAME, PASSWORD)
        self.go(reverse('edit-contacts'))
        sr = StoredRequest.objects.get_first_or_none()
        self.go(reverse('set-request-priority', args=(sr.pk,)))
        self.fv('1', 'priority', '999')
        self.fv('1', 'for_all_by_ip', '1')
        self.submit200()
        self.go(self.go(reverse('last-requests-by-priority')))
        self.find('pr: 999', count=StoredRequest.objects.all().count())

    def test_requests_to_priority_modification_should_not_be_logged(self):
        num_requests = StoredRequest.objects.all().count()
        self.go(reverse('set-request-priority', args=(1,)))
        self.assert_count(StoredRequest, num_requests)


