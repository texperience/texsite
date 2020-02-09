# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.images.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('texsitecore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessCasualPage',
            fields=[
                ('basepage_ptr', models.OneToOneField(to='texsitecore.BasePage', primary_key=True, parent_link=True, serialize=False, auto_created=True, on_delete=models.CASCADE)),
                ('body', wagtail.core.fields.StreamField((('content', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('paragraph', wagtail.core.blocks.RichTextBlock(required=True))))),))),
            ],
            options={
                'verbose_name': 'Business Casual Page (texsite.businesscasual)',
            },
            bases=('texsitecore.basepage',),
        ),
    ]
