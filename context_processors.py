from django.conf import settings


def settings_context_processor(request):
     """adds settings var to RequestContext"""
     return {'settings':settings}
