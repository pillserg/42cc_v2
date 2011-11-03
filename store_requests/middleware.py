from django.conf import settings

from models import StoredRequest


def should_be_logged(request):
    """
    Chose what urls should not be logged
    """
    exclude = ('/last-requests/', '/admin/', settings.STATIC_URL)

    if any(request.path.startswith(p) for p in exclude):
        return False
    return True


class SaveEveryIncomingRequestToDB(object):
    def process_request(self, request):
        if should_be_logged(request):
            parsed_request = StoredRequest.parse_request(request)
            StoredRequest.objects.create(**parsed_request)
