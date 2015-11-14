# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore.models import Page


class BasePage(Page):
    """Abstract base page for all texsite pages"""
    is_creatable = False

    class Meta:
        verbose_name = _('Base Page') + ' (' + __package__ + ')'
