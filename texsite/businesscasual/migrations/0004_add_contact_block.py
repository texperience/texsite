# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.fields
import wagtail.core.blocks
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('texsitebusinesscasual', '0003_add_people_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesscasualpage',
            name='body',
            field=wagtail.core.fields.StreamField((('content', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('paragraph', wagtail.core.blocks.RichTextBlock(required=True))))), ('documents', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=True)), ('paragraph', wagtail.core.blocks.RichTextBlock(required=False)), ('files', wagtail.core.blocks.ListBlock(wagtail.documents.blocks.DocumentChooserBlock(), template='texsitebusinesscasual/blocks/documentlist.html'))))), ('people', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=True)), ('paragraph', wagtail.core.blocks.RichTextBlock(required=False)), ('people', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('name', wagtail.core.blocks.CharBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('position', wagtail.core.blocks.CharBlock(required=False)))), template='texsitebusinesscasual/blocks/peoplelist.html'))))), ('contact', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=True)), ('map', wagtail.core.blocks.CharBlock(required=False)), ('name', wagtail.core.blocks.CharBlock(required=True)), ('phone', wagtail.core.blocks.CharBlock(required=False)), ('mail', wagtail.core.blocks.EmailBlock(required=False)), ('bank', wagtail.core.blocks.CharBlock(required=False))))))),
        ),
    ]
