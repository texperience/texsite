# -*- coding: utf-8 -*-

from wagtail.wagtailcore.blocks import CharBlock, StructBlock, TextBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock


class HeadingBlock(StructBlock):
    title = CharBlock(required=True)
    subtitle = CharBlock(required=False)

    class Meta:
        icon = 'placeholder'


class ImageBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)

    class Meta:
        icon = 'image'


class IntroBlock(StructBlock):
    keyvisual = ImageChooserBlock(required=False)
    slogan = CharBlock(required=True)

    class Meta:
        icon = 'placeholder'


class QuoteBlock(StructBlock):
    quote = TextBlock(required=True)
    originator = CharBlock(required=False)

    class Meta:
        icon = 'openquote'
