# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.fields
import wagtail.core.blocks
import wagtail.images.blocks

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
            field=wagtail.core.fields.StreamField([(b'intro', wagtail.core.blocks.StructBlock([(b'keyvisual', wagtail.images.blocks.ImageChooserBlock(required=False)), (b'slogan', wagtail.core.blocks.CharBlock(required=True))])), (b'heading', wagtail.core.blocks.StructBlock([(b'title', wagtail.core.blocks.CharBlock(required=True)), (b'subtitle', wagtail.core.blocks.CharBlock(required=False))], template=b'texsitecleanblog/blocks/heading.html')), (b'paragraph', wagtail.core.blocks.RichTextBlock()), (b'image', wagtail.images.blocks.ImageChooserBlock(template=b'texsitecleanblog/blocks/image.html')), (b'extendedimage', wagtail.core.blocks.StructBlock([(b'image', wagtail.images.blocks.ImageChooserBlock(required=True)), (b'caption', wagtail.core.blocks.CharBlock(required=False))], template=b'texsitecleanblog/blocks/image.html')), (b'quote', wagtail.core.blocks.StructBlock([(b'quote', wagtail.core.blocks.TextBlock(required=True)), (b'originator', wagtail.core.blocks.CharBlock(required=False))], template=b'texsitecleanblog/blocks/quote.html'))]),
        ),
        migrations.RunPython(
            convert_to_imageblock,
            noop,
        ),
        migrations.AlterField(
            model_name='cleanblogarticlepage',
            name='body',
            field=wagtail.core.fields.StreamField([(b'intro', wagtail.core.blocks.StructBlock([(b'keyvisual', wagtail.images.blocks.ImageChooserBlock(required=False)), (b'slogan', wagtail.core.blocks.CharBlock(required=True))])), (b'heading', wagtail.core.blocks.StructBlock([(b'title', wagtail.core.blocks.CharBlock(required=True)), (b'subtitle', wagtail.core.blocks.CharBlock(required=False))], template=b'texsitecleanblog/blocks/heading.html')), (b'paragraph', wagtail.core.blocks.RichTextBlock()), (b'image', wagtail.core.blocks.StructBlock([(b'image', wagtail.images.blocks.ImageChooserBlock(required=True)), (b'caption', wagtail.core.blocks.CharBlock(required=False))], template=b'texsitecleanblog/blocks/image.html')), (b'extendedimage', wagtail.core.blocks.StructBlock([(b'image', wagtail.images.blocks.ImageChooserBlock(required=True)), (b'caption', wagtail.core.blocks.CharBlock(required=False))], template=b'texsitecleanblog/blocks/image.html')), (b'quote', wagtail.core.blocks.StructBlock([(b'quote', wagtail.core.blocks.TextBlock(required=True)), (b'originator', wagtail.core.blocks.CharBlock(required=False))], template=b'texsitecleanblog/blocks/quote.html'))]),
        ),
        migrations.RunPython(
            rename_imageblock,
            noop,
        ),
        migrations.AlterField(
            model_name='cleanblogarticlepage',
            name='body',
            field=wagtail.core.fields.StreamField([(b'intro', wagtail.core.blocks.StructBlock([(b'keyvisual', wagtail.images.blocks.ImageChooserBlock(required=False)), (b'slogan', wagtail.core.blocks.CharBlock(required=True))])), (b'heading', wagtail.core.blocks.StructBlock([(b'title', wagtail.core.blocks.CharBlock(required=True)), (b'subtitle', wagtail.core.blocks.CharBlock(required=False))], template=b'texsitecleanblog/blocks/heading.html')), (b'paragraph', wagtail.core.blocks.RichTextBlock()), (b'image', wagtail.core.blocks.StructBlock([(b'image', wagtail.images.blocks.ImageChooserBlock(required=True)), (b'caption', wagtail.core.blocks.CharBlock(required=False))], template=b'texsitecleanblog/blocks/image.html')), (b'quote', wagtail.core.blocks.StructBlock([(b'quote', wagtail.core.blocks.TextBlock(required=True)), (b'originator', wagtail.core.blocks.CharBlock(required=False))], template=b'texsitecleanblog/blocks/quote.html'))]),
        ),
    ]
