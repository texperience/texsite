# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks
import wagtail.wagtaildocs.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('texsitebusinesscasual', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesscasualpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('content', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=True))))), ('documents', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('files', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtaildocs.blocks.DocumentChooserBlock(), template='texsitebusinesscasual/blocks/documentlist.html'))))))),
        ),
    ]
