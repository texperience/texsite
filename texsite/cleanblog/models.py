# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.blocks import RichTextBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock

from texsite.core.models import BasePage
from texsite.core.blocks import HeadingBlock, IntroBlock


class CleanBlogArticlePage(BasePage):
    """Clean blog article page"""
    # Page model fields
    body = StreamField([
        ('intro', IntroBlock()),
        ('heading', HeadingBlock(template="texsitecleanblog/blocks/heading.html")),
        ('paragraph', RichTextBlock()),
        ('image', ImageChooserBlock(template="texsitecleanblog/blocks/image.html")),
    ])

    # Editor interface configuration
    content_panels = BasePage.content_panels + [
        StreamFieldPanel('body'),
    ]

    class Meta:
        verbose_name = _('Clean Blog Article Page') + ' (' + __package__ + ')'
