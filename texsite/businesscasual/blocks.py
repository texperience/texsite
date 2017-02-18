# -*- coding: utf-8 -*-

from wagtail.wagtailcore.blocks import CharBlock, ListBlock, RichTextBlock, StructBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock


class ContentBlock(StructBlock):
    heading = CharBlock(required=True)
    image = ImageChooserBlock(required=False)
    paragraph = RichTextBlock(required=True)

    class Meta:
        icon = 'placeholder'
        template = 'texsitebusinesscasual/blocks/content.html'


class DocumentsBlock(StructBlock):
    heading = CharBlock(required=True)
    paragraph = RichTextBlock(required=False)
    files = ListBlock(DocumentChooserBlock(), template="texsitebusinesscasual/blocks/documentlist.html")

    class Meta:
        icon = 'doc-full'
        template = 'texsitebusinesscasual/blocks/documents.html'
