# -*- coding: utf-8 -*-

from wagtail.wagtailcore.blocks import CharBlock, EmailBlock, ListBlock, RichTextBlock, StructBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock


class ContactBlock(StructBlock):
    heading = CharBlock(required=True)
    map = CharBlock(required=False)
    name = CharBlock(required=True)
    phone = CharBlock(required=False)
    mail = EmailBlock(required=False)
    bank = CharBlock(required=False)

    class Meta:
        icon = 'site'
        template = 'texsitebusinesscasual/blocks/contact.html'


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


class PersonBlock(StructBlock):
    name = CharBlock(required=True)
    image = ImageChooserBlock(required=True)
    position = CharBlock(required=False)


class PeopleBlock(StructBlock):
    heading = CharBlock(required=True)
    paragraph = RichTextBlock(required=False)
    people = ListBlock(PersonBlock(), template="texsitebusinesscasual/blocks/peoplelist.html")

    class Meta:
        icon = 'user'
        template = 'texsitebusinesscasual/blocks/people.html'
