# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.fields
import wagtail.core.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('texsitecleanblog', '0004_cleanblogarticleindexpage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cleanblogarticleindexpage',
            options={'verbose_name': 'Clean Blog Artikel Übersicht (texsite.cleanblog)'},
        ),
        migrations.AlterModelOptions(
            name='cleanblogarticlepage',
            options={'verbose_name': 'Clean Blog Artikel Seite (texsite.cleanblog)'},
        ),
        migrations.AlterField(
            model_name='cleanblogarticleindexpage',
            name='body',
            field=wagtail.core.fields.StreamField((('intro', wagtail.core.blocks.StructBlock((('keyvisual', wagtail.images.blocks.ImageChooserBlock(required=False)), ('slogan', wagtail.core.blocks.CharBlock(required=True))), template='texsitecleanblog/blocks/intro.html')),)),
        ),
        migrations.AlterField(
            model_name='cleanblogarticlepage',
            name='body',
            field=wagtail.core.fields.StreamField((('intro', wagtail.core.blocks.StructBlock((('keyvisual', wagtail.images.blocks.ImageChooserBlock(required=False)), ('slogan', wagtail.core.blocks.CharBlock(required=True))), template='texsitecleanblog/blocks/intro.html')), ('heading', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=True)), ('subtitle', wagtail.core.blocks.CharBlock(required=False))), template='texsitecleanblog/blocks/heading.html')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False))), template='texsitecleanblog/blocks/image.html')), ('quote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock(required=True)), ('originator', wagtail.core.blocks.CharBlock(required=False))), template='texsitecleanblog/blocks/quote.html')))),
        ),
    ]
