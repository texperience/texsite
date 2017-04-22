# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtaildocs.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('texsitebusinesscasual', '0003_add_people_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesscasualpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('content', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=True))))), ('documents', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('files', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtaildocs.blocks.DocumentChooserBlock(), template='texsitebusinesscasual/blocks/documentlist.html'))))), ('people', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('people', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('name', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('position', wagtail.wagtailcore.blocks.CharBlock(required=False)))), template='texsitebusinesscasual/blocks/peoplelist.html'))))), ('contact', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('map', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('name', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('phone', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('mail', wagtail.wagtailcore.blocks.EmailBlock(required=False)), ('bank', wagtail.wagtailcore.blocks.CharBlock(required=False))))))),
        ),
    ]