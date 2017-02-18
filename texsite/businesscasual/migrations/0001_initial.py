# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('texsitecore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessCasualPage',
            fields=[
                ('basepage_ptr', models.OneToOneField(to='texsitecore.BasePage', primary_key=True, parent_link=True, serialize=False, auto_created=True)),
                ('body', wagtail.wagtailcore.fields.StreamField((('content', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=True))))),))),
            ],
            options={
                'verbose_name': 'Business Casual Page (texsite.businesscasual)',
            },
            bases=('texsitecore.basepage',),
        ),
    ]
