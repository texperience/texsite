# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('texsitecore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CleanBlogArticlePage',
            fields=[
                ('basepage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='texsitecore.BasePage')),
                ('body', wagtail.wagtailcore.fields.StreamField([(b'intro', wagtail.wagtailcore.blocks.StructBlock([(b'keyvisual', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'slogan', wagtail.wagtailcore.blocks.CharBlock(required=True))])), (b'heading', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'subtitle', wagtail.wagtailcore.blocks.CharBlock(required=False))], template=b'texsitecleanblog/blocks/heading.html')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(template=b'texsitecleanblog/blocks/image.html'))])),
            ],
            options={
                'verbose_name': 'Clean Blog Article Page (texsite.cleanblog)',
            },
            bases=('texsitecore.basepage',),
        ),
    ]
