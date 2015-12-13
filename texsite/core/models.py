# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore.models import Page


class BasePage(Page):
    """Abstract base page for all texsite pages"""
    is_creatable = False

    @property
    def next_sibling(self):
        # Get next live sibling page by sort order
        return self.get_next_siblings().live().first()

    @property
    def previous_sibling(self):
        # Get previous live sibling page by sort order
        return self.get_prev_siblings().live().first()

    class Meta:
        verbose_name = _('Base Page') + ' (' + __package__ + ')'
