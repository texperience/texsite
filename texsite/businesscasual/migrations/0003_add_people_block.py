# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.images.blocks
import wagtail.core.fields
import wagtail.core.blocks
import wagtail.documents.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('texsitebusinesscasual', '0002_add_documents_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesscasualpage',
            name='body',
            field=wagtail.core.fields.StreamField((('content', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('paragraph', wagtail.core.blocks.RichTextBlock(required=True))))), ('documents', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=True)), ('paragraph', wagtail.core.blocks.RichTextBlock(required=False)), ('files', wagtail.core.blocks.ListBlock(wagtail.documents.blocks.DocumentChooserBlock(), template='texsitebusinesscasual/blocks/documentlist.html'))))), ('people', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=True)), ('paragraph', wagtail.core.blocks.RichTextBlock(required=False)), ('people', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('name', wagtail.core.blocks.CharBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('position', wagtail.core.blocks.CharBlock(required=False)))), template='texsitebusinesscasual/blocks/peoplelist.html'))))))),
        ),
    ]
