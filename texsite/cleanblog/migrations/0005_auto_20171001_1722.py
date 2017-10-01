# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks


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
            field=wagtail.wagtailcore.fields.StreamField((('intro', wagtail.wagtailcore.blocks.StructBlock((('keyvisual', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('slogan', wagtail.wagtailcore.blocks.CharBlock(required=True))), template='texsitecleanblog/blocks/intro.html')),)),
        ),
        migrations.AlterField(
            model_name='cleanblogarticlepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('intro', wagtail.wagtailcore.blocks.StructBlock((('keyvisual', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('slogan', wagtail.wagtailcore.blocks.CharBlock(required=True))), template='texsitecleanblog/blocks/intro.html')), ('heading', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('subtitle', wagtail.wagtailcore.blocks.CharBlock(required=False))), template='texsitecleanblog/blocks/heading.html')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.wagtailcore.blocks.CharBlock(required=False))), template='texsitecleanblog/blocks/image.html')), ('quote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('originator', wagtail.wagtailcore.blocks.CharBlock(required=False))), template='texsitecleanblog/blocks/quote.html')))),
        ),
    ]
