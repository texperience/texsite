# -*- coding: utf-8 -*-

from django.test import Client, TestCase


class TexsiteTestCase(TestCase):
    def setUp(self):
        self.client = Client()
