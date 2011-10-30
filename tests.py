from django.conf import settings
from django.core.urlresolvers import reverse

from tddspry.django import HttpTestCase, DatabaseTestCase


class TestSettingsContextProcessor(HttpTestCase):
    def test_settings_attributes_are_present_on_main_page(self):
        self.go(reverse('main-page'))
        self.find(settings.TIME_ZONE)
