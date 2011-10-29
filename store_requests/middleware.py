from django.core.urlresolvers import reverse
from django.conf import settings

from models import StoredRequest


class SaveEveryIncomingRequestToDB(object):
    def process_request(self, request):
        def _include():
            """checks if current request really must be added to DB"""
            if request.path == reverse('last-requests'):
                return False
            if request.path.startswith(settings.STATIC_URL):
                return False
            return True

        if _include():
            parsed_request = StoredRequest.parse_request(request)
            StoredRequest.objects.create(**parsed_request)
