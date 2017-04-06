# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 12:49
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20170313_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='infos_de',
            field=wagtail.wagtailcore.fields.StreamField((('info', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('photo', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('summary', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), ('action', wagtail.wagtailcore.blocks.CharBlock()), ('url', wagtail.wagtailcore.blocks.URLBlock())))),), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='infos_fr',
            field=wagtail.wagtailcore.fields.StreamField((('info', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('photo', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('summary', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), ('action', wagtail.wagtailcore.blocks.CharBlock()), ('url', wagtail.wagtailcore.blocks.URLBlock())))),), blank=True, null=True),
        ),
    ]