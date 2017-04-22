# -*- coding: utf-8 -*-

from django.core.exceptions import ObjectDoesNotExist

from ..tests import TexsiteTestCase
from texsite.businesscasual.models import BusinessCasualPage


class BusinessCasualTestCase(TexsiteTestCase):
    def setUp(self):
        super(BusinessCasualTestCase, self).setUp()

        try:
            self.business_casual_page = BusinessCasualPage.objects.get(pk=2)
        except ObjectDoesNotExist:
            pass

        self.business_casual_page_response = self.client.get('/business-casual-page/')


class BusinessCasualPageTest(BusinessCasualTestCase):
    fixtures = ['site.json', 'businesscasual.json']

    def test_business_casual_with_minimal_content_rendered(self):
        self.assertInHTML('<div class="brand">Texsite site</div>', str(self.business_casual_page_response.content))
        self.assertInHTML('<div class="address-bar">Business Casual page</div>', str(self.business_casual_page_response.content))
