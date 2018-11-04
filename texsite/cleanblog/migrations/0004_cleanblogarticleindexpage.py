# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.fields
import wagtail.core.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('texsitecore', '0001_initial'),
        ('texsitecleanblog', '0003_change_image_to_image_block'),
    ]

    operations = [
        migrations.CreateModel(
            name='CleanBlogArticleIndexPage',
            fields=[
                ('basepage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='texsitecore.BasePage')),
                ('body', wagtail.core.fields.StreamField([(b'intro', wagtail.core.blocks.StructBlock([(b'keyvisual', wagtail.images.blocks.ImageChooserBlock(required=False)), (b'slogan', wagtail.core.blocks.CharBlock(required=True))]))])),
            ],
            options={
                'verbose_name': 'Clean Blog Article Index Page (texsite.cleanblog)',
            },
            bases=('texsitecore.basepage',),
        ),
    ]
