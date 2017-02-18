# -*- coding: utf-8 -*-

from wagtail.wagtailcore.blocks import CharBlock, RichTextBlock, StructBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock


class ContentBlock(StructBlock):
    heading = CharBlock(required=True)
    image = ImageChooserBlock(required=False)
    paragraph = RichTextBlock(required=True)

    class Meta:
        icon = 'placeholder'
        template = 'texsitebusinesscasual/blocks/content.html'
