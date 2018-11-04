# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.fields
import wagtail.core.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('texsitecleanblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleanblogarticlepage',
            name='body',
            field=wagtail.core.fields.StreamField([(b'intro', wagtail.core.blocks.StructBlock([(b'keyvisual', wagtail.images.blocks.ImageChooserBlock(required=False)), (b'slogan', wagtail.core.blocks.CharBlock(required=True))])), (b'heading', wagtail.core.blocks.StructBlock([(b'title', wagtail.core.blocks.CharBlock(required=True)), (b'subtitle', wagtail.core.blocks.CharBlock(required=False))], template=b'texsitecleanblog/blocks/heading.html')), (b'paragraph', wagtail.core.blocks.RichTextBlock()), (b'image', wagtail.images.blocks.ImageChooserBlock(template=b'texsitecleanblog/blocks/image.html')), (b'quote', wagtail.core.blocks.StructBlock([(b'quote', wagtail.core.blocks.TextBlock(required=True)), (b'originator', wagtail.core.blocks.CharBlock(required=False))], template=b'texsitecleanblog/blocks/quote.html'))]),
        ),
    ]
