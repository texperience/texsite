# -*- coding: utf-8 -*-

from wagtail.wagtailcore.blocks import CharBlock, RichTextBlock, StreamBlock, StructBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock


class IntroBlock(StructBlock):
    keyvisual = ImageChooserBlock(required=False)
    slogan = CharBlock(required=True)

    class Meta:
        icon = 'placeholder'


class HeadingBlock(StructBlock):
    title = CharBlock(required=True)
    subtitle = CharBlock(required=False)

    class Meta:
        icon = 'placeholder'
