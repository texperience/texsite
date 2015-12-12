# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks

import json


def convert_to_imageblock(apps, schema_editor):
    CleanBlogArticlePage = apps.get_model("texsitecleanblog", "CleanBlogArticlePage")

    for page in CleanBlogArticlePage.objects.all():
        new_stream_data = []

        for block in page.body.stream_data:
            if block["type"] == "image":
                extendedimage = {
                    "type": "extendedimage",
                    "value": {
                        "image": block["value"]
                    }
                }
                new_stream_data.append(extendedimage)
            else:
                new_stream_data.append(block)

        page.body = json.dumps(new_stream_data)
        page.save()


def rename_imageblock(apps, schema_editor):
    CleanBlogArticlePage = apps.get_model("texsitecleanblog", "CleanBlogArticlePage")

    for page in CleanBlogArticlePage.objects.all():
        new_stream_data = []

        for block in page.body.stream_data:
            if block["type"] == "extendedimage":
                block["type"] = "image"

            new_stream_data.append(block)

        page.body = json.dumps(new_stream_data)
        page.save()


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('texsitecleanblog', '0002_add_quote_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleanblogarticlepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'intro', wagtail.wagtailcore.blocks.StructBlock([(b'keyvisual', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'slogan', wagtail.wagtailcore.blocks.CharBlock(required=True))])), (b'heading', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'subtitle', wagtail.wagtailcore.blocks.CharBlock(required=False))], template=b'texsitecleanblog/blocks/heading.html')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(template=b'texsitecleanblog/blocks/image.html')), (b'extendedimage', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), (b'caption', wagtail.wagtailcore.blocks.CharBlock(required=False))], template=b'texsitecleanblog/blocks/image.html')), (b'quote', wagtail.wagtailcore.blocks.StructBlock([(b'quote', wagtail.wagtailcore.blocks.TextBlock(required=True)), (b'originator', wagtail.wagtailcore.blocks.CharBlock(required=False))], template=b'texsitecleanblog/blocks/quote.html'))]),
        ),
        migrations.RunPython(
            convert_to_imageblock,
            noop,
        ),
        migrations.AlterField(
            model_name='cleanblogarticlepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'intro', wagtail.wagtailcore.blocks.StructBlock([(b'keyvisual', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'slogan', wagtail.wagtailcore.blocks.CharBlock(required=True))])), (b'heading', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'subtitle', wagtail.wagtailcore.blocks.CharBlock(required=False))], template=b'texsitecleanblog/blocks/heading.html')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), (b'caption', wagtail.wagtailcore.blocks.CharBlock(required=False))], template=b'texsitecleanblog/blocks/image.html')), (b'extendedimage', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), (b'caption', wagtail.wagtailcore.blocks.CharBlock(required=False))], template=b'texsitecleanblog/blocks/image.html')), (b'quote', wagtail.wagtailcore.blocks.StructBlock([(b'quote', wagtail.wagtailcore.blocks.TextBlock(required=True)), (b'originator', wagtail.wagtailcore.blocks.CharBlock(required=False))], template=b'texsitecleanblog/blocks/quote.html'))]),
        ),
        migrations.RunPython(
            rename_imageblock,
            noop,
        ),
        migrations.AlterField(
            model_name='cleanblogarticlepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'intro', wagtail.wagtailcore.blocks.StructBlock([(b'keyvisual', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'slogan', wagtail.wagtailcore.blocks.CharBlock(required=True))])), (b'heading', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'subtitle', wagtail.wagtailcore.blocks.CharBlock(required=False))], template=b'texsitecleanblog/blocks/heading.html')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), (b'caption', wagtail.wagtailcore.blocks.CharBlock(required=False))], template=b'texsitecleanblog/blocks/image.html')), (b'quote', wagtail.wagtailcore.blocks.StructBlock([(b'quote', wagtail.wagtailcore.blocks.TextBlock(required=True)), (b'originator', wagtail.wagtailcore.blocks.CharBlock(required=False))], template=b'texsitecleanblog/blocks/quote.html'))]),
        ),
    ]
