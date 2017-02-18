# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField

from texsite.core.models import BasePage

from .blocks import ContentBlock, DocumentsBlock


class BusinessCasualPage(BasePage):
    """Business Casual page"""
    # Page model fields
    body = StreamField([
        ('content', ContentBlock()),
        ('documents', DocumentsBlock())
    ])

    content_panels = BasePage.content_panels + [
        StreamFieldPanel('body'),
    ]

    class Meta:
        verbose_name = _('Business Casual Page') + ' (' + __package__ + ')'
