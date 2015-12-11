# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.blocks import RichTextBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock

from texsite.core.models import BasePage
from texsite.core.blocks import HeadingBlock, IntroBlock


class ArticlePage(BasePage):
    """Article page"""
    # Page model fields
    body = StreamField([
        ('intro', IntroBlock(template="texsitebootstrap/blocks/intro.html")),
        ('heading', HeadingBlock(template="texsitebootstrap/blocks/heading.html")),
        ('paragraph', RichTextBlock()),
        ('image', ImageChooserBlock(template="texsitebootstrap/blocks/image.html")),
    ])

    # Editor interface configuration
    content_panels = BasePage.content_panels + [
        StreamFieldPanel('body'),
    ]

    class Meta:
        verbose_name = _('Article Page') + ' (' + __package__ + ')'
